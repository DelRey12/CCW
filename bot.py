import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()  # This enables the default intents
intents.typing = False  # You can adjust individual intents as needed
intents.message_content = True  # Add this line to enable message content intent

# Set up the bot's command prefix and create a bot instance
bot = commands.Bot(command_prefix='/', intents=intents)

# Define a function to create an embedded message for the event card
def create_event_card():
    embed = discord.Embed(title="Wrestling Event Card", color=discord.Color.blue())
    
    # Add matches to the event card
    matches = [
        ("Match 1", "Gregory Gains vs. Jason Lobo"),
        ("Match 2", "Wrestler C vs. Wrestler D"),
        ("Match 3", "Wrestler E vs. Wrestler F"),
        # Add more matches here
    ]
    
    for match in matches:
        embed.add_field(name=match[0], value=match[1], inline=False)
    
    return embed

# Define a command to display the event card
@bot.command(name='eventcard')
async def display_event_card(ctx):
    event_card = create_event_card()
    await ctx.send(embed=event_card)

# Run the bot using your bot token
bot.run('BOT_TOKEN')