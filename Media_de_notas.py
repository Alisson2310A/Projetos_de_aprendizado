def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"

if __name__ == "__main__":
    notas = []
    num_notas = int(input("Quantas notas deseja inserir? "))

    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    print(f"Sua média é: {media:.2f}")
    print(f"Situação: {situacao}")