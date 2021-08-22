from django.shortcuts import render,redirect

# Create your views here.
#
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from .models import BlogModel#, Folder
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# 検索機能
from django.db.models import Q

# ページング
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic


def homeview(request):
    return render(request,'home.html')


def signupview(request):
    print(request.method)
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html',
                          {'error': 'このユーザーは既に登録されています'})
    else:
        print(User.objects.all())
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logoutview(request):
    logout(request)
    return redirect('home')



#"""
class BlogList(LoginRequiredMixin, generic.ListView):
    template_name = 'list.html'
    paginate_by = 10
    model = BlogModel

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        #ページング別の方法
        print(q_word)
        #page = self.request.GET.get('page')
        if q_word:
            object_list = BlogModel.objects.filter(Q(title__icontains=q_word)|Q(category__icontains=q_word))
        else:
            #object_list2 = Folder.objects.all()
            object_list = BlogModel.objects.all()
            #paginator = Paginator(object_list, 2)
            #pages = paginator.get_page(page)
        #return pages
        return object_list





"""
@login_required
def ListView(request):
    object_list = BlogModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})
"""




class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel


class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title','content','category')
    success_url =reverse_lazy('list')


class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')


class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

"""
class BlogCreate2(CreateView):
    template_name = 'create2.html'
    model = Folder
    fields = ('title',)
    success_url = reverse_lazy('list')
"""
