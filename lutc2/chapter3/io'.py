from io import StringIO
import sys

buff = StringIO()
temp = sys.stdout
sys.stdout = buff
print(5)
print(buff.getvalue())
sys.stdout = temp
print(buff.getvalue())
