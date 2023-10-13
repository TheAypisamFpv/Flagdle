import os
import requests


with open(".env", "r") as f:
    webhook_url = f.read()
    webhook_url = webhook_url.split("=")[1]
    
user_name = os.getlogin()
    
def save_score(score, game):
    prev_score = get_score()
    prev_score = int(prev_score.split(":")[2]) if ":" in prev_score else 0
    high_score = f"{user_name}:{game}:{score}"
    if prev_score < score:
        try:
            with open("high_score.txt", "w") as f:
                f.write(high_score)
            send_high_score()
            return 0
        except:
            return 1

def get_score():
    try:
        with open("high_score.txt", "r") as f:
            score = f.read()
        return score
    except:
        return "No high score yet !"



def send_high_score():
    score = get_score()
    
    username, game, score = score.split(":") if ":" in score else ("none", "none", "none")
    # good looking embed
    json = {
        "embeds": [
            {
                "title": f"New High Score !",
                "description": f"{username} just got a new high score in {game} : {score} !",
                "color": 0x00ff00
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1083744401970450532/1162283609303023666/il.png?ex=653b5ff6&is=6528eaf6&hm=3ff6e52b41c98476c8db696d0c2fd874a8c1f6744c914060732bb41733f6c1ce&"
    }

    error_code = requests.post(webhook_url, json=json)
    return 0
