import numpy as np

def main():
    print("=== 1. CRIAÇÃO DE ARRAYS ===")
    vetor = np.array([10, 20, 30, 40, 50])
    print("Vetor 1D:\n", vetor)
    print("Formato (shape):", vetor.shape)
    print("Dimensões (ndim):", vetor.ndim)

    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("\nMatriz 2D:\n", matriz)
    print("Formato da matriz:", matriz.shape)
    print("Tipo de dados:", matriz.dtype)

    print("\n=== 2. OPERAÇÕES ARITMÉTICAS ===")
    matriz_dobro = matriz * 2
    print("Matriz multiplicada por 2:\n", matriz_dobro)
    print("Soma element-wise:\n", matriz + matriz_dobro)

    print("\n=== 3. FATIAMENTO (SLICING) ===")
    print("Primeira linha:", matriz[0, :])
    print("Segunda coluna:", matriz[:, 1])
    print("Submatriz 2x2:\n", matriz[0:2, 0:2])

if __name__ == "__main__":
    main()
