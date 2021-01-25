
from csv import DictWriter
from csv import DictReader
from reset_screen import clear_console, clear_pycharm
from os.path import exists


class Address:

    #  A dictionary containing the alias as keys and the names as values, of the states in the country
    country_uf = {
        'RO': 'Rondônia',
        'AC': 'Acre',
        'AM': 'Amazonas',
        'RR': 'Roraima',
        'PA': 'Pará',
        'AP': 'Amapá',
        'TO': 'Tocantins',
        'MA': 'Maranhão',
        'PI': 'Piauí',
        'CE': 'Ceará',
        'RN': 'Rio Grande do Norte',
        'PB': 'Paraíba',
        'PE': 'Pernambuco',
        'AL': 'Alagoas',
        'SE': 'Sergipe',
        'BA': 'Bahia',
        'MG': 'Minas Gerais',
        'ES': 'Espírito Santo',
        'RJ': 'Rio de Janeiro',
        'SP': 'São Paulo',
        'PR': 'Paraná',
        'SC': 'Santa Catarina',
        'RS': 'Rio Grande do Sul',
        'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso',
        'GO': 'Goiás',
        'DF': 'Distrito Federal'
    }

    # complemento & descricao are optionals
    def __init__(self, cep, endereco, numero, bairro, uf, cidade, complemento=None, descricao=None):
        self.__cep = cep
        self.__endereco = endereco
        self.__numero = numero
        self.__bairro = bairro
        self.__uf = uf
        self.__cidade = cidade
        self.__complemento = complemento
        self.__descricao = descricao

    # Getters
    @property
    def cep(self):
        """Getter for 'cep'"""
        return self.__cep

    @property
    def endereco(self):
        """Getter for 'endereco'"""
        return self.__endereco

    @property
    def numero(self):
        """Getter for 'numero'"""
        return self.__numero

    @property
    def bairro(self):
        """Getter for 'bairro'"""
        return self.__bairro

    @property
    def uf(self):
        """Getter for 'uf'"""
        return self.__uf

    @property
    def cidade(self):
        """Getter for 'cidade'"""
        return self.__cidade

    @property
    def complemento(self):
        """Getter for 'complemento'"""
        return self.__complemento

    @property
    def descricao(self):
        """Getter for 'descricao'"""
        return self.__descricao

    def save_on_database(self):
        """
        This method is the one responsible for adding the new addresses to the database, which in this case, is a CSV
        file. It imports the DictWriter class from csv module, to write the instance attributes in the file.
        :return: None.
        """
        try:
            with open(create_database(), mode='a', encoding='utf-8', newline='') as file:
                keys = ['CEP', 'Endereco', 'Numero', 'Bairro', 'UF', 'Cidade', 'Complemento', 'Descricao']
                writer = DictWriter(file, fieldnames=keys)
                writer.writerow(
                    {'CEP': self.cep,
                        'Endereco': self.endereco,
                        'Numero': self.numero,
                        'Bairro': self.bairro,
                        'UF': self.uf,
                        'Cidade': self.cidade,
                        'Complemento': self.complemento,
                        'Descricao': self.descricao}
                    )
        except Exception as error:
            return f"Houve um problema na hora de salvar os dados. Detalhes do problema: {error}"


def create_database():
    """
    This functions checks if the databse exists in the relative path of the system file. If it doesn't, creates a new
    csv file with a header in it, if it does, pass to the next instruction.
    :return: Returns the path to the csv file created or existing.
    """
    new_db = ".\\addresses.csv"
    if exists(new_db) is False:
        try:
            with open(new_db, mode='a', encoding='utf-8', newline='') as db:
                keys = ['CEP', 'Endereco', 'Numero', 'Bairro', 'UF', 'Cidade', 'Complemento', 'Descricao']
                db_creator = DictWriter(db, fieldnames=keys)
                db_creator.writeheader()
        except Exception as error:
            return print(f"Houve um erro na hora de criar a base de dados do sistema. Detalhes do erro: {error}")
    else:
        return new_db


def read_database():
    """This function reads the csv file that the function create_database() returns, to show all the elements that are
     in it, trying to replicate a search query in a database. Also added a minor verification to show only the values
    and not the keys from the dictionary.
    :return: Returns the amount of addresses registered."""
    try:
        with open(create_database(), mode='r', encoding='utf-8') as db:
            reader = DictReader(db)
            counter = 0
            for row in reader:
                if row['CEP'] == 'CEP':
                    pass
                else:
                    print(f"CEP: {row['CEP']}"
                          f"| Endereço: {row['Endereco']}"
                          f"| Número: {row['Numero']}"
                          f"| Bairro: {row['Bairro']}"
                          f"| UF: {row['UF']}"
                          f"| Cidade: {row['Cidade']}"
                          f"| Complemento: {row['Complemento']}"
                          f"| Descrição: {row['Descricao']}")
                    counter = counter + 1

    except FileNotFoundError as error:
        return f"O arquivo de dados selecionado não existe! Detalhes do erro: {error}"
    except KeyError as error:
        return f"O arquivo de dados está corrompido! Problemas nas chaves do mesmo. Detalhes do erro: {error}"
    else:
        return f"Total de endereços cadastrados: {counter}"


def check_cep(element):
    """
    This function checks if the instance attribute 'CEP' already exists in the csv file that is working as a database.
    :param element: Receives the argument 'CEP' from the user.
    :return: Returns True if the 'CEP' received as element is in the database or False if isn't.
    """
    database = create_database()
    try:
        with open(database):
            pass
    except Exception as error:
        return f"Houve um erro inesperado: {error}"

    array_of_ceps = []
    with open(database, mode='r', encoding='utf-8') as db:
        reader = DictReader(db)
        for row in reader:
            if row['CEP'] == 'CEP':
                pass
            else:
                array_of_ceps.append(row['CEP'])
    if element in array_of_ceps:
        return True
    return False


def register_address():
    """
    This function is responsible for creating a new instance of the class Address, collecting from the user, the
    arguments needed for the builder method in the Address class. It also has some minor verifications to make sure
    that the arguments inserted are valid.
    :return: Returns an input option to get back to the initial screen.
    """
    # Asking for cep
    # I added a verification with list comprehension, to make sure the 'cep' typed is numbers only and has 8 digits
    numbers = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    print("Informe o CEP do novo endereço com 8 dígitos, sem traços ou espaços. (Obrigatório)")
    cep = input("CEP: ")
    num = [number for number in cep if number in numbers]
    while len(num) != 8:
        print("O CEP informado é inválido! Insira o CEP do novo endereço com 8 dígitos, sem traços ou espaços.")
        cep = input("CEP: ")
        num = [number for number in cep if number in numbers]
    if check_cep("".join(num)):
        clear_pycharm()
        clear_console()
        print("\nO CEP informado já se encontra cadastrado no sistema!")
        return input("Pressione 'enter' para voltar ao menu principal: ")

    # Asking for endereco
    # I added a simple verification with while loop to make sure something is typed in this field, since it is mandatory
    clear_pycharm()
    clear_console()
    print("\nInforme o endereço (nome da rua). (Obrigatório)")
    address = input("Endereço: ").strip().title()
    while len(address) < 1:
        print("O endereço é obrigatório!")
        address = input("Endereço: ").strip().title()

    # Asking for numero
    # I added a simple verification with while loop to make sure something is typed in this field, since it is mandatory
    clear_pycharm()
    clear_console()
    print("\nInforme o número do endereço. Caso não exista número, insira 's/n'. (Obrigatório)")
    number = input("Número: ").strip()
    while len(number) < 1:
        print("O número é obrigatório!")
        number = input("Número: ").strip()

    # Asking for bairro
    # I added a simple verification with while loop to make sure something is typed in this field, since it is mandatory
    clear_pycharm()
    clear_console()
    print("\nInforme o nome do bairro. (Obrigatório)")
    neighborhood = input("Bairro: ").title().strip()
    while len(neighborhood) < 1:
        print("O bairro é obrigatório!")
        neighborhood = input("Bairro: ").title().strip()

    # Asking for uf
    # I added a verification with the keys from the dictionary that is created in the class Address
    clear_pycharm()
    clear_console()
    print("\nInforme o Estado(UF) do endereço, apenas a sigla. (Obrigatório)")
    state = input("Estado(UF): ").upper().strip()
    while state not in Address.country_uf.keys():
        print("O Estado informado é inválido! Insira apenas a sigla do mesmo.")
        state = input("Estado(UF): ").upper().strip()
    state_value = Address.country_uf[state]

    # Asking for cidade
    # I added a simple verification with while loop to make sure something is typed in this field, since it is mandatory
    clear_pycharm()
    clear_console()
    print("\nInforme a cidade do endereço. (Obrigatório)")
    city = input("Cidade: ").title().strip()
    while len(city) < 1:
        print("A cidade é obrigatória!")
        city = input("Cidade: ").title().strip()

    # Asking for complemento - optional
    # This field has no verifications, because it is optional
    clear_pycharm()
    clear_console()
    print("\nInforme o complemento do endereço. (Opcional).")
    additional = input("Complemento: ")

    # Asking for descricao - optional
    # This field has no verifications, because it is optional
    clear_pycharm()
    clear_console()
    print("\nInforme a descrição do endereço. (Opcional).")
    description = input("Descrição: ")

    # Creating a new object from the class Address, using the fields above as arguments for the parameters
    new_address = Address(
        cep=cep,
        endereco=address,
        numero=number,
        bairro=neighborhood,
        uf=state_value,
        cidade=city,
        complemento=additional,
        descricao=description
    )

    # Save the object created in a CSV file, with the save_on_database() method
    new_address.save_on_database()

    clear_pycharm()
    clear_console()
    print("\nEndereço cadastrado com sucesso!")
    return input("Pressione 'enter' para voltar ao menu principal: ")


if __name__ == '__main__':
    create_database()
    print(read_database())
    print(register_address())
