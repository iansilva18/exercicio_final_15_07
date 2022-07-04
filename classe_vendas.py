from classe_estoque import*
from classe_historico import*

class Vendas:
    def __init__(self):
        self.entrada = Estoque()
        self.historico = Historico()
    def vender(self):
        entrada = input('Codigo do Produto:  ')
        for i in range(len(self.entrada.listaProdutos)):
            if entrada == self.entrada.listaProdutos[i].cod:
                x=int(input('Quantidade Vendida:  '))
                self.entrada.listaProdutos[i].quantidade -= int(x)
                self.historico.transacoes.append(f'Venda de {x} unidades do produto: {self.entrada.listaProdutos[i].nome}')
    def extrato(self):
        print(self.historico.compras_vendas())