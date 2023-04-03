n = str(input())

if n.endswith ('11') or n.endswith ('12') or n.endswith ('13') or n.endswith ('14'):
  print(n + ' программистов')
elif  n.endswith('1'):
  print(n + ' программист')
elif n.endswith('2') or n.endswith('3') or n.endswith('4'):
  print(n + ' программиста')
else:
  print(n + ' программистов')
  