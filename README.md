# OTT API App: Headless Video Platform & Virtual FAST Channels

## Overview

**ott-api-app** is a functional prototype of a modern, API-first Over-the-Top (OTT) media service backend, built with Python and Flask. This project showcases key architectural concepts essential for scalable streaming platforms:

* **Content Management**
  A robust system for organizing video-on-demand (VOD) assets.

* **Dynamic Channel Creation**
  A sophisticated engine for generating rule-based “Virtual” FAST (Free Ad-supported Streaming TV) channels.

* **Headless Architecture**
  A dedicated API layer designed to serve content and playback logic to diverse client applications.

* **Dark-Themed Admin UI**
  The entire system’s backend functionality is managed through a comprehensive web interface.

---

## Core Features

* **API-First Design**
  Implemented using Flask Blueprints (`api_routes.py`), providing clean JSON data for channels, video metadata, and playback URLs. This enables seamless integration with various frontends.

* **Virtual FAST Channel Engine**
  Dynamic scheduler in `app.py` automatically generates 24/7 linear-style channels from a VOD library based on admin-defined tag rules. It calculates real-time playlist positions and `seek_offset` for a continuous “lean-back” TV experience.

* **Comprehensive Admin Panel**
  A web-based interface for full content lifecycle management:

  * Uploading and managing video assets, descriptions, and posters
  * Creating, editing, and deleting content tags
  * Building and managing both manual and virtual channels

* **Cross-Platform Client Readiness**
  Proof-of-concept testing performed on:

  * **Fire TV Client**: HTML/JS single-page application demonstrating API data fetching and video playback on Fire Stick hardware (via Web App Tester)
  * **Roku Client**: Minimal BrightScript channel proving API connectivity and data retrieval on a physical Roku device via the debug console

* **Robust Backend**
  Utilizes Flask’s Application Factory pattern for a modular structure, with SQLAlchemy managing the SQLite database (`models.py`) and `extensions.py` for shared app components.

* **Content Seeding**
  Includes a `bulk_insert.py` script to quickly populate the database with sample content and tags for demonstration purposes.

---

## Tech Stack

* **Backend:** Python 3
* **Web Framework:** Flask
* **Database ORM:** SQLAlchemy
* **Database:** SQLite (development/prototyping)
* **API Layer:** Flask Blueprints, Flask-CORS
* **Admin UI & Viewer:** HTML5, CSS3, Bootstrap 5
* **Client Testing:** HTML/JS (Fire TV), BrightScript (Roku)

---

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/dcarley24/ott-api-app.git
   cd ott-api-app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   *(Note: Ensure you have a `requirements.txt` file created from your environment. Key dependencies include Flask, Flask-SQLAlchemy, Flask-CORS.)*

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Media Assets**

   ```bash
   mkdir -p uploads/videos uploads/posters
   ```

   * Place sample video files (e.g., `BigBuckBunny_320x180.mp4`) in `uploads/videos/`
   * Place corresponding poster images (e.g., `BigBuckBunny_320x180.jpg`) in `uploads/posters/`
     *(The `bulk_insert.py` script requires these source files to exist.)*

5. **Populate the Database**

   ```bash
   python app.py          # Creates ott_platform.db & tables
   python bulk_insert.py  # Populates sample videos & tags
   ```

6. **Run the Application**

   ```bash
   python app.py
   ```

   The app will be available at `http://127.0.0.1:5017` (or your configured Flask port).

---

## Testing the API Endpoints

* **All Channels (JSON)**

  ```
  http://YOUR_SERVER_IP:5017/api/channels
  ```

* **Specific Channel Playback Data (JSON)**

  ```
  http://YOUR_SERVER_IP:5017/api/channel/play/1
  ```

  *(Replace `1` with an actual virtual channel ID created via the admin UI.)*

---

## Project Vision & Future Enhancements

* **Rich Metadata Ingestion**
  Automated pipelines to pull detailed metadata (genre, cast, release year, etc.) from external providers.

* **Advanced Ad Insertion**
  Deeper integration with ad servers for complex pre-roll/mid-roll logic within FAST channels.

* **User Authentication & Profiles**
  Personalized viewing experiences and user management.

* **Production Deployment**
  Containerize with Docker and deploy to cloud PaaS (e.g., Render, Heroku) or IaaS (AWS, GCP, Azure) for scalability.

* **Native Client Development**
  Build full native apps for Android TV (Java/Kotlin), Roku (BrightScript), iOS, and Android to leverage this API backend.

---

**License**
MIT
