# Secret_Calculator
Uma calculadora simples em Python.

Este script em **Bash** solicita seu nome e idade, em seguida, inicia uma calculadora desenvolvida em Python.

## Como Executar o Script

1. **Dê permissão de execução ao script (se necessário):**
   ```bash
   chmod +x calculadora_simples.sh

2. **Execute o script (se necessário):**
   ```bash
   ./calculadora_simples.sh

## Explicação do Código em Python

### Calculadora Python
Este script implementa uma calculadora interativa que permite realizar operações aritméticas básicas de forma contínua.

## Estrutura do Código

### Inicialização das Variáveis
- São definidas as variáveis `num1`, `num2`, `operation` e `result` para armazenar os números, a operação escolhida e o resultado do cálculo.

### Loop de Operações
- O código entra em um loop infinito, permitindo ao usuário realizar várias operações sem reiniciar o programa.
- Em cada iteração, o usuário é solicitado a:
  1. **Inserir o primeiro número**.
  2. **Inserir a operação** desejada (soma, subtração, multiplicação ou divisão).
  3. **Inserir o segundo número**.

### Execução das Operações
- O programa utiliza estruturas condicionais (`if`, `elif` e `else`) para identificar a operação escolhida:
  - Se a operação for `"+"`, soma os números.
  - Se for `"-"`, subtrai o segundo número do primeiro.
  - Se for `"*"`, multiplica os números.
  - Se for `"/"`, divide o primeiro número pelo segundo.
- Caso a operação informada não corresponda a nenhuma das operações válidas, o resultado será definido como `"Inválido"`.

### Exibição do Resultado
- Após realizar o cálculo, o resultado é exibido.
