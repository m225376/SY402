
# !usr/bin/python

import os
import hashlib
from datetime import datetime
import filecmp

major = []

for root,dirs,files in os.walk('.',topdown=True):
    
    for name in files:
        lists = []
        string = 'FILE'
        lists.append(string)
        x = os.path.join(root, name)
        lists.append(x)
        x = x.encode()
        new = hashlib.sha256(x)
        new = new.hexdigest()
        lists.append(new)
        t = datetime.now()
        lists.append(str(t))
        b = ''
        lists.append('\n')
        for e in lists:
            b=b+e+':'
        major.append(b)

    for name in dirs:
        if name == 'dev':
            continue
        elif name == 'proc':
            continue
        elif name == 'run':
            continue
        elif name == 'sys':
            continue
        elif name == 'tmp':
            continue
        else:
            lists = []
            string = 'DIR'
            lists.append(string)
            x = (os.path.join(root, name))
            lists.append(x)
            x = x.encode()
            new = hashlib.sha256(x)
            new = new.hexdigest()
            lists.append(new)
            t = datetime.now()
            lists.append(str(t))
            b = ''
            lists.append('\n')
            for e in lists:
                b=b+e+':'
            major.append(b)


if not os.path.exists('hashlist.txt'):

    with open('hashlist.txt', 'w') as f:
        f.writelines(major)
        f.close()
else:

    with open('hashlist_2.txt','w') as g:
        g.writelines(major)
        g.close()

if os.path.exists('hashlist_2.txt'):
    with open('hashlist.txt', 'r') as c:
        with open('hashlist_2.txt','r') as v:
            result = filecmp.cmp('hashlist.txt','hashlist_2.txt')
            if result == True:
                print('NO DISCREPANCY')
            else:
                print('DISCREPANCY....STAND BY FOR RESULTS....:')
            
            first = c.readlines()
            second = v.readlines()

            for e in first:
                e=e[:-29]
            for i in second:
                i=i[:-29]
            for r in first:
                if r not in second:
                    print(r)







