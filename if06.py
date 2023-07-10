def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    b=n//1000%10
    c=n//100%10
    d=n//10%10
    e=n%10
    if a>=b and a>=c and a>=d and a>=e:
        return 5
    elif b>=a and b>=c and b>=d and b>=c:
        return 4
    elif c>=a and c>=b and c>=d and c>=e:
        return 3
    elif d>=a and d>=b and d>=c and d>=e:
        return 2
    elif e>=a and e>=b and e>=c and e>=d:
        return 1
print(main(25789))    