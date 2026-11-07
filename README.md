# Tic-Tac-Toe

A browser-based Tic-Tac-Toe game built with **React and Django**, featuring an AI-powered computer opponent with multiple difficulty levels.

The application combines a React frontend with a Django REST API backend to manage game sessions, player moves, computer decisions and game state.

## Features

- **Play against the computer:** Challenge an AI opponent in a classic Tic-Tac-Toe game.
- **Multiple difficulty levels:** Choose between Easy, Medium, Hard and Impossible.
- **AI-powered opponent:** The computer uses the Minimax algorithm to evaluate possible moves and make strategic decisions, with randomized behavior at lower difficulty levels.
- **Dynamic player assignment:** The player and computer are randomly assigned X or O.
- **Turn management:** The backend tracks whose turn it is and prevents moves when it is not the player's turn.
- **Game state persistence:** Game sessions and board states are stored using Django's database-backed session system and SQLite.
- **Game management:** Start a game, replay, change difficulty or abandon an ongoing game.
- **Responsive interface:** A React frontend built with Material UI.

## Technology Stack

### Frontend
- React 18
- React Router
- Material UI (MUI)
- Webpack
- Babel

### Backend
- Python
- Django 5.0.4
- Django REST Framework
- Django Channels
- SQLite

### Architecture

The application follows a frontend/backend architecture:

- React handles the user interface, navigation, board rendering and player interactions.
- Django manages application routing, game sessions and persistence.
- Django REST Framework exposes endpoints for game setup, player moves and computer moves.
- The computer opponent uses the Minimax algorithm to evaluate available moves.
- Django Channels provides a WebSocket consumer and routing endpoint for game communication.

The current React gameplay flow communicates with the backend through HTTP API requests.

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
├── manage.py
└── .gitignore
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

### 2. Set up the Python environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

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

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Install frontend dependencies

Navigate to the frontend directory:

```bash
cd frontend
npm install
```

### 6. Build the frontend

```bash
npm run build
```

This generates the frontend JavaScript bundle used by the Django application.

Return to the project root:

```bash
cd ..
```

### 7. Start the development server

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

### WebSocket

The project also defines a Django Channels WebSocket endpoint:

```text
/ws/game/
```

The WebSocket consumer handles game-related messages, including player moves and computer moves. The current React gameplay implementation primarily uses the REST API.

## Game Logic

The computer opponent uses the **Minimax algorithm**, a decision-making algorithm commonly used in two-player games.

The algorithm evaluates possible game outcomes and selects moves based on their potential scores.

Difficulty levels modify how frequently the computer chooses a random move instead of following the optimal Minimax strategy:

- **Easy:** Mostly randomized moves.
- **Medium:** A mixture of randomized and strategic moves.
- **Hard:** Primarily strategic moves.
- **Impossible:** Uses the strategic Minimax algorithm without intentionally randomized moves.

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