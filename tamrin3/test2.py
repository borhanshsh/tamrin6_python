#    this code get cleaned

import re
address=input()
answer=re.findall('(+[0-9]|+[0-9]{2}|+[0-9]{3}|[0-9]{2}|[0-9]{3}|[0-9]{4})-([0-9]{2}|[0-9]{3}|[0-9]{4})-([0-9]{2}|[0-9]{3}|[0-9]{4})',address)
print(answer)