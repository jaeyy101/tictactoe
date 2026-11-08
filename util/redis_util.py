import os
import redis
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=int(os.getenv("REDIS_DB", 0)),
    password=os.getenv("REDIS_PASSWORD") or None,
    decode_responses=True,
    socket_timeout=5,
)

GAME_ROOM_ONLINE_PLAYERS_KEY = "game_room:{}"


def add_online_player(room_id, player_id):
    return redis_client.sadd(GAME_ROOM_ONLINE_PLAYERS_KEY.format(room_id), player_id)


def remove_online_player(room_id, player_id):
    return redis_client.srem(GAME_ROOM_ONLINE_PLAYERS_KEY.format(room_id), player_id)


def get_online_players_in_room_count(room_id):
    return redis_client.scard(GAME_ROOM_ONLINE_PLAYERS_KEY.format(room_id))


def is_game_ready(room_id):
    return redis_client.scard(GAME_ROOM_ONLINE_PLAYERS_KEY.format(room_id)) == 2
