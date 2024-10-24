name = "John"
print(name)
print(repr(name))
print(type(name))

data = b'abc-qwerty'
print(data)
print(repr(data))
print(type(data))

print(data.decode())

data = b"John".decode() + " Smith"
print(repr(data))
print(type(data))

symb = b"\xc2\xb1"
print(symb.decode())  # ±

yu = b"\xde"

print(len(yu))
print(yu.decode('cp1251'))  # Ю

encode_yu = "Ю".encode('cp1251')
print(encode_yu)

encode_yu = "Ю".encode('utf-16')
print(encode_yu)

decode_yu = b'\xff\xfe.\x04'
print(decode_yu.decode('utf-16'))  # Ю

unicode_yu = u"\u042e"
print(unicode_yu)  # Ю

unicode_yu2 = "\u042e"
print(unicode_yu2)  # Ю

line = "Hello, Ангелина!"
print(line)

line_bytes = line.encode("utf-8")
print(line_bytes.decode('ascii', 'ignore'))
