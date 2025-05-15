#criar um programa em python que cadatre informacoes de 5 alunos.para  cada aluno, o programa deve 
#solicitar:

alunos = []

for i in range (5):
     aluno= input("digite o nome do aluno:")
     av1= float(input("digite a nota da av1:"))
     av2= float(input("digite a nota av2:"))
     media = (av1 + av2)/2
     status= ("aprovado if media >= 6 else reprovado")

     alunos.append([aluno,av1,av2,media,status])
print ("\n --- resultado final ---")
for aluno in alunos:
 print(f"nome:{aluno[0]} - av1:{aluno[1]} - av2:{aluno[2]} - media:{aluno[3] :.2f} | status:{aluno[4]}")
