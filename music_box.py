import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import webbrowser as wb
import time
import json


wb.open('https://open.spotify.com/')
time.sleep(60)

# Set your Spotify API credentials
CLIENT_ID = '3ba4d36c9f274e30868f1baf06c6a16a'
CLIENT_SECRET = '4b1588d752b64b258919ebabcb7e52f7'
SPOTIPY_REDIRECT_URI = 'https://open.spotify.com/'


button_pressed=False
button_index=1

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

button_1=22
button_2=29
button_3=31
button_4=32
button_5=33
button_6=35
button_7=36
button_8=37
button_9=38
button_10=40
led_pin=7








playlists=None

def button_1_callback(channel):
    global button_pressed
    global button_index
    print("Button 1 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=0

def button_2_callback(channel):
    global button_pressed
    global button_index
    print("Button 2 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=1
    
def button_3_callback(channel):
    global button_pressed
    global button_index
    print("Button 3 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=2
    
def button_4_callback(channel):
    global button_pressed
    global button_index
    print("Button 4 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=3
    
def button_5_callback(channel):
    global button_pressed
    global button_index
    print("Button 5 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=4
    
def button_6_callback(channel):
    global button_pressed
    global button_index
    print("Button 6 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=5
    
def button_7_callback(channel):
    global button_pressed
    global button_index
    print("Button 7 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=6
    
def button_8_callback(channel):
    global button_pressed
    global button_index
    print("Button 8 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=7
    
def button_9_callback(channel):
    global button_pressed
    global button_index
    print("Button 9 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=8
    
def button_10_callback(channel):
    global button_pressed
    global button_index
    print("Button 10 was pushed!")
    time.sleep(1)
    button_pressed=True
    button_index=9    



def play_playlist(playlist_index):
    global playlists
    print("Playlist index:",playlist_index)
  
    stop_all_playlists()
    
    selected_playlist_uri = playlists[playlist_index]['uri']
    playlist_tracks = sp.playlist_tracks(selected_playlist_uri)
    track_uris = [track['track']['uri'] for track in playlist_tracks['items']]
    sp.shuffle(device_id=device_id,state=True)
    time.sleep(2)
    sp.repeat(state='context',device_id=device_id)
    time.sleep(2)
    sp.start_playback(device_id=device_id, uris=track_uris)
    time.sleep(2)
    
  

def stop_all_playlists():
    
    sp.pause_playback(device_id=device_id)
    time.sleep(2)
    
        
        
GPIO.cleanup()

#button setup
GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led setup
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin,GPIO.LOW)#set led state low
# Setup event on pin 10 rising edge
GPIO.add_event_detect(button_1,GPIO.RISING,callback=button_1_callback)
GPIO.add_event_detect(button_2,GPIO.RISING,callback=button_2_callback)
GPIO.add_event_detect(button_3,GPIO.RISING,callback=button_3_callback)
GPIO.add_event_detect(button_4,GPIO.RISING,callback=button_4_callback)
GPIO.add_event_detect(button_5,GPIO.RISING,callback=button_5_callback)
GPIO.add_event_detect(button_6,GPIO.RISING,callback=button_6_callback)
GPIO.add_event_detect(button_7,GPIO.RISING,callback=button_7_callback)
GPIO.add_event_detect(button_8,GPIO.RISING,callback=button_8_callback)
GPIO.add_event_detect(button_9,GPIO.RISING,callback=button_9_callback)
GPIO.add_event_detect(button_10,GPIO.RISING,callback=button_10_callback)

#os.system(sporify_cmd)





# Set the scope for the Spotify API
scope = 'user-library-read playlist-read-private user-read-playback-state user-modify-playback-state'

# Authenticate with the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

devices = sp.devices()
for device in devices:
    print("device:",device)


if devices['devices']:
    # Use the first available device
    device_id = devices['devices'][0]['id']
    print(f"Using device: {devices['devices'][0]['name']}")
    GPIO.output(led_pin,GPIO.HIGH)
else:
    print("No available devices found. Please ensure a device is active on your Spotify account.")
    GPIO.output(led_pin,GPIO.LOW)
    GPIO.cleanup()
    exit()
    
# Specify the URIs of the playlists you want to include
playlist_uris = [
    'spotify:playlist:1bZlEMfqTdxAjQC0fbRd9l',
    'spotify:playlist:4cfZJS85P7UEotaXvi4oNN',
    'spotify:playlist:5AAGIQidKh0pmhKaQC59tw',
    'spotify:playlist:3iiqBtArbxNBsswMrrlTgr',
    'spotify:playlist:0V4s8gaTFBPpn04ID5djE9',
    'spotify:playlist:27O5dKMQpVzlY3WtoyPFp9',
    'spotify:playlist:1RJmLKNllOOrJTJPv4LmGq',
    'spotify:playlist:1asO3zrbG9cu5F26sTeBsv',
    'spotify:playlist:2fbd8TbnxSTLCjVVjcW9Dd',
    
    
]    
# Get the details of the specified playlists
playlists = [sp.playlist(uri) for uri in playlist_uris]
#print(playlists)

print("Press button")
while True:
    if (button_pressed):
        play_playlist(button_index)
        print("set button_pressed=False")
        button_pressed=False
        

GPIO.cleanup() # Clean up
