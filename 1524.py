for i in range(int(input())):
    q = input()
    q,w = map(int,input().split())
    s = list(map(int,input().split()))
    e = list(map(int,input().split()))
    if max(s) >= max(e):
        print("S")
    else:
        print("B")