import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Predefined educational messages
educational_messages = [
    "Stay curious and keep learning!",
    "Knowledge is power. Read a book today!",
    "Remember, every expert was once a beginner.",
    "Learning never exhausts the mind!"
]

# Function to send messages to all members
async def send_message_to_all(ctx):
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(educational_messages[0])  # Sends the first message
                print(Fore.GREEN + f"Message sent to {member.name}")
            except:
                print(Fore.RED + f"Could not send message to {member.name}")

# Function to send a message to a specific member
async def send_message_to_specific(ctx, member_name):
    member = discord.utils.get(ctx.guild.members, name=member_name)
    if member and not member.bot:
        try:
            await member.send(educational_messages[1])  # Sends the second message
            print(Fore.GREEN + f"Message sent to {member.name}")
        except:
            print(Fore.RED + f"Could not send message to {member.name}")
    else:
        print(Fore.RED + f"Member {member_name} not found or is a bot.")

# Bot commands
async def run_bot(token):
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(Fore.CYAN + f"Bot is ready! Logged in as {bot.user}")

    @bot.command()
    async def menu(ctx):
        await ctx.send(Fore.CYAN + Style.BRIGHT + """
        ███╗   ██╗██╗   ██╗██╗   ██╗███████╗███╗   ███╗
        ████╗  ██║██║   ██║██║   ██║██╔════╝████╗ ████║
        ██╔██╗ ██║██║   ██║██║   ██║█████╗  ██╔████╔██║
        ██║╚██╗██║██║   ██║██║   ██║██╔══╝  ██║╚██╔╝██║
        ██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║ ╚═╝ ██║
        ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝     ╚═╝
        """ + Fore.YELLOW + Style.BRIGHT + """
        Author: Stan
        """ + Fore.GREEN + """
        01. Send Educational Message to All Members
        02. Send Educational Message to Specific Member
        03. Exit
        """)

    @bot.command()
    async def option(ctx, choice: str):
        if choice == "01":
            await send_message_to_all(ctx)
        elif choice == "02":
            await ctx.send("Enter the member's name:")
            member_name = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            await send_message_to_specific(ctx, member_name.content)
        elif choice == "03":
            await ctx.send("Exiting...")
            await bot.close()
        else:
            await ctx.send("Invalid choice. Try again.")

    await bot.start(token)

# List of tokens
tokens = [
    "MTM0MTcwNDkxMzA3OTc2Mjk4Ng.GQzVYt.LiffoKhKINjaOYvG8Xf-mhRbcnhvOP682T53Rc",

]
# Run all bots
async def main():
    tasks = [run_bot(token) for token in tokens]
    await asyncio.gather(*tasks)

asyncio.run(main())
