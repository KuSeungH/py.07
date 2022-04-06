# quz1.py

# 1) 한국배우목록.txt 파일을 불러오세요
# f = open(fileName, mode, bufferSize, encoding)


f = open('한국배우 목록.txt', 'r', 1024, 'utf-8')

# 2) 각 줄마다 배우의 이름이 저장되어 있습니다
#    각 배우의 이름을 리스트에 저장하세요
# f.read()      파일 내용을 통째로 하나의 문자열로 가져오기
# f.readline()  여러 줄로 구분한 상태에서 한줄만 가져오기
# f.readlines() 여러 줄로 구분된 상태에서 전체를 가져오기
'''
data = f.read()
print(data)
print(type(data))
'''
'''
while True:
    data = f.readline()
    print(data)
    if data == '':
        break
'''
'''
data = f.readlines()
for i in range(len(data)):
    name = data[i]
    data[i] = name.rstrip('\n')
print(data)
print(type(data))
'''
actorList = f.read().split('\n')

f.close()
# 3) 리스트에 저장된 이름을 기준으로 정렬을 수행하세요
actorList.sort()
print(actorList)
print(type(actorList))


# 4) 사용자에게 입력받아서 배우 목록에 검색한 이름이 있는지 확인하세요
#    만약, 검색결과가 있으면 몇번째에 위치하는지 index와 이름을 출력하세요
#    검색결과가 없다면, 결과가 없습니다 라는 문자열을 출력하세요

search = input('검색할 배우의 이름 입력 : ')

# 검색결과가 리스트에 있는지 확인하는 방법들
# print(search in actorList)
# print(actorList.index(search))
    
if search in actorList:                 # 만약 리스트에 있으면
    index = actorList.index(search)     # 몇번째에 위치하는지 찾기
    name = actorList[index]             # index 로 값 가져오기
    print('[{}] 베우는 [{}]번째에 있습니다'.format(name, index + 1))
    
else:
    print('[{}] 는 목록에 없습니다'.format(search))
    