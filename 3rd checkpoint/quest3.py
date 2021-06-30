
from collections import Counter
d1={'a':250,'b':600,'c':140}
d2={'a':50,'b':100,'d':60}
d = Counter(d1) + Counter(d2)
print(d)