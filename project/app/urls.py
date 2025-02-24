from django.urls import path
# from .import views
from app.views import Stu_List
from app.views import Stu_Details
urlpatterns = [
    # path('stu_list/',views.stu_list),
    # path('stu_details/<int:pk>',views.stu_details)
    path('Stu_List/',Stu_List.as_view(),name='Stu_List'),
    path('Stu_Details/<int:pk>',Stu_Details.as_view(),name='Stu_Details')
]