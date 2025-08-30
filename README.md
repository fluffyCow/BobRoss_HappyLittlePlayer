# BobRoss_HappyLittlePlayer

Welcome to the **Bob Ross - A Happy Little Player**—a Raspberry Pi-powered media player that brings Bob Ross’s soothing brushstrokes to your screen, 24/7.

This project checks for a live stream from the official Bob Ross YouTube channel and plays it using VLC. If no stream is live, it randomly selects a local episode from your personal collection and plays it instead. It’s a happy little hybrid of automation and relaxation. The code can be modified to play streams other than Bob Ross's, but why would you?

---

## Features

- ✅ Automatically detects live streams from Bob Ross’s YouTube channel
- ✅ Plays the stream until it ends, then checks again every 5 minutes
- ✅ Falls back to randomly playing local `.mp4` episodes
- ✅ Monitors for new live streams in the background and interrupts local playback if one starts
- ✅ Runs quietly in the background or as a boot-time service

---

## Getting Started

### 1. Install VLC and Python dependencies

```bash
sudo apt update
sudo apt install vlc python3 python3-pip
pip3 install requests python-vlc
```

### 2. Clone this repository
```bash
git clone https://github.com/fluffyCow/bob-ross-player.git
cd bob-ross-player
```

### 3. Add your YouTube API key
Create a free API key via Google Cloud Console (https://developers.google.com/youtube/v3/getting-started) and paste it into bobross_player.py:
```python
YOUTUBE_API_KEY = "YOUR_API_KEY"
```

### 4. Organize your episodes
Place your .mp4 files in:
```bash
/home/YOUR_USERNAME/bob_ross/
```
You can use subfolders like:
```bash
/home/YOUR_USERNAME/bob_ross/Season1/
```
## Run the Player
```
python3 bobross_player.py
```
Or run it in the background
```
nohup python3 bobross_player.py > ~/bobross.log 2>&1 &
```
## Autostart on Boot (Optional)
Create a systemd service:
```
[Unit]
Description=Bob Ross Player
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/bobross_player.py
WorkingDirectory=/home/YOUR_USERNAME
StandardOutput=append:/home/YOUR_USERNAME/bobross.log
StandardError=append:/home/YOUR_USERNAME/bobross.log
Restart=always
User=YOUR_USERNAME

[Install]
WantedBy=multi-user.target
```
Enable it
```
sudo systemctl daemon-reexec
sudo systemctl enable bobross.service
sudo systemctl start bobross.service
```
