import movimentacao
import menu

menu_fluxo = [
  {
    'descricao': 'Voltar',
    'exec': exit
  },
  {
    'descricao': 'Cadastrar entrada ou saida',
    'exec': lambda :movimentacao.cadastrar('fluxo')
  },
  {
    'descricao': 'Atualizar entrada ou saida',
    'exec': lambda : movimentacao.atualizar('fluxo')
  },
  {
    'descricao': 'Listar',
    'exec': lambda : movimentacao.listar('fluxo')
  },
  {
    'descricao': 'Remover entrada ou saida',
    'exec': lambda :movimentacao.remover('fluxo')
  },
]

def exibe_menu_fluxo():
  menu.display(menu_fluxo)

