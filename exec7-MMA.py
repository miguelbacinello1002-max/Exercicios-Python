# Código para classificação de lutadores de MMA

print("="*50)
print("       Classificação de Lutadores de MMA       ")
print("="*50 + "\n")

print("="*50 + "\n")
print("CATEGORIA DE PESO")
print("1. Peso Mosca: até 56,7 kg")
print("2. Peso Galo: até 61,2 kg")
print("3. Peso Pena: até 65,8 kg")
print("4. Peso Leve: até 70,3 kg")
print("5. Peso Médio: até 77,1 kg")
print("6. Peso Pesado: até 83,9 kg")
print("7. Peso Super Pesado: acima de 83,9 kg\n")
print("="*50 + "\n")

nome = input("Digite o nome do lutador: ").strip()
peso = float(input("Digite o peso do lutador (em kg): "))

if peso >= 40 and peso <= 56.7:
    print(f"O lutador {nome} está na categoria de Peso Mosca.")
elif peso >= 56.8 and peso <= 61.2:
    print(f"O lutador {nome} está na categoria de Peso Galo.")
elif peso >= 61.3 and peso <= 65.8:
    print(f"O lutador {nome} está na categoria de Peso Pena.")
elif peso >= 65.9 and peso <= 70.3:
    print(f"O lutador {nome} está na categoria de Peso Leve.")
elif peso >= 70.4 and peso <= 77.1:
    print(f"O lutador {nome} está na categoria de Peso Médio.")
elif peso >= 77.2 and peso <= 83.9:
    print(f"O lutador {nome} está na categoria de Peso Pesado.")
elif peso >= 84.0 and peso <= 120.0:
    print(f"O lutador {nome} está na categoria de Peso Super Pesado.")
else:
    print(f"O lutador {nome} não se enquadra em nenhuma categoria de peso válida.")

      
      
      