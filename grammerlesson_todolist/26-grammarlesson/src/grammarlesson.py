def isPetyaLanguage():
    def checkSuffix(List, suffix):
        for token in List:
            if not token.endswith(suffix):
                return False
        return True

    tokens = input().strip()
    allSuffix = ['lios', 'liala', 'etr', 'etra', 'initis', 'inites']

    if ' ' not in tokens:
        for suffix in allSuffix:
            if tokens.endswith(suffix):
                print('YES')
                return
        print('NO')
        return

    tokens = tokens.split(' ')
    noneList = list(filter(lambda x: x.endswith('etr') or x.endswith('etra'), tokens))
    if len(noneList) != 1:
        print('NO')
        return
    noneList = noneList[0]
    indexOfNoun = tokens.index(noneList)

    if (noneList.endswith('etr') and checkSuffix(tokens[:indexOfNoun], 'lios') and checkSuffix(tokens[indexOfNoun+1:], 'initis')) or (noneList.endswith('etra') and checkSuffix(tokens[:indexOfNoun], 'liala') and checkSuffix(tokens[indexOfNoun+1:], 'inites')): 
            print('YES')
            return
    print('NO')
