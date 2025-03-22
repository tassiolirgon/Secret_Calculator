# Inicialização das Variáveis
num1 = 0
num2 = 0
operation = ""
result = 0

# Coleta de Dados + Loop Infinito de Operações
while True:
  num1 = float(input("Digite o primeiro número: "))
  operation = input("Digite a operação: ")
  num2 = float(input("Digite o segundo número: "))

  # Condicionais dos Cálculos
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  else:
    result = "Inválido"

  # Visualização do Usuário
  print(num1, operation, num2, "=", result)
