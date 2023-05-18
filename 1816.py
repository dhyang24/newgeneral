for i in range(int(input())):
    s = int(input())
    st = True
    for i in range(2,1000000):
        if s%i == 0:
            st = False
            break
    print("YES"if st else "NO")