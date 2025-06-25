from django.shortcuts import render,redirect
#user creation form 

from django.contrib.auth.forms import UserCreationForm

#for messages after signup
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':#if submit button is pressed
        form = UserCreationForm(request.POST)  #  Bind form with POST data
        if form.is_valid(): # takes care fo the duplicated user names  
            form.save()  #  Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created!')#no need to pass the msssage to the templates , django 'django.contrib.messages.middleware.MessageMiddleware', does it for us
            return redirect('food:index')
    else:
        form = UserCreationForm()  # For GET request: display blank form
    
    return render(request, 'users/register.html', {'form': form})
