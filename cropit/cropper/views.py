from django.shortcuts import render

# Create your views here.
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
	photos = Photo.objects.all()

	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('photo_list')

	else:
		form = PhotoForm()

	context = {
		'form' : form,
		'photos' : photos,
	}
	return render(request, 'photo_list.html', context)