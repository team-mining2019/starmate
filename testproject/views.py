from django.shortcuts import render
from accounts.forms import UserForm, ProfileForm


def main(request):
    return render(request, 'main.html')

def main_from(request, user_id):
    from_user_id = user_id
    #처리에 필요한 경우의 수. -> 링크를 본인이 누름 : (이미 로그인이 되어있기에) done이 true면 바로 result로. 아니면 question_set_01로
    #                        링크를 타인이 누름 : (로그인 안되어있다고 가정) context로 from_user_id전달받고 그걸로 아이디 만들때에 넣어줘야함.
    # 내생각에는 로그인이 되었는가 여부로 판단할 수 있을듯.
    context = {'from_user_id': from_user_id}
    return render(request, 'main_from.html', context) 