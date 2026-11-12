SELECT descricao, quantidade_estoque
FROM Produtos
WHERE quantidade_estoque <= 10
ORDER BY quantidade_estoque ASC;