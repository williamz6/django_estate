from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm 
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)        
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!, you are now able to login')
            return redirect('login')
        else:
            messages.error(request, "Please correct the error below")
            
    else:
        form = UserRegistrationForm()
       
    
    return render(request, 'accounts/register.html', {
        'form':form
    })

class LoginFormView(SuccessMessageMixin,LoginView):
    template_name = 'accounts/login.html'
    model = User
    success_url = '/dashboard/'
    success_message = "You were successfully logged in!"


# def logout(request):
#     return redirect('index')

@login_required
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)