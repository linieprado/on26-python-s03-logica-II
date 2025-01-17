# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg 

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input("Quantidade de morangos (em Kg): "))
macas = float(input("Quantidade de maçãs (em Kg): "))

if morangos <= 5:
    valor_morangos = morangos * 2.50
else:
    valor_morangos = morangos * 2.20

if macas <= 5:
    valor_macas = macas * 1.80
else:
    valor_macas = macas * 1.50

valor_total_sem_desconto = valor_morangos + valor_macas

if (morangos + macas) > 8 or valor_total_sem_desconto > 25:
    desconto = 0.10 * valor_total_sem_desconto
else:
    desconto = 0

valor_final = valor_total_sem_desconto - desconto

print(f"Valor a ser pago: R$ {valor_final:.2f}")
