# quiz2.py
# 여러분이 파일을 생성해서, 전화번호부를 기록하는 내용을 작성하세요
# 이름과 전화번호는 한 줄에 작성되어야 하며, 둘을 구분하기 위해서 , 를 사용합니다
# 전화번호는 -를 포합한 형태로 작성되어야 합니다
# 처음 실행할 때 파일에서 데이터를 불러오고
# 종료하기 직전 리스트를 파일에 저장하면 됩니다
# 목록은 파일이 아니라, 프로그램상의 라스트를 출력하면 됩니다

def load():
    f = open('phoneBook.txt', 'a')    # 만약 파일이 없으면 만들어주는 코드
    f.close()                         # 만약 파일이 있다면 열었다가 닫으니 변화 없음

    f = open('phoneBook.txt', 'r', 1024, 'utf-8')
    dataList = f.read().split('\n')
    f.close()
    
    dataList.pop()  # 마지막 줄 내용에 '' 이 들어가있어서 없애줌
    return dataList

def save(dataList):
    f = open('phoneBook', 'w', 1024, 'utf-8')
    lines = ''
    for data in dataList:
        lines += data + '\n'
    f.write(lines)
    f.close()
    
### 위에는 함수 선언하는 부분 

dataList = load()

while True:
    print('1. 목록 ㅣ 2. 추가 ㅣ 0. 종료')
    menu = input('메뉴입력 >>> ')
    if menu == '1':
        for data in dataList:                   # data = '이지은,010-1234-1234'
            name = data.split(',')[0]           # ,로 구분하여 0번째 문자열
            phoneNumber = data.split(',')[1]    # ,로 구분하여 0번째 문자열
            print('{} : {}'.format(name, phoneNumber))
        
    elif menu == '2':
        name = input('이름 입력 : ')
        phoneNumber = input('전화번호 입력 : ')
        data = name + ',' + phoneNumber
        dataList.append(data)
        
    elif menu == '0':
        save(dataList)
        break
    
    print()