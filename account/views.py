from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .form import CreateUserForm,CreateProfileForm,UpdateUserForm,UpdateProfileForm
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeForm
from account.models import Profile,Company
from django.views.generic import ListView
from .filters import UserFilter


class UserListView(ListView):
    model=User
    paginate_by =10
    context_object_name='users'
    template_name='account/user_list.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=UserFilter(self.request.GET,self.get_queryset())
        return context


# Create your views here.
def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login successful ! Welcome")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')
    else:
        return render(request,'account/loginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    user_form=CreateUserForm()
    profile_form=CreateProfileForm()


    if request.method=='POST':
         user_form=CreateUserForm(request.POST)
         profile_form=CreateProfileForm(request.POST,request.FILES)
         if user_form.is_valid() and profile_form.is_valid():            
            user=user_form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.recorded_by=request.user
            profile.save()

            messages.success(request,"User Successfully created")
            return redirect('dashboard')
    context={
        'user_form':user_form,
        'profile_form':profile_form,
                }
    return render(request,'account/register.html',context)

def update(request):
    if request.method=='POST':
        user_form=UpdateUserForm(request.POST,instance=request.user)
        profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile Successfully Updated')
            return redirect('dashboard')
    else:
        user_form=UpdateUserForm(instance=request.user)
        profile_form=UpdateProfileForm(instance=request.user.profile)

    context={
        'user_form':user_form,
        'profile_form':profile_form,
                }
    return render(request,'account/update.html',context)

def viewProfile(request):
    user=request.user
    context={'user':user}
    return render(request,'account/view.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

# def userListView(request):
#     users=User.objects.all()
#     context={'users':users}
#     return render(request,'account/user_list.html',context)



