from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse
from .forms import RegisterForm
from .models import UserDetails

class HomePage(generic.View):
    pass

class LoginView(generic.View):
    pass

class RegisterView(generic.CreateView):
    template_name = "register.html"
    form_class = RegisterForm

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace() 
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST, request.FILES)
            username = request.POST.get('username') 
            if username in UserDetails.objects.all():
                pass
            elif form.is_valid():
                form.save()
                from django.http import HttpResponseRedirect
                return HttpResponseRedirect(reverse('blogapp:register'))
        return render(request, self.template_name)