from django.shortcuts import render, get_object_or_404
from scoring.models import Judge_Assignment# Project, Judge
from scoring.forms.scoring_form import ScoringForm

def add_score(request):
    if request.method == 'POST':
        form = ScoringForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ScoringForm()
    ja_items = Judge_Assignment.objects.all()
    context = {
        'form' : form,
        'ja_items' : ja_items,
            #'name' :
    }
    return render(request, 'scoring.html', context)

#def edit_score(request):
#     ja = Judge_Assignment.objects.create()
#     form = ScoringForm(request.POST or None, instance = ja)
#     if form.is_valid():
#         form.save()
#     return render(request, 'scoring.html', {'form':form})

# def display_scoring(request):
#     judges = Judge.objects.all()
#     projects = Project.objects.all()
#     button = "judges"
#     context = {
#         'button' : button,
#         'judges' : judges,
#         'projects' : projects,
#         #'name' :
#     }
#     return render(request, 'scoring.html', context)
