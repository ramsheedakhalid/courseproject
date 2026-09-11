from django.shortcuts import render,redirect
from . import views
from .models import Course,Student

# Create your views here.
def home(request):
    return render(request,'home.html')
def add_student(request):
    courses=Course.objects.all()
    return render(request,'add_student.html',{'course':courses})
def add_course(request):
    return render(request,'add_course.html')

def add_coursedb(request) :
    if request.method=="POST":
        course_name=request.POST.get('course')
        course_fee=request.POST.get('fee')
        course=Course(course_name=course_name,fee=course_fee)
        course.save ()
        return redirect('add_course')

def add_studentdb(request) :
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request. POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student = Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()

        return redirect('add_student')

def student_details(request):
    student = Student.objects.all()
    return render(request,'student_details.html', {'students': student})


def edit(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'stud':student,'course': course})

def editd(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST["name"]
        student.student_address=request.POST["address"]
        student.student_age=request.POST["age"]
        sel=request.POST["sel"]
        student.joining_date=request.POST["jdate"]
        course1=Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('student_details')
    return render(request,'edit.html')

def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student_details')