def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    return (a>0 and a+1) or (a<0 and a-2) or (a==0 and 0+10)
print(main(-44))