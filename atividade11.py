#um programa  simples para registrar  informacoes de  uma turma.o programa deve permitir cadastrar varios alunos.


soma_notas = 0
aluno_maior_nota = ""
maior_nota = 0
total = 0

#inicio de loop

while True:
    nome= input("digite o nome do aluno:")
    nota= input("digite a nota final do aluno:")

#verificar se as  notas nao numeros inteiro valido 

    if nota.isdigit(): #se todos caracteres sao digitos
        nota = int(nota) #converter a string para inteiro

#se a nota nao for valida, exibir uma mensagem de erro
    else:
     print("nota invalida.digite apenas numeros.")
     continue 

#atualizar a soma total das notas

    total+= 1
    soma_notas+= nota

#verificar o nome do aluno, com a nota maior
 
    if nota > maior_nota:
     maior_nota = nota 
     aluno_maior_nota = nome

#perguntar se o usuario deseja continuar

    continuar = input("deseja continuar? (S/N):").strip().upper()

#se a resposta for 'S' o loop termina
    if continuar != 'S':
     break

#exibir resultados finais
print("resultado final:")
print(f"total de alunos cadatrados, {total}:")
print(f"soma total das notas : {soma_notas / total:2f}")
print(f" nome do aluno com maior nota: {aluno_maior_nota}")