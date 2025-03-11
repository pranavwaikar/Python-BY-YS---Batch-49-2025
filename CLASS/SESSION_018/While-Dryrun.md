# Example 1

| Iteration | i Value (Before Condition Check) | Condition (i < N) | Output              | i Value (After Increment) |
| --------- | -------------------------------- | ----------------- | ------------------- | ------------------------- |
| 1st       | i = 1                            | 1 < 6 --> True    | 1                   | i = 2                     |
| 2nd       | i = 2                            | 2 < 6 --> True    | 2                   | i = 3                     |
| 3rd       | i = 3                            | 3 < 6 --> True    | 3                   | i = 4                     |
| 4th       | i = 4                            | 4 < 6 --> True    | 4                   | i = 5                     |
| 5th       | i = 5                            | 5 < 6 --> True    | 5                   | i = 6                     |
| -         | i = 6                            | 6 < 6 --> False   | (Stops)             | -                         |
| -         | (End)                            |                   | "End value of i: 6" | -                         |

# Example 2

| Iteration | i Value (Before Condition Check) | Condition (i <= N) | Output     | i Value (After Increment) |
| --------- | -------------------------------- | ------------------ | ---------- | ------------------------- |
| 1st       | i = 1                            | 1 <= 6 --> True    | 1          | i = 2                     |
| 2nd       | i = 2                            | 2 <= 6 --> True    | 2          | i = 3                     |
| 3rd       | i = 3                            | 3 <= 6 --> True    | 3          | i = 4                     |
| 4th       | i = 4                            | 4 <= 6 --> True    | 4          | i = 5                     |
| 5th       | i = 5                            | 5 <= 6 --> True    | 5          | i = 6                     |
| 6th       | i = 6                            | 6 <= 6 --> True    | 6          | i = 7                     |
| -         | i = 7                            | 7 <= 6 --> False   | (Stops)    | -                         |
| -         | (End)                            |                    | "EV(i): 7" | -                         |

# Example 3

| Iteration | i Value (Before Condition Check) | Condition (i < N) | Output     | i Value (After Increment) |
| --------- | -------------------------------- | ----------------- | ---------- | ------------------------- |
| 1st       | i = 0                            | 0 < 6 --> True    | 0          | i = 1                     |
| 2nd       | i = 1                            | 1 < 6 --> True    | 1          | i = 2                     |
| 3rd       | i = 2                            | 2 < 6 --> True    | 2          | i = 3                     |
| 4th       | i = 3                            | 3 < 6 --> True    | 3          | i = 4                     |
| 5th       | i = 4                            | 4 < 6 --> True    | 4          | i = 5                     |
| 6th       | i = 5                            | 5 < 6 --> True    | 5          | i = 6                     |
| -         | i = 6                            | 6 < 6 --> False   | (Stops)    | -                         |
| -         | (End)                            |                   | "EV(i): 6" | -                         |

# Example 4

| Iteration | i Value (Before Condition Check) | Condition (i <= N) | Output     | i Value (After Increment) |
| --------- | -------------------------------- | ------------------ | ---------- | ------------------------- |
| 1st       | i = 0                            | 0 <= 8 --> True    | 0          | i = 1                     |
| 2nd       | i = 1                            | 1 <= 8 --> True    | 1          | i = 2                     |
| 3rd       | i = 2                            | 2 <= 8 --> True    | 2          | i = 3                     |
| 4th       | i = 3                            | 3 <= 8 --> True    | 3          | i = 4                     |
| 5th       | i = 4                            | 4 <= 8 --> True    | 4          | i = 5                     |
| 6th       | i = 5                            | 5 <= 8 --> True    | 5          | i = 6                     |
| 7th       | i = 6                            | 6 <= 8 --> True    | 6          | i = 7                     |
| 8th       | i = 7                            | 7 <= 8 --> True    | 7          | i = 8                     |
| 9th       | i = 8                            | 8 <= 8 --> True    | 8          | i = 9                     |
| -         | i = 9                            | 9 <= 8 --> False   | (Stops)    | -                         |
| -         | (End)                            |                    | "EV(i): 9" | -                         |

# Example 5

| Iteration | i Value (Before Condition Check) | Condition (i > 0) | Output     | i Value (After Decrement) |
| --------- | -------------------------------- | ----------------- | ---------- | ------------------------- |
| 1st       | i = 4                            | 4 > 0 --> True    | 4          | i = 3                     |
| 2nd       | i = 3                            | 3 > 0 --> True    | 3          | i = 2                     |
| 3rd       | i = 2                            | 2 > 0 --> True    | 2          | i = 1                     |
| 4th       | i = 1                            | 1 > 0 --> True    | 1          | i = 0                     |
| -         | i = 0                            | 0 > 0 --> False   | (Stops)    | -                         |
| -         | (End)                            |                   | "EV(i): 0" | -                         |

# Example 6

| Iteration | i Value (Before Condition Check) | Condition (i >= 0) | Output      | i Value (After Decrement) |
| --------- | -------------------------------- | ------------------ | ----------- | ------------------------- |
| 1st       | i = 4                            | 4 >= 0 --> True    | 4           | i = 3                     |
| 2nd       | i = 3                            | 3 >= 0 --> True    | 3           | i = 2                     |
| 3rd       | i = 2                            | 2 >= 0 --> True    | 2           | i = 1                     |
| 4th       | i = 1                            | 1 >= 0 --> True    | 1           | i = 0                     |
| 5th       | i = 0                            | 0 >= 0 --> True    | 0           | i = -1                    |
| -         | i = -1                           | -1 >= 0 --> False  | (Stops)     | -                         |
| -         | (End)                            |                    | "EV(i): -1" | -                         |

# Example 7

| Iteration | i Value (Before Condition Check) | Condition (i > 0) | Output     | i Value (After Decrement) |
| --------- | -------------------------------- | ----------------- | ---------- | ------------------------- |
| 1st       | i = 4                            | 4 > 0 --> True    | 4          | i = 3                     |
| 2nd       | i = 3                            | 3 > 0 --> True    | 3          | i = 2                     |
| 3rd       | i = 2                            | 2 > 0 --> True    | 2          | i = 1                     |
| 4th       | i = 1                            | 1 > 0 --> True    | 1          | i = 0                     |
| -         | i = 0                            | 0 > 0 --> False   | (Stops)    | -                         |
| -         | (End)                            |                   | "EV(i): 0" | -                         |

# Example 8

| Iteration | i Value (Before Condition Check) | Condition (i >= 0) | Output      | i Value (After Decrement) |
| --------- | -------------------------------- | ------------------ | ----------- | ------------------------- |
| 1st       | i = 4                            | 4 >= 0 --> True    | 4           | i = 3                     |
| 2nd       | i = 3                            | 3 >= 0 --> True    | 3           | i = 2                     |
| 3rd       | i = 2                            | 2 >= 0 --> True    | 2           | i = 1                     |
| 4th       | i = 1                            | 1 >= 0 --> True    | 1           | i = 0                     |
| 5th       | i = 0                            | 0 >= 0 --> True    | 0           | i = -1                    |
| -         | i = -1                           | -1 >= 0 --> False  | (Stops)     | -                         |
| -         | (End)                            |                    | "EV(i): -1" | -                         |

# Example 9

| Iteration | i Value (Before Condition Check) | Condition (i < 100) | Output       | i Value (After Multiplication) |
| --------- | -------------------------------- | ------------------- | ------------ | ------------------------------ |
| 1st       | i = 1                            | 1 < 100 --> True    | 1            | i = 2                          |
| 2nd       | i = 2                            | 2 < 100 --> True    | 2            | i = 4                          |
| 3rd       | i = 4                            | 4 < 100 --> True    | 4            | i = 8                          |
| 4th       | i = 8                            | 8 < 100 --> True    | 8            | i = 16                         |
| 5th       | i = 16                           | 16 < 100 --> True   | 16           | i = 32                         |
| 6th       | i = 32                           | 32 < 100 --> True   | 32           | i = 64                         |
| 7th       | i = 64                           | 64 < 100 --> True   | 64           | i = 128                        |
| -         | i = 128                          | 128 < 100 --> False | (Stops)      | -                              |
| -         | (End)                            |                     | "EV(i): 128" | -                              |

# Example 10

| Iteration | i Value (Before Condition Check) | Condition (i > 0)        | Output              | i Value (After Division) |
| --------- | -------------------------------- | ------------------------ | ------------------- | ------------------------ |
| 1st       | i = 100                          | 100 > 0 --> True         | 100                 | i = 50.0                 |
| 2nd       | i = 50.0                         | 50.0 > 0 --> True        | 50.0                | i = 25.0                 |
| 3rd       | i = 25.0                         | 25.0 > 0 --> True        | 25.0                | i = 12.5                 |
| 4th       | i = 12.5                         | 12.5 > 0 --> True        | 12.5                | i = 6.25                 |
| 5th       | i = 6.25                         | 6.25 > 0 --> True        | 6.25                | i = 3.125                |
| 6th       | i = 3.125                        | 3.125 > 0 --> True       | 3.125               | i = 1.5625               |
| 7th       | i = 1.5625                       | 1.5625 > 0 --> True      | 1.5625              | i = 0.78125              |
| 8th       | i = 0.78125                      | 0.78125 > 0 --> True     | 0.78125             | i = 0.390625             |
| 9th       | i = 0.390625                     | 0.390625 > 0 --> True    | 0.390625            | i = 0.1953125            |
| 10th      | i = 0.1953125                    | 0.1953125 > 0 --> True   | 0.1953125           | i = 0.09765625           |
| -         | i = 0.09765625                   | 0.09765625 > 0 --> False | (Stops)             | -                        |
| -         | (End)                            |                          | "EV(i): 0.09765625" | -                        |

# Example 11

| Iteration | i Value (Before Condition Check) | Condition (i < 50) | Output | i Value (After Multiplication) |
| --------- | -------------------------------- | ------------------ | ------ | ------------------------------ |
| 1st       | i = 0                            | 0 < 50 --> True    | 0      | i = 0                          |
| -         | i = 0                            | 0 < 50 --> True    | 0      | i = 0                          |
| -         | Infinite loop (since i stays 0)  |                    |        |                                |

# Example 12

| Iteration | i Value (Before Condition Check) | Condition (i >= 0)        | Output              | i Value (After Division) |
| --------- | -------------------------------- | ------------------------- | ------------------- | ------------------------ |
| 1st       | i = 100                          | 100 >= 0 --> True         | 100                 | i = 50.0                 |
| 2nd       | i = 50.0                         | 50.0 >= 0 --> True        | 50.0                | i = 25.0                 |
| 3rd       | i = 25.0                         | 25.0 >= 0 --> True        | 25.0                | i = 12.5                 |
| 4th       | i = 12.5                         | 12.5 >= 0 --> True        | 12.5                | i = 6.25                 |
| 5th       | i = 6.25                         | 6.25 >= 0 --> True        | 6.25                | i = 3.125                |
| 6th       | i = 3.125                        | 3.125 >= 0 --> True       | 3.125               | i = 1.5625               |
| 7th       | i = 1.5625                       | 1.5625 >= 0 --> True      | 1.5625              | i = 0.78125              |
| 8th       | i = 0.78125                      | 0.78125 >= 0 --> True     | 0.78125             | i = 0.390625             |
| 9th       | i = 0.390625                     | 0.390625 >= 0 --> True    | 0.390625            | i = 0.1953125            |
| 10th      | i = 0.1953125                    | 0.1953125 >= 0 --> True   | 0.1953125           | i = 0.09765625           |
| -         | i = 0.09765625                   | 0.09765625 >= 0 --> False | (Stops)             | -                        |
| -         | (End)                            |                           | "EV(i): 0.09765625" | -                        |
