
from reset_screen import clear_console, clear_pycharm
from classes_and_functions import register_address, read_database, create_database


# Checking if the file that will be read as database exists, if it doesn't, creates a new one
create_database()

while True:
    # Intro of the program
    clear_pycharm()
    clear_console()
    print("\nOlá! Bem vindo(a) a lista de endereços cadastrados! Os seguintes endereços já se encontram cadastrados no"
          " sistema: \n")

    # Showing the addresses that are in the database already, with the function read_database()
    print(read_database())

    # Validating the option chosen by the user
    print("\nGostaria de cadastrar um novo endereço, ou sair do sistema?")
    choice = input("Digite (1) para cadastrar ou (2) para sair: ")
    while choice != '1' and choice != '2':
        print("\nOpção inválida!")
        print("Gostaria de Cadastrar um novo endereço, ou sair do sistema?")
        choice = input("Digite (1) para cadastrar ou (2) para sair: ")

    # Closing the program if '2' is chosen or registering a new address if '1' is chosen, with the function
    # register_address()
    if choice == '2':
        print("\nAté a próxima!")
        input("Pressione 'enter' para finalizar o programa: ")
        break
    else:
        clear_pycharm()
        clear_console()
        print("\nVocê optou por cadastrar um novo endereço!\n")
        print(register_address())
