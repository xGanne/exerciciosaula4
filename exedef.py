def cria_conta(numero, titular, saldo, limite):
    conta = {"Número: ": numero, "Titular: ": titular, "Saldo: ": saldo, "Limite: ": limite}
    return conta

def sacar(conta, valor):
    conta["Saldo"] -= valor
    return conta

c1 = cria_conta(123, "Juan", 1000, 5000)
c2 = cria_conta(444, "Matheus", 450, 800)

print(c1)