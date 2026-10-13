# Módulos e Bibliotecas em Python

Este material apresenta o conceito de **módulos e bibliotecas em Python**, mostrando como utilizar funcionalidades prontas, importar recursos específicos e criar módulos próprios para organizar e reutilizar código.

## Índice

1. [Introdução](#1-introdução)
2. [O que é um Módulo?](#2-o-que-é-um-módulo)
3. [Importando um Módulo](#3-importando-um-módulo)
4. [Módulo `math`](#4-módulo-math)

   * 4.1. `sqrt()`
   * 4.2. `pow()`
   * 4.3. `ceil()`
   * 4.4. `floor()`
   * 4.5. `pi`
5. [Importando Funções Específicas](#5-importando-funções-específicas)
6. [Utilizando Apelidos com `as`](#6-utilizando-apelidos-com-as)
7. [Módulo `random`](#7-módulo-random)

   * 7.1. `randint()`
   * 7.2. `choice()`
8. [Módulo `datetime`](#8-módulo-datetime)
9. [Criando um Módulo Próprio](#9-criando-um-módulo-próprio)
10. [Importando Funções de um Módulo Próprio](#10-importando-funções-de-um-módulo-próprio)
11. [O que são Bibliotecas?](#11-o-que-são-bibliotecas)
12. [Bibliotecas Externas](#12-bibliotecas-externas)
13. [Instalando Bibliotecas com `pip`](#13-instalando-bibliotecas-com-pip)
14. [Exemplos Práticos](#14-exemplos-práticos)

* 14.1. Número Aleatório
* 14.2. Sorteio de Alunos
* 14.3. Calculadora
* 14.4. Data e Hora Atual

15. [Resumo](#15-resumo)

---

# 1. Introdução

Durante o desenvolvimento de um sistema, nem sempre precisamos criar tudo do zero.

Python possui diversos recursos que já estão prontos e podem ser utilizados em nossos programas.

Por exemplo, se precisamos calcular uma raiz quadrada, podemos utilizar uma função que já existe no módulo `math`.

```python id="7p9w2k"
import math

numero = 25

raiz = math.sqrt(numero)

print(raiz)
```

Em vez de desenvolver manualmente todo o cálculo, podemos utilizar uma funcionalidade já disponível.

Os módulos e bibliotecas ajudam a:

* Reutilizar código.
* Evitar programação desnecessária.
* Organizar projetos.
* Utilizar funcionalidades prontas.
* Dividir sistemas em diferentes arquivos.
* Ampliar os recursos disponíveis no Python.

---

# 2. O que é um Módulo?

Um **módulo** é um arquivo Python que contém código que pode ser utilizado em outros programas.

Por exemplo, podemos ter um arquivo:

```text
calculadora.py
```

Dentro dele podemos criar funções:

```python id="q7m8x3"
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b
```

Outro arquivo poderá importar essas funções e utilizá-las.

Isso permite separar o código em diferentes arquivos e responsabilidades.

Podemos imaginar:

```text
Programa principal
       |
       v
   calculadora.py
       |
       +-- somar()
       |
       +-- subtrair()
```

---

# 3. Importando um Módulo

Para importar um módulo, utilizamos a palavra-chave `import`.

Por exemplo:

```python id="n6k3p4"
import math
```

Depois de importar o módulo, podemos utilizar seus recursos.

```python id="9l3f8a"
import math

numero = 25

raiz = math.sqrt(numero)

print(raiz)
```

A estrutura:

```text
math.sqrt()
```

significa:

```text
math → módulo
sqrt → função
```

---

# 4. Módulo `math`

O módulo `math` disponibiliza diversas funções e constantes matemáticas.

Para utilizá-lo:

```python id="q5n8w2"
import math
```

---

## 4.1. `sqrt()`

A função `sqrt()` calcula a raiz quadrada.

```python id="4c6q9e"
import math

print(math.sqrt(16))
```

Resultado:

```text
4.0
```

---

## 4.2. `pow()`

A função `pow()` pode ser utilizada para calcular uma potência.

``
