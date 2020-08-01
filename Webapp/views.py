from django.shortcuts import render, redirect
from Webapp.forms import QuestionForm,ScoreForm,ContactForm,FeedbackForm,QuestionAnsForm,MaxForm,SubForm,TimeForm
from Webapp.models import Question,Score2,Contact,Feedback,QuestionAns,Max,Sub,Time
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse


def homepage(request):
    return render(request, "home.html")


def start(request):
    return render(request, "register.html")


def insert(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        passwd = request.POST['password']
        user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=email, password=passwd)
        print(user)
        user.save()
        us=Max(user=uname,sc=0)
        us.save()
        return redirect('/login')
    else:
        return HttpResponse('<script>alert("request error..!!")</script>')


def loginpage(request):
    return render(request, "login.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        user = auth.authenticate(username=email, password=pwd)
        if user is not None:
            auth.login(request, user)
            u=Sub.objects.all()
           

            return render(request, "navbar.html", {'key': email,'data':u})
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('/')
    else:
        return HttpResponse('<script>alert("request error..!!")</script>')

def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request, "about.html")
def navbar(request,key):
    u=Sub.objects.all()
           
    return render(request, "navbar.html",{'key':key,'data':u})

def contactpg(request):
    return render(request, "contact.html")

def contactins(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        cont = request.POST['country']
        sub = request.POST['subject']
        user = Contact(firstname=fname, lastname=lname, country=cont, subject=sub)
        print(user)
        user.save()
        return redirect('/')
    else:
        return HttpResponse('<script>alert("request error..!!")</script>')

def feedbackpg(request,key):
    return render(request, "feedback.html",{'sr':key})


def feedbackins(request,sr):
    if request.method == 'POST':
        experience = request.POST['experience']
        comments = request.POST['comments']
        name = request.POST['name']
        email = request.POST['email']
        user = Feedback(experience=experience,cmnt=comments, name=name, email=email)
        print(user)
        user.save()
        return render(request, "navbar.html",{'key':sr})
    else:
        return HttpResponse('<script>alert("request error..!!")</script>')

def fetch(request, key):
    if request.method == 'POST':
        sr = request.POST['cars1']
        # sm= request.POST['sop']
        QuestionAns.objects.all().delete()
        match = Question.objects.filter(category=sr)
        ti=Time.objects.all()
        cont = {'code': match, 'cat': sr, 'name':key,'time':ti}
        return render(request, 'quizapp.html', {'cont': cont})


def ceck(request, cat, name):
    if request.method == 'POST':
        score = 0
        ques = Question.objects.filter(category=cat).all()
        for q in ques:
            a = request.POST['{}'.format(q.id)]
            if q.answer == a:
                user=QuestionAns(qno=q.qno,ques=q.ques, opt1=q.opt1, opt2=q.opt2, opt3=q.opt3, opt4=q.opt4, answer=q.answer,yanswer=a,com="Right Answer")
                user.save()
                score = score + 2
            else:
                user=QuestionAns(qno=q.qno,ques=q.ques, opt1=q.opt1, opt2=q.opt2, opt3=q.opt3, opt4=q.opt4, answer=q.answer,yanswer=a,com="Wrong Answer")
                user.save()

        us=Score2(cat=cat, user=name, scores=score)
        us.save()
        mat= Max.objects.get(user=name)
        if mat.sc < score:
            mat.sc=score
            mat.save()
        return render(request, 'scro.html', {'score': score,'key':name})
    else:
        return redirect('/nav')


def getans(request,key,score):
    match=QuestionAns.objects.all()
    return render(request, 'anspg.html',{'me':match,'key':key,'score':score})

def leaderboard(request,key):
    match=Score2.objects.all()
    return render(request, 'leader.html', {'ke':match,'key':key})

def scorepg(request,key,score):
    return render(request, "scro.html",{'key':key,'score':score})

def profl(request,key):
    us=User.objects.get(username=key)
    nc=Max.objects.get(user=key)
    match=Score2.objects.filter(user=key)
    cont = {'code': us, 'cat': nc, 'co':match}
    return render(request, 'profile.html', {'cont': cont})

