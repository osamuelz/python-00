import os
import re
from datetime import datetime

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    for j in range(9, 11):
        soma = sum(int(cpf[i]) * ((j + 1) - i) for i in range(j))
        digito = (soma * 10) % 11
        if digito == 10: digito = 0
        if digito != int(cpf[j]):
            return False
    return True

def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"
    if not re.match(padrao, data):
        return False
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def verificar_maioridade(data_nasc):
    try:
        nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
        hoje = datetime.now()
        idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
        return idade >= 18
    except:
        return False