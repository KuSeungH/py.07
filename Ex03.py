# ex03.py
# 파일 입출력


from unicodedata import name


path = 'ex03.txt'   # 불로오고 싶은 파일의 경로
mode = 'r'  # 읽기(r), 쓰기(W)

f = open(path, mode, encoding = 'utf-8')
data = f.read()
print(data)
f.close()

lines = data.split('\n')
print(lines)

for line in lines:
    if len(line) > 0:
        name = line.split()[0]
        age = line.split()[1]
        print('{}의 나이는 {}살입니다'.format(name, age))