# 🎥 YouTube Video Downloader with Streamlit

Welcome to the **YouTube Video Downloader** project! This tool allows users to download videos from YouTube easily through a web-based interface built with Streamlit. It's intuitive, simple, and efficient—ideal for anyone looking to save YouTube videos for offline viewing. 🚀

![YouTube Video Downloader](https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg)

---

## ✨ Features

- **High-Resolution Downloads**: Download the highest available resolution for any YouTube video.
- **Real-time Progress Bar**: Track the download process with a dynamic progress bar.
- **Streamlit Interface**: Simple, elegant, and interactive interface for an enhanced user experience.
- **Download Button**: Directly download the video once it's processed and ready.
- **Error Handling**: Built-in error messages to guide users in case of an invalid URL or download issues.

---

## 🛠️ How It Works

1. **Paste the YouTube URL**: Enter the URL of the video you want to download in the input field.
2. **Download Process**: The downloader fetches the highest quality available and provides a download link.
3. **Real-time Feedback**: Watch the download progress in real-time with the progress bar.
4. **Save the Video**: Click the download button to save the video to your local machine in MP4 format.

---

## 🚀 Getting Started

To set up and run this project on your local machine, follow these simple steps.

### Prerequisites

Make sure you have **Python 3.6+** installed. You'll also need the following packages:

- [Streamlit](https://streamlit.io)
- [Pytube](https://pytube.io)

Install them by running:

```bash
pip install streamlit pytube
```

### Running the App

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
```

Then run the Streamlit app:

```bash
streamlit run app.py
```

This will launch the app in your default web browser, where you can paste the video URL and download the video.

---

## 📂 Project Structure

```bash
youtube-downloader/
│
├── app.py          # Main application file
├── README.md       # Project documentation (this file)
└── requirements.txt # Project dependencies
```

---

## 🎯 Key Functions

### 1. `download_youtube_video(video_url)`
This function takes a YouTube URL, retrieves the highest resolution video stream, and returns the file in byte format for downloading.

### 2. `progress_callback(stream, chunk, bytes_remaining)`
Handles real-time progress tracking and updates the progress bar on the UI.

---

## ⚡ Demo

![Demo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/YouTube_down_arrow.png/320px-YouTube_down_arrow.png)

- **Input a YouTube URL**: Simply copy and paste the URL of the video.
- **Watch the Progress Bar**: Real-time feedback as your video downloads.
- **Download the Video**: Click the button to download the video in MP4 format.

---

## 📄 License

This project is licensed under the MIT License. Feel free to modify and distribute the code.

---

## 📧 Contact

For any questions or issues, feel free to reach out:

- **Email**: chandruganeshan24@gmail.com
- **GitHub**: [github/chandru-g24](https://github.com/chandru-g24)

---

## 🌟 Future Enhancements

- Add support for downloading audio-only streams.
- Allow users to select different video resolutions.
- Add support for downloading YouTube playlists.

Feel free to contribute and suggest more features!
