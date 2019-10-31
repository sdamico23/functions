def fn(n):
    ret = 0
    for i in range(0,n):
        i = 2*i + 1
        ret += (i*i)
    return ret
def main():
    n = int(input("Please enter n:"))
    print(fn(n))
main()
