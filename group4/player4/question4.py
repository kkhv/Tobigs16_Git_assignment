# 간단한 파이썬 문제!
# 주어진 코드를 디버깅 해서 오류가 없게 바꿔 주세요!

def question():
    # 문제 : 투빅이는 삼겹살이 먹고 싶어요... 먹고싶은 음식 딕셔너리에 '삼겹살'을 추가해 주세요 가격은 상관 없습니다!

    wish_food_price = {"황금올리브":18000, "연어초밥":15000}

    wish_food_price["삼겹살"] = "10000"
    
    assert '삼겹살' in wish_food_price.keys() # 삼겹살이 있는지 측정합니다. 이 줄은 수정하지 말아 주세요!
