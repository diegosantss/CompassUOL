#

import csv

with open("DESAFIO-ETL/actors.csv") as f:
    arquivo = csv.reader(f)
    next(arquivo)  # pula a primeira linha, que contém os nomes das colunas
    lista = []
    for linha in arquivo:
        actor = linha[0]
        Total_Gross = float(linha[1])
        lista.append({'actor': actor, 'Total Gross': Total_Gross})
    
ordem_lista = sorted(lista, key=lambda x: x['Total Gross'], reverse=True)

#um for para iterar sobre a lista ordenada e imprimir cada autor.
for elem in ordem_lista:
    print(elem['actor'])


'''
SAÍDA: 
Harrison Ford
Samuel L. Jackson
Morgan Freeman
Tom Hanks
Robert Downey, Jr.
Eddie Murphy
Tom Cruise
Johnny Depp
Michael Caine
Scarlett Johansson
Gary Oldman
Robin Williams
Bruce Willis
Stellan Skarsgard
Anthony Daniels
Ian McKellen
Will Smith
Stanley Tucci
Matt Damon
Robert DeNiro
Cameron Diaz
Liam Neeson
Andy Serkis
Don Cheadle
Ben Stiller
Helena Bonham Carter
Orlando Bloom
Woody Harrelson
Cate Blanchett
Julia Roberts
Elizabeth Banks
Ralph Fiennes
Emma Watson
Tommy Lee Jones
Brad Pitt
Adam Sandler
Daniel Radcliffe
Jonah Hill
Owen Wilson
Idris Elba
Bradley Cooper
Mark Wahlberg
Jim Carrey
Dustin Hoffman
Leonardo DiCaprio
Jeremy Renner
Philip Seymour Hoffman
Sandra Bullock
Chris Evans
Anne Hathaway
'''