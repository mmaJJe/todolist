from django.test import TestCase

import datetime

now = datetime.datetime.now()

plusthree =  now + datetime.timedelta(minutes=6)

print(now)
print(plusthree)

print(now <= plusthree)
