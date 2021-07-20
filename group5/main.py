import time, json, os, sys
from player1 import question1
from player2 import question2
from player3 import question3
from player4 import question4

sys.tracebacklimit = 0 # traceback을 띄우지 않음
WAITTIME = 2
NUM_PLAYERS = len(os.listdir())

class MissonNotFinishError(Exception):
    pass

def greeting():
    print("< Tobigs 16 정규세션 오픈소스 & git >")
    time.sleep(WAITTIME)
    print("투빅스 16기 여러분들 환영합니다.")
    time.sleep(WAITTIME)
    print("여기는 정규세션 과제 월드입니다.")
    time.sleep(WAITTIME + 1) # 연출을 위해 1초 추가
    print("그리고 저는 당신의 과제 달성을 도와줄 과제 요정입니다 ^^ ")
    time.sleep(WAITTIME)
    print("여러분들이 투빅스 생활을 잘 해쳐 나갈 수 있도록 간단하게 몇 가지 파이썬 문제를 준비했습니다.")
    time.sleep(WAITTIME)
    print("과제 중 막히는 부분이 있으면 '15기 안민준'에게 언제든지 카톡 주세요~ ")
    time.sleep(WAITTIME)
    print("저와 함께 과제 제출을 위해 힘내도록 해요!")


def nameCheck():
    global players # 전역 변수 생성
    players = []
    
    for i in range(1, NUM_PLAYERS): # 플레이어 4명을 players 배열에 담슴니다.
        try:
            with open("player" + str(i) + "/profile.json", "r") as f: 
                data = json.load(f)
                if(data["닉네임"] == "[여기에 별명을 적어주세요]" or data["한마디"] == "[투빅스 16기에 임하는 각오 한 마디 적어 주세요!]"): # 모두의 파일이 작성되지 않음
                    time.sleep(WAITTIME)
                    print("우선 여러분들에 대해서 알려주세요!")
                    time.sleep(WAITTIME)
                    print("각 player폴더 안에 'profile.json' 을 작성하고 다시 와 주세요.")
                    time.sleep(WAITTIME)
                    print("파일을 작성한 뒤에는 팀장의 레포지토리에 'git commit'하는 것 잊지 마세요!")
                    time.sleep(WAITTIME)
                    print("이 파일을 실행하는 사람은 'git pull' 을 통해 모두의 파일을 다시 내려받아야 합니다!")
                    time.sleep(WAITTIME)
                    print("\n빠이빠이!")
                    time.sleep(WAITTIME+2)

                    raise MissonNotFinishError(f"profile.json 파일을 모두 작성 후 다시 찾아와주세요!")
                    
                else:
                    players.append(dict(data))
                    time.sleep(WAITTIME)
                    print(f"안녕하세요! {players[i-1]['닉네임']}님!")
        except FileNotFoundError:
            time.sleep(WAITTIME)
            print("파일에 오류가 생긴 것 같아요.. 프로젝트를 제설치하거나 profile.json을 덮어써 주세요")
            time.sleep(WAITTIME+2)
            raise MissonNotFinishError(f"player{i}/profile.json 파일이 없거나 손상되었습니다. 다른 플레이어의 파일을 참고해서 다시 생성해주세요")
            

def questionCheck(p_num, question_func):
    try:
        print(f"{players[p_num]['닉네임']}의 문제를 확인하겠습니다!\n")
        time.sleep(WAITTIME)
        question_func()
        print(f"{players[p_num]['닉네임']}의 문제는 통과되었습니다.\n")
    except:
        time.sleep(WAITTIME)
        print("아직 해결되지 않은 문제가 있습니다!")
        time.sleep(WAITTIME)
        print("각 플레이어 폴더의 question 문제를 해결하고 다시 만나겠습니다!")
        time.sleep(WAITTIME)
        print("마찬가지로 커밋, 푸시 잊지 말아 주세요!")
        time.sleep(WAITTIME)
        print("빠이빠이!")
        time.sleep(WAITTIME+2)
        raise MissonNotFinishError(f"player{p_num+1}/question{p_num+1}.py 가 해결되지 않았습니다. 해결하고 다시 찾아와 주세요!")


def question():
    time.sleep(WAITTIME)
    print("모두 복잡한 미션 잘 해내 주셨습니다!\n\n")

    time.sleep(WAITTIME)
    print("파이썬 문제를 해결해 보겠습니다!")

    time.sleep(WAITTIME)
    print("모두가 협동해서 문제를 모두 풀어 보세요.\n")

    
    # 문제 체크
    questionCheck(0, question1.question)
    questionCheck(1, question2.question)
    questionCheck(2, question3.question)
    questionCheck(3, question4.question)
    

def clear():
    time.sleep(WAITTIME)
    print("여러분의 놀라운 협동력과 실력으로 모든 과제를 통과했습니다!")
    time.sleep(WAITTIME)
    print("이 기세로 투빅스 16기 컨퍼런스 까지 파이팅입니다!")
    time.sleep(WAITTIME)
    print("마지막 커밋과 푸시, 과제 제출 잊지 마세요!")
    time.sleep(WAITTIME)
    print("고생 정말 많이 하셨습니다.")

    time.sleep(WAITTIME)
    print("빠이빠이!")

    time.sleep(WAITTIME + 2)
    print("과제 출제 - 15기 안민준")

if __name__ == "__main__":
    greeting()
    print("\n\n")
    nameCheck()
    print("\n\n")
    question()
    print("\n\n")
    clear()

