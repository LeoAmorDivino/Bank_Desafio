
def depositar(saldo, deposito, extrato, /):
        
                if deposito > 0:
                        saldo += deposito
                        extrato += f"Depósito: R$ {deposito:.2f}\n"
                        print("Deposito feito com sucesso!")

                else:
                        print("O valor inserido não é compativel, tente novamente!")

                return saldo, extrato
   
def sacar(*, saldo, saque, extrato, limite, limite_saques, numero_saques):
                if saque <= 0:
                        print("O valor informado é inválido.")
                elif saque > saldo:
                        print("O saldo não é suficiente. Tente novamente!.")
                elif saque > limite:
                        print("O valor do saque excede o limite.")
                elif numero_saques >= limite_saques:
                        print("Número máximo de saques por hoje!. ")
                else:
                        saldo -= saque
                        extrato += f"Saque: R$ {saque:.2f}\n"
                        numero_saques += 1

                return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, * , extrato):
                
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")

                return saldo, extrato

       # def usuarios():


def usuario(usuarios):
    cpf = input("Digite seu CPF (Apenas números): ")
   
    
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            print("CPF já cadastrado. Por favor, tente novamente.")
            return


    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereco (logradouro - numero - bairro - cidade/sigla estado): ")    
        
    novo_usuario = {
        'cpf': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    }
    
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!!!.")

def criar_conta(agencia, numero_conta, usuarios):
        cpf = input("Digite seu CPF para continuar: ")  

        for usuario in usuarios:
          if cpf == usuario['cpf']: 
                  print("Conta criada com sucesso!!!") 
                  return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}

        print("Usuario não encontrado")
        

def main():
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        usuarios = []
        contas = []

        AGENCIA = "0001"
        LIMITE_SAQUES = 3 
        while True:
                Operacao = int(input("Escolha o que deseja fazer:\n1 - Realizar um depósito\n2 - Realizar um saque\n3 - Verificar saldo\n4 - Cadastrar novo Usuario\n5 - Criar nova conta\n6 - Cancelar operação\n"))

                if Operacao == 1:
                       deposito = float(input("Digite o valor de deposito: "))
                       saldo, extrato = depositar(saldo, deposito, extrato)    

                elif Operacao == 2:
                        saque = float(input("Digite o valor que deseja sacar: ")) 

                        saldo, extrato, numero_saques = sacar(
                                saldo = saldo, 
                                saque = saque, 
                                extrato = extrato, 
                                limite = limite, 
                                limite_saques = LIMITE_SAQUES, 
                                numero_saques = numero_saques
                        )

                elif Operacao == 3:
                       exibir_extrato(saldo, 
                       extrato= extrato)

                elif Operacao == 4:
                        usuario(usuarios)
                
                elif Operacao == 5:
                       numero_conta = len(contas) + 1
                       conta = criar_conta(AGENCIA, numero_conta, usuarios)

                       if conta:
                               contas.append(conta)

                elif Operacao == 6:
                        break

                else:
                        print("Operação invalida, Tente novamente.")

main()

