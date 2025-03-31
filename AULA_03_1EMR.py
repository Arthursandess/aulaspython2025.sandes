#TERCEIRA AULA DE PYTHON|CONTEÚDO: IF + ELSE

media_final = float(input("Média final de 0 a 10= "))
if media_final >= 6:
    print("Você está APROVADO!!")
else:
    print("Você foi REPROVADO!!")

 # EXERCICIO 1:
vel_max = int(input("Velocidade ao passar no radar = "))

if vel_max > 80:
    multa =(vel_max - 80) * 5
    print("VOCE FOI MULTADO EM R$ %.2f" %multa)
else:
    print("OK!")
# EXERCICIO 2:

num_1 = float(input("Nº1 ="))
num_2 = float(input("Nº2 ="))
num_3 = float(input("Nº3 ="))

if num_1>num_2 and num_1>num_3:
        print(f"o maior numero é: {num_1}")
if num_2>num_3 and num_2>num_1:
     print(f"o maior numero é: {num_2}")
if num_3>num_2 and num_3>num_1:
     print(f"o maior numero é: {num_3}")

if num_1<num_2 and num_1<num_3:
        print(f"o menor numero é: {num_1}")
if num_2<num_3 and num_2<num_1:
     print(f"o menor numero é: {num_2}")
if num_3<num_2 and num_3<num_1:
     print(f"o menor numero é: {num_3}")

# EXERCICIO 3

salario= float(input("Valor do seu salário atual: "))

if salario >1250:

    novo_salario =salario + salario*0.1
    print("Seu novo salário é R$ %.2f" %novo_salario)

if salario <1250:

    novo_salario =salario + salario*0.15
    print("Seu novo salário é R$ %.2f" %novo_salario)

