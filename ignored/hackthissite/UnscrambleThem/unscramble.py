import time
#3 Approachs:
    #a. Naiva approach, check all the characters with first letter of word in ques, 
    #if match found, then consider checking whole of the characters in the word
def Naive(words, ques):
    startTime = time.time()
    arr = []
    for q in ques:
        c = q[0]
        for w in words:
            matchW = 0
            for j in w:
                if len(q)!=len(w):
                    break
                if c==j:
                    Q=q
                    match = 0
                    for wi in w:
                        check = 0
                        for qi in range(0, len(q), 1):
                            if wi==q[qi]:
                                q = q[:qi] + q[(qi+1):]
                                check = 1
                                break
                        if check==0:
                            match = 0
                            q=Q
                            break
                        else:
                            match = 1
                    if match==1:
                        matchW = 1
                        arr.append(w)
                        break
            if matchW==1:
                break
    f = open('./sol.txt', 'w')
    for sol in arr:
        sol = sol[:-1] + ',' + sol[-1:]
        f.write(sol)
    f.close()
    print('TIME OF EXECUTION : ', time.time() - startTime)

    #b. Upgradation of Naive Approach. Sort the words alphabetically and then match them
def OptimisedNaive(words, ques):
    startTime = time.time()
    arr = []
    W = words
    for i in range(0, len(ques), 1):
        sortedques = sorted(ques[i])
        for j in range(0, len(words), 1):
            sortedword = sorted(words[j])
            if (sortedques[0] == sortedword[0]):
                if(len(ques[i]) == len(words[j])):
                    match = 0
                    for k in range(0, len(ques[i]), 1):
                        if(sortedques[k]==sortedword[k]):
                            match = 1
                        else:
                            match = 0
                            break
                    if(match==1):
                        arr.append(j)
    f = open('./sol.txt', 'w')
    for index in arr:
        w = W[index]
        w = w[:-1] + ',' + w[-1:]
        f.write(w)
    f.close()

    print('TIME OF EXECUTION : ', time.time() - startTime)


    #c. Equalize all the 26 alphabets with a numeric code and each word equals the sum of the codes.
def CodicApproach(words, ques):
    startTime = time.time()

    print('TIME OF EXECUTION : ', time.time() - startTime)

def validate():
    #Word can contain only alphabets or digits
    #Run this fn once in case the wordlist.txt is updated
    f4 = open('./wordlist.txt', 'r')
    words = f4.readlines()
    f3 = open('./validated.txt', 'w')
    for w in words:
        validatedstr = ''
        for i in w:
            if ((i.isalpha()) == True) or ((i.isdigit()) == True):
                validatedstr += i
        if(validatedstr != ''):
            f3.write(validatedstr + '\n')
    f3.close()
        

if __name__ == "__main__":
    
    # validate()
    f1 = open('./validated.txt', 'r')
    words = f1.readlines()

    f2 = open('./ques.txt', 'r')
    ques = f2.readlines()

    CodicApproach(words, ques)

    


