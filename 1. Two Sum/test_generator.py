from collections import defaultdict
import random
number_cases=20
test_samples=number_cases%7

if __name__=='__main__':
    examples=[]
    answers=[]
    i=0
    while i < number_cases+1:
        example=[]
        sums=defaultdict(int)   
        for j in range(3+i,i*2+6):
            v=random.randrange(-i*i-10,i*i+10)
            example.append(v)
        n=len(example)
        for k in range(n):
            for l in range(k):
                s=example[k]+example[l]
                sums[s]+=1
        flag = False
        for k,v in sums.items():
            if v==1:
                answers.append(k)
                flag = True
                break
        if flag:
            examples.append(example)
            i+=1
    train_samples = number_cases-test_samples
    with open('train.txt','w') as f:
        for i in range(train_samples):
            s=' '.join([str(a) for a in examples[i]])
            s=str(answers[i])+' '+s+'\n'
            f.write(s)
    with open('test.txt','w') as f:
        for i in range(train_samples,number_cases):
            s=' '.join([str(a) for a in examples[i]])
            s=str(answers[i])+' '+s+'\n'
            f.write(s)

        