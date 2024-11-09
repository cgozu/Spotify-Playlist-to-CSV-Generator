import requests
import base64
import pandas as pd

# Credenciales de la aplicación de Spotify
client_id = ''
client_secret = ''

# Obtener el token de acceso
def get_spotify_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    
    if 'access_token' in response_data:
        return response_data['access_token']
    else:
        print("Error al obtener el token de acceso:", response_data)
        raise Exception("No se pudo obtener el token de acceso")

# Obtener los datos de las canciones de una playlist
def get_playlist_tracks(playlist_id, token):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    
    if 'items' in response_data:
        return response_data['items']
    else:
        print("Error al obtener las canciones de la playlist:", response_data)
        raise Exception("No se pudo obtener las canciones de la playlist")

# Obtener los datos de una canción
def get_track_data(track_id, token):
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Obtener los datos de audio de una canción
def get_audio_features(track_id, token):
    url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Obtener los datos de un álbum
def get_album_data(album_id, token):
    url = f'https://api.spotify.com/v1/albums/{album_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Obtener los datos de un artista
def get_artist_data(artist_id, token):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Generar el CSV
def generate_csv(playlist_ids, start_index=1):
    token = get_spotify_token()
    data = []
    index = start_index
    song_ids = set()

    for playlist_id in playlist_ids:
        tracks = get_playlist_tracks(playlist_id, token)
        for item in tracks:
            track = item['track']
            track_id = track['id']

            # Validar si el songID ya está agregado
            if track_id in song_ids:
                print(f"El songID {track_id} ya está agregado. Pasando a la siguiente canción.")
                continue

            track_data = get_track_data(track_id, token)
            audio_features = get_audio_features(track_id, token)

            # Obtener los datos del primer artista
            artist_id = track['artists'][0]['id']
            artist_data = get_artist_data(artist_id, token)
            genres = artist_data.get('genres', [])
            images = track_data['album'].get('images', [])

            # Formatear los géneros como una lista de cadenas
            genres_str = f"[{', '.join([f'\'{genre}\'' for genre in genres])}]"

            # Esperar para obtener la URL de la vista previa
            preview_url = track['preview_url']
            if not preview_url:
                print(f"No se pudo obtener la URL de la vista previa para la canción {track['name']}. Pasando a la siguiente canción.")
                continue

            song_data = {
                'index': index,
                'songID': track_id,
                'Song': track['name'],
                'Performer': ', '.join([artist['name'] for artist in track['artists']]),
                'spotify_genre': genres_str,
                'spotify_track_id': track_id,
                'spotify_track_preview_url': preview_url,
                'album_image_url': images[0]['url'] if images else '',
                'spotify_track_album': track_data['album']['name'],
                'danceability': audio_features['danceability'],
                'loudness': audio_features['loudness'],
                'tempo': audio_features['tempo']
            }
            print(f"Procesando la canción {song_data['Song']} de {song_data['Performer']} (índice {index})")
            data.append(song_data)
            song_ids.add(track_id)
            index += 1

    df = pd.DataFrame(data)
    df.to_csv('data_clean.csv', index=False)

# Ejemplo de uso
playlist_ids = ['0uM2YdatpMMTB89C7Yudwk', '37i9dQZF1DXcBWIGoYBM5M', '6u4GaztHbiN51Et5rx6VmZ', '37i9dQZF1EQqA6klNdJvwx', '37i9dQZF1DX9C8KzGEUKV4', '37i9dQZF1DWSpF87bP6JSF', '3XffOiXW96Wb92yHL599q6', '37i9dQZF1EIdi2gB41AzQG']
generate_csv(playlist_ids, start_index=29503)