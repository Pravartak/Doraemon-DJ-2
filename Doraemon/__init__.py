from Doraemon.core.bot import DoraemonBot
from Doraemon.core.dir import dirr
from Doraemon.core.git import git
from Doraemon.core.userbot import Userbot
from Doraemon.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = DoraemonBot()

# Assistant Client
userbot = Userbot()

from Doraemon.platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
