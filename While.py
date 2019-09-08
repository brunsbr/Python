nota = float(input("Digite Sua nota:"))
while(nota > 10) or (nota < 0):
    print ("Inválido")
    nota = float(input("Digite uma nota válida"))
if(nota >= 5):
    print("APROVADO")
else :
    print ("REPROVADO!!")
   
