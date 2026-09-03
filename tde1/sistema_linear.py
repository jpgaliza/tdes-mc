import numpy as np

# Matriz dos coeficientes
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

# Vetor dos resultados
B = np.array([8, -11, -3])

# Cálculo do determinante
det_A = np.linalg.det(A)

# Cálculo da matriz inversa
A_inv = np.linalg.inv(A)

# Resolução do sistema linear
X = np.linalg.solve(A, B)

print("Matriz A:")
print(A)

print("\nVetor B:")
print(B)

print("\nDeterminante de A:")
print(det_A)

print("\nMatriz inversa de A:")
print(A_inv)

print("\nSolução do sistema:")
print(X)

# Verificação da solução
print("\nVerificação A @ X:")
print(A @ X)
