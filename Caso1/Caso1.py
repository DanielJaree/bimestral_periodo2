"""Programa para calcular la nota final de un estudiante en una materia 
por las calificaciones de sus evaluanciones"""

print("--------------------------------")
print("------ NOTAS ESTUDIANTES -------")
print("--------------------------------")

#Input
cod = int(input("Digite el código del estudiante: "))
if cod!=0:
    nota1 = float(input("Digite la de la 1ra evaluación: "))
    nota2 = float(input("Digite la de la 2da evaluación: "))
    nota3 = float(input("Digite la de la 3ra evaluación: "))
    nota4 = float(input("Digite la de la 4ta evaluación: "))
    nota5 = float(input("Digite la de la 5ta evaluación: "))

else:
    print("fin de la entrada")

#Prossecing
reprobados = 0
while cod != 0:
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    print("La nota definitiva de el estudiante con el codigo " + str(cod) + " fue de " + str(nota_final))
    cod = int(input("Digite el código del estudiante: "))
    if cod!=0:
            nota1 = float(input("Digite la de la 1ra evaluación: "))
            nota2 = float(input("Digite la de la 2da evaluación: "))
            nota3 = float(input("Digite la de la 3ra evaluación: "))
            nota4 = float(input("Digite la de la 4ta evaluación: "))
            nota5 = float(input("Digite la de la 5ta evaluación: "))
    else:
        print("fin de la entrada")
    if nota_final < 3:
        reprobados = reprobados + 1

#Output
print(str(reprobados) + " reprobaron la materia")
print("Eso era...")