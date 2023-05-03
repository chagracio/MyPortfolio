from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    portfolio = PersonalInfo.objects.all()
    education = Education.objects.all()
    language = Languages.objects.all()
    tech_skill = Technical_Skills.objects.all()
    # soft_skill = Soft_Skills.objects.all()
    project = Projects.objects.all()
    experience = Experience.objects.all()
    message = Contact.objects.order_by('-date')
    
    #adding contact/message
    contact_form = ContactForm()
    educ_form = EducationForm()
    tech_form = TechnicalForm()
    # soft_form = SoftForm()
    exp_form = ExperienceForm()
    lang_form = LangForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()

        educ_form = EducationForm(request.POST)
        if educ_form.is_valid():
            educ_form.save()

        tech_form = TechnicalForm(request.POST)
        if tech_form.is_valid():
            tech_form.save()

        # soft_form = SoftForm(request.POST)
        # if soft_form.is_valid():
        #     soft_form.save()

        exp_form = ExperienceForm(request.POST)
        if exp_form.is_valid():
            exp_form.save()

        lang_form = LangForm(request.POST)
        if lang_form.is_valid():
            lang_form.save()
        return redirect('index')

    context = {
        'portfolio':portfolio,
        'education':education,
        'tech_skill':tech_skill,
        # 'soft_skill':soft_skill,
        'experience':experience,
        'project':project,
        'language':language,
        'contact_form':contact_form,
        'educ_form':educ_form,
        'tech_form':tech_form,
        'lang_form':lang_form,
        'exp_form':exp_form,
        'message':message,
    }        
    return render (request, 'Portfolio.html', context)


# contact_form = ContactForm()
#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST, request.FILES)
#         if contact_form.is_valid():
#             contact_form.save()

def Profile(request, id):
    prof = PersonalInfo.objects.get(id=id)
    prof_form = ProfileForm(instance=prof)
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST, request.FILES, instance=prof)
        if prof_form.is_valid():
            prof_form.save()
        return redirect('index')
    context = {
        'prof_form':prof_form,
    }
    return render(request, 'updateProfile.html', context)

def Project(request, id):
    img = Projects.objects.get(id=id)
    proj_form = ProjectForm(instance=img)
    if request.method == 'POST':
        proj_form = ProjectForm(request.POST, request.FILES, instance=img)
        if proj_form.is_valid():
            proj_form.save()
        return redirect('index')
    context = {
        'img':img,
        'proj_form':proj_form,
    }
    return render(request, 'image.html', context)

def deleteExperience(request, id):
    obj= Experience.objects.get(id=id)
    obj.delete()
    return redirect('index')

def deleteEducation(request, id):
    x= Education.objects.get(id=id)
    x.delete()
    return redirect('index')

def deleteSkill(request, id):
    y= Technical_Skills.objects.get(id=id)
    y.delete()
    return redirect('index')

def deleteProject(request, id):
    z= Projects.objects.get(id=id)
    z.delete()
    return redirect('index')

def deleteLanguage(request, id):
    i= Languages.objects.get(id=id)
    i.delete()
    return redirect('index')

def deleteMessage(request, id):
    i= Contact.objects.get(id=id)
    i.delete()
    return redirect('index')

def UpdateEducation(request, id):
    educ = Education.objects.get(id=id)
    educ_form = EducationForm(instance=educ)
    if request.method == 'POST':
        educ_form = EducationForm(request.POST, instance=educ)
        if educ_form.is_valid():
            educ_form.save()
        return redirect('index')
    context = {
        'educ_form':educ_form,
    }
    return render(request, 'education.html', context)

def UpdateExperience(request, id):
    exp = Experience.objects.get(id=id)
    exp_form = ExperienceForm(instance=exp)
    if request.method == 'POST':
        exp_form = ExperienceForm(request.POST, instance=exp)
        if exp_form.is_valid():
            exp_form.save()
        return redirect('index')
    context = {
        'exp_form':exp_form,
    }
    return render(request, 'experience.html', context)

def UpdateLanguage(request, id):
    lang = Languages.objects.get(id=id)
    lang_form = LangForm(instance=lang)
    if request.method == 'POST':
        lang_form = LangForm(request.POST, instance=lang)
        if lang_form.is_valid():
            lang_form.save()
        return redirect('index')
    context = {
        'lang_form':lang_form,
    }
    return render(request, 'language.html', context)