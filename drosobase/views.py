# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.db.models import Q

from django.http import HttpResponse

from django.http import Http404

# Create your views here.

from .models import Stocks


class IndexView(generic.ListView):
    template_name = 'drosobase/index.html'
    context_object_name = 'stock_list'
    paginate_by = 40
    def get_queryset(self):
        """Return the last five published stocks."""
        return Stocks.objects.order_by('-post_date')


class DetailView(generic.DetailView):
    model = Stocks
    context_object_name = 'stock'
    template_name = 'drosobase/detail.html'

def searchstock(request):
    '''
    To do: switch to class style and paginate
    '''
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(post_title__icontains=query) | Q(post_content__icontains=query) | Q(post_date__icontains=query)
            results= Stocks.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'drosobase/search_stocks.html', context)
        else:
            return render(request, 'drosobase/search_stocks.html')
    else:
        return render(request, 'drosobase/search_stocks.html')

