import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

# Set up the bot prefix and create a bot instance
bot_prefix = "!"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

# Load sensitive information from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID'))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_member_join(member):
    # Welcome new members (customize the message as needed)
    welcome_channel = member.guild.get_channel(YOUR_WELCOME_CHANNEL_ID)
    await welcome_channel.send(f"Welcome, {member.mention}!")

@bot.command(name='kick', pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    # Kick a member
    if ctx.message.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await log_action(ctx.author, member, 'kick', reason)
        await ctx.send(f"{member.mention} has been kicked.")
    else:
        await ctx.send("You don't have permission to kick members.")

@bot.command(name='ban', pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    # Ban a member
    if ctx.message.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await log_action(ctx.author, member, 'ban', reason)
        await ctx.send(f"{member.mention} has been banned.")
    else:
        await ctx.send("You don't have permission to ban members.")

@bot.command(name='clear', pass_context=True)
async def clear(ctx, amount: int):
    # Clear a specified number of messages in the channel
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages cleared.", delete_after=5)
        await log_action(ctx.author, None, 'clear', f"{amount} messages")
    else:
        await ctx.send("You don't have permission to manage messages.")

async def log_action(moderator, target, action, reason):
    # Log moderation actions to a specified channel
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    if target:
        log_message = f"{timestamp} | {moderator} {action} {target} | Reason: {reason}"
    else:
        log_message = f"{timestamp} | {moderator} {action} | Reason: {reason}"
    await log_channel.send(log_message)

# Run the bot with your token
bot.run(TOKEN)
