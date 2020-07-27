from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from PIL import Image
from lib.numberGuess import predict

# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def guess(request):
    with open('aaaa.png', 'wb+') as destination:
        for chunk in request.FILES['file'].chunks():
            destination.write(chunk)

    image = Image.open('aaaa.png')

    # get original image size
    image_width, image_height = image.size
    print (image, image_width, image_height)

    # resize image
    image = image.resize((28, 28), Image.ANTIALIAS)
    image_width, image_height = image.size
    print (image, image_width, image_height)

    # response
    os.remove('aaaa.png')
    prediction = predict(image)
    return HttpResponse(prediction)
