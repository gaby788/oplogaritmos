import math 
b=float(input("ingrese numero"))
x=float(input("ingrese base"))
if b>0 and x>0 and x !=0:
    operacion=math.log(b,x)
    print(operacion)
else:
    print("no se puede realizar ese logaritmo")
