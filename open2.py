import sys
import os
beopen  = sys.argv[1] #"do.fa"
thread = sys.argv[2]
inside = sys.argv[3]
os.system("mkdir blastoutTemp")

beout = "blastoutTemp"#"./do"
os.system("mkdir " + beout)
file = open(beopen,"r")
lists = open(beout+"/list","w")
lines = file.readlines()
dic={}
temp = ""
for i in lines:
    if i.startswith(">"):
        temp = i.strip()
        dic[temp] = ""
       # print(i[1:].replace("/","_"),file = lists)
    else:
        dic[temp] =  dic[temp] + i.strip()
#print(dic)
cu = 0
m = 1
cua = len(list(dic.keys()))
cutout = int(len(list(dic.keys()))/thread))
          
for i in list(dic.keys()):
    if cu >= cutout:
        q = cu
        m += 1
        cu = 0
    cu += 1

    out = open(beout+ "/" + str(m) + "_" +str(cu).replace("/","_"), "w")
    #print(i[:17],file = lists)
    print(i, file = out)
    print( dic[i], file = out)
    out.close()

          
lists.close()

for j in range(m):
    j = j + 1
    q = cu
    command1 = "mkdir  blastoutTemp/" + str(j) + "_pro"
    command2 = "mv  blastoutTemp/"+str(j) + "*" + " "+ str(j) + "_pro"

    os.system(command1)    
    os.system(command2)

command3 = "mkdir blastguide"  
command4 = "mkdir cdsmiddle"
os.system(command3)   
os.system(command4) 

for j in range(m):
    j = j + 1
    q = cu
    command5 = "for i in blastoutTemp/"+str(j)+"_pro/*; do  echo i; tblastn -query  blastoutTemp/"+str(j)+"_pro/${i}  -db w0 -outfmt 6 -evalue 0.00001 -max_target_seqs 1 > blastguide/"+ str(j) + "_${i}_blastgui; python hitac.py blastguide/"+ str(j) + "_${i}_blastgui cdsmiddle/"+ str(j) + "_${i}_blastcds " + ;  done"
    os.system("printf '"+ command5 + "' > bla"+ str(j)+".sh")
    command6 = "nohup bash bla"+ str(j)+".sh &"
    os.system(command6)

beout = "blastoutTemp1"#"./do"  
os.system("mkdir blastoutTemp1")    
for i in list(dic.keys()):
    if cu >= cutout:
        q = cu
        m += 1
        cu = 0
    cu += 1

    out = open(beout+ "/" + str(m) + "_" +str(cu).replace("/","_"), "w")
    #print(i[:17],file = lists)
    print(i, file = out)
    print( dic[i], file = out)
    out.close()    



    
          

        
        
        
        
        
        
        
        
        
        
