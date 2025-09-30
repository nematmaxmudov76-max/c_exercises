#1
# meva=['olma','anjir',"o'rik",'uzum',"shaptoli"]
# print(meva)
#2
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)
#3
# mening_savatim=[]
# print(mening_savatim)
#4
# l=[1,2,3,4,5]
# print(l.extend(3))
#5 error
# l=[1,2,5,6]
# print(l.index[-1])

#6
# l=[23,45,12,345,434]
# print(l[0:3])
#7
# l=[1,2,3,4,5,6,7,8,9]
# l1=l[3:7]
# print(l1)
#8
# meva=['olma','anjir',"o'rik",'uzum',"shaptoli"]
# favour=input("sevimli meva:")
# if favour in meva:
    # print(f"{favour} meva mavjud")
# else: print("Mavjud emas!!")
#____________________________________________________________________________________________

#1
# l=["olma",'anjir']
# l.append("uzum")
# print(l)
#2
# l=["olma","uzum","shaptoli"]
# l.insert(1,"mango")
# print(l)
#3
# l=["olma","uzum","shaptoli"]
# l.insert(0,"kivi")
# print(l)
#4
# l=["olma","uzum","shaptoli"]
# l.pop(-1)
# print(l)
#5
# l=["olma","uzum","shaptoli"]
# l.remove("olma")
# print(l)
# #6
# l=["olma","uzum","shaptoli"]
# l.clear()
# print(l)
#7
# ism=["ahmat","mehroj","asad","nodir"]
# yosh=[18,17,19,20]
# print(ism+yosh)
#8
# l=[1,2,3,4]
# l1=l.copy()
# l1.append(5)
# print(l,l1)

# Ieratsiya va tsikllar:*

#1
# meva=['olma','anjir',"o'rik",'uzum',"shaptoli"]
# for meva in meva:
    # print(meva)

#2
# l=[1,2,3,4,5]
# while l in l:
    # print(l)

#3
# l=["a","d","r","a","y","a"]
# for i in l:
#     if i=='a':
#      print(("a harfi bor"))
#      break
# if i!="a":
#    print("a harfi berilmagan")

#4
# l=[1,3,4,8,6,10,2,15,18]
# for i in l:
#    if i%2==0:
#       print(f"juft sonlar:",i)
# if i%2 !=0:
#    print("juft sonlar mavjut emas")

#5
# l=[1,3,2,5,7,9,4,5]
# s=0
# for i in l:
#     s+=i
# print(s)

#6 error
# l=[3,5,2,15,6,8,9,1,10,]
# l.sort(reverse=True)
# l.index(0)
# print(l)

#7
# mevalar=["olma", "banan","uzum","mano","banan","anor","kiwi"]
# print(mevalar.count("banan"))

# 4 RO'XATNI TUSHUNISH

#1
# l1=[1,2,3,4,5,6,7,8,9,10]
# l3=l1.copy()
# l2=[]
# for l3 in range(1,11):
#     l2.append(l3**2)
# print(l2)

# l=["amma",'xola', 2,4,]
# for i in l:
#    print(i)

#2
l1=["ahmat","sher","uyishi","ishxona","niqob"]
l2=l1.copy()
l3=[]
flag=False
for i in l2:
   if len(l2)<=5:
      flag=True
      print(l2)
      break
if len(l2)>5:
   print("qolganlari 5 ta belgidan ortiqcha")

    
