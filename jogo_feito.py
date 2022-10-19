from random import choice
board = [
'''
+-----+
|     |
      |
      |
      |
      |
======     
''',
'''
+-----+
|     |
O     |
      |
      |
      |
======     
''',
'''
+-----+
|     |
O     |
|     |
      |
      |
======     
''',
'''
 +-----+
 |     |
 O     |
/|     |
       |
       |
======     
''',
'''
 +-----+
 |     |
 O     |
/|\    |
       |
       |
======     
''',   
'''
 +-----+
 |     |
 O     |
/|\    |
/      |
       |
======     
''',     
'''
 +-----+
 |     |
 O     |
/|\    |
/ \    |
       |
======     
''' ]

class forca:
       def __init__(self, palavra = ['arvore', 'folha', 'cachorro', 'ouvido', 'televisor', 'copo', 'banana','bebida', 'banheiro', 'cabelo',  'papel', 'monitor', 'leopardo']):
              self.palavra = choice(palavra)
              self.acertos = list()
              self.erros = list()
       

       def padronizar_palavra(self):
              self.palavra_separada = []
              self.oculto = ['_'] * len(self.palavra)
              
              
              for i in self.palavra:
                     self.palavra_separada.append(i)         

       def adivinha(self, letra):     
              if letra not in self.acertos and letra in self.palavra:
                     self.acertos.append(letra)   
                     for x in range(len(self.palavra)):    
                            for x in range(len(self.palavra)):
                                   if letra == self.palavra[x]:
                                          self.oculto[x] = letra 
                     print() 
                     print('Palavra:')
                     print()
                     
                     
                     for c in self.oculto:
                            print(c, end = ' ')
                       
              elif letra not in self.erros and letra not in self.palavra:
                     self.erros.append(letra)
              
       
              print()
              print('\nLetras acertadas: ')
              for a in self.acertos:
                     print(a , end = ' ')
              print()
              print('\nLetras erradas: ')
              print()
              for a in self.erros:
                     print(a , end = ' ')
              print()
              print('-=' *15)
              print()
              print()
              
       def mostrar_forca(self):
              print()
              print()
              if len(self.erros) <= 6:
                     print(board[len(self.erros)])     
              
       def perdedor(self):
              print()
              print()
              print(f'\033[31mVocê Perdeu!!! a palavra era {self.palavra.upper()}\033[m') 
              print('\033[33mFIM DE JOGO!!!!!!!!!!!!!!!. \033[m')
                     
       def ganhador(self):
              print()
              print()
              print(f'\033[32mVocê ganhou!! Parabens. \033[m')
              tent = len(self.acertos + self.erros)
              print()
              print(f'\033[33mVocê fez {tent} tentativas\033[m')
              print('\033[33mFIM DE JOGO!!!!!!!!!!!!!!!. \033[m')
              
              
       def start_game(self):
              print()
              print('Palavra: ')
              print()
              print('_' * len(self.palavra))
              
              while True:
                     self.clenar()
                     self.mostrar_forca()
                     self.adivinha(input('Digite uma letra: '))
                     
                     if len(self.erros) == 6:
                            self.perdedor()
                            break
                     if '_' not in self.oculto:
                            self.ganhador()
                            break
                     
                                   
                     
                     
                     
                     for c in self.oculto:
                            print(c, end = ' ')
         
       def clenar(self):
              print()
              print()
              print()
              print()
              print()
              print()       



game = forca()
game.padronizar_palavra()  # COMANDO OBRIGATÓRIO PARA O FUNCIONAMENTO NO CÓDIGO
game.start_game()
