#ex05.py
# 파일입출력을 활용한 간단한 관리 프로그램



dataList = []

def load():
    f = open('ex05.txt', 'r', 1024, 'utf-8')
    lines = f.readlines()
    for line in lines:
        dataList.append(line.rstrip())  # 줄 마지막에 '\n'이 있을테니 제거
    f.close()
    
def save():
    f = open('ex05.txt', 'w', 1024, 'utf-8')
    lines = ''
    for data in dataList:
        lines += data + '\n'
    f.write(lines)
    f.close()

def show():
    print('{:=^40s}'.format('목록 출력'))
    for data in dataList:
        print(data)
    print()
    
    
load()          # 파일 데이터 불러와서
show()          # 화면에 한번 출력
data = input('추가할 데이터를 입력하세요')      # 데이터 입력받서서
dataList.append(data)                    # 리스트에 추가
show()          # 변경된 내용 한번 더 출력
save()          # 변경된 리스트를 파일에 저장