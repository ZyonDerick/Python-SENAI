valor_total = 0

while True:
        valor_produto = float(input("Digite o valor do produto: "))
        if valor_produto > 0:
            valor_total += valor_produto
        elif valor_produto < 0:
            print("Valor inválido, digite outro")
            pass
        if valor_produto == 0 and valor_total >= 1000:
            desconto = (valor_total * 1.1) - valor_total 
            print(f"Total a pagar: R${valor_total - desconto}")
            break
        elif valor_produto == 0:
            print(f"Total a pagar: R${valor_total}")
            break