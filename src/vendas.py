import sqlite3

def buscar_produto(produto_id):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    conexao.close()
    return produto

def verificar_estoque(produto_id, quantidade):
    produto = buscar_produto(produto_id)

    if produto is None:
        return False


    if (produto[3]) >= quantidade:
        return True
    else:
        return False

def cadastrar_clientes(nome, cpf_cnpj):
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

def baixar_estoque(produto_id, quantidade):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()
    try:
        cursor.execute(
        "UPDATE Produtos SET quantidade_estoque = quantidade_estoque - ? WHERE id = ?",
        (quantidade, produto_id),
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

def criar_venda_teste(cliente_id, valor_total):
    conexao = sqlite3.connect("sql/mini_erp.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO Vendas (cliente_id, valor_total) VALUES (?, ?)",
        (cliente_id, valor_total),
    )
    venda_id = cursor.lastrowid

    conexao.commit()
    conexao.close()
    return venda_id

def calcular_total(preco, quantidade):
    return preco * quantidade

def criar_venda_com_item_teste(cliente_id, produto_id, quantidade, preco):
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

#print(criar_venda_com_item_teste(1, 3, 2, 7.0))     # com estoque
#print(criar_venda_com_item_teste(1, 3, 100, 7.0))   # sem estoque

def realizar_venda(cliente_id, produto_id, quantidade):
    ok, mensagem = validar_venda(produto_id, quantidade)

    if not ok:
        return False, mensagem

    produto = buscar_produto(produto_id)
    preco = produto[2]

    return criar_venda_com_item_teste(cliente_id, produto_id, quantidade, preco)

#print(realizar_venda(1, 3, 2))     # válida
#print(realizar_venda(1, 3, 100))   # estoque insuficiente
#print(realizar_venda(1, 999, 1))   # produto inexistente
#print(realizar_venda(1, 3, 0))     # quantidade inválida

print(realizar_venda(1, 4, 2))   # 2 Monster sem açúcar
print(realizar_venda(1, 5, 3))   # 3 Monster Original
print(realizar_venda(1, 2, 1))   # 1 Conti Cola

