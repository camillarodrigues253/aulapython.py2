#cria uma lista vazia que ira armazenar os dados das comissoes dos  funcionarios
comissoes = []

#loop que, neste caso, roda apenas 1 vez (poderia ser aumentado para mais funcionarios)
for i in range (1):
    nome  =  input("digite o nome do funcionario:")
    comissaoum = float(input("digite a sua  comissao  no primeiro  mes:"))
    ("numero com virgula")
    comissaodois = float(input("digite a sua comissao no segundo mes:"))

    #calcula a media
    media = (comissaoum + comissaodois) / 2
    #adiciona os dados coletados a lista 'comissoes' no formato de dicionario

    comissoes.append({
        "nome": nome,
        "comissao 1": comissaoum,
        "comissao 2": comissaodois,
        "media": media   
        })
print("\n--- resultado final ---")
#inicia um novo loop que percorre cada comissao da lista comissoes
for comissao in comissoes:
    print(f"{comissao['nome']} - comissao 1: {comissao['comissao 1']} | comissao 2:{comissao['comissao 2']} | media: {comissao['media']:.2f}")