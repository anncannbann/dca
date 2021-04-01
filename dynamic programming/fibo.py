def fibo(n):
    if (n<2):
        return n
    return fibo(n-1) +fibo(n-2)
def main():
    print('fibonacci for 3 nos:',fibo(3))

main()