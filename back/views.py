from django.shortcuts import redirect, render
from back.models import Book
from django.urls import reverse

# Create your views here.
def index(request):
    book = Book.objects.all()

    return render(request,'html/index.html',{"Book":book})


def add(request):
    method = request.method
    if method == 'GET':
        return render(request,'html/add.html')
    elif method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        Book.objects.create(title=title,price=price,date=date,publish=publish)
        return redirect(reverse("back:index"))

def delet(request):
    bid = request.GET.get("bid")
    Book.objects.filter(id=bid).delete()

    return redirect(reverse("back:index"))


def edit(request):
    method = request.method
    bid = request.GET.get("bid")
    if method == 'GET':
        book = Book.objects.filter(id=bid).first()
        return render(request,'html/edit.html',{"Book":book})
    elif method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        Book.objects.filter(id=bid).update(title=title,price=price,date=date,publish=publish)
        return redirect(reverse("back:index"))


# def detail(request):
#     bid = request.GET.get("bid")
#     book = Book.objects.filter(id=bid).first()

#     return render(request,"html/detail.html",{"Book":book})

    
