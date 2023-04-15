import discord
from discord.ext import commands
from gpt import gpt, prompts

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Loop through prompts and add each command and response to bot first time around
for command in prompts.prompts:
    @bot.command(name=command['name'])
    async def chat(ctx, *, user_input=None):
        command_name = ctx.command.name

        # Iterate through prompts to find the correct prompt for the command, by default only last prompt value is used if not iterating.
        for prompt in prompts.prompts:
            if prompt['name'] == command_name:
                response = gpt.chat_completion(prompt['prompt'], user_input)
                await ctx.send(response)

