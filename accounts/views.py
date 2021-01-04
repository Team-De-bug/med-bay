from django.contrib.auth.decorators import login_required
from admins.utils import validate_access
from django.http import HttpResponse
from django.shortcuts import render
from .models import Entries
import json


# Create your views here.
@login_required()
def home(request):
    validate_access(request, 'ac')

    # Getting the expenses
    expenses = Entries.objects.filter(type=False)

    exp_tally = {}
    for exp in expenses:
        if exp.cat not in exp_tally:
            exp_tally[exp.cat] = exp.price
        else:
            exp_tally[exp.cat] += exp.price

    return render(request, 'accounts/home.html', context={"exp_tally": exp_tally})


@login_required()
def entries(request):
    validate_access(request, 'ac')

    # Handling the request to save entries
    if 'entries' in request.GET:
        data = json.loads(request.GET['entries'])
        for ent in data.values():
            t = ent[3] == 'Income'
            entry = Entries(date=ent[0], desc=ent[1], cat=ent[2], type=t, price=int(ent[4]))
            entry.save()
        return HttpResponse('success')

    # getting all the entries and the unique categories
    entries = Entries.objects.all()
    cats = []
    for cat in entries.values('cat').distinct():
        cats.append(cat['cat'])

    return render(request, 'accounts/entries.html', context={"entries": entries, "cats": cats})
