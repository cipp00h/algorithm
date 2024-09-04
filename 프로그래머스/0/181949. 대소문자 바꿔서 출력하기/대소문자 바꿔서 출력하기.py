str = input()
result = ''.join([s.lower() if s.isupper() else s.upper() for s in str])
print(result)