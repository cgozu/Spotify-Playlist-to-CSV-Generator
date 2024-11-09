# Spotify Playlist to CSV Generator / Generador de CSV de Playlist de Spotify

This Python script generates a CSV file from Spotify playlists. It retrieves various details about the songs in the playlists, including the song name, performer, genres, album name, and audio features.

Este script de Python genera un archivo CSV a partir de playlists de Spotify. Recupera varios detalles sobre las canciones en las playlists, incluyendo el nombre de la canción, el intérprete, los géneros, el nombre del álbum y las características de audio.

## Features / Características

- Retrieves song details from Spotify playlists.
- Includes song name, performer, genres, album name, and audio features.
- Handles duplicate song IDs.
- Skips songs without a preview URL.
- Allows specifying the starting index for the CSV.

- Recupera detalles de canciones de playlists de Spotify.
- Incluye el nombre de la canción, el intérprete, los géneros, el nombre del álbum y las características de audio.
- Maneja IDs de canciones duplicadas.
- Omite canciones sin URL de vista previa.
- Permite especificar el índice inicial para el CSV.

## Requirements / Requisitos

- Python 3.x
- `requests` library
- `pandas` library

- Python 3.x
- Biblioteca `requests`
- Biblioteca `pandas`

## Installation / Instalación

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Install the required libraries:
    ```sh
    pip install requests pandas
    ```

1. Clona el repositorio:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Instala las bibliotecas requeridas:
    ```sh
    pip install requests pandas
    ```

## Usage / Uso

1. Set your Spotify API credentials in the script:
    ```python
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    ```

2. Specify the playlist IDs and the starting index:
    ```python
    playlist_ids = ['YOUR_PLAYLIST_ID_1', 'YOUR_PLAYLIST_ID_2']
    generate_csv(playlist_ids, start_index=100)
    ```

3. Run the script:
    ```sh
    python datasetGenerator.py
    ```

1. Establece tus credenciales de la API de Spotify en el script:
    ```python
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    ```

2. Especifica los IDs de las playlists y el índice inicial:
    ```python
    playlist_ids = ['YOUR_PLAYLIST_ID_1', 'YOUR_PLAYLIST_ID_2']
    generate_csv(playlist_ids, start_index=100)
    ```

3. Ejecuta el script:
    ```sh
    python datasetGenerator.py
    ```

## Example / Ejemplo

```python
playlist_ids = ['0uM2YdatpMMTB89C7Yudwk', '37i9dQZF1DXcBWIGoYBM5M', '6u4GaztHbiN51Et5rx6VmZ', '37i9dQZF1EQqA6klNdJvwx', '37i9dQZF1DX9C8KzGEUKV4', '37i9dQZF1DWSpF87bP6JSF', '3XffOiXW96Wb92yHL599q6', '37i9dQZF1EIdi2gB41AzQG']
generate_csv(playlist_ids, start_index=1)
