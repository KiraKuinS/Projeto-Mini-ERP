SELECT Produtos.descricao, SUM(Itens_Venda.quantidade) AS total_vendido, SUM(Itens_Venda.quantidade * Itens_Venda.preco_unitario) AS faturamento
FROM Itens_Venda
JOIN Produtos ON Itens_Venda.produto_id = Produtos.id
GROUP BY Produtos.descricao
ORDER BY faturamento DESC;