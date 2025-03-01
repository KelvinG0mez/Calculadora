def menu():
   print('''\n
[1] SOMAR 
[2] MULTIPLICAR
[3] DIVISÃO
[4] PORCENTAGEM
[5] MAIOR 
[6] NOVOS NUMEROS
[7] SAIR DO PROGRAMA''')
#AQUI PEDIMOS AO USUARIO QUE DIGITE OS VALORES.
print("="*28)
valor1 = int(input("\nDigite o prineiro valor: "))
valor2 = int(input("\nDigite o segundo valor: "))
print("-"*28)
#DIFINIMOS UMA VARIAVEL PARA A ESCOLHA E RECEBE 0.
escolha = 0
#AQUI COMEÇA O LAÇO DE REPETIÇÃO.
while True:
    #CHAMAMOS MENU PARA MOSTRAR AO USUARIO AS OPÇÕES.
    menu()
    #AQUI PEDIMOS AO USUARIO QUE ESCOLHA UMA DAS OPÇOES DO MENU.
    print("-"*28)
    escolha = int(input("\nQual a sua escolha? "))
    print("-"*28)
    #SE ESCOLHA FOR 1, ELE SOMA. 
    if escolha == 1:
       print(f"\nA soma de {valor1} + {valor2} = {valor1+valor2}")
       print("-"*28)
    #SE ESCOLHA FOR 2, ELE MULTIPLICA.
    elif escolha == 2:
       print(f"\nA multiplicacao de {valor1} x {valor2} = {valor1*valor2}")
       print("-"*28)
    #SE ESCOLHA FOR 3, ELE FAZ A DIVISÃO.
    elif escolha == 3:
        print(f"A divisão de {valor1} / {valor2} = {valor1/valor2:.1f}")
        print("-"*28)
    #SE ESCOLHA FOR 4, ELE MOSTRA A PORCENTAGEM.
    elif escolha == 4:
        print(f"{valor1} % de {valor2} = {valor1*(valor2/100)}")
    #SE ESCOLHA FOR 5, ELE MOSTRA O MAIOR DIGITADO.  
    elif escolha == 5:
        if valor1 > valor2:
           escolha = valor1
        elif valor2 > valor1:
             escolha = valor2
        print(f"\nO maior numero digitado: {escolha}")
        print("-"*28)
    #SE ESCOLHA FOR 6, ELE RENOVA OS NUMEROS.   
    elif escolha == 6:
         valor1 = int(input("\nDigite o prineiro valor: "))
         valor2 = int(input("\nDigite o segundo valor: "))  
         print("-"*28)
    #SE ESCOLHA FOR 7, O CODIGO ENCERRA.  
    elif escolha == 7:
        print("\nSaindo do Programa!")
        print("-"*28)
        break
    #CASO USUARIO DIGITE UM NUMERO QUE NAO ESTA NAS OPÇÕES.    
    else: 
         print("\nOpcao ivalida!\nTente novamente!")
         print("-"*28)
#MENSAGEM DE FINALIZAÇÃO.        
print("\nPrograma Finalizado!")
print("="*28)
