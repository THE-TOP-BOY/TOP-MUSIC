from TopZ.core.bot import Dil
from TopZ.core.dir import dirr
from TopZ.core.git import git
from Topz.core.userbot import Userbot
from TopZ.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Top()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
