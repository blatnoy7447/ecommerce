from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from mainapp.models import Categories, SubCategories, CustomUser, MerchantUser
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.messages.views import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


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

class MerchantUserListView(ListView):
    model=MerchantUser
    template_name="admin_templates/merchant_list.html"

class MerchantUserCreateView(SuccessMessageMixin, CreateView):
    template_name="admin_templates/merchant_create.html"
    model=CustomUser
    fields=["first_name","last_name","email","username","password"]

    def form_valid(self, form):
        #Saving Custom User Object for Merchant User
        user=form.save(commit=False)
        user.is_active=True
        user.user_type=3
        user.set_password(form.cleaned_data["password"])
        user.save()
        #Saving Merchant User
        profile_pic=self.request.FILES["profile_pic"]
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url=fs.url(filename)

        user.merchantuser.profile_pic=profile_pic_url
        user.merchantuser.company_name=self.request.POST.get("company_name")
        user.merchantuser.gst_details=self.request.POST.get("gst_details")
        user.merchantuser.address=self.request.POST.get("address")
        is_added_by_admin=False

        if self.request.POST.get("is_added_by_admin")=="on":
            is_added_by_admin=True

        user.merchantuser.is_added_by_admin=is_added_by_admin
        user.save()
        messages.success(self.request,"Merchant User Created")
        return HttpResponseRedirect(reverse("merchant_list"))
        


