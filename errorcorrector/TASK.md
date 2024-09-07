                  Error Corrector
---------------------------------------------------
Implement a error correction and/or detection
algorithm using method you'd like. If you create a
error correction algorithm, it should be able to
correct atleast a single bit error while still
returning the original data. Try not to use a built
in algorithm, rather implement yourself.

## Example (error correcting)
```
data = [1, 0, 1, 0]
corrupted = (flip a random bit in data)
decoded = [1, 0, 1, 0]
```

## Example (Error detecting)
```
data = [1, 0, 1, 0]
corrupted = (flip a random bit in data)
data = (ERROR DETECTED SOMEHOW)
```

Note: use some mathematical construct to detect
error, like parity or polynomial behaviour, etc.