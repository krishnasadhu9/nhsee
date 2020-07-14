import csv
from scoring.models import Judge_Assignment
from scoring.models import Project
from django.http import HttpResponse

def export_judge_assignment(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="judge_assignments.csv"'

    writer = csv.writer(response)
    writer.writerow(['Judge ID', 'Project ID', 'goal score', 'plan_score', 'action score', 'result Analyis score', 'communication score',  'Raw Score', 'z_score', 'rank' ])

    jas = Judge_Assignment.objects.all().values_list('judge_id', 'project_id', 'goal_score', 'plan_score', 'action_score', 'result_analysis_score',  'communication_score', 'raw_score', 'z_score', 'rank' )
    for ja in jas:
        writer.writerow(list(ja))

    return response


def export_project(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'

    writer = csv.writer(response)
    writer.writerow(['project_id', 'table_id', 'project_title', 'project_category', 'avg_score', 'rank', 'z_score', 'z_score_rank', 'avg_01', 'avg_01_rank', 'scaled_score', 'scaled_rank', 'scaled_z', 'isef_score', 'isef_rank', 'category_rank', 'fair_rank'  ])

    projs = Project.objects.all().values_list('project_id', 'table_id', 'project_title', 'project_category', 'avg_score', 'rank', 'z_score', 'z_score_rank', 'avg_01', 'avg_01_rank', 'scaled_score', 'scaled_rank', 'scaled_z', 'isef_score', 'isef_rank', 'category_rank', 'fair_rank' )
    for proj in projs:
        writer.writerow(list(proj))

    return response
