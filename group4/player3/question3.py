# 간단한 파이썬 문제!
# 주어진 코드를 디버깅 해서 오류가 없게 바꿔 주세요!

def question():
    # 문제 : 주어진 리스트에서 짝수만 추출할게요!
    original = [1,2,3,4,5,6,7,8,9]
    result = []

    for i in original:
        if i%2 == 0:
            result.append(i)
            
    return result

<<<<<<< HEAD
    return result

=======
>>>>>>> 623be541df708727827a88531eb68a8646e1e169
    assert result == [2,4,6,8] # 짝수만 추출되었는지 확인합니다. 이 줄은 수정하지 말아 주세요!
