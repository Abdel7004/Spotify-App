from django.urls import path
from . import views 

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),# <- here is the new line to include the urls of our app
    path('about/', views.About.as_view(), name="about"),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('songs/', views.SongList.as_view(), name="song_list"),
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create"),
    # Our new Route including the pk param
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
     # Our new Route including the pk param
    path('artists/<int:pk>/update',views.ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete',views.ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/songs/new/', views.SongCreate.as_view(), name="song_create"),
    # Here is our new url
    path('playlists/<int:pk>/songs/<int:song_pk>/', views.PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
]