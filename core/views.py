from django.shortcuts import render, redirect
from .models import UrlModel
from .forms import UrlCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def signup(request):
    if request.method == "POST":
        pass
    return render(request, "", {})


def viewer(request):
    url = UrlModel.objects.all()
    return render(request, 'core/viewer.html', {"url": url})


def create(request):
    current_user = request.user   # used current_user to avoid selecting from a list of existing users
    form = UrlCreationForm()

    if request.method == "POST":
        form = UrlCreationForm(request.POST)
        if form.is_valid():
            name_of_url = form.cleaned_data['url_name']
            new_url = UrlModel.objects.create(user=current_user,  url_name=name_of_url)
            new_url.save()

        return redirect('/')
    else:
        return render(request, 'core/create.html', {"form": form})
