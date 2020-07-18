from django.urls import path
from .import views


urlpatterns = [
    #path('create/', views.create_student, name="create-student"),
    #path('list/', views.student_list, name="student-list"),
    #path('search/', views.search_student, name="search-student"),
	
	#path('edit/<int:pk>', views.edit_student, name="edit-student"),

    #path('delete/<int:student_id>', views.delete_student, name="delete-student"),
	

    path('search_result/', views.search_result, name="search-result"),
	
	
    #path('register/', views.register_student, name="register-student"),
    

]
