Caixa Eletrônico XS (Python)

Um mini–sistema de caixa eletrônico feito em Python, com validação de entrada, cálculo automático de cédulas, histórico de saques e aplicação de taxa bancária.
O projeto foi criado para treinar lógica, loops, dicionários, funções e boas práticas de código.

🚀 Funcionalidades

Sacar dinheiro com aplicação automática de taxa bancária.

Calcular a distribuição de cédulas do valor solicitado.

Validar entradas do usuário (aceita apenas números).

Listar histórico de saques já realizados.

Código simples, organizado e fácil de expandir para POO ou interfaces gráficas.

📌 Como funciona
1. Menu principal

O usuário escolhe:

1 - Sacar Dinheiro
2 - Calcular Cédulas
3 - Ver Saques

2. Saque com taxa

Aplica automaticamente a taxa definida em:

TAXA = {
    "taxa-banco": 0.30
}


O saque final é calculado por:

valor_recebido = valor_digitado * (1 - taxa)

3. Cálculo de cédulas

O algoritmo distribui o valor nas cédulas disponíveis:

[200, 100, 50, 20, 10, 5, 2]


Exemplo:

210 → 1x 200, 1x 10

4. Histórico

Todos os saques ficam guardados em uma lista.

🧠 Tecnologias e conceitos usados

Python 3

Estruturas de repetição (for, while)

Validação com .isdigit()

Dicionários e listas

Formatação com f-strings

Funções bem separadas por responsabilidade

Algoritmo guloso para cédulas (greedy algorithm)

📂 Estrutura do Código
projeto/
│
├── main.py        # código principal
├── README.md      # documentação
└── ...            # outros arquivos opcionais

🏁 Como executar

Instale o Python 3.

Baixe ou clone este repositório:

git clone https://github.com/{Carlos-coder-c}/{Caixa-Eletronico-em-Python}.git


Execute:

python main.py

📈 Possíveis evoluções

Migrar para POO (classes: CaixaEletronico, Cliente, Saque…).

Criar interface gráfica com Tkinter.

Adicionar limites de saque.

Salvar histórico em arquivo JSON.

Implementar sistema de login.

📄 Licença

Este projeto é livre para estudo e modificação.
