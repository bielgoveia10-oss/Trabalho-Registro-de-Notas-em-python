# ============================================================
# funcoes.py — Lógica específica do sistema
# Responsabilidade: cada função aqui representa uma ação
# concreta do sistema (cadastrar aluno, inserir notas, etc.).
# Todas usam utilitários de utils.py e recebem/retornam
# o dicionário principal de dados.
# ============================================================

from datetime import datetime

# Importa todas as funções auxiliares do módulo utils
from utils import (
    salvar_dados,
    calcular_media,
    situacao_aluno,
    linha_separadora,
    cabecalho,
    validar_nota,
)


# ------------------------------------------------------------
# FUNÇÃO 1 — Cadastrar novo aluno
# ------------------------------------------------------------

def cadastrar_aluno(dados):
    # Coleta nome, matrícula e curso do novo aluno.
    # A matrícula é usada como chave única no dicionário de dados.
    cabecalho("Cadastro de Aluno")

    nome = input("  Nome do aluno: ").strip()
    if not nome:
        print("  ❌ Nome não pode ser vazio.")
        return dados

    matricula = input("  Matrícula    : ").strip()
    if not matricula:
        print("  ❌ Matrícula não pode ser vazia.")
        return dados

    # Verifica se a matrícula já está cadastrada para evitar duplicatas
    if matricula in dados:
        print(f"  ⚠️  Matrícula '{matricula}' já existe no sistema.")
        return dados

    curso = input("  Curso        : ").strip()

    # Monta a estrutura de dados do aluno.
    # 'disciplinas' começa vazio e será preenchido ao inserir notas.
    dados[matricula] = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso,
        "disciplinas": {},
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    salvar_dados(dados)
    print(f"\n  🎓 Aluno '{nome}' cadastrado com sucesso!")
    return dados


# ------------------------------------------------------------
# FUNÇÃO 2 — Inserir notas por disciplina
# ------------------------------------------------------------

def inserir_notas(dados):
    # Permite adicionar notas a uma disciplina de um aluno.
    # Se a disciplina não existir, ela é criada automaticamente.
    cabecalho("Inserir Notas")

    matricula = input("  Matrícula do aluno: ").strip()
    if matricula not in dados:
        print("  ❌ Aluno não encontrado.")
        return dados

    aluno = dados[matricula]
    print(f"\n  Aluno : {aluno['nome']}")
    print(f"  Curso : {aluno['curso']}")

    disciplina = input("\n  Nome da disciplina: ").strip()
    if not disciplina:
        print("  ❌ Nome da disciplina inválido.")
        return dados

    # Cria a lista de notas da disciplina se ainda não existir
    if disciplina not in aluno["disciplinas"]:
        aluno["disciplinas"][disciplina] = []

    print(f"\n  Digite as notas de '{disciplina}' (ENTER vazio para encerrar):")
    print("  Escala aceita: 0.0 até 10.0\n")

    # Contador começa após as notas já existentes (caso haja adição posterior)
    contador = len(aluno["disciplinas"][disciplina]) + 1

    while True:
        entrada = input(f"    Nota {contador}: ").strip()

        # ENTER vazio encerra a entrada de notas
        if entrada == "":
            break

        nota = validar_nota(entrada)  # Valida via utils.py

        if nota is not None:
            aluno["disciplinas"][disciplina].append(nota)
            contador += 1
        else:
            print("    ⚠️  Valor inválido. Use números entre 0.0 e 10.0.")

    # Exibe um resumo logo após inserir as notas
    notas = aluno["disciplinas"][disciplina]
    if notas:
        media = calcular_media(notas)
        print(f"\n  📊 Notas registradas : {notas}")
        print(f"  📈 Média calculada   : {media:.2f} — {situacao_aluno(media)}")

    salvar_dados(dados)
    return dados


# ------------------------------------------------------------
# FUNÇÃO 3 — Exibir histórico completo de um aluno
# ------------------------------------------------------------

def exibir_historico(dados):
    # Mostra uma tabela com todas as disciplinas, notas,
    # médias e situação do aluno, além da média geral.
    cabecalho("Histórico do Aluno")

    matricula = input("  Matrícula do aluno: ").strip()
    if matricula not in dados:
        print("  ❌ Aluno não encontrado.")
        return

    aluno = dados[matricula]

    # Cabeçalho com dados pessoais do aluno
    linha_separadora()
    print(f"  Nome     : {aluno['nome']}")
    print(f"  Matrícula: {aluno['matricula']}")
    print(f"  Curso    : {aluno['curso']}")
    print(f"  Cadastro : {aluno['data_cadastro']}")
    linha_separadora()

    disciplinas = aluno["disciplinas"]

    if not disciplinas:
        print("\n  Nenhuma nota registrada ainda.")
        return

    # Cabeçalho da tabela de notas
    print(f"\n  {'DISCIPLINA':<22} {'NOTAS':<14} {'MÉDIA':>5}  SITUAÇÃO")
    linha_separadora()

    medias_gerais = []  # Acumula médias para calcular a média geral ao final

    for disciplina, notas in disciplinas.items():
        if notas:
            media = calcular_media(notas)
            medias_gerais.append(media)

            # Trunca a exibição das notas se for muito longa
            notas_str = ", ".join(str(n) for n in notas)
            if len(notas_str) > 14:
                notas_str = notas_str[:12] + "…"

            situacao = situacao_aluno(media)
            print(f"  {disciplina:<22} {notas_str:<14} {media:>5.2f}  {situacao}")
        else:
            print(f"  {disciplina:<22} {'—':<14} {'—':>5}  Sem notas")

    # Exibe a média geral (média das médias de cada disciplina)
    if medias_gerais:
        media_geral = calcular_media(medias_gerais)
        linha_separadora()
        print(f"  {'MÉDIA GERAL':<37} {media_geral:>5.2f}  {situacao_aluno(media_geral)}")

    linha_separadora()


# ------------------------------------------------------------
# FUNÇÃO 4 — Listar todos os alunos cadastrados
# ------------------------------------------------------------

def listar_alunos(dados):
    # Exibe uma listagem simples com matrícula, nome e curso
    # de todos os alunos presentes no arquivo de dados.
    cabecalho("Lista de Alunos")

    if not dados:
        print("  Nenhum aluno cadastrado.")
        return

    print(f"\n  {'MATRÍCULA':<12} {'NOME':<24} CURSO")
    linha_separadora()

    for matricula, aluno in dados.items():
        print(f"  {matricula:<12} {aluno['nome']:<24} {aluno['curso']}")

    linha_separadora()
    print(f"  Total: {len(dados)} aluno(s) cadastrado(s)")


# ------------------------------------------------------------
# FUNÇÃO 5 — Remover uma disciplina de um aluno
# ------------------------------------------------------------

def remover_disciplina(dados):
    # Lista as disciplinas do aluno e permite remover uma delas.
    # Pede confirmação antes de deletar para evitar exclusão acidental.
    cabecalho("Remover Disciplina")

    matricula = input("  Matrícula do aluno: ").strip()
    if matricula not in dados:
        print("  ❌ Aluno não encontrado.")
        return dados

    aluno = dados[matricula]
    disciplinas = list(aluno["disciplinas"].keys())

    if not disciplinas:
        print("  Nenhuma disciplina cadastrada para este aluno.")
        return dados

    print(f"\n  Disciplinas de {aluno['nome']}:")
    for i, disc in enumerate(disciplinas, 1):
        print(f"    {i}. {disc}")

    try:
        opcao = int(input("\n  Número da disciplina a remover (0 = cancelar): "))
        if opcao == 0:
            print("  Operação cancelada.")
            return dados

        if 1 <= opcao <= len(disciplinas):
            disciplina = disciplinas[opcao - 1]

            # Confirmação explícita antes de remover
            confirmacao = input(f"  Confirma remoção de '{disciplina}'? (s/n): ").strip().lower()
            if confirmacao == "s":
                del aluno["disciplinas"][disciplina]
                salvar_dados(dados)
                print(f"  ✅ Disciplina '{disciplina}' removida.")
            else:
                print("  Operação cancelada.")
        else:
            print("  ❌ Número fora do intervalo.")

    except ValueError:
        # Captura caso o usuário digite algo que não seja número
        print("  ❌ Digite um número válido.")

    return dados
