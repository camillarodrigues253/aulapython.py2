#crie um programa que calcule o valor total a ser pago a um funcionario com base
#no umero de horas trabalhadas por dia, no valor da hora e na quantidade de dias
#trabalhados.

def pagamento ():
    
    horas =int(input("digite suas horas trabalhadas: "))
    valor =int(input("digite o valor da hora trabalhada: "))
    dias = int(input("digite os dias trabalhados"))
    total = (horas*valor) * dias

    print("total de pagamento",total)

pagamento()