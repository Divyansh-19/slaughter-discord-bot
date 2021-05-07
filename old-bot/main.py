import discord
import os
import requests
import json
import webbrowser
from time import sleep

client = discord.Client()

def get_quote():
  response = requests.get ('https://zenquotes.io/api/random')
  json_data = json.loads (response.text)
  quote = json_data[0] ['q'] + " -" + json_data[0]['a']
  return(quote)

def Respond():
    if message.content.startswith(["exit" or "goodbye" or "quit"]):
        exit()

@client.event
async def on_ready():
  print('{0.user} has Logged in !'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('https://tenor.com/view/narendra-modi-nerendra-gif-6160706')

  if message.content.startswith('who are you'):
    await message.channel.send('I am a Bot made by 𝔻𝕚𝕧𝕪𝕒𝕟𝕤𝕙𝟙𝟡#𝟜𝟙𝟘𝟟')

  if message.content.startswith('q gm'):
    await message.channel.send('Hey Good Morning !')

  if message.content.startswith('q what can you do'):
      await message.channel.send('I am still under development :/')

  if message.content.startswith('q abtyou'):
    await message.channel.send('Hello, I am bot being developed by @𝔻𝕚𝕧𝕪𝕒𝕟𝕤𝕙𝟙𝟡#𝟜𝟙𝟘𝟟, I can do only basic things, bcoz my developer didnt buy premium for me ;/ ')

  

  if message.content.startswith('q give spotify'):
    await message.channel.send(os.getenv('Spotify'))
    await message.channel.send("Enjoy the Best of Songs!")

  if message.content.startswith('q spotify chill me'):
    await message.channel.send('https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7?si=3a812a590dfa4493')

  if message.content.startswith('q spotify inception'):
    await message.channel.send('https://open.spotify.com/album/2qvA7HmSg1iM6XMiFF76dp?si=97701180e6844dcb>')
  
  if message.content.startswith('q give yt'):
    await message.channel.send(os.getenv('Youtube'))

  if message.content.startswith('q give money'):
    await message.channel.send('Ask that other Bot')

  
  
  if message.content.startswith('q help'):
    await message.channel.send('All Info here : ')

    await message.channel.send('All commands to start with *q* ')

    await message.channel.send('​ ')

    await message.channel.send('About me = q abtyou')

    await message.channel.send('Spotify => q give spotify')

    await message.channel.send('YouTube => q give yt')

    await message.channel.send('​ ')

    await message.channel.send('​Emoji Help')

    await message.channel.send('​ ')

    await message.channel.send('​q grin')

    await message.channel.send('​q laugh')

    await message.channel.send('​q poop')

    await message.channel.send('​q cry')

    await message.channel.send('​ ')
     
    await message.channel.send('GIF OP')

    await message.channel.send('​ ')

    await message.channel.send('noice')

    await message.channel.send('​ ')

    await message.channel.send('dId or dance')



  

  if message.content.startswith('q spotify help'):
    await message.channel.send('Chilling => https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7?si=3a812a590dfa4493')

    await message.channel.send('Inception => https://open.spotify.com/album/2qvA7HmSg1iM6XMiFF76dp?si=97701180e6844dcb>')

  if message.content.startswith('q rip gyaan'):
    await message.channel.send('https://www.youtube.com/watch?v=fF6T7GWPygk&t=62s')

  if message.content.startswith('q inspire me'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('bbye'):
    await message.channel.send('𝔹𝕪𝕖❕')


  

  if message.content.startswith('q grin'):
    await message.channel.send(':grin:')

  if message.content.startswith('q laugh'):
    await message.channel.send(':laughing:')

  if message.content.startswith('q poop'):
    await message.channel.send(':poop:')

  if message.content.startswith('q cry'):
    await message.channel.send(':cry:')

  

  if message.content.startswith('noice'):
    await message.channel.send('https://tenor.com/view/noice-nice-click-gif-8843762')

  if message.content.startswith('dId' or 'dance kar'):
    await message.channel.send('https://tenor.com/view/dancing-cute-baby-happy-dance-gif-7730100')

  if message.content.startswith('annoyed' or 'i m annoyed'):
    await message.channel.send('https://tenor.com/view/blank-stare-really-idontbelieveyou-side-gif-6151149')

  if message.content.startswith('waah' or 'excellent'):
    await message.channel.send('https://tenor.com/view/cricistan-amir-liaquat-amir-bhai-wah-wah-wah-gif-17404289')
  
  if message.content.startswith('bhangra'):
    await message.channel.send('https://tenor.com/view/modiji-bhangra-dance-happy-celebrate-gif-17569464')

  if message.content.startswith('brainless'):
    await message.channel.send('https://tenor.com/view/modi-ji-gif-18967085')

  if message.content.startswith('big brain'):
    await message.channel.send('https://tenor.com/view/big-brain-markiplier-gif-14835823')

  if message.content.startswith('thinking' or 'think'):
    await message.channel.send('https://tenor.com/view/think-gif-20734499')

  if message.content.startswith('wth'):
    await message.channel.send('https://tenor.com/view/kuch-bhi-arnab-angry-hindi-gif-15180956')

  if message.content.startswith('MotaBhai'):
    await message.channel.send('https://m.economictimes.com/thumb/msid-68940203,width-1200,height-900,resizemode-4,imgsize-139592/mukesh-ambani.jpg')

  if message.content.startswith('sus'):
    await message.channel.send('https://images.outlookindia.com/public/uploads/articles/2019/11/23/Amit-Shah-Twitter_571_855.jpg')

  

  if message.content.startswith('Fuck'):
      await message.delete()
      
  if message.content.startswith('phuck'):
      await message.delete()

  if message.content.startswith('ass'):
    await message.delete()

  

  if message.content.startswith('pls'):
    await message.delete()

  if message.content.startswith('Google'):
    await message.channel.send('https://www.google.com/search?q=google+cloud+source+repositories&rlz=1C1CHBD_enIN914IN914&oq=google&aqs=chrome.0.0i67j69i57j69i60l3j69i65l3.1133j0j7&sourceid=chrome&ie=UTF-8')

  

client.run(os.getenv('TOKENNEW'))
