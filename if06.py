def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    s=0
    if a<0:
        s+=1
    if b<0:
        s+=1
    if c<0:
        s+=1
    v=0
    if a>0:
        v+=1
    if b>0:
        v+=1
    if c>0:
        v+=1

    return s,v

print(main(5,6,-7))