from moduleA import distribution
from moduleB import graph

d=distribution('20231231.csv')

g=graph(d)

g.bar_chart(True)
