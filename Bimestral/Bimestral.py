print("----------------------------")
print("---------- CAJERO ----------")
print("----------------------------")

# input 
Dinero = int (input ("Digite el dinero para retirar: "))
conta_monedas_100=0
conta_billetes_10000=0
conta_billetes_2000=0

# processing
while Dinero !=0:
    monedas_100=Dinero
    billetes_10000=(monedas_100-monedas_100%10000)//10000
    monedas_100=monedas_100%10000
    billetes_2000=(monedas_100-monedas_100%2000)//2000
    monedas_100=monedas_100%2000
    monedas_100=(monedas_100-monedas_100%100)//100
    monedas_100=monedas_100%100

    print ('Cantidad de billetes de 10000: ' + repr (billetes_10000))
    print ('Cantidad de billetes de 2000: ' + repr (billetes_2000))
    print ('Cantidad de monedas de 100: ' + repr (monedas_100))

    conta_monedas_100=conta_monedas_100 + monedas_100
    conta_billetes_10000=conta_billetes_10000 + billetes_10000
    conta_billetes_2000=conta_billetes_2000 + billetes_2000
    
    Dinero = int (input ("Digite el dinero para retirar: "))

else:
    print("Al final del dia...")

# output

print("El total de billetes de 10000 utilizados fueron: " + str(conta_billetes_10000))
print("El total de billetes de  de 2000 utilizados fueron: " + str(conta_billetes_2000))
print("El total de monedas de 100 utilizadas fueron:  " + str(conta_monedas_100))
