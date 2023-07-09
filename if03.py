def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b and a<=c:
        return a
    elif b>=a and b<=c:
        return b
    else:
        return c
print(main(4,8,6))    
    