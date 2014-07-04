# IPython log file

import datetime
get_ipython().magic(u'who ')
get_ipython().magic(u'who int')
get_ipython().magic(u'logstart ')
get_ipython().magic(u'logon ')
a = 5
a
b = [1,2,3]
get_ipython().magic(u'pinfo b')
def add_numbers(a,b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b

get_ipython().magic(u'pinfo add_numbers')
get_ipython().magic(u'pinfo2 add_numbers')
import numpy as np
get_ipython().magic(u'psearch np.*load*')
import pandas as pd
get_ipython().magic(u'psearch pd.*')
pd.__version__
get_ipython().magic(u'pinfo pd.__repr__')
get_ipython().magic(u'pinfo2 pd.__repr__')
get_ipython().magic(u'pinfo2 pd.value_counts')
get_ipython().magic(u'pinfo2 pd.Series')
x = 5
x = 5
x = 5
get_ipython().magic(u'paste')
if x > 5:
x += 1
y = 8
get_ipython().magic(u'paste')
x = 5
y = 7
if x > 5:
x += 1
y = 8
get_ipython().magic(u'cpaste')
x = 5




x = 5





x = 5


get_ipython().magic(u'pinfo %logstart')
get_ipython().magic(u'logstart -o -r -t append')
get_ipython().magic(u'logstop')
import datetime
who
who int
logstart
logon
a = 5
a
#[Out]# 5
b = [1,2,3]
b?
def add_numbers(a,b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b
add_numbers?
add_numbers??
import numpy as np
np.*load*?
import pandas as pd
pd.*?
pd.__version__
#[Out]# '0.13.1'
pd.__repr__?
pd.__repr__??
pd.value_counts??
pd.Series??
x = 5
x = 5
x = 5
%paste
%paste
%cpaste
%logstart?
%logstart -o -r -t append
%logstop
%logstart -o -r -t append
a = 1
a
#[Out]# 1
%logstop
# Wed, 21 May 2014 09:08:55
ts = pd.Series(['2012-01-01', '2012-02-01'])
# Wed, 21 May 2014 09:08:56
ts
#[Out]# 0    2012-01-01
#[Out]# 1    2012-02-01
#[Out]# dtype: object
# Thu, 22 May 2014 22:42:54
%pwd
#[Out]# u'C:\\Users\\millerdr\\Documents\\Python Scripts'
# Thu, 22 May 2014 23:01:15
import numpy as np
# Thu, 22 May 2014 23:01:26
from numpy.linalg import eigvals
# Thu, 22 May 2014 23:03:02
def run_experiment(niter=100):
    K = 100
    results = []
    for _ in xrange(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

# Thu, 22 May 2014 23:03:20
some_results = run_experiment()
# Thu, 22 May 2014 23:04:03
print 'Largest one we saw: %s' % np.max(some_results)
# Thu, 22 May 2014 23:06:41
%prun -l 7 -s cumulative run_experiment()
# Thu, 22 May 2014 23:40:41
%logoff
