import discord
from discord.ext import commands

class information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def channele(ctx):
        return ctx.message.channel.id == 827241970899484702 or ctx.message.channel.id == 827223619838541825

    @commands.command()
    @commands.check(channele)
    async def rank(self, ctx, user : discord.User = None):
        """if user.bot:
            return"""
        if user != None:
            author = ctx.guild.get_member(user.id)
        else:
            author = ctx.message.author

        seconListe = []

        guild = self.bot.get_guild(827685549027885117)
        for channel in guild.channels:
            discri = f"{channel.name[len(channel.name)-4]}{channel.name[len(channel.name)-3]}{channel.name[len(channel.name)-2]}{channel.name[len(channel.name)-1]}"
            if discri == author.discriminator:
                messages = await channel.history(limit = None).flatten()
                for message in messages:
                    message = message.content
                    message = message.split(" ")
                    try:
                        seconListe.append(int(message[0]))
                    except:
                        seconListe.append(0)
                heure = messages[len(messages)-1].content
                place = messages[len(messages)-2].content

        nombreMessage = 0
        for i in seconListe:
            nombreMessage += i
        if author.id == 720254559888605234 or author.id == 438022903305338890:
            mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre",
                    "novembre", "decembre"]
            creation = ctx.guild.created_at
            creation = str(creation)
            creation = creation.split('-')
            demarquation = creation[2].split(" ")
            heure = []
            for i in range(8):
                heure.append(demarquation[1][i])
            heure = f"{demarquation[0]} {mois[int(creation[1]) - 1]} {creation[0]} à {heure[0]}{heure[1]} h {heure[3]}{heure[4]} min et {heure[6]}{heure[7]} sec"
        colour = 0x08ebcf
        if author.id == 438022903305338890:
            place = "1er"
            colour = 0xeb0808
        elif author.id == 720254559888605234:
            place = "2eme"
            colour = 0x1deb08

        embed = discord.Embed(title = author.name, description = author.discriminator, color = colour)
        embed.set_thumbnail(url = author.avatar_url)
        embed.add_field(name = "messages envoyés", value = nombreMessage-1, inline = False)
        embed.add_field(name = "arrivé le", value = heure, inline = False)
        embed.add_field(name="position", value = place, inline=False)
        embed.set_footer(text = author.id)

        await ctx.send(embed = embed)

    @commands.command()
    @commands.check(channele)
    async def serverinfo(self, ctx):
        guild = ctx.guild
        nBot = 0
        for member in guild.members:
            if member.bot:
                nBot += 1
        creation = ctx.guild.created_at
        embed = discord.Embed(title=ctx.guild.name, description="serveur sympa", color=0xeb9c08)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="nombre de membres", value = ctx.guild.member_count-nBot, inline=False)
        embed.add_field(name = "nombre de bot", value = nBot, inline = False)
        embed.add_field(name="nombre de salon textuel", value=len(ctx.guild.text_channels), inline=False)
        embed.add_field(name="nombre de salon vocaux", value=len(ctx.guild.voice_channels), inline=False)

        mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre",
                "novembre", "decembre"]
        creation = str(creation)
        creation = creation.split('-')
        demarquation = creation[2].split(" ")
        heure = []
        for i in range(8):
            heure.append(demarquation[1][i])
        a = f"le serveur à été créé le {demarquation[0]} {mois[int(creation[1]) - 1]} {creation[0]} à {heure[0]}{heure[1]} h {heure[3]}{heure[4]} min et {heure[6]}{heure[7]} sec"
        embed.set_footer(text=a)
        await ctx.send(embed=embed)
