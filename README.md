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
