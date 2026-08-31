import numpy as np

print('---'*10)
valores = np.array([1, 4, 9, 16])
print(f"Valores: {valores}")
print('---'*10)


raiz = np.sqrt(valores)
print(f'Raiz quadrada: \n{raiz}\n')

potencia = np.power(valores,3)
print(f'Potencia: \n{potencia}\n')

log = np.round(np.log(valores),2)
print(f'Logaritmo: \n{log}\n')

seno = np.round(np.sin(valores),2)
print(f'Seno: \n{seno}\n')

cosseno = np.round(np.cos(valores),2)
print(f'Cosseno: \n{cosseno}\n')

tangente = np.round(np.tan(valores),2)
print(f'Tanjente: \n{tangente}\n')

