anos_exp = float(input("Anos de experiência da área: "))

if anos_exp >= 5:
    print("Categoria: Desenvolvedor Sênior")
elif anos_exp >= 2:
    print("Categoria: Desenvolvedor Pleno")
else:
    print("Categoria: Desenvolvedor Junior")