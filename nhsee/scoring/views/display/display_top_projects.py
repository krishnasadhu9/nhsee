from scoring.models import Project, Student
from django.shortcuts import render

def display_top_projects(request):
    button = "top_projects"
    top_all_list = []
    top_all_categories = []
    top_all = list(Project.objects.order_by('fair_rank').exclude(fair_rank__isnull=True)[:5])
    for tls in top_all:
        stu = Student.objects.filter(project_id=tls.project_id)
        fns = " "
        school = " "
        for st in stu:
            fns = fns + " " + st.id
            school = st.school
        top_all_list.append({"project_id":tls.project_id, "project_title":tls.project_title, "project_category":tls.project_category,  "category_rank":tls.category_rank, "fair_rank":tls.fair_rank, "student_names":fns, "school_name":school})



    projects = list(Project.objects.all())
    categories = []
    for project in projects:
        if not project.project_category in categories:
            categories.append(project.project_category)

    top_all_studcat = []
    print(categories)
    for category in categories:
#        print(category)
        top_in_category = Project.objects.filter(project_category=category).order_by('category_rank')[:5]
        top_in_categorys = []
        for top in top_in_category:
            students = list(Student.objects.filter(project_id=top.project_id))
            sn = ""
            schooln = ""
            for s in students:
                sn = sn + " " + s.id
                schooln = s.school
            top_in_categorys.append({"project_id":top.project_id, "project_title":top.project_title, "project_category":top.project_category,  "category_rank":top.category_rank, "fair_rank":top.fair_rank, "student_names":sn, "school_name":schooln})
#            print(sn)
        top_all_categories.append(top_in_categorys)

    for p in projects:
        print(p)
    context = {
        'button' : button,
        'top_all_list' : top_all_list,
        'top_all_categories' : top_all_categories,
        #'name' :
    }
    return render(request, 'home.html', context)
