import datetime
import time
import random
from nba_api.stats.endpoints import Scoreboard
from nba_api.stats.endpoints import PlayByPlay
from nba_api.stats.endpoints import playbyplay
from nba_api.stats.library.parameters import LeagueID
from nba_api.stats.library.eventmsgtype import EventMsgType
from nba_api.stats.library.playbyplayregex import eventmsgtype_to_re

for a in eventmsgtype_to_re:
    for re in eventmsgtype_to_re[a]:
        print("{}: {}".format(a, re.pattern))