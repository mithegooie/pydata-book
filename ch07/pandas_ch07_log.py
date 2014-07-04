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
# Fri, 04 Jul 2014 09:13:00
data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
'k2': [1,1,2,3,3,4,4]})
# Fri, 04 Jul 2014 09:13:08
import pandas
# Fri, 04 Jul 2014 09:13:38
import pandas as pd
# Fri, 04 Jul 2014 09:13:43
import numpy as np
# Fri, 04 Jul 2014 09:13:50
from pandas import DataFrame, Series
# Fri, 04 Jul 2014 09:14:03
data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
'k2': [1,1,2,3,3,4,4]})
# Fri, 04 Jul 2014 09:14:07
data
#[Out]#     k1  k2
#[Out]# 0  one   1
#[Out]# 1  one   1
#[Out]# 2  one   2
#[Out]# 3  two   3
#[Out]# 4  two   3
#[Out]# 5  two   4
#[Out]# 6  two   4
#[Out]# 
#[Out]# [7 rows x 2 columns]
# Fri, 04 Jul 2014 09:14:22
data.duplicated()
#[Out]# 0    False
#[Out]# 1     True
#[Out]# 2    False
#[Out]# 3    False
#[Out]# 4     True
#[Out]# 5    False
#[Out]# 6     True
#[Out]# dtype: bool
# Fri, 04 Jul 2014 09:14:57
data.drop_duplicates()
#[Out]#     k1  k2
#[Out]# 0  one   1
#[Out]# 2  one   2
#[Out]# 3  two   3
#[Out]# 5  two   4
#[Out]# 
#[Out]# [4 rows x 2 columns]
# Fri, 04 Jul 2014 09:15:36
data['v1'] = range(7)
# Fri, 04 Jul 2014 09:15:57
data.drop_duplicates(['k1'])
#[Out]#     k1  k2  v1
#[Out]# 0  one   1   0
#[Out]# 3  two   3   3
#[Out]# 
#[Out]# [2 rows x 3 columns]
# Fri, 04 Jul 2014 09:16:52
data.drop_duplicates(['k1', 'k2'], take_last=True)
#[Out]#     k1  k2  v1
#[Out]# 1  one   1   1
#[Out]# 2  one   2   2
#[Out]# 4  two   3   4
#[Out]# 6  two   4   6
#[Out]# 
#[Out]# [4 rows x 3 columns]
# Fri, 04 Jul 2014 09:25:28
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef, 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
# Fri, 04 Jul 2014 09:25:56
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef, 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
# Fri, 04 Jul 2014 09:26:31
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
'ounces': [4,3,12,6,7.5,8,3,5,6]})
# Fri, 04 Jul 2014 09:26:33
data
#[Out]#           food  ounces
#[Out]# 0        bacon     4.0
#[Out]# 1  pulled pork     3.0
#[Out]# 2        bacon    12.0
#[Out]# 3     Pastrami     6.0
#[Out]# 4  corned beef     7.5
#[Out]# 5        Bacon     8.0
#[Out]# 6     pastrami     3.0
#[Out]# 7    honey ham     5.0
#[Out]# 8     nova lox     6.0
#[Out]# 
#[Out]# [9 rows x 2 columns]
# Fri, 04 Jul 2014 09:28:16
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
# Fri, 04 Jul 2014 09:30:22
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
# Fri, 04 Jul 2014 09:30:25
data
#[Out]#           food  ounces  animal
#[Out]# 0        bacon     4.0     pig
#[Out]# 1  pulled pork     3.0     pig
#[Out]# 2        bacon    12.0     pig
#[Out]# 3     Pastrami     6.0     cow
#[Out]# 4  corned beef     7.5     cow
#[Out]# 5        Bacon     8.0     pig
#[Out]# 6     pastrami     3.0     cow
#[Out]# 7    honey ham     5.0     pig
#[Out]# 8     nova lox     6.0  salmon
#[Out]# 
#[Out]# [9 rows x 3 columns]
# Fri, 04 Jul 2014 09:31:35
data['food'].map(lambda x: meat_to_animal[x.lower()])
#[Out]# 0       pig
#[Out]# 1       pig
#[Out]# 2       pig
#[Out]# 3       cow
#[Out]# 4       cow
#[Out]# 5       pig
#[Out]# 6       cow
#[Out]# 7       pig
#[Out]# 8    salmon
#[Out]# Name: food, dtype: object
# Fri, 04 Jul 2014 09:32:31
map?
# Fri, 04 Jul 2014 09:33:21
pd.map?
# Fri, 04 Jul 2014 09:33:35
DataFrame.map?
# Fri, 04 Jul 2014 09:35:30
map(lambda x: meat_to_animal[x.lower()], data['food'])
#[Out]# ['pig', 'pig', 'pig', 'cow', 'cow', 'pig', 'cow', 'pig', 'salmon']
# Fri, 04 Jul 2014 09:36:56
meat_to_animal['Pastrami'.lower()]
#[Out]# 'cow'
# Fri, 04 Jul 2014 09:37:08
'Pastrami'.lower()
#[Out]# 'pastrami'
# Fri, 04 Jul 2014 09:37:57
data = Series([1., -999., 2., -999., -1000., 3.])
# Fri, 04 Jul 2014 09:38:00
data
#[Out]# 0       1
#[Out]# 1    -999
#[Out]# 2       2
#[Out]# 3    -999
#[Out]# 4   -1000
#[Out]# 5       3
#[Out]# dtype: float64
# Fri, 04 Jul 2014 09:38:41
data.replace(-999, np.nan)
#[Out]# 0       1
#[Out]# 1     NaN
#[Out]# 2       2
#[Out]# 3     NaN
#[Out]# 4   -1000
#[Out]# 5       3
#[Out]# dtype: float64
# Fri, 04 Jul 2014 09:39:07
data.replace([-999, -1000], np.nan)
#[Out]# 0     1
#[Out]# 1   NaN
#[Out]# 2     2
#[Out]# 3   NaN
#[Out]# 4   NaN
#[Out]# 5     3
#[Out]# dtype: float64
# Fri, 04 Jul 2014 09:39:21
data.replace([-999, -1000], [np.nan, 0])
#[Out]# 0     1
#[Out]# 1   NaN
#[Out]# 2     2
#[Out]# 3   NaN
#[Out]# 4     0
#[Out]# 5     3
#[Out]# dtype: float64
# Fri, 04 Jul 2014 09:39:50
data.replace({-999: np.nan, -1000: 0})
#[Out]# 0     1
#[Out]# 1   NaN
#[Out]# 2     2
#[Out]# 3   NaN
#[Out]# 4     0
#[Out]# 5     3
#[Out]# dtype: float64
# Fri, 04 Jul 2014 09:41:20
data = DataFrame(np.arange(12).reshape((3,4)),
index=['Ohio', 'Colorado', 'New York'],
columns=['one', 'two', 'three', 'four'])
# Fri, 04 Jul 2014 09:58:12
data.index.map(str.upper)
#[Out]# array(['OHIO', 'COLORADO', 'NEW YORK'], dtype=object)
# Fri, 04 Jul 2014 09:58:38
data.index = data.index.map(str.upper)
# Fri, 04 Jul 2014 09:58:40
data
#[Out]#           one  two  three  four
#[Out]# OHIO        0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 09:59:50
data.rename(index=str.title, columns=str.upper)
#[Out]#           ONE  TWO  THREE  FOUR
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# New York    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 09:59:53
data.title
# Fri, 04 Jul 2014 10:01:08
DataFrame.rename?
# Fri, 04 Jul 2014 10:02:19
DataFrame?
# Fri, 04 Jul 2014 10:02:46
title?
# Fri, 04 Jul 2014 10:03:49
DataFrame.title?
# Fri, 04 Jul 2014 10:04:17
str.title?
# Fri, 04 Jul 2014 10:05:26
data.rename(index=str.title, columns=str.upper)
#[Out]#           ONE  TWO  THREE  FOUR
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# New York    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:05:33
data.rename(index=str.lower, columns=str.upper)
#[Out]#           ONE  TWO  THREE  FOUR
#[Out]# ohio        0    1      2     3
#[Out]# colorado    4    5      6     7
#[Out]# new york    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:05:41
data.rename(index=str.title, columns=str.upper)
#[Out]#           ONE  TWO  THREE  FOUR
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# New York    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:05:50
data.rename(index=str.upper, columns=str.upper)
#[Out]#           ONE  TWO  THREE  FOUR
#[Out]# OHIO        0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:06:02
data
#[Out]#           one  two  three  four
#[Out]# OHIO        0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:09:20
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})
#[Out]#           one  two  peekaboo  four
#[Out]# INDIANA     0    1         2     3
#[Out]# COLORADO    4    5         6     7
#[Out]# NEW YORK    8    9        10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:09:59
data
#[Out]#           one  two  three  four
#[Out]# OHIO        0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:10:03
data.rename()
# Fri, 04 Jul 2014 10:10:24
data.rename(index=index)
# Fri, 04 Jul 2014 10:10:44
data.rename(index=str.title)
#[Out]#           one  two  three  four
#[Out]# Ohio        0    1      2     3
#[Out]# Colorado    4    5      6     7
#[Out]# New York    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:11:05
data.rename(index=data.index
)
# Fri, 04 Jul 2014 10:11:46
data.index
#[Out]# Index([u'OHIO', u'COLORADO', u'NEW YORK'], dtype='object')
# Fri, 04 Jul 2014 10:12:22
data.rename(index=str)
#[Out]#           one  two  three  four
#[Out]# OHIO        0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:12:30
str?
# Fri, 04 Jul 2014 10:13:29
DataFrame.rename?
# Fri, 04 Jul 2014 10:15:49
_ = data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
# Fri, 04 Jul 2014 10:16:06
data
#[Out]#           one  two  three  four
#[Out]# INDIANA     0    1      2     3
#[Out]# COLORADO    4    5      6     7
#[Out]# NEW YORK    8    9     10    11
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 10:33:45
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
# Fri, 04 Jul 2014 10:34:15
bins = [18,25,35,60,100]
# Fri, 04 Jul 2014 10:34:28
cats = pd.cut(ages, bins)
# Fri, 04 Jul 2014 10:34:31
cats
#[Out]#   (18, 25]
#[Out]#   (18, 25]
#[Out]#   (18, 25]
#[Out]#   (25, 35]
#[Out]#   (18, 25]
#[Out]#   (18, 25]
#[Out]#   (35, 60]
#[Out]#   (25, 35]
#[Out]#  (60, 100]
#[Out]#   (35, 60]
#[Out]#   (35, 60]
#[Out]#   (25, 35]
#[Out]# Levels (4): Index(['(18, 25]', '(25, 35]', '(35, 60]', '(60, 100]'], dtype=object)
# Fri, 04 Jul 2014 10:36:47
cats.labels
#[Out]# array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int64)
# Fri, 04 Jul 2014 10:36:59
cats.levels
#[Out]# Index([u'(18, 25]', u'(25, 35]', u'(35, 60]', u'(60, 100]'], dtype='object')
# Fri, 04 Jul 2014 10:38:01
pd.value_counts(cats)
#[Out]# (18, 25]     5
#[Out]# (35, 60]     3
#[Out]# (25, 35]     3
#[Out]# (60, 100]    1
#[Out]# dtype: int64
# Fri, 04 Jul 2014 10:39:42
pd.cut(ages, [18,26,36,61,100], right=False)
#[Out]#   [18, 26)
#[Out]#   [18, 26)
#[Out]#   [18, 26)
#[Out]#   [26, 36)
#[Out]#   [18, 26)
#[Out]#   [18, 26)
#[Out]#   [36, 61)
#[Out]#   [26, 36)
#[Out]#  [61, 100)
#[Out]#   [36, 61)
#[Out]#   [36, 61)
#[Out]#   [26, 36)
#[Out]# Levels (4): Index(['[18, 26)', '[26, 36)', '[36, 61)', '[61, 100)'], dtype=object)
# Fri, 04 Jul 2014 10:40:12
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# Fri, 04 Jul 2014 10:40:28
pd.cut(ages, bins, labels=group_names)
#[Out]#       Youth
#[Out]#       Youth
#[Out]#       Youth
#[Out]#  YoungAdult
#[Out]#       Youth
#[Out]#       Youth
#[Out]#  MiddleAged
#[Out]#  YoungAdult
#[Out]#      Senior
#[Out]#  MiddleAged
#[Out]#  MiddleAged
#[Out]#  YoungAdult
#[Out]# Levels (4): Index(['Youth', 'YoungAdult', 'MiddleAged', 'Senior'], dtype=object)
# Fri, 04 Jul 2014 10:41:28
data = np.random.rand(20)
# Fri, 04 Jul 2014 10:41:39
pd.cut(data, 4, precision=2)
#[Out]#  (0.56, 0.77]
#[Out]#  (0.56, 0.77]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.56, 0.77]
#[Out]#  (0.35, 0.56]
#[Out]#  (0.35, 0.56]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.35, 0.56]
#[Out]#  (0.14, 0.35]
#[Out]#  (0.35, 0.56]
#[Out]#  (0.77, 0.98]
#[Out]#  (0.35, 0.56]
#[Out]# Levels (4): Index(['(0.14, 0.35]', '(0.35, 0.56]', '(0.56, 0.77]',
#[Out]#                    '(0.77, 0.98]'], dtype=object)
# Fri, 04 Jul 2014 10:43:07
data = np.random.rand(1000)
# Fri, 04 Jul 2014 10:43:18
cats = pd.qcut(data, 4)
# Fri, 04 Jul 2014 10:43:20
cats
#[Out]#      (0.74, 0.999]
#[Out]#      (0.74, 0.999]
#[Out]#  [0.000456, 0.252]
#[Out]#        (0.5, 0.74]
#[Out]#       (0.252, 0.5]
#[Out]#  [0.000456, 0.252]
#[Out]#      (0.74, 0.999]
#[Out]#       (0.252, 0.5]
#[Out]#       (0.252, 0.5]
#[Out]#        (0.5, 0.74]
#[Out]#        (0.5, 0.74]
#[Out]#      (0.74, 0.999]
#[Out]#        (0.5, 0.74]
#[Out]# ...
#[Out]#       (0.252, 0.5]
#[Out]#       (0.252, 0.5]
#[Out]#  [0.000456, 0.252]
#[Out]#       (0.252, 0.5]
#[Out]#      (0.74, 0.999]
#[Out]#        (0.5, 0.74]
#[Out]#        (0.5, 0.74]
#[Out]#       (0.252, 0.5]
#[Out]#  [0.000456, 0.252]
#[Out]#        (0.5, 0.74]
#[Out]#       (0.252, 0.5]
#[Out]#       (0.252, 0.5]
#[Out]#        (0.5, 0.74]
#[Out]# Levels (4): Index(['[0.000456, 0.252]', '(0.252, 0.5]', '(0.5, 0.74]',
#[Out]#                    '(0.74, 0.999]'], dtype=object)
#[Out]# Length: 1000
# Fri, 04 Jul 2014 10:43:38
pd.value_counts(cats)
#[Out]# (0.252, 0.5]         250
#[Out]# (0.74, 0.999]        250
#[Out]# (0.5, 0.74]          250
#[Out]# [0.000456, 0.252]    250
#[Out]# dtype: int64
# Fri, 04 Jul 2014 10:44:39
pd.value_counts(pd.cut(ages, bins))
#[Out]# (18, 25]     5
#[Out]# (35, 60]     3
#[Out]# (25, 35]     3
#[Out]# (60, 100]    1
#[Out]# dtype: int64
# Fri, 04 Jul 2014 10:45:48
cats1 = pd.cut(data, 4)
# Fri, 04 Jul 2014 10:46:01
pd.value_counts(cats1)
#[Out]# (0.5, 0.749]         263
#[Out]# (-0.000542, 0.25]    250
#[Out]# (0.25, 0.5]          249
#[Out]# (0.749, 0.999]       238
#[Out]# dtype: int64
# Fri, 04 Jul 2014 10:47:02
pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
#[Out]#  (0.881, 0.999]
#[Out]#  (0.881, 0.999]
#[Out]#   (0.0973, 0.5]
#[Out]#    (0.5, 0.881]
#[Out]#   (0.0973, 0.5]
#[Out]#   (0.0973, 0.5]
#[Out]#    (0.5, 0.881]
#[Out]#   (0.0973, 0.5]
#[Out]#   (0.0973, 0.5]
#[Out]#    (0.5, 0.881]
#[Out]#    (0.5, 0.881]
#[Out]#    (0.5, 0.881]
#[Out]#    (0.5, 0.881]
#[Out]# ...
#[Out]#  (0.0973, 0.5]
#[Out]#  (0.0973, 0.5]
#[Out]#  (0.0973, 0.5]
#[Out]#  (0.0973, 0.5]
#[Out]#   (0.5, 0.881]
#[Out]#   (0.5, 0.881]
#[Out]#   (0.5, 0.881]
#[Out]#  (0.0973, 0.5]
#[Out]#  (0.0973, 0.5]
#[Out]#   (0.5, 0.881]
#[Out]#  (0.0973, 0.5]
#[Out]#  (0.0973, 0.5]
#[Out]#   (0.5, 0.881]
#[Out]# Levels (4): Index(['[0.000456, 0.0973]', '(0.0973, 0.5]',
#[Out]#                    '(0.5, 0.881]', '(0.881, 0.999]'], dtype=object)
#[Out]# Length: 1000
# Fri, 04 Jul 2014 10:48:14
pd.value_counts(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))
#[Out]# (0.0973, 0.5]         400
#[Out]# (0.5, 0.881]          400
#[Out]# (0.881, 0.999]        100
#[Out]# [0.000456, 0.0973]    100
#[Out]# dtype: int64
# Fri, 04 Jul 2014 12:08:55
np.random.seed(12345)
# Fri, 04 Jul 2014 12:09:16
data = DataFrame(np.random.randn(1000,4))
# Fri, 04 Jul 2014 12:09:24
data.describe()
#[Out]#                  0            1            2            3
#[Out]# count  1000.000000  1000.000000  1000.000000  1000.000000
#[Out]# mean     -0.067684     0.067924     0.025598    -0.002298
#[Out]# std       0.998035     0.992106     1.006835     0.996794
#[Out]# min      -3.428254    -3.548824    -3.184377    -3.745356
#[Out]# 25%      -0.774890    -0.591841    -0.641675    -0.644144
#[Out]# 50%      -0.116401     0.101143     0.002073    -0.013611
#[Out]# 75%       0.616366     0.780282     0.680391     0.654328
#[Out]# max       3.366626     2.653656     3.260383     3.927528
#[Out]# 
#[Out]# [8 rows x 4 columns]
# Fri, 04 Jul 2014 12:10:40
col = data[3]
# Fri, 04 Jul 2014 12:10:48
col.describe()
#[Out]# count    1000.000000
#[Out]# mean       -0.002298
#[Out]# std         0.996794
#[Out]# min        -3.745356
#[Out]# 25%        -0.644144
#[Out]# 50%        -0.013611
#[Out]# 75%         0.654328
#[Out]# max         3.927528
#[Out]# Name: 3, dtype: float64
# Fri, 04 Jul 2014 12:11:37
col[np.abs(col)>3]
#[Out]# 97     3.927528
#[Out]# 305   -3.399312
#[Out]# 400   -3.745356
#[Out]# Name: 3, dtype: float64
# Fri, 04 Jul 2014 12:12:47
data[np.abs(data) > 3).any(1)]
# Fri, 04 Jul 2014 12:13:25
data[(np.abs(data) > 3).any(1)]
#[Out]#             0         1         2         3
#[Out]# 5   -0.539741  0.476985  3.248944 -1.021228
#[Out]# 97  -0.774363  0.552936  0.106061  3.927528
#[Out]# 102 -0.655054 -0.565230  3.176873  0.959533
#[Out]# 305 -2.315555  0.457246 -0.025907 -3.399312
#[Out]# 324  0.050188  1.951312  3.260383  0.963301
#[Out]# 400  0.146326  0.508391 -0.196713 -3.745356
#[Out]# 499 -0.293333 -0.242459 -3.056990  1.918403
#[Out]# 523 -3.428254 -0.296336 -0.439938 -0.867165
#[Out]# 586  0.275144  1.179227 -3.184377  1.369891
#[Out]# 808 -0.362528 -3.548824  1.553205 -2.186301
#[Out]# 900  3.366626 -2.372214  0.851010  1.332846
#[Out]# 
#[Out]# [11 rows x 4 columns]
# Fri, 04 Jul 2014 12:15:21
data[np.abs(data) > 3] = np.sign(data) * 3
# Fri, 04 Jul 2014 12:15:26
data.describe()
#[Out]#                  0            1            2            3
#[Out]# count  1000.000000  1000.000000  1000.000000  1000.000000
#[Out]# mean     -0.067623     0.068473     0.025153    -0.002081
#[Out]# std       0.995485     0.990253     1.003977     0.989736
#[Out]# min      -3.000000    -3.000000    -3.000000    -3.000000
#[Out]# 25%      -0.774890    -0.591841    -0.641675    -0.644144
#[Out]# 50%      -0.116401     0.101143     0.002073    -0.013611
#[Out]# 75%       0.616366     0.780282     0.680391     0.654328
#[Out]# max       3.000000     2.653656     3.000000     3.000000
#[Out]# 
#[Out]# [8 rows x 4 columns]
# Fri, 04 Jul 2014 12:15:30
np.sign?
# Fri, 04 Jul 2014 13:15:36
df = DataFrame(np.arange(5*4).reshape((5, 4))
)
# Fri, 04 Jul 2014 13:15:37
df
#[Out]#     0   1   2   3
#[Out]# 0   0   1   2   3
#[Out]# 1   4   5   6   7
#[Out]# 2   8   9  10  11
#[Out]# 3  12  13  14  15
#[Out]# 4  16  17  18  19
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Fri, 04 Jul 2014 13:15:59
df = DataFrame(np.arange(5*4).reshape(5,4))
# Fri, 04 Jul 2014 13:16:00
df
#[Out]#     0   1   2   3
#[Out]# 0   0   1   2   3
#[Out]# 1   4   5   6   7
#[Out]# 2   8   9  10  11
#[Out]# 3  12  13  14  15
#[Out]# 4  16  17  18  19
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Fri, 04 Jul 2014 13:16:35
sampler = np.random.permutation(5)
# Fri, 04 Jul 2014 13:16:57
sampler
#[Out]# array([1, 0, 2, 3, 4])
# Fri, 04 Jul 2014 13:17:26
df.take(sampler)
#[Out]#     0   1   2   3
#[Out]# 1   4   5   6   7
#[Out]# 0   0   1   2   3
#[Out]# 2   8   9  10  11
#[Out]# 3  12  13  14  15
#[Out]# 4  16  17  18  19
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Fri, 04 Jul 2014 13:17:31
df.take?
# Fri, 04 Jul 2014 13:18:00
np.ndarray.take?
# Fri, 04 Jul 2014 13:18:43
numpy.take?
# Fri, 04 Jul 2014 13:18:51
np.take?
# Fri, 04 Jul 2014 13:22:37
df.take(np.random.permutation(len(df))[:3])
#[Out]#     0   1   2   3
#[Out]# 1   4   5   6   7
#[Out]# 3  12  13  14  15
#[Out]# 4  16  17  18  19
#[Out]# 
#[Out]# [3 rows x 4 columns]
# Fri, 04 Jul 2014 13:22:51
sampler
#[Out]# array([1, 0, 2, 3, 4])
# Fri, 04 Jul 2014 13:23:26
np.random.permutation(len(df))
#[Out]# array([1, 3, 0, 2, 4])
# Fri, 04 Jul 2014 13:23:44
np.random.permutation(len(df))
#[Out]# array([1, 0, 4, 3, 2])
# Fri, 04 Jul 2014 13:23:56
np.random.permutation(len(df))
#[Out]# array([1, 4, 0, 2, 3])
# Fri, 04 Jul 2014 13:24:00
np.random.permutation(len(df))
#[Out]# array([0, 3, 2, 4, 1])
# Fri, 04 Jul 2014 13:24:46
bag = np.array([5,7,-1,6,4])
# Fri, 04 Jul 2014 13:25:09
sampler = np.random.randint(0, len(bag), size=10)
# Fri, 04 Jul 2014 13:25:11
sampler
#[Out]# array([3, 0, 1, 2, 2, 3, 2, 1, 2, 0])
# Fri, 04 Jul 2014 13:25:31
draws = bag.take(sampler)
# Fri, 04 Jul 2014 13:25:34
draws
#[Out]# array([ 6,  5,  7, -1, -1,  6, -1,  7, -1,  5])
# Fri, 04 Jul 2014 13:28:05
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
'data1': range(6)})
# Fri, 04 Jul 2014 13:28:23
pd.get_dummies(df['key'])
#[Out]#    a  b  c
#[Out]# 0  0  1  0
#[Out]# 1  0  1  0
#[Out]# 2  1  0  0
#[Out]# 3  0  0  1
#[Out]# 4  1  0  0
#[Out]# 5  0  1  0
#[Out]# 
#[Out]# [6 rows x 3 columns]
# Fri, 04 Jul 2014 13:29:04
dummies = pd.get_dummies(df['key'], prefix='key')
# Fri, 04 Jul 2014 13:29:30
df_with_dummy = df[['data1']].join(dummies)
# Fri, 04 Jul 2014 13:29:35
df_with_dummy
#[Out]#    data1  key_a  key_b  key_c
#[Out]# 0      0      0      1      0
#[Out]# 1      1      0      1      0
#[Out]# 2      2      1      0      0
#[Out]# 3      3      0      0      1
#[Out]# 4      4      1      0      0
#[Out]# 5      5      0      1      0
#[Out]# 
#[Out]# [6 rows x 4 columns]
# Fri, 04 Jul 2014 13:30:17
df['data1']
#[Out]# 0    0
#[Out]# 1    1
#[Out]# 2    2
#[Out]# 3    3
#[Out]# 4    4
#[Out]# 5    5
#[Out]# Name: data1, dtype: int64
# Fri, 04 Jul 2014 13:30:25
df[['data1']]
#[Out]#    data1
#[Out]# 0      0
#[Out]# 1      1
#[Out]# 2      2
#[Out]# 3      3
#[Out]# 4      4
#[Out]# 5      5
#[Out]# 
#[Out]# [6 rows x 1 columns]
# Fri, 04 Jul 2014 13:32:45
mnames = ['movie_id', 'title', 'genres']
# Fri, 04 Jul 2014 13:33:38
movies = pd.read_table('../ch02/movielens/movies.dat', sep='::', header=None, names=mnames)
# Fri, 04 Jul 2014 13:33:47
movies[:10]
#[Out]#    movie_id                               title                        genres
#[Out]# 0         1                    Toy Story (1995)   Animation|Children's|Comedy
#[Out]# 1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
#[Out]# 2         3             Grumpier Old Men (1995)                Comedy|Romance
#[Out]# 3         4            Waiting to Exhale (1995)                  Comedy|Drama
#[Out]# 4         5  Father of the Bride Part II (1995)                        Comedy
#[Out]# 5         6                         Heat (1995)         Action|Crime|Thriller
#[Out]# 6         7                      Sabrina (1995)                Comedy|Romance
#[Out]# 7         8                 Tom and Huck (1995)          Adventure|Children's
#[Out]# 8         9                 Sudden Death (1995)                        Action
#[Out]# 9        10                    GoldenEye (1995)     Action|Adventure|Thriller
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Fri, 04 Jul 2014 13:35:12
genre_iter = (set(x.split('|')) for x in movies.genres)
# Fri, 04 Jul 2014 13:35:38
genres = sorted(set.union(*genre_iter))
# Fri, 04 Jul 2014 13:35:44
genre_iter
#[Out]# <generator object <genexpr> at 0x000000000A483D38>
# Fri, 04 Jul 2014 13:36:06
genre_iter[:10]
# Fri, 04 Jul 2014 13:36:43
print (*genre_iter)
# Fri, 04 Jul 2014 13:36:56
print *genre_iter
# Fri, 04 Jul 2014 13:37:12
a, b = *genre_iter
# Fri, 04 Jul 2014 13:37:20
a, b = genre_iter
# Fri, 04 Jul 2014 13:37:37
set?
# Fri, 04 Jul 2014 13:38:00
set.union?
# Fri, 04 Jul 2014 13:39:18
genres
#[Out]# ['Action',
#[Out]#  'Adventure',
#[Out]#  'Animation',
#[Out]#  "Children's",
#[Out]#  'Comedy',
#[Out]#  'Crime',
#[Out]#  'Documentary',
#[Out]#  'Drama',
#[Out]#  'Fantasy',
#[Out]#  'Film-Noir',
#[Out]#  'Horror',
#[Out]#  'Musical',
#[Out]#  'Mystery',
#[Out]#  'Romance',
#[Out]#  'Sci-Fi',
#[Out]#  'Thriller',
#[Out]#  'War',
#[Out]#  'Western']
# Fri, 04 Jul 2014 13:40:17
a, b, c = genre_iter[0]
# Fri, 04 Jul 2014 13:42:26
dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)
# Fri, 04 Jul 2014 13:42:32
dummies
#[Out]#     Action  Adventure  Animation  Children's  Comedy  Crime  Documentary  \
#[Out]# 0        0          0          0           0       0      0            0   
#[Out]# 1        0          0          0           0       0      0            0   
#[Out]# 2        0          0          0           0       0      0            0   
#[Out]# 3        0          0          0           0       0      0            0   
#[Out]# 4        0          0          0           0       0      0            0   
#[Out]# 5        0          0          0           0       0      0            0   
#[Out]# 6        0          0          0           0       0      0            0   
#[Out]# 7        0          0          0           0       0      0            0   
#[Out]# 8        0          0          0           0       0      0            0   
#[Out]# 9        0          0          0           0       0      0            0   
#[Out]# 10       0          0          0           0       0      0            0   
#[Out]# 11       0          0          0           0       0      0            0   
#[Out]# 12       0          0          0           0       0      0            0   
#[Out]# 13       0          0          0           0       0      0            0   
#[Out]# 14       0          0          0           0       0      0            0   
#[Out]# 15       0          0          0           0       0      0            0   
#[Out]# 16       0          0          0           0       0      0            0   
#[Out]# 17       0          0          0           0       0      0            0   
#[Out]# 18       0          0          0           0       0      0            0   
#[Out]# 19       0          0          0           0       0      0            0   
#[Out]# 20       0          0          0           0       0      0            0   
#[Out]# 21       0          0          0           0       0      0            0   
#[Out]# 22       0          0          0           0       0      0            0   
#[Out]# 23       0          0          0           0       0      0            0   
#[Out]# 24       0          0          0           0       0      0            0   
#[Out]# 25       0          0          0           0       0      0            0   
#[Out]# 26       0          0          0           0       0      0            0   
#[Out]# 27       0          0          0           0       0      0            0   
#[Out]# 28       0          0          0           0       0      0            0   
#[Out]# 29       0          0          0           0       0      0            0   
#[Out]# 30       0          0          0           0       0      0            0   
#[Out]# 31       0          0          0           0       0      0            0   
#[Out]# 32       0          0          0           0       0      0            0   
#[Out]# 33       0          0          0           0       0      0            0   
#[Out]# 34       0          0          0           0       0      0            0   
#[Out]# 35       0          0          0           0       0      0            0   
#[Out]# 36       0          0          0           0       0      0            0   
#[Out]# 37       0          0          0           0       0      0            0   
#[Out]# 38       0          0          0           0       0      0            0   
#[Out]# 39       0          0          0           0       0      0            0   
#[Out]# 40       0          0          0           0       0      0            0   
#[Out]# 41       0          0          0           0       0      0            0   
#[Out]# 42       0          0          0           0       0      0            0   
#[Out]# 43       0          0          0           0       0      0            0   
#[Out]# 44       0          0          0           0       0      0            0   
#[Out]# 45       0          0          0           0       0      0            0   
#[Out]# 46       0          0          0           0       0      0            0   
#[Out]# 47       0          0          0           0       0      0            0   
#[Out]# 48       0          0          0           0       0      0            0   
#[Out]# 49       0          0          0           0       0      0            0   
#[Out]# 50       0          0          0           0       0      0            0   
#[Out]# 51       0          0          0           0       0      0            0   
#[Out]# 52       0          0          0           0       0      0            0   
#[Out]# 53       0          0          0           0       0      0            0   
#[Out]# 54       0          0          0           0       0      0            0   
#[Out]# 55       0          0          0           0       0      0            0   
#[Out]# 56       0          0          0           0       0      0            0   
#[Out]# 57       0          0          0           0       0      0            0   
#[Out]# 58       0          0          0           0       0      0            0   
#[Out]# 59       0          0          0           0       0      0            0   
#[Out]#        ...        ...        ...         ...     ...    ...          ...   
#[Out]# 
#[Out]#     Drama  Fantasy  Film-Noir  Horror  Musical  Mystery  Romance  Sci-Fi  \
#[Out]# 0       0        0          0       0        0        0        0       0   
#[Out]# 1       0        0          0       0        0        0        0       0   
#[Out]# 2       0        0          0       0        0        0        0       0   
#[Out]# 3       0        0          0       0        0        0        0       0   
#[Out]# 4       0        0          0       0        0        0        0       0   
#[Out]# 5       0        0          0       0        0        0        0       0   
#[Out]# 6       0        0          0       0        0        0        0       0   
#[Out]# 7       0        0          0       0        0        0        0       0   
#[Out]# 8       0        0          0       0        0        0        0       0   
#[Out]# 9       0        0          0       0        0        0        0       0   
#[Out]# 10      0        0          0       0        0        0        0       0   
#[Out]# 11      0        0          0       0        0        0        0       0   
#[Out]# 12      0        0          0       0        0        0        0       0   
#[Out]# 13      0        0          0       0        0        0        0       0   
#[Out]# 14      0        0          0       0        0        0        0       0   
#[Out]# 15      0        0          0       0        0        0        0       0   
#[Out]# 16      0        0          0       0        0        0        0       0   
#[Out]# 17      0        0          0       0        0        0        0       0   
#[Out]# 18      0        0          0       0        0        0        0       0   
#[Out]# 19      0        0          0       0        0        0        0       0   
#[Out]# 20      0        0          0       0        0        0        0       0   
#[Out]# 21      0        0          0       0        0        0        0       0   
#[Out]# 22      0        0          0       0        0        0        0       0   
#[Out]# 23      0        0          0       0        0        0        0       0   
#[Out]# 24      0        0          0       0        0        0        0       0   
#[Out]# 25      0        0          0       0        0        0        0       0   
#[Out]# 26      0        0          0       0        0        0        0       0   
#[Out]# 27      0        0          0       0        0        0        0       0   
#[Out]# 28      0        0          0       0        0        0        0       0   
#[Out]# 29      0        0          0       0        0        0        0       0   
#[Out]# 30      0        0          0       0        0        0        0       0   
#[Out]# 31      0        0          0       0        0        0        0       0   
#[Out]# 32      0        0          0       0        0        0        0       0   
#[Out]# 33      0        0          0       0        0        0        0       0   
#[Out]# 34      0        0          0       0        0        0        0       0   
#[Out]# 35      0        0          0       0        0        0        0       0   
#[Out]# 36      0        0          0       0        0        0        0       0   
#[Out]# 37      0        0          0       0        0        0        0       0   
#[Out]# 38      0        0          0       0        0        0        0       0   
#[Out]# 39      0        0          0       0        0        0        0       0   
#[Out]# 40      0        0          0       0        0        0        0       0   
#[Out]# 41      0        0          0       0        0        0        0       0   
#[Out]# 42      0        0          0       0        0        0        0       0   
#[Out]# 43      0        0          0       0        0        0        0       0   
#[Out]# 44      0        0          0       0        0        0        0       0   
#[Out]# 45      0        0          0       0        0        0        0       0   
#[Out]# 46      0        0          0       0        0        0        0       0   
#[Out]# 47      0        0          0       0        0        0        0       0   
#[Out]# 48      0        0          0       0        0        0        0       0   
#[Out]# 49      0        0          0       0        0        0        0       0   
#[Out]# 50      0        0          0       0        0        0        0       0   
#[Out]# 51      0        0          0       0        0        0        0       0   
#[Out]# 52      0        0          0       0        0        0        0       0   
#[Out]# 53      0        0          0       0        0        0        0       0   
#[Out]# 54      0        0          0       0        0        0        0       0   
#[Out]# 55      0        0          0       0        0        0        0       0   
#[Out]# 56      0        0          0       0        0        0        0       0   
#[Out]# 57      0        0          0       0        0        0        0       0   
#[Out]# 58      0        0          0       0        0        0        0       0   
#[Out]# 59      0        0          0       0        0        0        0       0   
#[Out]#       ...      ...        ...     ...      ...      ...      ...     ...   
#[Out]# 
#[Out]#     Thriller  War  Western  
#[Out]# 0          0    0        0  
#[Out]# 1          0    0        0  
#[Out]# 2          0    0        0  
#[Out]# 3          0    0        0  
#[Out]# 4          0    0        0  
#[Out]# 5          0    0        0  
#[Out]# 6          0    0        0  
#[Out]# 7          0    0        0  
#[Out]# 8          0    0        0  
#[Out]# 9          0    0        0  
#[Out]# 10         0    0        0  
#[Out]# 11         0    0        0  
#[Out]# 12         0    0        0  
#[Out]# 13         0    0        0  
#[Out]# 14         0    0        0  
#[Out]# 15         0    0        0  
#[Out]# 16         0    0        0  
#[Out]# 17         0    0        0  
#[Out]# 18         0    0        0  
#[Out]# 19         0    0        0  
#[Out]# 20         0    0        0  
#[Out]# 21         0    0        0  
#[Out]# 22         0    0        0  
#[Out]# 23         0    0        0  
#[Out]# 24         0    0        0  
#[Out]# 25         0    0        0  
#[Out]# 26         0    0        0  
#[Out]# 27         0    0        0  
#[Out]# 28         0    0        0  
#[Out]# 29         0    0        0  
#[Out]# 30         0    0        0  
#[Out]# 31         0    0        0  
#[Out]# 32         0    0        0  
#[Out]# 33         0    0        0  
#[Out]# 34         0    0        0  
#[Out]# 35         0    0        0  
#[Out]# 36         0    0        0  
#[Out]# 37         0    0        0  
#[Out]# 38         0    0        0  
#[Out]# 39         0    0        0  
#[Out]# 40         0    0        0  
#[Out]# 41         0    0        0  
#[Out]# 42         0    0        0  
#[Out]# 43         0    0        0  
#[Out]# 44         0    0        0  
#[Out]# 45         0    0        0  
#[Out]# 46         0    0        0  
#[Out]# 47         0    0        0  
#[Out]# 48         0    0        0  
#[Out]# 49         0    0        0  
#[Out]# 50         0    0        0  
#[Out]# 51         0    0        0  
#[Out]# 52         0    0        0  
#[Out]# 53         0    0        0  
#[Out]# 54         0    0        0  
#[Out]# 55         0    0        0  
#[Out]# 56         0    0        0  
#[Out]# 57         0    0        0  
#[Out]# 58         0    0        0  
#[Out]# 59         0    0        0  
#[Out]#          ...  ...      ...  
#[Out]# 
#[Out]# [3883 rows x 18 columns]
# Fri, 04 Jul 2014 13:43:56
for i, gen in enumerate(movies.genres):
    dummies.ix[i, gen.split('|')] = 1
    
# Fri, 04 Jul 2014 13:44:35
movies_windic = movies.join(dummies.add_prefix('Genre_'))
# Fri, 04 Jul 2014 13:44:48
movies_windic.ix[0]
#[Out]# movie_id                                       1
#[Out]# title                           Toy Story (1995)
#[Out]# genres               Animation|Children's|Comedy
#[Out]# Genre_Action                                   0
#[Out]# Genre_Adventure                                0
#[Out]# Genre_Animation                                1
#[Out]# Genre_Children's                               1
#[Out]# Genre_Comedy                                   1
#[Out]# Genre_Crime                                    0
#[Out]# Genre_Documentary                              0
#[Out]# Genre_Drama                                    0
#[Out]# Genre_Fantasy                                  0
#[Out]# Genre_Film-Noir                                0
#[Out]# Genre_Horror                                   0
#[Out]# Genre_Musical                                  0
#[Out]# Genre_Mystery                                  0
#[Out]# Genre_Romance                                  0
#[Out]# Genre_Sci-Fi                                   0
#[Out]# Genre_Thriller                                 0
#[Out]# Genre_War                                      0
#[Out]# Genre_Western                                  0
#[Out]# Name: 0, dtype: object
# Fri, 04 Jul 2014 13:49:51
values = np.random.rand(10)
# Fri, 04 Jul 2014 13:49:55
values
#[Out]# array([ 0.90953758,  0.38441329,  0.08127486,  0.95663486,  0.04387138,
#[Out]#         0.14476865,  0.11766477,  0.13018305,  0.62275769,  0.08497892])
# Fri, 04 Jul 2014 13:50:16
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
# Fri, 04 Jul 2014 13:50:30
pd.get_dummies(pd.cut(values, bins))
#[Out]#    (0, 0.2]  (0.2, 0.4]  (0.6, 0.8]  (0.8, 1]
#[Out]# 0         0           0           0         1
#[Out]# 1         0           1           0         0
#[Out]# 2         1           0           0         0
#[Out]# 3         0           0           0         1
#[Out]# 4         1           0           0         0
#[Out]# 5         1           0           0         0
#[Out]# 6         1           0           0         0
#[Out]# 7         1           0           0         0
#[Out]# 8         0           0           1         0
#[Out]# 9         1           0           0         0
#[Out]# 
#[Out]# [10 rows x 4 columns]
# Fri, 04 Jul 2014 13:52:10
val = 'a,b,  guido'
# Fri, 04 Jul 2014 13:52:18
val.split(',')
#[Out]# ['a', 'b', '  guido']
# Fri, 04 Jul 2014 13:52:54
pieces = [x.strip() for x in val.split(',')]
# Fri, 04 Jul 2014 13:52:56
pieces
#[Out]# ['a', 'b', 'guido']
# Fri, 04 Jul 2014 13:53:23
first, second, third = pieces
# Fri, 04 Jul 2014 13:53:45
first + '::' + second + '::' + third
#[Out]# 'a::b::guido'
# Fri, 04 Jul 2014 13:54:12
'::'.join(pieces)
#[Out]# 'a::b::guido'
# Fri, 04 Jul 2014 13:54:29
'guido' in val
#[Out]# True
# Fri, 04 Jul 2014 13:54:37
val.index(',')
#[Out]# 1
# Fri, 04 Jul 2014 13:54:50
val.find(':')
#[Out]# -1
# Fri, 04 Jul 2014 13:55:08
val.index(':')
# Fri, 04 Jul 2014 13:55:34
val.count(',')
#[Out]# 2
# Fri, 04 Jul 2014 13:55:57
val.replace(',', '::')
#[Out]# 'a::b::  guido'
# Fri, 04 Jul 2014 13:56:11
val.replace(',', '')
#[Out]# 'ab  guido'
# Fri, 04 Jul 2014 14:00:35
import re
# Fri, 04 Jul 2014 14:00:57
text = "foo    bar\t baz  \tqux"
# Fri, 04 Jul 2014 14:01:12
re.split('\s+', text)
#[Out]# ['foo', 'bar', 'baz', 'qux']
# Fri, 04 Jul 2014 14:02:08
regex = re.compile('\s+')
# Fri, 04 Jul 2014 14:02:19
regex.split(text)
#[Out]# ['foo', 'bar', 'baz', 'qux']
# Fri, 04 Jul 2014 14:03:09
regex.findall(text)
#[Out]# ['    ', '\t ', '  \t']
# Fri, 04 Jul 2014 14:05:33
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
# Fri, 04 Jul 2014 14:07:15
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
# Fri, 04 Jul 2014 14:07:35
regex = re.compile(pattern, flags=re.IGNORECASE)
# Fri, 04 Jul 2014 14:07:58
regex.findall(text)
#[Out]# ['dave@google.com', 'steve@gmail.com', 'rob@gmail.com', 'ryan@yahoo.com']
# Fri, 04 Jul 2014 14:08:20
regex.search(text)
#[Out]# <_sre.SRE_Match at 0xa4e94a8>
# Fri, 04 Jul 2014 14:08:59
m = regex.search(text)
# Fri, 04 Jul 2014 14:09:01
m
#[Out]# <_sre.SRE_Match at 0xa4e9648>
# Fri, 04 Jul 2014 14:09:20
text[m.start():m.end()]
#[Out]# 'dave@google.com'
# Fri, 04 Jul 2014 14:09:38
print regex.match(text)
# Fri, 04 Jul 2014 14:10:04
print regex.sub('REDACTED', text)
# Fri, 04 Jul 2014 14:11:20
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
# Fri, 04 Jul 2014 14:11:54
regex = re.compile(pattern, flags=re.IGNORECASE)
# Fri, 04 Jul 2014 14:12:19
m = regex.match('wesm@bright.net')
# Fri, 04 Jul 2014 14:12:26
m.groups()
#[Out]# ('wesm', 'bright', 'net')
# Fri, 04 Jul 2014 14:12:46
regex.findall(text)
#[Out]# [('dave', 'google', 'com'),
#[Out]#  ('steve', 'gmail', 'com'),
#[Out]#  ('rob', 'gmail', 'com'),
#[Out]#  ('ryan', 'yahoo', 'com')]
# Fri, 04 Jul 2014 14:14:04
print regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text)
# Fri, 04 Jul 2014 14:15:34
regex = re.compile(r"""
"""

)
# Fri, 04 Jul 2014 14:17:08
regex = re.compile(r"""([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(r"""(?P<username>[A-Z0-9._%+-]+)
# Fri, 04 Jul 2014 14:19:53
regex = re.compile(r"""
(?P<username>[A-Z0-9._%+-]+)
@
(?P<domain>[A-Z0-9.-]+)
\.
(?P<suffix>[A-Z]{2,4})
""", flags=re.IGNORECASE|re.VERBOSE)
# Fri, 04 Jul 2014 14:20:25
m = regex.match(text)
# Fri, 04 Jul 2014 14:20:33
m.groupdict()
# Fri, 04 Jul 2014 14:20:45
m = regex.match('wesm@bright.net')
# Fri, 04 Jul 2014 14:20:49
m.groupdict()
#[Out]# {'domain': 'bright', 'suffix': 'net', 'username': 'wesm'}
# Fri, 04 Jul 2014 14:23:01
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
'Rob': 'rob@gmail.com', 'Wes': np.nan}
# Fri, 04 Jul 2014 14:23:08
data = Series(data)
# Fri, 04 Jul 2014 14:23:10
data
#[Out]# Dave     dave@google.com
#[Out]# Rob        rob@gmail.com
#[Out]# Steve    steve@gmail.com
#[Out]# Wes                  NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:23:20
data.isnull()
#[Out]# Dave     False
#[Out]# Rob      False
#[Out]# Steve    False
#[Out]# Wes       True
#[Out]# dtype: bool
# Fri, 04 Jul 2014 14:24:17
data.str.contains('gmail')
#[Out]# Dave     False
#[Out]# Rob       True
#[Out]# Steve     True
#[Out]# Wes        NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:24:35
pattern
#[Out]# '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
# Fri, 04 Jul 2014 14:25:10
data.str.findall(pattern, flags=re.IGNORECASE)
#[Out]# Dave     [(dave, google, com)]
#[Out]# Rob        [(rob, gmail, com)]
#[Out]# Steve    [(steve, gmail, com)]
#[Out]# Wes                        NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:26:20
matches = data.str.match(pattern, flags=re.IGNORECASE)
# Fri, 04 Jul 2014 14:26:58
matches
#[Out]# Dave     (dave, google, com)
#[Out]# Rob        (rob, gmail, com)
#[Out]# Steve    (steve, gmail, com)
#[Out]# Wes                      NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:27:39
matches.str.get(1)
#[Out]# Dave     google
#[Out]# Rob       gmail
#[Out]# Steve     gmail
#[Out]# Wes         NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:27:55
matches.str[0]
#[Out]# Dave      dave
#[Out]# Rob        rob
#[Out]# Steve    steve
#[Out]# Wes        NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:28:14
data.str[:5]
#[Out]# Dave     dave@
#[Out]# Rob      rob@g
#[Out]# Steve    steve
#[Out]# Wes        NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:28:44
data
#[Out]# Dave     dave@google.com
#[Out]# Rob        rob@gmail.com
#[Out]# Steve    steve@gmail.com
#[Out]# Wes                  NaN
#[Out]# dtype: object
# Fri, 04 Jul 2014 14:36:12
import json
# Fri, 04 Jul 2014 14:36:39
db = json.load(open('foods-2011-10-03.json'))
# Fri, 04 Jul 2014 14:36:48
len(db)
#[Out]# 6636
# Fri, 04 Jul 2014 14:37:03
db[0].keys()
#[Out]# [u'portions',
#[Out]#  u'description',
#[Out]#  u'tags',
#[Out]#  u'nutrients',
#[Out]#  u'group',
#[Out]#  u'id',
#[Out]#  u'manufacturer']
# Fri, 04 Jul 2014 14:38:04
db[0][3][0]
# Fri, 04 Jul 2014 14:38:35
db[0]
#[Out]# {u'description': u'Cheese, caraway',
#[Out]#  u'group': u'Dairy and Egg Products',
#[Out]#  u'id': 1008,
#[Out]#  u'manufacturer': u'',
#[Out]#  u'nutrients': [{u'description': u'Protein',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 25.18},
#[Out]#   {u'description': u'Total lipid (fat)',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 29.2},
#[Out]#   {u'description': u'Carbohydrate, by difference',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 3.06},
#[Out]#   {u'description': u'Ash', u'group': u'Other', u'units': u'g', u'value': 3.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kcal',
#[Out]#    u'value': 376.0},
#[Out]#   {u'description': u'Water',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 39.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kJ',
#[Out]#    u'value': 1573.0},
#[Out]#   {u'description': u'Fiber, total dietary',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Calcium, Ca',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 673.0},
#[Out]#   {u'description': u'Iron, Fe',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.64},
#[Out]#   {u'description': u'Magnesium, Mg',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 22.0},
#[Out]#   {u'description': u'Phosphorus, P',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 490.0},
#[Out]#   {u'description': u'Potassium, K',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Sodium, Na',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 690.0},
#[Out]#   {u'description': u'Zinc, Zn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 2.94},
#[Out]#   {u'description': u'Copper, Cu',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.024},
#[Out]#   {u'description': u'Manganese, Mn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.021},
#[Out]#   {u'description': u'Selenium, Se',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 14.5},
#[Out]#   {u'description': u'Vitamin A, IU',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'IU',
#[Out]#    u'value': 1054.0},
#[Out]#   {u'description': u'Retinol',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 262.0},
#[Out]#   {u'description': u'Vitamin A, RAE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_RAE',
#[Out]#    u'value': 271.0},
#[Out]#   {u'description': u'Vitamin C, total ascorbic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Thiamin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.031},
#[Out]#   {u'description': u'Riboflavin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.45},
#[Out]#   {u'description': u'Niacin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.18},
#[Out]#   {u'description': u'Pantothenic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.19},
#[Out]#   {u'description': u'Vitamin B-6',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.074},
#[Out]#   {u'description': u'Folate, total',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Vitamin B-12',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.27},
#[Out]#   {u'description': u'Folic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Folate, food',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Folate, DFE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_DFE',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Cholesterol',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Fatty acids, total saturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 18.584},
#[Out]#   {u'description': u'Fatty acids, total monounsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 8.275},
#[Out]#   {u'description': u'Fatty acids, total polyunsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.83},
#[Out]#   {u'description': u'Tryptophan',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.324},
#[Out]#   {u'description': u'Threonine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.896},
#[Out]#   {u'description': u'Isoleucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.563},
#[Out]#   {u'description': u'Leucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.412},
#[Out]#   {u'description': u'Lysine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.095},
#[Out]#   {u'description': u'Methionine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.659},
#[Out]#   {u'description': u'Cystine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.126},
#[Out]#   {u'description': u'Phenylalanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.326},
#[Out]#   {u'description': u'Tyrosine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.216},
#[Out]#   {u'description': u'Valine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.682},
#[Out]#   {u'description': u'Arginine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.952},
#[Out]#   {u'description': u'Histidine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.884},
#[Out]#   {u'description': u'Alanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.711},
#[Out]#   {u'description': u'Aspartic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.618},
#[Out]#   {u'description': u'Glutamic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 6.16},
#[Out]#   {u'description': u'Glycine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.439},
#[Out]#   {u'description': u'Proline',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.838},
#[Out]#   {u'description': u'Serine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.472},
#[Out]#   {u'description': u'Protein',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 25.18},
#[Out]#   {u'description': u'Total lipid (fat)',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 29.2},
#[Out]#   {u'description': u'Carbohydrate, by difference',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 3.06},
#[Out]#   {u'description': u'Ash', u'group': u'Other', u'units': u'g', u'value': 3.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kcal',
#[Out]#    u'value': 376.0},
#[Out]#   {u'description': u'Water',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 39.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kJ',
#[Out]#    u'value': 1573.0},
#[Out]#   {u'description': u'Fiber, total dietary',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Calcium, Ca',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 673.0},
#[Out]#   {u'description': u'Iron, Fe',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.64},
#[Out]#   {u'description': u'Magnesium, Mg',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 22.0},
#[Out]#   {u'description': u'Phosphorus, P',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 490.0},
#[Out]#   {u'description': u'Potassium, K',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Sodium, Na',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 690.0},
#[Out]#   {u'description': u'Zinc, Zn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 2.94},
#[Out]#   {u'description': u'Copper, Cu',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.024},
#[Out]#   {u'description': u'Manganese, Mn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.021},
#[Out]#   {u'description': u'Selenium, Se',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 14.5},
#[Out]#   {u'description': u'Vitamin A, IU',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'IU',
#[Out]#    u'value': 1054.0},
#[Out]#   {u'description': u'Retinol',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 262.0},
#[Out]#   {u'description': u'Vitamin A, RAE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_RAE',
#[Out]#    u'value': 271.0},
#[Out]#   {u'description': u'Vitamin C, total ascorbic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Thiamin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.031},
#[Out]#   {u'description': u'Riboflavin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.45},
#[Out]#   {u'description': u'Niacin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.18},
#[Out]#   {u'description': u'Pantothenic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.19},
#[Out]#   {u'description': u'Vitamin B-6',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.074},
#[Out]#   {u'description': u'Folate, total',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Vitamin B-12',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.27},
#[Out]#   {u'description': u'Folic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Folate, food',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Folate, DFE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_DFE',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Tryptophan',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.324},
#[Out]#   {u'description': u'Threonine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.896},
#[Out]#   {u'description': u'Isoleucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.563},
#[Out]#   {u'description': u'Leucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.412},
#[Out]#   {u'description': u'Lysine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.095},
#[Out]#   {u'description': u'Methionine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.659},
#[Out]#   {u'description': u'Cystine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.126},
#[Out]#   {u'description': u'Phenylalanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.326},
#[Out]#   {u'description': u'Tyrosine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.216},
#[Out]#   {u'description': u'Valine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.682},
#[Out]#   {u'description': u'Arginine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.952},
#[Out]#   {u'description': u'Histidine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.884},
#[Out]#   {u'description': u'Alanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.711},
#[Out]#   {u'description': u'Aspartic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.618},
#[Out]#   {u'description': u'Glutamic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 6.16},
#[Out]#   {u'description': u'Glycine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.439},
#[Out]#   {u'description': u'Proline',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.838},
#[Out]#   {u'description': u'Serine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.472},
#[Out]#   {u'description': u'Cholesterol',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Fatty acids, total saturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 18.584},
#[Out]#   {u'description': u'Fatty acids, total monounsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 8.275},
#[Out]#   {u'description': u'Fatty acids, total polyunsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.83},
#[Out]#   {u'description': u'Protein',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 25.18},
#[Out]#   {u'description': u'Total lipid (fat)',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 29.2},
#[Out]#   {u'description': u'Carbohydrate, by difference',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 3.06},
#[Out]#   {u'description': u'Ash', u'group': u'Other', u'units': u'g', u'value': 3.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kcal',
#[Out]#    u'value': 376.0},
#[Out]#   {u'description': u'Water',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 39.28},
#[Out]#   {u'description': u'Energy',
#[Out]#    u'group': u'Energy',
#[Out]#    u'units': u'kJ',
#[Out]#    u'value': 1573.0},
#[Out]#   {u'description': u'Fiber, total dietary',
#[Out]#    u'group': u'Composition',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Calcium, Ca',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 673.0},
#[Out]#   {u'description': u'Iron, Fe',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.64},
#[Out]#   {u'description': u'Magnesium, Mg',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 22.0},
#[Out]#   {u'description': u'Phosphorus, P',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 490.0},
#[Out]#   {u'description': u'Potassium, K',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Sodium, Na',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 690.0},
#[Out]#   {u'description': u'Zinc, Zn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 2.94},
#[Out]#   {u'description': u'Copper, Cu',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.024},
#[Out]#   {u'description': u'Manganese, Mn',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.021},
#[Out]#   {u'description': u'Selenium, Se',
#[Out]#    u'group': u'Elements',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 14.5},
#[Out]#   {u'description': u'Vitamin A, IU',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'IU',
#[Out]#    u'value': 1054.0},
#[Out]#   {u'description': u'Retinol',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 262.0},
#[Out]#   {u'description': u'Vitamin A, RAE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_RAE',
#[Out]#    u'value': 271.0},
#[Out]#   {u'description': u'Vitamin C, total ascorbic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Thiamin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.031},
#[Out]#   {u'description': u'Riboflavin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.45},
#[Out]#   {u'description': u'Niacin',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.18},
#[Out]#   {u'description': u'Pantothenic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.19},
#[Out]#   {u'description': u'Vitamin B-6',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 0.074},
#[Out]#   {u'description': u'Folate, total',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Vitamin B-12',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.27},
#[Out]#   {u'description': u'Folic acid',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 0.0},
#[Out]#   {u'description': u'Folate, food',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Folate, DFE',
#[Out]#    u'group': u'Vitamins',
#[Out]#    u'units': u'mcg_DFE',
#[Out]#    u'value': 18.0},
#[Out]#   {u'description': u'Tryptophan',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.324},
#[Out]#   {u'description': u'Threonine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.896},
#[Out]#   {u'description': u'Isoleucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.563},
#[Out]#   {u'description': u'Leucine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.412},
#[Out]#   {u'description': u'Lysine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.095},
#[Out]#   {u'description': u'Methionine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.659},
#[Out]#   {u'description': u'Cystine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.126},
#[Out]#   {u'description': u'Phenylalanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.326},
#[Out]#   {u'description': u'Tyrosine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.216},
#[Out]#   {u'description': u'Valine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.682},
#[Out]#   {u'description': u'Arginine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.952},
#[Out]#   {u'description': u'Histidine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.884},
#[Out]#   {u'description': u'Alanine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.711},
#[Out]#   {u'description': u'Aspartic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.618},
#[Out]#   {u'description': u'Glutamic acid',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 6.16},
#[Out]#   {u'description': u'Glycine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.439},
#[Out]#   {u'description': u'Proline',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 2.838},
#[Out]#   {u'description': u'Serine',
#[Out]#    u'group': u'Amino Acids',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 1.472},
#[Out]#   {u'description': u'Cholesterol',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'mg',
#[Out]#    u'value': 93.0},
#[Out]#   {u'description': u'Fatty acids, total saturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 18.584},
#[Out]#   {u'description': u'Fatty acids, total monounsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 8.275},
#[Out]#   {u'description': u'Fatty acids, total polyunsaturated',
#[Out]#    u'group': u'Other',
#[Out]#    u'units': u'g',
#[Out]#    u'value': 0.83}],
#[Out]#  u'portions': [{u'amount': 1, u'grams': 28.35, u'unit': u'oz'}],
#[Out]#  u'tags': []}
# Fri, 04 Jul 2014 14:38:53
db[0]['nutrients'][0]
#[Out]# {u'description': u'Protein',
#[Out]#  u'group': u'Composition',
#[Out]#  u'units': u'g',
#[Out]#  u'value': 25.18}
# Fri, 04 Jul 2014 14:39:42
nutrients = DataFrame(db[0]['nutrients])
# Fri, 04 Jul 2014 14:39:51
nutrients = DataFrame(db[0]['nutrients'])
# Fri, 04 Jul 2014 14:39:59
nutrients[:7]
#[Out]#                    description        group units    value
#[Out]# 0                      Protein  Composition     g    25.18
#[Out]# 1            Total lipid (fat)  Composition     g    29.20
#[Out]# 2  Carbohydrate, by difference  Composition     g     3.06
#[Out]# 3                          Ash        Other     g     3.28
#[Out]# 4                       Energy       Energy  kcal   376.00
#[Out]# 5                        Water  Composition     g    39.28
#[Out]# 6                       Energy       Energy    kJ  1573.00
#[Out]# 
#[Out]# [7 rows x 4 columns]
# Fri, 04 Jul 2014 14:41:08
info_keys = ['description', 'group', 'id', 'manufacturer']
# Fri, 04 Jul 2014 14:41:22
info = DataFrame(db, columns=info_keys)
# Fri, 04 Jul 2014 14:41:28
info[:5]
#[Out]#                           description                   group    id  \
#[Out]# 0                     Cheese, caraway  Dairy and Egg Products  1008   
#[Out]# 1                     Cheese, cheddar  Dairy and Egg Products  1009   
#[Out]# 2                        Cheese, edam  Dairy and Egg Products  1018   
#[Out]# 3                        Cheese, feta  Dairy and Egg Products  1019   
#[Out]# 4  Cheese, mozzarella, part skim milk  Dairy and Egg Products  1028   
#[Out]# 
#[Out]#   manufacturer  
#[Out]# 0               
#[Out]# 1               
#[Out]# 2               
#[Out]# 3               
#[Out]# 4               
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Fri, 04 Jul 2014 14:42:03
info
#[Out]#                                           description                   group  \
#[Out]# 0                                     Cheese, caraway  Dairy and Egg Products   
#[Out]# 1                                     Cheese, cheddar  Dairy and Egg Products   
#[Out]# 2                                        Cheese, edam  Dairy and Egg Products   
#[Out]# 3                                        Cheese, feta  Dairy and Egg Products   
#[Out]# 4                  Cheese, mozzarella, part skim milk  Dairy and Egg Products   
#[Out]# 5    Cheese, mozzarella, part skim milk, low moisture  Dairy and Egg Products   
#[Out]# 6                                      Cheese, romano  Dairy and Egg Products   
#[Out]# 7                                   Cheese, roquefort  Dairy and Egg Products   
#[Out]# 8   Cheese spread, pasteurized process, american, ...  Dairy and Egg Products   
#[Out]# 9                         Cream, fluid, half and half  Dairy and Egg Products   
#[Out]# 10  Sour dressing, non-butterfat, cultured, filled...  Dairy and Egg Products   
#[Out]# 11  Milk, filled, fluid, with blend of hydrogenate...  Dairy and Egg Products   
#[Out]# 12  Cream substitute, liquid, with lauric acid oil...  Dairy and Egg Products   
#[Out]# 13                         Cream substitute, powdered  Dairy and Egg Products   
#[Out]# 14                Milk, producer, fluid, 3.7% milkfat  Dairy and Egg Products   
#[Out]# 15  Milk, reduced fat, fluid, 2% milkfat, with add...  Dairy and Egg Products   
#[Out]# 16  Milk, reduced fat, fluid, 2% milkfat, with add...  Dairy and Egg Products   
#[Out]# 17  Milk, reduced fat, fluid, 2% milkfat, protein ...  Dairy and Egg Products   
#[Out]# 18  Milk, lowfat, fluid, 1% milkfat, with added vi...  Dairy and Egg Products   
#[Out]# 19  Milk, lowfat, fluid, 1% milkfat, with added no...  Dairy and Egg Products   
#[Out]# 20  Milk, lowfat, fluid, 1% milkfat, protein forti...  Dairy and Egg Products   
#[Out]# 21  Milk, nonfat, fluid, with added vitamin A and ...  Dairy and Egg Products   
#[Out]# 22  Milk, nonfat, fluid, with added nonfat milk so...  Dairy and Egg Products   
#[Out]# 23  Milk, nonfat, fluid, protein fortified, with a...  Dairy and Egg Products   
#[Out]# 24          Milk, buttermilk, fluid, cultured, lowfat  Dairy and Egg Products   
#[Out]# 25                            Milk, low sodium, fluid  Dairy and Egg Products   
#[Out]# 26             Milk, dry, whole, with added vitamin D  Dairy and Egg Products   
#[Out]# 27  Milk, dry, nonfat, regular, without added vita...  Dairy and Egg Products   
#[Out]# 28  Milk, dry, nonfat, instant, with added vitamin...  Dairy and Egg Products   
#[Out]# 29                 Milk, dry, nonfat, calcium reduced  Dairy and Egg Products   
#[Out]# 30                            Milk, buttermilk, dried  Dairy and Egg Products   
#[Out]# 31                 Milk, canned, condensed, sweetened  Dairy and Egg Products   
#[Out]# 32  Milk, canned, evaporated, with added vitamin D...  Dairy and Egg Products   
#[Out]# 33  Milk, canned, evaporated, nonfat, with added v...  Dairy and Egg Products   
#[Out]# 34                        Milk, indian buffalo, fluid  Dairy and Egg Products   
#[Out]# 35                                 Milk, sheep, fluid  Dairy and Egg Products   
#[Out]# 36  Yogurt, plain, skim milk, 13 grams protein per...  Dairy and Egg Products   
#[Out]# 37  Yogurt, vanilla, low fat, 11 grams protein per...  Dairy and Egg Products   
#[Out]# 38                          Egg, whole, cooked, fried  Dairy and Egg Products   
#[Out]# 39                    Egg, whole, cooked, hard-boiled  Dairy and Egg Products   
#[Out]# 40                       Egg, duck, whole, fresh, raw  Dairy and Egg Products   
#[Out]# 41                      Egg, goose, whole, fresh, raw  Dairy and Egg Products   
#[Out]# 42  Cheese, pasteurized process, swiss, without di...  Dairy and Egg Products   
#[Out]# 43  Cheese food, pasteurized process, american, wi...  Dairy and Egg Products   
#[Out]# 44                            Cheese, goat, soft type  Dairy and Egg Products   
#[Out]# 45                  Cheese, low fat, cheddar or colby  Dairy and Egg Products   
#[Out]# 46               Cheese, low-sodium, cheddar or colby  Dairy and Egg Products   
#[Out]# 47                            Sour cream, reduced fat  Dairy and Egg Products   
#[Out]# 48                                  Sour cream, light  Dairy and Egg Products   
#[Out]# 49                               Sour cream, fat free  Dairy and Egg Products   
#[Out]# 50       USDA Commodity, cheese, cheddar, reduced fat  Dairy and Egg Products   
#[Out]# 51  Yogurt, vanilla or lemon flavor, nonfat milk, ...  Dairy and Egg Products   
#[Out]# 52                  Parmesan cheese topping, fat free  Dairy and Egg Products   
#[Out]# 53                            Cheese, cream, fat free  Dairy and Egg Products   
#[Out]# 54                     Yogurt, chocolate, nonfat milk  Dairy and Egg Products   
#[Out]# 55  KRAFT CHEEZ WHIZ Pasteurized Process Cheese Sauce  Dairy and Egg Products   
#[Out]# 56  KRAFT CHEEZ WHIZ LIGHT Pasteurized Process Che...  Dairy and Egg Products   
#[Out]# 57  KRAFT FREE Singles American Nonfat Pasteurized...  Dairy and Egg Products   
#[Out]# 58   KRAFT VELVEETA Pasteurized Process Cheese Spread  Dairy and Egg Products   
#[Out]# 59  KRAFT VELVEETA LIGHT Reduced Fat Pasteurized P...  Dairy and Egg Products   
#[Out]#                                                   ...                     ...   
#[Out]# 
#[Out]#       id manufacturer  
#[Out]# 0   1008               
#[Out]# 1   1009               
#[Out]# 2   1018               
#[Out]# 3   1019               
#[Out]# 4   1028               
#[Out]# 5   1029               
#[Out]# 6   1038               
#[Out]# 7   1039               
#[Out]# 8   1048               
#[Out]# 9   1049               
#[Out]# 10  1058               
#[Out]# 11  1059               
#[Out]# 12  1068               
#[Out]# 13  1069               
#[Out]# 14  1078               
#[Out]# 15  1079         None  
#[Out]# 16  1080               
#[Out]# 17  1081               
#[Out]# 18  1082               
#[Out]# 19  1083               
#[Out]# 20  1084               
#[Out]# 21  1085               
#[Out]# 22  1086               
#[Out]# 23  1087               
#[Out]# 24  1088               
#[Out]# 25  1089               
#[Out]# 26  1090               
#[Out]# 27  1091               
#[Out]# 28  1092               
#[Out]# 29  1093               
#[Out]# 30  1094               
#[Out]# 31  1095               
#[Out]# 32  1096               
#[Out]# 33  1097               
#[Out]# 34  1108               
#[Out]# 35  1109               
#[Out]# 36  1118               
#[Out]# 37  1119               
#[Out]# 38  1128               
#[Out]# 39  1129               
#[Out]# 40  1138               
#[Out]# 41  1139               
#[Out]# 42  1148               
#[Out]# 43  1149               
#[Out]# 44  1159               
#[Out]# 45  1168               
#[Out]# 46  1169               
#[Out]# 47  1178         None  
#[Out]# 48  1179         None  
#[Out]# 49  1180         None  
#[Out]# 50  1182         None  
#[Out]# 51  1184         None  
#[Out]# 52  1185               
#[Out]# 53  1186               
#[Out]# 54  1187         None  
#[Out]# 55  1188         None  
#[Out]# 56  1189         None  
#[Out]# 57  1190         None  
#[Out]# 58  1191         None  
#[Out]# 59  1192         None  
#[Out]#      ...          ...  
#[Out]# 
#[Out]# [6636 rows x 4 columns]
# Fri, 04 Jul 2014 14:42:21
info.describe()
#[Out]#                  id
#[Out]# count   6636.000000
#[Out]# mean   15733.055304
#[Out]# std     8715.095274
#[Out]# min     1008.000000
#[Out]# 25%    10170.750000
#[Out]# 50%    14445.000000
#[Out]# 75%    19188.250000
#[Out]# max    93600.000000
#[Out]# 
#[Out]# [8 rows x 1 columns]
# Fri, 04 Jul 2014 14:43:02
pd.value_counts(info.group)
#[Out]# Vegetables and Vegetable Products    812
#[Out]# Beef Products                        618
#[Out]# Baked Products                       496
#[Out]# Breakfast Cereals                    403
#[Out]# Legumes and Legume Products          365
#[Out]# Fast Foods                           365
#[Out]# Lamb, Veal, and Game Products        345
#[Out]# Sweets                               341
#[Out]# Fruits and Fruit Juices              328
#[Out]# Pork Products                        328
#[Out]# Beverages                            278
#[Out]# Soups, Sauces, and Gravies           275
#[Out]# Finfish and Shellfish Products       255
#[Out]# Baby Foods                           209
#[Out]# Cereal Grains and Pasta              183
#[Out]# Ethnic Foods                         165
#[Out]# Snacks                               162
#[Out]# Nut and Seed Products                128
#[Out]# Poultry Products                     116
#[Out]# Sausages and Luncheon Meats          111
#[Out]# Dairy and Egg Products               107
#[Out]# Fats and Oils                         97
#[Out]# Meals, Entrees, and Sidedishes        57
#[Out]# Restaurant Foods                      51
#[Out]# Spices and Herbs                      41
#[Out]# dtype: int64
# Fri, 04 Jul 2014 14:44:01
nutrients = []
# Fri, 04 Jul 2014 14:45:04
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
    
# Fri, 04 Jul 2014 14:45:26
nutrients[:5]
#[Out]# [                           description        group    units     value    id
#[Out]# 0                              Protein  Composition        g    25.180  1008
#[Out]# 1                    Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 2          Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 3                                  Ash        Other        g     3.280  1008
#[Out]# 4                               Energy       Energy     kcal   376.000  1008
#[Out]# 5                                Water  Composition        g    39.280  1008
#[Out]# 6                               Energy       Energy       kJ  1573.000  1008
#[Out]# 7                 Fiber, total dietary  Composition        g     0.000  1008
#[Out]# 8                          Calcium, Ca     Elements       mg   673.000  1008
#[Out]# 9                             Iron, Fe     Elements       mg     0.640  1008
#[Out]# 10                       Magnesium, Mg     Elements       mg    22.000  1008
#[Out]# 11                       Phosphorus, P     Elements       mg   490.000  1008
#[Out]# 12                        Potassium, K     Elements       mg    93.000  1008
#[Out]# 13                          Sodium, Na     Elements       mg   690.000  1008
#[Out]# 14                            Zinc, Zn     Elements       mg     2.940  1008
#[Out]# 15                          Copper, Cu     Elements       mg     0.024  1008
#[Out]# 16                       Manganese, Mn     Elements       mg     0.021  1008
#[Out]# 17                        Selenium, Se     Elements      mcg    14.500  1008
#[Out]# 18                       Vitamin A, IU     Vitamins       IU  1054.000  1008
#[Out]# 19                             Retinol     Vitamins      mcg   262.000  1008
#[Out]# 20                      Vitamin A, RAE     Vitamins  mcg_RAE   271.000  1008
#[Out]# 21      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1008
#[Out]# 22                             Thiamin     Vitamins       mg     0.031  1008
#[Out]# 23                          Riboflavin     Vitamins       mg     0.450  1008
#[Out]# 24                              Niacin     Vitamins       mg     0.180  1008
#[Out]# 25                    Pantothenic acid     Vitamins       mg     0.190  1008
#[Out]# 26                         Vitamin B-6     Vitamins       mg     0.074  1008
#[Out]# 27                       Folate, total     Vitamins      mcg    18.000  1008
#[Out]# 28                        Vitamin B-12     Vitamins      mcg     0.270  1008
#[Out]# 29                          Folic acid     Vitamins      mcg     0.000  1008
#[Out]# 30                        Folate, food     Vitamins      mcg    18.000  1008
#[Out]# 31                         Folate, DFE     Vitamins  mcg_DFE    18.000  1008
#[Out]# 32                         Cholesterol        Other       mg    93.000  1008
#[Out]# 33        Fatty acids, total saturated        Other        g    18.584  1008
#[Out]# 34  Fatty acids, total monounsaturated        Other        g     8.275  1008
#[Out]# 35  Fatty acids, total polyunsaturated        Other        g     0.830  1008
#[Out]# 36                          Tryptophan  Amino Acids        g     0.324  1008
#[Out]# 37                           Threonine  Amino Acids        g     0.896  1008
#[Out]# 38                          Isoleucine  Amino Acids        g     1.563  1008
#[Out]# 39                             Leucine  Amino Acids        g     2.412  1008
#[Out]# 40                              Lysine  Amino Acids        g     2.095  1008
#[Out]# 41                          Methionine  Amino Acids        g     0.659  1008
#[Out]# 42                             Cystine  Amino Acids        g     0.126  1008
#[Out]# 43                       Phenylalanine  Amino Acids        g     1.326  1008
#[Out]# 44                            Tyrosine  Amino Acids        g     1.216  1008
#[Out]# 45                              Valine  Amino Acids        g     1.682  1008
#[Out]# 46                            Arginine  Amino Acids        g     0.952  1008
#[Out]# 47                           Histidine  Amino Acids        g     0.884  1008
#[Out]# 48                             Alanine  Amino Acids        g     0.711  1008
#[Out]# 49                       Aspartic acid  Amino Acids        g     1.618  1008
#[Out]# 50                       Glutamic acid  Amino Acids        g     6.160  1008
#[Out]# 51                             Glycine  Amino Acids        g     0.439  1008
#[Out]# 52                             Proline  Amino Acids        g     2.838  1008
#[Out]# 53                              Serine  Amino Acids        g     1.472  1008
#[Out]# 54                             Protein  Composition        g    25.180  1008
#[Out]# 55                   Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 56         Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 57                                 Ash        Other        g     3.280  1008
#[Out]# 58                              Energy       Energy     kcal   376.000  1008
#[Out]# 59                               Water  Composition        g    39.280  1008
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [162 rows x 5 columns],
#[Out]#                             description        group    units     value    id
#[Out]# 0                              Protein  Composition        g    24.900  1009
#[Out]# 1                    Total lipid (fat)  Composition        g    33.140  1009
#[Out]# 2          Carbohydrate, by difference  Composition        g     1.280  1009
#[Out]# 3                                  Ash        Other        g     3.930  1009
#[Out]# 4                               Energy       Energy     kcal   403.000  1009
#[Out]# 5                              Sucrose       Sugars        g     0.240  1009
#[Out]# 6                              Lactose       Sugars        g     0.230  1009
#[Out]# 7                              Maltose       Sugars        g     0.150  1009
#[Out]# 8                       Alcohol, ethyl        Other        g     0.000  1009
#[Out]# 9                                Water  Composition        g    36.750  1009
#[Out]# 10                            Caffeine        Other       mg     0.000  1009
#[Out]# 11                         Theobromine        Other       mg     0.000  1009
#[Out]# 12                              Energy       Energy       kJ  1684.000  1009
#[Out]# 13                       Sugars, total  Composition        g     0.520  1009
#[Out]# 14                Fiber, total dietary  Composition        g     0.000  1009
#[Out]# 15                         Calcium, Ca     Elements       mg   721.000  1009
#[Out]# 16                            Iron, Fe     Elements       mg     0.680  1009
#[Out]# 17                       Magnesium, Mg     Elements       mg    28.000  1009
#[Out]# 18                       Phosphorus, P     Elements       mg   512.000  1009
#[Out]# 19                        Potassium, K     Elements       mg    98.000  1009
#[Out]# 20                          Sodium, Na     Elements       mg   621.000  1009
#[Out]# 21                            Zinc, Zn     Elements       mg     3.110  1009
#[Out]# 22                          Copper, Cu     Elements       mg     0.031  1009
#[Out]# 23                         Fluoride, F     Elements      mcg    34.900  1009
#[Out]# 24                       Manganese, Mn     Elements       mg     0.010  1009
#[Out]# 25                        Selenium, Se     Elements      mcg    13.900  1009
#[Out]# 26                       Vitamin A, IU     Vitamins       IU  1002.000  1009
#[Out]# 27                             Retinol     Vitamins      mcg   258.000  1009
#[Out]# 28                      Vitamin A, RAE     Vitamins  mcg_RAE   265.000  1009
#[Out]# 29                      Carotene, beta     Vitamins      mcg    85.000  1009
#[Out]# 30                     Carotene, alpha     Vitamins      mcg     0.000  1009
#[Out]# 31        Vitamin E (alpha-tocopherol)     Vitamins       mg     0.290  1009
#[Out]# 32                           Vitamin D     Vitamins       IU    24.000  1009
#[Out]# 33        Vitamin D3 (cholecalciferol)     Vitamins      mcg     0.600  1009
#[Out]# 34                 Vitamin D (D2 + D3)     Vitamins      mcg     0.600  1009
#[Out]# 35                 Cryptoxanthin, beta     Vitamins      mcg     0.000  1009
#[Out]# 36                            Lycopene     Vitamins      mcg     0.000  1009
#[Out]# 37                 Lutein + zeaxanthin     Vitamins      mcg     0.000  1009
#[Out]# 38                   Tocopherol, gamma     Vitamins       mg     0.000  1009
#[Out]# 39                   Tocopherol, delta     Vitamins       mg     0.000  1009
#[Out]# 40      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1009
#[Out]# 41                             Thiamin     Vitamins       mg     0.027  1009
#[Out]# 42                          Riboflavin     Vitamins       mg     0.375  1009
#[Out]# 43                              Niacin     Vitamins       mg     0.080  1009
#[Out]# 44                    Pantothenic acid     Vitamins       mg     0.413  1009
#[Out]# 45                         Vitamin B-6     Vitamins       mg     0.074  1009
#[Out]# 46                       Folate, total     Vitamins      mcg    18.000  1009
#[Out]# 47                        Vitamin B-12     Vitamins      mcg     0.830  1009
#[Out]# 48                      Choline, total     Vitamins       mg    16.500  1009
#[Out]# 49           Vitamin K (phylloquinone)     Vitamins      mcg     2.800  1009
#[Out]# 50                          Folic acid     Vitamins      mcg     0.000  1009
#[Out]# 51                        Folate, food     Vitamins      mcg    18.000  1009
#[Out]# 52                         Folate, DFE     Vitamins  mcg_DFE    18.000  1009
#[Out]# 53                             Betaine     Vitamins       mg     0.700  1009
#[Out]# 54                    Vitamin E, added     Vitamins       mg     0.000  1009
#[Out]# 55                 Vitamin B-12, added     Vitamins      mcg     0.000  1009
#[Out]# 56                         Cholesterol        Other       mg   105.000  1009
#[Out]# 57        Fatty acids, total saturated        Other        g    21.092  1009
#[Out]# 58  Fatty acids, total monounsaturated        Other        g     9.391  1009
#[Out]# 59  Fatty acids, total polyunsaturated        Other        g     0.942  1009
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [237 rows x 5 columns],
#[Out]#                             description        group    units     value    id
#[Out]# 0                                  Ash        Other        g     4.220  1018
#[Out]# 1                              Protein  Composition        g    24.990  1018
#[Out]# 2                    Total lipid (fat)  Composition        g    27.800  1018
#[Out]# 3          Carbohydrate, by difference  Composition        g     1.430  1018
#[Out]# 4                                  Ash        Other        g     4.220  1018
#[Out]# 5                               Energy       Energy     kcal   357.000  1018
#[Out]# 6                       Alcohol, ethyl        Other        g     0.000  1018
#[Out]# 7                                Water  Composition        g    41.560  1018
#[Out]# 8                             Caffeine        Other       mg     0.000  1018
#[Out]# 9                          Theobromine        Other       mg     0.000  1018
#[Out]# 10                              Energy       Energy       kJ  1492.000  1018
#[Out]# 11                       Sugars, total  Composition        g     1.430  1018
#[Out]# 12                Fiber, total dietary  Composition        g     0.000  1018
#[Out]# 13                         Calcium, Ca     Elements       mg   731.000  1018
#[Out]# 14                            Iron, Fe     Elements       mg     0.440  1018
#[Out]# 15                       Magnesium, Mg     Elements       mg    30.000  1018
#[Out]# 16                       Phosphorus, P     Elements       mg   536.000  1018
#[Out]# 17                        Potassium, K     Elements       mg   188.000  1018
#[Out]# 18                          Sodium, Na     Elements       mg   965.000  1018
#[Out]# 19                            Zinc, Zn     Elements       mg     3.750  1018
#[Out]# 20                          Copper, Cu     Elements       mg     0.036  1018
#[Out]# 21                       Manganese, Mn     Elements       mg     0.011  1018
#[Out]# 22                        Selenium, Se     Elements      mcg    14.500  1018
#[Out]# 23                       Vitamin A, IU     Vitamins       IU   825.000  1018
#[Out]# 24                             Retinol     Vitamins      mcg   242.000  1018
#[Out]# 25                      Vitamin A, RAE     Vitamins  mcg_RAE   243.000  1018
#[Out]# 26                      Carotene, beta     Vitamins      mcg    11.000  1018
#[Out]# 27                     Carotene, alpha     Vitamins      mcg     0.000  1018
#[Out]# 28        Vitamin E (alpha-tocopherol)     Vitamins       mg     0.240  1018
#[Out]# 29                           Vitamin D     Vitamins       IU    20.000  1018
#[Out]# 30        Vitamin D3 (cholecalciferol)     Vitamins      mcg     0.500  1018
#[Out]# 31                 Vitamin D (D2 + D3)     Vitamins      mcg     0.500  1018
#[Out]# 32                 Cryptoxanthin, beta     Vitamins      mcg     0.000  1018
#[Out]# 33                            Lycopene     Vitamins      mcg     0.000  1018
#[Out]# 34                 Lutein + zeaxanthin     Vitamins      mcg     0.000  1018
#[Out]# 35      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1018
#[Out]# 36                             Thiamin     Vitamins       mg     0.037  1018
#[Out]# 37                          Riboflavin     Vitamins       mg     0.389  1018
#[Out]# 38                              Niacin     Vitamins       mg     0.082  1018
#[Out]# 39                    Pantothenic acid     Vitamins       mg     0.281  1018
#[Out]# 40                         Vitamin B-6     Vitamins       mg     0.076  1018
#[Out]# 41                       Folate, total     Vitamins      mcg    16.000  1018
#[Out]# 42                        Vitamin B-12     Vitamins      mcg     1.540  1018
#[Out]# 43                      Choline, total     Vitamins       mg    15.400  1018
#[Out]# 44           Vitamin K (phylloquinone)     Vitamins      mcg     2.300  1018
#[Out]# 45                          Folic acid     Vitamins      mcg     0.000  1018
#[Out]# 46                        Folate, food     Vitamins      mcg    16.000  1018
#[Out]# 47                         Folate, DFE     Vitamins  mcg_DFE    16.000  1018
#[Out]# 48                    Vitamin E, added     Vitamins       mg     0.000  1018
#[Out]# 49                 Vitamin B-12, added     Vitamins      mcg     0.000  1018
#[Out]# 50                         Cholesterol        Other       mg    89.000  1018
#[Out]# 51        Fatty acids, total saturated        Other        g    17.572  1018
#[Out]# 52  Fatty acids, total monounsaturated        Other        g     8.125  1018
#[Out]# 53  Fatty acids, total polyunsaturated        Other        g     0.665  1018
#[Out]# 54                          Tryptophan  Amino Acids        g     0.352  1018
#[Out]# 55                           Threonine  Amino Acids        g     0.932  1018
#[Out]# 56                          Isoleucine  Amino Acids        g     1.308  1018
#[Out]# 57                             Leucine  Amino Acids        g     2.570  1018
#[Out]# 58                              Lysine  Amino Acids        g     2.660  1018
#[Out]# 59                          Methionine  Amino Acids        g     0.721  1018
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [213 rows x 5 columns],
#[Out]#                             description        group    units     value    id
#[Out]# 0                                  Ash        Other        g     5.200  1019
#[Out]# 1                              Protein  Composition        g    14.210  1019
#[Out]# 2                    Total lipid (fat)  Composition        g    21.280  1019
#[Out]# 3          Carbohydrate, by difference  Composition        g     4.090  1019
#[Out]# 4                                  Ash        Other        g     5.200  1019
#[Out]# 5                               Energy       Energy     kcal   264.000  1019
#[Out]# 6                       Alcohol, ethyl        Other        g     0.000  1019
#[Out]# 7                                Water  Composition        g    55.220  1019
#[Out]# 8                             Caffeine        Other       mg     0.000  1019
#[Out]# 9                          Theobromine        Other       mg     0.000  1019
#[Out]# 10                              Energy       Energy       kJ  1103.000  1019
#[Out]# 11                       Sugars, total  Composition        g     4.090  1019
#[Out]# 12                Fiber, total dietary  Composition        g     0.000  1019
#[Out]# 13                         Calcium, Ca     Elements       mg   493.000  1019
#[Out]# 14                            Iron, Fe     Elements       mg     0.650  1019
#[Out]# 15                       Magnesium, Mg     Elements       mg    19.000  1019
#[Out]# 16                       Phosphorus, P     Elements       mg   337.000  1019
#[Out]# 17                        Potassium, K     Elements       mg    62.000  1019
#[Out]# 18                          Sodium, Na     Elements       mg  1116.000  1019
#[Out]# 19                            Zinc, Zn     Elements       mg     2.880  1019
#[Out]# 20                          Copper, Cu     Elements       mg     0.032  1019
#[Out]# 21                       Manganese, Mn     Elements       mg     0.028  1019
#[Out]# 22                        Selenium, Se     Elements      mcg    15.000  1019
#[Out]# 23                       Vitamin A, IU     Vitamins       IU   422.000  1019
#[Out]# 24                             Retinol     Vitamins      mcg   125.000  1019
#[Out]# 25                      Vitamin A, RAE     Vitamins  mcg_RAE   125.000  1019
#[Out]# 26                      Carotene, beta     Vitamins      mcg     3.000  1019
#[Out]# 27                     Carotene, alpha     Vitamins      mcg     0.000  1019
#[Out]# 28        Vitamin E (alpha-tocopherol)     Vitamins       mg     0.180  1019
#[Out]# 29                           Vitamin D     Vitamins       IU    16.000  1019
#[Out]# 30        Vitamin D3 (cholecalciferol)     Vitamins      mcg     0.400  1019
#[Out]# 31                 Vitamin D (D2 + D3)     Vitamins      mcg     0.400  1019
#[Out]# 32                 Cryptoxanthin, beta     Vitamins      mcg     0.000  1019
#[Out]# 33                            Lycopene     Vitamins      mcg     0.000  1019
#[Out]# 34                 Lutein + zeaxanthin     Vitamins      mcg     0.000  1019
#[Out]# 35      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1019
#[Out]# 36                             Thiamin     Vitamins       mg     0.154  1019
#[Out]# 37                          Riboflavin     Vitamins       mg     0.844  1019
#[Out]# 38                              Niacin     Vitamins       mg     0.991  1019
#[Out]# 39                    Pantothenic acid     Vitamins       mg     0.967  1019
#[Out]# 40                         Vitamin B-6     Vitamins       mg     0.424  1019
#[Out]# 41                       Folate, total     Vitamins      mcg    32.000  1019
#[Out]# 42                        Vitamin B-12     Vitamins      mcg     1.690  1019
#[Out]# 43                      Choline, total     Vitamins       mg    15.400  1019
#[Out]# 44           Vitamin K (phylloquinone)     Vitamins      mcg     1.800  1019
#[Out]# 45                          Folic acid     Vitamins      mcg     0.000  1019
#[Out]# 46                        Folate, food     Vitamins      mcg    32.000  1019
#[Out]# 47                         Folate, DFE     Vitamins  mcg_DFE    32.000  1019
#[Out]# 48                    Vitamin E, added     Vitamins       mg     0.000  1019
#[Out]# 49                 Vitamin B-12, added     Vitamins      mcg     0.000  1019
#[Out]# 50                         Cholesterol        Other       mg    89.000  1019
#[Out]# 51        Fatty acids, total saturated        Other        g    14.946  1019
#[Out]# 52  Fatty acids, total monounsaturated        Other        g     4.623  1019
#[Out]# 53  Fatty acids, total polyunsaturated        Other        g     0.591  1019
#[Out]# 54                          Tryptophan  Amino Acids        g     0.200  1019
#[Out]# 55                           Threonine  Amino Acids        g     0.637  1019
#[Out]# 56                          Isoleucine  Amino Acids        g     0.803  1019
#[Out]# 57                             Leucine  Amino Acids        g     1.395  1019
#[Out]# 58                              Lysine  Amino Acids        g     1.219  1019
#[Out]# 59                          Methionine  Amino Acids        g     0.368  1019
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [213 rows x 5 columns],
#[Out]#                             description        group    units     value    id
#[Out]# 0                                  Ash        Other        g     3.270  1028
#[Out]# 1                              Protein  Composition        g    24.260  1028
#[Out]# 2                    Total lipid (fat)  Composition        g    15.920  1028
#[Out]# 3          Carbohydrate, by difference  Composition        g     2.770  1028
#[Out]# 4                                  Ash        Other        g     3.270  1028
#[Out]# 5                               Energy       Energy     kcal   254.000  1028
#[Out]# 6                       Alcohol, ethyl        Other        g     0.000  1028
#[Out]# 7                                Water  Composition        g    53.780  1028
#[Out]# 8                             Caffeine        Other       mg     0.000  1028
#[Out]# 9                          Theobromine        Other       mg     0.000  1028
#[Out]# 10                              Energy       Energy       kJ  1064.000  1028
#[Out]# 11                       Sugars, total  Composition        g     1.130  1028
#[Out]# 12                Fiber, total dietary  Composition        g     0.000  1028
#[Out]# 13                         Calcium, Ca     Elements       mg   782.000  1028
#[Out]# 14                            Iron, Fe     Elements       mg     0.220  1028
#[Out]# 15                       Magnesium, Mg     Elements       mg    23.000  1028
#[Out]# 16                       Phosphorus, P     Elements       mg   463.000  1028
#[Out]# 17                        Potassium, K     Elements       mg    84.000  1028
#[Out]# 18                          Sodium, Na     Elements       mg   619.000  1028
#[Out]# 19                            Zinc, Zn     Elements       mg     2.760  1028
#[Out]# 20                          Copper, Cu     Elements       mg     0.025  1028
#[Out]# 21                       Manganese, Mn     Elements       mg     0.010  1028
#[Out]# 22                        Selenium, Se     Elements      mcg    14.400  1028
#[Out]# 23                       Vitamin A, IU     Vitamins       IU   481.000  1028
#[Out]# 24                             Retinol     Vitamins      mcg   124.000  1028
#[Out]# 25                      Vitamin A, RAE     Vitamins  mcg_RAE   127.000  1028
#[Out]# 26                      Carotene, beta     Vitamins      mcg    41.000  1028
#[Out]# 27                     Carotene, alpha     Vitamins      mcg     0.000  1028
#[Out]# 28        Vitamin E (alpha-tocopherol)     Vitamins       mg     0.140  1028
#[Out]# 29                           Vitamin D     Vitamins       IU    12.000  1028
#[Out]# 30        Vitamin D3 (cholecalciferol)     Vitamins      mcg     0.300  1028
#[Out]# 31                 Vitamin D (D2 + D3)     Vitamins      mcg     0.300  1028
#[Out]# 32                 Cryptoxanthin, beta     Vitamins      mcg     0.000  1028
#[Out]# 33                            Lycopene     Vitamins      mcg     0.000  1028
#[Out]# 34                 Lutein + zeaxanthin     Vitamins      mcg     0.000  1028
#[Out]# 35      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1028
#[Out]# 36                             Thiamin     Vitamins       mg     0.018  1028
#[Out]# 37                          Riboflavin     Vitamins       mg     0.303  1028
#[Out]# 38                              Niacin     Vitamins       mg     0.105  1028
#[Out]# 39                    Pantothenic acid     Vitamins       mg     0.079  1028
#[Out]# 40                         Vitamin B-6     Vitamins       mg     0.070  1028
#[Out]# 41                       Folate, total     Vitamins      mcg     9.000  1028
#[Out]# 42                        Vitamin B-12     Vitamins      mcg     0.820  1028
#[Out]# 43                      Choline, total     Vitamins       mg    15.400  1028
#[Out]# 44           Vitamin K (phylloquinone)     Vitamins      mcg     1.600  1028
#[Out]# 45                          Folic acid     Vitamins      mcg     0.000  1028
#[Out]# 46                        Folate, food     Vitamins      mcg     9.000  1028
#[Out]# 47                         Folate, DFE     Vitamins  mcg_DFE     9.000  1028
#[Out]# 48                    Vitamin E, added     Vitamins       mg     0.000  1028
#[Out]# 49                 Vitamin B-12, added     Vitamins      mcg     0.000  1028
#[Out]# 50                         Cholesterol        Other       mg    64.000  1028
#[Out]# 51        Fatty acids, total saturated        Other        g    10.114  1028
#[Out]# 52  Fatty acids, total monounsaturated        Other        g     4.510  1028
#[Out]# 53  Fatty acids, total polyunsaturated        Other        g     0.472  1028
#[Out]# 54                          Tryptophan  Amino Acids        g     0.339  1028
#[Out]# 55                           Threonine  Amino Acids        g     0.924  1028
#[Out]# 56                          Isoleucine  Amino Acids        g     1.164  1028
#[Out]# 57                             Leucine  Amino Acids        g     2.365  1028
#[Out]# 58                              Lysine  Amino Acids        g     2.464  1028
#[Out]# 59                          Methionine  Amino Acids        g     0.677  1028
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [213 rows x 5 columns]]
# Fri, 04 Jul 2014 14:45:37
nutrients[:1]
#[Out]# [                           description        group    units     value    id
#[Out]# 0                              Protein  Composition        g    25.180  1008
#[Out]# 1                    Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 2          Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 3                                  Ash        Other        g     3.280  1008
#[Out]# 4                               Energy       Energy     kcal   376.000  1008
#[Out]# 5                                Water  Composition        g    39.280  1008
#[Out]# 6                               Energy       Energy       kJ  1573.000  1008
#[Out]# 7                 Fiber, total dietary  Composition        g     0.000  1008
#[Out]# 8                          Calcium, Ca     Elements       mg   673.000  1008
#[Out]# 9                             Iron, Fe     Elements       mg     0.640  1008
#[Out]# 10                       Magnesium, Mg     Elements       mg    22.000  1008
#[Out]# 11                       Phosphorus, P     Elements       mg   490.000  1008
#[Out]# 12                        Potassium, K     Elements       mg    93.000  1008
#[Out]# 13                          Sodium, Na     Elements       mg   690.000  1008
#[Out]# 14                            Zinc, Zn     Elements       mg     2.940  1008
#[Out]# 15                          Copper, Cu     Elements       mg     0.024  1008
#[Out]# 16                       Manganese, Mn     Elements       mg     0.021  1008
#[Out]# 17                        Selenium, Se     Elements      mcg    14.500  1008
#[Out]# 18                       Vitamin A, IU     Vitamins       IU  1054.000  1008
#[Out]# 19                             Retinol     Vitamins      mcg   262.000  1008
#[Out]# 20                      Vitamin A, RAE     Vitamins  mcg_RAE   271.000  1008
#[Out]# 21      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1008
#[Out]# 22                             Thiamin     Vitamins       mg     0.031  1008
#[Out]# 23                          Riboflavin     Vitamins       mg     0.450  1008
#[Out]# 24                              Niacin     Vitamins       mg     0.180  1008
#[Out]# 25                    Pantothenic acid     Vitamins       mg     0.190  1008
#[Out]# 26                         Vitamin B-6     Vitamins       mg     0.074  1008
#[Out]# 27                       Folate, total     Vitamins      mcg    18.000  1008
#[Out]# 28                        Vitamin B-12     Vitamins      mcg     0.270  1008
#[Out]# 29                          Folic acid     Vitamins      mcg     0.000  1008
#[Out]# 30                        Folate, food     Vitamins      mcg    18.000  1008
#[Out]# 31                         Folate, DFE     Vitamins  mcg_DFE    18.000  1008
#[Out]# 32                         Cholesterol        Other       mg    93.000  1008
#[Out]# 33        Fatty acids, total saturated        Other        g    18.584  1008
#[Out]# 34  Fatty acids, total monounsaturated        Other        g     8.275  1008
#[Out]# 35  Fatty acids, total polyunsaturated        Other        g     0.830  1008
#[Out]# 36                          Tryptophan  Amino Acids        g     0.324  1008
#[Out]# 37                           Threonine  Amino Acids        g     0.896  1008
#[Out]# 38                          Isoleucine  Amino Acids        g     1.563  1008
#[Out]# 39                             Leucine  Amino Acids        g     2.412  1008
#[Out]# 40                              Lysine  Amino Acids        g     2.095  1008
#[Out]# 41                          Methionine  Amino Acids        g     0.659  1008
#[Out]# 42                             Cystine  Amino Acids        g     0.126  1008
#[Out]# 43                       Phenylalanine  Amino Acids        g     1.326  1008
#[Out]# 44                            Tyrosine  Amino Acids        g     1.216  1008
#[Out]# 45                              Valine  Amino Acids        g     1.682  1008
#[Out]# 46                            Arginine  Amino Acids        g     0.952  1008
#[Out]# 47                           Histidine  Amino Acids        g     0.884  1008
#[Out]# 48                             Alanine  Amino Acids        g     0.711  1008
#[Out]# 49                       Aspartic acid  Amino Acids        g     1.618  1008
#[Out]# 50                       Glutamic acid  Amino Acids        g     6.160  1008
#[Out]# 51                             Glycine  Amino Acids        g     0.439  1008
#[Out]# 52                             Proline  Amino Acids        g     2.838  1008
#[Out]# 53                              Serine  Amino Acids        g     1.472  1008
#[Out]# 54                             Protein  Composition        g    25.180  1008
#[Out]# 55                   Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 56         Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 57                                 Ash        Other        g     3.280  1008
#[Out]# 58                              Energy       Energy     kcal   376.000  1008
#[Out]# 59                               Water  Composition        g    39.280  1008
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [162 rows x 5 columns]]
# Fri, 04 Jul 2014 14:45:59
nutrients[:1][:1]
#[Out]# [                           description        group    units     value    id
#[Out]# 0                              Protein  Composition        g    25.180  1008
#[Out]# 1                    Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 2          Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 3                                  Ash        Other        g     3.280  1008
#[Out]# 4                               Energy       Energy     kcal   376.000  1008
#[Out]# 5                                Water  Composition        g    39.280  1008
#[Out]# 6                               Energy       Energy       kJ  1573.000  1008
#[Out]# 7                 Fiber, total dietary  Composition        g     0.000  1008
#[Out]# 8                          Calcium, Ca     Elements       mg   673.000  1008
#[Out]# 9                             Iron, Fe     Elements       mg     0.640  1008
#[Out]# 10                       Magnesium, Mg     Elements       mg    22.000  1008
#[Out]# 11                       Phosphorus, P     Elements       mg   490.000  1008
#[Out]# 12                        Potassium, K     Elements       mg    93.000  1008
#[Out]# 13                          Sodium, Na     Elements       mg   690.000  1008
#[Out]# 14                            Zinc, Zn     Elements       mg     2.940  1008
#[Out]# 15                          Copper, Cu     Elements       mg     0.024  1008
#[Out]# 16                       Manganese, Mn     Elements       mg     0.021  1008
#[Out]# 17                        Selenium, Se     Elements      mcg    14.500  1008
#[Out]# 18                       Vitamin A, IU     Vitamins       IU  1054.000  1008
#[Out]# 19                             Retinol     Vitamins      mcg   262.000  1008
#[Out]# 20                      Vitamin A, RAE     Vitamins  mcg_RAE   271.000  1008
#[Out]# 21      Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1008
#[Out]# 22                             Thiamin     Vitamins       mg     0.031  1008
#[Out]# 23                          Riboflavin     Vitamins       mg     0.450  1008
#[Out]# 24                              Niacin     Vitamins       mg     0.180  1008
#[Out]# 25                    Pantothenic acid     Vitamins       mg     0.190  1008
#[Out]# 26                         Vitamin B-6     Vitamins       mg     0.074  1008
#[Out]# 27                       Folate, total     Vitamins      mcg    18.000  1008
#[Out]# 28                        Vitamin B-12     Vitamins      mcg     0.270  1008
#[Out]# 29                          Folic acid     Vitamins      mcg     0.000  1008
#[Out]# 30                        Folate, food     Vitamins      mcg    18.000  1008
#[Out]# 31                         Folate, DFE     Vitamins  mcg_DFE    18.000  1008
#[Out]# 32                         Cholesterol        Other       mg    93.000  1008
#[Out]# 33        Fatty acids, total saturated        Other        g    18.584  1008
#[Out]# 34  Fatty acids, total monounsaturated        Other        g     8.275  1008
#[Out]# 35  Fatty acids, total polyunsaturated        Other        g     0.830  1008
#[Out]# 36                          Tryptophan  Amino Acids        g     0.324  1008
#[Out]# 37                           Threonine  Amino Acids        g     0.896  1008
#[Out]# 38                          Isoleucine  Amino Acids        g     1.563  1008
#[Out]# 39                             Leucine  Amino Acids        g     2.412  1008
#[Out]# 40                              Lysine  Amino Acids        g     2.095  1008
#[Out]# 41                          Methionine  Amino Acids        g     0.659  1008
#[Out]# 42                             Cystine  Amino Acids        g     0.126  1008
#[Out]# 43                       Phenylalanine  Amino Acids        g     1.326  1008
#[Out]# 44                            Tyrosine  Amino Acids        g     1.216  1008
#[Out]# 45                              Valine  Amino Acids        g     1.682  1008
#[Out]# 46                            Arginine  Amino Acids        g     0.952  1008
#[Out]# 47                           Histidine  Amino Acids        g     0.884  1008
#[Out]# 48                             Alanine  Amino Acids        g     0.711  1008
#[Out]# 49                       Aspartic acid  Amino Acids        g     1.618  1008
#[Out]# 50                       Glutamic acid  Amino Acids        g     6.160  1008
#[Out]# 51                             Glycine  Amino Acids        g     0.439  1008
#[Out]# 52                             Proline  Amino Acids        g     2.838  1008
#[Out]# 53                              Serine  Amino Acids        g     1.472  1008
#[Out]# 54                             Protein  Composition        g    25.180  1008
#[Out]# 55                   Total lipid (fat)  Composition        g    29.200  1008
#[Out]# 56         Carbohydrate, by difference  Composition        g     3.060  1008
#[Out]# 57                                 Ash        Other        g     3.280  1008
#[Out]# 58                              Energy       Energy     kcal   376.000  1008
#[Out]# 59                               Water  Composition        g    39.280  1008
#[Out]#                                    ...          ...      ...       ...   ...
#[Out]# 
#[Out]# [162 rows x 5 columns]]
# Fri, 04 Jul 2014 14:46:41
nutrients = pd.concat(nutrients, ignore_index=True)
# Fri, 04 Jul 2014 14:47:11
nutrients.describe()
#[Out]#                value             id
#[Out]# count  389355.000000  389355.000000
#[Out]# mean       66.074429   14951.226806
#[Out]# std       644.176571    8664.025821
#[Out]# min         0.000000    1008.000000
#[Out]# 25%         0.040000   10047.000000
#[Out]# 50%         0.784000   13898.000000
#[Out]# 75%         9.000000   19019.000000
#[Out]# max    100000.000000   93600.000000
#[Out]# 
#[Out]# [8 rows x 2 columns]
# Fri, 04 Jul 2014 14:47:32
nutrients[:10]
#[Out]#                    description        group units    value    id
#[Out]# 0                      Protein  Composition     g    25.18  1008
#[Out]# 1            Total lipid (fat)  Composition     g    29.20  1008
#[Out]# 2  Carbohydrate, by difference  Composition     g     3.06  1008
#[Out]# 3                          Ash        Other     g     3.28  1008
#[Out]# 4                       Energy       Energy  kcal   376.00  1008
#[Out]# 5                        Water  Composition     g    39.28  1008
#[Out]# 6                       Energy       Energy    kJ  1573.00  1008
#[Out]# 7         Fiber, total dietary  Composition     g     0.00  1008
#[Out]# 8                  Calcium, Ca     Elements    mg   673.00  1008
#[Out]# 9                     Iron, Fe     Elements    mg     0.64  1008
#[Out]# 
#[Out]# [10 rows x 5 columns]
# Fri, 04 Jul 2014 14:48:06
nutrients.duplicated().sum()
#[Out]# 14179
# Fri, 04 Jul 2014 14:48:32
nutrients = nutrients.drop_duplicates()
# Fri, 04 Jul 2014 14:49:30
col_mapping = {'description': 'food',
'group': 'fgroup'}
# Fri, 04 Jul 2014 14:49:48
info = info.rename(columns=col_mapping, copy=False)
# Fri, 04 Jul 2014 14:49:58
info[:10]
#[Out]#                                                 food                  fgroup  \
#[Out]# 0                                    Cheese, caraway  Dairy and Egg Products   
#[Out]# 1                                    Cheese, cheddar  Dairy and Egg Products   
#[Out]# 2                                       Cheese, edam  Dairy and Egg Products   
#[Out]# 3                                       Cheese, feta  Dairy and Egg Products   
#[Out]# 4                 Cheese, mozzarella, part skim milk  Dairy and Egg Products   
#[Out]# 5   Cheese, mozzarella, part skim milk, low moisture  Dairy and Egg Products   
#[Out]# 6                                     Cheese, romano  Dairy and Egg Products   
#[Out]# 7                                  Cheese, roquefort  Dairy and Egg Products   
#[Out]# 8  Cheese spread, pasteurized process, american, ...  Dairy and Egg Products   
#[Out]# 9                        Cream, fluid, half and half  Dairy and Egg Products   
#[Out]# 
#[Out]#      id manufacturer  
#[Out]# 0  1008               
#[Out]# 1  1009               
#[Out]# 2  1018               
#[Out]# 3  1019               
#[Out]# 4  1028               
#[Out]# 5  1029               
#[Out]# 6  1038               
#[Out]# 7  1039               
#[Out]# 8  1048               
#[Out]# 9  1049               
#[Out]# 
#[Out]# [10 rows x 4 columns]
# Fri, 04 Jul 2014 14:51:47
col_mapping = {'description': 'nutrient',
'group': 'nutgroup'}
# Fri, 04 Jul 2014 14:52:09
nutrients = nutrients.rename(columns=col_mapping, copy=False)
# Fri, 04 Jul 2014 14:52:17
nutrients.head()
#[Out]#                       nutrient     nutgroup units   value    id
#[Out]# 0                      Protein  Composition     g   25.18  1008
#[Out]# 1            Total lipid (fat)  Composition     g   29.20  1008
#[Out]# 2  Carbohydrate, by difference  Composition     g    3.06  1008
#[Out]# 3                          Ash        Other     g    3.28  1008
#[Out]# 4                       Energy       Energy  kcal  376.00  1008
#[Out]# 
#[Out]# [5 rows x 5 columns]
# Fri, 04 Jul 2014 14:53:22
ndata = pd.merge(nutrients, info, on='id', how='outer')
# Fri, 04 Jul 2014 14:53:37
ndata.head()
#[Out]#                       nutrient     nutgroup units   value    id  \
#[Out]# 0                      Protein  Composition     g   25.18  1008   
#[Out]# 1            Total lipid (fat)  Composition     g   29.20  1008   
#[Out]# 2  Carbohydrate, by difference  Composition     g    3.06  1008   
#[Out]# 3                          Ash        Other     g    3.28  1008   
#[Out]# 4                       Energy       Energy  kcal  376.00  1008   
#[Out]# 
#[Out]#               food                  fgroup manufacturer  
#[Out]# 0  Cheese, caraway  Dairy and Egg Products               
#[Out]# 1  Cheese, caraway  Dairy and Egg Products               
#[Out]# 2  Cheese, caraway  Dairy and Egg Products               
#[Out]# 3  Cheese, caraway  Dairy and Egg Products               
#[Out]# 4  Cheese, caraway  Dairy and Egg Products               
#[Out]# 
#[Out]# [5 rows x 8 columns]
# Fri, 04 Jul 2014 14:54:08
ndata.ix[30000]
#[Out]# nutrient                                       Glycine
#[Out]# nutgroup                                   Amino Acids
#[Out]# units                                                g
#[Out]# value                                             0.04
#[Out]# id                                                6158
#[Out]# food            Soup, tomato bisque, canned, condensed
#[Out]# fgroup                      Soups, Sauces, and Gravies
#[Out]# manufacturer                                          
#[Out]# Name: 30000, dtype: object
# Fri, 04 Jul 2014 14:59:21
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
# Fri, 04 Jul 2014 15:00:51
result['Zinc, Zn'].order().plot(kind='barh')
#[Out]# <matplotlib.axes.AxesSubplot at 0x254700b8>
# Fri, 04 Jul 2014 15:04:53
%pylab inline
# Fri, 04 Jul 2014 15:06:34
%pylab
# Fri, 04 Jul 2014 15:08:52
ipython --help
# Fri, 04 Jul 2014 15:09:06
%pylab qt
# Fri, 04 Jul 2014 15:09:28
result['Zinc, Zn'].order().plot(kind='barh')
#[Out]# <matplotlib.axes.AxesSubplot at 0xa390668>
# Fri, 04 Jul 2014 15:11:20
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])
# Fri, 04 Jul 2014 15:12:41
get_maximum = lambda x: x.xs(x.value.idxmax())
# Fri, 04 Jul 2014 15:12:58
get_minimum = lambda x: x.xs(x.value.idxmin())
# Fri, 04 Jul 2014 15:13:24
max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]
# Fri, 04 Jul 2014 15:13:49
max_foods.food = max_foods.food.str[:50]
# Fri, 04 Jul 2014 15:14:42
max_foods.ix['Amino Acids']['food']
#[Out]# nutrient
#[Out]# Alanine                           Gelatins, dry powder, unsweetened
#[Out]# Arginine                               Seeds, sesame flour, low-fat
#[Out]# Aspartic acid                                   Soy protein isolate
#[Out]# Cystine                Seeds, cottonseed flour, low fat (glandless)
#[Out]# Glutamic acid                                   Soy protein isolate
#[Out]# Glycine                           Gelatins, dry powder, unsweetened
#[Out]# Histidine                Whale, beluga, meat, dried (Alaska Native)
#[Out]# Hydroxyproline    KENTUCKY FRIED CHICKEN, Fried Chicken, ORIGINA...
#[Out]# Isoleucine        Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Leucine           Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Lysine            Seal, bearded (Oogruk), meat, dried (Alaska Na...
#[Out]# Methionine                    Fish, cod, Atlantic, dried and salted
#[Out]# Phenylalanine     Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Proline                           Gelatins, dry powder, unsweetened
#[Out]# Serine            Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Threonine         Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Tryptophan         Sea lion, Steller, meat with fat (Alaska Native)
#[Out]# Tyrosine          Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Valine            Soy protein isolate, PROTEIN TECHNOLOGIES INTE...
#[Out]# Name: food, dtype: object
# Fri, 04 Jul 2014 15:15:24
max_foods
#[Out]#                                                     value  \
#[Out]# nutgroup    nutrient                                        
#[Out]# Amino Acids Alanine                                 8.009   
#[Out]#             Arginine                                7.436   
#[Out]#             Aspartic acid                          10.203   
#[Out]#             Cystine                                 1.307   
#[Out]#             Glutamic acid                          17.452   
#[Out]#             Glycine                                19.049   
#[Out]#             Histidine                               2.999   
#[Out]#             Hydroxyproline                          0.803   
#[Out]#             Isoleucine                              4.300   
#[Out]#             Leucine                                 7.200   
#[Out]#             Lysine                                  6.690   
#[Out]#             Methionine                              1.859   
#[Out]#             Phenylalanine                           4.600   
#[Out]#             Proline                                12.295   
#[Out]#             Serine                                  4.600   
#[Out]#             Threonine                               3.300   
#[Out]#             Tryptophan                              1.600   
#[Out]#             Tyrosine                                3.300   
#[Out]#             Valine                                  4.500   
#[Out]# Composition Adjusted Protein                       12.900   
#[Out]#             Carbohydrate, by difference           100.000   
#[Out]#             Fiber, total dietary                   79.000   
#[Out]#             Protein                                88.320   
#[Out]#             Sugars, total                          99.800   
#[Out]#             Total lipid (fat)                     100.000   
#[Out]#             Water                                 100.000   
#[Out]# Elements    Calcium, Ca                          7364.000   
#[Out]#             Copper, Cu                             15.050   
#[Out]#             Fluoride, F                           584.000   
#[Out]#             Iron, Fe                               87.470   
#[Out]#             Magnesium, Mg                         781.000   
#[Out]#             Manganese, Mn                         133.000   
#[Out]#             Phosphorus, P                        9918.000   
#[Out]#             Potassium, K                        16500.000   
#[Out]#             Selenium, Se                         1917.000   
#[Out]#             Sodium, Na                          27360.000   
#[Out]#             Zinc, Zn                               90.950   
#[Out]# Energy      Energy                               3774.000   
#[Out]# Other       Alcohol, ethyl                         42.500   
#[Out]#             Ash                                    72.500   
#[Out]#             Beta-sitosterol                       426.000   
#[Out]#             Caffeine                             3680.000   
#[Out]#             Campesterol                           241.000   
#[Out]#             Cholesterol                          3100.000   
#[Out]#             Fatty acids, total monounsaturated     83.689   
#[Out]#             Fatty acids, total polyunsaturated     66.000   
#[Out]#             Fatty acids, total saturated           95.600   
#[Out]#             Fatty acids, total trans               20.578   
#[Out]#             Fatty acids, total trans-monoenoic     18.970   
#[Out]#             Fatty acids, total trans-polyenoic      3.543   
#[Out]#             Phytosterols                         9060.000   
#[Out]#             Stigmasterol                           38.000   
#[Out]#             Theobromine                          2634.000   
#[Out]# Sugars      Fructose                               42.830   
#[Out]#             Galactose                               5.620   
#[Out]#             Glucose (dextrose)                     57.000   
#[Out]#             Lactose                                56.000   
#[Out]#             Maltose                                10.430   
#[Out]#             Starch                                 73.770   
#[Out]#             Sucrose                                99.800   
#[Out]#                                                       ...   
#[Out]# 
#[Out]#                                                                                              food  
#[Out]# nutgroup    nutrient                                                                               
#[Out]# Amino Acids Alanine                                             Gelatins, dry powder, unsweetened  
#[Out]#             Arginine                                                 Seeds, sesame flour, low-fat  
#[Out]#             Aspartic acid                                                     Soy protein isolate  
#[Out]#             Cystine                                  Seeds, cottonseed flour, low fat (glandless)  
#[Out]#             Glutamic acid                                                     Soy protein isolate  
#[Out]#             Glycine                                             Gelatins, dry powder, unsweetened  
#[Out]#             Histidine                                  Whale, beluga, meat, dried (Alaska Native)  
#[Out]#             Hydroxyproline                      KENTUCKY FRIED CHICKEN, Fried Chicken, ORIGINA...  
#[Out]#             Isoleucine                          Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Leucine                             Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Lysine                              Seal, bearded (Oogruk), meat, dried (Alaska Na...  
#[Out]#             Methionine                                      Fish, cod, Atlantic, dried and salted  
#[Out]#             Phenylalanine                       Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Proline                                             Gelatins, dry powder, unsweetened  
#[Out]#             Serine                              Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Threonine                           Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Tryptophan                           Sea lion, Steller, meat with fat (Alaska Native)  
#[Out]#             Tyrosine                            Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]#             Valine                              Soy protein isolate, PROTEIN TECHNOLOGIES INTE...  
#[Out]# Composition Adjusted Protein                               Baking chocolate, unsweetened, squares  
#[Out]#             Carbohydrate, by difference               Sweeteners, tabletop, fructose, dry, powder  
#[Out]#             Fiber, total dietary                                                 Corn bran, crude  
#[Out]#             Protein                             Soy protein isolate, potassium type, crude pro...  
#[Out]#             Sugars, total                                                      Sugars, granulated  
#[Out]#             Total lipid (fat)                                                     Oil, wheat germ  
#[Out]#             Water                                                   Water, bottled, POLAND SPRING  
#[Out]# Elements    Calcium, Ca                         Leavening agents, baking powder, double-acting...  
#[Out]#             Copper, Cu                          Veal, variety meats and by-products, liver, co...  
#[Out]#             Fluoride, F                         Tea, instant, sweetened with sugar, lemon-flav...  
#[Out]#             Iron, Fe                                Salad dressing, russian dressing, low calorie  
#[Out]#             Magnesium, Mg                                                        Rice bran, crude  
#[Out]#             Manganese, Mn                        Tea, instant, unsweetened, powder, decaffeinated  
#[Out]#             Phosphorus, P                       Leavening agents, baking powder, double-acting...  
#[Out]#             Potassium, K                                        Leavening agents, cream of tartar  
#[Out]#             Selenium, Se                                      Nuts, brazilnuts, dried, unblanched  
#[Out]#             Sodium, Na                                              Leavening agents, baking soda  
#[Out]#             Zinc, Zn                                            Mollusks, oyster, eastern, canned  
#[Out]# Energy      Energy                                                            Fish oil, cod liver  
#[Out]# Other       Alcohol, ethyl                      Alcoholic beverage, distilled, all (gin, rum, ...  
#[Out]#             Ash                                            Desserts, rennin, tablets, unsweetened  
#[Out]#             Beta-sitosterol                     Oil, vegetable, Natreon canola, high stability...  
#[Out]#             Caffeine                                            Tea, instant, unsweetened, powder  
#[Out]#             Campesterol                                                               Oil, canola  
#[Out]#             Cholesterol                         Beef, variety meats and by-products, brain, co...  
#[Out]#             Fatty acids, total monounsaturated          Oil, sunflower, high oleic (70% and over)  
#[Out]#             Fatty acids, total polyunsaturated                                      Oil, flaxseed  
#[Out]#             Fatty acids, total saturated                   Fish oil, menhaden, fully hydrogenated  
#[Out]#             Fatty acids, total trans            Margarine, industrial, soy and partially hydro...  
#[Out]#             Fatty acids, total trans-monoenoic  Margarine, industrial, soy and partially hydro...  
#[Out]#             Fatty acids, total trans-polyenoic  Oil, industrial, soy (partially hydrogenated),...  
#[Out]#             Phytosterols                        Margarine-like, vegetable oil spread, approxim...  
#[Out]#             Stigmasterol                                   Baking chocolate, unsweetened, squares  
#[Out]#             Theobromine                         Cocoa, dry powder, unsweetened, processed with...  
#[Out]# Sugars      Fructose                                                     Agave, dried (Southwest)  
#[Out]#             Galactose                           Formulated bar, SLIM-FAST OPTIMA meal bar, mil...  
#[Out]#             Glucose (dextrose)                  Infant formula, MEAD JOHNSON, ENFAMIL, LACTOFR...  
#[Out]#             Lactose                             Infant formula, MEAD JOHNSON, ENFAMIL, with ir...  
#[Out]#             Maltose                                 Cereals ready-to-eat, POST, GRAPE-NUTS Cereal  
#[Out]#             Starch                              Rice, white, long-grain, precooked or instant,...  
#[Out]#             Sucrose                                                            Sugars, granulated  
#[Out]#                                                                                               ...  
#[Out]# 
#[Out]# [94 rows x 2 columns]
# Fri, 04 Jul 2014 15:15:46
max_foods.head()
#[Out]#                             value  \
#[Out]# nutgroup    nutrient                
#[Out]# Amino Acids Alanine         8.009   
#[Out]#             Arginine        7.436   
#[Out]#             Aspartic acid  10.203   
#[Out]#             Cystine         1.307   
#[Out]#             Glutamic acid  17.452   
#[Out]# 
#[Out]#                                                                    food  
#[Out]# nutgroup    nutrient                                                     
#[Out]# Amino Acids Alanine                   Gelatins, dry powder, unsweetened  
#[Out]#             Arginine                       Seeds, sesame flour, low-fat  
#[Out]#             Aspartic acid                           Soy protein isolate  
#[Out]#             Cystine        Seeds, cottonseed flour, low fat (glandless)  
#[Out]#             Glutamic acid                           Soy protein isolate  
#[Out]# 
#[Out]# [5 rows x 2 columns]
# Fri, 04 Jul 2014 15:16:31
%logstop
