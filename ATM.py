#imports
import time
import os

#definiçoes

saldo=1100.10
cartão=False
atm=False
tentativas=0
#funçoes
def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.08)


#programa
print("")
while atm==False:
    print('============')
    print('ATM DESLIGDA')
    print('============')
    on=input('DIGITE [ON] PARA LIGA-LA: ')
    if on=='on':
        atm=True
    test()    
    os.system('cls' if os.name == 'nt' else 'clear')

print("")
while cartão==False:
    print(' ____________')
    print('|            |')
    print('|   E corp.  |')
    print('|____________|')
    print('')
    print('')
    print('insira seu cartão para iniciar')
    insere=('pressione enter para inserir seu cartão:')
    cartão=True
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print(' ____________')
    print('|            |')
    print('|   E corp.  |')
    print('|____________|')
    print('')
    senha1=input('digite sua senha numerica: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if senha1=='1234':
        print('acesso permitido')

        while True:
           
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

            print(' ____________')
            print('|            |')
            print('|   E corp.  |')
            print('|____________|')
            print('')
            print('[1]-vizualizar saldo')
            print('[2]-efetuar deposito')
            print('[3]-efetuar saque')
            print('[4]-efetuar tansferencia')
            print('[E}-sair')
            opçao=input('selecione sua opção: ')
            os.system('cls' if os.name == 'nt' else 'clear')

            if opçao=='1':
                print('O seu saldo é de: ',saldo)
                retorna=input('pressione enter para retornar ao menu principal')
                os.system('cls' if os.name == 'nt' else 'clear')
            
            if opçao=='2':
                quantia=int(input('qual a quantia a ser depositada: R$ '))
                saldo=saldo+quantia
                time.sleep(2)
                print('operação concluida ')
                print('O seu saldo é de: ',saldo)
                retorna=input('pressione enter para retornar ao menu principal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if opçao=='3':
                quantia=int(input('qual a quantia a ser sacada: R$ '))
                saldo=saldo-quantia
                time.sleep(2)
                print('operação concluida ')
                print('O seu saldo é de: ',saldo)
                retorna=input('pressione enter para retornar ao menu principal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if opçao=='4':
                conta=input('selecione a conta para receber a trasnferencia: ')
                quantia=int(input('qual a quantia a ser transferida: R$ '))
                saldo=saldo-quantia
                time.sleep(2)
                print('operação concluida ')
                print('O seu saldo é de: ',saldo)
                retorna=input('pressione enter para retornar ao menu principal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if opçao=='e':
                print('saindo...')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break


    else:        
        print('acesso negado')
        tentativas=tentativas+1
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if tentativas>3:
            print('encerrando seção')
            time.sleep(5)
            break
            
