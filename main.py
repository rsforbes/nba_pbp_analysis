import datetime
import time
import operator
import random
from nba_api.stats.endpoints import Scoreboard
from nba_api.stats.endpoints import PlayByPlay
from nba_api.stats.endpoints import playbyplay
from nba_api.stats.library.parameters import LeagueID
from nba_api.stats.library.eventmsgtype import EventMsgType
from nba_api.stats.library.playbyplayregex import eventmsgtype_to_re

season_date = datetime.datetime(2018, 10, 1)
end_of_season_date = datetime.datetime(2018, 10, 1)

def get_games(game_date):
    gamefinder = Scoreboard(league_id=LeagueID.nba,
                                day_offset=0,
                                game_date=game_date) 

    games_dict = gamefinder.get_normalized_dict()
    games = []
    for game in games_dict['GameHeader']:
        games.append(game['GAME_ID'])

    return games

def get_play_by_play(game_id):
    # Delay briefly to prevent throttling
    time.sleep(.6)
    return PlayByPlay(game_id).get_normalized_dict()['PlayByPlay']

event_msg_action_types = {}
description = ''

while season_date < end_of_season_date:
        
    games = get_games(season_date)


    for game_id in games:
        print(game_id)
        plays = get_play_by_play(game_id)

        for play in plays:

            if play["EVENTMSGTYPE"] != 5: continue

            for count in range(0, 1):
            
                description = play["HOMEDESCRIPTION"] if count == 0 else play["VISITORDESCRIPTION"]
                
                if description is None: continue

                if "STEAL" in description: continue  


                if play['EVENTMSGACTIONTYPE'] not in event_msg_action_types:
                    print(description)
                    event_msg_action_types[play['EVENTMSGACTIONTYPE']] = description

    #increment day by 1            
    season_date += datetime.timedelta(days=1)

#sort it all
event_msg_action_types = sorted(event_msg_action_types.items(), key=operator.itemgetter(0))

#output a class that we could plug into our code base
for action in event_msg_action_types:
    print(f'\t{action[0]} = {action[1]}')