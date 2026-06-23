from django.urls import path
from .views import * 

urlpatterns = [
    path('navigation/', navigation, name='navigation'),
    path('footer/', footer, name='footer'),
     path('index/', index, name='index'),
   path("category/<str:category_name>/", category, name="category"),
]