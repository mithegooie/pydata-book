%logstart?
!pwd
pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
cd "C:\\Users\\millerdr\\Google Drive\\Python for Data Analysis\\pydata-book\\ch06
ls
# Sat, 28 Jun 2014 13:45:56
!cat ex1.csv
# Sat, 28 Jun 2014 13:46:13
cat ex1.csv
# Sat, 28 Jun 2014 13:47:22
!echo ex1.csv
# Sat, 28 Jun 2014 13:47:32
!stream ex1.csv
# Sat, 28 Jun 2014 13:47:52
import pandas as pd
# Sat, 28 Jun 2014 13:48:27
import numpy as np
# Sat, 28 Jun 2014 13:48:44
df = pd.read_csv('ex1.csv')
# Sat, 28 Jun 2014 13:48:46
df
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sat, 28 Jun 2014 13:49:12
df = pd.read_table('ex1.csv', sep=',')
# Sat, 28 Jun 2014 13:49:14
df
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sat, 28 Jun 2014 13:49:35
!type ex1.csv
# Sat, 28 Jun 2014 13:49:58
!type ex2.csv
# Sat, 28 Jun 2014 13:50:27
pd.read_csv('ex2.csv', header=None
)
#[Out]#    0   1   2   3      4
#[Out]# 0  1   2   3   4  hello
#[Out]# 1  5   6   7   8  world
#[Out]# 2  9  10  11  12    foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sat, 28 Jun 2014 13:51:16
pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sat, 28 Jun 2014 13:52:20
names = ['a', 'b', 'c', 'd', 'message']
# Sat, 28 Jun 2014 13:52:47
pd.read_csv('ex2.csv', names=names, index_col='message')
#[Out]#          a   b   c   d
#[Out]# message               
#[Out]# hello    1   2   3   4
#[Out]# world    5   6   7   8
#[Out]# foo      9  10  11  12
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Sat, 28 Jun 2014 13:53:25
!type csv_mindex.csv
# Sat, 28 Jun 2014 13:54:08
parsed = pd.read_csv('csv_mindex.csv', index_col=['key1', 'key2'])
# Sat, 28 Jun 2014 13:54:12
parsed
#[Out]#            value1  value2
#[Out]# key1 key2                
#[Out]# one  a          1       2
#[Out]#      b          3       4
#[Out]#      c          5       6
#[Out]#      d          7       8
#[Out]# two  a          9      10
#[Out]#      b         11      12
#[Out]#      c         13      14
#[Out]#      d         15      16
#[Out]# 
#[Out]# [8 rows x 2 columns]
# Sat, 28 Jun 2014 13:56:17
list(open('ex3.txt'))
#[Out]# ['            A         B         C\n',
#[Out]#  'aaa -0.264438 -1.026059 -0.619500\n',
#[Out]#  'bbb  0.927272  0.302904 -0.032399\n',
#[Out]#  'ccc -0.264273 -0.386314 -0.217601\n',
#[Out]#  'ddd -0.871858 -0.348382  1.100491\n']
# Sat, 28 Jun 2014 13:57:55
result = pd.read_table('ex3.txt', sep='\s+')
# Sat, 28 Jun 2014 13:57:57
result
#[Out]#             A         B         C
#[Out]# aaa -0.264438 -1.026059 -0.619500
#[Out]# bbb  0.927272  0.302904 -0.032399
#[Out]# ccc -0.264273 -0.386314 -0.217601
#[Out]# ddd -0.871858 -0.348382  1.100491
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Sat, 28 Jun 2014 13:59:12
!type ex4.csv
# Sat, 28 Jun 2014 13:59:39
pd.read_csv('ex4.csv', skiprows=[0, 2, 3])
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sat, 28 Jun 2014 14:00:29
!type ex5.csv
# Sat, 28 Jun 2014 14:00:56
result = pd.read_csv('ex5.csv')
# Sat, 28 Jun 2014 14:00:58
result
#[Out]#   something  a   b   c   d message
#[Out]# 0       one  1   2   3   4     NaN
#[Out]# 1       two  5   6 NaN   8   world
#[Out]# 2     three  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Sat, 28 Jun 2014 14:01:19
pd.isnull(result)
#[Out]#   something      a      b      c      d message
#[Out]# 0     False  False  False  False  False    True
#[Out]# 1     False  False  False   True  False   False
#[Out]# 2     False  False  False  False  False   False
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Sat, 28 Jun 2014 14:02:10
result = pd.read_csv('ex5.csv', na_values=['NULL'])
# Sat, 28 Jun 2014 14:02:12
result
#[Out]#   something  a   b   c   d message
#[Out]# 0       one  1   2   3   4     NaN
#[Out]# 1       two  5   6 NaN   8   world
#[Out]# 2     three  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Sat, 28 Jun 2014 14:04:23
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
# Sat, 28 Jun 2014 14:04:36
result = pd.read_csv('ex5.csv', na_values=sentinels)
# Sat, 28 Jun 2014 14:04:39
result
#[Out]#   something  a   b   c   d message
#[Out]# 0       one  1   2   3   4     NaN
#[Out]# 1       NaN  5   6 NaN   8   world
#[Out]# 2     three  9  10  11  12     NaN
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Sat, 28 Jun 2014 14:08:27
result = pd.read_csv('ex6.csv')
# Sat, 28 Jun 2014 14:08:28
result
#[Out]#          one       two     three      four key
#[Out]# 0   0.467976 -0.038649 -0.295344 -1.824726   L
#[Out]# 1  -0.358893  1.404453  0.704965 -0.200638   B
#[Out]# 2  -0.501840  0.659254 -0.421691 -0.057688   G
#[Out]# 3   0.204886  1.074134  1.388361 -0.982404   R
#[Out]# 4   0.354628 -0.133116  0.283763 -0.837063   Q
#[Out]# 5   1.817480  0.742273  0.419395 -2.251035   Q
#[Out]# 6  -0.776764  0.935518 -0.332872 -1.875641   U
#[Out]# 7  -0.913135  1.530624 -0.572657  0.477252   K
#[Out]# 8   0.358480 -0.497572 -0.367016  0.507702   S
#[Out]# 9  -1.740877 -1.160417 -1.637830  2.172201   G
#[Out]# 10  0.240564 -0.328249  1.252155  1.072796   8
#[Out]# 11  0.764018  1.165476 -0.639544  1.495258   R
#[Out]# 12  0.571035 -0.310537  0.582437 -0.298765   1
#[Out]# 13  2.317658  0.430710 -1.334216  0.199679   P
#[Out]# 14  1.547771 -1.119753 -2.277634  0.329586   J
#[Out]# 15 -1.310608  0.401719 -1.000987  1.156708   E
#[Out]# 16 -0.088496  0.634712  0.153324  0.415335   B
#[Out]# 17 -0.018663 -0.247487 -1.446522  0.750938   A
#[Out]# 18 -0.070127 -1.579097  0.120892  0.671432   F
#[Out]# 19 -0.194678 -0.492039  2.359605  0.319810   H
#[Out]# 20 -0.248618  0.868707 -0.492226 -0.717959   W
#[Out]# 21 -1.091549 -0.867110 -0.647760 -0.832562   C
#[Out]# 22  0.641404 -0.138822 -0.621963 -0.284839   C
#[Out]# 23  1.216408  0.992687  0.165162 -0.069619   V
#[Out]# 24 -0.564474  0.792832  0.747053  0.571675   I
#[Out]# 25  1.759879 -0.515666 -0.230481  1.362317   S
#[Out]# 26  0.126266  0.309281  0.382820 -0.239199   L
#[Out]# 27  1.334360 -0.100152 -0.840731 -0.643967   6
#[Out]# 28 -0.737620  0.278087 -0.053235 -0.950972   J
#[Out]# 29 -1.148486 -0.986292 -0.144963  0.124362   Y
#[Out]# 30  1.630594  0.243886  0.468368  1.258048   F
#[Out]# 31  1.044890  0.080718  0.857886 -0.298382   J
#[Out]# 32 -0.262543 -1.615199 -1.087239  0.759029   T
#[Out]# 33  0.020144  1.107792 -0.559435 -0.481925   M
#[Out]# 34 -1.203916  1.885343 -0.080470  0.250646   J
#[Out]# 35  0.366915 -2.430086 -1.053447  0.346279   A
#[Out]# 36  0.434220 -0.079863 -0.422977 -0.074272   I
#[Out]# 37  0.040666 -1.810216 -0.189193  1.229266   G
#[Out]# 38  1.338459  0.338489 -0.213446  2.325923   Q
#[Out]# 39  0.572981  0.782664  1.307673  1.619957   X
#[Out]# 40  0.762428 -0.648529  1.936515 -1.159666   J
#[Out]# 41 -1.252046 -1.538539  1.042281  0.623835   A
#[Out]# 42 -0.047530 -0.494310 -0.165460  0.472929   J
#[Out]# 43  0.124548  0.730791 -0.257527 -1.511257   G
#[Out]# 44  0.801889 -0.462781 -1.734621  0.674768   R
#[Out]# 45 -0.992307 -1.096830 -2.061794  0.035391   R
#[Out]# 46 -0.109663  2.577094  0.913563  0.613594   V
#[Out]# 47 -0.541681  1.510031  0.467945  0.553225   N
#[Out]# 48 -0.079587 -0.609924  0.353834  1.108030   M
#[Out]# 49 -0.043752 -0.410666 -0.729599  0.263223   P
#[Out]# 50 -0.761490  1.104182  1.270609 -0.319284   O
#[Out]# 51 -0.804975  0.559520  1.052232 -0.645574   F
#[Out]# 52  0.353941  1.829963  0.398922 -1.522231   O
#[Out]# 53  1.541636  0.478316 -0.666760  1.367175   X
#[Out]# 54 -0.987621  0.337534  0.386935  1.996144   Z
#[Out]# 55 -0.353462 -0.448433 -0.420520  0.606223   N
#[Out]# 56 -0.275687  0.127910  0.877756  0.141774   6
#[Out]# 57  0.448882 -0.016410 -0.041434  0.483096   6
#[Out]# 58 -0.043765 -0.878446  1.525075  0.008223   Q
#[Out]# 59 -0.064416  0.080921  0.644715  0.393025   T
#[Out]#          ...       ...       ...       ... ...
#[Out]# 
#[Out]# [10000 rows x 5 columns]
# Sat, 28 Jun 2014 14:09:35
result.summary
# Sat, 28 Jun 2014 14:09:44
pd.summary(result)
# Sat, 28 Jun 2014 14:11:22
result = pd.read_csv('ex6.csv', nrows=5)
# Sat, 28 Jun 2014 14:11:25
result
#[Out]#         one       two     three      four key
#[Out]# 0  0.467976 -0.038649 -0.295344 -1.824726   L
#[Out]# 1 -0.358893  1.404453  0.704965 -0.200638   B
#[Out]# 2 -0.501840  0.659254 -0.421691 -0.057688   G
#[Out]# 3  0.204886  1.074134  1.388361 -0.982404   R
#[Out]# 4  0.354628 -0.133116  0.283763 -0.837063   Q
#[Out]# 
#[Out]# [5 rows x 5 columns]
# Sat, 28 Jun 2014 14:11:59
chunker = pd.read_csv('ex6.csv', chunksize=1000)
# Sat, 28 Jun 2014 14:12:03
chunker
#[Out]# <pandas.io.parsers.TextFileReader at 0xa2747f0>
# Sat, 28 Jun 2014 14:12:48
tot = Series([])
# Sat, 28 Jun 2014 14:13:00
from pandas import DataFrame, Series
# Sat, 28 Jun 2014 14:13:03
tot = Series([])
# Sat, 28 Jun 2014 14:13:39
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
    
# Sat, 28 Jun 2014 14:13:52
tot = tot.order(ascending=False)
# Sat, 28 Jun 2014 14:14:00
tot[:10]
#[Out]# E    368
#[Out]# X    364
#[Out]# L    346
#[Out]# O    343
#[Out]# Q    340
#[Out]# M    338
#[Out]# J    337
#[Out]# F    335
#[Out]# K    334
#[Out]# H    330
#[Out]# dtype: float64
# Sat, 28 Jun 2014 14:15:49
data = pd.read_csv('ex5.csv')
# Sat, 28 Jun 2014 14:15:50
data
#[Out]#   something  a   b   c   d message
#[Out]# 0       one  1   2   3   4     NaN
#[Out]# 1       two  5   6 NaN   8   world
#[Out]# 2     three  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Sat, 28 Jun 2014 14:17:15
data.to_csv('out_dm.csv')
# Sat, 28 Jun 2014 14:17:28
!type out_dm.csv
# Sat, 28 Jun 2014 14:18:15
data.to_csv(sys.stdout, sep='|')
# Sat, 28 Jun 2014 14:18:19
import sys
# Sat, 28 Jun 2014 14:18:23
data.to_csv(sys.stdout, sep='|')
# Sat, 28 Jun 2014 14:19:34
data.to_csv(sys.stdout, na_rep='NULL')
# Sat, 28 Jun 2014 14:20:26
data.to_csv(sys.stdout, index=False, header=False)
# Sat, 28 Jun 2014 14:21:02
data.to_csv(sys.stdout, index=False, cols=['a', 'b', 'c'])
# Sat, 28 Jun 2014 14:21:26
dates = pd.date_range('1/1/2000', periods=7)
# Sat, 28 Jun 2014 14:21:43
ts = Series(np.arange(7), index=dates)
# Sat, 28 Jun 2014 14:22:06
ts.to_csv('tseries_dm.csv')
# Sat, 28 Jun 2014 14:22:19
!type tseries_dm.csv
# Sat, 28 Jun 2014 14:23:25
Series.from_csv('tseries_dm.csv', parse_dates=True)
#[Out]# 2000-01-01    0
#[Out]# 2000-01-02    1
#[Out]# 2000-01-03    2
#[Out]# 2000-01-04    3
#[Out]# 2000-01-05    4
#[Out]# 2000-01-06    5
#[Out]# 2000-01-07    6
#[Out]# dtype: int64
# Sat, 28 Jun 2014 14:48:25
!type ex7.csv
# Sat, 28 Jun 2014 14:49:59
import csv
# Sat, 28 Jun 2014 14:50:11
f = open('ex7.csv')
# Sat, 28 Jun 2014 14:50:25
reader = csv.reader(f)
# Sat, 28 Jun 2014 14:50:29
reader
#[Out]# <_csv.reader at 0xa257ee8>
# Sat, 28 Jun 2014 14:50:34
print reader
# Sat, 28 Jun 2014 14:50:48
for line in reader:
    print line
    
# Sat, 28 Jun 2014 14:51:53
lines = list(csv.reader(open('ex7.csv')))
# Sat, 28 Jun 2014 14:51:55
lines
#[Out]# [['a', 'b', 'c'], ['1', '2', '3'], ['1', '2', '3', '4']]
# Sat, 28 Jun 2014 14:52:39
header, values = lines[0], lines[1:]
# Sat, 28 Jun 2014 14:52:41
header
#[Out]# ['a', 'b', 'c']
# Sat, 28 Jun 2014 14:52:44
values
#[Out]# [['1', '2', '3'], ['1', '2', '3', '4']]
# Sat, 28 Jun 2014 14:54:43
data_dict = {h: v for h, v in zip(header, zip(*values))}
# Sat, 28 Jun 2014 14:54:48
data_dict
#[Out]# {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}
# Sat, 28 Jun 2014 14:56:08
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    
# Sat, 28 Jun 2014 14:56:25
reader = csv.reader(f, dialect=my_dialect)
# Sat, 28 Jun 2014 14:58:31
reader = csv.reader(f, delimiter='|')
# Sat, 28 Jun 2014 14:58:34
reader
#[Out]# <_csv.reader at 0xa257d08>
# Sat, 28 Jun 2014 14:58:47
for line in reader:
    print line
    
# Sat, 28 Jun 2014 14:59:22
f
#[Out]# <open file 'ex7.csv', mode 'r' at 0x000000000A072660>
# Sat, 28 Jun 2014 14:59:37
!type f
# Sat, 28 Jun 2014 14:59:41
print f
# Sat, 28 Jun 2014 15:00:13
f.close
#[Out]# <function close>
# Sat, 28 Jun 2014 15:00:17
f.close()
# Sat, 28 Jun 2014 15:00:42
f = open('ex7.csv')
# Sat, 28 Jun 2014 15:01:00
reader = csv.reader(f, delimiter='|')
# Sat, 28 Jun 2014 15:01:03
reader
#[Out]# <_csv.reader at 0xa2579a8>
# Sat, 28 Jun 2014 15:01:11
for line in reader:
    print line
    
# Sat, 28 Jun 2014 15:02:06
reader = csv.reader(f)
# Sat, 28 Jun 2014 15:02:12
for line in reader:
    print line
    
# Sat, 28 Jun 2014 15:02:20
f.close()
# Sat, 28 Jun 2014 15:02:27
f = open('ex7.csv')
# Sat, 28 Jun 2014 15:02:32
reader = csv.reader(f)
# Sat, 28 Jun 2014 15:02:37
for line in reader:
    print line
    
# Sat, 28 Jun 2014 15:06:00
with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
    
# Sat, 28 Jun 2014 15:06:11
!type mydata.csv
# Sat, 28 Jun 2014 20:17:58
obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
# Sat, 28 Jun 2014 20:18:01
obj
#[Out]# '\n{"name": "Wes",\n"places_lived": ["United States", "Spain", "Germany"],\n"pet": null,\n"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},\n{"name": "Katie", "age": 33, "pet": "Cisco"}]\n}\n'
# Sat, 28 Jun 2014 20:18:38
import json
# Sat, 28 Jun 2014 20:18:56
result = json.loads(obj)
# Sat, 28 Jun 2014 20:19:00
result
#[Out]# {u'name': u'Wes',
#[Out]#  u'pet': None,
#[Out]#  u'places_lived': [u'United States', u'Spain', u'Germany'],
#[Out]#  u'siblings': [{u'age': 25, u'name': u'Scott', u'pet': u'Zuko'},
#[Out]#   {u'age': 33, u'name': u'Katie', u'pet': u'Cisco'}]}
# Sat, 28 Jun 2014 20:19:28
asjson = json.dumps(result)
# Sat, 28 Jun 2014 20:19:33
asjason
# Sat, 28 Jun 2014 20:19:44
asjson
#[Out]# '{"pet": null, "siblings": [{"pet": "Zuko", "age": 25, "name": "Scott"}, {"pet": "Cisco", "age": 33, "name": "Katie"}], "name": "Wes", "places_lived": ["United States", "Spain", "Germany"]}'
# Sat, 28 Jun 2014 20:21:35
siblings = DataFrame(result['siblings'], columns=['name', 'age'])
# Sat, 28 Jun 2014 20:21:38
siblings
#[Out]#     name  age
#[Out]# 0  Scott   25
#[Out]# 1  Katie   33
#[Out]# 
#[Out]# [2 rows x 2 columns]
# Sat, 28 Jun 2014 20:22:30
asjson.to_json
# Sat, 28 Jun 2014 20:24:08
data = pd.from_json(obj)
# Sat, 28 Jun 2014 20:27:00
from lxml.html import parse
# Sat, 28 Jun 2014 20:27:08
from urllib2 import urlopen
# Sat, 28 Jun 2014 20:27:38
parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
# Sat, 28 Jun 2014 20:27:58
doc = parsed.getroot()
# Sat, 28 Jun 2014 20:28:18
doc
#[Out]# <Element html at 0xa2a09f8>
# Sat, 28 Jun 2014 20:29:15
links = doc.findall('.//a')
# Sat, 28 Jun 2014 20:29:23
links[15:20]
#[Out]# [<Element a at 0xa2a0f98>,
#[Out]#  <Element a at 0xa3aa048>,
#[Out]#  <Element a at 0xa3aa098>,
#[Out]#  <Element a at 0xa3aa138>,
#[Out]#  <Element a at 0xa3aa188>]
# Sat, 28 Jun 2014 20:29:30
links[0]
#[Out]# <Element a at 0xa2a0ae8>
# Sat, 28 Jun 2014 20:32:02
all_links = [[x, y] for x, y in links.get, links.text_content]
# Sat, 28 Jun 2014 20:32:26
all_links = [[x, y] for x, y in links.get('href'), links.text_content]
# Sat, 28 Jun 2014 20:32:48
all_links = [[x, y] for x, y in [links.get('href'), links.text_content]]
# Sat, 28 Jun 2014 20:37:09
urls = [x for x in links[:].get('href')]
# Sat, 28 Jun 2014 20:37:42
lnk = links[28]
# Sat, 28 Jun 2014 20:37:45
lnk
#[Out]# <Element a at 0xa3aa458>
# Sat, 28 Jun 2014 20:37:52
lnk.get('href')
#[Out]# 'https://login.yahoo.com/config/login?.src=quote&.intl=us&.lang=en-US&.done=http://finance.yahoo.com/q/op%3fs=AAPL%2bOptions'
# Sat, 28 Jun 2014 20:38:13
lnk.text_content()
#[Out]# ' Sign In '
# Sat, 28 Jun 2014 20:39:01
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
# Sat, 28 Jun 2014 20:39:03
urls
#[Out]# ['https://www.yahoo.com/',
#[Out]#  'https://mail.yahoo.com/?.intl=us&.lang=en-US&.src=ym',
#[Out]#  'http://news.yahoo.com/',
#[Out]#  'http://sports.yahoo.com/',
#[Out]#  'http://finance.yahoo.com/',
#[Out]#  'https://weather.yahoo.com/',
#[Out]#  'https://games.yahoo.com/',
#[Out]#  'https://groups.yahoo.com/',
#[Out]#  'https://answers.yahoo.com/',
#[Out]#  'https://screen.yahoo.com/',
#[Out]#  'https://www.flickr.com/',
#[Out]#  'https://mobile.yahoo.com/',
#[Out]#  '#',
#[Out]#  'https://celebrity.yahoo.com/',
#[Out]#  'https://shine.yahoo.com/',
#[Out]#  'https://www.yahoo.com/movies',
#[Out]#  'https://music.yahoo.com/',
#[Out]#  'https://tv.yahoo.com/',
#[Out]#  'http://health.yahoo.com/',
#[Out]#  'https://www.yahoo.com/beauty',
#[Out]#  'https://www.yahoo.com/food',
#[Out]#  'https://www.yahoo.com/tech',
#[Out]#  'http://shopping.yahoo.com/',
#[Out]#  'https://www.yahoo.com/travel',
#[Out]#  'https://autos.yahoo.com/',
#[Out]#  'https://homes.yahoo.com/',
#[Out]#  'http://finance.yahoo.com',
#[Out]#  'https://login.yahoo.com/config/login?.src=quote&.intl=us&.lang=en-US&.done=http://finance.yahoo.com/q/op%3fs=AAPL%2bOptions',
#[Out]#  'https://login.yahoo.com/config/login?.src=quote&.intl=us&.lang=en-US&.done=http://finance.yahoo.com/q/op%3fs=AAPL%2bOptions',
#[Out]#  'https://mail.yahoo.com/?.intl=us&.lang=en-US&.src=ym',
#[Out]#  'javascript:void(0);',
#[Out]#  'https://edit.yahoo.com/mc2.0/eval_profile?.intl=us&.lang=en-US&.done=http://finance.yahoo.com/q/op%3fs=AAPL%2bOptions&.src=quote&.intl=us&.lang=en-US',
#[Out]#  'https://help.yahoo.com/l/us/yahoo/finance/',
#[Out]#  'http://feedback.yahoo.com/forums/207809',
#[Out]#  'https://www.yahoo.com/',
#[Out]#  'https://itunes.apple.com/app/yahoo!-finance/id328412701?ls=1&mt=8',
#[Out]#  'https://play.google.com/store/apps/details?id=com.yahoo.mobile.client.android.finance',
#[Out]#  '/',
#[Out]#  '/portfolios.html',
#[Out]#  '/portfolios/',
#[Out]#  'http://billing.finance.yahoo.com/realtime_quotes/signup?.src=quote&.refer=nb',
#[Out]#  '/market-overview/',
#[Out]#  '/stock-center/',
#[Out]#  '/funds/',
#[Out]#  '/options/',
#[Out]#  '/etf/',
#[Out]#  '/bonds',
#[Out]#  '/futures',
#[Out]#  '/currency-investing',
#[Out]#  '/news/',
#[Out]#  '/corporate-news/',
#[Out]#  '/economic-policy-news/',
#[Out]#  '/investing-news/',
#[Out]#  '/personal-finance/',
#[Out]#  '/career-education/',
#[Out]#  '/real-estate/',
#[Out]#  '/retirement/',
#[Out]#  '/credit-debt/',
#[Out]#  '/taxes/',
#[Out]#  '/lifestyle/',
#[Out]#  '/videos/',
#[Out]#  '/rates/',
#[Out]#  '/calculator/index/',
#[Out]#  '/blogs/',
#[Out]#  '/blogs/breakout/',
#[Out]#  '/blogs/daily-ticker/',
#[Out]#  '/blogs/driven/',
#[Out]#  '/blogs/the-exchange/',
#[Out]#  '/blogs/hot-stock-minute/',
#[Out]#  '/blogs/just-explain-it/',
#[Out]#  '/blogs/michael-santoli/',
#[Out]#  '/cnbc/',
#[Out]#  '/blogs/big-data-download/',
#[Out]#  '/blogs/off-the-cuff/',
#[Out]#  '/blogs/power-pitch/',
#[Out]#  '/blogs/talking-numbers/',
#[Out]#  '/blogs/the-biz-fix/',
#[Out]#  '/blogs/top-best-most/',
#[Out]#  'http://finance.search.yahoo.com?fr=fin-v1',
#[Out]#  'https://yahoo.uservoice.com/forums/207809-finance-gs/category/68435-data-accuracy',
#[Out]#  '/q?s=%5EDJI',
#[Out]#  '/q?s=%5EIXIC',
#[Out]#  '/q?s=AAPL',
#[Out]#  '/q/ecn?s=AAPL+Order+Book',
#[Out]#  '/q/hp?s=AAPL+Historical+Prices',
#[Out]#  '/echarts?s=AAPL+Interactive#symbol=AAPL;range=',
#[Out]#  '/q/bc?s=AAPL+Basic+Chart',
#[Out]#  '/q/ta?s=AAPL+Basic+Tech.+Analysis',
#[Out]#  '/q/h?s=AAPL+Headlines',
#[Out]#  '/q/p?s=AAPL+Press+Releases',
#[Out]#  '/q/ce?s=AAPL+Company+Events',
#[Out]#  '/mb/AAPL/',
#[Out]#  '/marketpulse/AAPL',
#[Out]#  '/q/pr?s=AAPL+Profile',
#[Out]#  '/q/ks?s=AAPL+Key+Statistics',
#[Out]#  '/q/sec?s=AAPL+SEC+Filings',
#[Out]#  '/q/co?s=AAPL+Competitors',
#[Out]#  '/q/in?s=AAPL+Industry',
#[Out]#  '/q/ct?s=AAPL+Components',
#[Out]#  '/q/ao?s=AAPL+Analyst+Opinion',
#[Out]#  '/q/ae?s=AAPL+Analyst+Estimates',
#[Out]#  '/q/mh?s=AAPL+Major+Holders',
#[Out]#  '/q/it?s=AAPL+Insider+Transactions',
#[Out]#  '/q/ir?s=AAPL+Insider+Roster',
#[Out]#  '/q/is?s=AAPL+Income+Statement&annual',
#[Out]#  '/q/bs?s=AAPL+Balance+Sheet&annual',
#[Out]#  '/q/cf?s=AAPL+Cash+Flow&annual',
#[Out]#  'https://finance.yahoo.com/portfolio/ytosv2',
#[Out]#  '/q/op?s=AAPL&m=2014-08',
#[Out]#  '/q/op?s=AAPL&m=2014-10',
#[Out]#  '/q/op?s=AAPL&m=2015-01',
#[Out]#  '/q/op?s=AAPL&m=2015-04',
#[Out]#  '/q/op?s=AAPL&m=2016-01',
#[Out]#  '/q/op?s=AAPL&k=33.570000',
#[Out]#  '/q?s=AAPL140719C00033570',
#[Out]#  '/q/op?s=AAPL&k=40.000000',
#[Out]#  '/q?s=AAPL140719C00040000',
#[Out]#  '/q/op?s=AAPL&k=41.430000',
#[Out]#  '/q?s=AAPL140719C00041430',
#[Out]#  '/q/op?s=AAPL&k=42.860001',
#[Out]#  '/q?s=AAPL140719C00042860',
#[Out]#  '/q/op?s=AAPL&k=44.290001',
#[Out]#  '/q?s=AAPL140719C00044290',
#[Out]#  '/q/op?s=AAPL&k=48.570000',
#[Out]#  '/q?s=AAPL140719C00048570',
#[Out]#  '/q/op?s=AAPL&k=49.290001',
#[Out]#  '/q?s=AAPL140719C00049290',
#[Out]#  '/q/op?s=AAPL&k=50.000000',
#[Out]#  '/q?s=AAPL140719C00050000',
#[Out]#  '/q/op?s=AAPL&k=52.139999',
#[Out]#  '/q?s=AAPL140719C00052140',
#[Out]#  '/q/op?s=AAPL&k=54.290001',
#[Out]#  '/q?s=AAPL140719C00054290',
#[Out]#  '/q/op?s=AAPL&k=54.290001',
#[Out]#  '/q?s=AAPL7140719C00054290',
#[Out]#  '/q/op?s=AAPL&k=55.000000',
#[Out]#  '/q?s=AAPL140719C00055000',
#[Out]#  '/q/op?s=AAPL&k=56.430000',
#[Out]#  '/q?s=AAPL140719C00056430',
#[Out]#  '/q/op?s=AAPL&k=56.430000',
#[Out]#  '/q?s=AAPL7140719C00056430',
#[Out]#  '/q/op?s=AAPL&k=57.139999',
#[Out]#  '/q?s=AAPL140719C00057140',
#[Out]#  '/q/op?s=AAPL&k=57.139999',
#[Out]#  '/q?s=AAPL7140719C00057140',
#[Out]#  '/q/op?s=AAPL&k=57.860001',
#[Out]#  '/q?s=AAPL140719C00057860',
#[Out]#  '/q/op?s=AAPL&k=58.570000',
#[Out]#  '/q?s=AAPL140719C00058570',
#[Out]#  '/q/op?s=AAPL&k=59.290001',
#[Out]#  '/q?s=AAPL140719C00059290',
#[Out]#  '/q/op?s=AAPL&k=59.290001',
#[Out]#  '/q?s=AAPL7140719C00059290',
#[Out]#  '/q/op?s=AAPL&k=60.000000',
#[Out]#  '/q?s=AAPL140719C00060000',
#[Out]#  '/q/op?s=AAPL&k=60.000000',
#[Out]#  '/q?s=AAPL7140719C00060000',
#[Out]#  '/q/op?s=AAPL&k=60.709999',
#[Out]#  '/q?s=AAPL140719C00060710',
#[Out]#  '/q/op?s=AAPL&k=60.709999',
#[Out]#  '/q?s=AAPL7140719C00060710',
#[Out]#  '/q/op?s=AAPL&k=61.430000',
#[Out]#  '/q?s=AAPL140719C00061430',
#[Out]#  '/q/op?s=AAPL&k=61.430000',
#[Out]#  '/q?s=AAPL7140719C00061430',
#[Out]#  '/q/op?s=AAPL&k=62.139999',
#[Out]#  '/q?s=AAPL140719C00062140',
#[Out]#  '/q/op?s=AAPL&k=62.860001',
#[Out]#  '/q?s=AAPL140719C00062860',
#[Out]#  '/q/op?s=AAPL&k=62.860001',
#[Out]#  '/q?s=AAPL7140719C00062860',
#[Out]#  '/q/op?s=AAPL&k=63.570000',
#[Out]#  '/q?s=AAPL140719C00063570',
#[Out]#  '/q/op?s=AAPL&k=63.570000',
#[Out]#  '/q?s=AAPL7140719C00063570',
#[Out]#  '/q/op?s=AAPL&k=64.290001',
#[Out]#  '/q?s=AAPL140719C00064290',
#[Out]#  '/q/op?s=AAPL&k=64.290001',
#[Out]#  '/q?s=AAPL7140719C00064290',
#[Out]#  '/q/op?s=AAPL&k=65.000000',
#[Out]#  '/q?s=AAPL140719C00065000',
#[Out]#  '/q/op?s=AAPL&k=65.000000',
#[Out]#  '/q?s=AAPL7140719C00065000',
#[Out]#  '/q/op?s=AAPL&k=65.709999',
#[Out]#  '/q?s=AAPL140719C00065710',
#[Out]#  '/q/op?s=AAPL&k=65.709999',
#[Out]#  '/q?s=AAPL7140719C00065710',
#[Out]#  '/q/op?s=AAPL&k=66.430000',
#[Out]#  '/q?s=AAPL140719C00066430',
#[Out]#  '/q/op?s=AAPL&k=66.430000',
#[Out]#  '/q?s=AAPL7140719C00066430',
#[Out]#  '/q/op?s=AAPL&k=67.139999',
#[Out]#  '/q?s=AAPL140719C00067140',
#[Out]#  '/q/op?s=AAPL&k=67.139999',
#[Out]#  '/q?s=AAPL7140719C00067140',
#[Out]#  '/q/op?s=AAPL&k=67.860001',
#[Out]#  '/q?s=AAPL140719C00067860',
#[Out]#  '/q/op?s=AAPL&k=67.860001',
#[Out]#  '/q?s=AAPL7140719C00067860',
#[Out]#  '/q/op?s=AAPL&k=68.570000',
#[Out]#  '/q?s=AAPL140719C00068570',
#[Out]#  '/q/op?s=AAPL&k=68.570000',
#[Out]#  '/q?s=AAPL7140719C00068570',
#[Out]#  '/q/op?s=AAPL&k=69.290001',
#[Out]#  '/q?s=AAPL140719C00069290',
#[Out]#  '/q/op?s=AAPL&k=70.000000',
#[Out]#  '/q?s=AAPL140719C00070000',
#[Out]#  '/q/op?s=AAPL&k=70.000000',
#[Out]#  '/q?s=AAPL7140719C00070000',
#[Out]#  '/q/op?s=AAPL&k=70.709999',
#[Out]#  '/q?s=AAPL140719C00070710',
#[Out]#  '/q/op?s=AAPL&k=70.709999',
#[Out]#  '/q?s=AAPL7140719C00070710',
#[Out]#  '/q/op?s=AAPL&k=71.430000',
#[Out]#  '/q?s=AAPL140719C00071430',
#[Out]#  '/q/op?s=AAPL&k=71.430000',
#[Out]#  '/q?s=AAPL7140719C00071430',
#[Out]#  '/q/op?s=AAPL&k=72.139999',
#[Out]#  '/q?s=AAPL140719C00072140',
#[Out]#  '/q/op?s=AAPL&k=72.139999',
#[Out]#  '/q?s=AAPL7140719C00072140',
#[Out]#  '/q/op?s=AAPL&k=72.860001',
#[Out]#  '/q?s=AAPL140719C00072860',
#[Out]#  '/q/op?s=AAPL&k=72.860001',
#[Out]#  '/q?s=AAPL7140719C00072860',
#[Out]#  '/q/op?s=AAPL&k=73.570000',
#[Out]#  '/q?s=AAPL140719C00073570',
#[Out]#  '/q/op?s=AAPL&k=73.570000',
#[Out]#  '/q?s=AAPL7140719C00073570',
#[Out]#  '/q/op?s=AAPL&k=74.290001',
#[Out]#  '/q?s=AAPL140719C00074290',
#[Out]#  '/q/op?s=AAPL&k=74.290001',
#[Out]#  '/q?s=AAPL7140719C00074290',
#[Out]#  '/q/op?s=AAPL&k=75.000000',
#[Out]#  '/q?s=AAPL140719C00075000',
#[Out]#  '/q/op?s=AAPL&k=75.000000',
#[Out]#  '/q?s=AAPL7140719C00075000',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL140711C00075710',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL140719C00075710',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL7140719C00075710',
#[Out]#  '/q/op?s=AAPL&k=76.430000',
#[Out]#  '/q?s=AAPL140719C00076430',
#[Out]#  '/q/op?s=AAPL&k=76.430000',
#[Out]#  '/q?s=AAPL7140719C00076430',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL140711C00077140',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL140719C00077140',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL7140719C00077140',
#[Out]#  '/q/op?s=AAPL&k=77.860001',
#[Out]#  '/q?s=AAPL140719C00077860',
#[Out]#  '/q/op?s=AAPL&k=77.860001',
#[Out]#  '/q?s=AAPL7140719C00077860',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140703C00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140719C00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL7140719C00078570',
#[Out]#  '/q/op?s=AAPL&k=79.000000',
#[Out]#  '/q?s=AAPL140703C00079000',
#[Out]#  '/q/op?s=AAPL&k=79.290001',
#[Out]#  '/q?s=AAPL140719C00079290',
#[Out]#  '/q/op?s=AAPL&k=79.290001',
#[Out]#  '/q?s=AAPL7140719C00079290',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140703C00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140711C00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140719C00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL7140719C00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140725C00080000',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL140703C00080710',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL140719C00080710',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL7140719C00080710',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140703C00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140719C00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL7140719C00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140725C00081430',
#[Out]#  '/q/op?s=AAPL&k=81.790001',
#[Out]#  '/q?s=AAPL140703C00081790',
#[Out]#  '/q/op?s=AAPL&k=82.000000',
#[Out]#  '/q?s=AAPL140703C00082000',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140703C00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140719C00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL7140719C00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140725C00082140',
#[Out]#  '/q/op?s=AAPL&k=82.500000',
#[Out]#  '/q?s=AAPL140703C00082500',
#[Out]#  '/q/op?s=AAPL&k=82.500000',
#[Out]#  '/q?s=AAPL7140703C00082500',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140703C00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140711C00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140719C00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL7140719C00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140725C00082860',
#[Out]#  '/q/op?s=AAPL&k=83.000000',
#[Out]#  '/q?s=AAPL140703C00083000',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140703C00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140719C00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL7140719C00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140725C00083570',
#[Out]#  '/q/op?s=AAPL&k=83.930000',
#[Out]#  '/q?s=AAPL140703C00083930',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140703C00084000',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140711C00084000',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140725C00084000',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140703C00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140711C00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140719C00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL7140719C00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140725C00084290',
#[Out]#  '/q/op?s=AAPL&k=84.639999',
#[Out]#  '/q?s=AAPL140703C00084640',
#[Out]#  '/q/op?s=AAPL&k=84.639999',
#[Out]#  '/q?s=AAPL140711C00084640',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140703C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140703C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140711C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140719C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140719C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140725C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140725C00085000',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL140703C00085360',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL140711C00085360',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140703C00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140703C00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140711C00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140719C00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140719C00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140725C00085710',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140703C00086000',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140711C00086000',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140725C00086000',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL140703C00086070',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL140711C00086070',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140703C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140703C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140711C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140711C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140719C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140719C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140725C00086430',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140703C00086790',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140711C00086790',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140725C00086790',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140703C00087000',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140711C00087000',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140725C00087000',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140703C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140703C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140711C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140711C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140719C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140719C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140725C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140725C00087140',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140703C00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140711C00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140725C00087500',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140703C00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140711C00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140719C00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL7140719C00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140725C00087860',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140703C00088000',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140711C00088000',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140725C00088000',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140703C00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140711C00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140725C00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL7140725C00088210',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140703C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL7140703C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140711C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140719C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL7140719C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140725C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL7140725C00088570',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140703C00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140711C00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140725C00088930',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140703C00089000',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140711C00089000',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140725C00089000',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140703C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140703C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140711C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140719C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140719C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140725C00089290',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140703C00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140711C00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140725C00089640',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140703C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140703C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140711C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140711C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140719C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140719C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140725C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140725C00090000',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140703C00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL7140703C00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140711C00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL7140711C00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140725C00090360',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140703C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140703C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140711C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140711C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140719C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140719C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140725C00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140725C00090710',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140703C00091000',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140711C00091000',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140725C00091000',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140703C00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL7140703C00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140711C00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL7140711C00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140725C00091070',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140703C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140703C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140711C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140711C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140719C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140719C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140725C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140725C00091430',
#[Out]#  '/q/op?s=AAPL&k=91.790001',
#[Out]#  '/q?s=AAPL140711C00091790',
#[Out]#  '/q/op?s=AAPL&k=91.790001',
#[Out]#  '/q?s=AAPL140725C00091790',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140703C00092000',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140711C00092000',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140725C00092000',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140711C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL7140711C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140719C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL7140719C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140725C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL7140725C00092140',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL140711C00092500',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL7140711C00092500',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL140725C00092500',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL7140725C00092500',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140703C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140703C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140711C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140711C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140719C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140719C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140725C00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140725C00092860',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140703C00093000',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140711C00093000',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140725C00093000',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL140711C00093210',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL7140711C00093210',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL140725C00093210',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL7140725C00093210',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140711C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL7140711C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140719C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL7140719C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140725C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL7140725C00093570',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL140711C00093930',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL7140711C00093930',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL140725C00093930',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL7140725C00093930',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140703C00094000',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140711C00094000',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140725C00094000',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140703C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140711C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL7140711C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140719C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL7140719C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140725C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL7140725C00094290',
#[Out]#  '/q/op?s=AAPL&k=94.639999',
#[Out]#  '/q?s=AAPL140725C00094640',
#[Out]#  '/q/op?s=AAPL&k=94.639999',
#[Out]#  '/q?s=AAPL7140725C00094640',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140703C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140711C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140719C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL7140719C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140725C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL7140725C00095000',
#[Out]#  '/q/op?s=AAPL&k=95.360001',
#[Out]#  '/q?s=AAPL140725C00095360',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140703C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140711C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL7140711C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140719C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL7140719C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140725C00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL7140725C00095710',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140703C00096000',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140711C00096000',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140725C00096000',
#[Out]#  '/q/op?s=AAPL&k=96.430000',
#[Out]#  '/q?s=AAPL140719C00096430',
#[Out]#  '/q/op?s=AAPL&k=96.430000',
#[Out]#  '/q?s=AAPL7140719C00096430',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140703C00097000',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140711C00097000',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140725C00097000',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140703C00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140711C00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140719C00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL7140719C00097140',
#[Out]#  '/q/op?s=AAPL&k=97.860001',
#[Out]#  '/q?s=AAPL140719C00097860',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140703C00098000',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140711C00098000',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140725C00098000',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140703C00098570',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140711C00098570',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140719C00098570',
#[Out]#  '/q/op?s=AAPL&k=99.000000',
#[Out]#  '/q?s=AAPL140703C00099000',
#[Out]#  '/q/op?s=AAPL&k=99.000000',
#[Out]#  '/q?s=AAPL140711C00099000',
#[Out]#  '/q/op?s=AAPL&k=99.000000',
#[Out]#  '/q?s=AAPL140725C00099000',
#[Out]#  '/q/op?s=AAPL&k=99.290001',
#[Out]#  '/q?s=AAPL140719C00099290',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140703C00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140711C00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140719C00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140725C00100000',
#[Out]#  '/q/op?s=AAPL&k=100.709999',
#[Out]#  '/q?s=AAPL140719C00100710',
#[Out]#  '/q/op?s=AAPL&k=101.000000',
#[Out]#  '/q?s=AAPL140703C00101000',
#[Out]#  '/q/op?s=AAPL&k=101.000000',
#[Out]#  '/q?s=AAPL140711C00101000',
#[Out]#  '/q/op?s=AAPL&k=101.000000',
#[Out]#  '/q?s=AAPL140725C00101000',
#[Out]#  '/q/op?s=AAPL&k=101.430000',
#[Out]#  '/q?s=AAPL140703C00101430',
#[Out]#  '/q/op?s=AAPL&k=101.430000',
#[Out]#  '/q?s=AAPL140711C00101430',
#[Out]#  '/q/op?s=AAPL&k=101.430000',
#[Out]#  '/q?s=AAPL140719C00101430',
#[Out]#  '/q/op?s=AAPL&k=102.000000',
#[Out]#  '/q?s=AAPL140703C00102000',
#[Out]#  '/q/op?s=AAPL&k=102.000000',
#[Out]#  '/q?s=AAPL140711C00102000',
#[Out]#  '/q/op?s=AAPL&k=102.000000',
#[Out]#  '/q?s=AAPL140725C00102000',
#[Out]#  '/q/op?s=AAPL&k=102.139999',
#[Out]#  '/q?s=AAPL140719C00102140',
#[Out]#  '/q/op?s=AAPL&k=102.860001',
#[Out]#  '/q?s=AAPL140703C00102860',
#[Out]#  '/q/op?s=AAPL&k=102.860001',
#[Out]#  '/q?s=AAPL140711C00102860',
#[Out]#  '/q/op?s=AAPL&k=102.860001',
#[Out]#  '/q?s=AAPL140719C00102860',
#[Out]#  '/q/op?s=AAPL&k=103.000000',
#[Out]#  '/q?s=AAPL140703C00103000',
#[Out]#  '/q/op?s=AAPL&k=103.000000',
#[Out]#  '/q?s=AAPL140711C00103000',
#[Out]#  '/q/op?s=AAPL&k=103.000000',
#[Out]#  '/q?s=AAPL140725C00103000',
#[Out]#  '/q/op?s=AAPL&k=103.570000',
#[Out]#  '/q?s=AAPL140719C00103570',
#[Out]#  '/q/op?s=AAPL&k=104.290001',
#[Out]#  '/q?s=AAPL140703C00104290',
#[Out]#  '/q/op?s=AAPL&k=104.290001',
#[Out]#  '/q?s=AAPL140711C00104290',
#[Out]#  '/q/op?s=AAPL&k=104.290001',
#[Out]#  '/q?s=AAPL140719C00104290',
#[Out]#  '/q/op?s=AAPL&k=105.000000',
#[Out]#  '/q?s=AAPL140719C00105000',
#[Out]#  '/q/op?s=AAPL&k=105.709999',
#[Out]#  '/q?s=AAPL140703C00105710',
#[Out]#  '/q/op?s=AAPL&k=105.709999',
#[Out]#  '/q?s=AAPL140711C00105710',
#[Out]#  '/q/op?s=AAPL&k=105.709999',
#[Out]#  '/q?s=AAPL140719C00105710',
#[Out]#  '/q/op?s=AAPL&k=106.430000',
#[Out]#  '/q?s=AAPL140719C00106430',
#[Out]#  '/q/op?s=AAPL&k=107.139999',
#[Out]#  '/q?s=AAPL140703C00107140',
#[Out]#  '/q/op?s=AAPL&k=107.139999',
#[Out]#  '/q?s=AAPL140711C00107140',
#[Out]#  '/q/op?s=AAPL&k=107.139999',
#[Out]#  '/q?s=AAPL140719C00107140',
#[Out]#  '/q/op?s=AAPL&k=107.860001',
#[Out]#  '/q?s=AAPL140719C00107860',
#[Out]#  '/q/op?s=AAPL&k=108.570000',
#[Out]#  '/q?s=AAPL140703C00108570',
#[Out]#  '/q/op?s=AAPL&k=108.570000',
#[Out]#  '/q?s=AAPL140719C00108570',
#[Out]#  '/q/op?s=AAPL&k=109.290001',
#[Out]#  '/q?s=AAPL140719C00109290',
#[Out]#  '/q/op?s=AAPL&k=110.000000',
#[Out]#  '/q?s=AAPL140703C00110000',
#[Out]#  '/q/op?s=AAPL&k=110.000000',
#[Out]#  '/q?s=AAPL140711C00110000',
#[Out]#  '/q/op?s=AAPL&k=110.000000',
#[Out]#  '/q?s=AAPL140719C00110000',
#[Out]#  '/q/op?s=AAPL&k=110.709999',
#[Out]#  '/q?s=AAPL140719C00110710',
#[Out]#  '/q/op?s=AAPL&k=111.430000',
#[Out]#  '/q?s=AAPL140703C00111430',
#[Out]#  '/q/op?s=AAPL&k=111.430000',
#[Out]#  '/q?s=AAPL140711C00111430',
#[Out]#  '/q/op?s=AAPL&k=111.430000',
#[Out]#  '/q?s=AAPL140719C00111430',
#[Out]#  '/q/op?s=AAPL&k=112.139999',
#[Out]#  '/q?s=AAPL140719C00112140',
#[Out]#  '/q/op?s=AAPL&k=112.860001',
#[Out]#  '/q?s=AAPL140703C00112860',
#[Out]#  '/q/op?s=AAPL&k=112.860001',
#[Out]#  '/q?s=AAPL140711C00112860',
#[Out]#  '/q/op?s=AAPL&k=112.860001',
#[Out]#  '/q?s=AAPL140719C00112860',
#[Out]#  '/q/op?s=AAPL&k=113.570000',
#[Out]#  '/q?s=AAPL140719C00113570',
#[Out]#  '/q/op?s=AAPL&k=114.290001',
#[Out]#  '/q?s=AAPL140711C00114290',
#[Out]#  '/q/op?s=AAPL&k=114.290001',
#[Out]#  '/q?s=AAPL140719C00114290',
#[Out]#  '/q/op?s=AAPL&k=115.000000',
#[Out]#  '/q?s=AAPL140719C00115000',
#[Out]#  '/q/op?s=AAPL&k=115.709999',
#[Out]#  '/q?s=AAPL140719C00115710',
#[Out]#  '/q/op?s=AAPL&k=116.430000',
#[Out]#  '/q?s=AAPL140719C00116430',
#[Out]#  '/q/op?s=AAPL&k=117.139999',
#[Out]#  '/q?s=AAPL140719C00117140',
#[Out]#  '/q/op?s=AAPL&k=117.860001',
#[Out]#  '/q?s=AAPL140719C00117860',
#[Out]#  '/q/op?s=AAPL&k=118.570000',
#[Out]#  '/q?s=AAPL140719C00118570',
#[Out]#  '/q/op?s=AAPL&k=119.290001',
#[Out]#  '/q?s=AAPL140719C00119290',
#[Out]#  '/q/op?s=AAPL&k=120.000000',
#[Out]#  '/q?s=AAPL140719C00120000',
#[Out]#  '/q/op?s=AAPL&k=120.709999',
#[Out]#  '/q?s=AAPL140719C00120710',
#[Out]#  '/q/op?s=AAPL&k=121.430000',
#[Out]#  '/q?s=AAPL140719C00121430',
#[Out]#  '/q/op?s=AAPL&k=122.139999',
#[Out]#  '/q?s=AAPL140719C00122140',
#[Out]#  '/q/op?s=AAPL&k=125.000000',
#[Out]#  '/q?s=AAPL140719C00125000',
#[Out]#  '/q/op?s=AAPL&k=130.000000',
#[Out]#  '/q?s=AAPL140719C00130000',
#[Out]#  '/q/op?s=AAPL&k=135.000000',
#[Out]#  '/q?s=AAPL140719C00135000',
#[Out]#  '/q/op?s=AAPL&k=140.000000',
#[Out]#  '/q?s=AAPL140719C00140000',
#[Out]#  '/q/op?s=AAPL&k=235.000000',
#[Out]#  '/q?s=AAPL140719C00235000',
#[Out]#  '/q/op?s=AAPL&k=290.000000',
#[Out]#  '/q?s=AAPL140719C00290000',
#[Out]#  '/q/op?s=AAPL&k=300.000000',
#[Out]#  '/q?s=AAPL140719C00300000',
#[Out]#  '/q/op?s=AAPL&k=310.000000',
#[Out]#  '/q?s=AAPL140719C00310000',
#[Out]#  '/q/op?s=AAPL&k=340.000000',
#[Out]#  '/q?s=AAPL140719C00340000',
#[Out]#  '/q/op?s=AAPL&k=345.000000',
#[Out]#  '/q?s=AAPL140719C00345000',
#[Out]#  '/q/op?s=AAPL&k=350.000000',
#[Out]#  '/q?s=AAPL140719C00350000',
#[Out]#  '/q/op?s=AAPL&k=365.000000',
#[Out]#  '/q?s=AAPL140719C00365000',
#[Out]#  '/q/op?s=AAPL&k=375.000000',
#[Out]#  '/q?s=AAPL7140719C00375000',
#[Out]#  '/q/op?s=AAPL&k=380.000000',
#[Out]#  '/q?s=AAPL140719C00380000',
#[Out]#  '/q/op?s=AAPL&k=380.000000',
#[Out]#  '/q?s=AAPL7140719C00380000',
#[Out]#  '/q/op?s=AAPL&k=385.000000',
#[Out]#  '/q?s=AAPL140719C00385000',
#[Out]#  '/q/op?s=AAPL&k=395.000000',
#[Out]#  '/q?s=AAPL140719C00395000',
#[Out]#  '/q/op?s=AAPL&k=395.000000',
#[Out]#  '/q?s=AAPL7140719C00395000',
#[Out]#  '/q/op?s=AAPL&k=400.000000',
#[Out]#  '/q?s=AAPL140719C00400000',
#[Out]#  '/q/op?s=AAPL&k=400.000000',
#[Out]#  '/q?s=AAPL7140719C00400000',
#[Out]#  '/q/op?s=AAPL&k=405.000000',
#[Out]#  '/q?s=AAPL140719C00405000',
#[Out]#  '/q/op?s=AAPL&k=410.000000',
#[Out]#  '/q?s=AAPL140719C00410000',
#[Out]#  '/q/op?s=AAPL&k=415.000000',
#[Out]#  '/q?s=AAPL140719C00415000',
#[Out]#  '/q/op?s=AAPL&k=415.000000',
#[Out]#  '/q?s=AAPL7140719C00415000',
#[Out]#  '/q/op?s=AAPL&k=420.000000',
#[Out]#  '/q?s=AAPL140719C00420000',
#[Out]#  '/q/op?s=AAPL&k=420.000000',
#[Out]#  '/q?s=AAPL7140719C00420000',
#[Out]#  '/q/op?s=AAPL&k=425.000000',
#[Out]#  '/q?s=AAPL140719C00425000',
#[Out]#  '/q/op?s=AAPL&k=425.000000',
#[Out]#  '/q?s=AAPL7140719C00425000',
#[Out]#  '/q/op?s=AAPL&k=430.000000',
#[Out]#  '/q?s=AAPL140719C00430000',
#[Out]#  '/q/op?s=AAPL&k=430.000000',
#[Out]#  '/q?s=AAPL7140719C00430000',
#[Out]#  '/q/op?s=AAPL&k=435.000000',
#[Out]#  '/q?s=AAPL140719C00435000',
#[Out]#  '/q/op?s=AAPL&k=440.000000',
#[Out]#  '/q?s=AAPL140719C00440000',
#[Out]#  '/q/op?s=AAPL&k=440.000000',
#[Out]#  '/q?s=AAPL7140719C00440000',
#[Out]#  '/q/op?s=AAPL&k=445.000000',
#[Out]#  '/q?s=AAPL140719C00445000',
#[Out]#  '/q/op?s=AAPL&k=445.000000',
#[Out]#  '/q?s=AAPL7140719C00445000',
#[Out]#  '/q/op?s=AAPL&k=450.000000',
#[Out]#  '/q?s=AAPL140719C00450000',
#[Out]#  '/q/op?s=AAPL&k=450.000000',
#[Out]#  '/q?s=AAPL7140719C00450000',
#[Out]#  '/q/op?s=AAPL&k=455.000000',
#[Out]#  '/q?s=AAPL140719C00455000',
#[Out]#  '/q/op?s=AAPL&k=455.000000',
#[Out]#  '/q?s=AAPL7140719C00455000',
#[Out]#  '/q/op?s=AAPL&k=460.000000',
#[Out]#  '/q?s=AAPL140719C00460000',
#[Out]#  '/q/op?s=AAPL&k=460.000000',
#[Out]#  '/q?s=AAPL7140719C00460000',
#[Out]#  '/q/op?s=AAPL&k=465.000000',
#[Out]#  '/q?s=AAPL140719C00465000',
#[Out]#  '/q/op?s=AAPL&k=465.000000',
#[Out]#  '/q?s=AAPL7140719C00465000',
#[Out]#  '/q/op?s=AAPL&k=470.000000',
#[Out]#  '/q?s=AAPL140719C00470000',
#[Out]#  '/q/op?s=AAPL&k=470.000000',
#[Out]#  '/q?s=AAPL7140719C00470000',
#[Out]#  '/q/op?s=AAPL&k=475.000000',
#[Out]#  '/q?s=AAPL140719C00475000',
#[Out]#  '/q/op?s=AAPL&k=475.000000',
#[Out]#  '/q?s=AAPL7140719C00475000',
#[Out]#  '/q/op?s=AAPL&k=480.000000',
#[Out]#  '/q?s=AAPL140719C00480000',
#[Out]#  '/q/op?s=AAPL&k=480.000000',
#[Out]#  '/q?s=AAPL7140719C00480000',
#[Out]#  '/q/op?s=AAPL&k=485.000000',
#[Out]#  '/q?s=AAPL140719C00485000',
#[Out]#  '/q/op?s=AAPL&k=490.000000',
#[Out]#  '/q?s=AAPL140719C00490000',
#[Out]#  '/q/op?s=AAPL&k=490.000000',
#[Out]#  '/q?s=AAPL7140719C00490000',
#[Out]#  '/q/op?s=AAPL&k=495.000000',
#[Out]#  '/q?s=AAPL140719C00495000',
#[Out]#  '/q/op?s=AAPL&k=495.000000',
#[Out]#  '/q?s=AAPL7140719C00495000',
#[Out]#  '/q/op?s=AAPL&k=500.000000',
#[Out]#  '/q?s=AAPL140719C00500000',
#[Out]#  '/q/op?s=AAPL&k=500.000000',
#[Out]#  '/q?s=AAPL7140719C00500000',
#[Out]#  '/q/op?s=AAPL&k=505.000000',
#[Out]#  '/q?s=AAPL140719C00505000',
#[Out]#  '/q/op?s=AAPL&k=505.000000',
#[Out]#  '/q?s=AAPL7140719C00505000',
#[Out]#  '/q/op?s=AAPL&k=510.000000',
#[Out]#  '/q?s=AAPL140719C00510000',
#[Out]#  '/q/op?s=AAPL&k=510.000000',
#[Out]#  '/q?s=AAPL7140719C00510000',
#[Out]#  '/q/op?s=AAPL&k=515.000000',
#[Out]#  '/q?s=AAPL140719C00515000',
#[Out]#  '/q/op?s=AAPL&k=515.000000',
#[Out]#  '/q?s=AAPL7140719C00515000',
#[Out]#  '/q/op?s=AAPL&k=520.000000',
#[Out]#  '/q?s=AAPL140719C00520000',
#[Out]#  '/q/op?s=AAPL&k=520.000000',
#[Out]#  '/q?s=AAPL7140719C00520000',
#[Out]#  '/q/op?s=AAPL&k=525.000000',
#[Out]#  '/q?s=AAPL140719C00525000',
#[Out]#  '/q/op?s=AAPL&k=525.000000',
#[Out]#  '/q?s=AAPL7140719C00525000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL140719C00530000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL7140719C00530000',
#[Out]#  '/q/op?s=AAPL&k=535.000000',
#[Out]#  '/q?s=AAPL140719C00535000',
#[Out]#  '/q/op?s=AAPL&k=535.000000',
#[Out]#  '/q?s=AAPL7140719C00535000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL140719C00540000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL7140719C00540000',
#[Out]#  '/q/op?s=AAPL&k=545.000000',
#[Out]#  '/q?s=AAPL140719C00545000',
#[Out]#  '/q/op?s=AAPL&k=545.000000',
#[Out]#  '/q?s=AAPL7140719C00545000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140703C00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140719C00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL7140719C00550000',
#[Out]#  '/q/op?s=AAPL&k=555.000000',
#[Out]#  '/q?s=AAPL140719C00555000',
#[Out]#  '/q/op?s=AAPL&k=555.000000',
#[Out]#  '/q?s=AAPL7140719C00555000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140703C00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140711C00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140719C00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL7140719C00560000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL140719C00565000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL7140719C00565000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140703C00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140719C00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL7140719C00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140725C00570000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140703C00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140719C00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL7140719C00575000',
#[Out]#  '/q/op?s=AAPL&k=577.500000',
#[Out]#  '/q?s=AAPL140703C00577500',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140703C00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140719C00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL7140719C00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140725C00580000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140703C00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140719C00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL7140719C00585000',
#[Out]#  '/q/op?s=AAPL&k=587.500000',
#[Out]#  '/q?s=AAPL140703C00587500',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140703C00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140711C00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140719C00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL7140719C00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140725C00590000',
#[Out]#  '/q/op?s=AAPL&k=592.500000',
#[Out]#  '/q?s=AAPL140703C00592500',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140703C00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140711C00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140719C00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL7140719C00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140725C00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL7140725C00595000',
#[Out]#  '/q/op?s=AAPL&k=597.500000',
#[Out]#  '/q?s=AAPL140703C00597500',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140703C00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140703C00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140711C00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140719C00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140719C00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140725C00600000',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL140703C00602500',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL140711C00602500',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140703C00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140703C00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140711C00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140711C00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140719C00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140719C00605000',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL140703C00607500',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL140711C00607500',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140703C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140703C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140711C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140711C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140719C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140719C00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140725C00610000',
#[Out]#  '/q/op?s=AAPL&k=612.500000',
#[Out]#  '/q?s=AAPL140703C00612500',
#[Out]#  '/q/op?s=AAPL&k=612.500000',
#[Out]#  '/q?s=AAPL140711C00612500',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140703C00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140711C00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140719C00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL7140719C00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140725C00615000',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL140703C00617500',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL140711C00617500',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140703C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL7140703C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140711C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140719C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL7140719C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140725C00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL7140725C00620000',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL140703C00622500',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL140711C00622500',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140703C00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL7140703C00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140711C00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140719C00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL7140719C00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140725C00625000',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140703C00627500',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140711C00627500',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140725C00627500',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140703C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140703C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140711C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140711C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140719C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140719C00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140725C00630000',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL140703C00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL7140703C00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL140711C00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL7140711C00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL140725C00632500',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140703C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140703C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140711C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140711C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140719C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140719C00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140725C00635000',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL140703C00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL7140703C00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL140711C00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL7140711C00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL140725C00637500',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140703C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL7140703C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140711C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL7140711C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140719C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL7140719C00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140725C00640000',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL140711C00642500',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL140725C00642500',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140711C00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL7140711C00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140719C00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL7140719C00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140725C00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL7140725C00645000',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL140711C00647500',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL7140711C00647500',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL140725C00647500',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL7140725C00647500',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140703C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140703C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140711C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140711C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140719C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140719C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140725C00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140725C00650000',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL140711C00652500',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL7140711C00652500',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL140725C00652500',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL7140725C00652500',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140711C00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL7140711C00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140719C00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL7140719C00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140725C00655000',
#[Out]#  '/q/op?s=AAPL&k=657.500000',
#[Out]#  '/q?s=AAPL140711C00657500',
#[Out]#  '/q/op?s=AAPL&k=657.500000',
#[Out]#  '/q?s=AAPL7140711C00657500',
#[Out]#  '/q/op?s=AAPL&k=657.500000',
#[Out]#  '/q?s=AAPL140725C00657500',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140703C00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140711C00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL7140711C00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140719C00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL7140719C00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140725C00660000',
#[Out]#  '/q/op?s=AAPL&k=662.500000',
#[Out]#  '/q?s=AAPL140725C00662500',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL140719C00665000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL7140719C00665000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL140725C00665000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL7140725C00665000',
#[Out]#  '/q/op?s=AAPL&k=667.500000',
#[Out]#  '/q?s=AAPL140725C00667500',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140703C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140711C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL7140711C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140719C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL7140719C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140725C00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL7140725C00670000',
#[Out]#  '/q/op?s=AAPL&k=675.000000',
#[Out]#  '/q?s=AAPL140719C00675000',
#[Out]#  '/q/op?s=AAPL&k=675.000000',
#[Out]#  '/q?s=AAPL7140719C00675000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL140703C00680000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL140711C00680000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL140719C00680000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL7140719C00680000',
#[Out]#  '/q/op?s=AAPL&k=685.000000',
#[Out]#  '/q?s=AAPL140719C00685000',
#[Out]#  '/q/op?s=AAPL&k=690.000000',
#[Out]#  '/q?s=AAPL140703C00690000',
#[Out]#  '/q/op?s=AAPL&k=690.000000',
#[Out]#  '/q?s=AAPL140711C00690000',
#[Out]#  '/q/op?s=AAPL&k=690.000000',
#[Out]#  '/q?s=AAPL140719C00690000',
#[Out]#  '/q/op?s=AAPL&k=695.000000',
#[Out]#  '/q?s=AAPL140719C00695000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140703C00700000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140711C00700000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140719C00700000',
#[Out]#  '/q/op?s=AAPL&k=705.000000',
#[Out]#  '/q?s=AAPL140719C00705000',
#[Out]#  '/q/op?s=AAPL&k=710.000000',
#[Out]#  '/q?s=AAPL140703C00710000',
#[Out]#  '/q/op?s=AAPL&k=710.000000',
#[Out]#  '/q?s=AAPL140711C00710000',
#[Out]#  '/q/op?s=AAPL&k=710.000000',
#[Out]#  '/q?s=AAPL140719C00710000',
#[Out]#  '/q/op?s=AAPL&k=715.000000',
#[Out]#  '/q?s=AAPL140719C00715000',
#[Out]#  '/q/op?s=AAPL&k=720.000000',
#[Out]#  '/q?s=AAPL140703C00720000',
#[Out]#  '/q/op?s=AAPL&k=720.000000',
#[Out]#  '/q?s=AAPL140711C00720000',
#[Out]#  '/q/op?s=AAPL&k=720.000000',
#[Out]#  '/q?s=AAPL140719C00720000',
#[Out]#  '/q/op?s=AAPL&k=725.000000',
#[Out]#  '/q?s=AAPL140719C00725000',
#[Out]#  '/q/op?s=AAPL&k=730.000000',
#[Out]#  '/q?s=AAPL140703C00730000',
#[Out]#  '/q/op?s=AAPL&k=730.000000',
#[Out]#  '/q?s=AAPL140719C00730000',
#[Out]#  '/q/op?s=AAPL&k=735.000000',
#[Out]#  '/q?s=AAPL140719C00735000',
#[Out]#  '/q/op?s=AAPL&k=740.000000',
#[Out]#  '/q?s=AAPL140703C00740000',
#[Out]#  '/q/op?s=AAPL&k=740.000000',
#[Out]#  '/q?s=AAPL140711C00740000',
#[Out]#  '/q/op?s=AAPL&k=740.000000',
#[Out]#  '/q?s=AAPL140719C00740000',
#[Out]#  '/q/op?s=AAPL&k=745.000000',
#[Out]#  '/q?s=AAPL140719C00745000',
#[Out]#  '/q/op?s=AAPL&k=750.000000',
#[Out]#  '/q?s=AAPL140711C00750000',
#[Out]#  '/q/op?s=AAPL&k=750.000000',
#[Out]#  '/q?s=AAPL140719C00750000',
#[Out]#  '/q/op?s=AAPL&k=755.000000',
#[Out]#  '/q?s=AAPL140719C00755000',
#[Out]#  '/q/op?s=AAPL&k=760.000000',
#[Out]#  '/q?s=AAPL140703C00760000',
#[Out]#  '/q/op?s=AAPL&k=760.000000',
#[Out]#  '/q?s=AAPL140719C00760000',
#[Out]#  '/q/op?s=AAPL&k=765.000000',
#[Out]#  '/q?s=AAPL140719C00765000',
#[Out]#  '/q/op?s=AAPL&k=770.000000',
#[Out]#  '/q?s=AAPL140703C00770000',
#[Out]#  '/q/op?s=AAPL&k=770.000000',
#[Out]#  '/q?s=AAPL140719C00770000',
#[Out]#  '/q/op?s=AAPL&k=775.000000',
#[Out]#  '/q?s=AAPL140719C00775000',
#[Out]#  '/q/op?s=AAPL&k=780.000000',
#[Out]#  '/q?s=AAPL140703C00780000',
#[Out]#  '/q/op?s=AAPL&k=780.000000',
#[Out]#  '/q?s=AAPL140719C00780000',
#[Out]#  '/q/op?s=AAPL&k=785.000000',
#[Out]#  '/q?s=AAPL140719C00785000',
#[Out]#  '/q/op?s=AAPL&k=790.000000',
#[Out]#  '/q?s=AAPL140703C00790000',
#[Out]#  '/q/op?s=AAPL&k=790.000000',
#[Out]#  '/q?s=AAPL140711C00790000',
#[Out]#  '/q/op?s=AAPL&k=790.000000',
#[Out]#  '/q?s=AAPL140719C00790000',
#[Out]#  '/q/op?s=AAPL&k=795.000000',
#[Out]#  '/q?s=AAPL140719C00795000',
#[Out]#  '/q/op?s=AAPL&k=800.000000',
#[Out]#  '/q?s=AAPL140719C00800000',
#[Out]#  '/q/op?s=AAPL&k=805.000000',
#[Out]#  '/q?s=AAPL140719C00805000',
#[Out]#  '/q/op?s=AAPL&k=810.000000',
#[Out]#  '/q?s=AAPL140719C00810000',
#[Out]#  '/q/op?s=AAPL&k=815.000000',
#[Out]#  '/q?s=AAPL140719C00815000',
#[Out]#  '/q/op?s=AAPL&k=820.000000',
#[Out]#  '/q?s=AAPL140719C00820000',
#[Out]#  '/q/op?s=AAPL&k=825.000000',
#[Out]#  '/q?s=AAPL140719C00825000',
#[Out]#  '/q/op?s=AAPL&k=830.000000',
#[Out]#  '/q?s=AAPL140719C00830000',
#[Out]#  '/q/op?s=AAPL&k=835.000000',
#[Out]#  '/q?s=AAPL140719C00835000',
#[Out]#  '/q/op?s=AAPL&k=840.000000',
#[Out]#  '/q?s=AAPL140719C00840000',
#[Out]#  '/q/op?s=AAPL&k=845.000000',
#[Out]#  '/q?s=AAPL140719C00845000',
#[Out]#  '/q/op?s=AAPL&k=850.000000',
#[Out]#  '/q?s=AAPL140719C00850000',
#[Out]#  '/q/op?s=AAPL&k=855.000000',
#[Out]#  '/q?s=AAPL140719C00855000',
#[Out]#  '/q/op?s=AAPL&k=33.570000',
#[Out]#  '/q?s=AAPL140719P00033570',
#[Out]#  '/q/op?s=AAPL&k=34.290001',
#[Out]#  '/q?s=AAPL140719P00034290',
#[Out]#  '/q/op?s=AAPL&k=35.000000',
#[Out]#  '/q?s=AAPL140719P00035000',
#[Out]#  '/q/op?s=AAPL&k=35.709999',
#[Out]#  '/q?s=AAPL140719P00035710',
#[Out]#  '/q/op?s=AAPL&k=36.430000',
#[Out]#  '/q?s=AAPL140719P00036430',
#[Out]#  '/q/op?s=AAPL&k=37.139999',
#[Out]#  '/q?s=AAPL140719P00037140',
#[Out]#  '/q/op?s=AAPL&k=37.860001',
#[Out]#  '/q?s=AAPL140719P00037860',
#[Out]#  '/q/op?s=AAPL&k=38.570000',
#[Out]#  '/q?s=AAPL140719P00038570',
#[Out]#  '/q/op?s=AAPL&k=39.290001',
#[Out]#  '/q?s=AAPL140719P00039290',
#[Out]#  '/q/op?s=AAPL&k=40.000000',
#[Out]#  '/q?s=AAPL140719P00040000',
#[Out]#  '/q/op?s=AAPL&k=40.709999',
#[Out]#  '/q?s=AAPL140719P00040710',
#[Out]#  '/q/op?s=AAPL&k=41.430000',
#[Out]#  '/q?s=AAPL140719P00041430',
#[Out]#  '/q/op?s=AAPL&k=42.139999',
#[Out]#  '/q?s=AAPL140719P00042140',
#[Out]#  '/q/op?s=AAPL&k=42.860001',
#[Out]#  '/q?s=AAPL140719P00042860',
#[Out]#  '/q/op?s=AAPL&k=43.570000',
#[Out]#  '/q?s=AAPL140719P00043570',
#[Out]#  '/q/op?s=AAPL&k=44.290001',
#[Out]#  '/q?s=AAPL140719P00044290',
#[Out]#  '/q/op?s=AAPL&k=45.000000',
#[Out]#  '/q?s=AAPL140719P00045000',
#[Out]#  '/q/op?s=AAPL&k=45.709999',
#[Out]#  '/q?s=AAPL140719P00045710',
#[Out]#  '/q/op?s=AAPL&k=46.430000',
#[Out]#  '/q?s=AAPL140719P00046430',
#[Out]#  '/q/op?s=AAPL&k=47.139999',
#[Out]#  '/q?s=AAPL140719P00047140',
#[Out]#  '/q/op?s=AAPL&k=47.860001',
#[Out]#  '/q?s=AAPL140719P00047860',
#[Out]#  '/q/op?s=AAPL&k=48.570000',
#[Out]#  '/q?s=AAPL140719P00048570',
#[Out]#  '/q/op?s=AAPL&k=49.290001',
#[Out]#  '/q?s=AAPL140719P00049290',
#[Out]#  '/q/op?s=AAPL&k=50.000000',
#[Out]#  '/q?s=AAPL140719P00050000',
#[Out]#  '/q/op?s=AAPL&k=50.709999',
#[Out]#  '/q?s=AAPL140719P00050710',
#[Out]#  '/q/op?s=AAPL&k=51.430000',
#[Out]#  '/q?s=AAPL140719P00051430',
#[Out]#  '/q/op?s=AAPL&k=52.139999',
#[Out]#  '/q?s=AAPL140719P00052140',
#[Out]#  '/q/op?s=AAPL&k=52.860001',
#[Out]#  '/q?s=AAPL140719P00052860',
#[Out]#  '/q/op?s=AAPL&k=52.860001',
#[Out]#  '/q?s=AAPL7140719P00052860',
#[Out]#  '/q/op?s=AAPL&k=53.570000',
#[Out]#  '/q?s=AAPL140719P00053570',
#[Out]#  '/q/op?s=AAPL&k=53.570000',
#[Out]#  '/q?s=AAPL7140719P00053570',
#[Out]#  '/q/op?s=AAPL&k=54.290001',
#[Out]#  '/q?s=AAPL140719P00054290',
#[Out]#  '/q/op?s=AAPL&k=54.290001',
#[Out]#  '/q?s=AAPL7140719P00054290',
#[Out]#  '/q/op?s=AAPL&k=55.000000',
#[Out]#  '/q?s=AAPL140719P00055000',
#[Out]#  '/q/op?s=AAPL&k=55.000000',
#[Out]#  '/q?s=AAPL7140719P00055000',
#[Out]#  '/q/op?s=AAPL&k=55.709999',
#[Out]#  '/q?s=AAPL140719P00055710',
#[Out]#  '/q/op?s=AAPL&k=55.709999',
#[Out]#  '/q?s=AAPL7140719P00055710',
#[Out]#  '/q/op?s=AAPL&k=56.430000',
#[Out]#  '/q?s=AAPL140719P00056430',
#[Out]#  '/q/op?s=AAPL&k=56.430000',
#[Out]#  '/q?s=AAPL7140719P00056430',
#[Out]#  '/q/op?s=AAPL&k=57.139999',
#[Out]#  '/q?s=AAPL140719P00057140',
#[Out]#  '/q/op?s=AAPL&k=57.139999',
#[Out]#  '/q?s=AAPL7140719P00057140',
#[Out]#  '/q/op?s=AAPL&k=57.860001',
#[Out]#  '/q?s=AAPL140719P00057860',
#[Out]#  '/q/op?s=AAPL&k=57.860001',
#[Out]#  '/q?s=AAPL7140719P00057860',
#[Out]#  '/q/op?s=AAPL&k=58.570000',
#[Out]#  '/q?s=AAPL140719P00058570',
#[Out]#  '/q/op?s=AAPL&k=58.570000',
#[Out]#  '/q?s=AAPL7140719P00058570',
#[Out]#  '/q/op?s=AAPL&k=59.290001',
#[Out]#  '/q?s=AAPL140719P00059290',
#[Out]#  '/q/op?s=AAPL&k=59.290001',
#[Out]#  '/q?s=AAPL7140719P00059290',
#[Out]#  '/q/op?s=AAPL&k=60.000000',
#[Out]#  '/q?s=AAPL140719P00060000',
#[Out]#  '/q/op?s=AAPL&k=60.000000',
#[Out]#  '/q?s=AAPL7140719P00060000',
#[Out]#  '/q/op?s=AAPL&k=60.709999',
#[Out]#  '/q?s=AAPL140719P00060710',
#[Out]#  '/q/op?s=AAPL&k=60.709999',
#[Out]#  '/q?s=AAPL7140719P00060710',
#[Out]#  '/q/op?s=AAPL&k=61.430000',
#[Out]#  '/q?s=AAPL140719P00061430',
#[Out]#  '/q/op?s=AAPL&k=61.430000',
#[Out]#  '/q?s=AAPL7140719P00061430',
#[Out]#  '/q/op?s=AAPL&k=62.139999',
#[Out]#  '/q?s=AAPL140719P00062140',
#[Out]#  '/q/op?s=AAPL&k=62.139999',
#[Out]#  '/q?s=AAPL7140719P00062140',
#[Out]#  '/q/op?s=AAPL&k=62.860001',
#[Out]#  '/q?s=AAPL140719P00062860',
#[Out]#  '/q/op?s=AAPL&k=62.860001',
#[Out]#  '/q?s=AAPL7140719P00062860',
#[Out]#  '/q/op?s=AAPL&k=63.570000',
#[Out]#  '/q?s=AAPL140719P00063570',
#[Out]#  '/q/op?s=AAPL&k=63.570000',
#[Out]#  '/q?s=AAPL7140719P00063570',
#[Out]#  '/q/op?s=AAPL&k=64.290001',
#[Out]#  '/q?s=AAPL140719P00064290',
#[Out]#  '/q/op?s=AAPL&k=64.290001',
#[Out]#  '/q?s=AAPL7140719P00064290',
#[Out]#  '/q/op?s=AAPL&k=65.000000',
#[Out]#  '/q?s=AAPL140719P00065000',
#[Out]#  '/q/op?s=AAPL&k=65.000000',
#[Out]#  '/q?s=AAPL7140719P00065000',
#[Out]#  '/q/op?s=AAPL&k=65.709999',
#[Out]#  '/q?s=AAPL140719P00065710',
#[Out]#  '/q/op?s=AAPL&k=65.709999',
#[Out]#  '/q?s=AAPL7140719P00065710',
#[Out]#  '/q/op?s=AAPL&k=66.430000',
#[Out]#  '/q?s=AAPL140719P00066430',
#[Out]#  '/q/op?s=AAPL&k=66.430000',
#[Out]#  '/q?s=AAPL7140719P00066430',
#[Out]#  '/q/op?s=AAPL&k=67.139999',
#[Out]#  '/q?s=AAPL140719P00067140',
#[Out]#  '/q/op?s=AAPL&k=67.139999',
#[Out]#  '/q?s=AAPL7140719P00067140',
#[Out]#  '/q/op?s=AAPL&k=67.860001',
#[Out]#  '/q?s=AAPL140719P00067860',
#[Out]#  '/q/op?s=AAPL&k=67.860001',
#[Out]#  '/q?s=AAPL7140719P00067860',
#[Out]#  '/q/op?s=AAPL&k=68.570000',
#[Out]#  '/q?s=AAPL140719P00068570',
#[Out]#  '/q/op?s=AAPL&k=68.570000',
#[Out]#  '/q?s=AAPL7140719P00068570',
#[Out]#  '/q/op?s=AAPL&k=69.290001',
#[Out]#  '/q?s=AAPL140719P00069290',
#[Out]#  '/q/op?s=AAPL&k=69.290001',
#[Out]#  '/q?s=AAPL7140719P00069290',
#[Out]#  '/q/op?s=AAPL&k=70.000000',
#[Out]#  '/q?s=AAPL140719P00070000',
#[Out]#  '/q/op?s=AAPL&k=70.000000',
#[Out]#  '/q?s=AAPL7140719P00070000',
#[Out]#  '/q/op?s=AAPL&k=70.709999',
#[Out]#  '/q?s=AAPL140719P00070710',
#[Out]#  '/q/op?s=AAPL&k=70.709999',
#[Out]#  '/q?s=AAPL7140719P00070710',
#[Out]#  '/q/op?s=AAPL&k=71.430000',
#[Out]#  '/q?s=AAPL140719P00071430',
#[Out]#  '/q/op?s=AAPL&k=71.430000',
#[Out]#  '/q?s=AAPL7140719P00071430',
#[Out]#  '/q/op?s=AAPL&k=72.139999',
#[Out]#  '/q?s=AAPL140719P00072140',
#[Out]#  '/q/op?s=AAPL&k=72.139999',
#[Out]#  '/q?s=AAPL7140719P00072140',
#[Out]#  '/q/op?s=AAPL&k=72.860001',
#[Out]#  '/q?s=AAPL140719P00072860',
#[Out]#  '/q/op?s=AAPL&k=72.860001',
#[Out]#  '/q?s=AAPL7140719P00072860',
#[Out]#  '/q/op?s=AAPL&k=73.570000',
#[Out]#  '/q?s=AAPL140719P00073570',
#[Out]#  '/q/op?s=AAPL&k=73.570000',
#[Out]#  '/q?s=AAPL7140719P00073570',
#[Out]#  '/q/op?s=AAPL&k=74.290001',
#[Out]#  '/q?s=AAPL140719P00074290',
#[Out]#  '/q/op?s=AAPL&k=74.290001',
#[Out]#  '/q?s=AAPL7140719P00074290',
#[Out]#  '/q/op?s=AAPL&k=75.000000',
#[Out]#  '/q?s=AAPL140719P00075000',
#[Out]#  '/q/op?s=AAPL&k=75.000000',
#[Out]#  '/q?s=AAPL7140719P00075000',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL140703P00075710',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL140711P00075710',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL140719P00075710',
#[Out]#  '/q/op?s=AAPL&k=75.709999',
#[Out]#  '/q?s=AAPL7140719P00075710',
#[Out]#  '/q/op?s=AAPL&k=76.430000',
#[Out]#  '/q?s=AAPL140719P00076430',
#[Out]#  '/q/op?s=AAPL&k=76.430000',
#[Out]#  '/q?s=AAPL7140719P00076430',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL140703P00077140',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL140711P00077140',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL140719P00077140',
#[Out]#  '/q/op?s=AAPL&k=77.139999',
#[Out]#  '/q?s=AAPL7140719P00077140',
#[Out]#  '/q/op?s=AAPL&k=77.860001',
#[Out]#  '/q?s=AAPL140719P00077860',
#[Out]#  '/q/op?s=AAPL&k=77.860001',
#[Out]#  '/q?s=AAPL7140719P00077860',
#[Out]#  '/q/op?s=AAPL&k=78.000000',
#[Out]#  '/q?s=AAPL140703P00078000',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140703P00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140711P00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140719P00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL7140719P00078570',
#[Out]#  '/q/op?s=AAPL&k=78.570000',
#[Out]#  '/q?s=AAPL140725P00078570',
#[Out]#  '/q/op?s=AAPL&k=79.000000',
#[Out]#  '/q?s=AAPL140703P00079000',
#[Out]#  '/q/op?s=AAPL&k=79.290001',
#[Out]#  '/q?s=AAPL140719P00079290',
#[Out]#  '/q/op?s=AAPL&k=79.290001',
#[Out]#  '/q?s=AAPL7140719P00079290',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140703P00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140711P00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140719P00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL7140719P00080000',
#[Out]#  '/q/op?s=AAPL&k=80.000000',
#[Out]#  '/q?s=AAPL140725P00080000',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL140703P00080710',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL140711P00080710',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL140719P00080710',
#[Out]#  '/q/op?s=AAPL&k=80.709999',
#[Out]#  '/q?s=AAPL7140719P00080710',
#[Out]#  '/q/op?s=AAPL&k=81.070000',
#[Out]#  '/q?s=AAPL140703P00081070',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140703P00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140711P00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140719P00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL7140719P00081430',
#[Out]#  '/q/op?s=AAPL&k=81.430000',
#[Out]#  '/q?s=AAPL140725P00081430',
#[Out]#  '/q/op?s=AAPL&k=81.790001',
#[Out]#  '/q?s=AAPL140703P00081790',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140703P00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140711P00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140719P00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL7140719P00082140',
#[Out]#  '/q/op?s=AAPL&k=82.139999',
#[Out]#  '/q?s=AAPL140725P00082140',
#[Out]#  '/q/op?s=AAPL&k=82.500000',
#[Out]#  '/q?s=AAPL140703P00082500',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140703P00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL7140703P00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140711P00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140719P00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL7140719P00082860',
#[Out]#  '/q/op?s=AAPL&k=82.860001',
#[Out]#  '/q?s=AAPL140725P00082860',
#[Out]#  '/q/op?s=AAPL&k=83.000000',
#[Out]#  '/q?s=AAPL140703P00083000',
#[Out]#  '/q/op?s=AAPL&k=83.209999',
#[Out]#  '/q?s=AAPL140703P00083210',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140703P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL7140703P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140711P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140719P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL7140719P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.570000',
#[Out]#  '/q?s=AAPL140725P00083570',
#[Out]#  '/q/op?s=AAPL&k=83.930000',
#[Out]#  '/q?s=AAPL140703P00083930',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140703P00084000',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140711P00084000',
#[Out]#  '/q/op?s=AAPL&k=84.000000',
#[Out]#  '/q?s=AAPL140725P00084000',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140703P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL7140703P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140711P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140719P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL7140719P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.290001',
#[Out]#  '/q?s=AAPL140725P00084290',
#[Out]#  '/q/op?s=AAPL&k=84.639999',
#[Out]#  '/q?s=AAPL140703P00084640',
#[Out]#  '/q/op?s=AAPL&k=84.639999',
#[Out]#  '/q?s=AAPL140711P00084640',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140703P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140703P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140711P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140719P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140719P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL140725P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.000000',
#[Out]#  '/q?s=AAPL7140725P00085000',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL140703P00085360',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL7140703P00085360',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL140711P00085360',
#[Out]#  '/q/op?s=AAPL&k=85.360001',
#[Out]#  '/q?s=AAPL7140711P00085360',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140703P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140703P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140711P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140711P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140719P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140719P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL140725P00085710',
#[Out]#  '/q/op?s=AAPL&k=85.709999',
#[Out]#  '/q?s=AAPL7140725P00085710',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140703P00086000',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140711P00086000',
#[Out]#  '/q/op?s=AAPL&k=86.000000',
#[Out]#  '/q?s=AAPL140725P00086000',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL140703P00086070',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL7140703P00086070',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL140711P00086070',
#[Out]#  '/q/op?s=AAPL&k=86.070000',
#[Out]#  '/q?s=AAPL7140711P00086070',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140703P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140703P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140711P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140711P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140719P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140719P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL140725P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.430000',
#[Out]#  '/q?s=AAPL7140725P00086430',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140703P00086790',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140711P00086790',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL7140711P00086790',
#[Out]#  '/q/op?s=AAPL&k=86.790001',
#[Out]#  '/q?s=AAPL140725P00086790',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140703P00087000',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140711P00087000',
#[Out]#  '/q/op?s=AAPL&k=87.000000',
#[Out]#  '/q?s=AAPL140725P00087000',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140703P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140703P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140711P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140711P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140719P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140719P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL140725P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.139999',
#[Out]#  '/q?s=AAPL7140725P00087140',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140703P00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140711P00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL7140711P00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL140725P00087500',
#[Out]#  '/q/op?s=AAPL&k=87.500000',
#[Out]#  '/q?s=AAPL7140725P00087500',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140703P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL7140703P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140711P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL7140711P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140719P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL7140719P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL140725P00087860',
#[Out]#  '/q/op?s=AAPL&k=87.860001',
#[Out]#  '/q?s=AAPL7140725P00087860',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140703P00088000',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140711P00088000',
#[Out]#  '/q/op?s=AAPL&k=88.000000',
#[Out]#  '/q?s=AAPL140725P00088000',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140703P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL7140703P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140711P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL7140711P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL140725P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.209999',
#[Out]#  '/q?s=AAPL7140725P00088210',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140703P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL7140703P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140711P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140719P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL7140719P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.570000',
#[Out]#  '/q?s=AAPL140725P00088570',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140703P00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL7140703P00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140711P00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL140725P00088930',
#[Out]#  '/q/op?s=AAPL&k=88.930000',
#[Out]#  '/q?s=AAPL7140725P00088930',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140703P00089000',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140711P00089000',
#[Out]#  '/q/op?s=AAPL&k=89.000000',
#[Out]#  '/q?s=AAPL140725P00089000',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140703P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140703P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140711P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140711P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140719P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140719P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL140725P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.290001',
#[Out]#  '/q?s=AAPL7140725P00089290',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140703P00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL7140703P00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140711P00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL7140711P00089640',
#[Out]#  '/q/op?s=AAPL&k=89.639999',
#[Out]#  '/q?s=AAPL140725P00089640',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140703P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140703P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140711P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140711P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140719P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140719P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL140725P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.000000',
#[Out]#  '/q?s=AAPL7140725P00090000',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140703P00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL7140703P00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140711P00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL7140711P00090360',
#[Out]#  '/q/op?s=AAPL&k=90.360001',
#[Out]#  '/q?s=AAPL140725P00090360',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140703P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140703P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140711P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140711P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140719P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL7140719P00090710',
#[Out]#  '/q/op?s=AAPL&k=90.709999',
#[Out]#  '/q?s=AAPL140725P00090710',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140703P00091000',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140711P00091000',
#[Out]#  '/q/op?s=AAPL&k=91.000000',
#[Out]#  '/q?s=AAPL140725P00091000',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140703P00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL7140703P00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140711P00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL7140711P00091070',
#[Out]#  '/q/op?s=AAPL&k=91.070000',
#[Out]#  '/q?s=AAPL140725P00091070',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140703P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140703P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140711P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140719P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140719P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL140725P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.430000',
#[Out]#  '/q?s=AAPL7140725P00091430',
#[Out]#  '/q/op?s=AAPL&k=91.790001',
#[Out]#  '/q?s=AAPL140711P00091790',
#[Out]#  '/q/op?s=AAPL&k=91.790001',
#[Out]#  '/q?s=AAPL7140711P00091790',
#[Out]#  '/q/op?s=AAPL&k=91.790001',
#[Out]#  '/q?s=AAPL140725P00091790',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140703P00092000',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140711P00092000',
#[Out]#  '/q/op?s=AAPL&k=92.000000',
#[Out]#  '/q?s=AAPL140725P00092000',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140711P00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL7140711P00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140719P00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL7140719P00092140',
#[Out]#  '/q/op?s=AAPL&k=92.139999',
#[Out]#  '/q?s=AAPL140725P00092140',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL140711P00092500',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL7140711P00092500',
#[Out]#  '/q/op?s=AAPL&k=92.500000',
#[Out]#  '/q?s=AAPL140725P00092500',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140703P00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140703P00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140711P00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140719P00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL7140719P00092860',
#[Out]#  '/q/op?s=AAPL&k=92.860001',
#[Out]#  '/q?s=AAPL140725P00092860',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140703P00093000',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140711P00093000',
#[Out]#  '/q/op?s=AAPL&k=93.000000',
#[Out]#  '/q?s=AAPL140725P00093000',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL140711P00093210',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL7140711P00093210',
#[Out]#  '/q/op?s=AAPL&k=93.209999',
#[Out]#  '/q?s=AAPL140725P00093210',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140711P00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL7140711P00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140719P00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL7140719P00093570',
#[Out]#  '/q/op?s=AAPL&k=93.570000',
#[Out]#  '/q?s=AAPL140725P00093570',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL140711P00093930',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL140725P00093930',
#[Out]#  '/q/op?s=AAPL&k=93.930000',
#[Out]#  '/q?s=AAPL7140725P00093930',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140703P00094000',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140711P00094000',
#[Out]#  '/q/op?s=AAPL&k=94.000000',
#[Out]#  '/q?s=AAPL140725P00094000',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140703P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140711P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL7140711P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140719P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL7140719P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.290001',
#[Out]#  '/q?s=AAPL140725P00094290',
#[Out]#  '/q/op?s=AAPL&k=94.639999',
#[Out]#  '/q?s=AAPL140725P00094640',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140703P00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140711P00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140719P00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL7140719P00095000',
#[Out]#  '/q/op?s=AAPL&k=95.000000',
#[Out]#  '/q?s=AAPL140725P00095000',
#[Out]#  '/q/op?s=AAPL&k=95.360001',
#[Out]#  '/q?s=AAPL140725P00095360',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140703P00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140711P00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL7140711P00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140719P00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL7140719P00095710',
#[Out]#  '/q/op?s=AAPL&k=95.709999',
#[Out]#  '/q?s=AAPL140725P00095710',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140703P00096000',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140711P00096000',
#[Out]#  '/q/op?s=AAPL&k=96.000000',
#[Out]#  '/q?s=AAPL140725P00096000',
#[Out]#  '/q/op?s=AAPL&k=96.430000',
#[Out]#  '/q?s=AAPL140719P00096430',
#[Out]#  '/q/op?s=AAPL&k=96.430000',
#[Out]#  '/q?s=AAPL7140719P00096430',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140703P00097000',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140711P00097000',
#[Out]#  '/q/op?s=AAPL&k=97.000000',
#[Out]#  '/q?s=AAPL140725P00097000',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140703P00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140711P00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL140719P00097140',
#[Out]#  '/q/op?s=AAPL&k=97.139999',
#[Out]#  '/q?s=AAPL7140719P00097140',
#[Out]#  '/q/op?s=AAPL&k=97.860001',
#[Out]#  '/q?s=AAPL140719P00097860',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140703P00098000',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140711P00098000',
#[Out]#  '/q/op?s=AAPL&k=98.000000',
#[Out]#  '/q?s=AAPL140725P00098000',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140703P00098570',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140711P00098570',
#[Out]#  '/q/op?s=AAPL&k=98.570000',
#[Out]#  '/q?s=AAPL140719P00098570',
#[Out]#  '/q/op?s=AAPL&k=99.000000',
#[Out]#  '/q?s=AAPL140703P00099000',
#[Out]#  '/q/op?s=AAPL&k=99.290001',
#[Out]#  '/q?s=AAPL140719P00099290',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140703P00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140711P00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140719P00100000',
#[Out]#  '/q/op?s=AAPL&k=100.000000',
#[Out]#  '/q?s=AAPL140725P00100000',
#[Out]#  '/q/op?s=AAPL&k=100.709999',
#[Out]#  '/q?s=AAPL140719P00100710',
#[Out]#  '/q/op?s=AAPL&k=101.430000',
#[Out]#  '/q?s=AAPL140719P00101430',
#[Out]#  '/q/op?s=AAPL&k=102.000000',
#[Out]#  '/q?s=AAPL140703P00102000',
#[Out]#  '/q/op?s=AAPL&k=102.000000',
#[Out]#  '/q?s=AAPL140725P00102000',
#[Out]#  '/q/op?s=AAPL&k=102.139999',
#[Out]#  '/q?s=AAPL140719P00102140',
#[Out]#  '/q/op?s=AAPL&k=102.860001',
#[Out]#  '/q?s=AAPL140719P00102860',
#[Out]#  '/q/op?s=AAPL&k=103.000000',
#[Out]#  '/q?s=AAPL140725P00103000',
#[Out]#  '/q/op?s=AAPL&k=103.570000',
#[Out]#  '/q?s=AAPL140719P00103570',
#[Out]#  '/q/op?s=AAPL&k=104.290001',
#[Out]#  '/q?s=AAPL140719P00104290',
#[Out]#  '/q/op?s=AAPL&k=105.000000',
#[Out]#  '/q?s=AAPL140719P00105000',
#[Out]#  '/q/op?s=AAPL&k=105.709999',
#[Out]#  '/q?s=AAPL140719P00105710',
#[Out]#  '/q/op?s=AAPL&k=106.430000',
#[Out]#  '/q?s=AAPL140719P00106430',
#[Out]#  '/q/op?s=AAPL&k=107.139999',
#[Out]#  '/q?s=AAPL140719P00107140',
#[Out]#  '/q/op?s=AAPL&k=107.860001',
#[Out]#  '/q?s=AAPL140719P00107860',
#[Out]#  '/q/op?s=AAPL&k=108.570000',
#[Out]#  '/q?s=AAPL140719P00108570',
#[Out]#  '/q/op?s=AAPL&k=109.290001',
#[Out]#  '/q?s=AAPL140719P00109290',
#[Out]#  '/q/op?s=AAPL&k=110.000000',
#[Out]#  '/q?s=AAPL140703P00110000',
#[Out]#  '/q/op?s=AAPL&k=110.000000',
#[Out]#  '/q?s=AAPL140719P00110000',
#[Out]#  '/q/op?s=AAPL&k=110.709999',
#[Out]#  '/q?s=AAPL140719P00110710',
#[Out]#  '/q/op?s=AAPL&k=111.430000',
#[Out]#  '/q?s=AAPL140719P00111430',
#[Out]#  '/q/op?s=AAPL&k=112.139999',
#[Out]#  '/q?s=AAPL140719P00112140',
#[Out]#  '/q/op?s=AAPL&k=112.860001',
#[Out]#  '/q?s=AAPL140719P00112860',
#[Out]#  '/q/op?s=AAPL&k=113.570000',
#[Out]#  '/q?s=AAPL140719P00113570',
#[Out]#  '/q/op?s=AAPL&k=114.290001',
#[Out]#  '/q?s=AAPL140719P00114290',
#[Out]#  '/q/op?s=AAPL&k=115.000000',
#[Out]#  '/q?s=AAPL140719P00115000',
#[Out]#  '/q/op?s=AAPL&k=115.709999',
#[Out]#  '/q?s=AAPL140719P00115710',
#[Out]#  '/q/op?s=AAPL&k=116.430000',
#[Out]#  '/q?s=AAPL140719P00116430',
#[Out]#  '/q/op?s=AAPL&k=117.139999',
#[Out]#  '/q?s=AAPL140719P00117140',
#[Out]#  '/q/op?s=AAPL&k=117.860001',
#[Out]#  '/q?s=AAPL140719P00117860',
#[Out]#  '/q/op?s=AAPL&k=118.570000',
#[Out]#  '/q?s=AAPL140719P00118570',
#[Out]#  '/q/op?s=AAPL&k=119.290001',
#[Out]#  '/q?s=AAPL140719P00119290',
#[Out]#  '/q/op?s=AAPL&k=120.000000',
#[Out]#  '/q?s=AAPL140719P00120000',
#[Out]#  '/q/op?s=AAPL&k=121.430000',
#[Out]#  '/q?s=AAPL140719P00121430',
#[Out]#  '/q/op?s=AAPL&k=122.139999',
#[Out]#  '/q?s=AAPL140719P00122140',
#[Out]#  '/q/op?s=AAPL&k=235.000000',
#[Out]#  '/q?s=AAPL140719P00235000',
#[Out]#  '/q/op?s=AAPL&k=240.000000',
#[Out]#  '/q?s=AAPL140719P00240000',
#[Out]#  '/q/op?s=AAPL&k=245.000000',
#[Out]#  '/q?s=AAPL140719P00245000',
#[Out]#  '/q/op?s=AAPL&k=250.000000',
#[Out]#  '/q?s=AAPL140719P00250000',
#[Out]#  '/q/op?s=AAPL&k=255.000000',
#[Out]#  '/q?s=AAPL140719P00255000',
#[Out]#  '/q/op?s=AAPL&k=260.000000',
#[Out]#  '/q?s=AAPL140719P00260000',
#[Out]#  '/q/op?s=AAPL&k=265.000000',
#[Out]#  '/q?s=AAPL140719P00265000',
#[Out]#  '/q/op?s=AAPL&k=270.000000',
#[Out]#  '/q?s=AAPL140719P00270000',
#[Out]#  '/q/op?s=AAPL&k=275.000000',
#[Out]#  '/q?s=AAPL140719P00275000',
#[Out]#  '/q/op?s=AAPL&k=280.000000',
#[Out]#  '/q?s=AAPL140719P00280000',
#[Out]#  '/q/op?s=AAPL&k=285.000000',
#[Out]#  '/q?s=AAPL140719P00285000',
#[Out]#  '/q/op?s=AAPL&k=290.000000',
#[Out]#  '/q?s=AAPL140719P00290000',
#[Out]#  '/q/op?s=AAPL&k=295.000000',
#[Out]#  '/q?s=AAPL140719P00295000',
#[Out]#  '/q/op?s=AAPL&k=300.000000',
#[Out]#  '/q?s=AAPL140719P00300000',
#[Out]#  '/q/op?s=AAPL&k=305.000000',
#[Out]#  '/q?s=AAPL140719P00305000',
#[Out]#  '/q/op?s=AAPL&k=310.000000',
#[Out]#  '/q?s=AAPL140719P00310000',
#[Out]#  '/q/op?s=AAPL&k=315.000000',
#[Out]#  '/q?s=AAPL140719P00315000',
#[Out]#  '/q/op?s=AAPL&k=320.000000',
#[Out]#  '/q?s=AAPL140719P00320000',
#[Out]#  '/q/op?s=AAPL&k=325.000000',
#[Out]#  '/q?s=AAPL140719P00325000',
#[Out]#  '/q/op?s=AAPL&k=330.000000',
#[Out]#  '/q?s=AAPL140719P00330000',
#[Out]#  '/q/op?s=AAPL&k=335.000000',
#[Out]#  '/q?s=AAPL140719P00335000',
#[Out]#  '/q/op?s=AAPL&k=340.000000',
#[Out]#  '/q?s=AAPL140719P00340000',
#[Out]#  '/q/op?s=AAPL&k=345.000000',
#[Out]#  '/q?s=AAPL140719P00345000',
#[Out]#  '/q/op?s=AAPL&k=350.000000',
#[Out]#  '/q?s=AAPL140719P00350000',
#[Out]#  '/q/op?s=AAPL&k=355.000000',
#[Out]#  '/q?s=AAPL140719P00355000',
#[Out]#  '/q/op?s=AAPL&k=360.000000',
#[Out]#  '/q?s=AAPL140719P00360000',
#[Out]#  '/q/op?s=AAPL&k=365.000000',
#[Out]#  '/q?s=AAPL140719P00365000',
#[Out]#  '/q/op?s=AAPL&k=370.000000',
#[Out]#  '/q?s=AAPL140719P00370000',
#[Out]#  '/q/op?s=AAPL&k=370.000000',
#[Out]#  '/q?s=AAPL7140719P00370000',
#[Out]#  '/q/op?s=AAPL&k=375.000000',
#[Out]#  '/q?s=AAPL140719P00375000',
#[Out]#  '/q/op?s=AAPL&k=375.000000',
#[Out]#  '/q?s=AAPL7140719P00375000',
#[Out]#  '/q/op?s=AAPL&k=380.000000',
#[Out]#  '/q?s=AAPL140719P00380000',
#[Out]#  '/q/op?s=AAPL&k=380.000000',
#[Out]#  '/q?s=AAPL7140719P00380000',
#[Out]#  '/q/op?s=AAPL&k=385.000000',
#[Out]#  '/q?s=AAPL140719P00385000',
#[Out]#  '/q/op?s=AAPL&k=385.000000',
#[Out]#  '/q?s=AAPL7140719P00385000',
#[Out]#  '/q/op?s=AAPL&k=390.000000',
#[Out]#  '/q?s=AAPL140719P00390000',
#[Out]#  '/q/op?s=AAPL&k=390.000000',
#[Out]#  '/q?s=AAPL7140719P00390000',
#[Out]#  '/q/op?s=AAPL&k=395.000000',
#[Out]#  '/q?s=AAPL140719P00395000',
#[Out]#  '/q/op?s=AAPL&k=395.000000',
#[Out]#  '/q?s=AAPL7140719P00395000',
#[Out]#  '/q/op?s=AAPL&k=400.000000',
#[Out]#  '/q?s=AAPL140719P00400000',
#[Out]#  '/q/op?s=AAPL&k=400.000000',
#[Out]#  '/q?s=AAPL7140719P00400000',
#[Out]#  '/q/op?s=AAPL&k=405.000000',
#[Out]#  '/q?s=AAPL140719P00405000',
#[Out]#  '/q/op?s=AAPL&k=405.000000',
#[Out]#  '/q?s=AAPL7140719P00405000',
#[Out]#  '/q/op?s=AAPL&k=410.000000',
#[Out]#  '/q?s=AAPL140719P00410000',
#[Out]#  '/q/op?s=AAPL&k=410.000000',
#[Out]#  '/q?s=AAPL7140719P00410000',
#[Out]#  '/q/op?s=AAPL&k=415.000000',
#[Out]#  '/q?s=AAPL140719P00415000',
#[Out]#  '/q/op?s=AAPL&k=415.000000',
#[Out]#  '/q?s=AAPL7140719P00415000',
#[Out]#  '/q/op?s=AAPL&k=420.000000',
#[Out]#  '/q?s=AAPL140719P00420000',
#[Out]#  '/q/op?s=AAPL&k=420.000000',
#[Out]#  '/q?s=AAPL7140719P00420000',
#[Out]#  '/q/op?s=AAPL&k=425.000000',
#[Out]#  '/q?s=AAPL140719P00425000',
#[Out]#  '/q/op?s=AAPL&k=425.000000',
#[Out]#  '/q?s=AAPL7140719P00425000',
#[Out]#  '/q/op?s=AAPL&k=430.000000',
#[Out]#  '/q?s=AAPL140719P00430000',
#[Out]#  '/q/op?s=AAPL&k=430.000000',
#[Out]#  '/q?s=AAPL7140719P00430000',
#[Out]#  '/q/op?s=AAPL&k=435.000000',
#[Out]#  '/q?s=AAPL140719P00435000',
#[Out]#  '/q/op?s=AAPL&k=435.000000',
#[Out]#  '/q?s=AAPL7140719P00435000',
#[Out]#  '/q/op?s=AAPL&k=440.000000',
#[Out]#  '/q?s=AAPL140719P00440000',
#[Out]#  '/q/op?s=AAPL&k=440.000000',
#[Out]#  '/q?s=AAPL7140719P00440000',
#[Out]#  '/q/op?s=AAPL&k=445.000000',
#[Out]#  '/q?s=AAPL140719P00445000',
#[Out]#  '/q/op?s=AAPL&k=445.000000',
#[Out]#  '/q?s=AAPL7140719P00445000',
#[Out]#  '/q/op?s=AAPL&k=450.000000',
#[Out]#  '/q?s=AAPL140719P00450000',
#[Out]#  '/q/op?s=AAPL&k=450.000000',
#[Out]#  '/q?s=AAPL7140719P00450000',
#[Out]#  '/q/op?s=AAPL&k=455.000000',
#[Out]#  '/q?s=AAPL140719P00455000',
#[Out]#  '/q/op?s=AAPL&k=455.000000',
#[Out]#  '/q?s=AAPL7140719P00455000',
#[Out]#  '/q/op?s=AAPL&k=460.000000',
#[Out]#  '/q?s=AAPL140719P00460000',
#[Out]#  '/q/op?s=AAPL&k=460.000000',
#[Out]#  '/q?s=AAPL7140719P00460000',
#[Out]#  '/q/op?s=AAPL&k=465.000000',
#[Out]#  '/q?s=AAPL140719P00465000',
#[Out]#  '/q/op?s=AAPL&k=465.000000',
#[Out]#  '/q?s=AAPL7140719P00465000',
#[Out]#  '/q/op?s=AAPL&k=470.000000',
#[Out]#  '/q?s=AAPL140719P00470000',
#[Out]#  '/q/op?s=AAPL&k=470.000000',
#[Out]#  '/q?s=AAPL7140719P00470000',
#[Out]#  '/q/op?s=AAPL&k=475.000000',
#[Out]#  '/q?s=AAPL140719P00475000',
#[Out]#  '/q/op?s=AAPL&k=475.000000',
#[Out]#  '/q?s=AAPL7140719P00475000',
#[Out]#  '/q/op?s=AAPL&k=480.000000',
#[Out]#  '/q?s=AAPL140719P00480000',
#[Out]#  '/q/op?s=AAPL&k=480.000000',
#[Out]#  '/q?s=AAPL7140719P00480000',
#[Out]#  '/q/op?s=AAPL&k=485.000000',
#[Out]#  '/q?s=AAPL140719P00485000',
#[Out]#  '/q/op?s=AAPL&k=485.000000',
#[Out]#  '/q?s=AAPL7140719P00485000',
#[Out]#  '/q/op?s=AAPL&k=490.000000',
#[Out]#  '/q?s=AAPL140719P00490000',
#[Out]#  '/q/op?s=AAPL&k=490.000000',
#[Out]#  '/q?s=AAPL7140719P00490000',
#[Out]#  '/q/op?s=AAPL&k=495.000000',
#[Out]#  '/q?s=AAPL140719P00495000',
#[Out]#  '/q/op?s=AAPL&k=495.000000',
#[Out]#  '/q?s=AAPL7140719P00495000',
#[Out]#  '/q/op?s=AAPL&k=500.000000',
#[Out]#  '/q?s=AAPL140719P00500000',
#[Out]#  '/q/op?s=AAPL&k=500.000000',
#[Out]#  '/q?s=AAPL7140719P00500000',
#[Out]#  '/q/op?s=AAPL&k=505.000000',
#[Out]#  '/q?s=AAPL140719P00505000',
#[Out]#  '/q/op?s=AAPL&k=505.000000',
#[Out]#  '/q?s=AAPL7140719P00505000',
#[Out]#  '/q/op?s=AAPL&k=510.000000',
#[Out]#  '/q?s=AAPL140719P00510000',
#[Out]#  '/q/op?s=AAPL&k=510.000000',
#[Out]#  '/q?s=AAPL7140719P00510000',
#[Out]#  '/q/op?s=AAPL&k=515.000000',
#[Out]#  '/q?s=AAPL140719P00515000',
#[Out]#  '/q/op?s=AAPL&k=515.000000',
#[Out]#  '/q?s=AAPL7140719P00515000',
#[Out]#  '/q/op?s=AAPL&k=520.000000',
#[Out]#  '/q?s=AAPL140719P00520000',
#[Out]#  '/q/op?s=AAPL&k=520.000000',
#[Out]#  '/q?s=AAPL7140719P00520000',
#[Out]#  '/q/op?s=AAPL&k=525.000000',
#[Out]#  '/q?s=AAPL140719P00525000',
#[Out]#  '/q/op?s=AAPL&k=525.000000',
#[Out]#  '/q?s=AAPL7140719P00525000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL140703P00530000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL140711P00530000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL140719P00530000',
#[Out]#  '/q/op?s=AAPL&k=530.000000',
#[Out]#  '/q?s=AAPL7140719P00530000',
#[Out]#  '/q/op?s=AAPL&k=535.000000',
#[Out]#  '/q?s=AAPL140719P00535000',
#[Out]#  '/q/op?s=AAPL&k=535.000000',
#[Out]#  '/q?s=AAPL7140719P00535000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL140703P00540000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL140711P00540000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL140719P00540000',
#[Out]#  '/q/op?s=AAPL&k=540.000000',
#[Out]#  '/q?s=AAPL7140719P00540000',
#[Out]#  '/q/op?s=AAPL&k=545.000000',
#[Out]#  '/q?s=AAPL140719P00545000',
#[Out]#  '/q/op?s=AAPL&k=545.000000',
#[Out]#  '/q?s=AAPL7140719P00545000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140703P00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140711P00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140719P00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL7140719P00550000',
#[Out]#  '/q/op?s=AAPL&k=550.000000',
#[Out]#  '/q?s=AAPL140725P00550000',
#[Out]#  '/q/op?s=AAPL&k=555.000000',
#[Out]#  '/q?s=AAPL140719P00555000',
#[Out]#  '/q/op?s=AAPL&k=555.000000',
#[Out]#  '/q?s=AAPL7140719P00555000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140703P00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140711P00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL140719P00560000',
#[Out]#  '/q/op?s=AAPL&k=560.000000',
#[Out]#  '/q?s=AAPL7140719P00560000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL140703P00565000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL140711P00565000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL140719P00565000',
#[Out]#  '/q/op?s=AAPL&k=565.000000',
#[Out]#  '/q?s=AAPL7140719P00565000',
#[Out]#  '/q/op?s=AAPL&k=567.500000',
#[Out]#  '/q?s=AAPL140703P00567500',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140703P00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140711P00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140719P00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL7140719P00570000',
#[Out]#  '/q/op?s=AAPL&k=570.000000',
#[Out]#  '/q?s=AAPL140725P00570000',
#[Out]#  '/q/op?s=AAPL&k=572.500000',
#[Out]#  '/q?s=AAPL140703P00572500',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140703P00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140711P00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140719P00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL7140719P00575000',
#[Out]#  '/q/op?s=AAPL&k=575.000000',
#[Out]#  '/q?s=AAPL140725P00575000',
#[Out]#  '/q/op?s=AAPL&k=577.500000',
#[Out]#  '/q?s=AAPL140703P00577500',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140703P00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL7140703P00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140711P00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140719P00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL7140719P00580000',
#[Out]#  '/q/op?s=AAPL&k=580.000000',
#[Out]#  '/q?s=AAPL140725P00580000',
#[Out]#  '/q/op?s=AAPL&k=582.500000',
#[Out]#  '/q?s=AAPL140703P00582500',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140703P00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL7140703P00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140711P00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140719P00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL7140719P00585000',
#[Out]#  '/q/op?s=AAPL&k=585.000000',
#[Out]#  '/q?s=AAPL140725P00585000',
#[Out]#  '/q/op?s=AAPL&k=587.500000',
#[Out]#  '/q?s=AAPL140703P00587500',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140703P00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL7140703P00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140711P00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140719P00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL7140719P00590000',
#[Out]#  '/q/op?s=AAPL&k=590.000000',
#[Out]#  '/q?s=AAPL140725P00590000',
#[Out]#  '/q/op?s=AAPL&k=592.500000',
#[Out]#  '/q?s=AAPL140703P00592500',
#[Out]#  '/q/op?s=AAPL&k=592.500000',
#[Out]#  '/q?s=AAPL140711P00592500',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140703P00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL7140703P00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140711P00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140719P00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL7140719P00595000',
#[Out]#  '/q/op?s=AAPL&k=595.000000',
#[Out]#  '/q?s=AAPL140725P00595000',
#[Out]#  '/q/op?s=AAPL&k=597.500000',
#[Out]#  '/q?s=AAPL140703P00597500',
#[Out]#  '/q/op?s=AAPL&k=597.500000',
#[Out]#  '/q?s=AAPL7140703P00597500',
#[Out]#  '/q/op?s=AAPL&k=597.500000',
#[Out]#  '/q?s=AAPL140711P00597500',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140703P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140703P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140711P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140711P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140719P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140719P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL140725P00600000',
#[Out]#  '/q/op?s=AAPL&k=600.000000',
#[Out]#  '/q?s=AAPL7140725P00600000',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL140703P00602500',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL7140703P00602500',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL140711P00602500',
#[Out]#  '/q/op?s=AAPL&k=602.500000',
#[Out]#  '/q?s=AAPL7140711P00602500',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140703P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140703P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140711P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140711P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140719P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140719P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL140725P00605000',
#[Out]#  '/q/op?s=AAPL&k=605.000000',
#[Out]#  '/q?s=AAPL7140725P00605000',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL140703P00607500',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL140711P00607500',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL7140711P00607500',
#[Out]#  '/q/op?s=AAPL&k=607.500000',
#[Out]#  '/q?s=AAPL140725P00607500',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140703P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140703P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140711P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140711P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140719P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140719P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL140725P00610000',
#[Out]#  '/q/op?s=AAPL&k=610.000000',
#[Out]#  '/q?s=AAPL7140725P00610000',
#[Out]#  '/q/op?s=AAPL&k=612.500000',
#[Out]#  '/q?s=AAPL140703P00612500',
#[Out]#  '/q/op?s=AAPL&k=612.500000',
#[Out]#  '/q?s=AAPL140711P00612500',
#[Out]#  '/q/op?s=AAPL&k=612.500000',
#[Out]#  '/q?s=AAPL7140711P00612500',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140703P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL7140703P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140711P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL7140711P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140719P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL7140719P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL140725P00615000',
#[Out]#  '/q/op?s=AAPL&k=615.000000',
#[Out]#  '/q?s=AAPL7140725P00615000',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL140703P00617500',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL7140703P00617500',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL140711P00617500',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL140725P00617500',
#[Out]#  '/q/op?s=AAPL&k=617.500000',
#[Out]#  '/q?s=AAPL7140725P00617500',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140703P00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL7140703P00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140711P00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140719P00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL7140719P00620000',
#[Out]#  '/q/op?s=AAPL&k=620.000000',
#[Out]#  '/q?s=AAPL140725P00620000',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL140703P00622500',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL7140703P00622500',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL140711P00622500',
#[Out]#  '/q/op?s=AAPL&k=622.500000',
#[Out]#  '/q?s=AAPL7140725P00622500',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140703P00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL7140703P00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140711P00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL140719P00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL7140719P00625000',
#[Out]#  '/q/op?s=AAPL&k=625.000000',
#[Out]#  '/q?s=AAPL7140725P00625000',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140703P00627500',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL7140703P00627500',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140711P00627500',
#[Out]#  '/q/op?s=AAPL&k=627.500000',
#[Out]#  '/q?s=AAPL140725P00627500',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140703P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140703P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140711P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140711P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140719P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140719P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL140725P00630000',
#[Out]#  '/q/op?s=AAPL&k=630.000000',
#[Out]#  '/q?s=AAPL7140725P00630000',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL140703P00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL7140703P00632500',
#[Out]#  '/q/op?s=AAPL&k=632.500000',
#[Out]#  '/q?s=AAPL140711P00632500',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140703P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140703P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140711P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140711P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140719P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL7140719P00635000',
#[Out]#  '/q/op?s=AAPL&k=635.000000',
#[Out]#  '/q?s=AAPL140725P00635000',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL140703P00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL7140703P00637500',
#[Out]#  '/q/op?s=AAPL&k=637.500000',
#[Out]#  '/q?s=AAPL140711P00637500',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140703P00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140711P00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140719P00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL7140719P00640000',
#[Out]#  '/q/op?s=AAPL&k=640.000000',
#[Out]#  '/q?s=AAPL140725P00640000',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL140711P00642500',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL7140711P00642500',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL140725P00642500',
#[Out]#  '/q/op?s=AAPL&k=642.500000',
#[Out]#  '/q?s=AAPL7140725P00642500',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140711P00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL7140711P00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140719P00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL7140719P00645000',
#[Out]#  '/q/op?s=AAPL&k=645.000000',
#[Out]#  '/q?s=AAPL140725P00645000',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL140711P00647500',
#[Out]#  '/q/op?s=AAPL&k=647.500000',
#[Out]#  '/q?s=AAPL140725P00647500',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140703P00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140703P00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140711P00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140719P00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL7140719P00650000',
#[Out]#  '/q/op?s=AAPL&k=650.000000',
#[Out]#  '/q?s=AAPL140725P00650000',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL140711P00652500',
#[Out]#  '/q/op?s=AAPL&k=652.500000',
#[Out]#  '/q?s=AAPL140725P00652500',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140711P00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL7140711P00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140719P00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL7140719P00655000',
#[Out]#  '/q/op?s=AAPL&k=655.000000',
#[Out]#  '/q?s=AAPL140725P00655000',
#[Out]#  '/q/op?s=AAPL&k=657.500000',
#[Out]#  '/q?s=AAPL140711P00657500',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140703P00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140719P00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL7140719P00660000',
#[Out]#  '/q/op?s=AAPL&k=660.000000',
#[Out]#  '/q?s=AAPL140725P00660000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL140719P00665000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL7140719P00665000',
#[Out]#  '/q/op?s=AAPL&k=665.000000',
#[Out]#  '/q?s=AAPL140725P00665000',
#[Out]#  '/q/op?s=AAPL&k=667.500000',
#[Out]#  '/q?s=AAPL140725P00667500',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140703P00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140711P00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL7140711P00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140719P00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL7140719P00670000',
#[Out]#  '/q/op?s=AAPL&k=670.000000',
#[Out]#  '/q?s=AAPL140725P00670000',
#[Out]#  '/q/op?s=AAPL&k=675.000000',
#[Out]#  '/q?s=AAPL140719P00675000',
#[Out]#  '/q/op?s=AAPL&k=675.000000',
#[Out]#  '/q?s=AAPL7140719P00675000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL140703P00680000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL140719P00680000',
#[Out]#  '/q/op?s=AAPL&k=680.000000',
#[Out]#  '/q?s=AAPL7140719P00680000',
#[Out]#  '/q/op?s=AAPL&k=685.000000',
#[Out]#  '/q?s=AAPL140719P00685000',
#[Out]#  '/q/op?s=AAPL&k=690.000000',
#[Out]#  '/q?s=AAPL140719P00690000',
#[Out]#  '/q/op?s=AAPL&k=695.000000',
#[Out]#  '/q?s=AAPL140719P00695000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140703P00700000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140711P00700000',
#[Out]#  '/q/op?s=AAPL&k=700.000000',
#[Out]#  '/q?s=AAPL140719P00700000',
#[Out]#  '/q/op?s=AAPL&k=705.000000',
#[Out]#  '/q?s=AAPL140719P00705000',
#[Out]#  '/q/op?s=AAPL&k=710.000000',
#[Out]#  '/q?s=AAPL140719P00710000',
#[Out]#  '/q/op?s=AAPL&k=715.000000',
#[Out]#  '/q?s=AAPL140719P00715000',
#[Out]#  '/q/op?s=AAPL&k=720.000000',
#[Out]#  '/q?s=AAPL140719P00720000',
#[Out]#  '/q/op?s=AAPL&k=725.000000',
#[Out]#  '/q?s=AAPL140719P00725000',
#[Out]#  '/q/op?s=AAPL&k=730.000000',
#[Out]#  '/q?s=AAPL140719P00730000',
#[Out]#  '/q/op?s=AAPL&k=740.000000',
#[Out]#  '/q?s=AAPL140711P00740000',
#[Out]#  '/q/op?s=AAPL&k=740.000000',
#[Out]#  '/q?s=AAPL140719P00740000',
#[Out]#  '/q/op?s=AAPL&k=745.000000',
#[Out]#  '/q?s=AAPL140719P00745000',
#[Out]#  '/q/op?s=AAPL&k=750.000000',
#[Out]#  '/q?s=AAPL140711P00750000',
#[Out]#  '/q/op?s=AAPL&k=750.000000',
#[Out]#  '/q?s=AAPL140719P00750000',
#[Out]#  '/q/op?s=AAPL&k=755.000000',
#[Out]#  '/q?s=AAPL140719P00755000',
#[Out]#  '/q/op?s=AAPL&k=760.000000',
#[Out]#  '/q?s=AAPL140719P00760000',
#[Out]#  '/q/op?s=AAPL&k=765.000000',
#[Out]#  '/q?s=AAPL140719P00765000',
#[Out]#  '/q/op?s=AAPL&k=770.000000',
#[Out]#  '/q?s=AAPL140719P00770000',
#[Out]#  '/q/op?s=AAPL&k=775.000000',
#[Out]#  '/q?s=AAPL140719P00775000',
#[Out]#  '/q/op?s=AAPL&k=780.000000',
#[Out]#  '/q?s=AAPL140719P00780000',
#[Out]#  '/q/op?s=AAPL&k=785.000000',
#[Out]#  '/q?s=AAPL140719P00785000',
#[Out]#  '/q/op?s=AAPL&k=790.000000',
#[Out]#  '/q?s=AAPL140719P00790000',
#[Out]#  '/q/op?s=AAPL&k=800.000000',
#[Out]#  '/q?s=AAPL140719P00800000',
#[Out]#  '/q/op?s=AAPL&k=810.000000',
#[Out]#  '/q?s=AAPL140719P00810000',
#[Out]#  '/q/op?s=AAPL&k=820.000000',
#[Out]#  '/q?s=AAPL140719P00820000',
#[Out]#  '/q/op?s=AAPL&k=825.000000',
#[Out]#  '/q?s=AAPL140719P00825000',
#[Out]#  '/q/op?s=AAPL&k=830.000000',
#[Out]#  '/q?s=AAPL140719P00830000',
#[Out]#  '/q/op?s=AAPL&k=835.000000',
#[Out]#  '/q?s=AAPL140719P00835000',
#[Out]#  '/q/op?s=AAPL&k=840.000000',
#[Out]#  '/q?s=AAPL140719P00840000',
#[Out]#  '/q/op?s=AAPL&k=850.000000',
#[Out]#  '/q?s=AAPL140719P00850000',
#[Out]#  '/q/op?s=AAPL&k=855.000000',
#[Out]#  '/q?s=AAPL140719P00855000',
#[Out]#  '/q/os?s=AAPL&m=2014-07-25',
#[Out]#  'http://help.yahoo.com/l/us/yahoo/finance/quotes/fitadelay.html',
#[Out]#  'http://www.capitaliq.com',
#[Out]#  'http://www.csidata.com',
#[Out]#  'http://www.morningstar.com/']
# Sat, 28 Jun 2014 20:39:42
urls[:10]
#[Out]# ['https://www.yahoo.com/',
#[Out]#  'https://mail.yahoo.com/?.intl=us&.lang=en-US&.src=ym',
#[Out]#  'http://news.yahoo.com/',
#[Out]#  'http://sports.yahoo.com/',
#[Out]#  'http://finance.yahoo.com/',
#[Out]#  'https://weather.yahoo.com/',
#[Out]#  'https://games.yahoo.com/',
#[Out]#  'https://groups.yahoo.com/',
#[Out]#  'https://answers.yahoo.com/',
#[Out]#  'https://screen.yahoo.com/']
# Sat, 28 Jun 2014 20:40:05
urls[-10:]
#[Out]# ['/q?s=AAPL140719P00840000',
#[Out]#  '/q/op?s=AAPL&k=850.000000',
#[Out]#  '/q?s=AAPL140719P00850000',
#[Out]#  '/q/op?s=AAPL&k=855.000000',
#[Out]#  '/q?s=AAPL140719P00855000',
#[Out]#  '/q/os?s=AAPL&m=2014-07-25',
#[Out]#  'http://help.yahoo.com/l/us/yahoo/finance/quotes/fitadelay.html',
#[Out]#  'http://www.capitaliq.com',
#[Out]#  'http://www.csidata.com',
#[Out]#  'http://www.morningstar.com/']
# Sat, 28 Jun 2014 20:41:47
content = [lnk.text_content() for lnk in doc.findall('.//a')]
# Sat, 28 Jun 2014 20:42:00
content[-10:]
#[Out]# ['AAPL140719P00840000',
#[Out]#  '850.00',
#[Out]#  'AAPL140719P00850000',
#[Out]#  '855.00',
#[Out]#  'AAPL140719P00855000',
#[Out]#  'Expand to Straddle View...',
#[Out]#  'other exchanges',
#[Out]#  'Capital IQ',
#[Out]#  'Commodity Systems, Inc. (CSI)',
#[Out]#  'Morningstar, Inc.']
# Sat, 28 Jun 2014 20:42:34
tables = doc.findall('.//table')
# Sat, 28 Jun 2014 20:42:45
calls = tables[9]
# Sat, 28 Jun 2014 20:42:54
puts = tables[13]
# Sat, 28 Jun 2014 20:43:29
rows = calls.findall('.//tr')
# Sat, 28 Jun 2014 20:44:29
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]

# Sat, 28 Jun 2014 20:45:10
_unpack(rows[0], kind='th')
#[Out]# ['Strike', 'Symbol', 'Last', 'Chg', 'Bid', 'Ask', 'Vol', 'Open Int']
# Sat, 28 Jun 2014 20:45:42
_unpack(rows[1], kind='td')
#[Out]# ['33.57',
#[Out]#  'AAPL140719C00033570',
#[Out]#  '60.70',
#[Out]#  ' 0.00',
#[Out]#  '57.35',
#[Out]#  '59.40',
#[Out]#  '1',
#[Out]#  '141']
# Sat, 28 Jun 2014 20:46:50
from pandas.io.parsers import TextParser
# Sat, 28 Jun 2014 20:50:02
def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

# Sat, 28 Jun 2014 20:50:33
call_data = parse_options_data(calls)
# Sat, 28 Jun 2014 20:50:47
put_data = parse_options_data(puts)
# Sat, 28 Jun 2014 20:50:55
call_data[:10]
#[Out]#    Strike               Symbol   Last   Chg    Bid    Ask  Vol Open Int
#[Out]# 0   33.57  AAPL140719C00033570  60.70  0.00  57.35  59.40    1      141
#[Out]# 1   40.00  AAPL140719C00040000  51.50  0.00  50.90  52.95    1        1
#[Out]# 2   41.43  AAPL140719C00041430  50.25  6.71  49.50  51.55    7       14
#[Out]# 3   42.86  AAPL140719C00042860  41.86  0.00  48.05  50.10    0       28
#[Out]# 4   44.29  AAPL140719C00044290  47.18  0.00  46.60  48.65   14       14
#[Out]# 5   48.57  AAPL140719C00048570  42.05  0.00  42.35  44.40    0      518
#[Out]# 6   49.29  AAPL140719C00049290  35.23  0.00  41.60  43.65    0       42
#[Out]# 7   50.00  AAPL140719C00050000  40.35  0.00  40.90  42.35  133      823
#[Out]# 8   52.14  AAPL140719C00052140  35.08  0.00  38.75  40.80    3        7
#[Out]# 9   54.29  AAPL140719C00054290  36.50  0.00  36.60  38.65   21       42
#[Out]# 
#[Out]# [10 rows x 8 columns]
# Sun, 29 Jun 2014 22:53:50
from lxml import objectify
# Sun, 29 Jun 2014 22:54:44
path = 'Performance_MNR.xml'
# Sun, 29 Jun 2014 22:54:56
parsed = objectify.parse(open(path))
# Sun, 29 Jun 2014 23:01:58
parsed = objectify.parse(open(path))
# Sun, 29 Jun 2014 23:02:14
root = parsed.getroot()
# Sun, 29 Jun 2014 23:02:38
root.INDICATOR
# Sun, 29 Jun 2014 23:02:49
root
#[Out]# <Element INDICATOR at 0xa26f908>
# Sun, 29 Jun 2014 23:03:58
data = []
# Sun, 29 Jun 2014 23:04:36
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',
'DESIRED_CHANGE', 'DECIMAL_PLACES']
# Sun, 29 Jun 2014 23:05:55
for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
    
# Sun, 29 Jun 2014 23:07:51
path = 'Performance_MNR.xml'
# Sun, 29 Jun 2014 23:08:14
parsed = objectify.parse(open(path))
# Sun, 29 Jun 2014 23:08:19
parsed
#[Out]# <lxml.etree._ElementTree at 0xa27e6c8>
# Sun, 29 Jun 2014 23:08:34
root = parsed.getroot()
# Sun, 29 Jun 2014 23:08:37
root
#[Out]# <Element INDICATOR at 0xbd6ce08>
# Sun, 29 Jun 2014 23:11:08
from StringIO import StringIO
# Sun, 29 Jun 2014 23:11:46
tag = '<a href="http://www.google.com">Google</a>'
# Sun, 29 Jun 2014 23:12:08
root = objectify.parse(StringIO(tag)).getroot()
# Sun, 29 Jun 2014 23:12:28
root
#[Out]# <Element a at 0xa413d88>
# Sun, 29 Jun 2014 23:12:42
root.get('href')
#[Out]# 'http://www.google.com'
# Sun, 29 Jun 2014 23:12:51
root.text
#[Out]# 'Google'
# Sun, 29 Jun 2014 23:14:18
frame = pd.read_csv('ex1.csv')
# Sun, 29 Jun 2014 23:14:22
frame
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sun, 29 Jun 2014 23:14:56
frame.save('frame_pickle_dm')
# Sun, 29 Jun 2014 23:15:38
pd.load('frame_pickle_dm')
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sun, 29 Jun 2014 23:20:00
store = pd.HDFStore('mydata.h5')
# Sun, 29 Jun 2014 23:20:20
store['obj1'] = frame
# Sun, 29 Jun 2014 23:20:35
store['obj1_col'] = frame'1
# Sun, 29 Jun 2014 23:20:46
store['obj1_col'] = frame['a']
# Sun, 29 Jun 2014 23:20:52
store
#[Out]# <class 'pandas.io.pytables.HDFStore'>
#[Out]# File path: mydata.h5
#[Out]# /obj1                frame        (shape->[3,5])
#[Out]# /obj1_col            series       (shape->[3])  
# Sun, 29 Jun 2014 23:21:30
store['obj1']
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sun, 29 Jun 2014 23:21:39
store['obj1_col']
#[Out]# 0    1
#[Out]# 1    5
#[Out]# 2    9
#[Out]# Name: a, dtype: int64
# Sun, 29 Jun 2014 23:26:06
xls_file = pd.ExcelFile('data.xls')
# Sun, 29 Jun 2014 23:26:14
xls_file = pd.ExcelFile('data.xlsx')
# Sun, 29 Jun 2014 23:26:40
xls_file = pd.ExcelFile('data.xls.xlsx')
# Sun, 29 Jun 2014 23:26:59
table = xls_file.parse('Sheet1')
# Sun, 29 Jun 2014 23:27:07
table
#[Out]#    a   b   c   d message
#[Out]# 0  1   2   3   4   hello
#[Out]# 1  5   6   7   8   world
#[Out]# 2  9  10  11  12     foo
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Sun, 29 Jun 2014 23:28:14
import requests
# Sun, 29 Jun 2014 23:28:49
url = 'http://search.twitter.com/search.json?q=python%20pandas'
# Sun, 29 Jun 2014 23:29:01
resp = requests.get(url)
# Sun, 29 Jun 2014 23:29:04
resp
#[Out]# <Response [401]>
# Sun, 29 Jun 2014 23:34:36
url = 'https://api.twitter.com/1.1/search/tweets.json?q=python%20pandas'
# Sun, 29 Jun 2014 23:34:40
resp = requests.get(url)
# Sun, 29 Jun 2014 23:34:46
resp
#[Out]# <Response [400]>
# Sun, 29 Jun 2014 23:36:17
resp.text[:10]
#[Out]# u'{"errors":'
# Sun, 29 Jun 2014 23:50:20
import sqlite3
# Sun, 29 Jun 2014 23:51:19
query = """
CREATE TABLE test
(a VARCHAR(20, b VARCHAR(20),
c REAL, d INTEGER
);"""
# Sun, 29 Jun 2014 23:51:48
con = sqlite3.connect(':memory:')
# Sun, 29 Jun 2014 23:51:57
con.execute(query)
# Sun, 29 Jun 2014 23:53:17
query = """
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
"""
# Sun, 29 Jun 2014 23:53:49
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
);"""
# Sun, 29 Jun 2014 23:54:11
con = sqlite3.connect(':memory:')
# Sun, 29 Jun 2014 23:54:18
con.execute(query)
#[Out]# <sqlite3.Cursor at 0xc319dc0>
# Sun, 29 Jun 2014 23:54:37
con.commit()
# Sun, 29 Jun 2014 23:55:51
data = [('Atlanta', 'Georgia', 1.25, 6),
('Tallahassee', 'Florida', 2.6, 3),
('Sacramento', 'California', 1.7, 5)]
# Sun, 29 Jun 2014 23:56:19
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
# Sun, 29 Jun 2014 23:56:37
con.executemany(stmt, data)
#[Out]# <sqlite3.Cursor at 0x2251180>
# Sun, 29 Jun 2014 23:56:41
con.commit()
# Mon, 30 Jun 2014 00:02:40
cursor = con.execute('select * from test')
# Mon, 30 Jun 2014 00:02:49
rows = cursor.fetchall()
# Mon, 30 Jun 2014 00:02:52
rows
#[Out]# [(u'Atlanta', u'Georgia', 1.25, 6),
#[Out]#  (u'Tallahassee', u'Florida', 2.6, 3),
#[Out]#  (u'Sacramento', u'California', 1.7, 5)]
# Mon, 30 Jun 2014 00:03:31
cursor.description
#[Out]# (('a', None, None, None, None, None, None),
#[Out]#  ('b', None, None, None, None, None, None),
#[Out]#  ('c', None, None, None, None, None, None),
#[Out]#  ('d', None, None, None, None, None, None))
# Mon, 30 Jun 2014 00:04:09
cursor.description[0]
#[Out]# ('a', None, None, None, None, None, None)
# Mon, 30 Jun 2014 00:04:45
zip(cursor.description)
#[Out]# [(('a', None, None, None, None, None, None),),
#[Out]#  (('b', None, None, None, None, None, None),),
#[Out]#  (('c', None, None, None, None, None, None),),
#[Out]#  (('d', None, None, None, None, None, None),)]
# Mon, 30 Jun 2014 00:04:57
zip
#[Out]# <function zip>
# Mon, 30 Jun 2014 00:05:09
cursor.description
#[Out]# (('a', None, None, None, None, None, None),
#[Out]#  ('b', None, None, None, None, None, None),
#[Out]#  ('c', None, None, None, None, None, None),
#[Out]#  ('d', None, None, None, None, None, None))
# Mon, 30 Jun 2014 00:06:05
zip(*cursor.description)
#[Out]# [('a', 'b', 'c', 'd'),
#[Out]#  (None, None, None, None),
#[Out]#  (None, None, None, None),
#[Out]#  (None, None, None, None),
#[Out]#  (None, None, None, None),
#[Out]#  (None, None, None, None),
#[Out]#  (None, None, None, None)]
# Mon, 30 Jun 2014 00:09:17
zip(*cursor.description)[0]
#[Out]# ('a', 'b', 'c', 'd')
# Mon, 30 Jun 2014 00:15:44
DataFrame(rows, columns=zip(*cursor.description)[0])
#[Out]#              a           b     c  d
#[Out]# 0      Atlanta     Georgia  1.25  6
#[Out]# 1  Tallahassee     Florida  2.60  3
#[Out]# 2   Sacramento  California  1.70  5
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Mon, 30 Jun 2014 00:19:43
import pandas.io.sql as sql
# Mon, 30 Jun 2014 00:20:03
sql.read_frame('select * from test', con)
#[Out]#              a           b     c  d
#[Out]# 0      Atlanta     Georgia  1.25  6
#[Out]# 1  Tallahassee     Florida  2.60  3
#[Out]# 2   Sacramento  California  1.70  5
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Mon, 30 Jun 2014 00:23:46
%logstop
