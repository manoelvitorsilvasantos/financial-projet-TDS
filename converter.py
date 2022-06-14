import requests

API_KEY = '410a78ed80f94de4aff6b31389899ac5'

class Converter:
    def __init__(self, value, ofMoney, fromMoney):
        self.value = value
        self.ofMoney = ofMoney
        self.fromMoney = fromMoney
    def fromNewCoin(self):
        moedas = [self.ofMoney, self.fromMoney]
        outMoney = '{},{}'.format(moedas[0], moedas[1])
        r = requests.get(
            'https://openexchangerates.org/api/latest.json',
            params = {
                'app_id':API_KEY,
                'symbols':outMoney,
                'show_alternative':'true',
                'base':'USD'
            }
        )

        rates  = r.json()['rates']
        out = self.value * 1/rates.get(moedas[0])*rates.get(moedas[1])
        return out
