import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_all_playlist_tracks(client_id, client_secret, playlist_id_or_url):
    # Authenticate with Spotify
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    tracks = []
    try:
        # Initialize variables for pagination
        offset = 0
        limit = 100
        while True:
            # Fetch a batch of playlist tracks
            results = sp.playlist_items(playlist_id_or_url, offset=offset, limit=limit)
            for item in results['items']:
                track = item['track']
                if track:  # Check if the track data is valid
                    tracks.append({
                        'title': track['name'],
                        'artist': ", ".join(artist['name'] for artist in track['artists']),
                    })

            # Break the loop if no more tracks are available
            if len(results['items']) < limit:
                break

            # Move to the next batch
            offset += limit

    except Exception as e:
        print(f"An error occurred: {e}")

    return tracks

# Replace with your Spotify API credentials
client_id = '2dbd33f3e7144dcc83937c16c8f8a674'
client_secret = 'bf772ab0a3494498a73f5d25589ee3ac'

# Replace with the Spotify playlist URL or ID
playlist_id_or_url = '0mOzeDojBfeAXp6rJZ1BTt'  # Example: Use ID or 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M'

if __name__ == "__main__":
    playlist_tracks = get_all_playlist_tracks(client_id, client_secret, playlist_id_or_url)
    print(playlist_tracks)
