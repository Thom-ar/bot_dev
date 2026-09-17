import discord

# Configuração das intents (permissões do bot)
intents = discord.Intents.default()
intents.message_content = True

# Inicialização do cliente
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}!')

@client.event
async def on_message(message):
    # Evita que o bot responda a si mesmo
    if message.author == client.user:
        return

    # Comando simples de resposta
    if message.content.lower() == '!ping':
        await message.channel.send('Pong!')

# Insira o token do seu bot entre as aspas
client.run('')
