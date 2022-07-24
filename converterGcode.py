import sys

str = ""
linea = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
       str += line.replace('\n', '\r\n')
       linea += 1

nome = "Modify_" +  sys.argv[1]

if(len( sys.argv) == 3):
    nome = sys.argv[2] + ".nc"

open(nome, 'w').write(str)

print("File completato.\nLinee: {}".format(linea))
       