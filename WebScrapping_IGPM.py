import requests
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.idinheiro.com.br/tabelas/tabela-igp-m/')  
soup = BeautifulSoup(page.content, 'html.parser')

tabela1 = soup.find(class_ = 'table-all__value')

ano = []
janeiro = []
fevereiro =[]
marco =[]
abril = []
maio = []
junho = []
julho = []
agosto = []
setembro = []
outubro = []
novembro = []
dezembro = []
total = []

tabela = {
1: janeiro,
2: fevereiro,
3: marco,
4: abril,
5: maio,
6: junho,
7: julho,
8: agosto,
9: setembro,
10: outubro,
11: novembro,
12: dezembro,
13: total
}

for i in tabela1.select('tr'):
    linha = i.get_text()
    lista1 = linha.split(" ")
    lista1.remove('')
    ano.append(lista1[0])
    janeiro.append(lista1[1])
    fevereiro.append(lista1[2])
    marco.append(lista1[3])
    abril.append(lista1[4])
    maio.append(lista1[5])
    junho.append(lista1[6])
    julho.append(lista1[7])
    agosto.append(lista1[8])
    setembro.append(lista1[9])
    outubro.append(lista1[10])
    novembro.append(lista1[11])
    dezembro.append(lista1[12])
    total.append(lista1[13])
    

titulos = [tabela[c][0] for c in tabela]
[tabela[c].pop(0) for c in tabela] and ano.pop(0)

planilha = pd.DataFrame(tabela)

planilha.set_axis(titulos, axis = 1, inplace = 1)
planilha.set_axis(ano, axis = 0, inplace = 1)
planilha.to_excel('igpm.xlsx')
print(planilha)