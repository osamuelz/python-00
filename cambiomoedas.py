def conversor_moedas():
    print(" - Conversor de moedas -")
    
    taxas = {
        "USD": 0.20,
        "EUR": 0.18, 
    }

    try:
        valor_brl = float(input("digite o valor em R$: "))
        
        print("\nmoedas disponíveis:")
       
        for moeda in taxas.keys(): #retirar apenas os valores da lista
            print(f"{moeda}")
    
        cambio = input("\nqual moeda converter? ").upper() #transformar as letras em maiusculas

        if cambio in taxas: #cambio - guarda a variavel da MOEDA
            resultado = valor_brl * taxas[cambio]
            print(f"\nR$ {valor_brl} equivalem a {cambio} {resultado}")
        else:
            print("\nMmeda não encontrada")
            
    except ValueError:
        print("\n Erro : digite os numeros corretamente")

conversor_moedas()