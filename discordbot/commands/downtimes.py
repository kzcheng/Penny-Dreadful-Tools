from discord.ext import commands

from discordbot.command import MtgContext
from magic import fetcher

@commands.command
async def downtimes(ctx: MtgContext) -> None:
    await ctx.send(fetcher.downtimes())
