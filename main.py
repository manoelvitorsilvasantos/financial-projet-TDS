import menu
import fluxo
import planejamento

menu_obj = [
  {
    'descricao': 'Sair',
    'exec': exit
  },
  {
    'descricao': 'Fluxo',
    'exec': fluxo.exibe_menu_fluxo,
  },
  {
    'descricao': 'Plano financeiro',
    'exec': planejamento.exibir_menu_planejamento
  },
  {
    'descricao': 'Converter moedas',
    'exec': exit
  },
]

def exibe_menu_principal():
  menu.display(menu_obj)

exibe_menu_principal()
