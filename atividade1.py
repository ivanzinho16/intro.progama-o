valor = float(input("Valor da conta: "))
pessoas = int(input("Quantidade de pessoas:"))
taxa = input("ADiciona 10% (s ou n): ")

if taxa == "s":
    valor = valor + valor*0.10
elif  taxa == "n":
   print("sem taxa para o trabalhador")
else:
   print("Opção inválida! Desconsiderar taxa")
valor_por_pessoa = valor/pessoas
print("===== Resumo Da Conta =====")
print(f" valor da conta = R$ {valor:.2f}")
print(f" Valor por pessoa = R$ {valor_por_pessoa:.2f}")
