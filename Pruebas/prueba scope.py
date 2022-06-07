matriz = {"A":[1,0,1,0,0],"B":[1,0,0,1,1]}
for j in matriz.keys():
    for i in matriz[j]:
        print(i, end=" ")
    print("")
print ("la matriz ahora es: ",matriz["A"][1])
matriz["A"][1] = 1
print ("se ocupo el asiento: ",matriz["A"][1])
print (matriz["A"])     