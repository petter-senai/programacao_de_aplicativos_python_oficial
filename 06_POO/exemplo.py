# =============================================================
# CLASSES E OBJETOS, ATRIBUTOS, MÉTODOS E CONSTRUTOR
# Exemplo: um celular
# =============================================================


# -------------------------------------------------------------
# 1. A CLASSE: o modelo (a "planta")
# -------------------------------------------------------------
# A palavra "class" cria um novo modelo.
# Por convenção, o nome da classe começa com letra maiúscula.

class Celular:

    # ---------------------------------------------------------
    # 2. O CONSTRUTOR: __init__
    # ---------------------------------------------------------
    # É um método especial, executado AUTOMATICAMENTE
    # toda vez que criamos um novo celular.
    # A função dele é preparar o objeto: guardar os dados iniciais.
    #
    # "self" é o próprio objeto que está sendo criado.
    # É através do self que o objeto guarda e acessa os seus dados.
    #
    # "bateria=100" é um valor padrão: se ninguém informar,
    # o celular já nasce com 100% de bateria.

    def __init__(self, marca, modelo, cor, bateria = 100):

        # -----------------------------------------------------
        # 3. OS ATRIBUTOS: as características do objeto
        # -----------------------------------------------------
        # self.algumacoisa = valor  -> cria um atributo no objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False     # todo celular começa desligado

    # ---------------------------------------------------------
    # 4. OS MÉTODOS: os comportamentos do objeto
    # ---------------------------------------------------------
    # Métodos são funções que ficam DENTRO da classe.
    # O primeiro parâmetro é sempre o self.

    def ligar(self):
        # O método consulta um atributo do próprio objeto
        if self.bateria == 0:
            print(f"{self.modelo}: sem bateria! Coloque para carregar.")
        else:
            self.ligado = True          # e também pode alterá-lo
            print(f"{self.modelo} ligado.")

    def desligar(self):
        self.ligado = False
        print(f"{self.modelo} desligado.")

    # Um método também pode receber parâmetros, como uma função comum
    def usar(self, minutos):
        if not self.ligado:
            print(f"{self.modelo} está desligado. Ligue primeiro!")
            return                      # sai do método aqui

        # A cada 10 minutos de uso, gasta 1% de bateria
        gasto = minutos // 10
        self.bateria = self.bateria - gasto

        if self.bateria <= 0:
            self.bateria = 0
            self.ligado = False
            print(f"{self.modelo} descarregou e desligou sozinho.")
        else:
            print(f"Usou o {self.modelo} por {minutos} min. Bateria: {self.bateria}%")

    def carregar(self, porcentagem):
        self.bateria = self.bateria + porcentagem
        if self.bateria > 100:          # a bateria não passa de 100%
            self.bateria = 100
        print(f"{self.modelo} carregado. Bateria: {self.bateria}%")

    def mostrar_info(self):
        situacao = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} ({self.cor}) - {self.bateria}% - {situacao}")


# =============================================================
# 5. OS OBJETOS: criados a partir da classe (as "casas")
# =============================================================
# Ao escrever Celular(...), o Python chama o __init__ sozinho.
# Não passamos o self: o Python faz isso por nós.

celular1 = Celular("Samsung", "Galaxy A15", "preto")       # bateria padrão: 100
celular2 = Celular("Motorola", "Moto G54", "azul", 30)     # bateria informada: 30

celular1.mostrar_info()   # Samsung Galaxy A15 (preto) - 100% - desligado
celular2.mostrar_info()   # Motorola Moto G54 (azul) - 30% - desligado


# -------------------------------------------------------------
# 6. ACESSANDO E ALTERANDO ATRIBUTOS
# -------------------------------------------------------------
# Usamos objeto.atributo para ler um dado
print(celular1.marca)     # Samsung
print(celular2.bateria)   # 30

# E também podemos alterar diretamente
celular1.cor = "branco"
celular1.mostrar_info()   # Samsung Galaxy A15 (branco) - 100% - desligado


# -------------------------------------------------------------
# 7. CHAMANDO MÉTODOS
# -------------------------------------------------------------
# Usamos objeto.metodo() para pedir que o objeto faça algo

celular2.usar(60)         # Moto G54 está desligado. Ligue primeiro!

celular2.ligar()          # Moto G54 ligado.
celular2.usar(60)         # Usou o Moto G54 por 60 min. Bateria: 24%
celular2.mostrar_info()   # Motorola Moto G54 (azul) - 24% - ligado

celular2.usar(300)        # Moto G54 descarregou e desligou sozinho.
celular2.ligar()          # Moto G54: sem bateria! Coloque para carregar.

celular2.carregar(50)     # Moto G54 carregado. Bateria: 50%
celular2.ligar()          # Moto G54 ligado.
celular2.mostrar_info()   # Motorola Moto G54 (azul) - 50% - ligado


# -------------------------------------------------------------
# 8. CADA OBJETO É INDEPENDENTE
# -------------------------------------------------------------
# Tudo o que aconteceu com o celular2 não afetou o celular1
celular1.mostrar_info()   # Samsung Galaxy A15 (branco) - 100% - desligado