# 🎓 Sistema de Registro de Notas

Projeto universitário em Python para registrar notas por disciplina, calcular médias e salvar o histórico dos alunos.

## Estrutura do Projeto

```
meu_projeto/
├── main.py        → Menu principal e loop do programa
├── funcoes.py     → Lógica específica (cadastrar, listar, calcular)
├── utils.py       → Validações e funções auxiliares
├── dados/
│   └── registro.txt  → Arquivo de persistência (gerado automaticamente)
├── .gitignore
└── README.md
```

## Como executar

```bash
python main.py
```

> Nenhuma biblioteca externa necessária. Usa apenas a biblioteca padrão do Python.

## Funcionalidades

| Opção | Ação |
|-------|------|
| 1 | Cadastrar aluno (nome, matrícula, curso) |
| 2 | Inserir notas por disciplina |
| 3 | Ver histórico completo com médias |
| 4 | Listar todos os alunos |
| 5 | Remover uma disciplina |

## Critério de aprovação

| Média | Situação |
|-------|----------|
| ≥ 7.0 | ✅ Aprovado |
| ≥ 5.0 | ⚠️ Recuperação |
| < 5.0 | ❌ Reprovado |

## Persistência

Os dados são salvos automaticamente em `dados/registro.txt` no formato JSON sempre que uma alteração é feita.
