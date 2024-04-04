nota1 = float(input("Qual a sua nota da P1: "))
nota2 = float(input("Qual a sua nota da P2: "))

notas = nota1*0.4 + nota2*0.6

if notas > 5.0: 
    print(f"A sua nota na disciplina de Teoria de eletronica digital 1 foi: {notas}. Parabéns, voce esta aprovado!")
else: 
    print(f"A sua nota na disciplina de Teoria de eletronica digital 1 foi: {notas}. Infelizmente, voce esta reprovado!")
