# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile


# ===============================
# MAIN WEBSITE PAGES
# ===============================

def index(request):
    return render(request, 'myapp/index.html')

def study(request):
    return render(request, 'myapp/study.html')

def student_services(request):
    return render(request, 'myapp/student_services.html')

def research(request):
    return render(request, 'myapp/research.html')

def faculties(request):
    return render(request, 'myapp/faculties.html')

def about(request):
    return render(request, 'myapp/about.html')

def subjects(request):
    return render(request, 'myapp/subjects.html')

def courses(request):
    return render(request, 'myapp/courses.html')

def apply(request):
    return render(request, 'myapp/apply.html')

def fees(request):
    return render(request, 'myapp/fees.html')

def international(request):
    return render(request, 'myapp/international.html')

def experience(request):
    return render(request, 'myapp/experience.html')

def events(request):
    return render(request, 'myapp/events.html')

def offer_holders(request):
    return render(request, 'myapp/offer_holders.html')

def contact(request):
    return render(request, 'myapp/contact.html')


# ===============================
# DASHBOARD + CHAPTER
# ===============================

def dashboard(request):
    return render(request, 'myapp/dashboard.html')


def chap1(request):
    """
    Chapter 1 page
    Later you can replace coursework_start_time
    from database (admin controlled)
    """

    coursework_start_time = None  # Default (admin not started)

    return render(request, 'myapp/chap1.html', {
        "coursework_start_time": coursework_start_time
    })


# ===============================
# ASSESSMENT SYSTEM
# ===============================

def ass1(request):

    correct_answers = {
        "q1": "c", "q2": "b", 
    }

    if request.method == "POST":

        score = 0
        total = len(correct_answers)

        for q, ans in correct_answers.items():
            user_ans = request.POST.get(q)
            if user_ans == ans:
                score += 1

        # Store result in session
        request.session["quiz_score"] = score
        request.session["quiz_total"] = total

        return redirect("result")

    return render(request, "myapp/ass1.html")


def result(request):

    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        total = int(request.POST.get("total", 1))

        percentage = round((score / total) * 100)

        return render(request, "myapp/result.html", {
            "score": score,
            "total": total,
            "percentage": percentage
        })

    return redirect("ass1")





# ===============================
# AUTHENTICATION SYSTEM
# ===============================

def signup_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role', 'student')

        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        # Username exists check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        # Create Django user
        user = User.objects.create_user(
            username=username,
            password=password1
        )

        # Create MongoDB profile
        UserProfile.objects.create(
            name=username,
            password=user.password,
            role=role
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'myapp/signup.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'myapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
