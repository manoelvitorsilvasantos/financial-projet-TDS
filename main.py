import movimentacao
import utils

menu = [
  {
    'descricao': 'Sair',
    'exec': exit
  },
  {
    'descricao': 'Cadastrar entrada ou saida',
    'exec': movimentacao.cadastrar
  },
  {
    'descricao': 'Atualizar entrada ou saida',
    'exec': movimentacao.atualizar
  },
  {
    'descricao': 'Remover entrada ou saida',
    'exec': movimentacao.remover
  },
]

def display_menu():
  utils.limparTela()
  for i in range(len(menu)):
    print('{} - {}'.format(i, menu[i]['descricao']))
  
  op = int(input('Selecione uma opção: '))

  menu[op]['exec']()

  display_menu()

display_menu()
