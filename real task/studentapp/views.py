from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Department, Course, Purpose, Customer, Material
from django.http import JsonResponse

def home(request):
    department = Department.objects.all()
    return render(request, 'home.html', {'departments': department})

@login_required(login_url='login') 
def new_page(request):
    return render(request, 'new.html')

@login_required(login_url='login') 
def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    courses_dict = {course['id']: course['name'] for course in courses}
    return JsonResponse({'courses': courses_dict})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'You have registered successfully! You can now log in.')
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('new')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login') 
def add_customer(request):
    departments = Department.objects.all()
    purposes = Purpose.objects.all()
    materials = Material.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        department_id = request.POST['department']
        course_id = request.POST['course']
        purpose_id = request.POST['purpose']
        selected_materials = request.POST.getlist('materials_provided')

        customer = Customer(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            department_id=department_id,
            course_id=course_id,
            purpose_id=purpose_id
        )
        customer.save()
        customer.materials_provided.set(selected_materials)
        messages.success(request, 'Information sent successfully!')

    return render(request, 'add_customer.html', {'departments': departments, 'purposes': purposes ,'materials': materials})
