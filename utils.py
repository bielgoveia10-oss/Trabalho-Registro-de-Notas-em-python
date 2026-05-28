# ============================================================
# utils.py — Validações e funções auxiliares
# Responsabilidade: funções genéricas reutilizáveis em
# qualquer parte do projeto (validar dados, formatar textos,
# calcular médias, determinar situação do aluno).
# ============================================================

import json
import os

# Caminho do arquivo de persistência dentro da pasta dados/
ARQUIVO_DADOS = os.path.join("dados", "registro.txt")


# ------------------------------------------------------------
# FUNÇÕES DE PERSISTÊNCIA (leitura e escrita em disco)
# ------------------------------------------------------------

def carregar_dados():
    # Lê o arquivo registro.txt e converte o JSON para dicionário Python.
    # Se o arquivo não existir ainda, retorna um dicionário vazio.
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_dados(dados):
    # Garante que a pasta dados/ existe antes de tentar salvar.
    os.makedirs("dados", exist_ok=True)

    # Converte o dicionário Python para JSON e salva no arquivo.
    # indent=4 deixa o arquivo legível para humanos.
    # ensure_ascii=False preserva acentos e caracteres especiais.
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print("\n  ✅ Dados salvos em dados/registro.txt")


# ------------------------------------------------------------
# FUNÇÕES DE CÁLCULO
# ------------------------------------------------------------

def calcular_media(notas):
    # Calcula a média aritmética simples de uma lista de notas.
    # Retorna 0.0 caso a lista esteja vazia (evita divisão por zero).
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def situacao_aluno(media):
    # Determina a situação do aluno com base na média calculada.
    # Critério: aprovado >= 7.0 | recuperação >= 5.0 | reprovado < 5.0
    if media >= 7.0:
        return "✅ APROVADO"
    elif media >= 5.0:
        return "⚠️  RECUPERAÇÃO"
    else:
        return "❌ REPROVADO"


# ------------------------------------------------------------
# FUNÇÕES DE FORMATAÇÃO / EXIBIÇÃO
# ------------------------------------------------------------

def linha_separadora(char="─", tamanho=47):
    # Gera uma linha horizontal para separar seções no terminal.
    # O caractere e o tamanho podem ser customizados.
    print("  " + char * tamanho)


def cabecalho(titulo):
    # Exibe um cabeçalho padronizado para cada tela do sistema.
    print("\n" + "=" * 49)
    print(f"   {titulo.upper()}")
    print("=" * 49)


def validar_nota(entrada):
    # Tenta converter a entrada do usuário para float.
    # Aceita tanto ponto quanto vírgula como separador decimal.
    # Retorna a nota se válida (0.0 a 10.0), ou None se inválida.
    try:
        nota = float(entrada.replace(",", "."))
        if 0.0 <= nota <= 10.0:
            return nota
        return None  # Fora do intervalo permitido
    except ValueError:
        return None  # Não é um número
