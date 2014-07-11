pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
cd ..\\..
cd "Google Drive\\Python for Data Analysis\\pydata-book\\ch08"
ls
# Sun, 06 Jul 2014 13:50:55
%pylab# Sun, 06 Jul 2014 13:51:25
%pylab inline
# Sun, 06 Jul 2014 13:51:37
import pandas as pd
# Sun, 06 Jul 2014 13:53:21
import numpy as np
# Sun, 06 Jul 2014 13:53:30
from pandas import DataFrame, Series
# Sun, 06 Jul 2014 14:08:58
plot(np.arange(10))
#[Out]# [<matplotlib.lines.Line2D at 0xc799ef0>]
# Sun, 06 Jul 2014 14:09:36
import matplotlib.pyplot as plt
# Sun, 06 Jul 2014 14:18:20
fig = plt.figure()
%logstart -o -r -t pandas_ch08_log.py append
cd ..\\..
cd "Google Drive\\Python for Data Analysis\\pydata-book\\ch08"
ls
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
%pylab
import matplotlib.pyplot as plt
fig = plt.figure()
plt.figure(2)
#[Out]# <matplotlib.figure.Figure object at 0x00000000035717F0>
plt.gcf
#[Out]# <function gcf at 0x000000000BC41198>
plt.gcf()
#[Out]# <matplotlib.figure.Figure object at 0x000000000345FB38>
fig
#[Out]# <matplotlib.figure.Figure object at 0x000000000345FB38>
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--')
#[Out]# [<matplotlib.lines.Line2D object at 0x0000000010685C50>]
_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
#[Out]# <matplotlib.collections.PathCollection object at 0x000000001096C7F0>
fig, axes = plt.subplots(2, 3)
axes
#[Out]# array([[<matplotlib.axes.AxesSubplot object at 0x0000000010977C18>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000010AA7CF8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000010982128>],
#[Out]#        [<matplotlib.axes.AxesSubplot object at 0x0000000010C3E748>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000010C624A8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000010DCA128>]], dtype=object)
axes[0, 1]
#[Out]# <matplotlib.axes.AxesSubplot object at 0x0000000010AA7CF8>
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.plot(randn(30).cumsum(), 'ko--')
#[Out]# [<matplotlib.lines.Line2D object at 0x0000000012447CC0>]
plt.plot(randn(30).cumsum(), 'ko--')
#[Out]# [<matplotlib.lines.Line2D object at 0x0000000010C27128>]
plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
#[Out]# [<matplotlib.lines.Line2D object at 0x000000000C3BE2B0>]
data = randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
#[Out]# [<matplotlib.lines.Line2D object at 0x000000000C189400>]
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
#[Out]# [<matplotlib.lines.Line2D object at 0x00000000126214E0>]
plt.legend(loc='best')
#[Out]# <matplotlib.legend.Legend object at 0x0000000012621F28>
plt.xlim()
#[Out]# (0.0, 30.0)
fig = plt.figure(); ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum())
#[Out]# [<matplotlib.lines.Line2D object at 0x0000000012655A90>]
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
#[Out]# <matplotlib.text.Text object at 0x000000001263B5F8>
ax.set_xlabel('Stages')
#[Out]# <matplotlib.text.Text object at 0x000000000C1A0898>
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum(), 'k', label='one')
#[Out]# [<matplotlib.lines.Line2D object at 0x00000000133D24A8>]
ax.plot(randn(1000).cumsum(), 'k--', label='two')
#[Out]# [<matplotlib.lines.Line2D object at 0x00000000133D6400>]
ax.plot(randn(1000).cumsum(), 'k.', label='three')
#[Out]# [<matplotlib.lines.Line2D object at 0x000000000C3D4BA8>]
ax.legend(loc='best')
#[Out]# <matplotlib.legend.Legend object at 0x00000000126272E8>
ax.text(700, -10, 'Hello World!', family='monospace', fontsize=10)
#[Out]# <matplotlib.text.Text object at 0x00000000129979B0>
from datetime import datetime
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
data = pd.read_csv('spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']
spx.plot(ax=ax, style='k')
#[Out]# <matplotlib.axes.AxesSubplot object at 0x000000001264FD68>
crisis_data = [
(datetime(2007, 10, 11), 'Peak of bull market'),
(datetime(2008, 3, 12), 'Bear Stearns Fails'),
(datetime(2008, 9, 15), 'Lehman Bankruptcy')
]
for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 50),
    xytext=(date, spx.asof(date) + 200),
    arrowprops=dict(facecolor='black'),
    horizontalalignment='left', verticalalignment='top')
ax.set_xlim(['1/1/2007', '1/1/2011'])
#[Out]# (732677.0, 734138.0)
ax.set_ylim([600, 1800])
#[Out]# (600, 1800)
ax.set_title('Important dates in 2008-2009 financial crisis')
#[Out]# <matplotlib.text.Text object at 0x00000000133E7FD0>
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([0.15, 0.15], [0.35, 0.4]), [0.2, 0.6]], color='g', alpha=0.5)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4]), [0.2, 0.6]], color='g', alpha=0.5)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax.add_patch(rect)
#[Out]# <matplotlib.patches.Rectangle object at 0x000000001373F320>
ax.add_patch(circ)
#[Out]# <matplotlib.patches.Circle object at 0x000000000C1728D0>
ax.add_patch(pgon)
#[Out]# <matplotlib.patches.Polygon object at 0x000000000C191748>
plt.savefig('figs/shapes.svg')
plt.savefig('figs/shapes.png', dpi=400, bbox_inches='tight')
from io import StringIO
buffer = StringIO()
plt.savefig(buffer)
ax = fig.add_subplot(1, 1, 1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.add_patch(rect)
#[Out]# <matplotlib.patches.Rectangle object at 0x000000001373F320>
ax.add_patch(circ)
#[Out]# <matplotlib.patches.Circle object at 0x000000000C1728D0>
ax.add_patch(pgon)
#[Out]# <matplotlib.patches.Polygon object at 0x000000000C191748>
plt.savefig(buffer)
buffer = StringIO()
plt.savefig(buffer)
plt.savefig(buffer)
plt.rc('figure', figsize=(10, 10))
font_options = {'family': 'monospace',
'weight': 'bold',
'size': 'small'}
plt.rc('font', **font_options)
s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
#[Out]# <matplotlib.axes.AxesSubplot object at 0x00000000129ADBA8>
s.plot()
#[Out]# <matplotlib.axes.AxesSubplot object at 0x0000000013DAB9B0>
df = DataFrame(np.random.randn(10, 4).cumsum(),
columns=['A', 'B', 'C', 'D'],
index=np.arange(0, 100, 10))
df = DataFrame(np.random.randn(10, 4).cumsum(0),
columns=['A', 'B', 'C', 'D'],
index=np.arange(0, 100, 10))
df.plot()
#[Out]# <matplotlib.axes.AxesSubplot object at 0x0000000013B3BB38>
pwd
#[Out]# u'C:\\Users\\millerdr\\Google Drive\\Python for Data Analysis\\pydata-book\\ch08'
%logstart -o -r -t pandas_ch08_log.py append
%logstop
# Tue, 08 Jul 2014 23:44:26
fig, axes = plt.subplots(2, 1)
# Tue, 08 Jul 2014 23:45:16
data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))
# Tue, 08 Jul 2014 23:45:42
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
#[Out]# <matplotlib.axes.AxesSubplot at 0x13734b70>
# Tue, 08 Jul 2014 23:46:36
data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
#[Out]# <matplotlib.axes.AxesSubplot at 0x14078390>
# Tue, 08 Jul 2014 23:48:46
df = DataFrame(np.random.rand(6, 4),
index=['one', 'two', 'three', 'four', 'five', 'six'],
columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
# Tue, 08 Jul 2014 23:48:49
df
#[Out]# Genus         A         B         C         D
#[Out]# one    0.625339  0.443034  0.915870  0.269553
#[Out]# two    0.660908  0.381452  0.704113  0.793592
#[Out]# three  0.184232  0.124493  0.719687  0.646947
#[Out]# four   0.020887  0.550337  0.158771  0.184804
#[Out]# five   0.450322  0.274612  0.626289  0.250693
#[Out]# six    0.077707  0.961181  0.183830  0.190275
#[Out]# 
#[Out]# [6 rows x 4 columns]
# Tue, 08 Jul 2014 23:49:03
df.plot(kind='bar')
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b0a4048>
# Tue, 08 Jul 2014 23:50:45
df.plot(kind='barh', stacked=True, alpha=0.5)
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b21e160>
# Tue, 08 Jul 2014 23:52:09
tips = pd.read_csv('tips.csv')
# Tue, 08 Jul 2014 23:52:27
party_counts = pd.crosstab(tips.day, tips.size)
# Tue, 08 Jul 2014 23:52:31
party_counts
#[Out]# size  1   2   3   4  5  6
#[Out]# day                      
#[Out]# Fri   1  16   1   1  0  0
#[Out]# Sat   2  53  18  13  1  0
#[Out]# Sun   0  39  15  18  3  1
#[Out]# Thur  1  48   4   5  1  3
#[Out]# 
#[Out]# [4 rows x 6 columns]
# Tue, 08 Jul 2014 23:55:14
party_counts = party_counts.ix[:, 2:5]
# Tue, 08 Jul 2014 23:55:17
party_counts
#[Out]# size   2   3   4  5
#[Out]# day                
#[Out]# Fri   16   1   1  0
#[Out]# Sat   53  18  13  1
#[Out]# Sun   39  15  18  3
#[Out]# Thur  48   4   5  1
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Tue, 08 Jul 2014 23:56:13
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
# Tue, 08 Jul 2014 23:56:19
party_pcts
#[Out]# size         2         3         4         5
#[Out]# day                                         
#[Out]# Fri   0.888889  0.055556  0.055556  0.000000
#[Out]# Sat   0.623529  0.211765  0.152941  0.011765
#[Out]# Sun   0.520000  0.200000  0.240000  0.040000
#[Out]# Thur  0.827586  0.068966  0.086207  0.017241
#[Out]# 
#[Out]# [4 rows x 4 columns]
# Tue, 08 Jul 2014 23:57:27
party_pcts.plot(kind='bar', stacked=True)
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b09a9b0>
# Tue, 08 Jul 2014 23:58:08
plt.savefig('figs/tips_stacked_bar.png')
# Wed, 09 Jul 2014 00:00:29
tips['tip_pct'] = tips['tip'] / tips['total_bill']
# Wed, 09 Jul 2014 00:00:45
tips['tip_pct'].hist(bins=50)
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b7cbac8>
# Wed, 09 Jul 2014 00:01:09
plt.savefig('figs/tips_hist.png')
# Wed, 09 Jul 2014 00:02:38
tips['tip_pct'].plot(kind='kde')
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b7e6208>
# Wed, 09 Jul 2014 00:03:40
plt.savefig('figs/tips_kde.png')
# Wed, 09 Jul 2014 00:05:56
comp1 = np.random.normal(0, 1, size=200)
# Wed, 09 Jul 2014 00:06:27
comp2 = np.random.normal(10, 2, size=200)
# Wed, 09 Jul 2014 00:06:51
values = Series(np.concatenate([comp1, comp2]))
# Wed, 09 Jul 2014 00:07:20
values.hist(bins=100, alpha=0.3, color='k', normed=True)
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b09e5f8>
# Wed, 09 Jul 2014 00:08:01
values.plot(kind='kde', style='k--')
#[Out]# <matplotlib.axes.AxesSubplot at 0x1b09e5f8>
# Wed, 09 Jul 2014 00:08:33
plt.savefig('figs/composite_hist_kde.png')
# Wed, 09 Jul 2014 00:10:41
values.hist(bins=100, alpha=0.3, color='k', normed=True)
#[Out]# <matplotlib.axes.AxesSubplot at 0x20300128>
# Wed, 09 Jul 2014 00:10:48
values.plot(kind='kde', style='k--')
#[Out]# <matplotlib.axes.AxesSubplot at 0x20300128>
# Wed, 09 Jul 2014 00:10:52
plt.savefig('figs/composite_hist_kde.png')
# Wed, 09 Jul 2014 00:12:05
macro = pd.read_csv('macrodata.csv')
# Wed, 09 Jul 2014 00:12:29
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
# Wed, 09 Jul 2014 00:12:47
trans_data = np.log(data).diff().dropna()
# Wed, 09 Jul 2014 00:13:02
trans_data[-5:]
#[Out]#           cpi        m1  tbilrate     unemp
#[Out]# 198 -0.007904  0.045361 -0.396881  0.105361
#[Out]# 199 -0.021979  0.066753 -2.277267  0.139762
#[Out]# 200  0.002340  0.010286  0.606136  0.160343
#[Out]# 201  0.008419  0.037461 -0.200671  0.127339
#[Out]# 202  0.008894  0.012202 -0.405465  0.042560
#[Out]# 
#[Out]# [5 rows x 4 columns]
# Wed, 09 Jul 2014 00:13:49
plt.scatter(trans_data['m1'], trans_data['unemp'])
#[Out]# <matplotlib.collections.PathCollection at 0x295c4860>
# Wed, 09 Jul 2014 00:14:33
plt.title('Changes in log %s vs. log %s' % ('m1', 'unemp'))
#[Out]# <matplotlib.text.Text at 0x295b7860>
# Wed, 09 Jul 2014 00:15:16
plt.savefig('figs/Changes in log v1 vs. v2.png')
# Wed, 09 Jul 2014 00:16:45
scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)
# Wed, 09 Jul 2014 00:17:00
pd.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3)
#[Out]# array([[<matplotlib.axes.AxesSubplot object at 0x00000000295AFF60>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x00000000297C40B8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029771898>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x000000002978B978>],
#[Out]#        [<matplotlib.axes.AxesSubplot object at 0x00000000299EE978>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029798EB8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029B68F60>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029B8CEF0>],
#[Out]#        [<matplotlib.axes.AxesSubplot object at 0x0000000029CEF828>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029D0F9E8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029D1E898>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029E8E668>],
#[Out]#        [<matplotlib.axes.AxesSubplot object at 0x000000002A0325F8>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x0000000029CF7518>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x000000002A197860>,
#[Out]#         <matplotlib.axes.AxesSubplot object at 0x000000002A1B97F0>]], dtype=object)
# Wed, 09 Jul 2014 00:17:25
plt.savefig('figs/scatter_matrix.png')
# Wed, 09 Jul 2014 00:21:02
data = pd.read_csv('Haiti.csv')
# Wed, 09 Jul 2014 00:21:06
data
# Wed, 09 Jul 2014 00:35:06
data[['INCIDENT DATE', 'LATITUDE', 'LOGITUDE']][:10]
# Wed, 09 Jul 2014 00:35:15
data[['INCIDENT DATE', 'LATITUDE', 'LONGITUDE']][:10]
#[Out]#       INCIDENT DATE   LATITUDE   LONGITUDE
#[Out]# 0  05/07/2010 17:26  18.233333  -72.533333
#[Out]# 1  28/06/2010 23:06  50.226029    5.729886
#[Out]# 2  24/06/2010 16:21  22.278381  114.174287
#[Out]# 3  20/06/2010 21:59  44.407062    8.933989
#[Out]# 4  18/05/2010 16:26  18.571084  -72.334671
#[Out]# 5  26/04/2010 13:14  18.593707  -72.310079
#[Out]# 6  26/04/2010 14:19  18.482800  -73.638800
#[Out]# 7  26/04/2010 14:27  18.415000  -73.195000
#[Out]# 8  15/03/2010 10:58  18.517443  -72.236841
#[Out]# 9  15/03/2010 11:00  18.547790  -72.410010
#[Out]# 
#[Out]# [10 rows x 3 columns]
# Wed, 09 Jul 2014 00:38:24
data.describe()
#[Out]#             Serial     LATITUDE    LONGITUDE
#[Out]# count  3593.000000  3593.000000  3593.000000
#[Out]# mean   2080.277484    18.611495   -72.322680
#[Out]# std    1171.100360     0.738572     3.650776
#[Out]# min       4.000000    18.041313   -74.452757
#[Out]# 25%    1074.000000    18.524070   -72.417500
#[Out]# 50%    2163.000000    18.539269   -72.335000
#[Out]# 75%    3088.000000    18.561820   -72.293570
#[Out]# max    4052.000000    50.226029   114.174287
#[Out]# 
#[Out]# [8 rows x 3 columns]
# Wed, 09 Jul 2014 00:38:53
data['CATEGORY'][:6]
#[Out]# 0          1. Urgences | Emergency, 3. Public Health, 
#[Out]# 1    1. Urgences | Emergency, 2. Urgences logistiqu...
#[Out]# 2    2. Urgences logistiques | Vital Lines, 8. Autr...
#[Out]# 3                            1. Urgences | Emergency, 
#[Out]# 4                            1. Urgences | Emergency, 
#[Out]# 5                       5e. Communication lines down, 
#[Out]# Name: CATEGORY, dtype: object
# Wed, 09 Jul 2014 00:41:24
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) &
(data.LONGITUDE > -75) & (data.LONGITUDE < -70) &
data.CATEGORY.notnull()]
# Wed, 09 Jul 2014 00:43:50
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]

# Wed, 09 Jul 2014 00:45:55
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))

# Wed, 09 Jul 2014 00:46:03
set?
# Wed, 09 Jul 2014 00:46:41
set.union?
# Wed, 09 Jul 2014 00:48:33
def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names = names.split(' | ')[1]
    return code, names.strip()

# Wed, 09 Jul 2014 00:49:04
get_english('2. Urgences logistiques | Vital Lines')
#[Out]# ('2', 'Vital Lines')
# Wed, 09 Jul 2014 00:50:00
all_cats = get_all_categories(data.CATEGORY)
# Wed, 09 Jul 2014 00:51:22
english_mapping = dict(get_english(x) for x in all_cats)
# Wed, 09 Jul 2014 00:51:29
english_mapping
#[Out]# {'1': 'Emergency',
#[Out]#  '1a': 'Highly vulnerable',
#[Out]#  '1b': 'Medical Emergency',
#[Out]#  '1c': 'People trapped',
#[Out]#  '1d': 'Fire',
#[Out]#  '2': 'Vital Lines',
#[Out]#  '2a': 'Food Shortage',
#[Out]#  '2b': 'Water shortage',
#[Out]#  '2c': 'Security Concern',
#[Out]#  '2d': 'Shelter needed',
#[Out]#  '2e': 'Fuel shortage',
#[Out]#  '2f': 'Power Outage',
#[Out]#  '3': 'Public Health',
#[Out]#  '3a': 'Infectious human disease',
#[Out]#  '3b': 'Chronic care needs',
#[Out]#  '3c': 'Medical equipment and supply needs',
#[Out]#  '3d': "OBGYN/Women's Health",
#[Out]#  '3e': 'Psychiatric need',
#[Out]#  '4': 'Security Threats',
#[Out]#  '4a': 'Looting',
#[Out]#  '4c': 'Group violence',
#[Out]#  '4e': 'Water sanitation and hygiene promotion',
#[Out]#  '5': 'Infrastructure Damage',
#[Out]#  '5a': 'Collapsed structure',
#[Out]#  '5b': 'Unstable Structure',
#[Out]#  '5c': 'Road blocked',
#[Out]#  '5d': 'Compromised bridge',
#[Out]#  '5e': 'Communication lines down',
#[Out]#  '6': 'Natural Hazards',
#[Out]#  '6a': 'Deaths',
#[Out]#  '6b': 'Missing Persons',
#[Out]#  '6c': 'Earthquake and aftershocks',
#[Out]#  '7': 'Services Available',
#[Out]#  '7a': 'Food distribution point',
#[Out]#  '7b': 'Water distribution point',
#[Out]#  '7c': 'Non-food aid distribution point',
#[Out]#  '7d': 'Hospital/Clinics Operating',
#[Out]#  '7g': 'Human remains management',
#[Out]#  '7h': 'Rubble removal',
#[Out]#  '8': 'Other',
#[Out]#  '8a': 'IDP concentration',
#[Out]#  '8c': 'Price gouging',
#[Out]#  '8d': 'Search and Rescue',
#[Out]#  '8e': 'Persons News',
#[Out]#  '8f': 'Other'}
# Wed, 09 Jul 2014 00:51:48
english_mapping['2a']
#[Out]# 'Food Shortage'
# Wed, 09 Jul 2014 00:51:57
english_mapping['6c']
#[Out]# 'Earthquake and aftershocks'
# Wed, 09 Jul 2014 00:53:20
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]

# Wed, 09 Jul 2014 00:54:42
all_codes = get_code(all_cats)
# Wed, 09 Jul 2014 00:54:55
all_cats[:10]
#[Out]# ['1. Urgences | Emergency',
#[Out]#  '1a. Highly vulnerable',
#[Out]#  '1b. Urgence medicale | Medical Emergency',
#[Out]#  '1c. Personnes prises au piege | People trapped',
#[Out]#  '1d. Incendie | Fire',
#[Out]#  '2. Urgences logistiques | Vital Lines',
#[Out]#  "2a. Penurie d'aliments | Food Shortage",
#[Out]#  "2b. Penurie d'eau | Water shortage",
#[Out]#  '2c. Eau contaminee | Contaminated water',
#[Out]#  '2c. Probleme de securite | Security Concern']
# Wed, 09 Jul 2014 00:55:20
all_codes
#[Out]# ['1',
#[Out]#  '1a',
#[Out]#  '1b',
#[Out]#  '1c',
#[Out]#  '1d',
#[Out]#  '2',
#[Out]#  '2a',
#[Out]#  '2b',
#[Out]#  '2c',
#[Out]#  '2c',
#[Out]#  '2d',
#[Out]#  '2e',
#[Out]#  '2f',
#[Out]#  '3',
#[Out]#  '3a',
#[Out]#  '3b',
#[Out]#  '3c',
#[Out]#  '3d',
#[Out]#  '3e',
#[Out]#  '4',
#[Out]#  '4a',
#[Out]#  '4c',
#[Out]#  '4e',
#[Out]#  '5',
#[Out]#  '5a',
#[Out]#  '5b',
#[Out]#  '5c',
#[Out]#  '5d',
#[Out]#  '5e',
#[Out]#  '6',
#[Out]#  '6a',
#[Out]#  '6b',
#[Out]#  '6c',
#[Out]#  '6c',
#[Out]#  '7',
#[Out]#  '7a',
#[Out]#  '7b',
#[Out]#  '7c',
#[Out]#  '7d',
#[Out]#  '7g',
#[Out]#  '7h',
#[Out]#  '8',
#[Out]#  '8a',
#[Out]#  '8c',
#[Out]#  '8d',
#[Out]#  '8e',
#[Out]#  '8f']
# Wed, 09 Jul 2014 00:56:03
code_index = pd.Index(np.unique(all_codes))
# Wed, 09 Jul 2014 00:56:10
code_index
#[Out]# Index([u'1', u'1a', u'1b', u'1c', u'1d', u'2', u'2a', u'2b', u'2c', u'2d', u'2e', u'2f', u'3', u'3a', u'3b', u'3c', u'3d', u'3e', u'4', u'4a', u'4c', u'4e', u'5', u'5a', u'5b', u'5c', u'5d', u'5e', u'6', u'6a', u'6b', u'6c', u'7', u'7a', u'7b', u'7c', u'7d', u'7g', u'7h', u'8', u'8a', u'8c', u'8d', u'8e', u'8f'], dtype='object')
# Wed, 09 Jul 2014 00:56:59
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))),
index=data.index, columns=code_index)
# Wed, 09 Jul 2014 00:57:09
dummy_frame
#[Out]#     1  1a  1b  1c  1d  2  2a  2b  2c  2d  2e  2f  3  3a  3b  3c  3d  3e  4  \
#[Out]# 0   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 4   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 5   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 6   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 7   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 8   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 9   0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 10  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 11  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 12  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 13  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 14  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 15  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 16  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 17  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 18  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 19  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 20  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 21  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 22  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 23  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 24  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 25  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 26  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 27  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 28  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 29  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 30  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 31  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 32  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 33  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 34  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 35  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 36  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 37  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 38  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 39  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 40  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 41  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 42  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 43  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 44  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 45  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 46  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 47  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 48  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 49  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 50  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 51  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 52  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 53  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 54  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 55  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 56  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 57  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 58  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 59  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 60  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 61  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]# 62  0   0   0   0   0  0   0   0   0   0   0   0  0   0   0   0   0   0  0   
#[Out]#    .. ... ... ... ... .. ... ... ... ... ... ... .. ... ... ... ... ... ..   
#[Out]# 
#[Out]#     4a      
#[Out]# 0    0 ...  
#[Out]# 4    0 ...  
#[Out]# 5    0 ...  
#[Out]# 6    0 ...  
#[Out]# 7    0 ...  
#[Out]# 8    0 ...  
#[Out]# 9    0 ...  
#[Out]# 10   0 ...  
#[Out]# 11   0 ...  
#[Out]# 12   0 ...  
#[Out]# 13   0 ...  
#[Out]# 14   0 ...  
#[Out]# 15   0 ...  
#[Out]# 16   0 ...  
#[Out]# 17   0 ...  
#[Out]# 18   0 ...  
#[Out]# 19   0 ...  
#[Out]# 20   0 ...  
#[Out]# 21   0 ...  
#[Out]# 22   0 ...  
#[Out]# 23   0 ...  
#[Out]# 24   0 ...  
#[Out]# 25   0 ...  
#[Out]# 26   0 ...  
#[Out]# 27   0 ...  
#[Out]# 28   0 ...  
#[Out]# 29   0 ...  
#[Out]# 30   0 ...  
#[Out]# 31   0 ...  
#[Out]# 32   0 ...  
#[Out]# 33   0 ...  
#[Out]# 34   0 ...  
#[Out]# 35   0 ...  
#[Out]# 36   0 ...  
#[Out]# 37   0 ...  
#[Out]# 38   0 ...  
#[Out]# 39   0 ...  
#[Out]# 40   0 ...  
#[Out]# 41   0 ...  
#[Out]# 42   0 ...  
#[Out]# 43   0 ...  
#[Out]# 44   0 ...  
#[Out]# 45   0 ...  
#[Out]# 46   0 ...  
#[Out]# 47   0 ...  
#[Out]# 48   0 ...  
#[Out]# 49   0 ...  
#[Out]# 50   0 ...  
#[Out]# 51   0 ...  
#[Out]# 52   0 ...  
#[Out]# 53   0 ...  
#[Out]# 54   0 ...  
#[Out]# 55   0 ...  
#[Out]# 56   0 ...  
#[Out]# 57   0 ...  
#[Out]# 58   0 ...  
#[Out]# 59   0 ...  
#[Out]# 60   0 ...  
#[Out]# 61   0 ...  
#[Out]# 62   0 ...  
#[Out]#    ...      
#[Out]# 
#[Out]# [3569 rows x 45 columns]
# Wed, 09 Jul 2014 00:58:00
dummy_frame.ix[:, :6]
#[Out]#     1  1a  1b  1c  1d  2
#[Out]# 0   0   0   0   0   0  0
#[Out]# 4   0   0   0   0   0  0
#[Out]# 5   0   0   0   0   0  0
#[Out]# 6   0   0   0   0   0  0
#[Out]# 7   0   0   0   0   0  0
#[Out]# 8   0   0   0   0   0  0
#[Out]# 9   0   0   0   0   0  0
#[Out]# 10  0   0   0   0   0  0
#[Out]# 11  0   0   0   0   0  0
#[Out]# 12  0   0   0   0   0  0
#[Out]# 13  0   0   0   0   0  0
#[Out]# 14  0   0   0   0   0  0
#[Out]# 15  0   0   0   0   0  0
#[Out]# 16  0   0   0   0   0  0
#[Out]# 17  0   0   0   0   0  0
#[Out]# 18  0   0   0   0   0  0
#[Out]# 19  0   0   0   0   0  0
#[Out]# 20  0   0   0   0   0  0
#[Out]# 21  0   0   0   0   0  0
#[Out]# 22  0   0   0   0   0  0
#[Out]# 23  0   0   0   0   0  0
#[Out]# 24  0   0   0   0   0  0
#[Out]# 25  0   0   0   0   0  0
#[Out]# 26  0   0   0   0   0  0
#[Out]# 27  0   0   0   0   0  0
#[Out]# 28  0   0   0   0   0  0
#[Out]# 29  0   0   0   0   0  0
#[Out]# 30  0   0   0   0   0  0
#[Out]# 31  0   0   0   0   0  0
#[Out]# 32  0   0   0   0   0  0
#[Out]# 33  0   0   0   0   0  0
#[Out]# 34  0   0   0   0   0  0
#[Out]# 35  0   0   0   0   0  0
#[Out]# 36  0   0   0   0   0  0
#[Out]# 37  0   0   0   0   0  0
#[Out]# 38  0   0   0   0   0  0
#[Out]# 39  0   0   0   0   0  0
#[Out]# 40  0   0   0   0   0  0
#[Out]# 41  0   0   0   0   0  0
#[Out]# 42  0   0   0   0   0  0
#[Out]# 43  0   0   0   0   0  0
#[Out]# 44  0   0   0   0   0  0
#[Out]# 45  0   0   0   0   0  0
#[Out]# 46  0   0   0   0   0  0
#[Out]# 47  0   0   0   0   0  0
#[Out]# 48  0   0   0   0   0  0
#[Out]# 49  0   0   0   0   0  0
#[Out]# 50  0   0   0   0   0  0
#[Out]# 51  0   0   0   0   0  0
#[Out]# 52  0   0   0   0   0  0
#[Out]# 53  0   0   0   0   0  0
#[Out]# 54  0   0   0   0   0  0
#[Out]# 55  0   0   0   0   0  0
#[Out]# 56  0   0   0   0   0  0
#[Out]# 57  0   0   0   0   0  0
#[Out]# 58  0   0   0   0   0  0
#[Out]# 59  0   0   0   0   0  0
#[Out]# 60  0   0   0   0   0  0
#[Out]# 61  0   0   0   0   0  0
#[Out]# 62  0   0   0   0   0  0
#[Out]#    .. ... ... ... ... ..
#[Out]# 
#[Out]# [3569 rows x 6 columns]
# Wed, 09 Jul 2014 01:00:41
for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes] = 1
    
# Wed, 09 Jul 2014 01:01:14
data = data.join(dummy_frame.add_prefix('category_'))
# Wed, 09 Jul 2014 01:01:33
data.ix[:, 10:15]
#[Out]#     category_1  category_1a  category_1b  category_1c  category_1d
#[Out]# 0            1            0            0            0            0
#[Out]# 4            1            0            0            0            0
#[Out]# 5            0            0            0            0            0
#[Out]# 6            0            0            0            0            0
#[Out]# 7            0            0            0            0            0
#[Out]# 8            0            0            0            0            0
#[Out]# 9            0            0            0            0            0
#[Out]# 10           0            1            0            0            0
#[Out]# 11           0            0            0            0            0
#[Out]# 12           0            0            0            0            0
#[Out]# 13           0            0            0            0            0
#[Out]# 14           0            0            0            0            0
#[Out]# 15           0            0            0            0            0
#[Out]# 16           1            0            0            0            0
#[Out]# 17           0            0            0            0            0
#[Out]# 18           0            0            0            0            0
#[Out]# 19           1            0            0            0            0
#[Out]# 20           1            0            0            0            0
#[Out]# 21           0            0            0            0            0
#[Out]# 22           0            0            0            0            0
#[Out]# 23           0            0            0            0            0
#[Out]# 24           0            0            0            0            0
#[Out]# 25           0            0            1            0            0
#[Out]# 26           0            0            0            0            0
#[Out]# 27           0            0            0            0            0
#[Out]# 28           0            0            0            0            0
#[Out]# 29           0            0            0            0            0
#[Out]# 30           0            0            0            0            0
#[Out]# 31           0            0            0            0            0
#[Out]# 32           0            0            0            0            0
#[Out]# 33           0            0            0            0            0
#[Out]# 34           0            0            0            0            0
#[Out]# 35           0            0            0            0            0
#[Out]# 36           0            0            0            0            0
#[Out]# 37           0            0            0            0            0
#[Out]# 38           0            0            0            0            0
#[Out]# 39           0            0            0            0            0
#[Out]# 40           0            0            0            0            0
#[Out]# 41           0            0            0            0            0
#[Out]# 42           1            0            1            0            1
#[Out]# 43           0            0            0            0            0
#[Out]# 44           1            0            1            0            1
#[Out]# 45           0            0            0            0            0
#[Out]# 46           0            0            0            0            0
#[Out]# 47           0            0            0            0            0
#[Out]# 48           0            0            0            0            0
#[Out]# 49           0            0            0            0            0
#[Out]# 50           0            0            0            0            0
#[Out]# 51           0            0            0            0            0
#[Out]# 52           0            0            0            0            0
#[Out]# 53           0            0            0            0            0
#[Out]# 54           0            0            0            0            0
#[Out]# 55           0            0            0            0            0
#[Out]# 56           0            0            0            0            0
#[Out]# 57           0            0            0            0            0
#[Out]# 58           0            0            0            0            0
#[Out]# 59           0            0            0            0            0
#[Out]# 60           0            0            0            0            0
#[Out]# 61           0            0            0            0            0
#[Out]# 62           0            0            0            0            0
#[Out]#            ...          ...          ...          ...          ...
#[Out]# 
#[Out]# [3569 rows x 5 columns]
# Wed, 09 Jul 2014 01:02:12
data.describe()
#[Out]#             Serial     LATITUDE    LONGITUDE   category_1  category_1a  \
#[Out]# count  3569.000000  3569.000000  3569.000000  3569.000000  3569.000000   
#[Out]# mean   2081.498459    18.592503   -72.424994     0.097506     0.000560   
#[Out]# std    1170.311824     0.273695     0.291018     0.296688     0.023669   
#[Out]# min       4.000000    18.041313   -74.452757     0.000000     0.000000   
#[Out]# 25%    1074.000000    18.524200   -72.417498     0.000000     0.000000   
#[Out]# 50%    2166.000000    18.539269   -72.335000     0.000000     0.000000   
#[Out]# 75%    3089.000000    18.561800   -72.293939     0.000000     0.000000   
#[Out]# max    4052.000000    19.940630   -71.099489     1.000000     1.000000   
#[Out]# 
#[Out]#        category_1b  category_1c  category_1d   category_2  category_2a  \
#[Out]# count  3569.000000  3569.000000  3569.000000  3569.000000  3569.000000   
#[Out]# mean      0.058280     0.046792     0.001961     0.137854     0.447184   
#[Out]# std       0.234304     0.211222     0.044250     0.344795     0.497272   
#[Out]# min       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 25%       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 50%       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 75%       0.000000     0.000000     0.000000     0.000000     1.000000   
#[Out]# max       1.000000     1.000000     1.000000     1.000000     1.000000   
#[Out]# 
#[Out]#        category_2b  category_2c  category_2d  category_2e  category_2f  \
#[Out]# count  3569.000000  3569.000000  3569.000000  3569.000000  3569.000000   
#[Out]# mean      0.372934     0.005884     0.133651     0.005884     0.009526   
#[Out]# std       0.483652     0.076492     0.340325     0.076492     0.097151   
#[Out]# min       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 25%       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 50%       0.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# 75%       1.000000     0.000000     0.000000     0.000000     0.000000   
#[Out]# max       1.000000     1.000000     1.000000     1.000000     1.000000   
#[Out]# 
#[Out]#         category_3  category_3a  category_3b  category_3c  category_3d      
#[Out]# count  3569.000000  3569.000000  3569.000000  3569.000000  3569.000000 ...  
#[Out]# mean      0.005043     0.002522     0.000560     0.085178     0.001961 ...  
#[Out]# std       0.070848     0.050160     0.023669     0.279185     0.044250 ...  
#[Out]# min       0.000000     0.000000     0.000000     0.000000     0.000000 ...  
#[Out]# 25%       0.000000     0.000000     0.000000     0.000000     0.000000 ...  
#[Out]# 50%       0.000000     0.000000     0.000000     0.000000     0.000000 ...  
#[Out]# 75%       0.000000     0.000000     0.000000     0.000000     0.000000 ...  
#[Out]# max       1.000000     1.000000     1.000000     1.000000     1.000000 ...  
#[Out]# 
#[Out]# [8 rows x 48 columns]
# Wed, 09 Jul 2014 01:03:43
from mpl_toolkits.basemap import Basemap
# Wed, 09 Jul 2014 01:11:58
from basemap import Basemap
# Wed, 09 Jul 2014 01:20:46
exit
%logstart -o -r -t pandas_ch08_log.py append
cd ..\\..
cd "Google Drive\\Python for Data Analysis\\pydata-book\\ch08"
ls
%logstop
# Wed, 09 Jul 2014 01:33:08
ls
# Wed, 09 Jul 2014 01:33:40
from basemap import Basemap
# Wed, 09 Jul 2014 01:33:53
import basemap
# Wed, 09 Jul 2014 01:34:38
from mtl_toolkits.basemap install Basemap
# Wed, 09 Jul 2014 01:34:47
from mtl_toolkits.basemap import Basemap
# Wed, 09 Jul 2014 01:35:10
from mpl_toolkits.basemap import Basemap
# Wed, 09 Jul 2014 01:35:48
data = pd.read_csv('Haiti.csv')
# Wed, 09 Jul 2014 01:36:00
import pandas as pd
# Wed, 09 Jul 2014 01:36:17
import numpy as np
# Wed, 09 Jul 2014 01:36:29
import matplotlib.pyplot as plt
# Wed, 09 Jul 2014 01:36:45
from pandas import Series, DataFrame
# Wed, 09 Jul 2014 01:36:53
data = pd.read_csv('Haiti.csv')
# Wed, 09 Jul 2014 01:37:35
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) &
(data.LONGITUDE > -75) & (data.LONGITUDE < -70) &
data.CATEGORY.notnull()]
# Wed, 09 Jul 2014 01:38:06
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]

# Wed, 09 Jul 2014 01:38:33
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))

# Wed, 09 Jul 2014 01:39:13
def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names = names.split(' | ')[1]
    return code, names.strip()

# Wed, 09 Jul 2014 01:39:22
all_cats = get_all_categories(data.CATEGORY)
# Wed, 09 Jul 2014 01:39:28
english_mapping = dict(get_english(x) for x in all_cats)
# Wed, 09 Jul 2014 01:39:48
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]

# Wed, 09 Jul 2014 01:39:55
all_codes = get_code(all_cats)
# Wed, 09 Jul 2014 01:40:08
code_index = pd.Index(np.unique(all_codes))
# Wed, 09 Jul 2014 01:40:22
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))),
index=data.index, columns=code_index)
# Wed, 09 Jul 2014 01:40:59
for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row, codes] = 1
    
# Wed, 09 Jul 2014 01:41:09
data = data.join(dummy_frame.add_prefix('category_'))
# Wed, 09 Jul 2014 01:44:52
def basic_haiti_map(ax=None, lllat=17.25, urlat=20.25,
lllon=-75, urlon=-71):
    # create polar stereographic Basemap instance.
    m = Basemap(ax=ax, projection='stere',
    lon_0=(urlon + lllon) / 2,
    lat_0=(urlat + lllat) / 2,
    llcrnrlat=lllat, urcrnrlat=urlat,
    llcrnrlon=lllon, urcrnrlon=urlon,
    resolution='f')
    # draw coastlines, state and country boundaries, edge of map.
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m

# Wed, 09 Jul 2014 01:46:47
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
# Wed, 09 Jul 2014 01:47:03
%pylab
# Wed, 09 Jul 2014 01:47:26
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
# Wed, 09 Jul 2014 01:48:01
fig.subplots_adjust(hspace=0.05, wspace=0.05)
# Wed, 09 Jul 2014 01:48:30
to_plot = ['2a', '1', '3c', '7a']
# Wed, 09 Jul 2014 01:48:57
lllat=17.25; urlat=20.25; lllon=-75; urlon=-71
# Wed, 09 Jul 2014 01:52:35
for code, ax in zip(to_plot, axes.flat):
    m = basic_haiti_map(ax, lllat=lllat, urlat=urlat, lllon=lllon,
    urlon=urlon)
    cat_data = data[data['category_%s' % code] == 1]
    # compute map proj coordinates.
    x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
    m.plot(x, y, 'k.', alpha=0.5)
    ax.set_title('%s: %s' % (code, english_mapping[code]))
    
# Wed, 09 Jul 2014 02:00:52
for code, ax in zip(to_plot, axes.flat):
    m = basic_haiti_map(ax, lllat=lllat, urlat=urlat, lllon=lllon,
    urlon=urlon)
    cat_data = data[data['category_%s' % code] == 1]
    # compute map proj coordinates.
    x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
    m.plot(x, y, 'k.', alpha=0.5)
    ax.set_title('%s: %s' % (code, english_mapping[code]))
    
# Wed, 09 Jul 2014 02:12:16
def basic_haiti_map(ax=None, lllat=17.25, urlat=20.25,
lllon=-75, urlon=-71):
    # create polar stereographic Basemap instance.
    m = Basemap(ax=ax, projection='npstere',
    lon_0=(urlon + lllon) / 2,
    lat_0=(urlat + lllat) / 2,
    llcrnrlat=lllat, urcrnrlat=urlat,
    llcrnrlon=lllon, urcrnrlon=urlon,
    resolution='f')
    # draw coastlines, state and country boundaries, edge of map.
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    return m

# Wed, 09 Jul 2014 02:14:03
for code, ax in zip(to_plot, axes.flat):
    m = basic_haiti_map(ax, lllat=lllat, urlat=urlat, lllon=lllon,
    urlon=urlon)
    cat_data = data[data['category_%s' % code] == 1]
    # compute map proj coordinates.
    x, y = m(cat_data.LONGITUDE, cat_data.LATITUDE)
    m.plot(x, y, 'k.', alpha=0.5)
    ax.set_title('%s: %s' % (code, english_mapping[code]))
    
