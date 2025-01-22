from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request,'login.html')

@login_required_decorator
def home_page(request):
    faculties=services.get_faculty()
    kafedras=services.get_kafedra()
    groups=services.get_group()
    students=services.get_student()
    teachers=services.get_teacher()
    subjects=services.get_subject()
    ctx={
        'counts':{'faculties':len(faculties),"kafedras":len(kafedras),
                  'groups':len(groups),'students':len(students),
                  'teachers':len(teachers),'subjects':len(subjects)}

    }
    return render(request,'index.html',ctx)


@login_required_decorator
def faculty_create(request):
    model=Faculty()
    form=FacultyForm(request.POST , instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx={
        'form':form
    }
    return render(request,'faculty/form.html',ctx)

@login_required_decorator
def faculty_edit(request,pk):
    model=Faculty.objects.get(pk=pk)
    form=FacultyForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx={
        'form':form,
        "model":model,
    }
    return render(request,'faculty/form.html',ctx)

@login_required_decorator
def faculty_delete(request,pk):
    model=Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')

@login_required_decorator
def faculty_list(request):
    faculties=services.get_faculty()

    ctx={
        'faculties':faculties
    }
    return render(request,'faculty/list.html',ctx)


@login_required_decorator
def kafedra_create(request):
    model=Kafedra()
    form=KafedraForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx={
        "form":form
    }
    return render(request,"kafedra/form.html",ctx)
@login_required_decorator
def kafedra_edit(request,pk):
    model=Kafedra.objects.get(pk=pk)
    form=KafedraForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx={
        'form':form,
        'model':model
    }
    return render(request,'kafedra/form.html',ctx)
@login_required_decorator
def kafedra_delete(request,pk):
    model=Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')

@login_required_decorator
def kafedra_list(request):
    kafedras=services.get_kafedra()
    context={
        'kafedras':kafedras
    }
    return render(request,'kafedra/list.html',context)



@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')

    ctx = {
        'form': form,
    }

    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request,pk):
    model=Subject.objects.get(pk=pk)
    form=SubjectForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx={
        'form':form,
        "model":model,
    }
    return render(request,'subject/form.html',ctx)


@login_required_decorator
def subject_delete(request,pk):
    model=Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects=services.get_subject()
    ctx={
        "subjects":subjects,
    }
    return render(request,"subject/list.html",ctx)

@login_required_decorator
def teacher_create(request):
    model=Teacher()
    form=TeacherForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx={
        "form":form
    }
    return render(request,"teacher/form.html",ctx)


@login_required_decorator
def teacher_edit(request,pk):
    model=Teacher.objects.get(pk=pk)
    form=TeacherForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        model.save()
        return redirect('teacher_list')
    ctx={
        'form':form,
        'model':model,
    }
    return render(request,'teacher/form.html',ctx)


@login_required_decorator
def teacher_delete(request,pk):
    model=Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')
@login_required_decorator
def teacher_list(request):
    teachers=services.get_teacher()
    ctx={
        'teachers':teachers,
    }
    return render(request,'teacher/list.html',ctx)


@login_required_decorator
def group_create(request):
    model=Group()
    form=GroupForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx={
        'form':form,
    }
    return render(request,'group/form.html',ctx)


@login_required_decorator
def group_edit(request,pk):
    model=Group.objects.get(pk=pk)
    form=GroupForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx={
        "model":model,
        'form':form,
    }
    return render(request,'group/form.html',ctx)


@login_required_decorator
def group_delete(request,pk):
    model=Group.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')

@login_required_decorator
def group_list(request):
    groups=services.get_group()
    ctx={
        'groups':groups,
    }
    return render(request,'group/list.html',ctx)


@login_required_decorator
def student_create(request):
    model=Student()
    form=SubjectForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx={
        'form':form
    }
    return render(request,'student/form.html',ctx)

@login_required_decorator
def student_edit(request,pk):
    model=Student.objects.get(pk=pk)
    form=SubjectForm(request.POST,instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx={
        'form':form,
        'model':model,

    }
    return render(request,'student/form.html',ctx)

@login_required_decorator
def student_delete(request,pk):
    model=Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    students=services.get_student()
    ctx={
        'students':students
    }
    return render(request,'student/list.html',ctx)









