from django.shortcuts import render
from django.http import JsonResponse
from .models import Forum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Simpan di session
            return redirect("/forum/")  # Arahkan ke forum setelah login
        else:
            messages.error(request, "Username atau password salah.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('/login/')

def forum_detail(request, id):
    forum = Forum.objects.get(id=id)
    
    return render(request, "forum_detail.html", {"forum": forum})

@login_required
def forum_list(request):
    forums = Forum.objects.exclude(owner__is_superuser=True)
    return render(request, 'forum_list.html', {'forums': forums})

from django.http import HttpResponse

def flag_view(request):
    forum_id = request.GET.get("id")

    try:
        forum = Forum.objects.get(id=forum_id)
    except Forum.DoesNotExist:
        return HttpResponse("Forum tidak ditemukan.", status=404)

    if forum.owner.is_superuser:
        try:
            with open("flag.txt") as f:
                flag = f.read().strip()
            return HttpResponse(flag)
        except FileNotFoundError:
            return HttpResponse("Flag tidak tersedia.")
    
    return HttpResponse("Bukan tempat yang tepat.")

