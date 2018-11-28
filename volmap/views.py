from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import json

from .models import Activity
from .models import Signup


# Create your views here.
def index(request):
    is_auth = request.user.is_authenticated
    future_activities = Activity.objects.filter(due__gte=timezone.now())
    past_activities = Activity.objects.filter(due__lte=timezone.now())

    paginator = Paginator(past_activities, 3)
    page = request.GET.get('page')
    page_past_activities = paginator.get_page(page)

    context = {'is_auth': is_auth, 'future_activities': future_activities, 'past_activities': page_past_activities,
               'user': request.user}
    return render(request, 'volmap/index.html', context)


def me(request):
    future_activities = request.user.activity_set.filter(due__gte=timezone.now())

    # past activities
    past_activities = request.user.activity_set.filter(due__lte=timezone.now())

    paginator = Paginator(past_activities, 3)
    page = request.GET.get('page')
    page_past_activities = paginator.get_page(page)

    context = {'is_auth': request.user.is_authenticated, 'future_activities': future_activities,
               'past_activities': page_past_activities}

    return render(request, 'volmap/me.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        return redirect('volmap:index')


def logout_user(request):
    logout(request)
    return redirect('volmap:index')


def signup(request, activity_id):
    if not request.user.is_authenticated:
        return redirect('volmap:index')

    activity = Activity.objects.get(pk=activity_id)
    sign_up = Signup.objects.filter(user=request.user, activity=activity)
    if sign_up:
        sign_up.delete()
    else:
        Signup(user=request.user, activity=activity).save()

    return redirect('volmap:index')

def route(request, destination):
    destination_point = {'keyword': destination, 'city': '北京'}
    context = {'destination': destination_point}
    return render(request, 'volmap/route.html', context)

