"""
struct используется для упаковывания и распаковывания двоичных данных
"""

import struct
data = struct.pack('>i4shf', 2, b'spam', 3, 1.234)  # '>i4shf' строка формата опр. прямой порядок следования байтов
print(data)
with open('data.bin', 'wb') as f:
    f.write(data)

with open('data.bin', 'rb') as f:
    data = f.read()

values = struct.unpack('>i4shf', data)
print(values)

