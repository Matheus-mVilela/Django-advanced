from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonList
from .views import PersonDetail
from .views import PersonCreate


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('personlist/', PersonList.as_view()),
    path('persondetail/<int:pk>/', PersonDetail.as_view(), name="persondetail"),
    path('personcreate/', PersonCreate.as_view()),
]