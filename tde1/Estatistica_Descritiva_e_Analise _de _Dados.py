import numpy as np

np.set_printoptions(
    formatter={'float_kind': lambda x: f"{x:.1f}"}
)

print('---'*10)
print('ANÁLISE DE NOTAS')
print('---'*10)

alunos = np.array([
    'Ana','Bruno','Carlos','Daniela','Eduardo','Fernanda','Gabriel','Helena','Igor','Julia'
])

notas = np.array([
    [8.0, 8.5, 9.0, 8.5],
    [7.0, 6.5, 7.5, 8.0],
    [9.0, 9.5, 8.5, 9.0],
    [6.0, 7.0, 6.5, 7.5],
    [8.5, 8.0, 9.0, 8.5],
    [5.5, 6.0, 5.0, 6.5],
    [9.5, 9.0, 10.0, 9.5],
    [7.5, 8.0, 7.0, 8.5],
    [6.5, 7.0, 6.0, 7.5],
    [8.0, 8.5, 9.0, 8.0]
])

for i in range(len(alunos)):
print(f'{alunos[i]}: {notas[i]}')
print('---'*10)

media_aluno = np.mean(notas, axis=1)

for i in range(len(alunos)):
print(f'Média de {alunos[i]}: {media_aluno[i]:.2f}')
print('---'*10)

media_geral = np.mean(notas)
print(f'Média geral: {media_geral:.2f}')

maior = np.max(notas)
print(f'Maior nota: {maior:.1f}')

menor = np.min(notas)
print(f'Menor nota: {menor:.1f}')

desvio = np.std(notas)
print(f'Desvio padrão: {desvio:.2f}')

print('---'*10)
