from django.shortcuts import render
from django.shortcuts import redirect

def redirect_to_gallery(request):
    return redirect('gallery')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')
