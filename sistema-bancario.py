
# Usuario tem que saber seu saldo 
# Usuario pode fazer operações saque, deposito e consulta de extrato
# limite de operações diarias igual a 3
# limite de saque diario igual a 1500
# obs: barrar saque maior que valor em conta 


atividade = -1
saldo = 6000
saque = 0
quantidade = 0
extrato = ""

while atividade != 0:
  comando = 0
  atividade = int(input(""" 
      ############### MENU ###############

    Operações disponiveis:
    1- Saque 
    2- Deposito
    3- Extrato

    0- Sair             Opção: """))
  print()
  print()
  if atividade == 1:
    if quantidade >= 3:
      print("Atingiu a quantidade de saques diario volte amanha.")
    else: 
      saque = int(input("Digite o valor a ser sacado: "))
      if saque <= 500 and saldo >= saque:
        saldo -= saque
        quantidade += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print(f"\nSaque realizado com sucesso, saldo atual de: R$ {saldo}")
      elif saldo < saque:
        print("Valor maior que o saldo atual.")
      elif saque > 500:
        print("Valor maior que limite do caixa." )
    comando = int(input("\nDesaja sair ? [1] SIM [2] NÃO      Opção: ")) 
    if comando == 1:
      break

  elif atividade == 2:
    deposito = int(input("Digite o valor a ser depositado: "))
    saldo += deposito
    extrato += f"Depósito: R$ {deposito:.2f}\n"
    print(f"Deposito realizado com sucesso, saldo atual de: R$ {saldo}")
    comando = int(input("\nDesaja sair ? [1] SIM [2] NÃO      Opção: ")) 
    if comando == 1:
      break


  elif atividade == 3:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    comando = int(input("\nDesaja sair ? [1] SIM [2] NÃO      Opção: ")) 
    if comando == 1:
      break

print("\n\nObrigado por utilizar nossos serviços!!\n\n\n")
