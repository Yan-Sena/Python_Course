# Inicialize uma lista vazia para a lista de compras
lista_de_compras = []

# Adicione itens à lista de compras
lista_de_compras.append("Maçãs")
lista_de_compras.append("Bananas")
lista_de_compras.append("Leite")
lista_de_compras.append("Pão")

# Exiba a lista de compras
print("Lista de Compras:")
for item in lista_de_compras:
    print(item)

# Remova um item da lista de compras
item_removido = lista_de_compras.pop(1)  # Remove o segundo item (índice 1)
print(f"\nItem removido: {item_removido}")

# Exiba a lista de compras atualizada
print("\nLista de Compras Atualizada:")
for item in lista_de_compras:
    print(item)
