from django.urls import path
from back import views

app_name = 'back'
urlpatterns = [

    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('delet/',views.delet,name="delet"),
    path('edit/',views.edit,name="edit"),
    # path('detail/',views.detail,name="detail"),

]