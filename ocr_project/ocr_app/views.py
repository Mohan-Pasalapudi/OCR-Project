
from django.shortcuts import render, redirect

from .models import ImageUpload
import pytesseract
from PIL import Image


def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        # Check if an image was provided
        if not image:
            return render(request, 'upload.html', {'error_message': 'Please select an image to upload.'})

        image_upload = ImageUpload.objects.create(image=image)

        # Redirect to result page with the ID of the newly created image_upload
        return redirect('process_image', image_id=image_upload.id)

    return render(request, 'upload.html')


def process_image(request, image_id):
    image_upload = ImageUpload.objects.get(id=image_id)
    image = Image.open(image_upload.image.path)
    text = pytesseract.image_to_string(image)
    return render(request, 'result.html', {'text': text})
