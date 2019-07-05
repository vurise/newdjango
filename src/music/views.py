from django.http import HttpResponse
from django.shortcuts import render
from .forms import AlbumForm
from .models import Album

def home_view(*args , **kwargs):
	return HttpResponse("<h1> This is my homepage</h1><h3> (type music in the url) </h3>")

def index(request):
	all_albums= Album.objects.all()
	return render(request , 'music/index.html' , {'all_albums': all_albums})
	#return "<h1> this the homepage </h1>"

def detail(request, album_id):
	try:
		album = Album.objects.get(pk =album_id)
	except  Album.DoesNotExist:
		raise Http404("album does not exist")
	return render(request , 'music/details.html' , {'album' : album})

def new_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('artist', pk=post.pk)
    else:
        form = AlbumForm()
    return render(request, 'music/form.html', {'form': form})