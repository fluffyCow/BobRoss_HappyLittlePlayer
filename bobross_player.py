import os
import random
import time
import requests
import vlc

# Replace with your actual YouTube Data API key
YOUTUBE_API_KEY = "YOUR_API_KEY"
CHANNEL_ID = "UCBVN9zNfGz3qXnH3dGqNNXA"  # Bob Ross official channel
CHECK_INTERVAL = 300  # seconds between live checks

LOCAL_EPISODE_DIR = os.path.expanduser("~/bob_ross")

def get_live_video_id():
    url = (
        f"https://www.googleapis.com/youtube/v3/search?"
        f"part=snippet&channelId={CHANNEL_ID}&eventType=live&type=video&key={YOUTUBE_API_KEY}"
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        if items:
            return items[0]["id"]["videoId"]
    except Exception as e:
        print(f"Error checking live stream: {e}")
    return None

def play_youtube(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Playing live stream: {url}")
    player = vlc.MediaPlayer(url)
    player.play()
    return player

def get_local_episodes():
    episodes = []
    for root, _, files in os.walk(LOCAL_EPISODE_DIR):
        for file in files:
            if file.lower().endswith(".mp4"):
                episodes.append(os.path.join(root, file))
    return episodes

def play_local_episode():
    episodes = get_local_episodes()
    if not episodes:
        print("ERROR: No local episodes found.")
        return None
    episode = random.choice(episodes)
    print(f"Playing local episode: {episode}")
    player = vlc.MediaPlayer(episode)
    player.play()
    return player

def is_player_playing(player):
    return player and player.get_state() in [vlc.State.Playing, vlc.State.Buffering]

def main():
    current_player = None
    playing_live = False

    while True:
        video_id = get_live_video_id()
        if video_id:
            if not playing_live:
                if current_player:
                    current_player.stop()
                current_player = play_youtube(video_id)
                playing_live = True
        else:
            if not is_player_playing(current_player):
                current_player = play_local_episode()
                playing_live = False

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
