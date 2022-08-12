#Estado 1: confere alfabeto
def estado1(texto):
  retorno = True
  alfabeto = ['a', 'b', 'c']
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se não pertence ao alfabeto encerra
    if letra not in alfabeto:
      return False
    #Se pertence segue para estado 2
    else:
      return estado2(letra)
  return retorno
  
#Estado 2: confere linguagem
def estado2(letra):
  retorno = True
  letras_linguagem = ['a', 'b']
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se não pertence a linguagem encerra
    if letra not in letras_linguagem:
      return False
    #Se pertence segue para estado 3
    else:
      return estado3(letra)
  return retorno

#Estado 3: confere a ou b
def estado3(letra):
  retorno = True
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se for a segue para estado 4
    if letra == 'a':
      return estado4(texto)
    #Se for b volta para o estado 3
    elif letra == 'b':
      return estado3(letra)
    else:
      return False
  return retorno

#Estado 4: confere b:
def estado4(letra):
  retorno = True
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se for b segue para estado 5
    if letra == 'b':
      return estado5(letra)
    #Se for a encerra
    else:
      return False
  return retorno

#Estado 5: confere segundo b
def estado5(letra):
  retorno = True
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se for b segue para estado 6
    if letra == 'b':
      return estado6(letra)
    #Se for a encerra
    else:
      return False
  return retorno

#Estado 6: confere depois da sequecia do a
def estado6(letra):
  retorno = True
  tamanho = len(texto)
  for i in range(0,tamanho):
    letra = texto[i]
    #Se for b segue para estado 3
    if letra == 'b':
      return estado3(letra)
    #Se for a segue para estado 4
    else:
      return estado4(letra)
  return retorno
    
#Abre arquivo com open(arquivo)
  #Para outro arquivo mudar numero do txt de acordo com demais arquivos diponibilizados
with open('String9.txt') as arquivo:
  lista = arquivo.readlines()
  linhas = int(lista[0])

  if len(lista) == linhas+1:
    contador = 1
    while contador <= linhas:
      texto = lista[contador].strip('\n')
      tamanho = len(texto)
      resultado = estado1(texto)   
    #Resultado com resposta de pertencimento ou não pertencimento
      if resultado:
        #Printa string e diz que pertence a linguagem L
          print('%s: pertence a linguagem' % texto)  
      else:
        #Printa string e diz que não pertence a linguagem L
        print('%s: não pertence a linguagem' % texto)

      contador += 1
  else:
    print('Não corresponde')
    
