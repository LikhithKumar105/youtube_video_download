# YouTube Video Downloader

This little program downloads a YouTube video to your computer in the best quality it can find.

You only need to set it up one time. After that, downloading a video is just one command.

## Before you start

You need a Mac, Windows computer, or Linux computer with:

- **Python 3**
- **FFmpeg**

Ask a grown-up for help if you do not have them yet. FFmpeg helps the program join the video and sound together.

## Mac setup — do this one time

1. Download this project from GitHub. Click the green **Code** button, then **Download ZIP**.
2. Open the ZIP file. It makes a folder called `youtube_automation`.
3. Open **Terminal**.
4. Type this, then press Enter:

   ```bash
   cd ~/Downloads/youtube_automation
   ```

   If you put the folder somewhere else, change this path to where your folder is.

5. Make the program's little helper box by typing:

   ```bash
   python3 -m venv .venv
   ```

6. Turn on the helper box:

   ```bash
   source .venv/bin/activate
   ```

   You should now see `(.venv)` at the beginning of the Terminal line. That means it worked.

7. Install the downloader helper:

   ```bash
   pip install -r requirements.txt
   ```

8. Install FFmpeg. If you already have Homebrew, type:

   ```bash
   brew install ffmpeg
   ```

   If Terminal says `brew: command not found`, first install Homebrew from [brew.sh](https://brew.sh), then run the command above again.

## Download a video

1. Copy a YouTube video link.
2. In Terminal, make sure you are inside the project folder and see `(.venv)`.
3. Type this. Put your own YouTube link between the quotation marks:

   ```bash
   python app.py "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

4. Press Enter and wait. Big, high-quality videos can take a while.
5. Your finished video will be inside the `downloads` folder.

Example:

```bash
python app.py "https://www.youtube.com/watch?v=OvKCESUCWII"
```

## Next time

You do **not** need to install everything again. Just open Terminal and type:

```bash
cd ~/Downloads/youtube_automation
source .venv/bin/activate
python app.py "PASTE_YOUTUBE_LINK_HERE"
```

## If something goes wrong

- **`command not found: python`**: use `python3`, or turn on the helper box with `source .venv/bin/activate`.
- **`No module named yt_dlp`**: run `pip install -r requirements.txt` after turning on the helper box.
- **FFmpeg error**: run `brew install ffmpeg`.
- **Video cannot be downloaded**: it may be private, age-restricted, region-restricted, or unavailable.

Only download videos you own or are allowed to save. Please respect copyright and YouTube's terms.
