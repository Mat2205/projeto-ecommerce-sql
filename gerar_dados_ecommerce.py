"""
Gera dados ficticios para o projeto de e-commerce (clientes, produtos, pedidos, itens_pedido)
e escreve os comandos INSERT em um arquivo .sql, pronto para rodar no pgAdmin.

Como usar:
1. pip install faker
2. python gerar_dados_ecommerce.py
3. Abra o arquivo dados_ecommerce.sql gerado e cole o conteudo na Query Tool do pgAdmin
"""

import random
from faker import Faker

fake = Faker("pt_BR")
random.seed(42)

N_CLIENTES = 50
N_PRODUTOS = 20
N_PEDIDOS = 150
MAX_ITENS_POR_PEDIDO = 4

CATEGORIAS = ["Eletronicos", "Roupas", "Casa", "Esportes", "Livros", "Beleza"]
STATUS_OPCOES = ["pendente", "concluído", "cancelado"]
STATUS_PESOS = [0.15, 0.75, 0.10]  # a maioria dos pedidos concluidos

linhas_sql = []

# ---------- CLIENTES ----------
linhas_sql.append("-- CLIENTES")
for i in range(1, N_CLIENTES + 1):
    nome = fake.name().replace("'", "''")
    cidade = fake.city().replace("'", "''")
    data_cadastro = fake.date_between(start_date="-2y", end_date="today")
    linhas_sql.append(
        f"INSERT INTO clientes (nome, cidade, data_cadastro) "
        f"VALUES ('{nome}', '{cidade}', '{data_cadastro}');"
    )

# ---------- PRODUTOS ----------
linhas_sql.append("\n-- PRODUTOS")
produtos_precos = []
for i in range(1, N_PRODUTOS + 1):
    nome_prod = fake.word().capitalize() + " " + fake.word().capitalize()
    categoria = random.choice(CATEGORIAS)
    preco = round(random.uniform(15.0, 1500.0), 2)
    produtos_precos.append(preco)
    linhas_sql.append(
        f"INSERT INTO produtos (nome_prod, categoria_prod, preco_prod) "
        f"VALUES ('{nome_prod}', '{categoria}', {preco});"
    )

# ---------- PEDIDOS ----------
linhas_sql.append("\n-- PEDIDOS")
for i in range(1, N_PEDIDOS + 1):
    cliente_id = random.randint(1, N_CLIENTES)
    data_pedido = fake.date_between(start_date="-1y", end_date="today")
    status = random.choices(STATUS_OPCOES, weights=STATUS_PESOS)[0]
    linhas_sql.append(
        f"INSERT INTO pedidos (data_pedidos, status, cliente_id) "
        f"VALUES ('{data_pedido}', '{status}', {cliente_id});"
    )

# ---------- ITENS_PEDIDO ----------
linhas_sql.append("\n-- ITENS_PEDIDO")
for pedido_id in range(1, N_PEDIDOS + 1):
    n_itens = random.randint(1, MAX_ITENS_POR_PEDIDO)
    produtos_do_pedido = random.sample(range(1, N_PRODUTOS + 1), min(n_itens, N_PRODUTOS))
    for produto_id in produtos_do_pedido:
        quantidade = random.randint(1, 5)
        preco_unitario = produtos_precos[produto_id - 1]
        linhas_sql.append(
            f"INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) "
            f"VALUES ({pedido_id}, {produto_id}, {quantidade}, {preco_unitario});"
        )

with open("dados_ecommerce.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(linhas_sql))

print("Arquivo 'dados_ecommerce.sql' gerado com sucesso!")
print(f"{N_CLIENTES} clientes, {N_PRODUTOS} produtos, {N_PEDIDOS} pedidos e seus itens.")
