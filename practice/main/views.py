from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth import login, logout

from .forms import *


def index(request):
    return render(request, 'main/index.html')


def events(request):
    evnts = Event.objects.order_by('-id')
    return render(request, 'main/events.html', {'evnts': evnts})


def people(request):
    search_query = request.GET.get('search', '')
    if search_query:
        people = UserCard.objects.filter(skill__name_s=search_query)
    else:
        people = UserCard.objects.order_by('-id')
    paginator = Paginator(people, 6)
    skills = Skills.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/people.html', {'page_obj': page_obj, 'people': people, 'skills': skills})


class usercards(ListView):
    paginate_by = 3
    model = UserCard
    skills = Skills.objects.all()
    template_name = 'main/people.html'
    context_object_name = 'people'

class create_event1(CreateView):
    form_class = EventForm
    template_name = 'main/create_event.html'
    success_url = 'success'


'''def create_event(request):
    if request.method == 'POST':
        ceform = EventForm(request.POST)
        ceform.save()
        return redirect('events')
    else:
        ceform = EventForm()
    return render(request, 'main/create_event.html', {'ceform': ceform})'''


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/enter.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def event_info(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
        'title': event.name_e,
        'event_selected': event.evtype_id
    }
    return render(request, 'main/event_info.html', context=context)


class userprofile(CreateView):
    form_class = UCardForm
    template_name = 'main/create_event.html'
    success_url = 'success2'


'''def userprofile(request):
    if request.method == 'post':
        uform = UCardForm(request.POST)
        uform.save()
        return redirect('events')
    else:
        uform = UCardForm()
    return render(request, 'main/userprofile.html', {'uform': uform})'''


def success(request):
    return render(request, 'main/success.html')


def success2(request):
    return render(request, 'main/success2.html')


def moderpage(request):
    evntss = Event.objects.order_by('-id')
    return render(request, 'main/moderpage.html', {'evntss': evntss})


class ModerEvent(UpdateView):
    model = Event
    template_name = 'main/create_event.html'
    form_class = EventFormModer

'''def enter(request):
    return render(request, 'main/enter.html')


def register(request):
    form = AddPostForm()
    return render(request, 'main/register.html')'''


'''def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))'''
