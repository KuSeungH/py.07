# ex04.py
# 파일에 내용 추가하기

path = 'ex04.txt'
mode = 'a'      # r : 읽기, w : 쓰기, a : 추가(append)

f = open(path, mode, encoding='utf-8')
f.write('드디어 줄바꿈과 추가가 됩니다')
f.write('\n')
f.close()

# w 모드는 기존 내용을 모두 지우고 덮어쓴다
# a 모드는 기존 내용을 유지라고 아래에 추가한다
# write함수가 자동으로 줄을 바꾸진 않아서 \n울 추가해야한다