from moduleA import distribution
import moduleB

d=distribution('20201231.csv','20211231.csv', '20221231.csv', '20231231.csv')

g= moduleB.Graph(d)
g.line_chart()