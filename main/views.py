from django.shortcuts import render, redirect
from .models import Catalog
from .forms import CatalogForm
from django.views.generic import DetailView


# Create your views here.
def index(request):
    catalog = Catalog.objects.order_by('id')
    return render(request, 'main/index.html', {'catalog': catalog})


def contacts(request):
    return render(request, 'main/contacts.html')

def cat(request):
    catalog = Catalog.objects.order_by('id')
    return render(request, 'main/cat.html', {'catalog': catalog})


def adm(request):
    
    error = ''
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Некоректне значення. Ціна має бути в форматі "12.50" а не "12,50"'
        
    form = CatalogForm()
    context ={'form': form,
    'error': error
    }

    return render(request, 'main/adm.html', context)

class ProductDetailView(DetailView):
    model = Catalog
    template_name =  'main/product.html'
    context_object_name = 'product'

