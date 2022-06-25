import movimentacao
import menu

menu_obj = [
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


menu.display(menu_obj)
