# Depuração e Correção: Sistema de Cálculo de Compra

## ERROS ENCONTRADOS E CORRIGIDOS

### ❌ ERRO 1: String sem aspas (SyntaxError)
**Localização:** Linha 6  
**Código com erro:**
```python
item1 = float(input(Preço do item 1? ))
```
**Problema:** A string `"Preço do item 1?"` está sem aspas, causando um erro de sintaxe.  
**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```
**Tipo:** SyntaxError - String sem delimitadores

---

### ❌ ERRO 2: Variável string usada em operação matemática (TypeError)
**Localização:** Linha 25  
**Código com erro:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)  # TypeError aqui!
```
**Problema:** A função `input()` retorna uma string, mas o código tenta dividir por 100 sem converter para número.  
**Mensagem de erro:** `TypeError: unsupported operand type(s) for /: 'str' and 'int'`  
**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```
**Tipo:** TypeError - Tipo de dado incorreto em operação

---

### ❌ ERRO 3: F-string sem prefixo 'f' (Variável não interpolada)
**Localização:** Linha 38  
**Código com erro:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```
**Problema:** A string não tem o prefixo `f`, então `{total_item2:.2f}` é exibido literalmente em vez de ser interpolado.  
**Saída esperada:** ` Item 2:        R$ 45.00`  
**Saída obtida:** ` Item 2:        R$ {total_item2:.2f}`  
**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```
**Tipo:** LogicError - Falta de prefixo em f-string

---

### ❌ ERRO 4: Comparação de string com número (TypeError)
**Localização:** Linha 43  
**Código com erro:**
```python
desconto_cupom = (input("..."))  # É uma string
if desconto_cupom > 0:  # TypeError: '>' not supported between instances of 'str' and 'int'
```
**Problema:** Tenta comparar uma string com o número inteiro 0. Strings e números não podem ser comparados dessa forma.  
**Correção:** Converter para número (já foi feito na correção do ERRO 2)
```python
desconto_cupom = float(input("..."))
if desconto_cupom > 0:
```
**Tipo:** TypeError - Comparação entre tipos incompatíveis

---

### ❌ ERRO 5: Indentação incorreta (IndentationError)
**Localização:** Linha 44  
**Código com erro:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema:** O bloco `print()` dentro do `if` não está indentado, causando erro de sintaxe.  
**Mensagem de erro:** `IndentationError: expected an indented block`  
**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Tipo:** IndentationError - Falta de indentação

---

## RESUMO DOS ERROS

| # | Tipo | Localização | Severidade | Caractere |
|---|------|------------|-----------|-----------|
| 1 | SyntaxError | Linha 6 | Crítico | Faltam aspas |
| 2 | TypeError | Linha 24-25 | Crítico | Conversão de tipo necessária |
| 3 | LogicError | Linha 38 | Médio | Falta prefixo 'f' |
| 4 | TypeError | Linha 43 | Crítico | Comparação tipo incompatível |
| 5 | IndentationError | Linha 44 | Crítico | Indentação faltante |

---

## CÓDIGO CORRIGIDO

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programa de cálculo de total de compra com itens, impostos e descontos.
"""

# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## LIÇÕES APRENDIDAS

1. **Sempre use aspas em strings** - SyntaxError é o tipo de erro mais fácil de evitar
2. **Converta entrada do usuário** - `input()` sempre retorna string, converta conforme necessário
3. **Use f-strings corretamente** - Não esqueça do prefixo `f` para interpolação de variáveis
4. **Verifique tipos de dados** - Antes de operações matemáticas ou comparações
5. **Mantenha indentação consistente** - Blocos de código dependem de indentação correta em Python