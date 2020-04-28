from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProductForm, RawProductForm

# def home_view(request, id, *args, **kwargs):
#     context = {
#         'name'  : "Lakshya",
#         'place' : "Ujjain",
#         'lang' : ["Python", "Java",  "C", "R", "C++"]
#     }
#     obj = Product.objects.get(id=id)
#     context = {
#         'obj':obj
#     }
#     # return render(request, "home.html", context)
#     return render(request, "home.html", context)

def render_initial_data(request):
    # initial_data ={
    #     'title': 'This is initial value'
    # }
    # form = ProductForm(request.POST or None, initial = initial_data)
    obj = Product.objects.get(id=11)
    form = ProductForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    return render(request, 'product_create.html', context)

def product_detail(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'obj':obj})

def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'product_create.html', context)

def rawproduct_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            form.cleaned_data['featured'] = True
            Product.objects.create(**form.cleaned_data)
        else:
            form.errors
    context = {'form':form}
    return render(request, 'product_create.html', context)

def product_delete(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect("../../")

def product_list(request):
    obj = Product.objects.all()
    return render(request, 'product_list.html', {'obj': obj})
