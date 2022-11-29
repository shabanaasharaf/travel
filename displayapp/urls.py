from django.urls import path


from displayapp import views

urlpatterns = [

    path('',views.display,name='display')
]