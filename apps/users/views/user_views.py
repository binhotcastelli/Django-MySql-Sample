from django.shortcuts import render, redirect
from apps.users.services.user_service import UserService
from apps.users.forms.user_form import UserForm

service = UserService()

def user_list(request):
    users = service.list()
    return render(request, 'users/list.html', {'users': users})


def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                service.create_user(
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"]
                )
                return redirect("user_list")
            except ValueError as e:
                form.add_error("email", str(e))
    else:
        form = UserForm()

    return render(request, "users/create.html", {"form": form})