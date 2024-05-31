import streamlit as st
from pytube import YouTube
import tempfile
import os

st.title("YouTube Video Downloader")

video_url = st.text_input("Paste your URL")

progress_bar = st.progress(0)

def download_youtube_video(video_url):
    try:

        yt = YouTube(video_url, on_progress_callback=progress_callback)

        video_stream = yt.streams.get_highest_resolution()

        temp_dir = tempfile.mkdtemp()
        video_path = video_stream.download(output_path=temp_dir)

        video_filename = os.path.basename(video_path)

        with open(video_path, "rb") as file:
            video_bytes = file.read()

        return video_filename, video_bytes
    except Exception as e:
        st.text(f"Error: {str(e)}")
        return None, None

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size
    progress_bar.progress(progress)

if st.button("Download"):
    if video_url:
        video_filename, video_bytes = download_youtube_video(video_url)
        if video_filename and video_bytes:
            st.download_button(label="Download Video",
                               data=video_bytes,
                               file_name=video_filename,
                               mime="video/mp4")
        else:
            st.warning("Failed to download the video.")
    else:
        st.warning("Please paste the YouTube video URL.")
