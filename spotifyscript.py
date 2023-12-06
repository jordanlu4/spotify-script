import tkinter as tk
from tkinter import PhotoImage
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify API credentials
SPOTIPY_CLIENT_ID = 'YOUR ID' # Removed mine for security   
SPOTIPY_CLIENT_SECRET = 'YOUR SECRET'# Removed mine for security 
SPOTIPY_REDIRECT_URI = 'http://localhost:2000'
SCOPE = 'user-read-currently-playing user-modify-playback-state'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

# Main GUI Application
class SpotifyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Spotify Controller')
        self.geometry('300x150')  # Set the window size

        # Song Information
        self.song_title = tk.StringVar()
        self.song_artist = tk.StringVar()
        
        tk.Label(self, textvariable=self.song_title, fg='green', font=('Helvetica', 12, 'bold')).pack()
        tk.Label(self, textvariable=self.song_artist, fg='green', font=('Helvetica', 10)).pack()
        
        # Frame for Playback Controls
        controls_frame = tk.Frame(self)
        controls_frame.pack(expand=True)
        
        # Playback Controls
        tk.Button(controls_frame, text="Play", command=self.play_song).pack(side='left', expand=True)
        tk.Button(controls_frame, text="Pause", command=self.pause_song).pack(side='left', expand=True)
        tk.Button(controls_frame, text="Next", command=self.next_song).pack(side='left', expand=True)
        tk.Button(controls_frame, text="Previous", command=self.prev_song).pack(side='left', expand=True)
        
        self.update_song_info()
    
    
    def update_song_info(self):
        current_track = sp.current_user_playing_track()
        if current_track:
            self.song_title.set(current_track['item']['name'])
            self.song_artist.set(current_track['item']['artists'][0]['name'])
        else:
            self.song_title.set("No song playing")
            self.song_artist.set("")
        # Schedule the update_song_info to run every second
        self.after(1000, self.update_song_info)

    def play_song(self):
        sp.start_playback()  # This will resume playback

    def pause_song(self):
        sp.pause_playback()  # This will pause playback

    def next_song(self):
        sp.next_track()  # Skip to next song

    def prev_song(self):
        sp.previous_track()  # Skip to previous song

# Run the application
if __name__ == '__main__':
    app = SpotifyApp()
    app.mainloop()