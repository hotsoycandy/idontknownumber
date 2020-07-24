from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import PIL

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def guess(request):
    print(request.FILES)
    return HttpResponse(1)
