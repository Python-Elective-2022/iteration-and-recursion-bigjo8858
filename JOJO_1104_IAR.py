def iterativePower(base, exp):
    SUM = 1
    for i in range(exp):
        SUM = SUM*base
    return SUM

def recursivePower(base, exp):
    if exp <= 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))



def main():
    print(iterativePower(5,3))
    print()
    print(recursivePower(5,3))


main()