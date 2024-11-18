# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produto = []
estoque = []

for i in range(5):
    p = input("Digite o produto: ")
    produto.append(p)
    estoq = int(input("Digite o estoque do produto acima"))
    estoque.append(estoq)

for i in range(len(produto)):
    if estoque[i] == 0:
        print(f"produto com estoque zerado: {produto[i]}")