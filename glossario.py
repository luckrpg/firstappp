# 1. Crie uma lista com os nomes de 5 objetos.
objetos = ['mesa', 'cadeira', 'livro', 'caneta', 'copo']

# 2. Adicione mais um objeto ao final da lista.
objetos.append('lâmpada')

# 3. pega o objeto q ta na 2 posição
print("Objeto na 2ª posição:", objetos[2])

# 4. Remova um objeto da lista.
objetos.remove('livro')  # Remove um sujeitinho da lista

# 5. Exiba o tamanho da lista
print("Tamanho da lista:", len(objetos))

# 6. Mostre todos os itens com um for.
print("Itens da lista:")
for objeto in objetos:
    print(objeto)

# 7. Verifique se 'cadeira' está na lista. Se sim, remova-a, se não adicione-a.
if 'cadeira' in objetos:
    objetos.remove('cadeira')
else:
    objetos.append('cadeira')

# 8. Ordene a lista em ordem alfabética.
objetos.sort()

# 9. Exiba o primeiro e o último objeto.
print("Primeiro objeto:", objetos[0])
print("Último objeto:", objetos[-1])

# 10. Limpe toda a lista.
objetos.clear()
print("Lista final após limpar:", objetos)
