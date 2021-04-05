import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(loupgarou(bot))

class loupgarou(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def me(ctx):
        return ctx.message.author.id == 720254559888605234

    @commands.command()
    @commands.check(me)
    async def clear(self, ctx, num):
        messages = await ctx.channel.history(limit = num).flatten()
        await ctx.channel.delete_messages(messages)

    @commands.command()
    async def ya(self, ctx):
        await ctx.send("plop")