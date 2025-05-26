
quantidade_pessoas = 0
soma_idade = 0
nome_mais_velho = ""
idade_mais_velho = 0

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    quantidade_pessoas += 1
    soma_idade += idade

    if quantidade_pessoas == 1 or idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

    while True:
        resposta = input("Deseja continuar? (sim/nao): ").strip().lower()
        if resposta in ['sim', 'nao']:
            break
        else:
            print("Resposta inválida. Digite apenas 'sim' ou 'nao'.")

    if resposta == 'nao':
        break

# Calcular média de idade
if quantidade_pessoas > 0:
    media_idade = soma_idade / quantidade_pessoas
else:
    
    media_idade = 0

# Mostrar os resultados
print(f"\nQuantidade de pessoas cadastradas: {quantidade_pessoas}")
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Pessoa mais velha: {nome_mais_velho} ({idade_mais_velho} anos)")
