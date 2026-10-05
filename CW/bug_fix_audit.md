# Bug Fix Audit

| Bug | Fix | Test |
|---|---|---|
| Wrong average | Used `len(marks)` | Single mark test |
| 40 was not handled correctly | Used `>= 40` | Pass boundary |
| 90 got B instead of A | Checked 90 first | A grade test |
