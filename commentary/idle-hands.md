# Idle Hands: a declaration and its implementation

## Title treatment

The author favored the Haskell signature as the display title, with the story's binary identifier directly below it.

```haskell
idleHands :: IO ()
```
`0b00000001`

*Idle Hands* is the spoken title. The eight-bit identifier continues the sequence established by *The Genesis Protocol* at `0b00000000`.

## Why Haskell

The signature describes an I/O action whose result is unit. It leaves the action's effects unspecified. A reader who looks it up can understand what the declaration promises and still wonder what the action will do.

One proposed ending reveals the implementation:

```haskell
idleHands = pure ()
```

This implementation produces unit without performing I/O. The space between the title and that possible ending mirrors the worker's experience: their abilities remain, while the role available to them gives those abilities no outlet. The ending is a device to try in drafting.

The spoken title carries the theological echo of the idle-hands proverb. It leaves the story room to ask who finds a use for those hands after employers stop paying for their work.

See the [story development notes](../canon/IDLE_HANDS_AND_SERIES_SLATE.md).
