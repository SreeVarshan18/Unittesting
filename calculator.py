def add2no(x, y):
    return x+y


def sub2no(x, y):
    return x-y


def mul2no(x, y):
    return x*y


def div2no(x, y):
    return x/y


if __name__ == "__main__":

    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    sum = add2no(a, b)
    print(sum)
    diff = sub2no(a, b)
    print(diff)
    prod = mul2no(a, b)
    print(prod)
    div = div2no(a, b)
    print(div)
