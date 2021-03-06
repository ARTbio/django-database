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

from .models import Patients, Sequencing


class IndexView(generic.ListView):
    template_name = 'db_conectaml/index.html'
    context_object_name = 'latest_patient_list'
    paginate_by = 3
    def get_queryset(self):
        """Return the last five published questions."""
        return Patients.objects.order_by('-date_diagnosis')

class DetailView(generic.DetailView):
    model = Patients
    context_object_name = 'patient'
    template_name = 'db_conectaml/detail.html'

def sequence(request, sequencing_id):
    return HttpResponse("specifications of  %s." % sequencing_id)

def searchpatient(request):
    '''
    To do: switch to class style and paginate
    '''
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(sex__icontains=query) | Q(age__icontains=query)
            results= Patients.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'db_conectaml/search_patients.html', context)
        else:
            return render(request, 'db_conectaml/search_patients.html')
    else:
        return render(request, 'db_conectaml/search_patients.html')

