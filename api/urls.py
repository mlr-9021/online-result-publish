from django.urls import path
from .import views


urlpatterns = [


        path('result/',views.ResultView.as_view(),name="student-result"),
		#path('search_result/', views.search_result, name="search-result"),
		#path('result2/',views.ResultView2.as_view(),name="student-result2"),
		
		#path('result3<int:roll>/',views.CustomSearchFilter,name="student-result2"),


]
