from django.forms import ModelForm
from scoring.models import Judge_Assignment
from scoring.views.calc_sort.calculate_scores import update_scores

class ScoringForm(ModelForm):
    class Meta:
        model = Judge_Assignment
        fields = ['project_id', 'judge_id', 'goal_score', 'plan_score', 'action_score', 'result_analysis_score', 'communication_score','raw_score']

    def save(self, commit=True):

        ja = super(ScoringForm, self).save(commit=False)

        ja.goal_score = self.cleaned_data['goal_score']
        ja.plan_score = self.cleaned_data['plan_score']
        ja.action_score = self.cleaned_data['action_score']
        ja.result_analysis_score = self.cleaned_data['result_analysis_score']
        ja.communication_score = self.cleaned_data['communication_score']
        ja.raw_score = self.cleaned_data['raw_score']
        exja = Judge_Assignment.objects.get(project_id = ja.project_id
                                                ,judge_id = ja.judge_id)

        print(ja.project_id)
        print(ja.judge_id)
        print(exja)
        ja.ja_id = exja.ja_id
        print(ja.ja_id)
        if commit:
            ja.save()
            update_scores()

        return ja
