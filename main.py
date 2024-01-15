from colorama import init, Fore
import time

init()

def print_cor(texto, cor=Fore.RESET):
    print(cor + texto + Fore.RESET)

def calculadora():
    while True:
        print("")
        print("")
        print("")
        print("Escolha uma das opções!\n")
        print_cor("1. Soma", Fore.LIGHTBLUE_EX)
        print_cor("2. Subtração", Fore.BLUE)
        print_cor("3. Multiplicação", Fore.LIGHTCYAN_EX)
        print_cor("4. Divisão", Fore.LIGHTMAGENTA_EX)
        print("")

        escolha = input("Escolha a operação que deseja realizar: ")

        if escolha in ('1', '2', '3', '4'):
            numero1 = float(input("Qual é o primeiro número: "))
            numero2 = float(input("Qual é o segundo número: "))

            if escolha == "1":
                resultado = numero1 + numero2
                print("O resultado é:", resultado)
            elif escolha == "2":
                resultado = numero1 - numero2
                print("O resultado é:", resultado)
            elif escolha == "3":
                resultado = numero1 * numero2
                print("O resultado é:", resultado)
            elif escolha == "4":
                if numero2 != 0:  
                    resultado = numero1 / numero2
                    print("O resultado é:", resultado)
                else:
                    print("")
                    print("Um número não pode ser dividido por 0!")
        else:
            print_cor("Opção inválida. Por favor, escolha uma das opções acima.", Fore.RED)

calculadora()
