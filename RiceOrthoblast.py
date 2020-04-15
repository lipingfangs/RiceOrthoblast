import os
import sys
input_file = sys.argv[1]
input_pro =  sys.argv[2]
thread = sys.argv[3]

command = "makeblastdb -in "+  input_file + " -dbtype nucl -title w0 -parse_seqids -out w0"
os.system(command)

command2 = "python ./open2.py " + input_pro +" " +thread  +" " + input_file 
os.system(command2)
