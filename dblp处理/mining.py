from efficient_apriori import apriori
import json
# 设置数据集

data_new = []

count = len(open("dblp_parse_result.txt",'r').readlines())
# print(count)

with open('dblp_parse_result.txt', 'r') as f:
    for i, ann in enumerate(f.readlines()):
        if(i %10000 == 0):
            print("{}/{}".format(i,count))
        ann = ann.split('&&&')
        ann.pop()
        ann = tuple(ann)
        if ann:
            data_new.append(ann)

itemsets, rules = apriori(data_new, min_support=0.00005,  min_confidence=0.03)  #最小支持度，最小置信度

with open('result.txt', 'w') as file:
    file.write(str(itemsets))



print(itemsets)

with open('result.txt', 'r') as file:
    context = file.read()

data = eval(context)
single = sorted(data[1].items(),key=lambda x:x[1],reverse=False)
print("以下是文章最多的10位作者的姓名及发表文章数：")
print(single[:10]) 
double = sorted(data[2].items(),key=lambda x:x[1],reverse=False)
print("以下是两人为一组，合著文章最多的10组作者的姓名及发表文章数：")
print(double[:10]) 
