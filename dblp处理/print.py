with open('result.txt', 'r') as file:
    context = file.read()

data = eval(context)
single = sorted(data[1].items(),key=lambda x:x[1],reverse=True)
print("以下是文章最多的10位作者的姓名及发表文章数：")
for i in single[:10]:
    print(i)
double = sorted(data[2].items(),key=lambda x:x[1],reverse=True)
print("以下是两人为一组，合著文章最多的10组作者的姓名及发表文章数：")
for i in double[:10]:
    print(i)

