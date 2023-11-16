import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16252145"))
API_HASH = getenv("API_HASH", "3c235bfd4e64b31ee11a25e47802ad6b")
BOT_TOKEN = getenv("BOT_TOKEN", "6907624117:AAHIU98IN3gWgcCQYrlXjxTp7v2B4pmjr5s")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ihsantopic:topicihsan@cluster0.jfejxle.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001983841726"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Spotify Bot")
OWNERS = int(getenv("OWNERS", "6811941116"))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6811941116").split())
)
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/YildizAtes21/Spotify",
)
KANAL = getenv(
    "KANAL", "BotsDuyuru"
)
GRUP = getenv(
    "GRUP", "BotsDestek"
)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "03052c5f8a324a58ad5cbb050b691d80")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2425bf87ba1f4a1fac3ae2e70eef2d39")

STRING1 = getenv("STRING_SESSION", "BAC_BZAWqVsSIA1X2QjQodLzrmQBs3T4pC1YcKl9Pfqii-wFr8fX5a2xyNDoeAgnYRBzANDtQT8Xc9Kd0d15GvRRbfsc3N32iLxwHHckkcf8e57UpkSalmfiTjHOUiA-iLU44289RMQfmbULT6nsCxR4G-XhUz44Kq-25oIbfV4IsBV04hUtp3QRDlja-GKKZNGkYAKqiyyjA9Qu95INkw8Oleu8H6UpqmHqwPPTag68yP6-eFXAa1SzDYKatdbbQynFGotTt-pxoRU0-kk4YB5y594Rt3UfTrEiktH1v3degL91a5cN4YoIhkVPgERbl20KVaITYe9rjlYaStGycFpAAAAAAYBgT_oA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "false")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "false")
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "false")
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "30"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "50"))
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "20"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "500")
) 
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "500")
)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "99999")
)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400")
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", None
)
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", None
)
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
SET_CMDS = getenv("SET_CMDS", False)
GITHUB_REPO = getenv("GITHUB_REPO", None)

#  __     ___    _ _  ___  _______   __  __ _    _  _____ _____ _____   ____   ____ _______
#  \ \   / / |  | | |/ / |/ /_   _| |  \/  | |  | |/ ____|_   _/ ____| |  _ \ / __ \__   __|
#   \ \_/ /| |  | | ' /| ' /  | |   | \  / | |  | | (___   | || |      | |_) | |  | | | |
#    \   / | |  | |  < |  <   | |   | |\/| | |  | |\___ \  | || |      |  _ <| |  | | | |
#     | |  | |__| | . \| . \ _| |_  | |  | | |__| |____) |_| || |____  | |_) | |__| | | |
#     |_|   \____/|_|\_\_|\_\_____| |_|  |_|\____/|_____/|_____\_____| |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/06e1f840ebbe0fb19f127.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
