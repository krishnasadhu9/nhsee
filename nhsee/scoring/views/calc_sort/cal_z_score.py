from scoring.models import Judge_Assignment
from statistics import mean, stdev

def cal_z_score():
    jas = list(Judge_Assignment.objects.all())
    for ja in jas:
        jas_projects = list(Judge_Assignment.objects.filter(judge_id = ja.judge_id))
        all_judge_scores = []
        for jas_project in jas_projects:
            if jas_project.raw_score != 0:
                all_judge_scores.append(jas_project.raw_score)
        if len(all_judge_scores) < 2 :
            continue
        if stdev(all_judge_scores) > 0:
            ja.z_score = (ja.raw_score - mean(all_judge_scores))/stdev(all_judge_scores)
            ja.save()
