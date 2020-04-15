def sequenceacq(a,b,c,d,m,k):
    def chromosome_select(num):
            dicrt = {}
            probest = ""
            chromosome = num
            #print(num)
            allreal = ""
            for line in range(len(allline)):
                if allline[line].startswith('>'):
                    probest = allline[line].split(" ")[0][1:]
                    dicrt[probest.strip()] = line
            dicrt_name = list(dicrt.keys())
            #print(dicrt_name)
            for i in range(len(dicrt_name)):
                if str(chromosome) == dicrt_name[i] and i < len(dicrt_name):
                    allreal = allline[int(dicrt[dicrt_name[i]]):int(dicrt[dicrt_name[i+1]])]
                    break
                if str(chromosome) == dicrt_name[i]:
                    allreal = allline[int(dicrt[dicrt_name[i]]):]
                    break
            #print(allreal)
            return allreal


    def seq_select(goin,endin,allreal,gggg):
        dic = ""
        dicr = {}
        goin = goin
        endin = endin
        golinenum = int(goin / (len(allline[1])-1))
        golocationnum = int(goin % (len(allline[1])-1))
        outlinenum = int(endin / (len(allline[1])-1)) 
        outlocationnum = int(endin % (len(allline[1])-1))
        cclist = list(allreal[golinenum+1:outlinenum+2])
        for i in cclist:
            dic = dic + i.strip()    
        dicout = dic[golocationnum:]
        dicout = dicout[:-(len(allline[1])-outlocationnum-1)]
        print(">"+ m +"-"+str(gggg)+"-"+ str(goin)+"-"+str(endin),file = k)
        print(dicout,file = k)
        return ">"+m+str(gggg)+"-"+ str(goin)+"-"+str(endin)+dicout


    goin = a
    chromosome = b
    start = c
    end =  d
            #goout = e        

    fr=open(goin, 'r')
    allline = fr.readlines()
            #outfile = open(goout, 'w')
    gggg = str(chromosome)
    #print(gggg)
    first = int(start)-1
    last = int(end)
    cc = chromosome_select(gggg)
    printtext = seq_select(first,last,cc,gggg)   
    fr.close()
    return printtext