"""write your code in following methods"""
file_path = './tasks.txt'

def to_do():
    def find(target):
        f = open(file_path)
        while True:
            line = f.readline()
            if len(line) == 0:
                break

            if (line.split(':'))[0] in target:
                print(line, end='')
        f.close()

    while True:
        firstIns = input().split()
        ins = []
        for token in firstIns:
            if token.endswith('"'):
                temList = [token]
                while not temList[-1].startswith('"'):
                    temList.append(ins.pop())
                token = ' '.join(reversed(temList))
            ins.append(token)

        if ins[1] == '-quit':
            break

        if ins[1] == '-a':
            f = open(file_path, 'a')
            for newplan in ins[2:]:
                f.write('todo:' + newplan.strip('"') + '\n')
            f.close()

        if ins[1] == '-d':
            f1 = open(file_path)
            todoList = f1.readlines()
            f2 = open(file_path, 'w')
            for line in todoList:
                planName = '"' + (line.split(':'))[1].strip() + '"'
                if planName not in ins[2:]:
                    f2.write(line)
            f1.close()
            f2.close()

        if ins[1] == '-c':
            f1 = open(file_path)
            todoList = f1.readlines()
            f2 = open(file_path, 'w')
            for line in todoList:
                tem = (line.split(':'))[1].strip()
                planName = '"' + tem + '"'
                if planName in ins[2:]:
                    f2.write('completed:' + tem + '\n')
                else:
                    f2.write(line)
            f1.close()
            f2.close()

        if ins[1] == '-f':
            find([ins[2]])

        if ins[1] == '-all':
            find(['todo', 'completed'])