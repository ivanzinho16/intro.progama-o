saldo = float(input("Saldo de moedas: "))
valor_skin = float(input("valor da skin: "))

if saldo >= valor_skin:
    print("Comprar realizada! Aproveite sua nova skin.")
    saldo = saldo - valor_skin
    print (f"saldo restante {saldo} moedas")
else:
    print("saldo insuficiente! ")
    restante = valor_skin - saldo
    print(f"Faltam {restante} moedas para comprar este item.")
