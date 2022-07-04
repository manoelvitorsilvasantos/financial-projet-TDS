import modules.utils as utils

def display(opcoes, cabecalho):
  utils.limparTela()
  print(':::::::::::::|{}|:::::::::::::'.format(cabecalho))
  for i in range(len(opcoes)):
    print('{} - {}'.format(i, opcoes[i]['descricao']))
  
  op = input('Selecione uma opção: ')

  if not op.isnumeric(): return display(opcoes, cabecalho)
  op = int(op)

  if not op in range(len(opcoes)): return display(opcoes, cabecalho)
  
  if op == 0: return 0

  opcoes[op]['exec']()

  return display(opcoes, cabecalho)
