from django.shortcuts import render,redirect,get_object_or_404
from .models import Registration
from .forms import RegistrationForm
# Create your views here.
def user_list(request):
    r = Registration.objects.all()
    d = {'reg': r}
    return render(request,'myapp/index.html',d)

def add_user(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list') 
    else:
        form = RegistrationForm()
    return render(request, 'myapp/add_user.html', {'form':form})

def update_user(request, user_id):
    user = get_object_or_404(Registration, pk=user_id)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'myapp/update_user.html', {'form': form})

 

def delete_user(request,user_id):
    user = get_object_or_404(Registration, pk=user_id)
    user.delete()
    return redirect('user_list')
    