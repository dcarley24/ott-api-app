# OTT API App: Headless Video Platform & Virtual FAST Channels

## Overview
**ott-api-app** is a functional prototype of a modern, API-first Over-the-Top (OTT) media service backend, built with Python and Flask. This project showcases key architectural concepts essential for scalable streaming platforms, including:

- **Content Management**  
  A robust system for organizing video-on-demand (VOD) assets.
- **Dynamic Channel Creation**  
  A sophisticated engine for generating rule-based “Virtual” FAST (Free Ad-supported Streaming TV) channels.
- **Headless Architecture**  
  A dedicated API layer designed to serve content and playback logic to diverse client applications.
- **Dark-Themed Admin UI**  
  Full backend functionality is managed through a comprehensive web interface.

---

## Core Features

- **API-First Design**  
  Implemented using Flask Blueprints (`api_routes.py`), providing clean JSON data for channels, video metadata, and playback URLs.  
- **Virtual FAST Channel Engine**  
  Dynamic scheduler in `app.py` automatically generates 24/7 linear-style channels from a VOD library based on admin-defined tag rules. Calculates real-time playlist positions and `seek_offset` for a continuous “lean-back” TV experience.  
- **Comprehensive Admin Panel**  
  Web-based interface for full content lifecycle management, including:  
  - Uploading and managing video assets, descriptions, and posters  
  - CRUD operations for content tags  
  - Creating and managing both manual and dynamic virtual channels  
- **Cross-Platform Client Readiness**  
  Proof-of-concept testing on:  
  - **Fire TV Client** (HTML/JS SPA) via Web App Tester & ADB  
  - **Roku Client** (BrightScript POC) on physical hardware  
- **Robust Backend**  
  Utilizes Flask’s Application Factory pattern with:  
  - `models.py` & SQLite (via SQLAlchemy)  
  - `extensions.py` for shared components  
- **Content Seeding**  
  `bulk_insert.py` script for quick database population with sample videos & tags.

---

## Tech Stack

- **Backend**: Python 3  
- **Web Framework**: Flask  
- **Database ORM**: SQLAlchemy  
- **Database**: SQLite (development/prototyping)  
- **API Layer**: Flask Blueprints, Flask-CORS  
- **Admin UI & Viewer**: HTML5, CSS3, Bootstrap 5  
- **Client Testing**: HTML/JS (Fire TV), BrightScript (Roku)  

---

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dcarley24/ott-api-app.git
   cd ott-api-app
