from .models import Department

def departments(request):
    departments_list = Department.objects.all()
    return {'departments_list': departments_list}
