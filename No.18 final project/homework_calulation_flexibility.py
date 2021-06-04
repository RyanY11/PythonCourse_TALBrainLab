# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:48:33 2021

@author: bailu6
"""
###########根据题目总维度和水平生成全难度表单################
#输入控制题目难度的水平,两个维度为目标数字范围和蒙对概率范围
dimen = [[(5,10),(11,15),(16,20)],            
      [(0.03,0.06),(0.01,0.03)]]

#各个维度的各个水平自动组合出题目的难度序列组合成为题目的全难度序列
def dfs(data, cur_idx, res, tmp):             
    max_idx = len(data) - 1
    for i in range(len(data[cur_idx])):
        tmp.append(data[cur_idx][i])
        if cur_idx == max_idx:
            res.append([*tmp])
        else:
            dfs(data, cur_idx + 1, res, tmp)
        tmp.pop()
    return res
nandu = dfs(dimen, cur_idx=0, res=[], tmp=[])
#print(nandu)



############根据所在难度自动生成题目并开始游戏#################
import random  
from scipy.special import comb
import time
import numpy as np

def addduc(a,b):  #定义相加相减函数
    return a+b,a-b,b-a

coun=0
#aim_num=int(input('请出题者输入你的目标数字') or 10)  #或让目标数字随机：aim_numbr=random.randint(0,20)
n=int(input('请输入题目方格中供需填入的数字总数(不小于5)，不填默认为9') or 9)
#lowerbound,upperbound=input('请输入题目难度：瞎蒙蒙对的概率，也就是正确算式/算式总数的下限和上限（建议0.01-0.06之间），两数字用空格隔开').split()
participant=input('请输入你喜欢的昵称代表自己')
list_log=[] #定义空列表，其中元素为字典
log={} #定义字典,记录作答数据：{姓名：participant，是否作答正确：Isright，反应时：RT}

#################一次作答中所有玩家遍历全难度的题目###########
for level in range(len(nandu)):
    aim_num=random.randint(nandu[level][0][0],nandu[level][0][1])
    lowerbound,upperbound=nandu[level][1]
    cdt=True
    while cdt:
        list_a=random.sample(range(aim_num*2),n) #在[)的范围随机生成不重复的n个数字
        
        for i in range(n):
            list_temp=list_a[i+1:len(list_a)]
            for t in list_temp:
                if t+list_a[i]==aim_num or t-list_a[i]==aim_num or list_a[i]-t==aim_num:  #也可以换成新def的函数：if aim_num in addduc(t,list_a[i])
                    coun+=1
        chance_guess=coun/(comb(n,2)*3)
               
        if lowerbound<chance_guess<upperbound:
            cdt=False
            print('请在如下几个数字中找出两个数(每个数字只能用一次)，满足相加或相减等于',aim_num)
            print('可选数字如下：',list_a)
            t1=time.time()                  ###t1的记放在这里，每次输入错误格式都惩罚性的增加了玩家反应时
            
            ##这个while+except的循环使得程序更加宽容，每次玩家输入格式错误都会重来一次
            while True:
                try:
                    answer1,answer2=input('请输入你的答案，两个数字用空格隔开！').split()
                    answer1=int(answer1)
                    answer2=int(answer2)
                    break
                except:
                    print('未能按照要求输入数据，请重试')
               
            t2=time.time()
            RT=int((t2-t1)*1000)
            
            answer=addduc(answer1,answer2)
            if aim_num in answer and answer1 in list_a and answer2 in list_a and answer1!=answer2:
                print('回答正确，本次作答用时',RT,'毫秒')
                Iscorr=1
            else:
                print('回答错误，加油鸭！')
                Iscorr=0
            log['玩家昵称']=participant
            log['目标数字']=aim_num
            log['猜对概率']=[lowerbound,upperbound]
            log['当前题目实际猜对概率']=chance_guess
            log['难度水平']=level+1
            log['是否正确']=Iscorr
            log['反应时']=RT       
            coun=0
            list_log.append(log)
            log = {}
            #print(list_log)
        else:
            coun=0
            continue
            print(chance_guess)
            
            
###############################反馈：向玩家反馈正本次游戏中正确的次数以及反应时########################
corrs=[]
RTs=[]
for dics in list_log:
    corrs.append(dics['是否正确']) 
    RTs.append(dics['反应时'])
count_corrs=corrs.count(1)
average_RT=np.mean(RTs) #所有题目反应时
print(participant,'你已经完成6个难度所有题目')
print('你一共答对的题目数量为',count_corrs,'所有题目的平局反应时为',int(average_RT),'毫秒')
print('啦啦啦啦啦，Produced by 心路相遇作业组,感谢来玩！！！')  