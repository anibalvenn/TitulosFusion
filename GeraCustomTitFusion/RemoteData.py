import pandas as pd
from urllib.request import Request, urlopen

def pegaHTML():
    req = Request('https://br.financas.yahoo.com/noticias/acoes-em-alta/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage

def pegaArrayYFinance():
    html = pegaHTML()
    list = pd.read_html(html)
    arr = list[0].values
    return arr

def listaTresPrimeiros():
    count = 0
    arr = pegaArrayYFinance()
    dict = {}

    for i in arr:
        if count < 3:  
            ticker=arr[count][0]
            nome=arr[count][1]
            deltaDay=arr[count][4]
            list = [ticker, nome, deltaDay]
            dict[count] = [list]
            

            count =+ count +1
    return dict


listaTresPrimeiros()