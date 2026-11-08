# Tic-Tac-Toe

A web-based Tic-Tac-Toe application built with **React, Django, Django REST Framework, and Django Channels**. Play against the computer or challenge another player in real time using multiplayer rooms.

## Features

- **Single-player mode:** Play Tic-Tac-Toe against a computer opponent.
- **Multiplayer mode:** Create a game room and invite another player using a six-digit room code.
- **Real-time gameplay:** Moves are synchronized between players using WebSockets.
- **Game state management:** Track player turns, game outcomes, and board state.
- **Rematches:** Request and accept rematches after multiplayer games.
- **Connection handling:** Handle player disconnections and WebSocket reconnections.
- **Persistent game state:** Store game information in PostgreSQL.
- **Redis integration:** Use Redis as the Django Channels channel layer and for tracking online players in game rooms.

## Technology Stack

### Frontend
- React
- Material UI (MUI)
- React Router
- React Use WebSocket
- Webpack
- Babel

### Backend
- Python
- Django
- Django REST Framework
- Django Channels
- Daphne (ASGI server)

### Infrastructure
- PostgreSQL
- Redis
- WebSockets

## Architecture

The application uses Django as its backend and serves the React frontend through Django templates and static files.

- **React** handles the user interface and game interactions.
- **Django REST Framework** provides HTTP endpoints for game setup, room creation, room joining, and game-state retrieval.
- **Django Channels** handles WebSocket connections and real-time game communication.
- **Redis** provides the Channels message layer and tracks players connected to multiplayer rooms.
- **PostgreSQL** stores game records and their associated state.

### Real-time communication

The application uses two WebSocket endpoints:

| Endpoint | Purpose |
|---|---|
| `/ws/play-computer/` | Communication between the player and computer game |
| `/ws/play-multiplayer/<room_code>` | Real-time communication between multiplayer participants |

## Project Structure

```text
tictactoe/
├── computer/                 # Single-player game logic and API
├── frontend/                 # React frontend and Django frontend app
│   ├── src/                  # React source code
│   ├── static/                # Compiled frontend assets
│   ├── templates/             # Django HTML templates
│   └── webpack.config.js
├── multiplayer/              # Multiplayer game logic and API
├── tictactoe/                # Django project configuration
│   ├── asgi.py                # HTTP and WebSocket routing
│   ├── settings.py
│   └── urls.py
├── util/                     # Shared game and Redis utilities
├── .env.example
├── manage.py
├── requirements.txt
└── LICENSE
```

## Getting Started

### Prerequisites

Install the following before setting up the application:

- Python 3.10 or later
- Node.js and npm
- PostgreSQL
- Redis

### 1. Clone the repository

```bash
git clone -b websocket https://github.com/jaeyy101/tictactoe.git
cd tictactoe
```

### 2. Set up the Python environment

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root using the provided example:

```bash
cp .env.example .env
```

On Windows, you can copy the file manually or run:

```powershell
Copy-Item .env.example .env
```

Update the values in `.env` to match your local configuration:

```dotenv
SECRET_KEY=your-generated-django-secret-key
DEBUG=True

DB_NAME=tictactoe
DB_USER=postgres
DB_PASSWORD=your-postgresql-password
DB_HOST=localhost
DB_PORT=5432

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=
```

Generate a Django secret key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Use the generated value for `SECRET_KEY`.

### 4. Configure PostgreSQL

Create a PostgreSQL database and user matching the credentials in your `.env` file.

For example, using the PostgreSQL command-line client:

```sql
CREATE DATABASE tictactoe;
```

Ensure the configured database user has permission to access the database.

### 5. Start Redis

Make sure your Redis server is running and accessible using the host, port, and credentials configured in `.env`.

For a local Redis installation, the default configuration is:

```text
Host: localhost
Port: 6379
Database: 0
```

### 6. Apply database migrations

From the project root, run:

```bash
python manage.py migrate
```

### 7. Install frontend dependencies

Navigate to the frontend directory:

```bash
cd frontend
npm install
```

### 8. Build the frontend

For development, run Webpack in watch mode:

```bash
npm run dev
```

For a production build:

```bash
npm run build
```

Webpack outputs the compiled frontend assets to `frontend/static/frontend/`.

### 9. Start the Django application

Open another terminal, activate the Python virtual environment, and run:

```bash
python manage.py runserver
```

The application should now be accessible at:

```text
http://127.0.0.1:8000/
```

Keep Redis running and leave the frontend development watcher active while developing.

## API Overview

### Computer game

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/computer/games` | Retrieve computer game records |
| GET | `/api/computer/game` | Retrieve the current player's game |
| POST | `/api/computer/setup` | Set up a computer game |
| GET | `/api/computer/is-ingame` | Check whether the player has an active game |
| POST | `/api/computer/leave` | Leave the current game |

### Multiplayer game

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/multiplayer/games` | Retrieve multiplayer game records |
| POST | `/api/multiplayer/create` | Create a multiplayer room |
| PATCH | `/api/multiplayer/join` | Join an existing room |
| GET | `/api/multiplayer/get-game/<room_code>` | Retrieve a room's game state |

## Development Notes

- Django manages HTTP requests and serves the React application.
- WebSocket connections are handled through Django Channels and the ASGI application.
- Redis must be available for multiplayer channel communication and online-player tracking.
- The application uses session-based player identification.
- Frontend source changes are compiled using Webpack.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
