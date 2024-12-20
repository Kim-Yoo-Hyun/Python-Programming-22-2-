
# 팀플 과제

from tkinter import*   # tkinter 모듈 사용
import average as test # average라는 새로운 모듈 사용 및 test로 이름 명명
import random          # random 모듈 사용


with open("score.txt", "w") as file:      # score이라는 이름의 txt파일 작성
    for i in range(5):                  # 5개의 점수 출력
        Korean=random.randrange(80, 100)  # 80~100점 사이의 점수 중 랜덤하게 출력
        Math=random.randrange(80, 100)    # 80~100점 사이의 점수 중 랜덤하게 출력
        English=random.randrange(80, 100) # 80~100점 사이의 점수 중 랜덤하게 출력
    file.write("{}, {}, {}\n" .format(Korean, Math, English)) #텍스트 작성
            
class myGrade:         # myGrade라는 class 사용
    def __init__(self):
        
        win=Tk()       # window 화면 생성
        win.title('성적 산출하기') # window 제목: 성적 산출하기
        f=Frame(win)
        f.pack()

        lblname=Label(f, text='이름')    # '이름'이라는 text로 출력
        lblname.grid(row=1, column=1)    # (1,1) 칸에 생성
        self.name=StringVar()            # string type
        entname=Entry(f, text=self.name) # 입력 할 수 있는 칸 생성
        entname.grid(row=1, column=2)    # (1,2) 칸에 생성
        
        btn=Button(f, text='성적 조회', command=self.ok) # '성적 조회'라는 text로 출력
        btn.grid(row=2, column=2)                        # (2,2)칸에 생성

    def ok(self):
        print('이름: ' +self.name.get()) #  self.name이라고 작성한 text를 get하기
        
        with open("score.txt", "r") as file:
            print("국어:{}" .format(Korean))
            print("수학:{}" .format(Math))
            print("영어:{}" .format(English))

        data=[Korean, Math, English]        # data라는 리스트 형성
        print("평균:{}".format(test.average(data)))
        
myGrade()
