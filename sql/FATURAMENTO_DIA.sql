SELECT DATE(data_venda) AS dia, COUNT(*) AS qtd_vendas, SUM(valor_total) AS faturamento
FROM Vendas
GROUP BY DATE(data_venda);