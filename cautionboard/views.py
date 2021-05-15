from django.shortcuts import render
from.models import Comment
from.models import Text
from django.utils import timezone
from PerfecTrip import cautionboard

# Create your views here.
def home(request):
    return render(request, "home.html")

def detail(request):
    return render(request, "detail.html")

def addcaution(request):
    comment=Comment()
    comment.author=request.POST.get('author',False)
    comment.place=request.POST.get('place',False)
    comment.caution=request.POST.get('caution',False)
    comment.id=request.POST.get('id',False)
    comment.no=request.POST.get('no',False)
    comment.yes=request.POST.get('yes',False)
    comment.pet=request.POST.get('pet',False)
    comment.tripType=request.POST.get('tripType',False)
    comment.pub_date=timezone.datetime.now()
    comment.save()
