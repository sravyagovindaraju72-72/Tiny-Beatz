import csv
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Load Spotify Credentials
load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)

# 2. Pick genres to collect
GENRES = [
    # --- POP / MAINSTREAM ---
    "pop", "hyperpop", "indie pop", "k-pop", "j-pop",
    "dance pop", "electropop", "bedroom pop",

    # --- HIP-HOP / RAP ---
    "hip hop", "rap", "underground hip hop", "trap", "emo rap",
    "lofi hip hop", "conscious hip hop",

    # --- R&B / SOUL ---
    "r&b", "soul", "neo-soul", "alt r&b",

    # --- ROCK / METAL ---
    "rock", "indie rock", "alternative rock", "classic rock",
    "punk", "pop punk", "metal", "hard rock",

    # --- EDM / ELECTRONIC ---
    "edm", "house", "deep house", "progressive house",
    "techno", "trance", "electronic", "dubstep", "drum and bass",

    # --- ACOUSTIC / SINGER-SONGWRITER ---
    "acoustic", "folk", "indie folk", "singer-songwriter",

    # --- JAZZ / BLUES ---
    "jazz", "smooth jazz", "blues",

    # --- COUNTRY / AMERICANA ---
    "country", "americana",

    # --- CLASSICAL / INSTRUMENTAL ---
    "classical", "instrumental", "piano", "orchestral",

    # --- MOOD / VIBES (VERY IMPORTANT FOR RECOMMENDER!) ---
    "sad", "happy", "chill", "study", "focus", "romantic",
    "party", "workout", "sleep", "rainy day", "cozy", "aesthetic",

    # --- TIKTOK / AESTHETIC VIBES ---
    "viral", "tiktok", "aesthetic", "dreamy", "nostalgia", "throwback",
    "summer vibes", "late night", "driving", "gym",

    # --- WORLD / CULTURAL ---
    "latin", "reggaeton", "bollywood", "afrobeats", "afro pop",
    "korean r&b", "phonk",

    # --- HOLIDAY / SEASONAL ---
    "christmas", "holiday", "winter", "halloween",

    # --- EXTRA NICE ONES ---
    "lofi", "ambient", "nature sounds", "cinematic"
]


# 3. Search Spotify & collect songs
def get_songs_by_genre(genre, limit=100):
    print(f"Collecting songs for genre: {genre}")

    results = sp.search(q=f"genre:{genre}", type="track", limit=50)
    tracks = results["tracks"]["items"]

    songs = []
    for t in tracks:
        songs.append({
            "name": t["name"],
            "artist": t["artists"][0]["name"],
            "genre": genre
        })

    return songs

# 4. Save everything to a CSV file
csv_file = "music_data.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "artist", "genre"])
    writer.writeheader()

    for g in GENRES:
        rows = get_songs_by_genre(g)
        writer.writerows(rows)

print(f"\nDONE! CSV saved as {csv_file}")
