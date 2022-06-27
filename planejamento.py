import movimentacao
import menu

menu_planejamento = [
  {
    'descricao': 'Voltar',
    'exec': exit
  },
  {
    'descricao': 'Cadastrar entrada ou saida',
    'exec': lambda :movimentacao.cadastrar('planejamento')
  },
  {
    'descricao': 'Atualizar entrada ou saida',
    'exec': lambda : movimentacao.atualizar('planejamento')
  },
  {
    'descricao': 'Listar',
    'exec': lambda : movimentacao.listar('planejamento')
  },
  {
    'descricao': 'Remover entrada ou saida',
    'exec': lambda :movimentacao.remover('planejamento')
  },
]

def exibir_menu_planejamento():
  menu.display(menu_planejamento, 'Planejamento')

