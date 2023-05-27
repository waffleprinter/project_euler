from math import sqrt
from decimal import *


def get_digital_sum(n):
    return sum(int(i) for i in n.replace(".", ""))


getcontext().prec = 120
print(sum(get_digital_sum(str(Decimal(i).sqrt())[:101]) for i in range(101) if not sqrt(i).is_integer()))
