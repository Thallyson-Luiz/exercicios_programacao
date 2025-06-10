lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,81],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,91],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,5,10,11],
    [1,6,1,5,1,1,1,4,7,3],
    [1,3,7,1,10,5,9,2,5,71,1],
    [4,7,6,5,2,9,2,1,2,1],
    [5,3,1,8,5,7,1,8,8,7],
    [10,9,8,7,6,5,4,3,2,1]]

# retorna o primeiro número duplicado de cada lista
# se não houver duplicados, retorna -1

def listas_duplicadas1(listas):
    def listas_duplicadas(lista):
        numeros_duplicados = set()
        primeiro_duplicado = -1
        for num in lista:
            if num in numeros_duplicados:
                primeiro_duplicado = num
                break
            numeros_duplicados.add(num)

        return primeiro_duplicado

    resultado = []
    for lista in listas:
        resultado.append((lista, listas_duplicadas(lista)))
    return resultado

# se quiser apague a tupla de retorno e retorne apenas o resultado do número duplicado

resultado = (listas_duplicadas1(lista_de_listas_de_inteiros))
for r in resultado:
    print(r)