from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment

def display_unassignedjudge(request):
    items = Judge.objects.all()
    judge_list= []
    unassigned_judges= []
    for judge in items:
        judgestatus = Judge_Assignment.objects.filter(judge_id=judge.judge_id)
        assign_judge_list = []
        graded = 0

        for ja in judgestatus:
            assign_judge_list.append(ja.judge_id)
            if ja.raw_score != 0:
                graded = graded + 1



        projects_assigned=len(assign_judge_list)
        if projects_assigned == 0:
            unassigned_judges.append({"judge_name":str(judge.name),"judge_id":judge.judge_id})
        else :
            judge_list.append({"judge_name":str(judge.name),"judge_id":judge.judge_id, "projects_assigned":projects_assigned, "graded":int(graded)})
    button = "judges"
    context = {
        'button' : button,
        'unassigned_judges' : unassigned_judges,

        #'name' :
    }
    return render(request, 'unassignedjudge.html', context)
