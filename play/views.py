from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Song, User


class IndexView(generic.ListView):
    template_name = 'play/song_list.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.all


class MusicFileView(generic.DetailView):
    template_name = 'play/play_page.html'
    model = Song


def likes(request, id):
    # template_name = 'play/likes_page.html'
    song = get_object_or_404(Song, id=request.POST.get('song_id'))
    if song.favorite_by.filter(id=request.user.id).exists():
        song.favorite_by.remove(request.user)
    else:
        song.favorite_by.add(request.user)
    return HttpResponseRedirect(reverse('play:index'))

