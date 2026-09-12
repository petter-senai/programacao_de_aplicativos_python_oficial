# Funções em Python

Este material apresenta o conceito de funções em Python e sua importância na organização e reutilização de código.

As funções permitem dividir um programa em partes menores, cada uma responsável por realizar uma determinada tarefa. Esse recurso facilita a leitura, a manutenção e a reutilização do código.

## Índice

1. [Introdução](#1-introdução)
2. [O que é uma Função?](#2-o-que-é-uma-função)
3. [Criando uma Função](#3-criando-uma-função)
4. [Funções com Parâmetros](#4-funções-com-parâmetros)

   * 4.1. Um Parâmetro
   * 4.2. Mais de um Parâmetro
5. [Funções com Cálculos](#5-funções-com-cálculos)
6. [Retornando Valores com `return`](#6-retornando-valores-com-return)
7. [Utilizando o Retorno em Outros Cálculos](#7-utilizando-o-retorno-em-outros-cálculos)
8. [Funções com Condições](#8-funções-com-condições)
9. [Funções com Entrada de Dados](#9-funções-com-entrada-de-dados)
10. [Parâmetros com Valores Padrão](#10-parâmetros-com-valores-padrão)
11. [Variáveis Dentro de Funções](#11-variáveis-dentro-de-funções)
12. [Funções com Listas](#12-funções-com-listas)
13. [Funções com Dicionários](#13-funções-com-dicionários)
14. [Utilizando Várias Funções](#14-utilizando-várias-funções)
15. [Exemplo Prático: Sistema de Notas](#15-exemplo-prático-sistema-de-notas)
16. [Atividade](#16-atividade)

* 16.1. Calculadora com Funções

17. [Resumo](#17-resumo)

---

# 1. Introdução

Durante o desenvolvimento de um programa, algumas tarefas precisam ser realizadas várias vezes.

Imagine, por exemplo, um sistema que precisa calcular a média de vários alunos.

Sem funções, poderíamos acabar repetindo o mesmo código diversas vezes.

Com funções, podemos criar uma solução uma única vez:

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
```

Depois, podemos utilizar essa função sempre que precisarmos calcular uma média.

As funções ajudam a:

* Organizar o programa.
* Evitar repetição de código.
* Facilitar a manutenção.
* Reutilizar funcionalidades.
* Dividir um problema grande em partes menores.
* Tornar o código mais fácil de entender.

---

# 2. O que é uma Função?

Uma função é um **bloco de código criado para realizar uma determinada tarefa**.

Uma função pode ser criada uma vez e chamada várias vezes durante o programa.

Podemos imaginar uma função como uma pequena máquina:

```text
Entrada
   ↓
 FUNÇÃO
   ↓
Processamento
   ↓
Resultado
```

Por exemplo:

```text
Números → Função somar() → Resultado
```

Essa ideia permite dividir um programa em várias pequenas funcionalidades.

---

# 3. Criando uma Função

Em Python, utilizamos a palavra-chave `def` para criar uma função.

```python
def saudacao():
    print("Olá, seja bem-vindo!")
```

Nesse exemplo, criamos uma função chamada `saudacao`.

Para executar a função, precisamos chamá-la:

```python
saudacao()
```

Podemos chamar a mesma função várias vezes:

```python
saudacao()
saudacao()
saudacao()
```

O código da função é definido uma vez, mas pode ser reutilizado diversas vezes.

---

# 4. Funções com Parâmetros

Uma função pode receber informações para realizar sua tarefa.

Essas informações são chamadas de **parâmetros**.

## 4.1. Um Parâmetro

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Agora podemos enviar diferentes nomes:

```python
saudacao("Ana")
saudacao("Carlos")
saudacao("João")
```

O parâmetro `nome` recebe o valor enviado quando a função é chamada.

Podemos representar isso da seguinte maneira:

```text
"João"
   ↓
saudacao(nome)
   ↓
"Olá, João!"
```

---

## 4.2. Mais de um Parâmetro

Uma função pode receber vários parâmetros.

```python
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
```

Chamando a função:

```python
apresentar("Maria", 17)
```

Nesse caso:

```text
nome → Maria
idade → 17
```

Os parâmetros permitem que uma mesma função trabalhe com diferentes informações.

---

# 5. Funções com Cálculos

As funções também podem realizar cálculos.

```python
def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
```

Podemos utilizar a função:

```python
somar(10, 5)
somar(20, 30)
```

O resultado será:

```text
Resultado: 15
Resultado: 50
```

Nesse caso, a função realiza o cálculo e apresenta o resultado.

---

# 6. Retornando Valores com `return`

Uma função pode devolver um resultado utilizando a palavra-chave `return`.

```python
def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
```

Agora podemos armazenar o resultado retornado pela função:

```python
resultado = somar(10, 5)

print(resultado)
```

O `return` é diferente do `print()`.

### `print()`

Mostra uma informação na tela.

### `return`

Devolve uma informação para quem chamou a função.

Por exemplo:

```python
def somar(a, b):
    return a + b
```

A função pode ser utilizada em diferentes situações:

```python
resultado = somar(10, 5)

print(resultado)
```

---

# 7. Utilizando o Retorno em Outros Cálculos

Um valor retornado por uma função pode ser utilizado posteriormente.

```python
def somar(numero1, numero2):
    return numero1 + numero2


resultado = somar(10, 5)

multiplicacao = resultado * 2

print(multiplicacao)
```

Nesse exemplo:

```text
10 + 5
 ↓
15
 ↓
15 × 2
 ↓
30
```

O `return` permite que o resultado de uma função seja utilizado em outras partes do programa.

---

# 8. Funções com Condições

Uma função também pode utilizar estruturas condicionais.

```python
def verificar_aprovacao(nota):

    if nota >= 7:
        return "Aprovado"

    elif nota >= 5:
        return "Recuperação"

    else:
        return "Reprovado"
```

Podemos chamar a função:

```python
situacao = verificar_aprovacao(8)

print(situacao)
```

Resultado:

```text
Aprovado
```

A função recebe uma nota, verifica uma condição e retorna a situação correspondente.

---

# 9. Funções com Entrada de Dados

Uma função também pode solicitar informações diretamente ao usuário.

```python
def cadastrar_aluno():

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))

    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
```

Para executar:

```python
cadastrar_aluno()
```

Nesse exemplo, a própria função é responsável por:

1. Solicitar o nome.
2. Solicitar a idade.
3. Apresentar as informações.

Embora seja possível utilizar `input()` dentro de funções, em programas maiores é importante separar as responsabilidades do código sempre que isso melhorar sua organização.

---

# 10. Parâmetros com Valores Padrão

Podemos definir um valor padrão para um parâmetro.

```python
def saudacao(nome="Aluno"):
    print(f"Olá, {nome}!")
```

Se fornecermos um nome:

```python
saudacao("Carlos")
```

Resultado:

```text
Olá, Carlos!
```

Se não fornecermos:

```python
saudacao()
```

Resultado:

```text
Olá, Aluno!
```

O valor `"Aluno"` é utilizado automaticamente quando nenhum argumento é informado.

---

# 11. Variáveis Dentro de Funções

Uma variável criada dentro de uma função normalmente pertence ao contexto daquela função.

```python
def calcular():

    numero1 = 10
    numero2 = 20

    resultado = numero1 + numero2

    print(resultado)


calcular()
```

As variáveis:

```text
numero1
numero2
resultado
```

foram criadas dentro da função.

Isso significa que elas não devem ser tratadas como variáveis disponíveis automaticamente em todo o programa.

Esse conceito está relacionado ao **escopo das variáveis**.

---

# 12. Funções com Listas

As funções podem receber listas como parâmetros.

```python
def calcular_media(notas):

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media
```

Podemos utilizar a função:

```python
notas = [8, 7, 9, 10]

media = calcular_media(notas)

print(f"Média: {media:.1f}")
```

Nesse caso, a lista é enviada para a função:

```text
[8, 7, 9, 10]
        ↓
calcular_media()
        ↓
   média = 8.5
```

Esse recurso é muito útil para trabalhar com conjuntos de dados.

---

# 13. Funções com Dicionários

Também podemos enviar dicionários para funções.

```python
def exibir_aluno(aluno):

    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Curso: {aluno['curso']}")
```

Podemos criar um dicionário:

```python
aluno = {
    "nome": "João",
    "idade": 18,
    "curso": "Informática"
}
```

E enviar para a função:

```python
exibir_aluno(aluno)
```

A função recebe o dicionário e acessa suas informações utilizando as respectivas chaves.

---

# 14. Utilizando Várias Funções

Um programa pode possuir várias funções, cada uma responsável por uma tarefa.

Por exemplo, podemos criar uma calculadora:

```python
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b
```

Depois podemos utilizar todas elas:

```python
numero1 = 20
numero2 = 5

print("Soma:", somar(numero1, numero2))
print("Subtração:", subtrair(numero1, numero2))
print("Multiplicação:", multiplicar(numero1, numero2))
print("Divisão:", dividir(numero1, numero2))
```

Cada função possui uma responsabilidade específica.

Essa organização facilita a compreensão e a manutenção do programa.

---

# 15. Exemplo Prático: Sistema de Notas

Podemos combinar funções, entrada de dados e estruturas condicionais para criar um pequeno sistema de notas.

Primeiro, criamos uma função para calcular a média:

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
```

Depois, criamos outra função para verificar a situação:

```python
def verificar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"
```

Agora podemos utilizar as funções no programa principal:

```python
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)
situacao = verificar_situacao(media)

print(f"\nAluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
```

O funcionamento pode ser representado assim:

```text
        Dados do aluno
              ↓
      calcular_media()
              ↓
           Média
              ↓
     verificar_situacao()
              ↓
          Situação
              ↓
        Resultado final
```

Nesse exemplo, cada função possui uma responsabilidade:

```text
calcular_media()
→ calcula a média

verificar_situacao()
→ determina a situação do aluno
```

Essa divisão torna o programa mais organizado.

---

# 16. Atividade

## 16.1. Calculadora com Funções

Crie um programa utilizando funções para realizar as operações básicas de uma calculadora.

O programa deverá possuir uma função para cada operação:

```python
somar()
subtrair()
multiplicar()
dividir()
```

Cada função deverá receber dois números como parâmetros e retornar o resultado da operação.

Exemplo:

```python
def somar(a, b):
    return a + b
```

O programa deverá:

1. Solicitar dois números ao usuário.
2. Apresentar um menu de operações.
3. Permitir que o usuário escolha a operação.
4. Chamar a função correspondente.
5. Apresentar o resultado.

Exemplo de menu:

```text
===== CALCULADORA =====

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair
```

### Desafio

Depois de criar a calculadora, implemente o menu utilizando `while` e `break`.

Utilize também `if`, `elif` e `else` para identificar a operação escolhida.

O objetivo é integrar os conteúdos estudados anteriormente com o conceito de funções.

---

# 17. Resumo

## O que é uma função?

É um bloco de código criado para realizar uma determinada tarefa.

```python
def saudacao():
    print("Olá!")
```

## Parâmetros

Permitem enviar informações para uma função.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

## `return`

Permite devolver um resultado.

```python
def somar(a, b):
    return a + b
```

## Valor padrão

Permite definir um valor utilizado quando nenhum argumento é informado.

```python
def saudacao(nome="Aluno"):
    print(f"Olá, {nome}!")
```

## Funções e estruturas de dados

Funções podem receber listas:

```python
def calcular_media(notas):
    ...
```

E também dicionários:

```python
def exibir_aluno(aluno):
    ...
```

## Principais conceitos

| Conceito     | Função                                      |
| ------------ | ------------------------------------------- |
| `def`        | Cria uma função                             |
| Parâmetro    | Recebe uma informação                       |
| Argumento    | Valor enviado para a função                 |
| `return`     | Retorna um resultado                        |
| Valor padrão | Define um valor automático                  |
| Escopo       | Define onde uma variável pode ser utilizada |

O uso de funções é um passo importante para transformar programas grandes em partes menores, organizadas e reutilizáveis. A partir desse conceito, torna-se possível desenvolver aplicações mais estruturadas e avançar para temas como módulos, bibliotecas, tratamento de erros e programação orientada a objetos.
