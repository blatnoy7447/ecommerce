from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from mainapp.models import Categories
from django.contrib.messages.views import SuccessMessageMixin


@login_required(login_url="/admin/")
def admin_home(request):
    return render(request,"admin_templates/home.html")

class CategoriesListView(ListView):
    model=Categories
    template_name="admin_templates/category_list.html"
    context_object_name='categories'

class CategoriesCreate(SuccessMessageMixin, CreateView):
    model=Categories
    success_message="Category Added!"
    fields="__all__"
    template_name="admin_templates/category_create.html"

class CategoriesUpdate(SuccessMessageMixin, UpdateView):
    model=Categories
    success_message="Category Updated!"
    fields="__all__"
    template_name="admin_templates/category_update.html"

