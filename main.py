#!/usr/bin/env python3


import modules.menu as menu
import fluxo
import planejamento
import modules.movimentacao.movimentacao as movimentacao
import modules.conversao.converter as conv
import comparativo

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
    'exec': lambda : movimentacao.mostrar_saldo()
  },
  {
    'descricao': 'Visualizar comparação: efetuado X planejado',
    'exec': lambda : comparativo.getData()
  },
  {
    'descricao': 'Viabilidade de investimento',
    'exec': lambda : input('Em desenvolvimento! (enter para voltar)')
  },
  {
    'descricao': 'Converter moedas',
    'exec': lambda : conv.main('CONVERSOR DE MOEDA')
  },
]

def exibe_menu_principal():
  menu.display(menu_obj,'Principal')

exibe_menu_principal()
