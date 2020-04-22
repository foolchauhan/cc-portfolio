from django.shortcuts import render

# Create your views here.
def resume_index(request):
    context = {
    }
    return render(request, "resume_index.html", context)

def resume_detail(request):
    context = {
    }
    return render(request, "resume_detail.html", context)

def resume_detail2(request):
    context = {
    }
    return render(request, "resume_detail2.html", context)