# Test Assistant Code

Este projeto contém uma coleção de scripts Python simples e explicações associadas, desenvolvidos para fins de aprendizado e prática em programação Python. Inclui exemplos de algoritmos básicos, depuração de código, refatoração e documentação.

## Descrição

O projeto é dividido em módulos independentes, cada um focado em um conceito específico:

- **Verificação de números primos**: Implementação eficiente de um algoritmo para verificar se um número é primo.
- **Cálculo de compras**: Programa interativo para calcular o total de uma compra com itens, impostos e descontos.
- **Refatoração de código**: Exemplo de melhoria de código, transformando uma implementação básica em uma versão mais legível e eficiente.
- **Explicações**: Documentos Markdown com análises linha a linha dos códigos, incluindo correções de bugs comuns.

## Estrutura do Projeto

```
test-assistent-code/
├── num_primos.py              # Função para verificar números primos
├── debug.py                   # Calculadora de compras com impostos e descontos
├── refatoracao.py             # Cálculo de estatísticas refatorado
├── explicacao_num_primo.md    # Explicação detalhada do código de primos
├── explicacao_ref.md          # Explicação da refatoração
├── explicacao-debug.md        # Análise de bugs e correções no debug.py
└── README.md                  # Este arquivo
```

## Requisitos

- Python 3.6 ou superior
- Nenhum pacote adicional é necessário (usa apenas bibliotecas padrão)

## Como Usar

### Executando os Scripts

1. **Verificação de primos**:
   ```bash
   python num_primos.py
   ```
   Executa testes simples com números pré-definidos.

2. **Calculadora de compras**:
   ```bash
   python debug.py
   ```
   Segue as instruções no terminal para inserir dados do cliente e itens.

3. **Cálculo de estatísticas**:
   ```bash
   python refatoracao.py
   ```
   Calcula e exibe estatísticas de uma lista de números definida no código.

### Lendo as Explicações

Os arquivos `.md` contêm explicações detalhadas:
- `explicacao_num_primo.md`: Análise linha a linha do algoritmo de primos
- `explicacao_ref.md`: Comparação entre código original e refatorado
- `explicacao-debug.md`: Identificação e correção de erros comuns em Python

## Exemplos de Uso

### num_primos.py
```python
from num_primos import is_prime

print(is_prime(17))  # True
print(is_prime(18))  # False
```

### debug.py
Entrada interativa:
```
Qual é seu nome? João
Quantidade do item 1: 2
Preço do item 1? 10.50
...
```

Saída:
```
===============================
 Cliente: João
===============================
 Item 1:        R$ 21.00
...
 TOTAL:         R$ 45.45
===============================
```

### refatoracao.py
```
Total:   346
Média:   34.6
Máximo:  89
Mínimo:  2
```

## Conceitos Abordados

- Algoritmos básicos (primos, estatísticas)
- Tratamento de entrada/saída
- Operações matemáticas
- Estruturas de controle (loops, condicionais)
- Funções e modularização
- Documentação com docstrings (estilo Google)
- Depuração e correção de erros comuns
- Refatoração para código mais limpo e eficiente
- Uso de funções built-in do Python

## Contribuição

Este é um projeto de aprendizado pessoal. Sugestões de melhorias são bem-vindas através de issues ou pull requests.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes (se aplicável).