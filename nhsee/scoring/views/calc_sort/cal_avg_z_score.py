from scoring.models import Judge_Assignment, Project
from statistics import mean

def cal_avg_z_score():
    projects = list(Project.objects.all())
    for project in projects:
        jas_z_score = list(Judge_Assignment.objects.filter(project_id = project.project_id).values_list('z_score', flat=True))
        not_none_scores = [i for i in jas_z_score if i is not None]
        if len(not_none_scores) < 2:
            continue
        project.z_score = mean(not_none_scores)
        project.save()
