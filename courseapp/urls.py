from django.urls import include,path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add_course/',views.add_course,name='add_course'),
    path('add_coursedb/',views.add_coursedb,name='add_coursedb'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_studentdb/',views.add_studentdb,name='add_studentdb'),
    path('student_details/',views.student_details,name='student_details'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('editd/<int:pk>/',views.editd,name='editd'),
    path('delete/<int:pk>/', views.delete, name='delete')
]
   


