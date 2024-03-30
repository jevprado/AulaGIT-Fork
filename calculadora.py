# calculadora python de notas -> C1 - UnB - Professor Fragelli 

nota1 = float(input("Qual a sua nota de questionarios: "))
nota2 = float(input("Qual a sua nota da P1: "))
nota3 = float(input("Qual a sua nota da P2: "))
nota4 = float(input("Qual a sua nota da P3: "))

notas = nota1*1 + nota2*2 + nota3*2 + nota4*3 
media = notas/8 

if media > 5.0: 
    print(f"A sua nota na disciplina de Cálculo 1 foi {media}. Parabéns, voce esta aprovado!")
else: 
    print(f"A sua nota na disciplina de Cálculo 1 foi {media}. Infelizmente, voce esta reprovado!")