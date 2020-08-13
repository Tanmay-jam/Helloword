import urllib.request, urllib.parse, urllib.error
print('Hello word')
for i in range(0,3):
  print(i,i+1,i+3)
fh = urllib.request.urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')
data = fh.read().decode()
print(data)
