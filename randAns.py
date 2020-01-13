import random
# language packs below can be updated
langPack = {'C':{'start': "准备好开始了吗？[Y/N]", 'end':'继续生成请调用randAns()','notyn': "请输入Y/N: ", 'no': "慢走:)\n需要我时请调用randAns()", 'yes': "请输入问题信息",  'Qn': '问题数：', 'Gn': '问题组数：', 'Cn':'选项数：', 'Fs': '满分：', 'int': "请输入整数！", 'N0int': "请输入非零整数！", 'collect': '需要分析输出吗？[Y/N]', 'group': "组别", 'getScores': "请在下方输入各组分数", 'ans': "输入", 'score': "输出", 'per': "百分比" }, \
'E':{'start': 'Would you like to start now?[Y/N]', 'end':'If you wish to play more, call randAns()', 'notyn': "please enter Y/N: ", 'no': "bye :)\ncall randAns() if you miss me", 'yes': "please enter info below", 'Qn': 'Question count: ', 'Gn': 'Question Group count: ', 'Cn': 'Choice count: ', 'Fs': 'Full score: ', 'int': 'Please input integers!', 'N0int': 'Please input non-zero integers!', 'collect':'Do you need output Analysis? [Y/N]', 'group': 'Group', 'getScores': 'Please enter outputs of each group below', 'ans': 'input', 'score': 'output', 'per': 'percentage'}}
def randAnswers(Qnum = 10, groupNum = 1, choiceNum = 5, fullScore = 100, lan=langPack['E'], collect  =True): 
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
    answers = [] #stores all the random answers
    for n in range(groupNum):
            #start a group
            print(lan['group']+' '+str(n+1)+': ')
            groupAns = [] #stores answers of this group
            for i in range(Qnum):
                    #forming random result
                    randInt = int(random.random()*choiceNum)+1
                    ans = (i+1, alphabets[randInt-1])
                    groupAns += [ans] 
                    print(str(ans[0])+': '+ans[1])
            answers += groupAns
            print()
    #getting the scores
    print(lan['getScores'])
    scores = [input(lan['group']+str(i+1)+lan["score"]+': ')for i in range(groupNum)]
    while not allInt(scores, False): 
        print(lan['int'])
        scores = [(i+1,input(lan['group']+str(i+1)+lan["score"]+': '))for i in range(groupNum)]
    #displaying answers & their matching scores
    print()
    print(lan['score'])
    for i in range(groupNum): 
            #printing scores
            print(lan['group']+': '+str(i+1)+": ")
            print(lan['ans']+": "+str(answers[(i)*Qnum:(i+1)*Qnum]))
            print(lan['score']+': '+str(scores[i]))
            if collect: 
                    print(lan['per']+': '+str(int(scores[i])/fullScore*100)+'%')
            if groupNum - n >1: print()
    print(lan['end'])

def chooseLang(choice): 
    if choice in langPack.keys():
        return langPack[choice]
    return langPack['E']

def yesorno(choice, lan):
    #returns boolean, if choice not valid, requests until valid
    if choice == 'Y': return True
    elif choice == 'N': return False
    while choice!='Y' and choice!='N':
        choice = input(lan['notyn'])
    return yesorno(choice, lan)

def nonZero(n): #given that n is a str that must be int
    return int(n)!=0
    
def isInt(c):
    return (c>='0' and c<='9')
    
def allInt(inputs, non0):
    for i in inputs:
        if i=="": return False
        for c in i:
            if not isInt(c): return False
        if non0 and not nonZero(i): return False
    return True
    
def randAns(): 
    print("欢迎来到答案随机生成器/Welcome to the random answer creator")
    lan = input("请选择语言/Please choose your language\n目前可选：中文(C)/英文(E)/Currently available: Chinese(C)/English(E): ")
    while lan not in langPack.keys():
        lan = input('请选择可用语言/Please choose available languages: ')
    lan = langPack[lan]
    start = yesorno(input(lan['start']), lan) # ask if user is ready to start
    if not start: print(lan['no'])
    else:
            print(lan['yes'])
            inputs = [input(lan['Qn']),input(lan['Gn']),input(lan['Cn']),input(lan['Fs'])] # taking info 
            while not allInt(inputs, True):
                print(lan['N0int'])
                inputs = [input(lan['Qn']),input(lan['Gn']),input(lan['Cn']),input(lan['Fs'])] # taking info until inputs are all int
            Qn,Gn,Cn,Fs = map(int,inputs)
            collect = yesorno(input(lan['collect']), lan) # ask if the user need data collection & analysis
            print()
            return randAnswers(Qn, Gn, Cn, Fs, lan, collect)
randAns()
