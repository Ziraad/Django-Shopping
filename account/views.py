from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from account.forms import PaymentForm, ProfileForm, MyUserForm
# from account.models import Payment


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('pooshak:homepage'))
        else:
            context = {
                'username': username,
                'error': "نام کاربری یا گذرواژه نادرست است"
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('pooshak:homepage'))
        context = {}
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))


@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'account/profile_details.html', context)

