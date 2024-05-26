saldo = 0
limite_qtd_saque = 3
qtd_saques = 0
limite_valor_saque = 500.00
extrato = ""

menu = ''' ESTE É O APLICATIVO DO SEMCRED
      
      Digite a opção desejada, seja breve e não me amole:
      
      1 - Depósito
      2 - Saque
      3 - Extrato
      4 - Vazar
      '''

while True:
    opcao =input(menu)
    if opcao == "1":
        valor_deposito = float(input("Ah, finalmente resolveu guardar um dinheiro? Digite a mixaria que deseja depositar:   "))
        if valor_deposito > 0:
            print("Só isso? Bom, melhor que nada")
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito}\n"

        elif valor_deposito == 0:
            print("ZERO? Oi? Não tem como né?")
        else:
            print("Tá me tirando? Como você pode depositar UM VALOR NEGATIVO?")
    elif opcao == "2":
        valor_saque = float(input("Ah, já vai gastar a mixaria? Digite o valor do saque:   "))
        if valor_saque <= limite_valor_saque and qtd_saques < limite_qtd_saque and valor_saque <= saldo:
            print("Toma! Vê se não gasta tudo de uma vez")
            qtd_saques += 1
            saldo -= valor_saque
            extrato += f"Saque de R$ {valor_saque}\n"
        elif valor_saque <= limite_valor_saque and qtd_saques < limite_qtd_saque and valor_saque >= saldo:
            print("Você não pode sacar o que não tem. PARA DE SER DOIDA!")
        elif valor_saque >= limite_valor_saque and qtd_saques <= limite_qtd_saque: 
            print("Aqui tem regras benhê, saque acima do seu limite")
        elif valor_saque <= limite_valor_saque and qtd_saques >= limite_qtd_saque: 
            print("Já tá bom, esgotou a quantidade diária de saques")
        else:
            print("AMIGA assim eu não consigo te ajudar, esgotou todos os limites!")


    elif opcao == "3":
        print("\n#################### EXTRATO SEM CRED ####################")
        print("NÃO TEM NADA AQUI!!!." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("############################################################")

    elif opcao == "4":
        print("Já vai tarde!")
        break
    

    else:
        print("VOCÊ ESTÁ VENDO ESTE NÚMERO NO MENU?")