def special_typing():
    # your code here ^_^
    def func(substring, location):
        Length = len(substring)
        if targetLen <= location:
            return Length
        nextList = []
        for i in range(0, Length, 2):
            if substring[i] == target[location]:
                nextList.append(i)

        for head in nextList:
            judge = func(substring[head + 1:], location + 1)
            if judge != None:
                return judge

    num = int(input())
    for i in range(num):
        origin = input()
        target = input()
        targetLen = len(target)
        originLen = len(origin)
        if targetLen > originLen:
            print('NO')
            continue
        
        storeHead = 0
        while True:
            head = origin.find(target[0], storeHead)
            if head == -1:
                print('NO')
                break

            left = func(origin[head + 1:], 1)
            if left == None or left % 2 != 0:
                storeHead = head + 1
                continue

            print('YES')
            break
