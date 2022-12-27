from django.urls import path 
from main import views
urlpatterns = [
    path('',views.StudentCreate.as_view(),name='add'),
    path('delete/<int:id>/',views.StudentDelete.as_view(),name='delete'),
    path('update/<int:id>/',views.StudentUpdate.as_view(),name='update')

]
