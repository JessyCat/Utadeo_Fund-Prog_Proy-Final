from django.shortcuts import render, redirect, render_to_response

# Create your views here.
def homepage(request):
    return render(request,'inicio.html')