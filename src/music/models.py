from django.db import models

# red pk 1
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title =models.CharField(max_length=500)
	genre= models.CharField(max_length=100)
	album_logo=models.CharField(max_length=1000)

	def __str__(self):
		return self.album_title + ' - ' + self.artist


class song(models.Model):
	#a song needs to part of the album , so how do we link them?
	Album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type= models.CharField(max_length=10)
	song_title= models.CharField(max_length=250)

	def __str__(self):
		return self.song_title