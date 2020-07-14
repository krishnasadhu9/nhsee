from django.urls import path
from django.conf.urls import url
import scoring.views
from scoring.views import *
from scoring.views.remove_all_data import remove_all_data
from scoring.views.display.display_top_projects import display_top_projects
from scoring.views.display.display_welcome import welcome
from scoring.views.calc_sort.calculate_scores import calculate_scores
from scoring.views.display.display_unassignedjudge import display_unassignedjudge
from scoring.views.display.display_unassignedproject import display_unassignedproject
from scoring.views.display.display_unassigned import display_unassigned
from scoring.views.display.unassigned_judgeassignment import display_unasigned, createjudgeassignment

#from .views import HomeListView

urlpatterns = [
    # url(r'add/score/$', add_score, name='add_score'),
    # url(r'^edit/$', edit_score, name='edit_score'),
    path('', welcome, name = 'welcome'),
    path('add_score/', add_score, name='add_score'),
    path('display_judges/', display_judges, name='display_judges'),
    path('display_projects/', display_projects, name='display_projects'),
    path('display_judge_assignments/', display_judge_assignments, name='display_judge_assignments'),
    path('display_students/', display_students, name='display_students'),
    path('import_file/', import_file, name='import_file'),
    path('export_judge_assignment/', export_judge_assignment, name='export_judge_assignment'),
    path('export_project/', export_project, name='export_project'),
    path('remove_all_data/', remove_all_data, name='remove_all_data'),
    path('calculate_scores/', calculate_scores, name='calculate_scores'),
    path('assigned', createjudgeassignment, name = "assigned_judge"),
    path('display_top_projects/', display_top_projects, name='display_top_projects'),
    path('display_unassignedjudge/', display_unassignedjudge, name='display_unassignedjudge'),
    path('display_unassignedproject/', display_unassignedproject, name='display_unassignedproject'),
    path('display_unassigned/', display_unassigned, name='display_unassigned'),
    path('unassigned-judgeassignment/', display_unasigned, name='unassigned-judgeassignment'),


]
