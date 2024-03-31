import os
import discord

from openai import OpenAI

openai = OpenAI()

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def cat_message(content):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content},
        ]
        )

    choice = response.choices[0]
    message = choice.message.content
    return message


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if 'walter' in message.content.lower():
        await message.channel.send('Walter is a cat!')

    if 'cat' in message.content:
        await message.channel.send(cat_message(message.content))

    if '1+1' in message.content.replace(' ', ''):
        await message.channel.send('1+1 is 11')




client.run(os.getenv('CAT_DISCORD_TOKEN', ''))

