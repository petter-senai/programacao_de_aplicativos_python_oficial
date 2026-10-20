# =============================================================
# AULAS 4 A 6 - Encapsulamento, Herança e Polimorfismo
# Projeto: sistema de funcionários de uma empresa
# =============================================================


# =============================================================
# PARTE 1: ENCAPSULAMENTO
# Proteger o salário para que ele só mude seguindo regras
# =============================================================

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome            # público: qualquer um pode ler e alterar
        self.__salario = salario    # privado: dois sublinhados

    # @property deixa ler o salário como se fosse um atributo
    # (funcionario.salario, sem parênteses), mas sem poder alterar
    @property
    def salario(self):
        return self.__salario

    # A ÚNICA forma de mudar o salário é por este método,
    # e ele tem uma regra: o aumento precisa ser positivo
    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}.")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento.")

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R$ {self.salario:.2f}")

    # Bônus padrão de qualquer funcionário: 10% do salário
    def bonus(self):
        return self.salario * 0.10


print("===== PARTE 1: ENCAPSULAMENTO =====")

ana = Funcionario("Ana", 3000)
ana.apresentar()            # Sou Ana e ganho R$ 3000.00

# Ler o salário funciona normalmente
print(ana.salario)          # 3000

# Mudar o salário só pelo método, que segue a regra
ana.dar_aumento(-20)        # Aumento inválido para Ana.
ana.dar_aumento(10)         # Ana recebeu 10% de aumento.
ana.apresentar()            # Sou Ana e ganho R$ 3300.00

# Tentar alterar o salário direto dá erro!
# O try/except "tenta" executar o código e, se der erro,
# executa o except em vez de parar o programa.
try:
    ana.salario = 1000000
except AttributeError:
    print("Não é permitido alterar o salário diretamente!")

# E o atributo privado fica escondido fora da classe
try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora.")


# =============================================================
# PARTE 2: HERANÇA
# Gerente e Estagiário SÃO funcionários: herdam tudo de Funcionario
# =============================================================

class Gerente(Funcionario):    # Gerente herda de Funcionario

    def __init__(self, nome, salario, equipe):
        # super() chama o construtor da classe mãe:
        # não precisamos repetir o código de nome e salário
        super().__init__(nome, salario)
        self.equipe = equipe    # atributo novo, só do gerente

    # Método novo, que só o gerente tem
    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe} pessoas.")


class Estagiario(Funcionario):

    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso      # atributo novo, só do estagiário


print("\n===== PARTE 2: HERANÇA =====")

bruno = Gerente("Bruno", 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de Sistemas")

# Métodos herdados: não foram escritos em Gerente nem em Estagiario,
# mas funcionam porque vêm de Funcionario
bruno.apresentar()          # Sou Bruno e ganho R$ 8000.00
caio.apresentar()           # Sou Caio e ganho R$ 1500.00
caio.dar_aumento(5)         # Caio recebeu 5% de aumento.

# Métodos e atributos novos, só das classes filhas
bruno.mostrar_equipe()      # Bruno gerencia 5 pessoas.
print(caio.curso)           # Análise de Sistemas

# isinstance confere se um objeto "é um" de certa classe
print(isinstance(bruno, Gerente))       # True
print(isinstance(bruno, Funcionario))   # True: todo gerente é funcionário
print(isinstance(ana, Gerente))         # False: nem todo funcionário é gerente


# =============================================================
# PARTE 3: POLIMORFISMO
# O mesmo método bonus(), com um jeito diferente em cada classe
# =============================================================

# Agora as classes filhas vão SOBRESCREVER o método bonus():
# escrever de novo um método que já veio da classe mãe.
# (Na aula, basta voltar nas classes da Parte 2 e acrescentar
# o bonus() nelas. Aqui elas foram reescritas para o script
# ficar organizado por partes.)

class Gerente(Funcionario):

    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    # Sobrescreve o bonus() da mãe: gerente ganha 20%
    # + R$ 100 por pessoa da equipe
    def bonus(self):
        # ATENÇÃO: aqui usamos self.salario (a property),
        # e não self.__salario. O atributo privado pertence
        # à classe Funcionario e nem as filhas acessam direto!
        return self.salario * 0.20 + self.equipe * 100


class Estagiario(Funcionario):

    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    # Sobrescreve o bonus(): estagiário recebe valor fixo
    def bonus(self):
        return 200


print("\n===== PARTE 3: POLIMORFISMO =====")

# Uma lista com objetos de classes DIFERENTES
equipe = [
    Funcionario("Ana", 3000),
    Gerente("Bruno", 8000, 5),
    Estagiario("Caio", 1500, "Análise de Sistemas"),
    Funcionario("Duda", 4200),
]

total_bonus = 0

# O laço não pergunta que tipo de funcionário é cada um:
# apenas chama bonus(), e cada objeto responde do seu jeito
for f in equipe:
    valor = f.bonus()
    total_bonus = total_bonus + valor
    # type(f).__name__ mostra o nome da classe do objeto
    print(f"{f.nome} ({type(f).__name__}): bônus de R$ {valor:.2f}")

print(f"Total de bônus da empresa: R$ {total_bonus:.2f}")