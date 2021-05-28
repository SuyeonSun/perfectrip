from django.shortcuts import redirect, render, get_object_or_404
from.models import Comment
from.models import Text
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, "home.html")

menu_bar = []  
# detail함수 : home에서 입력한 각각의 코스들이 DB의 Text Table에 있는지 조회하고 detail.html에 띄워줌
def detail(request): 
    trips=[]                                     # home.html에서 입력한 코스들을 저장할 리스트
    trips.append(request.GET['start'])           # 리스트에 출발지 추가
    trips += request.GET.getlist('middle')       # 리스트에 경유지들 추가
    trips.append(request.GET['end'])             # 리스트에 도착지 추가

    menu_bar.clear()

    for place_name in trips:                     # home에서 입력한 각 코스들에 대해 반복문 실행
        menu = []                                # menu = 각 코스의 1)'장소명'과 2)'그 장소에 대한 설명'을 담을 리스트
        menu.append(place_name)                  # 그 장소의 장소명을 추가, 이제 장소에 대한 설명만 담으면 됨.
        try:                                     # Text table에 해당 코스가 있는지 없는지 검사
            s = Text.objects.get(pk=place_name)   
        except Text.DoesNotExist:                # Text table에 해당 코스가 없으면 대체 문구로 대체
            menu.append("대체 문구")
        else:                                    # Text table에 해당 코스가 있으면 그 코스의 설명을 가져옴
            menu.append(s.summary())
        finally:
            menu_bar.append(menu)
            # menu_bar의 형태 : ex) [["출발지", "출발지에 대한 설명"], ["경유지", "경유지에 대한 설명"], ["도착지", "도착지에 대한 설명"]]
    return render(request, 'detail.html', {'trip_list' : menu_bar})


#place에 해당하는 comments들을 가져옴
def getplacedetails(request,place):  
    comments=Comment.objects.filter(place=place).order_by('-yes')   #비교
    text=Text.objects.get(pk=place)
    comment_list=list(comments)
    #comment_list.sort(key=lambda Comment: Comment.yes,reverse=True)
    return render(request, 'detail_detail.html', {'trip_list' : menu_bar, 'comment_list' : comment_list,'text' : text})  


#주의사항 더하기
def addcaution(request, place):
    comment=Comment()
    comment.author=request.POST.get('author',False)
    comment.place = Text.objects.get(pk=place)
    comment.caution=request.POST.get('caution',False)
    if request.POST.get("have-pet", False) == "yes":
        comment.pet = True
    else:
        comment.pet = False
    comment.tripType=request.POST.get("trip-type", False)
    comment.pub_date=timezone.datetime.now()
    comment.save()

    return redirect("detail_detail", place)

def yesUp(request,place): 
    text=Text.objects.get(pk=place)
    text.yes+=1
    return redirect('detail_detail.html')

def noUp(request,place):
    text=Text.objects.get(pk=place)
    text.no+=1
    return redirect('detail_detail.html')