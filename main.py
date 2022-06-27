import menu
import fluxo

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
    'exec': exit
  },
  {
    'descricao': 'Converter moedas',
    'exec': exit
  },
]

def exibe_menu_principal():
  menu.display(menu_obj)

exibe_menu_principal()
