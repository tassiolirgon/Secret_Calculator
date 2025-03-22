#!/bin/bash

# Solicita o nome e a idade do usuário
echo "Digite seu nome: "
read NOME

echo "Digite sua idade: "
read IDADE

# Exibe uma mensagem de boas vindas e inicialização da calculadora
echo "Olá $NOME! você tem $IDADE anos e pode utilizar a calculadora secreta!"
echo "Iniciando..."

# Executa a calculadora Python
python3 calculadora_python.py
