import os
import sys

commandendcreate = "mkdir pepnew"
os.system(commandendcreate)

m = int(sys.argv[1])
for i in range(m):
    i = i + 1
    commandlist = "for i in {1..+"+q + "};do  echo i; genewise  ./blastoutTemp1/"+str(i)+"_${i}  cdsmiddle/"+ str(i) + "_${i}_blastcds  -pep> pepnew/"+ str(i) + "_${i}.pep"
    os.system("printf '"+ commandlist + "' > glp"+ str(j)+".sh")
    os.system("nohup bash  glp"+ str(j)+".sh &")
    