# CHECKPOINT 2 VINICIUS BATISTA E ARTHUR SANDES
# Introdução:
print("Bem vindo a calculadora de media semestral da FIAP!!")
print("Lembrando que na calculadora, é aceito somente valores de 0 a 10!!")

excluir = 0  # Seletora de exclusão do menor checkpoint
media_sem1 = 0
media_sem2 = 0
chave = 0
media_final = 0

while chave != 2:
    if chave == 0:
        print("Por favor, digite as notas do Primeiro semestre")
    else:
        print("Por favor, digite as notas do Segundo semestre")
    # Variáveis
    cp1 = float(input("Checkpoint 1 (0 a 10) = "))
    cp2 = float(input("Checkpoint 2 (0 a 10) = "))
    cp3 = float(input("Checkpoint 3 (0 a 10) = "))
    sp1 = float(input("Sprint 1 (0 a 10) = "))
    sp2 = float(input("Sprint 2 (0 a 10) = "))
    gs = float(input("Global Solution (0 a 10) = "))

    # Exclusão da menor nota de checkpoint
    if cp1 < cp2 and cp1 < cp3:
        excluir = 1
    elif cp2 < cp1 and cp2 < cp3:
        excluir = 2
    elif cp3 < cp1 and cp3 < cp2:
        excluir = 3
    else:
        excluir = 0

    # Calculo da média semestral
    if excluir == 1:
        if chave == 0:
            media_sem1 = ((cp2 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
        else:
            media_sem2 = ((cp2 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    elif excluir == 2:
        if chave == 0:
            media_sem1 = ((cp1 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
        else:
            media_sem2 = ((cp1 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    elif excluir == 3:
        if chave == 0:
            media_sem1 = ((cp1 + cp2 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
        else:
            media_sem2 = ((cp1 + cp2 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    else:
        # Caso haja igualdade entre as notas
        if cp1 == cp2:
            if chave == 0:
                media_sem1 = ((cp1 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
            else:
                media_sem2 = ((cp1 + cp3 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
        else:
            if chave == 0:
                media_sem1 = ((cp1 + cp2 + sp1 + sp2) / 4) * 0.4 + gs * 0.6
            else:
                media_sem2 = ((cp1 + cp2 + sp1 + sp2) / 4) * 0.4 + gs * 0.6

    chave += 1

# Cálculo da média final.
media_final = (media_sem1 * 0.4) + (media_sem2 * 0.6)

# Impressão do resultado
print("Média semestral 1 = %.1f" % media_sem1)
print("Média semestral 2 = %.1f" % media_sem2)
print("Média final = %.1f" % media_final)