#!/usr/bin/env python3
"""CAN+ engineering budget: order-of-magnitude checks for the fictional CAN+
home network (a CAN XL profile with gated cells and a protected spine).

Standard library only. Every assumption is a named constant so the numbers in
README.md can be reproduced and challenged.

    python3 studio/experiments/can-plus/budget.py
"""

# --- Assumptions -----------------------------------------------------------

CABLE_DELAY_NS_PER_M = 5.0      # twisted pair, velocity factor ~0.66
TRX_LOOP_DELAY_NS = 255.0       # TXD->bus->RXD loop delay, ISO 11898-2 worst case
SYNC_MARGIN_NS = 100.0          # oscillator tolerance and sampling margin
SAMPLE_POINT = 0.80             # nominal sample point in the arbitration phase

OHMS_PER_KM = {"18 AWG": 20.95, "20 AWG": 33.31, "22 AWG": 52.96}  # copper, 20 C
SUPPLY_V = 24.0
NODE_MIN_V = 18.0               # node input range assumed 18-30 V
CLASS2_VA_LIMIT = 100.0         # NEC Class 2 limit for a source <= 30 V

ARB_BITS_HEADER = 35            # approx. arbitration-phase bits before data phase
ARB_BITS_TRAILER = 12           # approx. arbitration-phase bits after data phase
XL_OVERHEAD_BYTES = 20          # approx. XL control, acceptance field, CRCs
STUFF_FACTOR = 1.10             # allowance for stuffing and phase switching


def max_bus_length_m(arb_bps):
    """Longest bus where a dominant bit makes the round trip before sampling."""
    bit_ns = 1e9 / arb_bps
    budget = SAMPLE_POINT * bit_ns - 2 * TRX_LOOP_DELAY_NS - SYNC_MARGIN_NS
    return max(0.0, budget / (2 * CABLE_DELAY_NS_PER_M))


def voltage_drop(gauge, one_way_m, load_w):
    current = load_w / SUPPLY_V
    resistance = OHMS_PER_KM[gauge] / 1000 * 2 * one_way_m   # out and back
    drop = current * resistance
    return current, drop, SUPPLY_V - drop


def frame_time_us(payload_bytes, arb_bps, data_bps):
    arb = (ARB_BITS_HEADER + ARB_BITS_TRAILER) / arb_bps
    data = (payload_bytes + XL_OVERHEAD_BYTES) * 8 * STUFF_FACTOR / data_bps
    return (arb + data) * 1e6


def main():
    print("1. Arbitration bit rate vs. maximum segment length (round-trip limit)")
    for bps in (1_000_000, 500_000, 250_000, 125_000):
        print(f"   {bps/1000:>6.0f} kbit/s  ->  {max_bus_length_m(bps):6.0f} m")

    print("\n2. Voltage drop on the 24 V pair (out-and-back resistance)")
    for gauge, length, load in (("18 AWG", 30, 15), ("22 AWG", 30, 15),
                                ("18 AWG", 60, 30), ("22 AWG", 60, 30)):
        i, drop, v_end = voltage_drop(gauge, length, load)
        ok = "ok" if v_end >= NODE_MIN_V else "BELOW NODE MINIMUM"
        print(f"   {gauge}, {length:>2} m run, {load:>2} W: {i:4.2f} A, "
              f"drop {drop:4.2f} V ({drop/SUPPLY_V*100:4.1f}%), end {v_end:5.2f} V  {ok}")
    print(f"   Class 2 ceiling at 24 V: {CLASS2_VA_LIMIT/SUPPLY_V:.2f} A per power source")

    print("\n3. Frame times (arbitration 500 kbit/s, XL data phase 5 Mbit/s)")
    for payload in (8, 64, 256, 2048):
        print(f"   {payload:>5}-byte payload: {frame_time_us(payload, 500e3, 5e6):7.0f} us")

    print("\n4. Worst-case gate latency for a life-safety frame (64 bytes)")
    own = frame_time_us(64, 500e3, 5e6)
    for cap in (2048, 256):
        blocking = frame_time_us(cap, 500e3, 5e6)
        per_hop = blocking + own          # wait out one maximal frame, then send
        print(f"   max frame {cap:>4} B: per hop {per_hop/1000:5.2f} ms, "
              f"cell->spine->cell (3 buses) {3*per_hop/1000:5.2f} ms")

    print("\n5. Stuck-dominant detection")
    max_legal_dominant_bits = 6 + 7     # 6-bit error flag plus overlapping flags
    threshold_bits = 4 * max_legal_dominant_bits
    for bps in (1_000_000, 500_000):
        t_us = threshold_bits / bps * 1e6
        print(f"   {bps/1000:>6.0f} kbit/s: dominant > {threshold_bits} bits "
              f"({t_us:5.0f} us) -> gate isolates cell")


if __name__ == "__main__":
    main()
