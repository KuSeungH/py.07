# ex02.py
# 클래스 맛보기



class Member:   # 클래스의 이름은 첫글자를 대문자로 작성한다
    
    # 내가 활용할 객체의 모습을 생각하면서 작성하기
   
    # 객체가 가지는 속성값을 변수로 표현
    # 모든 객체가 같은 속성값을 가지면 의미가 없다
   
    name = ''
    age = 0
    starring = ''
   
   # 객체가 가지는 가능을 함수로 표현
   # 클래스 내부의 함수는 첫번째 매개변수로 반드시 self를 가져야 한다
    def intro(self):
        text = '{}은 {}살이고, [{}]에 나오는 캐릭터입니다'
        print(text.format(self.name, self.age, self.starring))
       
    # 객체마다 서로 다른 값을 가지도록 초기화하는 특수한 함수
    def __init__(self, name, age, starring):
        # 매개변수로 전달받은 값을 자신의 변수속성에 저장한다
        self.name = name
        self.age = age
        self.starring = starring
        
        # end of class
        
m1 = Member('짱구', 8, '짱구는 못말려')
m2 = Member('단비', 7, '아따아따')
m3 = Member('코난', 10, '명탐정 코난')

memberTuple = (m1, m2, m3)

for member in memberTuple:
    member.intro()

print(type(m1))
print(type(1234))
print(type('Hello'))
