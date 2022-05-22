from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Blogs.forms import BlogCategoryForm,BlogForm,EventForm
from Blogs.models import Blog,BlogCategory,Events
from subscribers.models import Subscriber,Recents
from django.views.generic import UpdateView,DeleteView
# Create your views here.
def add_blog_category(request):
    form = BlogCategoryForm
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, "blogs/add_category.html", context=context)
    if request.method == 'POST' and 'save' in request.POST:
        form = BlogCategoryForm(request.POST)
        if form.is_valid():
            Category_Id= form.cleaned_data["Category_Id"]
            Category_Name = form.cleaned_data["Category_Name"]

            new_BlogCategory = BlogCategory.objects.create(
                Category_Id = Category_Id,
                Category_Name=Category_Name
            )
            new_BlogCategory.save()
            messages.success(request, "Category added Successfully")
            return redirect('add_blog_category')
        else:
            messages.error(request, "unable to add Category: " + str(form.errors.as_json()))
            return redirect('add_blog_category')

    return render(request, "blogs/add_category.html", context=context)

class BlogCategoryUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'blogs/view_blogs.html'
    template_name = 'blogs/add_category.html'

    form_class = BlogCategoryForm
    model = BlogCategory

class BlogCategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = BlogCategory
    template_name = 'blogs/blog_category_confirm_delete.html'
    success_url = reverse_lazy('view_blogs')

def add_blog(request):
    form = BlogForm
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, "blogs/add_blog.html", context=context)
    if request.method == 'POST' and 'save' in request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid() and 'photo' in request.FILES:
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            photo = request.FILES['photo']
            category=form.cleaned_data['category']
            is_headline=form.cleaned_data['is_headline']
            is_popular=form.cleaned_data['is_popular']

            new_blog = Blog.objects.create(
                title=title,
                description=description,
                photo=photo,
                category=category,
                is_headline=is_headline,
                is_popular=is_popular,
            )
            new_blog.save()
            messages.success(request, "Blog item added Successfully")
            return redirect('add_blog')
        else:
            messages.error(request, "unable to add blog item: " + str(form.errors.as_json()))
            return redirect('add_blog')

    return render(request, "blogs/add_blog.html", context=context)

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'blogs/view_blogs.html'
    template_name = 'blogs/add_category.html'

    form_class = BlogForm
    model = Blog

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('view_blogs')

def add_event(request):
    form = EventForm
    context = {
        'form': form
    }
    if request.method == 'GET':
        return render(request, "blogs/addEvent.html", context=context)
    if request.method == 'POST' and 'save' in request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            venue = form.cleaned_data['venue']
            date_of_event = form.cleaned_data['date_of_event']
            event = Events.objects.create(
                title=title,
                description=description,
                venue = venue,
                date_of_event = date_of_event
            )
            event.save()
            messages.success(request, "Notice added Successfully")
            return redirect('add_event')
        else:
            messages.error(request, "unable to add notice: " + str(form.errors.as_json()))
            print("unable to add Event: " + str(form.errors.as_json()))
            return redirect('add_event')

    return render(request, "blogs/addEvent.html", context=context)

class EventsUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'blogs/view_events.html'
    template_name = 'blogs/addEvent.html'

    form_class = EventForm
    model = Events

class EventsDeleteView(LoginRequiredMixin,DeleteView):
    model = Events
    template_name = 'blogs/event_confirm_delete.html'
    success_url = reverse_lazy('view_noticeEvents')

def view_blogs(request):
    blogs = Blog.objects.filter(is_deleted=False)
    blog_categories = BlogCategory.objects.filter(is_deleted=False)
    context = {
        'blogs' :blogs,
        'blog_categories': blog_categories
    }
    return render(request,'blogs/view_blogs.html',context=context)

def view_events(request):
    events = Events.objects.filter(is_deleted=False)
    context = {
        'events' :events,
    }
    return render(request,'blogs/view_events.html',context=context)

def page_view(request):
    pass

def homepage(request):
    headlines = Blog.objects.filter(is_deleted=False).filter(is_headline=True)
    popular = Blog.objects.filter(is_deleted=False).filter(is_popular=True)
    events = Events.objects.filter(is_deleted=False)
    categories = BlogCategory.objects.filter(is_deleted=False)
    context = {
        'headlines': headlines,
        'events': events,
        'slide_items': headlines[:3],
        'populars':popular,
        'categories':categories,

    }
    return render(request, 'blogs/home.html', context=context)

def category_page(request,pk):
    chosen_category = BlogCategory.objects.get(pk=pk)
    required_blogs = Blog.objects.filter(category=chosen_category)
    categories = BlogCategory.objects.filter(is_deleted=False)
    user = request.user
    if str(user) is not 'AnonymousUser':
        try:
            subscriber = Subscriber.objects.filter(First_Name=user.first_name).filter(Last_name=user.last_name).filter(Email=user.email)[0]

        except:
            subscriber = Subscriber.objects.filter(First_Name=user.first_name).filter(Last_name=user.last_name).filter(Email=user.email)[0]
        recents = Recents.objects.filter(subscriber=subscriber)

        context = {
            'articles':required_blogs,
            'slide_items': required_blogs[:3],
            'categories':categories,
            'recents':recents
        }
    else:
        context = {
            'articles': required_blogs,
            'slide_items': required_blogs[:3],
            'categories': categories,
            'Category_Name':chosen_category,
        }

    return render(request, 'blogs/category_page.html', context=context)

def blog_item(request,pk):
    blog = Blog.objects.get(pk=pk)
    categories = BlogCategory.objects.filter(is_deleted=False)
    context = {
        'Blog':blog,
        'categories':categories
    }
    return render(request,"blogs/blog_item.html",context=context)


