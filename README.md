OTT API App: Dynamic Streaming Platform Prototype
This repository contains the backend for a lightweight, API-first Over-The-Top (OTT) video platform built from scratch using Python and Flask. This project serves as a proof-of-concept exploring flexible content management and dynamic streaming solutions often missing in more rigid enterprise systems.

It's designed to decouple the content and business logic from the frontend presentation, allowing a single backend to power various client applications (web, mobile, smart TVs, etc.).

Key Features & Architecture
Flask Application Factory Pattern: A clean, scalable application structure that cleanly separates configuration, extensions, and routes.

Modular API Layer: Dedicated Flask Blueprints (api_routes.py) provide a headless REST API for fetching channels, video metadata, and playback URLs, designed for consumption by external clients.

Virtual FAST Channel Engine: A core innovation that dynamically generates 24/7 linear-style channels from a Video-on-Demand (VOD) library. Channels are defined by simple, tag-based rules (e.g., "all 'comedy' videos"), and the backend calculates real-time playback positions to provide a seamless "live TV" experience.

Robust Content Management System (CMS):

models.py: Centralized SQLAlchemy database schema for Videos, Tags, Channels, ChannelSchedule, and Ads.

Admin UI: A comprehensive web-based interface for CRUD operations on videos and tags, and for creating/managing both manual and dynamic virtual channels.

Local Content Storage: Handles storage and serving of video (uploads/videos) and poster (uploads/posters) assets.

Cross-Platform Client Readiness: The API is built to serve content to various frontends. Proof-of-concept client testing has been performed on:

Web Browser: Standard HTML/CSS/JS frontend for admin and basic viewing.

Fire TV Client: An HTML/JS single-page application successfully fetching data and playing content on a Fire Stick via Web App Tester.

Roku Client: A minimal BrightScript channel successfully demonstrated API connectivity via debug console.

Deployment Ready: Includes requirements.txt for easy dependency management in cloud environments (e.g., PythonAnywhere, Heroku).

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8+

pip (Python package installer)

ffmpeg (for local video processing/metadata extraction, though not directly in the provided Flask code for runtime use yet)

A Fire TV Stick (for client testing)

A Roku device (for client testing)

adb (Android Debug Bridge) installed on your machine (for Fire TV)

Installation & Setup
Clone the repository:

git clone https://github.com/dcarley24/ott-api-app.git
cd ott-api-app

Create a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Prepare .env file:
Create a .env file in the project root with necessary configurations. For local development, you might need:

FLASK_APP=app.py
FLASK_ENV=development
FLASK_SECRET_KEY='your_random_secret_key_here'
# Optional: If you use an external AI API for any future features in this repo
# GOOGLE_API_KEY='your_google_ai_studio_key'

Set up uploads directory:
Create uploads/videos and uploads/posters folders. Place sample .mp4 video files and corresponding .jpg poster images inside these folders.

mkdir -p uploads/videos uploads/posters
# Copy your BigBuckBunny_320x180.mp4 and .jpg here for bulk_insert.py

Initialize the database and insert sample data:

python app.py # This will create ott_platform.db and necessary tables
python bulk_insert.py # Populates the database with sample videos and tags

Running the Application
flask run --host=0.0.0.0 --port=5017
# Or, if you have it in app.py's __name__ == '__main__': block
# python app.py

The application will be accessible at http://YOUR_SERVER_IP:5017.

Testing the API Endpoints (via Browser or curl)
All Channels (JSON): http://YOUR_SERVER_IP:5017/api/channels

Specific Channel Playback (JSON): http://YOUR_SERVER_IP:5017/api/channel/play/1 (replace 1 with an actual virtual channel ID after creating one in the admin UI)

Testing on Fire TV / Roku
This backend provides data to a separate frontend client. For testing on hardware:

Fire TV: Use the Amazon Web App Tester app on your Fire Stick. Serve your firestick_test_app/index.html (which talks to this API) from a simple local web server on your development machine (python3 -m http.server in firestick_test_app directory) and point the Web App Tester to http://YOUR_MAC_IP:8000.

Roku: A basic BrightScript test app (like the roku_test_app discussed) can be sideloaded to your Roku device to test API connectivity via its debug console.

Project Vision & Future Enhancements
This project demonstrates a core understanding of how to build a scalable OTT backend. Future enhancements could include:

Rich Metadata Ingestion: Moving beyond basic tags to full metadata schemas (genre, cast, release year, etc.) via external APIs (e.g., Gracenote, TiVo).

Advanced Ad Insertion Logic: Deeper integration with Ad Servers (e.g., Google Ad Manager) for pre-roll, mid-roll, and post-roll ad breaks in FAST channels.

User Authentication & Profiles: For personalized experiences and watchlists.

Production Deployment: Containerization with Docker and deployment to cloud services (AWS, GCP, Azure) for scalability and reliability.

Native Client Development: Building full native applications for Android TV/Fire TV (Java/Kotlin) and Roku (BrightScript) that leverage this robust API backend.
