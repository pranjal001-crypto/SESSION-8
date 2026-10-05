# Session 08 - HW

**Student:** Pranjal Agrawal

## Topic
E-Commerce Discount Calculator

## Specification

- Negative cart total raises `ValueError`
- 0-50 gives 0% discount
- 51-100 gives 10% discount
- Above 100 gives 20% discount
- VIP adds 5%
- Maximum discount is 25%

## Bugs Tested

1. Boundary bug
2. Unreachable branch
3. Arithmetic bug

## Files

- `discount.py` - Fixed code
- `original_discount.py` - Original buggy code
- `test_discount.py` - 6 specification-based tests
- `test_results.txt` - Test results

## Testing

Run:

```bash
python HW/test_discount.py
