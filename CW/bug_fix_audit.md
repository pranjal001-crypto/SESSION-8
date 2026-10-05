# Bug Fix Audit

| Bug | Original | Fix | Test |
|---|---|---|---|
| Arithmetic | `len(marks)-1` | `len(marks)` | Single mark |
| Boundary | `> 40` | `>= 40` | 40 test |
| Unreachable branch | 90 checked after 60 | 90 checked first | 90 test |

## Result

10 specification-based tests passed successfully.
