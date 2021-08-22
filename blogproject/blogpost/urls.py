"""
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/',admin.site.urls),
    path('list/',BlogList.as_view())
]
"""
from django.urls import path

from .views import  BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate, signupview, loginview, logoutview, homeview#,BlogCreate2

#from .views import ListView

#BlogListを消す


urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    #path('list/', ListView, name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
    path('signup', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('home/', homeview, name='home'),
    #path('create2/', BlogCreate2.as_view(), name='create2'),
]

"""
#from .views import ListView, DetailView, CreateView, DeleteView, UpdateView, signupview, loginview, logoutview
urlpatterns = [
    path('list/', ListView, name='list'),
    path('detail/<int:pk>/', DetailView, name='detail'),
    path('create/', CreateView, name='create'),
    path('delete/<int:pk>', DeleteView, name='delete'),
    path('update/<int:pk>', UpdateView, name='update'),
    path('signup', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout')
]
"""