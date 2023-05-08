import os
import discord
import openai

from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
opneai_key = os.getenv('OPENAI_KEY')

openai.api_key = opneai_key

intents = discord.Intents.all()
client = discord.Client(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prompt = message.content
        
    if client.user.mentioned_in(message):
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            temperature = 0.5,
            max_tokens = 256,
            top_p = 1.0,
            frequency_penalty = 0.0,
            presence_penalty = 0.0
        )
        await message.channel.send(response.choices[0].text)

client.run(token)