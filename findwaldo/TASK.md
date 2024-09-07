                    Find Waldo
---------------------------------------------------
Return the coordinates ([row, col]) of the element
that differs from the rest.

Examples
--------

```
>>> whereIsWaldo([
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
])

output = [3, 2]  # B is different from the rest.
```

```
>>> whereIsWaldo([
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
])

output = [2, 4]  # D is different from the rest.
```

```
>>> whereIsWaldo([
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
])

output = [5, 1]  # P is different from the rest.
```

Notes
-----
The given array will always be a square or
rectangle. Rows and columns are 1-indexed (not
zero-indexed).