import os
import requests


with open(".env", "r") as f:
    webhook_url = f.read()
    webhook_url = webhook_url.split("=")[1]
    
global user_name 
user_name = os.getlogin()
    
def save_score(score, game):
    global user_name
    # dict of the lines in the high score file
    high_socres = {}
    for line in get_score():
        if len(line) > 5:
            user_name ,game_mode, prev_score = line.removesuffix("\n").split(":")
            high_socres[game_mode] = prev_score


    #  if the game is not in the high score file, add it
    if game not in high_socres:
        high_socres[game] = score
        send_high_score(game, score)

    
    if int(score) > int(high_socres[game]):
        high_socres[game] = score
        send_high_score(game, score)
        
    user_name = os.getlogin()
    # write the new high score file
    with open("high_score.txt", "w") as f:
        for game_ in high_socres:
            f.write(f"{user_name}:{game_}:{high_socres[game_]}\n")

    return 0

    

def get_score(game_mode="all"):
    if not os.path.exists("high_score.txt"):
        # create the high score file if it does not exist
        with open("high_score.txt", "w") as f:
            pass
               
    with open("high_score.txt", "r") as f:
        scores = f.readlines()
        if game_mode == "all":
            return scores
        else:
            for score in scores:
                if game_mode in score:
                    return int(score.split(":")[2])
            return 0




def send_high_score(game, score):
    
    # good looking embed
    json = {
        "embeds": [
            {
                "title": f"New High Score !",
                "description": f"{user_name} just got a new high score in `{game}` : {score} !",
                "color": 0x00ff00
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1083744401970450532/1162283609303023666/il.png?ex=653b5ff6&is=6528eaf6&hm=3ff6e52b41c98476c8db696d0c2fd874a8c1f6744c914060732bb41733f6c1ce&"
    }

    error_code = requests.post(webhook_url, json=json)
    return 0
