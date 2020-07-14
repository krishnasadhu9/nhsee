from django.shortcuts import render
from scoring.models import Project, Judge_Assignment

def display_unassignedproject(request):
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
    button = "projects"
    context = {
        'button' : button,
        'unassigned_projects' : unassigned_projects,

        #'name' :
    }
    return render(request, 'unassignedproject.html', context)
