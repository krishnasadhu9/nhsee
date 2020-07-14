from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment, Project
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def display_unasigned(request):
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

    items = Project.objects.all()
    project_list= []
    unassigned_projects= []
    for project in items:
        projectstatus = Judge_Assignment.objects.filter(project_id=project.project_id)
        assign_project_list = []
        graded = 0

        for ja in projectstatus:
            assign_project_list.append(ja.project_id)
            if ja.raw_score != 0:
                graded = graded + 1

        judges_assigned=len(assign_project_list)
        if judges_assigned == 0:
            unassigned_projects.append({"project_id":project.project_id, "project_title":project.project_title})
        else:
            project_list.append({"project_id":project.project_id,"table_id":project.table_id, "project_title":project.project_title, "project_category":project.project_category, "avg_score":project.avg_score, "rank":project.rank, "z_score":project.z_score, "z_score_rank":project.z_score_rank, "avg_01":project.avg_01, "avg_01_rank":project.avg_01_rank, "scaled_score":project.scaled_score, "scaled_rank":project.scaled_rank, "scaled_z":project.scaled_z, "isef_score":project.isef_score,      "isef_rank":project.isef_rank, "category_rank":project.category_rank, "fair_rank":project.fair_rank, "judges_assigned":int(judges_assigned), "graded":int(graded)})
    button = "judges"
    context = {
        'button' : button,
        'unassigned_judges' : unassigned_judges,
        'unassigned_projects' : unassigned_projects,



        #'name' :
    }
    return render(request, 'assigned.html', context)



def createjudgeassignment(request):
    if request.method == "POST":
        context = {}
        project_id = request.POST['project']
        judge_id = request.POST['judge']

        project =  Project.objects.get(project_id = project_id)
        judge = Judge.objects.get(judge_id = judge_id)
        Judge_Assignment(judge_id = judge, project_id = project ).save()
        return HttpResponseRedirect(reverse('display_judges'))

    return render(request, 'home.html')
