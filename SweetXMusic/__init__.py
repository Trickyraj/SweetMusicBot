from SweetXMusic.core.bot import SweetXBot
from SweetXMusic.core.dir import dirr
from SweetXMusic.core.git import git
from SweetXMusic.core.userbot import Userbot
from SweetXMusic.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = SweetXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
