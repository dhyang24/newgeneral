for i in range(int(input())):
    q,w = map(str,input().split());q = int(q)
    for i in range(q):
        print(w*(i+1))
        w = chr((ord(w)+1-ord('A'))%26+ord('A'))
    print()