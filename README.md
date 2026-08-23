# Análise de Dados de E-commerce com SQL (PostgreSQL)

Projeto de modelagem e análise de dados de um e-commerce fictício, criado do zero como parte dos meus estudos em SQL e banco de dados relacionais.

## Objetivo

Praticar modelagem de banco de dados relacional, criação de tabelas com integridade referencial e escrita de queries SQL para responder perguntas de negócio, como vendas por período, produtos mais vendidos e comportamento de clientes.

## Tecnologias utilizadas

- **PostgreSQL** — banco de dados relacional
- **Python** (biblioteca Faker) — geração de dados fictícios
- **Git/GitHub** — versionamento

## Estrutura do banco de dados

O banco é composto por 4 tabelas:

- **clientes** — dados cadastrais dos clientes
- **produtos** — catálogo de produtos, com categoria e preço
- **pedidos** — pedidos feitos pelos clientes, com status (pendente, concluído, cancelado)
- **itens_pedido** — itens que compõem cada pedido, ligando pedidos a produtos

O schema completo (com as chaves primárias, chaves estrangeiras e restrições) está no arquivo [`schema.sql`](./schema.sql).

## Como reproduzir este projeto

1. Crie um banco PostgreSQL local (ex: `ecommerce_projeto`)
2. Rode o script [`schema.sql`](./schema.sql) para criar as 4 tabelas
3. Instale a dependência do gerador de dados:
4. Rode o script de geração de dados:
5. Isso vai gerar o arquivo `dados_ecommerce.sql` com os `INSERT`s. Rode esse arquivo no seu banco para popular as tabelas.

## Principais queries de análise

**1. Total de clientes cadastrados**
```sql
SELECT COUNT(*) FROM clientes;
```
Resultado: 50 clientes.

**2. Produtos ordenados por preço (do mais caro ao mais barato)**
```sql
SELECT nome_prod, preco_prod
FROM produtos
ORDER BY preco_prod DESC;
```

**3. Pedidos por status**
```sql
SELECT status, COUNT(*)
FROM pedidos
GROUP BY status;
```
Resultado: 111 concluídos, 21 pendentes, 18 cancelados — a maioria das vendas é finalizada com sucesso.

**4. Ticket médio (valor médio por pedido)**
```sql
SELECT ROUND(AVG(total_pedido), 2)
FROM (
    SELECT pedido_id, SUM(quantidade * preco_unitario) AS total_pedido
    FROM itens_pedido
    GROUP BY pedido_id
) AS subconsulta;
```
Resultado: R$ 5.008,74 por pedido. Essa query usa uma **subquery**: primeiro calcula o valor total de cada pedido individualmente, depois tira a média desses totais.

**5. Top 5 produtos mais vendidos (em unidades)**
```sql
SELECT nome_prod, SUM(quantidade) AS somado
FROM produtos
JOIN itens_pedido ON itens_pedido.produto_id = produtos.id_prod
GROUP BY nome_prod
ORDER BY somado DESC
LIMIT 5;
```
Usa **JOIN** para trazer o nome do produto (que fica na tabela `produtos`) junto com a quantidade vendida (que fica em `itens_pedido`).

**6. Pedidos com o nome do cliente**
```sql
SELECT id_pedidos, data_pedidos, nome
FROM pedidos
JOIN clientes ON clientes.id = pedidos.cliente_id;
```
Lista cada pedido junto com o nome do cliente que o fez, unindo as tabelas `pedidos` e `clientes`.

## Sobre o projeto

Este projeto foi desenvolvido manualmente, tabela por tabela, como parte do meu processo de aprendizado em SQL — incluindo decisões sobre tipos de dados, restrições de integridade (`NOT NULL`, `CHECK`, `REFERENCES`) e o porquê de cada escolha de modelagem.
