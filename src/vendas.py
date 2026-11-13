import sqlite3

def buscar_produto(produto_id):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    conexao.close()
    return produto

def cadastrar_cliente(nome, cpf_cnpj):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO Clientes (nome, cpf_cnpj) VALUES (?, ?)",
            (nome, cpf_cnpj),
        )
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        conexao.rollback()
        return False
    finally:
        conexao.close()

def validar_venda(produto_id, quantidade):
    produto = buscar_produto(produto_id)

    if produto is None:
        return False, "Produto não encontrado!"

    if quantidade <= 0:
        return False, "Quantidade inválida"

    if (produto[3]) < quantidade:
        return False, "Estoque insuficiente"

    else :
        return True, "OK"

def calcular_total(preco, quantidade):
    return preco * quantidade

def criar_venda_com_item(cliente_id, produto_id, quantidade, preco):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()
    conexao.execute("PRAGMA foreign_keys = ON")

    total = calcular_total(preco, quantidade)

    try:

        cursor.execute(
            "INSERT INTO Vendas (cliente_id, valor_total) VALUES (?, ?)",
            (cliente_id, total),
        )
        venda_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO Itens_Venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
            (venda_id, produto_id, quantidade, preco),
        )
        cursor.execute(
            "UPDATE Produtos SET quantidade_estoque = quantidade_estoque - ? WHERE id = ?",
            (quantidade, produto_id),
        )
        conexao.commit()
        return True, "Venda realizada com sucesso"
    except sqlite3.IntegrityError:
        conexao.rollback()
        return False, "Erro ao registrar venda"
    finally:
        conexao.close()

def realizar_venda(cliente_id, produto_id, quantidade):
    ok, mensagem = validar_venda(produto_id, quantidade)

    if not ok:
        return False, mensagem

    produto = buscar_produto(produto_id)
    preco = produto[2]

    return criar_venda_com_item(cliente_id, produto_id, quantidade, preco)

#if __name__ == "__main__":
    print(realizar_venda(1, 3, 1))