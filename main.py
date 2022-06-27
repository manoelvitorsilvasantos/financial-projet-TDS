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
    'descricao': 'Visualizar saldo',
    'exec': lambda : input('Em desenvolvimento! (enter para voltar)')
  },
  {
    'descricao': 'Visualizar comparação: efetuado X planejado',
    'exec': lambda : input('Em desenvolvimento! (enter para voltar)')
  },
  {
    'descricao': 'Viabilidade de investimento',
    'exec': lambda : input('Em desenvolvimento! (enter para voltar)')
  },
  {
    'descricao': 'Converter moedas',
    'exec': lambda : input('Em desenvolvimento! (enter para voltar)')
  },
]

def exibe_menu_principal():
  menu.display(menu_obj)

exibe_menu_principal()
