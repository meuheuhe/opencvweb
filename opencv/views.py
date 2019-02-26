from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_mix import opencv_mix

# Create your views here.
def home(request):
    return render(request, 'home.html')

def image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile1 = request.FILES['image1']
            myfile2 = request.FILES['image2']            
            fs = FileSystemStorage()
            filename1 = fs.save(myfile1.name, myfile1)
            filename2 = fs.save(myfile2.name, myfile2)
            uploaded_file_url1 = fs.url(filename1)
            uploaded_file_url2 = fs.url(filename2)
            return render(request, 'image.html', {'form': form, 'uploaded_file_url1': uploaded_file_url1, 'uploaded_file_url2': uploaded_file_url2})
    else:
        form = UploadImageForm()
        return render(request, 'image.html', {'form': form})


def opencvweb(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    
            imageURL1 = settings.MEDIA_URL + form.instance.document.name
            imageURL2 = settings.MEDIA_URL + form.instance.document1.name            
            opencv_mix(settings.MEDIA_ROOT_URL + imageURL1, settings.MEDIA_ROOT_URL + imageURL2)
    
            return render(request, 'opencvweb.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'opencvweb.html',{'form':form})