from django.shortcuts import render
from django.http import HttpResponse
from .models import PortfolioItem

# Create your views here.

def portfolio_list(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'items': items})
