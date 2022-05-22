from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView
from subscribers.forms import Subscriberform,SubscriberClassForm
from subscribers.models import Subscriber,Recents
from Blogs.models import Blog,BlogCategory
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def add_subscriber(request):
    form = Subscriberform
    context = {
        'form': form
    }

    if request.method == 'GET':


        return render(request,'subscribers/add_subscriber.html',context=context)

    if request.method == 'POST' and 'save' in request.POST:
        form = Subscriberform(request.POST)
        if form.is_valid():
            First_Name = form.cleaned_data['First_Name']
            Last_name=form.cleaned_data['Last_name']
            Email= form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirm_password=form.cleaned_data['confirm_password']
            if password == confirm_password:
                new_subscriber = Subscriber.objects.create(
                    First_Name=First_Name,
                    Last_name=Last_name,
                    Email=Email
                )
                new_subscriber.save()

                user = User.objects.create_user(username=First_Name+" "+Last_name,email=Email,password=password)
                user.save()
                print('You are now subscribed')
                messages.success(request, "You are now subscribed")
                return redirect('login')
            else:
                messages.success(request, "You are now subscribed")
                return redirect('add_subscriber')

        else:
            messages.success(request, "You are now subscribed")
            return redirect('add_subscriber')

    return render(request,"subscribers/add_subscriber.html",context=context)

class SubscriberUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'subscribers/view_subscribers.html'
    template_name = 'subscribers/subscriber_form.html'

    form_class = SubscriberClassForm
    model = Subscriber

class SubscriberDeleteView(LoginRequiredMixin,DeleteView):
    model = Subscriber
    template_name = 'subscribers/subscriber_confirm_delete.html'
    success_url = reverse_lazy('view_noticeEvents')

def view_subscribers(request):
    subscribers = Subscriber.objects.all()
    context = {
        'subscribers':subscribers
    }
    return render(request,'subscribers/view_subscribers.html',context=context)

def subscribe_now(request):
    form = Subscriberform
    blogs = Blog.objects.filter(is_popular=True).filter(is_deleted=False)

    context = {
        'form': form,
        'slide_items':blogs[:4],
    }

    if request.method == 'GET':
        return render(request, 'subscribers/subscribe_now.html', context=context)

    if request.method == 'POST' and 'save' in request.POST:
        form = Subscriberform(request.POST)
        if form.is_valid():
            First_Name = form.cleaned_data['First_Name']
            Last_name = form.cleaned_data['Last_name']
            Email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                new_subscriber = Subscriber.objects.create(
                    First_Name=First_Name,
                    Last_name=Last_name,
                    Email=Email
                )
                new_subscriber.save()

                user = User.objects.create_user(username=First_Name + " " + Last_name, email=Email, password=password)
                user.save()
                print('You are now subscribed')
                messages.success(request, "You are now subscribed")
                return redirect('login')
            else:
                messages.success(request, "You are now subscribed")
                return redirect('subscribe_now')

        else:
            messages.success(request, "You are now subscribed")
            return redirect('subscribe_now')

    return render(request, "subscribers/subscribe_now.html", context=context)

def subscriber_login(request):
    if request.method == 'GET':
        return render(request,'subscribers/login.html')
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            if "@" in username:
                req_user = User.objects.get(email=username)
                user = authenticate(request=request, username=req_user.username, password=password)
            else:
                req_user = User.objects.get(username = username)
                user = authenticate(request=request, username=username, password=password)
        except:
            messages.error(request, "invalid login credentials supplied")
            return redirect('login')
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                First_Name = user.first_name
                Last_Name = user.last_name
                login(request, user)
                print('user logged in ')
                # Send the user back to some page.
                # In this case their homepage.
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('view_applicationforms'))
                else:
                    return HttpResponseRedirect(reverse('view_applicationforms'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:

            messages.error(request, "invalid login credentials supplied")
            return redirect('login')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")
