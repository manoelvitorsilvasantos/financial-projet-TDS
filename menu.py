import utils

def display(opcoes):
  utils.limparTela()
  for i in range(len(opcoes)):
    print('{} - {}'.format(i, opcoes[i]['descricao']))
  
  op = int(input('Selecione uma opção: '))

  opcoes[op]['exec']()

  display(opcoes)
