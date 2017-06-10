print 'Python', python_version()
print 'Hello, World!'        #python 2 version doesnt contain paranthesis for print function

Python 2.7.6
Hello, World!                #Result of python 2 version
Hello, World!

print('Python', python_version())
print('Hello, World!')       #python 3 requires paranthesis for print function otherwise it throws syntax error

Python 3.4.1
Hello, World!                #Result of python 3 version

print 'Python', python_version()
print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)    #Typeerror cannot be informed to user as warning if try to compare unorderable types

Python 2.7.6
[1, 2] > 'foo' =  False                     #Result of unorderable type comparison
(1, 2) > 'foo' =  True
[1, 2] > (1, 2) =  False

print('Python', python_version())             #Typeerror would be informed to user if try to compare unorderable types
print("[1, 2] > 'foo' = ", [1, 2] > 'foo')
print("(1, 2) > 'foo' = ", (1, 2) > 'foo')
print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))

print type(unicode('this is like a python3 str type'))
<type 'unicode'>                          #Python 2 has ASCII str() types, separate unicode(), but no byte type
print type(b'byte type does not exist')    #Result of Python 2
<type 'str'>

print('Python', python_version())
print('strings are now utf-8 \u03BCnico\u0394é!')   #python 3 now contains unicode 

Python 3.4.1
strings are now utf-8 μnicoΔé!         #In Python 3, we finally have Unicode (utf-8) strings, and 2 byte classes: byte and bytearrays.
Python 3.4.1
strings are now utf-8 μnicoΔé!
print('Python', python_version(), end="")
print(' has', type(b' bytes for storing data'))
Python 3.4.1 has <class 'bytes'>
print('and Python', python_version(), end="")
print(' also has', type(bytearray(b'bytearrays')))        #Result as bytearray and byte as different classes
and Python 3.4.1 also has <class 'bytearray'>
'note that we cannot add a string' + b'bytes for data'