def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if -100 < a < -9 or 9 < a < 100:
        if a % 2 == 1:
            return "two-digit odd number"
    if -100 < a < -9 or 9 < a < 100:
        if a % 2 == 0:
            return "two-digit even number"
    if -1000 < a < -99 or 99 < a < 1000:
        if a % 2 == 1:
            return "three-digit odd number"
    if -1000 < a < -99 or 99 < a < 1000:
        if a % 2 == 0:
            return "three-digit even number"


print(main(int(input())))
