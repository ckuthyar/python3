questions=[]
answers=[]
responses=[]
marks=[]
f1=open("GK2.txt")
for i in range(0,9,1):
    s1=f1.readline().strip()
    list1=s1.split("$$")
    questions.append(list1[0])
    answers.append(list1[1].strip())
print(answers)
for i in range(0,9,1):
    print(questions[i])
    responses.append(input())

for i in range(0,9,1):
    if answers[i]==responses[i]:
        marks.append(10)
    else:
        marks.append(0)
for i in range(0,9,1):
    if(marks[i]==0):
        print(questions[i])
        print(answers[i])
print(marks)

