from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url="/register/")
def index(request):
    return render(request, "home/index.html")


@login_required(login_url="/register/")
def pages(request):
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        template_name = request.path.split('/')[-1]
        if template_name == 'admin':
            return redirect('admin:index')
        context = {'segment': template_name}
        return render(request, f'home/{template_name}', context)
    except template.TemplateDoesNotExist:
        return render(request, 'home/page-404.html')
    except:
        return render(request, 'home/page-500.html')
