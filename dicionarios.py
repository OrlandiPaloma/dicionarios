meu_dicionario = {"A":"Ameixa", "B": "BOLA", "C":"CACHORRO"}
print(meu_dicionario['A'])
print(meu_dicionario['B'])
print(meu_dicionario['C'])

#é possivel navegar no dicionario, utilizando for, ou funções
meu_dicionario = {"A":"Ameixa", "B": "BOLA", "C":"CACHORRO"}
for chave in meu_dicionario:
  print(chave + "-" + meu_dicionario[chave])

#items retornará tuplas, que são imutaveis:
meu_dicionario = {"A":"Ameixa", "B": "BOLA", "C":"CACHORRO"}
for i in meu_dicionario.items():
  print(i)
for i in meu_dicionario.values():
  print(i)
for i in meu_dicionario.keys():
  print(i)