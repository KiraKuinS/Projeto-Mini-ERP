# 📦 Projeto Mini-ERP: Gestão de Vendas e Estoque

Sistema backend de gerenciamento de vendas, controle de estoque e relatórios gerenciais desenvolvido em **Python** e **SQLite**. O projeto simula a lógica de negócio de um ERP comercial, focando em integridade relacional, validação de transações e estruturação profissional de código para portfólio.

---

## 🚀 Funcionalidades

- **Gestão de Clientes:** Cadastro de clientes com tratamento de unicidade para CPF/CNPJ.
- **Controle de Estoque Inteligente:** Validação prévia de disponibilidade, baixa automática e verificação de estoque crítico.
- **Processamento de Vendas:** Lançamento de vendas vinculadas a itens transacionais (`INSERT` múltiplos e controle de chaves estrangeiras).
- **Relatórios Gerenciais em SQL:** Consultas analíticas para faturamento diário, ranking de produtos mais vendidos e alertas de reposição.

---

## 📂 Estrutura do Repositório

```text
Projeto-Mini-ERP/
├── src/
│   └── vendas.py             # Script principal de regras de negócio, validações e transações de vendas
├── sql/
│   ├── ESTOQUE_CRITICO.sql   # Consulta SQL para alerta de itens com baixo estoque (ORDER BY ASC)
│   ├── FATURAMENTO_DIA.sql   # Consulta SQL para faturamento agrupado por data
│   └── FATURAMENTO_PRODUTO.sql # Consulta SQL de faturamento por produto (JOIN, GROUP BY e DESC)
├── .gitignore                # Arquivos ignorados pelo Git (banco .db, cache, etc.)
├── IDEA_MELHORIAS.txt        # Anotações de melhorias futuras e ideias de negócio
└── README.md                 # Documentação oficial do projeto
(Nota: O arquivo de banco de dados .db local não é versionado por boas práticas; a estrutura relacional e os relatórios são recriados a partir dos scripts .sql.)

🛠️ Tecnologias Utilizadas
Python 3: Lógica de aplicação, tratamento de exceções e automação de banco de dados.

SQLite: Banco de dados relacional embarcado e leve.

SQL: Consultas analíticas (JOIN, GROUP BY, SUM, ORDER BY).

Git & GitHub: Versionamento e organização de código.

⚙️ Como Executar o Projeto
Clone o repositório:

Bash
git clone [https://github.com/KiraKuinS/Projeto-Mini-ERP.git](https://github.com/KiraKuinS/Projeto-Mini-ERP.git)
cd Projeto-Mini-ERP
Configure o Banco de Dados:

Utilize o DB Browser for SQLite ou o terminal para criar o banco e as tabelas com base nos arquivos da pasta sql/.

Execute o script de vendas:

Bash
python src/vendas.py
💡 Próximos Passos (Melhorias Futuras)
[ ] Estoque Mínimo Dinâmico: Adicionar uma coluna de estoque mínimo individualizado na tabela de produtos.

[ ] Portabilidade para ADVPL / TL++: Traduzir a lógica de negócio e as consultas SQL para o ambiente TOTVS Protheus.

[ ] Camada de Interface: Desenvolver uma interface gráfica simples para agilizar o lançamento de pedidos.


---

Depois de salvar o arquivo no VS Code, basta dar os comandos finais no terminal para atualizar o seu GitHub:

```powershell
git add README.md
git commit -m "docs: atualiza readme com estrutura real do projeto"
git push origin main