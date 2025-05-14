#criar um programa em python que cadatre informacoes de 5 alunos.para  cada aluno, o programa deve 
#solicitar:

alunos = []

for i in range (1):
     aluno= input("digite o nome do aluno")
     av1= float(input("digite a nota da av1:"))
     av2= float(input("digite a nota av2:"))
     media = (av1 + av2)/2
     alunos.append({
          "nome":aluno,
          "av1": av1,
          "av2":av2,
          "media":media
     })
print ("\n --- resultado final ---")
for aluno in alunos:
 print(f"nome:{aluno['nome']} - av1: {aluno['av1']} - av2: {aluno['av1']:2f}")


     
     
    
            
    