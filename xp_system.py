from discord.ext import commands
import json
import random
import discord


with open('level.json', encoding='utf-8') as f:
  try:
    level = json.load(f)
  except ValueError:
    level = {}
    level['users'] = []


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        
        user = message.author.id
        new_xp = random.choice(range(5,25))
       
            
        

        for current_user in level['users']:
            last_xp= int(current_user['xp'])
            current_xp = last_xp + new_xp

            if message.author.bot: return

            if current_user['id'] == user:
                last_xp= int(current_user['xp'])
                current_xp = str(last_xp + new_xp)
                
                current_user['xp']= current_xp
                
                break
        else:
            level['users'].append({
                'id':user,
                'xp': new_xp,
            })
        
        with open('level.json','w+') as f:
            json.dump(level,f)

def setup(client):
    client.add_cog(Level(client))
        
