a = '3'
b = 5

a = int(a)
print (a + b)

c = '2.323233443'
c = float (c)
print (c + b)

#Cast de int a float y viceversa
print ('Float:', c)
print ('Float - cast a int:', int(c))
print ('Int:', b)
print ('Int - cast a float:', float(b))

# Cast a string
print ('Antes del cast')
d = 9
e = 83279.4
print (d+e)

print ('Despues del cast')
d = str (d)
e = str (e)

print (d+e)
