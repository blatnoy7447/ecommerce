from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from mainapp.models import Categories, SubCategories
from django.contrib.messages.views import SuccessMessageMixin


@login_required(login_url="/admin/")
def admin_home(request):
    return render(request,"admin_templates/home.html")

#CATEGORIES
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

#SUBCATEGORIES
class SubCategoriesListView(ListView):
    model=SubCategories
    template_name="admin_templates/sub_category_list.html"
    context_object_name='categories'

class SubCategoriesCreate(SuccessMessageMixin, CreateView):
    model=SubCategories
    success_message="SubCategory Added!"
    fields="__all__"
    template_name="admin_templates/sub_category_create.html"

class SubCategoriesUpdate(SuccessMessageMixin, UpdateView):
    model=SubCategories
    success_message="SubCategory Updated!"
    fields="__all__"
    template_name="admin_templates/sub_category_update.html"
