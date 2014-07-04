# IPython log file

# Thu, 05 Jun 2014 01:30:28
from pandas import Series, DataFrame
# Thu, 05 Jun 2014 01:30:47
import pandas as pd
# Thu, 05 Jun 2014 01:31:05
obj = Series([4,7,-5,3])
# Thu, 05 Jun 2014 01:31:08
obj
#[Out]# 0    4
#[Out]# 1    7
#[Out]# 2   -5
#[Out]# 3    3
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:31:40
obj.values
#[Out]# array([ 4,  7, -5,  3], dtype=int64)
# Thu, 05 Jun 2014 01:31:43
obj.index
#[Out]# Int64Index([0, 1, 2, 3], dtype='int64')
# Thu, 05 Jun 2014 01:32:36
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# Thu, 05 Jun 2014 01:32:39
obj2
#[Out]# d    4
#[Out]# b    7
#[Out]# a   -5
#[Out]# c    3
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:32:55
obj2.index
#[Out]# Index([u'd', u'b', u'a', u'c'], dtype='object')
# Thu, 05 Jun 2014 01:33:29
obj2['a']
#[Out]# -5
# Thu, 05 Jun 2014 01:33:43
obj2['d'] = 6
# Thu, 05 Jun 2014 01:34:06
obj2[['c', 'a', 'd']]
#[Out]# c    3
#[Out]# a   -5
#[Out]# d    6
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:34:20
obj2
#[Out]# d    6
#[Out]# b    7
#[Out]# a   -5
#[Out]# c    3
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:35:10
obj2[obj2 > 0]
#[Out]# d    6
#[Out]# b    7
#[Out]# c    3
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:35:19
obj2 * 2
#[Out]# d    12
#[Out]# b    14
#[Out]# a   -10
#[Out]# c     6
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:35:26
np.exp(obj2)
#[Out]# d     403.428793
#[Out]# b    1096.633158
#[Out]# a       0.006738
#[Out]# c      20.085537
#[Out]# dtype: float64
# Thu, 05 Jun 2014 01:37:31
'b' in obj2
#[Out]# True
# Thu, 05 Jun 2014 01:37:35
'e' in obje2
# Thu, 05 Jun 2014 01:37:44
'e' in obj2
#[Out]# False
# Thu, 05 Jun 2014 01:38:31
sdata = {'Ohio': 35000, 'Texas':71000, 'Oregon': 16000, 'Utah': 5000}
# Thu, 05 Jun 2014 01:38:41
obj3 = Series(sdata)
# Thu, 05 Jun 2014 01:38:44
obj3
#[Out]# Ohio      35000
#[Out]# Oregon    16000
#[Out]# Texas     71000
#[Out]# Utah       5000
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:40:08
states = ['California', 'Ohio', 'Oregon', 'Texas']
# Thu, 05 Jun 2014 01:40:27
obj4 = Series(sdata, index=states)
# Thu, 05 Jun 2014 01:40:32
obj4
#[Out]# California      NaN
#[Out]# Ohio          35000
#[Out]# Oregon        16000
#[Out]# Texas         71000
#[Out]# dtype: float64
# Thu, 05 Jun 2014 01:41:18
pd.isnull(obj4)
#[Out]# California     True
#[Out]# Ohio          False
#[Out]# Oregon        False
#[Out]# Texas         False
#[Out]# dtype: bool
# Thu, 05 Jun 2014 01:41:29
pd.notnull(obj4)
#[Out]# California    False
#[Out]# Ohio           True
#[Out]# Oregon         True
#[Out]# Texas          True
#[Out]# dtype: bool
# Thu, 05 Jun 2014 01:42:17
obj3
#[Out]# Ohio      35000
#[Out]# Oregon    16000
#[Out]# Texas     71000
#[Out]# Utah       5000
#[Out]# dtype: int64
# Thu, 05 Jun 2014 01:42:21
obj4
#[Out]# California      NaN
#[Out]# Ohio          35000
#[Out]# Oregon        16000
#[Out]# Texas         71000
#[Out]# dtype: float64
# Thu, 05 Jun 2014 01:42:32
obj3 + obj4
#[Out]# California       NaN
#[Out]# Ohio           70000
#[Out]# Oregon         32000
#[Out]# Texas         142000
#[Out]# Utah             NaN
#[Out]# dtype: float64
# Thu, 05 Jun 2014 01:43:42
obj4.name = 'population'
# Thu, 05 Jun 2014 01:43:53
obj4.index.name = 'state'
# Thu, 05 Jun 2014 01:43:56
obj4
#[Out]# state
#[Out]# California      NaN
#[Out]# Ohio          35000
#[Out]# Oregon        16000
#[Out]# Texas         71000
#[Out]# Name: population, dtype: float64
# Thu, 05 Jun 2014 01:44:28
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
# Thu, 05 Jun 2014 01:44:30
obj
#[Out]# Bob      4
#[Out]# Steve    7
#[Out]# Jeff    -5
#[Out]# Ryan     3
#[Out]# dtype: int64
# Sat, 07 Jun 2014 21:17:50
$logon
# Sat, 07 Jun 2014 21:17:55
%logon
# Sat, 07 Jun 2014 21:21:08
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# Sat, 07 Jun 2014 21:21:16
frame = DataFrame(data)
# Sat, 07 Jun 2014 21:21:23
frame
#[Out]#    pop   state  year
#[Out]# 0  1.5    Ohio  2000
#[Out]# 1  1.7    Ohio  2001
#[Out]# 2  3.6    Ohio  2002
#[Out]# 3  2.4  Nevada  2001
#[Out]# 4  2.9  Nevada  2002
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Sat, 07 Jun 2014 21:22:04
DataFrame(data, columns=['year', 'state', 'pop'])
#[Out]#    year   state  pop
#[Out]# 0  2000    Ohio  1.5
#[Out]# 1  2001    Ohio  1.7
#[Out]# 2  2002    Ohio  3.6
#[Out]# 3  2001  Nevada  2.4
#[Out]# 4  2002  Nevada  2.9
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Sat, 07 Jun 2014 21:23:18
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
index=['one', 'two', 'three', 'four', 'five'])
# Sat, 07 Jun 2014 21:23:22
frame2
#[Out]#        year   state  pop debt
#[Out]# one    2000    Ohio  1.5  NaN
#[Out]# two    2001    Ohio  1.7  NaN
#[Out]# three  2002    Ohio  3.6  NaN
#[Out]# four   2001  Nevada  2.4  NaN
#[Out]# five   2002  Nevada  2.9  NaN
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Sat, 07 Jun 2014 21:23:47
frame2['state']
#[Out]# one        Ohio
#[Out]# two        Ohio
#[Out]# three      Ohio
#[Out]# four     Nevada
#[Out]# five     Nevada
#[Out]# Name: state, dtype: object
# Sat, 07 Jun 2014 21:23:54
frame2.year
#[Out]# one      2000
#[Out]# two      2001
#[Out]# three    2002
#[Out]# four     2001
#[Out]# five     2002
#[Out]# Name: year, dtype: int64
# Sat, 07 Jun 2014 21:24:58
frame2.ix['three']
#[Out]# year     2002
#[Out]# state    Ohio
#[Out]# pop       3.6
#[Out]# debt      NaN
#[Out]# Name: three, dtype: object
# Sat, 07 Jun 2014 21:25:22
frame2['debt'] = 16.5
# Sat, 07 Jun 2014 21:25:24
frame2
#[Out]#        year   state  pop  debt
#[Out]# one    2000    Ohio  1.5  16.5
#[Out]# two    2001    Ohio  1.7  16.5
#[Out]# three  2002    Ohio  3.6  16.5
#[Out]# four   2001  Nevada  2.4  16.5
#[Out]# five   2002  Nevada  2.9  16.5
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Sat, 07 Jun 2014 21:25:46
frame2['debt'] = np.arange(5.)
# Sat, 07 Jun 2014 21:25:49
frame2
#[Out]#        year   state  pop  debt
#[Out]# one    2000    Ohio  1.5     0
#[Out]# two    2001    Ohio  1.7     1
#[Out]# three  2002    Ohio  3.6     2
#[Out]# four   2001  Nevada  2.4     3
#[Out]# five   2002  Nevada  2.9     4
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Sat, 07 Jun 2014 21:28:03
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# Sat, 07 Jun 2014 21:28:13
frame2['debt'] = val
# Sat, 07 Jun 2014 21:28:15
frame2
#[Out]#        year   state  pop  debt
#[Out]# one    2000    Ohio  1.5   NaN
#[Out]# two    2001    Ohio  1.7  -1.2
#[Out]# three  2002    Ohio  3.6   NaN
#[Out]# four   2001  Nevada  2.4  -1.5
#[Out]# five   2002  Nevada  2.9  -1.7
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Sat, 07 Jun 2014 21:29:09
frame2['eastern'] = frame2.state == 'Ohio'
# Sat, 07 Jun 2014 21:29:14
frame2
#[Out]#        year   state  pop  debt eastern
#[Out]# one    2000    Ohio  1.5   NaN    True
#[Out]# two    2001    Ohio  1.7  -1.2    True
#[Out]# three  2002    Ohio  3.6   NaN    True
#[Out]# four   2001  Nevada  2.4  -1.5   False
#[Out]# five   2002  Nevada  2.9  -1.7   False
#[Out]# 
#[Out]# [5 rows x 5 columns]
# Sat, 07 Jun 2014 21:29:41
del frame2['eastern']
# Sat, 07 Jun 2014 21:29:46
frame2.columns
#[Out]# Index([u'year', u'state', u'pop', u'debt'], dtype='object')
# Sat, 07 Jun 2014 21:31:06
pop = {'Nevada': {2001: 2.4, 2002: 2.9},}
# Sat, 07 Jun 2014 21:31:42
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# Sat, 07 Jun 2014 21:32:16
frame3 = DataFrame(pop)
# Sat, 07 Jun 2014 21:32:18
frame3
#[Out]#       Nevada  Ohio
#[Out]# 2000     NaN   1.5
#[Out]# 2001     2.4   1.7
#[Out]# 2002     2.9   3.6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Sat, 07 Jun 2014 21:32:35
frame3.T
#[Out]#         2000  2001  2002
#[Out]# Nevada   NaN   2.4   2.9
#[Out]# Ohio     1.5   1.7   3.6
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Sat, 07 Jun 2014 21:32:53
frame3
#[Out]#       Nevada  Ohio
#[Out]# 2000     NaN   1.5
#[Out]# 2001     2.4   1.7
#[Out]# 2002     2.9   3.6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Sat, 07 Jun 2014 21:33:42
DataFrame(pop, index=[2001, 2002, 2003])
#[Out]#       Nevada  Ohio
#[Out]# 2001     2.4   1.7
#[Out]# 2002     2.9   3.6
#[Out]# 2003     NaN   NaN
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Sat, 07 Jun 2014 21:39:09
pdata = {'Ohio': frame3['Ohio'][:-1],
'Nevada': frame3['Nevada'][:2]}
# Sat, 07 Jun 2014 21:39:17
DataFrame(pdata)
#[Out]#       Nevada  Ohio
#[Out]# 2000     NaN   1.5
#[Out]# 2001     2.4   1.7
#[Out]# 
#[Out]# [2 rows x 2 columns]
# Sat, 07 Jun 2014 21:41:12
frame3.index.name = 'year'; frame3.columns.name = 'state'
# Sat, 07 Jun 2014 21:41:15
frame3
#[Out]# state  Nevada  Ohio
#[Out]# year               
#[Out]# 2000      NaN   1.5
#[Out]# 2001      2.4   1.7
#[Out]# 2002      2.9   3.6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Sat, 07 Jun 2014 21:41:39
frame3.values
#[Out]# array([[ nan,  1.5],
#[Out]#        [ 2.4,  1.7],
#[Out]#        [ 2.9,  3.6]])
# Sat, 07 Jun 2014 21:42:10
frame2.values
#[Out]# array([[2000L, 'Ohio', 1.5, nan],
#[Out]#        [2001L, 'Ohio', 1.7, -1.2],
#[Out]#        [2002L, 'Ohio', 3.6, nan],
#[Out]#        [2001L, 'Nevada', 2.4, -1.5],
#[Out]#        [2002L, 'Nevada', 2.9, -1.7]], dtype=object)
# Sat, 07 Jun 2014 21:43:57
obj = Series(range(3), index=['a', 'b', 'c'])
# Sat, 07 Jun 2014 21:44:02
index = obj.index
# Sat, 07 Jun 2014 21:44:05
index
#[Out]# Index([u'a', u'b', u'c'], dtype='object')
# Sat, 07 Jun 2014 21:44:41
index[1:]
#[Out]# Index([u'b', u'c'], dtype='object')
# Sat, 07 Jun 2014 21:44:50
index[1] = 'd'
# Sat, 07 Jun 2014 21:45:40
index = pd.Index(np.arange(3))
# Sat, 07 Jun 2014 21:46:06
obj2 = Series([1.5, -2.5, 0], index=index)
# Sat, 07 Jun 2014 21:46:13
obj2.index is index
#[Out]# True
# Sat, 07 Jun 2014 21:47:20
frame3
#[Out]# state  Nevada  Ohio
#[Out]# year               
#[Out]# 2000      NaN   1.5
#[Out]# 2001      2.4   1.7
#[Out]# 2002      2.9   3.6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Sat, 07 Jun 2014 21:47:30
'Ohio' in frame3.columns
#[Out]# True
# Sat, 07 Jun 2014 21:49:40
obj
#[Out]# a    0
#[Out]# b    1
#[Out]# c    2
#[Out]# dtype: int64
# Sat, 07 Jun 2014 21:51:17
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# Sat, 07 Jun 2014 21:51:19
obj
#[Out]# d    4.5
#[Out]# b    7.2
#[Out]# a   -5.3
#[Out]# c    3.6
#[Out]# dtype: float64
# Sat, 07 Jun 2014 21:52:01
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# Sat, 07 Jun 2014 21:52:03
obj2
#[Out]# a   -5.3
#[Out]# b    7.2
#[Out]# c    3.6
#[Out]# d    4.5
#[Out]# e    NaN
#[Out]# dtype: float64
# Sat, 07 Jun 2014 21:52:29
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# Sat, 07 Jun 2014 21:52:39
obje
# Sat, 07 Jun 2014 21:52:42
obj2
#[Out]# a   -5.3
#[Out]# b    7.2
#[Out]# c    3.6
#[Out]# d    4.5
#[Out]# e    0.0
#[Out]# dtype: float64
# Sat, 07 Jun 2014 21:52:55
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# Sat, 07 Jun 2014 21:53:12
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
#[Out]# a   -5.3
#[Out]# b    7.2
#[Out]# c    3.6
#[Out]# d    4.5
#[Out]# e    0.0
#[Out]# dtype: float64
# Sat, 07 Jun 2014 21:54:08
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# Sat, 07 Jun 2014 21:54:23
obj3.reindex(range(6), method='ffill')
#[Out]# 0      blue
#[Out]# 1      blue
#[Out]# 2    purple
#[Out]# 3    purple
#[Out]# 4    yellow
#[Out]# 5    yellow
#[Out]# dtype: object
# Sat, 07 Jun 2014 21:56:11
frame = DataFrame(np.arange(9).reshape((3.3)), index=['a', 'c', 'd'],
columns=['Ohio', 'Texas', 'California'])
# Sat, 07 Jun 2014 21:57:06
frame = DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'],
columns=['Ohio', 'Texas', 'California'])
# Sat, 07 Jun 2014 21:57:09
frame
#[Out]#    Ohio  Texas  California
#[Out]# a     0      1           2
#[Out]# c     3      4           5
#[Out]# d     6      7           8
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Sat, 07 Jun 2014 21:57:42
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
# Sat, 07 Jun 2014 21:57:44
frame2
#[Out]#    Ohio  Texas  California
#[Out]# a     0      1           2
#[Out]# b   NaN    NaN         NaN
#[Out]# c     3      4           5
#[Out]# d     6      7           8
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Sat, 07 Jun 2014 21:58:41
states = ['Texas', 'Utah', 'California']
# Sat, 07 Jun 2014 21:58:51
frame.reindex(columns=states)
#[Out]#    Texas  Utah  California
#[Out]# a      1   NaN           2
#[Out]# c      4   NaN           5
#[Out]# d      7   NaN           8
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Sat, 07 Jun 2014 21:59:32
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)
#[Out]#    Texas  Utah  California
#[Out]# a      1   NaN           2
#[Out]# b      1   NaN           2
#[Out]# c      4   NaN           5
#[Out]# d      7   NaN           8
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Sat, 07 Jun 2014 22:00:12
frame.ix[['a', 'b', 'c', 'd'], states]
#[Out]#    Texas  Utah  California
#[Out]# a      1   NaN           2
#[Out]# b    NaN   NaN         NaN
#[Out]# c      4   NaN           5
#[Out]# d      7   NaN           8
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Sat, 07 Jun 2014 22:02:35
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# Sat, 07 Jun 2014 22:02:48
new_obj = obj.drop('c')
# Sat, 07 Jun 2014 22:02:51
new_obj
#[Out]# a    0
#[Out]# b    1
#[Out]# d    3
#[Out]# e    4
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:03:11
obj.drop(['d', 'c'])
#[Out]# a    0
#[Out]# b    1
#[Out]# e    4
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:04:26
data = DataFrame(np.arange(16).reshape((4,4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
columns=['one', 'two', 'three', 'four'])
# Sat, 07 Jun 2014 22:04:29
data
#[Out]#           one  two  three  four
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# Utah        8    9     10    11
#[Out]# New York   12   13     14    15
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Sat, 07 Jun 2014 22:04:48
data.drop(['Colorado', 'Ohio'])
#[Out]#           one  two  three  four
#[Out]# Utah        8    9     10    11
#[Out]# New York   12   13     14    15
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Sat, 07 Jun 2014 22:05:06
data.drop('two', axis=1)
#[Out]#           one  three  four
#[Out]# Ohio        0      2     3
#[Out]# Colorado    4      6     7
#[Out]# Utah        8     10    11
#[Out]# New York   12     14    15
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Sat, 07 Jun 2014 22:05:26
data.drop(['two', 'four'], axis=1)
#[Out]#           one  three
#[Out]# Ohio        0      2
#[Out]# Colorado    4      6
#[Out]# Utah        8     10
#[Out]# New York   12     14
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Sat, 07 Jun 2014 22:07:29
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# Sat, 07 Jun 2014 22:07:33
obj['b
# Sat, 07 Jun 2014 22:07:37
obj['b']
#[Out]# 1.0
# Sat, 07 Jun 2014 22:07:42
obj[1]
#[Out]# 1.0
# Sat, 07 Jun 2014 22:07:48
obj[2:4]
#[Out]# c    2
#[Out]# d    3
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:08:06
obj[['b', 'a', 'd']]
#[Out]# b    1
#[Out]# a    0
#[Out]# d    3
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:08:28
obj[[1, 3]]
#[Out]# b    1
#[Out]# d    3
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:08:44
obj[obj < 2]
#[Out]# a    0
#[Out]# b    1
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:09:39
obj['b':'c']
#[Out]# b    1
#[Out]# c    2
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:09:54
obj['b';'c'] = 5
# Sat, 07 Jun 2014 22:10:02
obj['b':'c'] = 5
# Sat, 07 Jun 2014 22:10:04
obj
#[Out]# a    0
#[Out]# b    5
#[Out]# c    5
#[Out]# d    3
#[Out]# dtype: float64
# Sat, 07 Jun 2014 22:10:24
data
#[Out]#           one  two  three  four
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# Utah        8    9     10    11
#[Out]# New York   12   13     14    15
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Sat, 07 Jun 2014 22:11:28
data['two']
#[Out]# Ohio         1
#[Out]# Colorado     5
#[Out]# Utah         9
#[Out]# New York    13
#[Out]# Name: two, dtype: int32
# Sat, 07 Jun 2014 22:11:44
data[['three', 'one']]
#[Out]#           three  one
#[Out]# Ohio          2    0
#[Out]# Colorado      6    4
#[Out]# Utah         10    8
#[Out]# New York     14   12
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Sat, 07 Jun 2014 22:12:40
data[:2]
#[Out]#           one  two  three  four
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Sat, 07 Jun 2014 22:12:57
data[data['three'] > 5]
#[Out]#           one  two  three  four
#[Out]# Colorado    4    5      6     7
#[Out]# Utah        8    9     10    11
#[Out]# New York   12   13     14    15
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Sat, 07 Jun 2014 22:13:59
data < 5
#[Out]#             one    two  three   four
#[Out]# Ohio       True   True   True   True
#[Out]# Colorado   True  False  False  False
#[Out]# Utah      False  False  False  False
#[Out]# New York  False  False  False  False
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Sat, 07 Jun 2014 22:14:25
data[data < 5] = 0
# Sat, 07 Jun 2014 22:14:26
data
#[Out]#           one  two  three  four
#[Out]# Ohio        0    0      0     0
#[Out]# Colorado    0    5      6     7
#[Out]# Utah        8    9     10    11
#[Out]# New York   12   13     14    15
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Sat, 07 Jun 2014 22:16:01
data[[9, 13]]
# Sat, 07 Jun 2014 22:16:09
data[[9]]
# Sat, 07 Jun 2014 22:18:19
data.ix['Colorado', ['two', 'three']]
#[Out]# two      5
#[Out]# three    6
#[Out]# Name: Colorado, dtype: int32
# Sat, 07 Jun 2014 22:21:17
data.ix[['Colorado', 'Utah'], [3, 0, 1]]
#[Out]#           four  one  two
#[Out]# Colorado     7    0    5
#[Out]# Utah        11    8    9
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Sat, 07 Jun 2014 22:22:01
data.ix[2]
#[Out]# one       8
#[Out]# two       9
#[Out]# three    10
#[Out]# four     11
#[Out]# Name: Utah, dtype: int32
# Sat, 07 Jun 2014 22:22:57
data.ix[:'Utah', 'two']
#[Out]# Ohio        0
#[Out]# Colorado    5
#[Out]# Utah        9
#[Out]# Name: two, dtype: int32
# Sat, 07 Jun 2014 22:24:10
data.ix[:'Utah', 'two':]
#[Out]#           two  three  four
#[Out]# Ohio        0      0     0
#[Out]# Colorado    5      6     7
#[Out]# Utah        9     10    11
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Sat, 07 Jun 2014 22:25:16
data.ix[data.three > 5, :3]
#[Out]#           one  two  three
#[Out]# Colorado    0    5      6
#[Out]# Utah        8    9     10
#[Out]# New York   12   13     14
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Tue, 10 Jun 2014 22:50:04
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# Tue, 10 Jun 2014 22:51:16
s2 = Series([-2.1, 3.6, -1.5, 4, 3.4], index=['a', 'c', 'e', 'f', 'g'])
# Tue, 10 Jun 2014 22:51:20
s1
#[Out]# a    7.3
#[Out]# c   -2.5
#[Out]# d    3.4
#[Out]# e    1.5
#[Out]# dtype: float64
# Tue, 10 Jun 2014 22:51:27
s2
#[Out]# a   -2.1
#[Out]# c    3.6
#[Out]# e   -1.5
#[Out]# f    4.0
#[Out]# g    3.4
#[Out]# dtype: float64
# Tue, 10 Jun 2014 22:51:49
s1 + s2
#[Out]# a    5.2
#[Out]# c    1.1
#[Out]# d    NaN
#[Out]# e    0.0
#[Out]# f    NaN
#[Out]# g    NaN
#[Out]# dtype: float64
# Tue, 10 Jun 2014 22:55:08
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
# Tue, 10 Jun 2014 22:56:17
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# Tue, 10 Jun 2014 22:56:20
df1
#[Out]#           b  c  d
#[Out]# Ohio      0  1  2
#[Out]# Texas     3  4  5
#[Out]# Colorado  6  7  8
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Tue, 10 Jun 2014 22:56:23
df2
#[Out]#         b   d   e
#[Out]# Utah    0   1   2
#[Out]# Ohio    3   4   5
#[Out]# Texas   6   7   8
#[Out]# Oregon  9  10  11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 22:56:32
df1 + df2
#[Out]#            b   c   d   e
#[Out]# Colorado NaN NaN NaN NaN
#[Out]# Ohio       3 NaN   6 NaN
#[Out]# Oregon   NaN NaN NaN NaN
#[Out]# Texas      9 NaN  12 NaN
#[Out]# Utah     NaN NaN NaN NaN
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Tue, 10 Jun 2014 22:57:46
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
# Tue, 10 Jun 2014 22:58:09
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
# Tue, 10 Jun 2014 22:58:12
df1
#[Out]#    a  b   c   d
#[Out]# 0  0  1   2   3
#[Out]# 1  4  5   6   7
#[Out]# 2  8  9  10  11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 10 Jun 2014 22:58:14
df2
#[Out]#     a   b   c   d   e
#[Out]# 0   0   1   2   3   4
#[Out]# 1   5   6   7   8   9
#[Out]# 2  10  11  12  13  14
#[Out]# 3  15  16  17  18  19
#[Out]# 
#[Out]# [4 rows x 5 columns]
# Tue, 10 Jun 2014 22:59:15
df1 + df2
#[Out]#     a   b   c   d   e
#[Out]# 0   0   2   4   6 NaN
#[Out]# 1   9  11  13  15 NaN
#[Out]# 2  18  20  22  24 NaN
#[Out]# 3 NaN NaN NaN NaN NaN
#[Out]# 
#[Out]# [4 rows x 5 columns]
# Tue, 10 Jun 2014 23:00:00
df1.add(df2, fill_value=0)
#[Out]#     a   b   c   d   e
#[Out]# 0   0   2   4   6   4
#[Out]# 1   9  11  13  15   9
#[Out]# 2  18  20  22  24  14
#[Out]# 3  15  16  17  18  19
#[Out]# 
#[Out]# [4 rows x 5 columns]
# Tue, 10 Jun 2014 23:00:44
df1.reindex(columns=df2.columns, fill_value=0)
#[Out]#    a  b   c   d  e
#[Out]# 0  0  1   2   3  0
#[Out]# 1  4  5   6   7  0
#[Out]# 2  8  9  10  11  0
#[Out]# 
#[Out]# [3 rows x 5 columns]
# Tue, 10 Jun 2014 23:02:48
arr = np.arange(12.).reshape((3, 4))
# Tue, 10 Jun 2014 23:02:49
arr
#[Out]# array([[  0.,   1.,   2.,   3.],
#[Out]#        [  4.,   5.,   6.,   7.],
#[Out]#        [  8.,   9.,  10.,  11.]])
# Tue, 10 Jun 2014 23:03:10
arr[0]
#[Out]# array([ 0.,  1.,  2.,  3.])
# Tue, 10 Jun 2014 23:03:19
arr - arr[0]
#[Out]# array([[ 0.,  0.,  0.,  0.],
#[Out]#        [ 4.,  4.,  4.,  4.],
#[Out]#        [ 8.,  8.,  8.,  8.]])
# Tue, 10 Jun 2014 23:04:42
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# Tue, 10 Jun 2014 23:04:56
series = frame.ix[0]
# Tue, 10 Jun 2014 23:04:58
frame
#[Out]#         b   d   e
#[Out]# Utah    0   1   2
#[Out]# Ohio    3   4   5
#[Out]# Texas   6   7   8
#[Out]# Oregon  9  10  11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:05:03
series
#[Out]# b    0
#[Out]# d    1
#[Out]# e    2
#[Out]# Name: Utah, dtype: float64
# Tue, 10 Jun 2014 23:06:48
frame - series
#[Out]#         b  d  e
#[Out]# Utah    0  0  0
#[Out]# Ohio    3  3  3
#[Out]# Texas   6  6  6
#[Out]# Oregon  9  9  9
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:07:33
series2 = Series(range(3), index=['b', 'e', 'f'])
# Tue, 10 Jun 2014 23:07:40
frame + series2
#[Out]#         b   d   e   f
#[Out]# Utah    0 NaN   3 NaN
#[Out]# Ohio    3 NaN   6 NaN
#[Out]# Texas   6 NaN   9 NaN
#[Out]# Oregon  9 NaN  12 NaN
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Tue, 10 Jun 2014 23:07:46
frame - series2
#[Out]#         b   d   e   f
#[Out]# Utah    0 NaN   1 NaN
#[Out]# Ohio    3 NaN   4 NaN
#[Out]# Texas   6 NaN   7 NaN
#[Out]# Oregon  9 NaN  10 NaN
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Tue, 10 Jun 2014 23:07:58
series2
#[Out]# b    0
#[Out]# e    1
#[Out]# f    2
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:10:34
series3 = frame['d']
# Tue, 10 Jun 2014 23:10:37
series3
#[Out]# Utah       1
#[Out]# Ohio       4
#[Out]# Texas      7
#[Out]# Oregon    10
#[Out]# Name: d, dtype: float64
# Tue, 10 Jun 2014 23:10:49
frame
#[Out]#         b   d   e
#[Out]# Utah    0   1   2
#[Out]# Ohio    3   4   5
#[Out]# Texas   6   7   8
#[Out]# Oregon  9  10  11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:11:20
frame.sub(series3, axis=0)
#[Out]#         b  d  e
#[Out]# Utah   -1  0  1
#[Out]# Ohio   -1  0  1
#[Out]# Texas  -1  0  1
#[Out]# Oregon -1  0  1
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:14:42
frame = DataFrame(np.random.randn(4,3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# Tue, 10 Jun 2014 23:14:44
frame
#[Out]#                b         d         e
#[Out]# Utah    0.651990 -1.037057 -0.366171
#[Out]# Ohio   -0.166304  0.075301 -0.114286
#[Out]# Texas   0.093506 -0.933641  0.814027
#[Out]# Oregon -0.818855  1.258186  0.889279
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:14:58
np.abs(frame)
#[Out]#                b         d         e
#[Out]# Utah    0.651990  1.037057  0.366171
#[Out]# Ohio    0.166304  0.075301  0.114286
#[Out]# Texas   0.093506  0.933641  0.814027
#[Out]# Oregon  0.818855  1.258186  0.889279
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:15:35
f = lambda x: x.max() - x.min()
# Tue, 10 Jun 2014 23:15:44
frame.apply(f)
#[Out]# b    1.470845
#[Out]# d    2.295243
#[Out]# e    1.255451
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:18:26
frame.apply(f, axis=1)
#[Out]# Utah      1.689047
#[Out]# Ohio      0.241606
#[Out]# Texas     1.747668
#[Out]# Oregon    2.077041
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:19:58
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])

# Tue, 10 Jun 2014 23:20:05
frame.apply(f)
#[Out]#             b         d         e
#[Out]# min -0.818855 -1.037057 -0.366171
#[Out]# max  0.651990  1.258186  0.889279
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 10 Jun 2014 23:22:25
def f(x):
    return Series([x.min(), x.max(), x.max() - x.min()], index=['min', 'max', 'dist'])

# Tue, 10 Jun 2014 23:22:29
frame.apply(f)
#[Out]#              b         d         e
#[Out]# min  -0.818855 -1.037057 -0.366171
#[Out]# max   0.651990  1.258186  0.889279
#[Out]# dist  1.470845  2.295243  1.255451
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Tue, 10 Jun 2014 23:23:28
def f(x):
    return Series([x.min(), x.max(), (x.max() - x.min())], index=['min', 'max', 'dist'])

# Tue, 10 Jun 2014 23:23:32
frame.apply(f)
#[Out]#              b         d         e
#[Out]# min  -0.818855 -1.037057 -0.366171
#[Out]# max   0.651990  1.258186  0.889279
#[Out]# dist  1.470845  2.295243  1.255451
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Tue, 10 Jun 2014 23:24:45
format = lambda x: '%.2f' % x
# Tue, 10 Jun 2014 23:24:53
frame.applymap(format)
#[Out]#             b      d      e
#[Out]# Utah     0.65  -1.04  -0.37
#[Out]# Ohio    -0.17   0.08  -0.11
#[Out]# Texas    0.09  -0.93   0.81
#[Out]# Oregon  -0.82   1.26   0.89
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:25:13
frame['e'].map(format)
#[Out]# Utah      -0.37
#[Out]# Ohio      -0.11
#[Out]# Texas      0.81
#[Out]# Oregon     0.89
#[Out]# Name: e, dtype: object
# Tue, 10 Jun 2014 23:26:05
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
# Tue, 10 Jun 2014 23:26:13
obj.sort_index()
#[Out]# a    1
#[Out]# b    2
#[Out]# c    3
#[Out]# d    0
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:26:22
obj
#[Out]# d    0
#[Out]# a    1
#[Out]# b    2
#[Out]# c    3
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:27:37
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
# Tue, 10 Jun 2014 23:27:52
frame.sort_index()
#[Out]#        d  a  b  c
#[Out]# one    4  5  6  7
#[Out]# three  0  1  2  3
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Tue, 10 Jun 2014 23:28:08
frame.sort_index(axis=1)
#[Out]#        a  b  c  d
#[Out]# three  1  2  3  0
#[Out]# one    5  6  7  4
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Tue, 10 Jun 2014 23:28:32
frame.sort_index(axis=(0, 1))
# Tue, 10 Jun 2014 23:28:53
frame.sort_index(axis=[0, 1])
# Tue, 10 Jun 2014 23:29:53
frame.sort_index(axis=1, ascending=False)
#[Out]#        d  c  b  a
#[Out]# three  0  3  2  1
#[Out]# one    4  7  6  5
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Tue, 10 Jun 2014 23:30:06
frame
#[Out]#        d  a  b  c
#[Out]# three  0  1  2  3
#[Out]# one    4  5  6  7
#[Out]# 
#[Out]# [2 rows x 4 columns]
# Tue, 10 Jun 2014 23:32:00
obj = Series([4, 7, -3, 2])
# Tue, 10 Jun 2014 23:32:04
obj.order()
#[Out]# 2   -3
#[Out]# 3    2
#[Out]# 0    4
#[Out]# 1    7
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:32:53
obj = Series([4, np.nan, 7, np.nan, -3, 2])
# Tue, 10 Jun 2014 23:32:57
obj.order()
#[Out]# 4    -3
#[Out]# 5     2
#[Out]# 0     4
#[Out]# 2     7
#[Out]# 1   NaN
#[Out]# 3   NaN
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:34:14
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# Tue, 10 Jun 2014 23:34:17
frame
#[Out]#    a  b
#[Out]# 0  0  4
#[Out]# 1  1  7
#[Out]# 2  0 -3
#[Out]# 3  1  2
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 10 Jun 2014 23:34:44
frame.sort_index(by='b')
#[Out]#    a  b
#[Out]# 2  0 -3
#[Out]# 3  1  2
#[Out]# 0  0  4
#[Out]# 1  1  7
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 10 Jun 2014 23:35:12
frame.sort_index(by=['a', 'b'])
#[Out]#    a  b
#[Out]# 2  0 -3
#[Out]# 0  0  4
#[Out]# 3  1  2
#[Out]# 1  1  7
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 10 Jun 2014 23:39:35
obj = Series([7, -5, 7, 4, 2, 0, 4])
# Tue, 10 Jun 2014 23:39:40
obj.rank()
#[Out]# 0    6.5
#[Out]# 1    1.0
#[Out]# 2    6.5
#[Out]# 3    4.5
#[Out]# 4    3.0
#[Out]# 5    2.0
#[Out]# 6    4.5
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:40:02
obj.rank(method='first')
#[Out]# 0    6
#[Out]# 1    1
#[Out]# 2    7
#[Out]# 3    4
#[Out]# 4    3
#[Out]# 5    2
#[Out]# 6    5
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:40:49
obj.rank(ascending=False, method='max')
#[Out]# 0    2
#[Out]# 1    7
#[Out]# 2    2
#[Out]# 3    4
#[Out]# 4    5
#[Out]# 5    6
#[Out]# 6    4
#[Out]# dtype: float64
# Tue, 10 Jun 2014 23:43:08
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
# Tue, 10 Jun 2014 23:43:12
frame
#[Out]#    a    b    c
#[Out]# 0  0  4.3 -2.0
#[Out]# 1  1  7.0  5.0
#[Out]# 2  0 -3.0  8.0
#[Out]# 3  1  2.0 -2.5
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:44:31
frame.rank(axis=1)
#[Out]#    a  b  c
#[Out]# 0  2  3  1
#[Out]# 1  1  3  2
#[Out]# 2  2  1  3
#[Out]# 3  2  3  1
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:46:52
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
# Tue, 10 Jun 2014 23:46:53
obj
#[Out]# a    0
#[Out]# a    1
#[Out]# b    2
#[Out]# b    3
#[Out]# c    4
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:47:09
obj.index.is_unique
#[Out]# False
# Tue, 10 Jun 2014 23:47:29
obj['a']
#[Out]# a    0
#[Out]# a    1
#[Out]# dtype: int64
# Tue, 10 Jun 2014 23:47:43
obj['c']
#[Out]# 4
# Tue, 10 Jun 2014 23:48:50
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
# Tue, 10 Jun 2014 23:48:52
df
#[Out]#           0         1         2
#[Out]# a  1.392000 -1.510141 -0.526561
#[Out]# a -0.783230  0.186644  0.089751
#[Out]# b  1.473290 -1.015818 -0.310812
#[Out]# b -0.484412  1.290805 -0.789624
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 10 Jun 2014 23:49:06
df.ix['b']
#[Out]#           0         1         2
#[Out]# b  1.473290 -1.015818 -0.310812
#[Out]# b -0.484412  1.290805 -0.789624
#[Out]# 
#[Out]# [2 rows x 3 columns]
%logstart?
$logstart -o -r -t pandas_ch05_log.py append
%logstart -o -r -t pandas_ch05_log.py append
2+2
#[Out]# 4
%pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
!cd "C:\Users\millerdr\Google Drive\Python for Data Analysis\pydata-book\ch05"
%pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
!cd ..
%pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
!cd "C:\\Users\\millerdr\\Google Drive\\Python for Data Analysis\\pydata-book\\ch05"
%pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
%cd ..
%cd "C:\Users\millerdr\Google Drive\Python for Data Analysis\pydata-book\ch05"
!ls
%ls
!dir
%logstart -o -r -t pandas_ch05_log.py append
%logstop
# Mon, 16 Jun 2014 20:38:42
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
# Mon, 16 Jun 2014 20:38:55
import pandas as pd
# Mon, 16 Jun 2014 20:39:28
from pandas import Series, DataFrame
# Mon, 16 Jun 2014 20:39:32
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
# Mon, 16 Jun 2014 20:39:39
import numpy as np
# Mon, 16 Jun 2014 20:39:41
df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
# Mon, 16 Jun 2014 20:39:43
df
#[Out]#     one  two
#[Out]# a  1.40  NaN
#[Out]# b  7.10 -4.5
#[Out]# c   NaN  NaN
#[Out]# d  0.75 -1.3
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Mon, 16 Jun 2014 20:40:11
df.sum()
#[Out]# one    9.25
#[Out]# two   -5.80
#[Out]# dtype: float64
# Mon, 16 Jun 2014 20:40:21
df.sum(axis=1)
#[Out]# a    1.40
#[Out]# b    2.60
#[Out]# c     NaN
#[Out]# d   -0.55
#[Out]# dtype: float64
# Mon, 16 Jun 2014 20:40:56
df.sum(axis=1, skipna=False)
#[Out]# a     NaN
#[Out]# b    2.60
#[Out]# c     NaN
#[Out]# d   -0.55
#[Out]# dtype: float64
# Mon, 16 Jun 2014 20:41:43
df.mean(axis=1, skipna=False)
#[Out]# a      NaN
#[Out]# b    1.300
#[Out]# c      NaN
#[Out]# d   -0.275
#[Out]# dtype: float64
# Mon, 16 Jun 2014 20:42:30
df.idxmax()
#[Out]# one    b
#[Out]# two    d
#[Out]# dtype: object
# Mon, 16 Jun 2014 20:42:47
df.cumsum()
#[Out]#     one  two
#[Out]# a  1.40  NaN
#[Out]# b  8.50 -4.5
#[Out]# c   NaN  NaN
#[Out]# d  9.25 -5.8
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Mon, 16 Jun 2014 20:43:26
df['one'].cumsum()
#[Out]# a    1.40
#[Out]# b    8.50
#[Out]# c     NaN
#[Out]# d    9.25
#[Out]# Name: one, dtype: float64
# Mon, 16 Jun 2014 20:43:38
df['two'].cumsum()
#[Out]# a    NaN
#[Out]# b   -4.5
#[Out]# c    NaN
#[Out]# d   -5.8
#[Out]# Name: two, dtype: float64
# Mon, 16 Jun 2014 20:43:52
df['a'].cumsum()
# Mon, 16 Jun 2014 20:43:59
df[['a']].cumsum()
# Mon, 16 Jun 2014 20:44:16
df[,1].cumsum()
# Mon, 16 Jun 2014 20:44:40
df.cumsum(axis=1)
#[Out]#     one   two
#[Out]# a  1.40   NaN
#[Out]# b  7.10  2.60
#[Out]# c   NaN   NaN
#[Out]# d  0.75 -0.55
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Mon, 16 Jun 2014 20:45:57
df.describe()
#[Out]#             one       two
#[Out]# count  3.000000  2.000000
#[Out]# mean   3.083333 -2.900000
#[Out]# std    3.493685  2.262742
#[Out]# min    0.750000 -4.500000
#[Out]# 25%    1.075000 -3.700000
#[Out]# 50%    1.400000 -2.900000
#[Out]# 75%    4.250000 -2.100000
#[Out]# max    7.100000 -1.300000
#[Out]# 
#[Out]# [8 rows x 2 columns]
# Mon, 16 Jun 2014 20:48:07
obj = Series(['a', 'a', 'b', 'c'] * 4)
# Mon, 16 Jun 2014 20:48:10
obj
#[Out]# 0     a
#[Out]# 1     a
#[Out]# 2     b
#[Out]# 3     c
#[Out]# 4     a
#[Out]# 5     a
#[Out]# 6     b
#[Out]# 7     c
#[Out]# 8     a
#[Out]# 9     a
#[Out]# 10    b
#[Out]# 11    c
#[Out]# 12    a
#[Out]# 13    a
#[Out]# 14    b
#[Out]# 15    c
#[Out]# dtype: object
# Mon, 16 Jun 2014 20:48:15
obj.describe()
#[Out]# count     16
#[Out]# unique     3
#[Out]# top        a
#[Out]# freq       8
#[Out]# dtype: object
# Mon, 16 Jun 2014 20:50:26
import pandas.io.data as web
# Mon, 16 Jun 2014 20:50:33
all_data = {}
# Mon, 16 Jun 2014 20:52:48
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker[ = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    
    
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    
    
)
    
    
    ]
# Mon, 16 Jun 2014 20:54:18
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    
# Mon, 16 Jun 2014 20:56:09
for ticker in ['AAPL', 'IBM', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
    
# Mon, 16 Jun 2014 20:56:59
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
# Mon, 16 Jun 2014 20:57:31
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.iteritems()})
# Mon, 16 Jun 2014 20:57:43
returns = price.pct_change()
# Mon, 16 Jun 2014 20:57:47
returns.tail
#[Out]# <bound method DataFrame.tail of                 AAPL       IBM      MSFT
#[Out]# Date                                    
#[Out]# 2000-01-03       NaN       NaN       NaN
#[Out]# 2000-01-04 -0.083770 -0.033944 -0.033814
#[Out]# 2000-01-05  0.014286  0.035137  0.010524
#[Out]# 2000-01-06 -0.087324 -0.017284 -0.033422
#[Out]# 2000-01-07  0.049383 -0.004344  0.013029
#[Out]# 2000-01-10 -0.017647  0.039587  0.007420
#[Out]# 2000-01-11 -0.050898  0.008496 -0.025780
#[Out]# 2000-01-12 -0.059937  0.004263 -0.032510
#[Out]# 2000-01-13  0.107383 -0.010511  0.019015
#[Out]# 2000-01-14  0.039394  0.011645  0.041155
#[Out]# 2000-01-18  0.034985 -0.032411  0.027253
#[Out]# 2000-01-19  0.025352  0.032453 -0.072180
#[Out]# 2000-01-20  0.063187 -0.004245 -0.009274
#[Out]# 2000-01-21 -0.018088  0.021011 -0.021321
#[Out]# 2000-01-24 -0.044737  0.000000 -0.023911
#[Out]# 2000-01-25  0.055096 -0.019485  0.015242
#[Out]# 2000-01-26 -0.018277 -0.019974 -0.033244
#[Out]# 2000-01-27 -0.002660 -0.027830 -0.006378
#[Out]# 2000-01-28 -0.074667 -0.017133 -0.005024
#[Out]# 2000-01-31  0.020173  0.006172 -0.003927
#[Out]# 2000-02-01 -0.033898 -0.020015  0.051816
#[Out]# 2000-02-02 -0.014620  0.031844 -0.020616
#[Out]# 2000-02-03  0.047478  0.031925  0.027884
#[Out]# 2000-02-04  0.045326 -0.012787  0.028191
#[Out]# 2000-02-07  0.054201 -0.012953  0.000776
#[Out]# 2000-02-08  0.007712  0.042121  0.031016
#[Out]# 2000-02-09 -0.020408 -0.012085 -0.054149
#[Out]# 2000-02-10  0.007812  0.014905  0.019348
#[Out]# 2000-02-11 -0.041344 -0.031500 -0.057202
#[Out]# 2000-02-14  0.064690  0.005961 -0.003034
#[Out]# 2000-02-15  0.027848  0.009149 -0.010788
#[Out]# 2000-02-16 -0.039409 -0.011744 -0.009508
#[Out]# 2000-02-17  0.005128  0.008652  0.020610
#[Out]# 2000-02-18 -0.030612 -0.036379 -0.045920
#[Out]# 2000-02-22  0.023684 -0.013299 -0.013047
#[Out]# 2000-02-23  0.020566 -0.020326  0.004700
#[Out]# 2000-02-24 -0.010076  0.016088  0.005263
#[Out]# 2000-02-25 -0.040712 -0.022603 -0.036358
#[Out]# 2000-02-28  0.026525 -0.032399  0.002717
#[Out]# 2000-02-29  0.010336 -0.016742 -0.023781
#[Out]# 2000-03-01  0.138107 -0.024307  0.016035
#[Out]# 2000-03-02 -0.065169  0.028644  0.028225
#[Out]# 2000-03-03  0.050481  0.047268  0.029516
#[Out]# 2000-03-06 -0.018307 -0.045693 -0.057339
#[Out]# 2000-03-07 -0.023310 -0.000702  0.024939
#[Out]# 2000-03-08 -0.007160  0.031631  0.028783
#[Out]# 2000-03-09  0.002404  0.016466  0.046438
#[Out]# 2000-03-10  0.028777 -0.025472  0.010198
#[Out]# 2000-03-13 -0.034965  0.023157 -0.029741
#[Out]# 2000-03-14 -0.057971  0.008739 -0.029528
#[Out]# 2000-03-15  0.017949 -0.014995  0.002608
#[Out]# 2000-03-16  0.045340  0.018719  0.000000
#[Out]# 2000-03-17  0.028916  0.009188  0.042197
#[Out]# 2000-03-20 -0.016393  0.025008 -0.020244
#[Out]# 2000-03-21  0.097619  0.006635  0.055194
#[Out]# 2000-03-22  0.067245  0.006591  0.004828
#[Out]# 2000-03-23 -0.020325  0.008765  0.083556
#[Out]# 2000-03-24 -0.018672  0.046587 -0.001725
#[Out]# 2000-03-27  0.006342  0.051816 -0.068115
#[Out]# 2000-03-28 -0.002101 -0.034427  0.002383
#[Out]#                  ...       ...       ...
#[Out]# 
#[Out]# [2515 rows x 3 columns]>
# Mon, 16 Jun 2014 20:57:53
returns.tail()
#[Out]#                 AAPL       IBM      MSFT
#[Out]# Date                                    
#[Out]# 2009-12-24  0.034058  0.004346  0.002550
#[Out]# 2009-12-28  0.012263  0.013313  0.005451
#[Out]# 2009-12-29 -0.011769 -0.003449  0.007228
#[Out]# 2009-12-30  0.012259  0.005438 -0.013635
#[Out]# 2009-12-31 -0.004498 -0.012621 -0.015642
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Mon, 16 Jun 2014 20:59:53
returns.MSFT.corr(returns.IBM)
#[Out]# 0.49570106584058271
# Mon, 16 Jun 2014 21:00:06
returns.MSFT.cov(returns.IBM)
#[Out]# 0.00021581832606089538
# Mon, 16 Jun 2014 21:00:21
returns.corr()
#[Out]#           AAPL       IBM      MSFT
#[Out]# AAPL  1.000000  0.408069  0.424698
#[Out]# IBM   0.408069  1.000000  0.495701
#[Out]# MSFT  0.424698  0.495701  1.000000
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Mon, 16 Jun 2014 21:00:33
returns.cov()
#[Out]#           AAPL       IBM      MSFT
#[Out]# AAPL  0.001028  0.000251  0.000309
#[Out]# IBM   0.000251  0.000367  0.000216
#[Out]# MSFT  0.000309  0.000216  0.000516
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Mon, 16 Jun 2014 21:01:24
returns.corrwith(returns.IBM)
#[Out]# AAPL    0.408069
#[Out]# IBM     1.000000
#[Out]# MSFT    0.495701
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:02:06
returns.corrwith(volume)
#[Out]# AAPL   -0.057820
#[Out]# IBM    -0.007898
#[Out]# MSFT   -0.014438
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:03:08
price.head()
#[Out]#             AAPL    IBM   MSFT
#[Out]# Date                          
#[Out]# 2000-01-03  3.82  96.04  42.29
#[Out]# 2000-01-04  3.50  92.78  40.86
#[Out]# 2000-01-05  3.55  96.04  41.29
#[Out]# 2000-01-06  3.24  94.38  39.91
#[Out]# 2000-01-07  3.40  93.97  40.43
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Mon, 16 Jun 2014 21:03:47
returns.head()
#[Out]#                 AAPL       IBM      MSFT
#[Out]# Date                                    
#[Out]# 2000-01-03       NaN       NaN       NaN
#[Out]# 2000-01-04 -0.083770 -0.033944 -0.033814
#[Out]# 2000-01-05  0.014286  0.035137  0.010524
#[Out]# 2000-01-06 -0.087324 -0.017284 -0.033422
#[Out]# 2000-01-07  0.049383 -0.004344  0.013029
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Mon, 16 Jun 2014 21:04:23
returns.corrwith(volume, axis=1)
#[Out]# Date
#[Out]# 2000-01-03         NaN
#[Out]# 2000-01-04   -0.924375
#[Out]# 2000-01-05   -0.611945
#[Out]# 2000-01-06   -0.999648
#[Out]# 2000-01-07    0.983053
#[Out]# 2000-01-10   -0.958775
#[Out]# 2000-01-11   -0.974255
#[Out]# 2000-01-12   -0.934844
#[Out]# 2000-01-13    0.998623
#[Out]# 2000-01-14    0.946995
#[Out]# 2000-01-18    0.979351
#[Out]# 2000-01-19   -0.210147
#[Out]# 2000-01-20    0.990020
#[Out]# 2000-01-21   -0.843254
#[Out]# 2000-01-24   -0.999830
#[Out]# ...
#[Out]# 2009-12-10   -0.980030
#[Out]# 2009-12-11   -0.996279
#[Out]# 2009-12-14    0.889532
#[Out]# 2009-12-15   -0.370291
#[Out]# 2009-12-16    0.951659
#[Out]# 2009-12-17   -0.784929
#[Out]# 2009-12-18    0.745363
#[Out]# 2009-12-21    0.968502
#[Out]# 2009-12-22    0.756169
#[Out]# 2009-12-23    0.999226
#[Out]# 2009-12-24    0.994909
#[Out]# 2009-12-28    0.280504
#[Out]# 2009-12-29   -0.678332
#[Out]# 2009-12-30    0.379578
#[Out]# 2009-12-31    0.827971
#[Out]# Length: 2515
# Mon, 16 Jun 2014 21:05:36
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# Mon, 16 Jun 2014 21:05:53
uniques = obj.unique()
# Mon, 16 Jun 2014 21:06:00
uniques
#[Out]# array(['c', 'a', 'd', 'b'], dtype=object)
# Mon, 16 Jun 2014 21:06:44
uniques.sort()
# Mon, 16 Jun 2014 21:06:57
uniques
#[Out]# array(['a', 'b', 'c', 'd'], dtype=object)
# Mon, 16 Jun 2014 21:07:19
obj.value_counts()
#[Out]# c    3
#[Out]# a    3
#[Out]# b    2
#[Out]# d    1
#[Out]# dtype: int64
# Mon, 16 Jun 2014 21:07:50
pd.value_counts(obj.values, sort=False)
#[Out]# a    3
#[Out]# c    3
#[Out]# b    2
#[Out]# d    1
#[Out]# dtype: int64
# Mon, 16 Jun 2014 21:08:20
mask = obj.isin(['b', 'c'])
# Mon, 16 Jun 2014 21:08:27
mask
#[Out]# 0     True
#[Out]# 1    False
#[Out]# 2    False
#[Out]# 3    False
#[Out]# 4    False
#[Out]# 5     True
#[Out]# 6     True
#[Out]# 7     True
#[Out]# 8     True
#[Out]# dtype: bool
# Mon, 16 Jun 2014 21:08:36
obj[mask]
#[Out]# 0    c
#[Out]# 5    b
#[Out]# 6    b
#[Out]# 7    c
#[Out]# 8    c
#[Out]# dtype: object
# Mon, 16 Jun 2014 21:11:18
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
'Qu2': [2, 3, 1, 2, 3],
'Qu3': [1, 5, 2, 4, 4]})
# Mon, 16 Jun 2014 21:11:20
data
#[Out]#    Qu1  Qu2  Qu3
#[Out]# 0    1    2    1
#[Out]# 1    3    3    5
#[Out]# 2    4    1    2
#[Out]# 3    3    2    4
#[Out]# 4    4    3    4
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Mon, 16 Jun 2014 21:12:43
result = data.apply(pd.value_counts).fillna(0)
# Mon, 16 Jun 2014 21:12:45
result
#[Out]#    Qu1  Qu2  Qu3
#[Out]# 1    1    1    1
#[Out]# 2    0    2    1
#[Out]# 3    2    2    0
#[Out]# 4    2    0    2
#[Out]# 5    0    0    1
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Mon, 16 Jun 2014 21:14:33
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
# Mon, 16 Jun 2014 21:14:39
string_data
#[Out]# 0     aardvark
#[Out]# 1    artichoke
#[Out]# 2          NaN
#[Out]# 3      avocado
#[Out]# dtype: object
# Mon, 16 Jun 2014 21:14:47
string_data.isnull()
#[Out]# 0    False
#[Out]# 1    False
#[Out]# 2     True
#[Out]# 3    False
#[Out]# dtype: bool
# Mon, 16 Jun 2014 21:15:07
string_data[0] = None
# Mon, 16 Jun 2014 21:15:12
string_data
#[Out]# 0         None
#[Out]# 1    artichoke
#[Out]# 2          NaN
#[Out]# 3      avocado
#[Out]# dtype: object
# Mon, 16 Jun 2014 21:15:18
string_data.isnull()
#[Out]# 0     True
#[Out]# 1    False
#[Out]# 2     True
#[Out]# 3    False
#[Out]# dtype: bool
# Mon, 16 Jun 2014 21:16:28
from numpy import nan as NA
# Mon, 16 Jun 2014 21:16:45
data = Series([1, NA, 3.5, NA, 7])
# Mon, 16 Jun 2014 21:16:49
data.dropna()
#[Out]# 0    1.0
#[Out]# 2    3.5
#[Out]# 4    7.0
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:17:06
data
#[Out]# 0    1.0
#[Out]# 1    NaN
#[Out]# 2    3.5
#[Out]# 3    NaN
#[Out]# 4    7.0
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:17:20
data[data.notnull()]
#[Out]# 0    1.0
#[Out]# 2    3.5
#[Out]# 4    7.0
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:18:46
data = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
# Mon, 16 Jun 2014 21:18:56
cleaned = data.dropna()
# Mon, 16 Jun 2014 21:18:58
data
#[Out]#     0    1   2
#[Out]# 0   1  6.5   3
#[Out]# 1   1  NaN NaN
#[Out]# 2 NaN  NaN NaN
#[Out]# 3 NaN  6.5   3
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:19:32
cleaned
#[Out]#    0    1  2
#[Out]# 0  1  6.5  3
#[Out]# 
#[Out]# [1 rows x 3 columns]
# Mon, 16 Jun 2014 21:20:04
data.dropna(how='all')
#[Out]#     0    1   2
#[Out]# 0   1  6.5   3
#[Out]# 1   1  NaN NaN
#[Out]# 3 NaN  6.5   3
#[Out]# 
#[Out]# [3 rows x 3 columns]
# Mon, 16 Jun 2014 21:20:25
data[4] = NA
# Mon, 16 Jun 2014 21:20:28
data
#[Out]#     0    1   2   4
#[Out]# 0   1  6.5   3 NaN
#[Out]# 1   1  NaN NaN NaN
#[Out]# 2 NaN  NaN NaN NaN
#[Out]# 3 NaN  6.5   3 NaN
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Mon, 16 Jun 2014 21:20:42
data.dropna(axis=1, how='all')
#[Out]#     0    1   2
#[Out]# 0   1  6.5   3
#[Out]# 1   1  NaN NaN
#[Out]# 2 NaN  NaN NaN
#[Out]# 3 NaN  6.5   3
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:21:51
df = DataFrame(np.random.randn(7, 3))
# Mon, 16 Jun 2014 21:22:20
df.ix[:4, 1] = NA; df.ix[:2, 2] = NA
# Mon, 16 Jun 2014 21:22:23
df
#[Out]#           0         1         2
#[Out]# 0 -1.570018       NaN       NaN
#[Out]# 1  0.454172       NaN       NaN
#[Out]# 2 -0.206144       NaN       NaN
#[Out]# 3 -0.057423       NaN -0.560099
#[Out]# 4  1.093472       NaN -1.293087
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Mon, 16 Jun 2014 21:23:18
df.dropna(thresh=3)
#[Out]#           0         1         2
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Mon, 16 Jun 2014 21:23:49
df.fillna(0)
#[Out]#           0         1         2
#[Out]# 0 -1.570018  0.000000  0.000000
#[Out]# 1  0.454172  0.000000  0.000000
#[Out]# 2 -0.206144  0.000000  0.000000
#[Out]# 3 -0.057423  0.000000 -0.560099
#[Out]# 4  1.093472  0.000000 -1.293087
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Mon, 16 Jun 2014 21:24:07
df
#[Out]#           0         1         2
#[Out]# 0 -1.570018       NaN       NaN
#[Out]# 1  0.454172       NaN       NaN
#[Out]# 2 -0.206144       NaN       NaN
#[Out]# 3 -0.057423       NaN -0.560099
#[Out]# 4  1.093472       NaN -1.293087
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Mon, 16 Jun 2014 21:24:27
df.fillna({1: 0.5, 3: -1})
#[Out]#           0         1         2
#[Out]# 0 -1.570018  0.500000       NaN
#[Out]# 1  0.454172  0.500000       NaN
#[Out]# 2 -0.206144  0.500000       NaN
#[Out]# 3 -0.057423  0.500000 -0.560099
#[Out]# 4  1.093472  0.500000 -1.293087
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Mon, 16 Jun 2014 21:25:40
_ = df.fillna(0, inplace=True)
# Mon, 16 Jun 2014 21:25:41
df
#[Out]#           0         1         2
#[Out]# 0 -1.570018  0.000000  0.000000
#[Out]# 1  0.454172  0.000000  0.000000
#[Out]# 2 -0.206144  0.000000  0.000000
#[Out]# 3 -0.057423  0.000000 -0.560099
#[Out]# 4  1.093472  0.000000 -1.293087
#[Out]# 5 -0.000902 -0.445444  1.185352
#[Out]# 6  2.787491  0.273286 -0.495796
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Mon, 16 Jun 2014 21:26:19
df = DataFrame(np.random.randn(6, 3))
# Mon, 16 Jun 2014 21:26:41
df.ix[2:, 1] = NA; df.ix]4:, 2] = NA
# Mon, 16 Jun 2014 21:26:56
df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
# Mon, 16 Jun 2014 21:26:57
df
#[Out]#           0         1         2
#[Out]# 0  1.236348 -0.735893 -0.785867
#[Out]# 1 -1.020840  0.378434 -0.308851
#[Out]# 2  1.298939       NaN -1.961002
#[Out]# 3 -2.061950       NaN  0.295522
#[Out]# 4 -0.410084       NaN       NaN
#[Out]# 5 -0.508523       NaN       NaN
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Mon, 16 Jun 2014 21:27:17
df.fillna(method='ffill')
#[Out]#           0         1         2
#[Out]# 0  1.236348 -0.735893 -0.785867
#[Out]# 1 -1.020840  0.378434 -0.308851
#[Out]# 2  1.298939  0.378434 -1.961002
#[Out]# 3 -2.061950  0.378434  0.295522
#[Out]# 4 -0.410084  0.378434  0.295522
#[Out]# 5 -0.508523  0.378434  0.295522
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Mon, 16 Jun 2014 21:27:35
df.fillna(method='ffill', limit=2)
#[Out]#           0         1         2
#[Out]# 0  1.236348 -0.735893 -0.785867
#[Out]# 1 -1.020840  0.378434 -0.308851
#[Out]# 2  1.298939  0.378434 -1.961002
#[Out]# 3 -2.061950  0.378434  0.295522
#[Out]# 4 -0.410084       NaN  0.295522
#[Out]# 5 -0.508523       NaN  0.295522
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Mon, 16 Jun 2014 21:28:03
data = Series([1., NA, 3.5, NA, 7])
# Mon, 16 Jun 2014 21:28:16
data.fillna(data.mean())
#[Out]# 0    1.000000
#[Out]# 1    3.833333
#[Out]# 2    3.500000
#[Out]# 3    3.833333
#[Out]# 4    7.000000
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:30:54
data = Series(np.random.randn(10),
index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# Mon, 16 Jun 2014 21:30:59
data
#[Out]# a  1   -0.541203
#[Out]#    2   -2.067744
#[Out]#    3   -0.924626
#[Out]# b  1   -0.806645
#[Out]#    2    0.036941
#[Out]#    3    0.881314
#[Out]# c  1   -1.309656
#[Out]#    2    0.293280
#[Out]# d  2   -1.227799
#[Out]#    3   -0.491253
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:31:17
data.index
#[Out]# MultiIndex(levels=[[u'a', u'b', u'c', u'd'], [1, 2, 3]],
#[Out]#            labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
# Mon, 16 Jun 2014 21:32:42
data['b']
#[Out]# 1   -0.806645
#[Out]# 2    0.036941
#[Out]# 3    0.881314
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:32:59
data['b':'c']
#[Out]# b  1   -0.806645
#[Out]#    2    0.036941
#[Out]#    3    0.881314
#[Out]# c  1   -1.309656
#[Out]#    2    0.293280
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:33:28
data.ix[['b', 'd']]
#[Out]# b  1   -0.806645
#[Out]#    2    0.036941
#[Out]#    3    0.881314
#[Out]# d  2   -1.227799
#[Out]#    3   -0.491253
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:33:40
data[:, 2]
#[Out]# a   -2.067744
#[Out]# b    0.036941
#[Out]# c    0.293280
#[Out]# d   -1.227799
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:34:34
data.unstack()
#[Out]#           1         2         3
#[Out]# a -0.541203 -2.067744 -0.924626
#[Out]# b -0.806645  0.036941  0.881314
#[Out]# c -1.309656  0.293280       NaN
#[Out]# d       NaN -1.227799 -0.491253
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:34:52
data.unstack().stack()
#[Out]# a  1   -0.541203
#[Out]#    2   -2.067744
#[Out]#    3   -0.924626
#[Out]# b  1   -0.806645
#[Out]#    2    0.036941
#[Out]#    3    0.881314
#[Out]# c  1   -1.309656
#[Out]#    2    0.293280
#[Out]# d  2   -1.227799
#[Out]#    3   -0.491253
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:37:05
frame = DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'c', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
# Mon, 16 Jun 2014 21:37:07
frame
#[Out]#       Ohio       Colorado
#[Out]#      Green  Red     Green
#[Out]# a 1      0    1         2
#[Out]#   2      3    4         5
#[Out]# c 1      6    7         8
#[Out]# b 2      9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:37:45
frame = DataFrame(np.arange(12).reshape((4, 3)),
index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
# Mon, 16 Jun 2014 21:37:47
frame
#[Out]#       Ohio       Colorado
#[Out]#      Green  Red     Green
#[Out]# a 1      0    1         2
#[Out]#   2      3    4         5
#[Out]# b 1      6    7         8
#[Out]#   2      9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:38:27
frame.index.names = ['key1', 'key2']
# Mon, 16 Jun 2014 21:38:42
frame.columns.names = ['state', 'color']
# Mon, 16 Jun 2014 21:38:44
frame
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key1 key2                      
#[Out]# a    1         0    1         2
#[Out]#      2         3    4         5
#[Out]# b    1         6    7         8
#[Out]#      2         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:39:32
frame['Ohio']
#[Out]# color      Green  Red
#[Out]# key1 key2            
#[Out]# a    1         0    1
#[Out]#      2         3    4
#[Out]# b    1         6    7
#[Out]#      2         9   10
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Mon, 16 Jun 2014 21:41:05
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])
# Mon, 16 Jun 2014 21:44:20
frame.swaplevel('key1', 'key2')
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key2 key1                      
#[Out]# 1    a         0    1         2
#[Out]# 2    a         3    4         5
#[Out]# 1    b         6    7         8
#[Out]# 2    b         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:45:12
frame.sortlevel(1)
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key1 key2                      
#[Out]# a    1         0    1         2
#[Out]# b    1         6    7         8
#[Out]# a    2         3    4         5
#[Out]# b    2         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:45:17
frame.sortlevel(0)
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key1 key2                      
#[Out]# a    1         0    1         2
#[Out]#      2         3    4         5
#[Out]# b    1         6    7         8
#[Out]#      2         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:45:20
frame.sortlevel(1)
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key1 key2                      
#[Out]# a    1         0    1         2
#[Out]# b    1         6    7         8
#[Out]# a    2         3    4         5
#[Out]# b    2         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:46:18
frame.swaplevel(0, 1).sortlevel(0)
#[Out]# state       Ohio       Colorado
#[Out]# color      Green  Red     Green
#[Out]# key2 key1                      
#[Out]# 1    a         0    1         2
#[Out]#      b         6    7         8
#[Out]# 2    a         3    4         5
#[Out]#      b         9   10        11
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Mon, 16 Jun 2014 21:47:40
frame.sum(level='key2')
#[Out]# state   Ohio       Colorado
#[Out]# color  Green  Red     Green
#[Out]# key2                       
#[Out]# 1          6    8        10
#[Out]# 2         12   14        16
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Mon, 16 Jun 2014 21:49:05
frame.sum(level='color', axis=1)
#[Out]# color      Green  Red
#[Out]# key1 key2            
#[Out]# a    1         2    1
#[Out]#      2         8    4
#[Out]# b    1        14    7
#[Out]#      2        20   10
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Mon, 16 Jun 2014 21:51:19
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
'd': [0, 1, 2, 0, 1, 2, 3]})
# Mon, 16 Jun 2014 21:51:22
frame
#[Out]#    a  b    c  d
#[Out]# 0  0  7  one  0
#[Out]# 1  1  6  one  1
#[Out]# 2  2  5  one  2
#[Out]# 3  3  4  two  0
#[Out]# 4  4  3  two  1
#[Out]# 5  5  2  two  2
#[Out]# 6  6  1  two  3
#[Out]# 
#[Out]# [7 rows x 4 columns]
# Mon, 16 Jun 2014 21:52:21
frame2 = frame.set_index(['c', 'd'])
# Mon, 16 Jun 2014 21:52:23
frame2
#[Out]#        a  b
#[Out]# c   d      
#[Out]# one 0  0  7
#[Out]#     1  1  6
#[Out]#     2  2  5
#[Out]# two 0  3  4
#[Out]#     1  4  3
#[Out]#     2  5  2
#[Out]#     3  6  1
#[Out]# 
#[Out]# [7 rows x 2 columns]
# Mon, 16 Jun 2014 21:52:47
frame2 = frame.set_index(['c', 'd'], drop=False)
# Mon, 16 Jun 2014 21:52:50
frame2
#[Out]#        a  b    c  d
#[Out]# c   d              
#[Out]# one 0  0  7  one  0
#[Out]#     1  1  6  one  1
#[Out]#     2  2  5  one  2
#[Out]# two 0  3  4  two  0
#[Out]#     1  4  3  two  1
#[Out]#     2  5  2  two  2
#[Out]#     3  6  1  two  3
#[Out]# 
#[Out]# [7 rows x 4 columns]
# Mon, 16 Jun 2014 21:53:13
frame2.reset_index()
# Mon, 16 Jun 2014 21:53:29
frame2 = frame.set_index(['c', 'd'])
# Mon, 16 Jun 2014 21:53:31
frame2
#[Out]#        a  b
#[Out]# c   d      
#[Out]# one 0  0  7
#[Out]#     1  1  6
#[Out]#     2  2  5
#[Out]# two 0  3  4
#[Out]#     1  4  3
#[Out]#     2  5  2
#[Out]#     3  6  1
#[Out]# 
#[Out]# [7 rows x 2 columns]
# Mon, 16 Jun 2014 21:53:34
frame2.reset_index()
#[Out]#      c  d  a  b
#[Out]# 0  one  0  0  7
#[Out]# 1  one  1  1  6
#[Out]# 2  one  2  2  5
#[Out]# 3  two  0  3  4
#[Out]# 4  two  1  4  3
#[Out]# 5  two  2  5  2
#[Out]# 6  two  3  6  1
#[Out]# 
#[Out]# [7 rows x 4 columns]
# Mon, 16 Jun 2014 21:55:16
ser = Series(np.arange(3.))
# Mon, 16 Jun 2014 21:55:19
ser[-1]
# Mon, 16 Jun 2014 21:55:32
ser
#[Out]# 0    0
#[Out]# 1    1
#[Out]# 2    2
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:56:02
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
# Mon, 16 Jun 2014 21:56:06
ser2[-1]
#[Out]# 2.0
# Mon, 16 Jun 2014 21:56:16
ser
#[Out]# 0    0
#[Out]# 1    1
#[Out]# 2    2
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:56:18
ser2
#[Out]# a    0
#[Out]# b    1
#[Out]# c    2
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:56:26
ser2['c']
#[Out]# 2.0
# Mon, 16 Jun 2014 21:56:41
ser[:1]
#[Out]# 0    0
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:56:52
ser2[:1]
#[Out]# a    0
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:57:15
ser.ix[:1]
#[Out]# 0    0
#[Out]# 1    1
#[Out]# dtype: float64
# Mon, 16 Jun 2014 21:58:28
ser3 = Series(range(3), index=[-5, 1, 3])
# Mon, 16 Jun 2014 21:58:36
ser3.iget_value(2)
#[Out]# 2
# Mon, 16 Jun 2014 21:59:08
frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
# Mon, 16 Jun 2014 21:59:14
frame.irow(0)
#[Out]# 0    0
#[Out]# 1    1
#[Out]# Name: 2, dtype: int32
# Mon, 16 Jun 2014 22:02:11
pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))
# Mon, 16 Jun 2014 22:02:29
pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
for stk in ['AAPL', 'MSFT', 'DELL']))
# Mon, 16 Jun 2014 22:02:40
pdata
#[Out]# <class 'pandas.core.panel.Panel'>
#[Out]# Dimensions: 3 (items) x 868 (major_axis) x 6 (minor_axis)
#[Out]# Items axis: AAPL to MSFT
#[Out]# Major_axis axis: 2009-01-02 00:00:00 to 2012-06-01 00:00:00
#[Out]# Minor_axis axis: Open to Adj Close
# Mon, 16 Jun 2014 22:03:31
pdata = pdata.swapaxes('items', 'minor')
# Mon, 16 Jun 2014 22:03:40
pdata['Adj Close']
#[Out]#              AAPL   DELL   MSFT
#[Out]# Date                           
#[Out]# 2009-01-02  12.39  10.40  17.63
#[Out]# 2009-01-05  12.91  10.26  17.80
#[Out]# 2009-01-06  12.70  10.69  18.01
#[Out]# 2009-01-07  12.43  10.79  16.92
#[Out]# 2009-01-08  12.66  10.90  17.45
#[Out]# 2009-01-09  12.37  10.76  16.93
#[Out]# 2009-01-12  12.11  10.30  16.89
#[Out]# 2009-01-13  11.98  10.41  17.19
#[Out]# 2009-01-14  11.65   9.97  16.56
#[Out]# 2009-01-15  11.39  10.20  16.69
#[Out]# 2009-01-16  11.24   9.93  17.10
#[Out]# 2009-01-20  10.68   9.53  16.03
#[Out]# 2009-01-21  11.31   9.87  16.81
#[Out]# 2009-01-22  12.07   9.65  14.84
#[Out]# 2009-01-23  12.07   9.81  14.92
#[Out]# 2009-01-26  12.24   9.97  15.29
#[Out]# 2009-01-27  12.39   9.74  15.32
#[Out]# 2009-01-28  12.86  10.52  15.65
#[Out]# 2009-01-29  12.70   9.63  15.26
#[Out]# 2009-01-30  12.31   9.19  14.83
#[Out]# 2009-02-02  12.50   9.01  15.47
#[Out]# 2009-02-03  12.70   9.45  16.05
#[Out]# 2009-02-04  12.77   9.47  16.16
#[Out]# 2009-02-05  13.17   9.12  16.52
#[Out]# 2009-02-06  13.62   9.15  17.05
#[Out]# 2009-02-09  14.00   9.33  16.86
#[Out]# 2009-02-10  13.36   8.86  16.31
#[Out]# 2009-02-11  13.22   8.73  16.66
#[Out]# 2009-02-12  13.55   8.87  16.71
#[Out]# 2009-02-13  13.54   8.82  16.56
#[Out]# 2009-02-17  12.91   8.59  15.80
#[Out]# 2009-02-18  12.89   8.37  15.83
#[Out]# 2009-02-19  12.38   7.85  15.64
#[Out]# 2009-02-20  12.45   8.14  15.72
#[Out]# 2009-02-23  11.87   7.73  15.03
#[Out]# 2009-02-24  12.32   7.99  15.00
#[Out]# 2009-02-25  12.45   8.09  14.81
#[Out]# 2009-02-26  12.18   7.94  14.34
#[Out]# 2009-02-27  12.19   8.25  14.11
#[Out]# 2009-03-02  12.01   8.15  13.79
#[Out]# 2009-03-03  12.07   8.85  13.87
#[Out]# 2009-03-04  12.45   8.59  14.08
#[Out]# 2009-03-05  12.13   8.12  13.34
#[Out]# 2009-03-06  11.65   8.10  13.35
#[Out]# 2009-03-09  11.35   7.78  13.23
#[Out]# 2009-03-10  12.10   8.47  14.39
#[Out]# 2009-03-11  12.66   8.69  14.94
#[Out]# 2009-03-12  13.16   9.13  14.86
#[Out]# 2009-03-13  13.10   9.06  14.54
#[Out]# 2009-03-16  13.03   8.61  14.19
#[Out]# 2009-03-17  13.61   9.04  14.76
#[Out]# 2009-03-18  13.86   9.31  14.81
#[Out]# 2009-03-19  13.88   9.71  14.97
#[Out]# 2009-03-20  13.87   9.56  14.90
#[Out]# 2009-03-23  14.70  10.11  16.01
#[Out]# 2009-03-24  14.54  10.07  15.66
#[Out]# 2009-03-25  14.54   9.84  15.62
#[Out]# 2009-03-26  15.00  10.01  16.45
#[Out]# 2009-03-27  14.59   9.63  15.83
#[Out]# 2009-03-30  14.27   9.18  15.27
#[Out]#               ...    ...    ...
#[Out]# 
#[Out]# [868 rows x 3 columns]
# Mon, 16 Jun 2014 22:04:11
pdata.ix[:, '6/1/2012', :]
#[Out]#         Open    High     Low   Close     Volume  Adj Close
#[Out]# AAPL  569.16  572.65  560.52  560.99  130246900      76.60
#[Out]# DELL   12.15   12.30   12.05   12.07   19397600      11.68
#[Out]# MSFT   28.76   28.96   28.44   28.45   56634300      26.82
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Mon, 16 Jun 2014 22:04:58
pdata.ix['Adj Close', '5/22/2012', :]
#[Out]# AAPL    76.05
#[Out]# DELL    14.59
#[Out]# MSFT    28.05
#[Out]# Name: 2012-05-22 00:00:00, dtype: float64
# Mon, 16 Jun 2014 22:05:09
pdata.ix['Adj Close', '5/22/2012':, :]
#[Out]#              AAPL   DELL   MSFT
#[Out]# Date                           
#[Out]# 2012-05-22  76.05  14.59  28.05
#[Out]# 2012-05-23  77.91  12.08  27.44
#[Out]# 2012-05-24  77.19  12.04  27.40
#[Out]# 2012-05-25  76.78  12.05  27.39
#[Out]# 2012-05-28    NaN  12.05    NaN
#[Out]# 2012-05-29  78.14  12.25  27.86
#[Out]# 2012-05-30  79.08  12.15  27.66
#[Out]# 2012-05-31  78.89  11.93  27.51
#[Out]# 2012-06-01  76.60  11.68  26.82
#[Out]# 
#[Out]# [9 rows x 3 columns]
# Mon, 16 Jun 2014 22:06:25
stacked = pdata.ix[:, '5/30/2012':, :].to_frame()
# Mon, 16 Jun 2014 22:06:28
stacked
#[Out]#                     Open    High     Low   Close     Volume  Adj Close
#[Out]# Date       minor                                                      
#[Out]# 2012-05-30 AAPL   569.20  579.99  566.56  579.17  132357400      79.08
#[Out]#            DELL    12.59   12.70   12.46   12.56   19787800      12.15
#[Out]#            MSFT    29.35   29.48   29.12   29.34   41585500      27.66
#[Out]# 2012-05-31 AAPL   580.74  581.50  571.46  577.73  122918600      78.89
#[Out]#            DELL    12.53   12.54   12.33   12.33   19955600      11.93
#[Out]#            MSFT    29.30   29.42   28.94   29.19   39134000      27.51
#[Out]# 2012-06-01 AAPL   569.16  572.65  560.52  560.99  130246900      76.60
#[Out]#            DELL    12.15   12.30   12.05   12.07   19397600      11.68
#[Out]#            MSFT    28.76   28.96   28.44   28.45   56634300      26.82
#[Out]# 
#[Out]# [9 rows x 6 columns]
# Mon, 16 Jun 2014 22:06:55
stacked.to_panel()
#[Out]# <class 'pandas.core.panel.Panel'>
#[Out]# Dimensions: 6 (items) x 3 (major_axis) x 3 (minor_axis)
#[Out]# Items axis: Open to Adj Close
#[Out]# Major_axis axis: 2012-05-30 00:00:00 to 2012-06-01 00:00:00
#[Out]# Minor_axis axis: AAPL to MSFT
# Mon, 16 Jun 2014 22:07:30
%stoplog
# Mon, 16 Jun 2014 22:08:37
%logstop
