#watchdata
import argparse
def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', '--skipped_columns', action='store',
                        type=int,
                        default=30,
                        help='How many amino acid the shortest protein should be with [Default: 30]')
    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()
    number = options.skippe_dcolumns  
    import sys 
    import os 
    go = sys.argv[1]
    command1 = "cat "+go+"/* allseq.fa"
    os.system(command1)
    
    out = sys.argv[2]

    filed = open(go+"/* allseq.fa","r")
    files = open("o.tat","w")
    lines = filed.readlines()
    lines = list(lines)

    for i in lines:
        if i.find("/") == -1 and i.find("aking") == -1:
            print(i,file = files  )



    filed.close()
    files.close()

    file2 = open("o.tat","r")
    liness = file2.readlines()
    liness = list(liness)
    dic = {}
    for j in liness:
        j = j.strip()
        if j.startswith(">"):
            temp = j.strip()[1:]
            dic[temp] = ""
        else:
            dic[temp] = dic[temp] + j
    #print(dic)

    outfile = open(out,"w")
    dici = list(dic.keys())
    for i in dici:
        if dic[i].startswith("M") and len(dic[i]) > int(number):
            print(">"+i,file = outfile)
            print(dic[i],file = outfile)
    outfile.close()
