# Tic-Tac-Toe

A browser-based Tic-Tac-Toe application built with **React and Django**, featuring an AI-powered computer opponent with multiple difficulty levels.

The application combines a React frontend with a Django REST API backend to handle game sessions, player moves, computer decisions and game state persistence.

## Features

- **Play against the computer:** Challenge an AI opponent in a classic Tic-Tac-Toe game.
- **Multiple difficulty levels:** Choose between Easy, Medium, Hard and Impossible.
- **AI-powered opponent:** The computer uses the Minimax algorithm to evaluate possible moves and make strategic decisions.
- **Adjustable AI difficulty:** Lower difficulty levels introduce randomized moves, while higher levels favor optimal decisions.
- **Dynamic player assignment:** The player and computer are randomly assigned X or O.
- **Turn management:** The backend tracks game turns and validates whose turn it is.
- **Session-based gameplay:** Game state is associated with individual Django sessions.
- **Game management:** Start a game, replay, change difficulty or abandon an ongoing game.
- **WebSocket support:** Includes a Django Channels consumer and WebSocket routing for game-related communication.

## Technology Stack

### Frontend
- React 18
- React Router 6
- Material UI (MUI)
- Webpack 5
- Babel

### Backend
- Python
- Django 5.0.4
- Django REST Framework
- Django Channels
- SQLite

### Development and Configuration
- Node.js and npm
- Python virtual environments
- python-dotenv for environment variable management
- Git

## Architecture

The application follows a frontend/backend architecture.

- **React:** Handles the user interface, navigation, board rendering and player interactions.
- **Django:** Manages application routing, game sessions and persistence.
- **Django REST Framework:** Exposes API endpoints for game setup, player moves and computer moves.
- **Django Channels:** Provides WebSocket routing and a game consumer.
- **Minimax algorithm:** Evaluates possible game outcomes and helps the computer select strategic moves.
- **SQLite:** Stores game records and session data.

The current React gameplay flow communicates with the backend through HTTP API requests. Although WebSocket functionality is defined in the backend, it is not currently the primary communication mechanism used by the frontend.

## Project Structure

```text
tictactoe/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── App.js
│   │   │   ├── Board.js
│   │   │   ├── GameOver.js
│   │   │   ├── Homepage.js
│   │   │   ├── Play.js
│   │   │   ├── Routing.js
│   │   │   └── Setup.js
│   │   ├── index.js
│   │   └── ...
│   ├── static/
│   ├── templates/
│   ├── package.json
│   └── webpack.config.js
│
├── game/
│   ├── migrations/
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── serializers.py
│   ├── urls.py
│   ├── util.py
│   └── views.py
│
├── tictactoe/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── manage.py
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

Follow these instructions to run the application locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/jaeyy101/tictactoe.git
cd tictactoe
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

The application uses environment variables to manage sensitive configuration, including Django's secret key.

Create a `.env` file in the project root.

You can use `.env.example` as a starting point:

```bash
# Windows
copy .env.example .env
```

```bash
# macOS / Linux
cp .env.example .env
```

Generate a Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Open `.env` and replace the placeholder:

```env
SECRET_KEY=your-generated-secret-key
```

**Important:** Never commit your `.env` file or expose its contents publicly. The `.env` file is excluded through `.gitignore`.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Install frontend dependencies

```bash
cd frontend
npm install
```

### 7. Build the frontend

```bash
npm run build
```

This generates the frontend JavaScript bundle required by the Django application.

Return to the project root:

```bash
cd ..
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

You should now be able to access the application.

## API Endpoints

The backend exposes the following REST API endpoints under `/api/`:

| Endpoint | Method | Description |
|---|---|---|
| `/api/games` | GET | Retrieve game records. |
| `/api/game` | GET | Retrieve the current session's game. |
| `/api/setup` | POST | Create or configure a game. |
| `/api/is-ingame` | GET | Check whether a game exists for the current session. |
| `/api/leave` | POST | Abandon the current game and reset its state. |
| `/api/player-move` | PUT | Submit a player's move. |
| `/api/computer-move` | PUT | Request the computer's next move. |

### WebSocket Endpoint

The backend also defines a Django Channels WebSocket endpoint:

```text
/ws/game/
```

The WebSocket consumer handles game-related messages, including player moves and computer moves.

The current frontend gameplay implementation primarily uses the REST API.

## Game Logic

The computer opponent uses the **Minimax algorithm**, a decision-making algorithm commonly used in two-player games.

The algorithm evaluates possible game outcomes and selects moves based on their potential scores.

The available difficulty levels influence how frequently the computer chooses randomized moves instead of strategic Minimax decisions:

- **Easy:** Mostly randomized moves.
- **Medium:** A mixture of randomized and strategic moves.
- **Hard:** Primarily strategic moves.
- **Impossible:** Uses Minimax without intentionally randomized moves.

## Future Improvements

Potential areas for continued development include:

- Implementing fully functional player-versus-player gameplay.
- Improving WebSocket-based real-time communication.
- Adding better error handling and connection recovery.
- Expanding backend and frontend test coverage.
- Improving frontend responsiveness and accessibility.
- Introducing game statistics and match history.
- Improving application security and deployment configuration.
- Refactoring the backend game logic for better maintainability.

## Contributing

Contributions, suggestions and bug reports are welcome.

If you would like to contribute, feel free to open an issue or submit a pull request.

## License

See the repository's `LICENSE` file for licensing information.