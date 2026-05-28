# ============================================================
# main.py — Menu principal e loop do programa
# Responsabilidade: ponto de entrada do sistema. Exibe o menu,
# lê a escolha do usuário e chama a função correspondente
# em funcoes.py. Mantém o loop até o usuário optar por sair.
# ============================================================

# Importa as funções de carregamento de dados (utils.py)
from utils import carregar_dados

# Importa todas as ações disponíveis no sistema (funcoes.py)
from funcoes import (
    cadastrar_aluno,
    inserir_notas,
    exibir_historico,
    listar_alunos,
    remover_disciplina,
)


# ------------------------------------------------------------
# Função que renderiza o menu principal no terminal
# ------------------------------------------------------------

def exibir_menu():
    print("\n" + "═" * 49)
    print("     🎓 SISTEMA DE REGISTRO DE NOTAS 🎓")
    print("═" * 49)
    print("   1. Cadastrar aluno")
    print("   2. Inserir notas por disciplina")
    print("   3. Ver histórico do aluno")
    print("   4. Listar todos os alunos")
    print("   5. Remover disciplina")
    print("   0. Sair")
    print("═" * 49)
    return input("   Escolha uma opção: ").strip()


# ------------------------------------------------------------
# Função principal — loop central do programa
# ------------------------------------------------------------

def main():
    # Carrega os dados salvos em dados/registro.txt ao iniciar.
    # Se o arquivo não existir, começa com dicionário vazio.
    dados = carregar_dados()

    print("\n  Bem-vindo ao Sistema de Registro de Notas!")
    print("  Os dados são salvos automaticamente em dados/registro.txt")

    # Loop principal: fica rodando até o usuário digitar 0
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            # Cadastra um novo aluno e atualiza o dicionário dados
            dados = cadastrar_aluno(dados)

        elif opcao == "2":
            # Insere notas em uma disciplina do aluno informado
            dados = inserir_notas(dados)

        elif opcao == "3":
            # Exibe o histórico completo de notas e médias do aluno
            exibir_historico(dados)

        elif opcao == "4":
            # Lista todos os alunos cadastrados no sistema
            listar_alunos(dados)

        elif opcao == "5":
            # Remove uma disciplina (e suas notas) de um aluno
            dados = remover_disciplina(dados)

        elif opcao == "0":
            # Encerra o programa
            print("\n  Até logo! 👋\n")
            break

        else:
            # Opção digitada não corresponde a nenhum item do menu
            print("\n  ⚠️  Opção inválida. Digite um número de 0 a 5.")

        # Pausa antes de voltar ao menu, para o usuário ler a saída
        input("\n  Pressione ENTER para continuar...")


# ------------------------------------------------------------
# Ponto de entrada — garante que main() só rode quando este
# arquivo for executado diretamente (não ao ser importado)
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
