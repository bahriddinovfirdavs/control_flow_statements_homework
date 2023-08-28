def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.

    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    d = a % 10
    s = a // 10
    if -100 < a < -9 or 9 < a < 100:
        if d * 10 + s <= a:
            return True
    if -100 < a < -9 or 9 < a < 100:
        if d * 10 + s > a:
            return False


print(main(76))
