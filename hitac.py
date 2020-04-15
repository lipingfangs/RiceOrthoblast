from sequ import sequenceacq
import sys
#mp = open("x,")
gogo  = sys.argv[1]
gout = sys.argv[2]
inside = sys.argv[3]
file = open(gogo,"r")
lines = file.readlines()
lines = list(lines)
dic={}
temp = ""
for i in lines:
    i = i.split("	")
    i[0] = i[0] + "-" + i[1]
    
    if int(i[8]) > int(i[9]):
        k = i[8]
        i[8] = i[9]
        i[9] = k
        
    if temp != i[0]: 
        dic[i[0]] = [0,0]
        dic[i[0]][0] = i[8]
        dic[i[0]][1] = i[9]
        temp = i[0]
        camp = ""
        
    if temp == i[0]:
        if abs(int(i[8]) - int(dic[i[0]][0]))>20000:
            for j in i:
                print(j,end = ",")
            print()
            continue

            
        else:
            if int(i[8]) < int(dic[i[0]][0]):
                dic[i[0]][0] = i[8]
            if int(i[9]) > int(dic[i[0]][1]):
                dic[i[0]][1] = i[9]
print(dic)    
file.close()

nam = list(dic.keys())
k = open(gout,"w")

for i in nam:
    a = inside
    b = i.split("-")[1]
    m = i.split("-")[0]
    c = int(dic[i][0]) - 1000
    d = int(dic[i][1]) + 1000

    sequenceacq(a,b,c,d,m,k)
k.close()
