valores_xor = [
    0x3d, 0x7c, 0x24, 0x69, 0x25, 0x7a, 0x22, 0x69,
    0x27, 0x7f, 0x24, 0x32, 0x7f, 0x7e, 0x25, 0x66,
    0x7f, 0x7a, 0x70, 0x69, 0x20, 0x7e, 0x3c
]
        # F, I, A, P
chave = [0x46, 0x49, 0x41, 0x50]  
saida = []

tamanho = len(valores_xor)
mod = len(chave)

for indice in range(tamanho):
    k = chave[indice % mod]
    x = valores_xor[indice]

    if x == 0:
        letra = 'A'
    else:
        temp = x ^ k
        letra = chr(temp) if 32 <= temp <= 126 else '.'

    saida.append(letra)

print("FIAP" + ''.join(saida))
