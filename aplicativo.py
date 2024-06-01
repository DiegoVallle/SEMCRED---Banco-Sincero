saldo = 0
limite_qtd_saque = 3
qtd_saques = 0
limite_valor_saque = 500.00
extrato = ""
clientes = []
agencia = "0001"
num_conta = 1
contas = []



def deposito():
    global saldo, extrato
    valor_deposito = float(input("Ah, finalmente resolveu guardar um dinheiro? Digite a mixaria que deseja depositar:   "))
    if valor_deposito > 0:
        print("Só isso? Bom, melhor que nada")
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito}\n"

    elif valor_deposito == 0:
        print("ZERO? Oi? Não tem como né?")
    else:
        print("Tá me tirando? Como você pode depositar UM VALOR NEGATIVO?")
    return saldo, extrato
        

def saque():
    global saldo, extrato, limite_qtd_saque, limite_valor_saque, qtd_saques
    valor_saque = float(input("Ah, já vai gastar a mixaria? Digite o valor do saque:   "))
    if valor_saque <= 0:
        print("Valor de saque inválido")
    elif valor_saque > saldo:
        print("Você não pode sacar o que não tem. PARA DE SER DOIDA!")
    elif valor_saque > limite_valor_saque:
        print("Aqui tem regras benhê, saque acima do seu limite")
    elif qtd_saques >= limite_qtd_saque:
        print("Já tá bom, esgotou a quantidade diária de saques")
    else:
        print("Toma! Vê se não gasta tudo de uma vez")
        qtd_saques += 1
        saldo -= valor_saque
        extrato += f"Saque de R$ {valor_saque}\n"
    return saldo, extrato


def imprime_extrato():
    global extrato, saldo
    print("\n#################### EXTRATO SEM CRED ####################")
    print("NÃO TEM NADA AQUI!!!." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("############################################################")    


def cadastro_cliente():
    global clientes
    cpf = input("Digite seu CPF, mas ATENÇÃO, somente números viu?: ")
    if cpf in [cliente['cpf'] for cliente in clientes]:
        print("Já esqueceu de mim? Já tem um CPF igualzinho ao seu no meu sistema")
    else:
        nome = input("Digite o nome completo benzinho: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        endereco = input("E onde você mora? Rua, Bairro, Cidade, Estado e CEP. Essa informação é importante para eu NUNCA passar perto: ")
        clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Pronto, agora você já é um de nossos amados clientes")
    return 


def cadastro_conta():
    global agencia, num_conta, clientes, contas
    cpf = input("Digite seu CPF, benzinho: ")
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        nome_cliente = cliente_encontrado['nome']  
        
        print(f"Ah ótimo, sua agência é {agencia} e sua conta é {num_conta}. Vê se anota para eu não ter que passar novamente!")
        
        contas.append({
            "agencia": agencia,
            "numero_conta": num_conta,
            "cpf": cpf,
            "nome": nome_cliente  
        })
        
        num_conta += 1
    
    if not  cliente_encontrado:
        print("Não achei seu belo CPF aqui no meu cadastro. Faça o cadastro de cliente primeiro, seu afobado!")
    return
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['nome']}
        """
        print("=" * 100)
        print(linha)

menu = ''' 


    ESTE É O APLICATIVO DO SEMCRED
      
      Digite a opção desejada, seja breve e não me amole:
      
      1 - Depósito
      2 - Saque
      3 - Extrato
      4 - Novo cliente
      5 - Gerar nova conta
      6 - Listar contas
      9 - Vazar
      '''

while True:
    opcao =input(menu)
    if opcao == "1":
        deposito()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        imprime_extrato()
    elif opcao == "4":
        cadastro_cliente()
    elif opcao == "5":
        cadastro_conta()
    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "9":
        print("Já vai tarde!")
        break
    

    else:
        print("VOCÊ ESTÁ VENDO ESTE NÚMERO NO MENU?")