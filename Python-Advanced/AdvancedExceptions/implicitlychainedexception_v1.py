a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(1 / 0)
