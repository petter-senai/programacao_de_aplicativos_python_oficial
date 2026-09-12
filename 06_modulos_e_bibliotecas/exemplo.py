# ============================================================
# AULA: FUNÇÕES EM PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. O QUE É UMA FUNÇÃO?
# ------------------------------------------------------------

# Funções são blocos de código criados para realizar
# uma determinada tarefa.
#
# Uma função pode ser criada uma vez e utilizada
# várias vezes no programa.


# ------------------------------------------------------------
# 2. CRIANDO UMA FUNÇÃO
# ------------------------------------------------------------

# Utilizamos a palavra-chave def para criar uma função.

def saudacao():
    print("Olá, seja bem-vindo!")


# Para executar a função, basta chamá-la pelo nome.

saudacao()


# ------------------------------------------------------------
# 3. FUNÇÃO COM PARÂMETRO
# ------------------------------------------------------------

# Podemos enviar informações para uma função
# através dos parâmetros.

def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Ana")
saudacao("Carlos")
saudacao("João")


# ------------------------------------------------------------
# 4. MAIS DE UM PARÂMETRO
# ------------------------------------------------------------

def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")


apresentar("Maria", 17)


# ------------------------------------------------------------
# 5. FUNÇÃO COM CÁLCULO
# ------------------------------------------------------------

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")


somar(10, 5)
somar(20, 30)


# ------------------------------------------------------------
# 6. RETORNANDO UM VALOR
# ------------------------------------------------------------

# A palavra return permite que a função devolva
# um resultado para quem chamou a função.

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


resultado = somar(10, 5)

print(resultado)


# ------------------------------------------------------------
# 7. UTILIZANDO O RETORNO EM OUTRO CÁLCULO
# ------------------------------------------------------------

def somar(numero1, numero2):
    return numero1 + numero2


resultado = somar(10, 5)

multiplicacao = resultado * 2

print(multiplicacao)


# ------------------------------------------------------------
# 8. FUNÇÃO PARA CALCULAR MÉDIA
# ------------------------------------------------------------

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


media = calcular_media(8, 7)

print(f"Média: {media}")


# ------------------------------------------------------------
# 9. FUNÇÃO COM CONDIÇÃO
# ------------------------------------------------------------

def verificar_aprovacao(nota):

    if nota >= 7:
        return "Aprovado"

    elif nota >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


situacao = verificar_aprovacao(8)

print(situacao)


# ------------------------------------------------------------
# 10. FUNÇÃO COM ENTRADA DE DADOS
# ------------------------------------------------------------

def cadastrar_aluno():

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))

    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")


cadastrar_aluno()


# ------------------------------------------------------------
# 11. PARÂMETROS COM VALORES PADRÃO
# ------------------------------------------------------------

# Podemos definir um valor padrão para um parâmetro.

def saudacao(nome="Aluno"):
    print(f"Olá, {nome}!")


saudacao("Carlos")
saudacao()


# ------------------------------------------------------------
# 12. VARIÁVEIS DENTRO DE FUNÇÕES
# ------------------------------------------------------------

# Uma variável criada dentro de uma função normalmente
# existe somente dentro daquela função.

def calcular():

    numero1 = 10
    numero2 = 20

    resultado = numero1 + numero2

    print(resultado)


calcular()


# ------------------------------------------------------------
# 13. FUNÇÃO UTILIZANDO UMA LISTA
# ------------------------------------------------------------

def calcular_media(notas):

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media


notas = [8, 7, 9, 10]

media = calcular_media(notas)

print(f"Média: {media:.1f}")


# ------------------------------------------------------------
# 14. FUNÇÃO COM DICIONÁRIO
# ------------------------------------------------------------

def exibir_aluno(aluno):

    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Curso: {aluno['curso']}")


aluno = {
    "nome": "João",
    "idade": 18,
    "curso": "Informática"
}

exibir_aluno(aluno)


# ------------------------------------------------------------
# 15. VÁRIAS FUNÇÕES NO MESMO PROGRAMA
# ------------------------------------------------------------

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


numero1 = 20
numero2 = 5

print("Soma:", somar(numero1, numero2))
print("Subtração:", subtrair(numero1, numero2))
print("Multiplicação:", multiplicar(numero1, numero2))
print("Divisão:", dividir(numero1, numero2))


# ------------------------------------------------------------
# 16. EXEMPLO PRÁTICO - SISTEMA DE NOTAS
# ------------------------------------------------------------

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)

print(f"\nAluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")


# ------------------------------------------------------------
# 17. EXERCÍCIO
# ------------------------------------------------------------

# Crie um programa utilizando funções para realizar
# as operações de uma calculadora.
#
# Crie uma função para cada operação:
#
# somar()
# subtrair()
# multiplicar()
# dividir()
#
# O programa deve solicitar dois números e permitir
# que o usuário escolha qual operação deseja realizar.