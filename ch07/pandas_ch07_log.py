pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
cd ../..
cd "Google Drive/Python for Data Analysis/pydata-book/ch07"
%logstart?
# Tue, 01 Jul 2014 07:49:00
import pandas as pd
# Tue, 01 Jul 2014 07:49:24
import numpy as np
# Tue, 01 Jul 2014 07:49:32
from pandas import DataFrame, Series
# Tue, 01 Jul 2014 07:50:55
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1': range(7)})
# Tue, 01 Jul 2014 07:51:29
df2 = DataFrame({'key': ['a', 'b', 'd'],
'data2': range(3)})
# Tue, 01 Jul 2014 07:51:31
df1
#[Out]#    data1 key
#[Out]# 0      0   b
#[Out]# 1      1   b
#[Out]# 2      2   a
#[Out]# 3      3   c
#[Out]# 4      4   a
#[Out]# 5      5   a
#[Out]# 6      6   b
#[Out]# 
#[Out]# [7 rows x 2 columns]
# Tue, 01 Jul 2014 07:51:39
df2
#[Out]#    data2 key
#[Out]# 0      0   a
#[Out]# 1      1   b
#[Out]# 2      2   d
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 07:52:46
pd.merge(df1, df2)
#[Out]#    data1 key  data2
#[Out]# 0      0   b      1
#[Out]# 1      1   b      1
#[Out]# 2      6   b      1
#[Out]# 3      2   a      0
#[Out]# 4      4   a      0
#[Out]# 5      5   a      0
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Tue, 01 Jul 2014 07:53:42
pd.merge(df1, df2, on='key')
#[Out]#    data1 key  data2
#[Out]# 0      0   b      1
#[Out]# 1      1   b      1
#[Out]# 2      6   b      1
#[Out]# 3      2   a      0
#[Out]# 4      4   a      0
#[Out]# 5      5   a      0
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Tue, 01 Jul 2014 07:54:37
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1': range(7)})
# Tue, 01 Jul 2014 07:55:13
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
'data2': range(3)})
# Tue, 01 Jul 2014 07:55:43
pd.merge(df3, df4, left_on = 'lkey', right_on='rkey')
#[Out]#    data1 lkey  data2 rkey
#[Out]# 0      0    b      1    b
#[Out]# 1      1    b      1    b
#[Out]# 2      6    b      1    b
#[Out]# 3      2    a      0    a
#[Out]# 4      4    a      0    a
#[Out]# 5      5    a      0    a
#[Out]# 
#[Out]# [6 rows x 4 columns]
# Tue, 01 Jul 2014 07:56:34
pd.merge(df1, df2, how='outer')
#[Out]#    data1 key  data2
#[Out]# 0      0   b      1
#[Out]# 1      1   b      1
#[Out]# 2      6   b      1
#[Out]# 3      2   a      0
#[Out]# 4      4   a      0
#[Out]# 5      5   a      0
#[Out]# 6      3   c    NaN
#[Out]# 7    NaN   d      2
#[Out]# 
#[Out]# [8 rows x 3 columns]
# Tue, 01 Jul 2014 07:57:15
pd.merge(df1, df2, how='left')
#[Out]#    data1 key  data2
#[Out]# 0      0   b      1
#[Out]# 1      1   b      1
#[Out]# 2      6   b      1
#[Out]# 3      2   a      0
#[Out]# 4      4   a      0
#[Out]# 5      5   a      0
#[Out]# 6      3   c    NaN
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Tue, 01 Jul 2014 07:57:29
pd.merge(df1, df2, how='right')
#[Out]#    data1 key  data2
#[Out]# 0      0   b      1
#[Out]# 1      1   b      1
#[Out]# 2      6   b      1
#[Out]# 3      2   a      0
#[Out]# 4      4   a      0
#[Out]# 5      5   a      0
#[Out]# 6    NaN   d      2
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Tue, 01 Jul 2014 07:58:22
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})
# Tue, 01 Jul 2014 07:58:56
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
'data2': range(5)})
# Tue, 01 Jul 2014 07:58:59
df1
#[Out]#    data1 key
#[Out]# 0      0   b
#[Out]# 1      1   b
#[Out]# 2      2   a
#[Out]# 3      3   c
#[Out]# 4      4   a
#[Out]# 5      5   b
#[Out]# 
#[Out]# [6 rows x 2 columns]
# Tue, 01 Jul 2014 07:59:00
df2
#[Out]#    data2 key
#[Out]# 0      0   a
#[Out]# 1      1   b
#[Out]# 2      2   a
#[Out]# 3      3   b
#[Out]# 4      4   d
#[Out]# 
#[Out]# [5 rows x 2 columns]
# Tue, 01 Jul 2014 07:59:44
pd.merge(df1, df2, on='key', how='left')
#[Out]#     data1 key  data2
#[Out]# 0       0   b      1
#[Out]# 1       0   b      3
#[Out]# 2       1   b      1
#[Out]# 3       1   b      3
#[Out]# 4       5   b      1
#[Out]# 5       5   b      3
#[Out]# 6       2   a      0
#[Out]# 7       2   a      2
#[Out]# 8       4   a      0
#[Out]# 9       4   a      2
#[Out]# 10      3   c    NaN
#[Out]# 
#[Out]# [11 rows x 3 columns]
# Tue, 01 Jul 2014 08:03:40
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
'key2': ['one', 'two', 'one'],
'lval': [1, 2, 3]})
# Tue, 01 Jul 2014 08:04:48
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
'key2': ['one', 'one', 'one', 'two'],
'rval': [4, 5, 6, 7]})
# Tue, 01 Jul 2014 08:05:44
pd.merge(left, right, on=['key1', 'key2'], how='outer')
#[Out]#   key1 key2  lval  rval
#[Out]# 0  foo  one     1     4
#[Out]# 1  foo  one     1     5
#[Out]# 2  foo  two     2   NaN
#[Out]# 3  bar  one     3     6
#[Out]# 4  bar  two   NaN     7
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Tue, 01 Jul 2014 08:08:32
pd.merge(left, right, on='key1')
#[Out]#   key1 key2_x  lval key2_y  rval
#[Out]# 0  foo    one     1    one     4
#[Out]# 1  foo    one     1    one     5
#[Out]# 2  foo    two     2    one     4
#[Out]# 3  foo    two     2    one     5
#[Out]# 4  bar    one     3    one     6
#[Out]# 5  bar    one     3    two     7
#[Out]# 
#[Out]# [6 rows x 5 columns]
# Tue, 01 Jul 2014 08:11:57
pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
#[Out]#   key1 key2_left  lval key2_right  rval
#[Out]# 0  foo       one     1        one     4
#[Out]# 1  foo       one     1        one     5
#[Out]# 2  foo       two     2        one     4
#[Out]# 3  foo       two     2        one     5
#[Out]# 4  bar       one     3        one     6
#[Out]# 5  bar       one     3        two     7
#[Out]# 
#[Out]# [6 rows x 5 columns]
# Tue, 01 Jul 2014 08:15:06
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
'value': range(6)})
# Tue, 01 Jul 2014 08:16:03
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
# Tue, 01 Jul 2014 08:16:06
left1
#[Out]#   key  value
#[Out]# 0   a      0
#[Out]# 1   b      1
#[Out]# 2   a      2
#[Out]# 3   a      3
#[Out]# 4   b      4
#[Out]# 5   c      5
#[Out]# 
#[Out]# [6 rows x 2 columns]
# Tue, 01 Jul 2014 08:16:09
right1
#[Out]#    group_val
#[Out]# a        3.5
#[Out]# b        7.0
#[Out]# 
#[Out]# [2 rows x 1 columns]
# Tue, 01 Jul 2014 08:17:05
pd.merge(left1, right1, left_on='key', right_index=True)
#[Out]#   key  value  group_val
#[Out]# 0   a      0        3.5
#[Out]# 2   a      2        3.5
#[Out]# 3   a      3        3.5
#[Out]# 1   b      1        7.0
#[Out]# 4   b      4        7.0
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Tue, 01 Jul 2014 08:21:42
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
#[Out]#   key  value  group_val
#[Out]# 0   a      0        3.5
#[Out]# 2   a      2        3.5
#[Out]# 3   a      3        3.5
#[Out]# 1   b      1        7.0
#[Out]# 4   b      4        7.0
#[Out]# 5   c      5        NaN
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Tue, 01 Jul 2014 08:23:22
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'key2': [2000, 2001, 2002, 2001, 2002],
'data': np.arange(5.)})
# Tue, 01 Jul 2014 08:24:57
righth = DataFrame(np.arange(12).reshape((6, 2)),
index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
[2001, 2000, 2000, 2000, 2001, 2002]],
columns=['event1', 'event2'])
# Tue, 01 Jul 2014 08:25:01
lefth
#[Out]#    data    key1  key2
#[Out]# 0     0    Ohio  2000
#[Out]# 1     1    Ohio  2001
#[Out]# 2     2    Ohio  2002
#[Out]# 3     3  Nevada  2001
#[Out]# 4     4  Nevada  2002
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Tue, 01 Jul 2014 08:25:43
righth
#[Out]#              event1  event2
#[Out]# Nevada 2001       0       1
#[Out]#        2000       2       3
#[Out]# Ohio   2000       4       5
#[Out]#        2000       6       7
#[Out]#        2001       8       9
#[Out]#        2002      10      11
#[Out]# 
#[Out]# [6 rows x 2 columns]
# Tue, 01 Jul 2014 08:27:27
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
#[Out]#    data    key1  key2  event1  event2
#[Out]# 0     0    Ohio  2000       4       5
#[Out]# 0     0    Ohio  2000       6       7
#[Out]# 1     1    Ohio  2001       8       9
#[Out]# 2     2    Ohio  2002      10      11
#[Out]# 3     3  Nevada  2001       0       1
#[Out]# 
#[Out]# [5 rows x 5 columns]
# Tue, 01 Jul 2014 08:28:51
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
#[Out]#    data    key1  key2  event1  event2
#[Out]# 0     0    Ohio  2000       4       5
#[Out]# 0     0    Ohio  2000       6       7
#[Out]# 1     1    Ohio  2001       8       9
#[Out]# 2     2    Ohio  2002      10      11
#[Out]# 3     3  Nevada  2001       0       1
#[Out]# 4     4  Nevada  2002     NaN     NaN
#[Out]# 4   NaN  Nevada  2000       2       3
#[Out]# 
#[Out]# [7 rows x 5 columns]
# Tue, 01 Jul 2014 08:31:18
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.], index=['a', 'c', 'e'],
columns=['Ohio', 'Nevada'])
]
# Tue, 01 Jul 2014 08:31:31
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
columns=['Ohio', 'Nevada'])
# Tue, 01 Jul 2014 08:32:47
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama])
# Tue, 01 Jul 2014 08:33:17
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
# Tue, 01 Jul 2014 08:33:22
left2
#[Out]#    Ohio  Nevada
#[Out]# a     1       2
#[Out]# c     3       4
#[Out]# e     5       6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 08:34:00
right2
#[Out]#    Missouri  Alabama
#[Out]# b         7        8
#[Out]# c         9       10
#[Out]# d        11       12
#[Out]# e        13       14
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 01 Jul 2014 08:35:23
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
#[Out]#    Ohio  Nevada  Missouri  Alabama
#[Out]# a     1       2       NaN      NaN
#[Out]# b   NaN     NaN         7        8
#[Out]# c     3       4         9       10
#[Out]# d   NaN     NaN        11       12
#[Out]# e     5       6        13       14
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Tue, 01 Jul 2014 08:37:14
left2.join(right2, how='outer')
#[Out]#    Ohio  Nevada  Missouri  Alabama
#[Out]# a     1       2       NaN      NaN
#[Out]# b   NaN     NaN         7        8
#[Out]# c     3       4         9       10
#[Out]# d   NaN     NaN        11       12
#[Out]# e     5       6        13       14
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Tue, 01 Jul 2014 08:39:41
left1.join(right1, on='key')
#[Out]#   key  value  group_val
#[Out]# 0   a      0        3.5
#[Out]# 1   b      1        7.0
#[Out]# 2   a      2        3.5
#[Out]# 3   a      3        3.5
#[Out]# 4   b      4        7.0
#[Out]# 5   c      5        NaN
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Tue, 01 Jul 2014 08:41:46
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
# Tue, 01 Jul 2014 08:42:05
left2.join([right2, another])
#[Out]#    Ohio  Nevada  Missouri  Alabama  New York  Oregon
#[Out]# a     1       2       NaN      NaN         7       8
#[Out]# c     3       4         9       10         9      10
#[Out]# e     5       6        13       14        11      12
#[Out]# 
#[Out]# [3 rows x 6 columns]
# Tue, 01 Jul 2014 08:42:33
left2.join([right2, another], how='outer')
#[Out]#    Ohio  Nevada  Missouri  Alabama  New York  Oregon
#[Out]# a     1       2       NaN      NaN         7       8
#[Out]# b   NaN     NaN         7        8       NaN     NaN
#[Out]# c     3       4         9       10         9      10
#[Out]# d   NaN     NaN        11       12       NaN     NaN
#[Out]# e     5       6        13       14        11      12
#[Out]# f   NaN     NaN       NaN      NaN        16      17
#[Out]# 
#[Out]# [6 rows x 6 columns]
# Tue, 01 Jul 2014 23:03:36
arr = np.arange(12).reshape((3, 4))
# Tue, 01 Jul 2014 23:03:39
arr
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11]])
# Tue, 01 Jul 2014 23:03:57
np.concatenate([arr, arr], axis=1)
#[Out]# array([[ 0,  1,  2,  3,  0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7,  4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11,  8,  9, 10, 11]])
# Tue, 01 Jul 2014 23:04:06
np.concatenate([arr, arr], axis=0)
#[Out]# array([[ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11],
#[Out]#        [ 0,  1,  2,  3],
#[Out]#        [ 4,  5,  6,  7],
#[Out]#        [ 8,  9, 10, 11]])
# Tue, 01 Jul 2014 23:05:19
s1 = Series([0, 1], index=['a', 'b'])
# Tue, 01 Jul 2014 23:05:45
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
# Tue, 01 Jul 2014 23:06:06
s3 = Series([5, 6], index=['f', 'g'])
# Tue, 01 Jul 2014 23:06:25
pd.concat([s1, s2, s3])
#[Out]# a    0
#[Out]# b    1
#[Out]# c    2
#[Out]# d    3
#[Out]# e    4
#[Out]# f    5
#[Out]# g    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:07:11
pd.concat([s1, s2, s3], axis=1)
#[Out]#     0   1   2
#[Out]# a   0 NaN NaN
#[Out]# b   1 NaN NaN
#[Out]# c NaN   2 NaN
#[Out]# d NaN   3 NaN
#[Out]# e NaN   4 NaN
#[Out]# f NaN NaN   5
#[Out]# g NaN NaN   6
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Tue, 01 Jul 2014 23:07:45
pd.concat([s1, s2, s3], axis=1, join='inner')
#[Out]# Empty DataFrame
#[Out]# Columns: [0, 1, 2]
#[Out]# Index: []
#[Out]# 
#[Out]# [0 rows x 3 columns]
# Tue, 01 Jul 2014 23:08:14
s4 = pd.concat([s1 * 5, s3])
# Tue, 01 Jul 2014 23:08:34
pd.concat([s1, s4], axis=1)
#[Out]#     0  1
#[Out]# a   0  0
#[Out]# b   1  5
#[Out]# f NaN  5
#[Out]# g NaN  6
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 01 Jul 2014 23:10:26
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
#[Out]#     0   1
#[Out]# a   0   0
#[Out]# c NaN NaN
#[Out]# b   1   5
#[Out]# e NaN NaN
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Tue, 01 Jul 2014 23:12:06
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
# Tue, 01 Jul 2014 23:12:08
result
#[Out]# one    a    0
#[Out]#        b    1
#[Out]# two    a    0
#[Out]#        b    1
#[Out]# three  f    5
#[Out]#        g    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:12:22
result.unstack()
#[Out]#         a   b   f   g
#[Out]# one     0   1 NaN NaN
#[Out]# two     0   1 NaN NaN
#[Out]# three NaN NaN   5   6
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:12:32
result.unstack()
#[Out]#         a   b   f   g
#[Out]# one     0   1 NaN NaN
#[Out]# two     0   1 NaN NaN
#[Out]# three NaN NaN   5   6
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:12:34
result
#[Out]# one    a    0
#[Out]#        b    1
#[Out]# two    a    0
#[Out]#        b    1
#[Out]# three  f    5
#[Out]#        g    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:13:22
pd.concat([s1, s1, s3], axis=1, keys=['one', 'two', 'three'])
#[Out]#    one  two  three
#[Out]# a    0    0    NaN
#[Out]# b    1    1    NaN
#[Out]# f  NaN  NaN      5
#[Out]# g  NaN  NaN      6
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 01 Jul 2014 23:13:53
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])
#[Out]#    one  two  three
#[Out]# a    0  NaN    NaN
#[Out]# b    1  NaN    NaN
#[Out]# c  NaN    2    NaN
#[Out]# d  NaN    3    NaN
#[Out]# e  NaN    4    NaN
#[Out]# f  NaN  NaN      5
#[Out]# g  NaN  NaN      6
#[Out]# 
#[Out]# [7 rows x 3 columns]
# Tue, 01 Jul 2014 23:14:45
df1 = DataFrame(np.arange(6).reshape((3, 2)), index=['a', 'b', 'c'],
columns=['one', 'two'])
# Tue, 01 Jul 2014 23:15:37
df2 = DataFrame(5 + np.arange(4).reshape((2, 2)), index=['a', 'c'],
columns=['three', 'four'])
# Tue, 01 Jul 2014 23:16:10
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
#[Out]#    level1       level2      
#[Out]#       one  two   three  four
#[Out]# a       0    1       5     6
#[Out]# b       2    3     NaN   NaN
#[Out]# c       4    5       7     8
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:17:24
pd.concat({'level1': df1, 'level2': df2}, axis=1)
#[Out]#    level1       level2      
#[Out]#       one  two   three  four
#[Out]# a       0    1       5     6
#[Out]# b       2    3     NaN   NaN
#[Out]# c       4    5       7     8
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:18:38
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower'])
#[Out]# upper  level1       level2      
#[Out]# lower     one  two   three  four
#[Out]# a           0    1       5     6
#[Out]# b           2    3     NaN   NaN
#[Out]# c           4    5       7     8
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:19:39
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
# Tue, 01 Jul 2014 23:20:06
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
# Tue, 01 Jul 2014 23:20:08
df1
#[Out]#           a         b         c         d
#[Out]# 0  0.042501  0.772555  1.508112  0.300231
#[Out]# 1  1.694251 -0.036403 -0.680316  1.129959
#[Out]# 2 -0.287005 -0.401153  0.683854 -0.082944
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:20:12
df2
#[Out]#           b        d         a
#[Out]# 0 -0.207497  0.92876 -0.545224
#[Out]# 1 -0.818765 -1.41214 -1.219254
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:21:11
pd.concat([df1, df2], ignore_index=True)
#[Out]#           a         b         c         d
#[Out]# 0  0.042501  0.772555  1.508112  0.300231
#[Out]# 1  1.694251 -0.036403 -0.680316  1.129959
#[Out]# 2 -0.287005 -0.401153  0.683854 -0.082944
#[Out]# 3 -0.545224 -0.207497       NaN  0.928760
#[Out]# 4 -1.219254 -0.818765       NaN -1.412140
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Tue, 01 Jul 2014 23:23:08
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
index=['f', 'e', 'd', 'c', 'b', 'a'])
# Tue, 01 Jul 2014 23:24:23
a = Series(np.arange(len(a), dtype=np.float64),
index=['f', 'e', 'd', 'c', 'b', 'a'])
# Tue, 01 Jul 2014 23:24:26
a
#[Out]# f    0
#[Out]# e    1
#[Out]# d    2
#[Out]# c    3
#[Out]# b    4
#[Out]# a    5
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:24:40
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
index=['f', 'e', 'd', 'c', 'b', 'a'])
# Tue, 01 Jul 2014 23:24:52
b = Series(np.arange(len(a), dtype=np.float64),
index=['f', 'e', 'd', 'c', 'b', 'a'])
# Tue, 01 Jul 2014 23:24:54
a
#[Out]# f    NaN
#[Out]# e    2.5
#[Out]# d    NaN
#[Out]# c    3.5
#[Out]# b    4.5
#[Out]# a    NaN
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:24:55
b
#[Out]# f    0
#[Out]# e    1
#[Out]# d    2
#[Out]# c    3
#[Out]# b    4
#[Out]# a    5
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:25:15
np.where(pd.isnull(a), b, a)
#[Out]# array([ 0. ,  2.5,  2. ,  3.5,  4.5,  5. ])
# Tue, 01 Jul 2014 23:25:51
b[-1] = np.nan
# Tue, 01 Jul 2014 23:25:52
a
#[Out]# f    NaN
#[Out]# e    2.5
#[Out]# d    NaN
#[Out]# c    3.5
#[Out]# b    4.5
#[Out]# a    NaN
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:25:53
b
#[Out]# f     0
#[Out]# e     1
#[Out]# d     2
#[Out]# c     3
#[Out]# b     4
#[Out]# a   NaN
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:26:06
np.where(pd.isnull(a), b, a)
#[Out]# array([ 0. ,  2.5,  2. ,  3.5,  4.5,  nan])
# Tue, 01 Jul 2014 23:26:42
b[:-2].combine_first(a[2:])
#[Out]# a    NaN
#[Out]# b    4.5
#[Out]# c    3.0
#[Out]# d    2.0
#[Out]# e    1.0
#[Out]# f    0.0
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:29:54
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
'b': [np.nan, 2., np.nan, 6.],
'c': range(2, 18, 4)})
# Tue, 01 Jul 2014 23:30:57
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
'b': [np.nan, 3., 4., 6., 8.]})
# Tue, 01 Jul 2014 23:31:02
df1
#[Out]#     a   b   c
#[Out]# 0   1 NaN   2
#[Out]# 1 NaN   2   6
#[Out]# 2   5 NaN  10
#[Out]# 3 NaN   6  14
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Tue, 01 Jul 2014 23:31:03
df2
#[Out]#     a   b
#[Out]# 0   5 NaN
#[Out]# 1   4   3
#[Out]# 2 NaN   4
#[Out]# 3   3   6
#[Out]# 4   7   8
#[Out]# 
#[Out]# [5 rows x 2 columns]
# Tue, 01 Jul 2014 23:32:01
df3 = DataFrame([[1, 2, 3], [4, 5, 6]])
# Tue, 01 Jul 2014 23:32:03
df3
#[Out]#    0  1  2
#[Out]# 0  1  2  3
#[Out]# 1  4  5  6
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:32:44
df4 = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
# Tue, 01 Jul 2014 23:32:46
df4
#[Out]#    a  b
#[Out]# 0  1  4
#[Out]# 1  2  5
#[Out]# 2  3  6
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 23:33:24
df1.combine_first(df2)
#[Out]#    a   b   c
#[Out]# 0  1 NaN   2
#[Out]# 1  4   2   6
#[Out]# 2  5   4  10
#[Out]# 3  3   6  14
#[Out]# 4  7   8 NaN
#[Out]# 
#[Out]# [5 rows x 3 columns]
# Tue, 01 Jul 2014 23:37:57
data = DataFrame(np.arange(6).reshape((2, 3)),
index=pd.Index(['Ohio', 'Colorado'], name='state'),
columns=pd.Index(['one', 'two', 'three'], name='number'))
# Tue, 01 Jul 2014 23:37:59
data
#[Out]# number    one  two  three
#[Out]# state                    
#[Out]# Ohio        0    1      2
#[Out]# Colorado    3    4      5
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:38:17
result = data.stack()
# Tue, 01 Jul 2014 23:38:19
result
#[Out]# state     number
#[Out]# Ohio      one       0
#[Out]#           two       1
#[Out]#           three     2
#[Out]# Colorado  one       3
#[Out]#           two       4
#[Out]#           three     5
#[Out]# dtype: int32
# Tue, 01 Jul 2014 23:38:46
result.unstack()
#[Out]# number    one  two  three
#[Out]# state                    
#[Out]# Ohio        0    1      2
#[Out]# Colorado    3    4      5
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:39:04
data == result.unstack()
#[Out]# number     one   two three
#[Out]# state                     
#[Out]# Ohio      True  True  True
#[Out]# Colorado  True  True  True
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:40:13
data == result
# Tue, 01 Jul 2014 23:40:59
result.unstack(0)
#[Out]# state   Ohio  Colorado
#[Out]# number                
#[Out]# one        0         3
#[Out]# two        1         4
#[Out]# three      2         5
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 23:41:09
result
#[Out]# state     number
#[Out]# Ohio      one       0
#[Out]#           two       1
#[Out]#           three     2
#[Out]# Colorado  one       3
#[Out]#           two       4
#[Out]#           three     5
#[Out]# dtype: int32
# Tue, 01 Jul 2014 23:41:25
result.unstack(1)
#[Out]# number    one  two  three
#[Out]# state                    
#[Out]# Ohio        0    1      2
#[Out]# Colorado    3    4      5
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:42:34
result.unstack(2)
# Tue, 01 Jul 2014 23:43:19
result.stack(0)
# Tue, 01 Jul 2014 23:43:27
result.unstack(0)
#[Out]# state   Ohio  Colorado
#[Out]# number                
#[Out]# one        0         3
#[Out]# two        1         4
#[Out]# three      2         5
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 23:43:34
result.unstack('state')
#[Out]# state   Ohio  Colorado
#[Out]# number                
#[Out]# one        0         3
#[Out]# two        1         4
#[Out]# three      2         5
#[Out]# 
#[Out]# [3 rows x 2 columns]
# Tue, 01 Jul 2014 23:43:42
result.unstack(1)
#[Out]# number    one  two  three
#[Out]# state                    
#[Out]# Ohio        0    1      2
#[Out]# Colorado    3    4      5
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:43:49
result.unstack('number')
#[Out]# number    one  two  three
#[Out]# state                    
#[Out]# Ohio        0    1      2
#[Out]# Colorado    3    4      5
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Tue, 01 Jul 2014 23:44:01
result
#[Out]# state     number
#[Out]# Ohio      one       0
#[Out]#           two       1
#[Out]#           three     2
#[Out]# Colorado  one       3
#[Out]#           two       4
#[Out]#           three     5
#[Out]# dtype: int32
# Tue, 01 Jul 2014 23:45:28
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
# Tue, 01 Jul 2014 23:45:56
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
# Tue, 01 Jul 2014 23:46:20
data2 = pd.concat([s1, s2], keys=['one', 'two'])
# Tue, 01 Jul 2014 23:46:24
data2
#[Out]# one  a    0
#[Out]#      b    1
#[Out]#      c    2
#[Out]#      d    3
#[Out]# two  c    4
#[Out]#      d    5
#[Out]#      e    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:46:58
data2.unstack()
#[Out]#       a   b  c  d   e
#[Out]# one   0   1  2  3 NaN
#[Out]# two NaN NaN  4  5   6
#[Out]# 
#[Out]# [2 rows x 5 columns]
# Tue, 01 Jul 2014 23:47:44
data2.unstack().stack()
#[Out]# one  a    0
#[Out]#      b    1
#[Out]#      c    2
#[Out]#      d    3
#[Out]# two  c    4
#[Out]#      d    5
#[Out]#      e    6
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:47:57
data2
#[Out]# one  a    0
#[Out]#      b    1
#[Out]#      c    2
#[Out]#      d    3
#[Out]# two  c    4
#[Out]#      d    5
#[Out]#      e    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:48:27
data2.unstack().stack(dropna=False)
#[Out]# one  a     0
#[Out]#      b     1
#[Out]#      c     2
#[Out]#      d     3
#[Out]#      e   NaN
#[Out]# two  a   NaN
#[Out]#      b   NaN
#[Out]#      c     4
#[Out]#      d     5
#[Out]#      e     6
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:49:24
data2.unstack(1).stack(dropna=False)
#[Out]# one  a     0
#[Out]#      b     1
#[Out]#      c     2
#[Out]#      d     3
#[Out]#      e   NaN
#[Out]# two  a   NaN
#[Out]#      b   NaN
#[Out]#      c     4
#[Out]#      d     5
#[Out]#      e     6
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:49:36
data2.unstack(1)
#[Out]#       a   b  c  d   e
#[Out]# one   0   1  2  3 NaN
#[Out]# two NaN NaN  4  5   6
#[Out]# 
#[Out]# [2 rows x 5 columns]
# Tue, 01 Jul 2014 23:49:44
data2.unstack(0)
#[Out]#    one  two
#[Out]# a    0  NaN
#[Out]# b    1  NaN
#[Out]# c    2    4
#[Out]# d    3    5
#[Out]# e  NaN    6
#[Out]# 
#[Out]# [5 rows x 2 columns]
# Tue, 01 Jul 2014 23:50:02
data2.unstack(0).stack(dropna=False)
#[Out]# a  one     0
#[Out]#    two   NaN
#[Out]# b  one     1
#[Out]#    two   NaN
#[Out]# c  one     2
#[Out]#    two     4
#[Out]# d  one     3
#[Out]#    two     5
#[Out]# e  one   NaN
#[Out]#    two     6
#[Out]# dtype: float64
# Tue, 01 Jul 2014 23:50:39
data2
#[Out]# one  a    0
#[Out]#      b    1
#[Out]#      c    2
#[Out]#      d    3
#[Out]# two  c    4
#[Out]#      d    5
#[Out]#      e    6
#[Out]# dtype: int64
# Tue, 01 Jul 2014 23:51:38
df = DataFrame({'left': result, 'right': result + 5},
columns=pd.Index(['left', 'right'], name='side'))
# Tue, 01 Jul 2014 23:51:40
df
#[Out]# side             left  right
#[Out]# state    number             
#[Out]# Ohio     one        0      5
#[Out]#          two        1      6
#[Out]#          three      2      7
#[Out]# Colorado one        3      8
#[Out]#          two        4      9
#[Out]#          three      5     10
#[Out]# 
#[Out]# [6 rows x 2 columns]
# Tue, 01 Jul 2014 23:52:50
df.unstack('state')
#[Out]# side    left            right          
#[Out]# state   Ohio  Colorado   Ohio  Colorado
#[Out]# number                                 
#[Out]# one        0         3      5         8
#[Out]# two        1         4      6         9
#[Out]# three      2         5      7        10
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Tue, 01 Jul 2014 23:53:27
df.unstack('state').stack('side')
#[Out]# state         Ohio  Colorado
#[Out]# number side                 
#[Out]# one    left      0         3
#[Out]#        right     5         8
#[Out]# two    left      1         4
#[Out]#        right     6         9
#[Out]# three  left      2         5
#[Out]#        right     7        10
#[Out]# 
#[Out]# [6 rows x 2 columns]
# Tue, 01 Jul 2014 23:54:23
ldata[:10]
# Tue, 01 Jul 2014 23:57:46
ldata = pd.read_csv('macrodata.csv')
# Tue, 01 Jul 2014 23:57:53
ldata[:10]
#[Out]#    year  quarter   realgdp  realcons  realinv  realgovt  realdpi    cpi  \
#[Out]# 0  1959        1  2710.349    1707.4  286.898   470.045   1886.9  28.98   
#[Out]# 1  1959        2  2778.801    1733.7  310.859   481.301   1919.7  29.15   
#[Out]# 2  1959        3  2775.488    1751.8  289.226   491.260   1916.4  29.35   
#[Out]# 3  1959        4  2785.204    1753.7  299.356   484.052   1931.3  29.37   
#[Out]# 4  1960        1  2847.699    1770.5  331.722   462.199   1955.5  29.54   
#[Out]# 5  1960        2  2834.390    1792.9  298.152   460.400   1966.1  29.55   
#[Out]# 6  1960        3  2839.022    1785.8  296.375   474.676   1967.8  29.75   
#[Out]# 7  1960        4  2802.616    1788.2  259.764   476.434   1966.6  29.84   
#[Out]# 8  1961        1  2819.264    1787.7  266.405   475.854   1984.5  29.81   
#[Out]# 9  1961        2  2872.005    1814.3  286.246   480.328   2014.4  29.92   
#[Out]# 
#[Out]#       m1  tbilrate  unemp      pop  infl  realint  
#[Out]# 0  139.7      2.82    5.8  177.146  0.00     0.00  
#[Out]# 1  141.7      3.08    5.1  177.830  2.34     0.74  
#[Out]# 2  140.5      3.82    5.3  178.657  2.74     1.09  
#[Out]# 3  140.0      4.33    5.6  179.386  0.27     4.06  
#[Out]# 4  139.6      3.50    5.2  180.007  2.31     1.19  
#[Out]# 5  140.2      2.68    5.2  180.671  0.14     2.55  
#[Out]# 6  140.9      2.36    5.6  181.528  2.70    -0.34  
#[Out]# 7  141.1      2.29    6.3  182.287  1.21     1.08  
#[Out]# 8  142.1      2.37    6.8  182.992 -0.40     2.77  
#[Out]# 9  142.9      2.29    7.0  183.691  1.47     0.81  
#[Out]# 
#[Out]# [10 rows x 14 columns]
# Wed, 02 Jul 2014 00:02:57
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:02:59
ldata[:10]
#[Out]#                   date      item     value
#[Out]# 0  1959-03-31 00:00:00   realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00      infl     0.000
#[Out]# 2  1959-03-31 00:00:00     unemp     5.800
#[Out]# 3  1959-06-30 00:00:00   realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00      infl     2.340
#[Out]# 5  1959-06-30 00:00:00     unemp     5.100
#[Out]# 6  1959-09-30 00:00:00   realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00      infl     2.740
#[Out]# 8  1959-09-30 00:00:00     unemp     5.300
#[Out]# 9  1959-12-31 00:00:00   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:04:12
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:05:18
ldata
#[Out]#                   date      item     value
#[Out]# 0  1959-03-31 00:00:00   realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00      infl     0.000
#[Out]# 2  1959-03-31 00:00:00     unemp     5.800
#[Out]# 3  1959-06-30 00:00:00   realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00      infl     2.340
#[Out]# 5  1959-06-30 00:00:00     unemp     5.100
#[Out]# 6  1959-09-30 00:00:00   realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00      infl     2.740
#[Out]# 8  1959-09-30 00:00:00     unemp     5.300
#[Out]# 9  1959-12-31 00:00:00   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:05:54
ldata.stack('item')
# Wed, 02 Jul 2014 00:06:18
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:07:05
pd.stats(ldata)
# Wed, 02 Jul 2014 00:08:05
ldata = pd.read_csv('ldata.csv', index='date')
# Wed, 02 Jul 2014 00:08:30
ldata = DataFrame(ldata, index='date')
# Wed, 02 Jul 2014 00:09:35
!type ldata.csv
# Wed, 02 Jul 2014 00:12:27
ldata = pd.read_csv('ldata.csv', index_col='date', parse_dates=True)
# Wed, 02 Jul 2014 00:12:31
ldata
#[Out]#                 item     value
#[Out]# date                          
#[Out]# 1959-03-31   realgdp  2710.349
#[Out]# 1959-03-31      infl     0.000
#[Out]# 1959-03-31     unemp     5.800
#[Out]# 1959-06-30   realgdp  2778.801
#[Out]# 1959-06-30      infl     2.340
#[Out]# 1959-06-30     unemp     5.100
#[Out]# 1959-09-30   realgdp  2775.488
#[Out]# 1959-09-30      infl     2.740
#[Out]# 1959-09-30     unemp     5.300
#[Out]# 1959-12-31   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 2 columns]
# Wed, 02 Jul 2014 00:13:12
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:13:41
ldata
#[Out]#                 item     value
#[Out]# date                          
#[Out]# 1959-03-31   realgdp  2710.349
#[Out]# 1959-03-31      infl     0.000
#[Out]# 1959-03-31     unemp     5.800
#[Out]# 1959-06-30   realgdp  2778.801
#[Out]# 1959-06-30      infl     2.340
#[Out]# 1959-06-30     unemp     5.100
#[Out]# 1959-09-30   realgdp  2775.488
#[Out]# 1959-09-30      infl     2.740
#[Out]# 1959-09-30     unemp     5.300
#[Out]# 1959-12-31   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 2 columns]
# Wed, 02 Jul 2014 00:14:39
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:14:47
ldata[:10]
#[Out]#                   date      item     value
#[Out]# 0  1959-03-31 00:00:00   realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00      infl     0.000
#[Out]# 2  1959-03-31 00:00:00     unemp     5.800
#[Out]# 3  1959-06-30 00:00:00   realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00      infl     2.340
#[Out]# 5  1959-06-30 00:00:00     unemp     5.100
#[Out]# 6  1959-09-30 00:00:00   realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00      infl     2.740
#[Out]# 8  1959-09-30 00:00:00     unemp     5.300
#[Out]# 9  1959-12-31 00:00:00   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:15:04
pivoted = ldata.pivot('date', 'item')
# Wed, 02 Jul 2014 00:15:51
ldata
#[Out]#                   date      item     value
#[Out]# 0  1959-03-31 00:00:00   realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00      infl     0.000
#[Out]# 2  1959-03-31 00:00:00     unemp     5.800
#[Out]# 3  1959-06-30 00:00:00   realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00      infl     2.340
#[Out]# 5  1959-06-30 00:00:00     unemp     5.100
#[Out]# 6  1959-09-30 00:00:00   realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00      infl     2.740
#[Out]# 8  1959-09-30 00:00:00     unemp     5.300
#[Out]# 9  1959-12-31 00:00:00   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:17:54
!type ldata.csv
# Wed, 02 Jul 2014 00:19:35
pd.pivot?
# Wed, 02 Jul 2014 00:20:27
ldata
#[Out]#                   date      item     value
#[Out]# 0  1959-03-31 00:00:00   realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00      infl     0.000
#[Out]# 2  1959-03-31 00:00:00     unemp     5.800
#[Out]# 3  1959-06-30 00:00:00   realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00      infl     2.340
#[Out]# 5  1959-06-30 00:00:00     unemp     5.100
#[Out]# 6  1959-09-30 00:00:00   realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00      infl     2.740
#[Out]# 8  1959-09-30 00:00:00     unemp     5.300
#[Out]# 9  1959-12-31 00:00:00   realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:20:47
pivoted = ldata.pivot('date', 'item', values='value')
# Wed, 02 Jul 2014 00:21:15
ldata.sum()
#[Out]# date      1959-03-31 00:00:001959-03-31 00:00:001959-03-...
#[Out]#  item      realgdp infl unemp realgdp infl unemp realgdp...
#[Out]#  value                                            11071.122
#[Out]# dtype: object
# Wed, 02 Jul 2014 00:21:34
ldata.sum('value')
# Wed, 02 Jul 2014 00:22:15
macrodata = pd.read_csv('macrodata.csv')
# Wed, 02 Jul 2014 00:22:21
macrodata.head()
#[Out]#    year  quarter   realgdp  realcons  realinv  realgovt  realdpi    cpi  \
#[Out]# 0  1959        1  2710.349    1707.4  286.898   470.045   1886.9  28.98   
#[Out]# 1  1959        2  2778.801    1733.7  310.859   481.301   1919.7  29.15   
#[Out]# 2  1959        3  2775.488    1751.8  289.226   491.260   1916.4  29.35   
#[Out]# 3  1959        4  2785.204    1753.7  299.356   484.052   1931.3  29.37   
#[Out]# 4  1960        1  2847.699    1770.5  331.722   462.199   1955.5  29.54   
#[Out]# 
#[Out]#       m1  tbilrate  unemp      pop  infl  realint  
#[Out]# 0  139.7      2.82    5.8  177.146  0.00     0.00  
#[Out]# 1  141.7      3.08    5.1  177.830  2.34     0.74  
#[Out]# 2  140.5      3.82    5.3  178.657  2.74     1.09  
#[Out]# 3  140.0      4.33    5.6  179.386  0.27     4.06  
#[Out]# 4  139.6      3.50    5.2  180.007  2.31     1.19  
#[Out]# 
#[Out]# [5 rows x 14 columns]
# Wed, 02 Jul 2014 00:23:15
pivoted = macrodata.pivot('year', 'quarter', 'realgdp')
# Wed, 02 Jul 2014 00:23:24
pivoted.head()
#[Out]# quarter         1         2         3         4
#[Out]# year                                           
#[Out]# 1959     2710.349  2778.801  2775.488  2785.204
#[Out]# 1960     2847.699  2834.390  2839.022  2802.616
#[Out]# 1961     2819.264  2872.005  2918.419  2977.830
#[Out]# 1962     3031.241  3064.709  3093.047  3100.563
#[Out]# 1963     3141.087  3180.447  3240.332  3264.967
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Wed, 02 Jul 2014 00:25:31
pivoted = macrodata.pivot('year', 'quarter')
# Wed, 02 Jul 2014 00:25:41
pivoted[:5]
#[Out]# Empty DataFrame
#[Out]# Columns: [(realgdp, 1.0), (realgdp, 2.0), (realgdp, 3.0), (realgdp, 4.0), (realcons, 1.0), (realcons, 2.0), (realcons, 3.0), (realcons, 4.0), (realinv, 1.0), (realinv, 2.0), (realinv, 3.0), (realinv, 4.0), (realgovt, 1.0), (realgovt, 2.0), (realgovt, 3.0), (realgovt, 4.0), (realdpi, 1.0), (realdpi, 2.0), (realdpi, 3.0), (realdpi, 4.0), (cpi, 1.0), (cpi, 2.0), (cpi, 3.0), (cpi, 4.0), (m1, 1.0), (m1, 2.0), (m1, 3.0), (m1, 4.0), (tbilrate, 1.0), (tbilrate, 2.0), (tbilrate, 3.0), (tbilrate, 4.0), (unemp, 1.0), (unemp, 2.0), (unemp, 3.0), (unemp, 4.0), (pop, 1.0), (pop, 2.0), (pop, 3.0), (pop, 4.0), (infl, 1.0), (infl, 2.0), (infl, 3.0), (infl, 4.0), (realint, 1.0), (realint, 2.0), (realint, 3.0), (realint, 4.0)]
#[Out]# Index: []
#[Out]# 
#[Out]# [0 rows x 48 columns]
# Wed, 02 Jul 2014 00:27:33
unstacked = ldata.set_index(['date', 'item']).unstack('item')
# Wed, 02 Jul 2014 00:29:30
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:29:32
ldata
#[Out]#                 'date'      'item'   'value'
#[Out]# 0  1959-03-31 00:00:00   'realgdp'  2710.349
#[Out]# 1  1959-03-31 00:00:00      'infl'     0.000
#[Out]# 2  1959-03-31 00:00:00     'unemp'     5.800
#[Out]# 3  1959-06-30 00:00:00   'realgdp'  2778.801
#[Out]# 4  1959-06-30 00:00:00      'infl'     2.340
#[Out]# 5  1959-06-30 00:00:00     'unemp'     5.100
#[Out]# 6  1959-09-30 00:00:00   'realgdp'  2775.488
#[Out]# 7  1959-09-30 00:00:00      'infl'     2.740
#[Out]# 8  1959-09-30 00:00:00     'unemp'     5.300
#[Out]# 9  1959-12-31 00:00:00   'realgdp'  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:29:59
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:32:40
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:32:42
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:34:28
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:34:29
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:35:11
pivoted.head()
#[Out]# item             infl   realgdp  unemp
#[Out]# date                                  
#[Out]# 12/31/1959 0:00   NaN  2785.204    NaN
#[Out]# 3/31/1959 0:00   0.00  2710.349    5.8
#[Out]# 6/30/1959 0:00   2.34  2778.801    5.1
#[Out]# 9/30/1959 0:00   2.74  2775.488    5.3
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Wed, 02 Jul 2014 00:37:30
ldata = pd.read_csv('ldata.csv')
# Wed, 02 Jul 2014 00:37:33
pivoted = ldata.pivot('date', 'item', 'value')
# Wed, 02 Jul 2014 00:37:39
pivoted.head()
#[Out]# item                 infl   realgdp  unemp
#[Out]# date                                      
#[Out]# 1959-03-31 00:00:00  0.00  2710.349    5.8
#[Out]# 1959-06-30 00:00:00  2.34  2778.801    5.1
#[Out]# 1959-09-30 00:00:00  2.74  2775.488    5.3
#[Out]# 1959-12-31 00:00:00   NaN  2785.204    NaN
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Wed, 02 Jul 2014 00:38:45
ldata
#[Out]#                   date     item     value
#[Out]# 0  1959-03-31 00:00:00  realgdp  2710.349
#[Out]# 1  1959-03-31 00:00:00     infl     0.000
#[Out]# 2  1959-03-31 00:00:00    unemp     5.800
#[Out]# 3  1959-06-30 00:00:00  realgdp  2778.801
#[Out]# 4  1959-06-30 00:00:00     infl     2.340
#[Out]# 5  1959-06-30 00:00:00    unemp     5.100
#[Out]# 6  1959-09-30 00:00:00  realgdp  2775.488
#[Out]# 7  1959-09-30 00:00:00     infl     2.740
#[Out]# 8  1959-09-30 00:00:00    unemp     5.300
#[Out]# 9  1959-12-31 00:00:00  realgdp  2785.204
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 02 Jul 2014 00:38:49
pivoted
#[Out]# item                 infl   realgdp  unemp
#[Out]# date                                      
#[Out]# 1959-03-31 00:00:00  0.00  2710.349    5.8
#[Out]# 1959-06-30 00:00:00  2.34  2778.801    5.1
#[Out]# 1959-09-30 00:00:00  2.74  2775.488    5.3
#[Out]# 1959-12-31 00:00:00   NaN  2785.204    NaN
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Wed, 02 Jul 2014 00:39:18
ldata['value2'] = np.random.randn(len(ldata))
# Wed, 02 Jul 2014 00:39:21
ldata
#[Out]#                   date     item     value    value2
#[Out]# 0  1959-03-31 00:00:00  realgdp  2710.349 -0.281811
#[Out]# 1  1959-03-31 00:00:00     infl     0.000 -0.196519
#[Out]# 2  1959-03-31 00:00:00    unemp     5.800 -0.553107
#[Out]# 3  1959-06-30 00:00:00  realgdp  2778.801 -0.584687
#[Out]# 4  1959-06-30 00:00:00     infl     2.340 -0.513601
#[Out]# 5  1959-06-30 00:00:00    unemp     5.100  0.797450
#[Out]# 6  1959-09-30 00:00:00  realgdp  2775.488 -1.576455
#[Out]# 7  1959-09-30 00:00:00     infl     2.740 -0.921909
#[Out]# 8  1959-09-30 00:00:00    unemp     5.300  1.100640
#[Out]# 9  1959-12-31 00:00:00  realgdp  2785.204 -0.480383
#[Out]# 
#[Out]# [10 rows x 4 columns]
# Wed, 02 Jul 2014 00:39:50
pivoted = ldata.pivot('date', 'item')
# Wed, 02 Jul 2014 00:39:54
pivoted
#[Out]#                      value                     value2                    
#[Out]# item                  infl   realgdp  unemp      infl   realgdp     unemp
#[Out]# date                                                                     
#[Out]# 1959-03-31 00:00:00   0.00  2710.349    5.8 -0.196519 -0.281811 -0.553107
#[Out]# 1959-06-30 00:00:00   2.34  2778.801    5.1 -0.513601 -0.584687  0.797450
#[Out]# 1959-09-30 00:00:00   2.74  2775.488    5.3 -0.921909 -1.576455  1.100640
#[Out]# 1959-12-31 00:00:00    NaN  2785.204    NaN       NaN -0.480383       NaN
#[Out]# 
#[Out]# [4 rows x 6 columns]
# Wed, 02 Jul 2014 00:40:28
unstacked = ldata.set_index(['date', 'item']).unstack('item')
# Wed, 02 Jul 2014 00:40:31
unstacked
#[Out]#                      value                     value2                    
#[Out]# item                  infl   realgdp  unemp      infl   realgdp     unemp
#[Out]# date                                                                     
#[Out]# 1959-03-31 00:00:00   0.00  2710.349    5.8 -0.196519 -0.281811 -0.553107
#[Out]# 1959-06-30 00:00:00   2.34  2778.801    5.1 -0.513601 -0.584687  0.797450
#[Out]# 1959-09-30 00:00:00   2.74  2775.488    5.3 -0.921909 -1.576455  1.100640
#[Out]# 1959-12-31 00:00:00    NaN  2785.204    NaN       NaN -0.480383       NaN
#[Out]# 
#[Out]# [4 rows x 6 columns]
%logstart -o -r -t pandas_ch07_log.py append
%logstop
pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
cd ..\\..
cd "Google Drive\\Python For Data Analysis\\pydata-book
ls
cd ch07
ls
