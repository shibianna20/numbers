
def numbers(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    if n>0 and n<100:
        for i in range(2, n):

            a[i] = a[i - 2] + a[i - 1]
        c=a[i]
        print(str(c)*c)

        for i in range(n - 2, 0, -1):

            d=c-a[i]
            print("x"*d+str(str(a[i])*a[i]),"\n" )
        e=0
        print("x"*(c-1)+str(e))

n =int(input("enter the input : "))
numbers(n)