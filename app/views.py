
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    first_name = request.user.student.first_name
    lname = request.user.student.last_name
    eno = request.user.student.enrollment_no
    ra = request.user.student.room_allotted
    rn = request.user.student.room.room_type
    context = {
        'first_name': first_name,
        'last_name': lname,
        'e_no': eno,
        'ra': ra,
        'rn': rn
    }
    return render(request, "registration/homepage.html", context)
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})