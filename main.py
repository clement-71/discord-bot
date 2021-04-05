import discord
import time
import random
import info
from help import hilfen
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", description=":D", intents=intents)
bot.remove_command('help')
horl = hilfen()



@bot.event
async def on_ready():
    print(':D')
    message_count.start()


@bot.event
async def on_member_join(member):
    if member.guild != bot.get_guild(827221895421100123):
        return

    ch = bot.get_channel(828194069851275294)
    messages = await ch.history(limit = 1).flatten()
    if messages[0].content == "1":
        await member.kick()
        return

    guild = bot.get_guild(827685549027885117)
    try:
        channel = await guild.create_text_channel(str(member))
    except:
        print(f"probleme avec {member}")

    await channel.send(horl.horloge())
    await channel.send(f"vous etes la {member.guild.member_count - 4} personnes sur le serveur")

    guild = bot.get_guild(827221895421100123)


    def role(id):
        roles = guild.roles
        for role in roles:
            if role.id == id:
                return role

    time.sleep(1)
    await member.add_roles(role(827898259124256768))

    i = 0
    for mem in member.guild.members:
        if mem.bot:
            i += 1
    footers = [
        " Un potentiel Nouvelle éleve(e) ",
        " Accorder lui votre respect ",
        " C'est un(e) mec / meuf chouette ",
        " Un(e) meuf / mec qui plane ",
        " Il fait partie de l'élite ",
        " Encore une victime de M.Duboux ",
        " Partage les devoirs ou sinon va te faire voir ",
        " OH LE BO OH LA BELLE BETE",
        " Bouteille d'eau , Bouteille d'eau , Voulez vous une bouteille d'eau ? ",
        " Il a interet de rien faire en SES lui ",
        " Encore un mec qui a mis Mario sur sa calculette ",
        " J'espere que ce n'est pas l'imposteur ",
        " x+1 sa fait combien déja ? ",
        " Attention si il est scorpion c'est non ! ",
        " Il fait du vélo ( attention antoine ) ",
        " ET PAF il a bien visé le sanglier ",
        " A toi de le gérée Tao le Charo ! ",
        " C'est étrange je n'ai pas ce pokemon dans mon pokedex ",
        " j'espere que tu n'a pas oublier d'expurger le superflux de la boisson ",
        "IDIOOOOOOOOT"
    ]

    chan = bot.get_channel(827232270729216000)
    channel = member.guild.get_channel(827221895421100126)
    embed = discord.Embed(title=f"Bienvenue à {member}", description = f"va voir les regles dans le salon {chan.mention}", color=0xeb3108)
    embed.set_image(url=member.avatar_url)
    embed.add_field(name="place", value = f"tu es le(la) {member.guild.member_count - i} eme sur le serveur")
    embed.add_field(name = "arrivé le", value = horl.horloge())
    embed.set_footer(text=f"{random.choice(footers)}")
    await channel.send(embed=embed)

    rolea = role(827898259124256768)


    a = f"[ Hey ! {rolea.mention} ] Bienvenue dans ce salon qui explique rapidement les règles du serveur. Prenez le temps de lire et amuser vous :grin:"
    b = "                      1 - Respecter complètement les règles ( principe d'une règle enfaite )"
    c = "                      2 - Ne pas insulter ses copains :smile: ( sauf en cas de rigolol )"
    d = "                      3 - Ecrire de manière lisible ( sinon on va pas se comprendre )"
    e = "                      4 - Ne pas trop gueuler en vocal ( sinon c'est musolière direct )"
    f = "                      5 - Amuse toi un peu quand même."
    g = "                      6 - Partage les devoirs ( sa se fait pas sinon )"
    h = "                      7 - Respecter le staff ( il se sont donner du mal :(( )"
    mes = f"{a}\n\n{b}\n\n{c}\n\n{d}\n\n{e}\n\n{f}\n\n{g}\n\n{h}"

    channel = bot.get_channel(827232270729216000)
    messages = await channel.history(limit=None).flatten()
    await channel.delete_messages(messages)
    message = await channel.send(mes)
    await message.add_reaction('✅')

    use = bot.get_user(member.id)

    def checkReaction(reaction, user):
        return user == use and str(reaction.emoji) == '✅'

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=180, check=checkReaction)

        if reaction.emoji == '✅':
            await member.add_roles(role(827223809156710420))  # 827223809156710420
            await member.remove_roles(role(827898259124256768))
    except:
        await member.add_roles(role(827907525248679956))


@bot.event
async def on_message(message):
    if message.author.bot \
    or message.guild == bot.get_guild(827983934477566032) \
    or message.guild == bot.get_guild(827985593714606151):
        return

    r = random.random()
    if r > 0.99:
        await message.channel.send("re")

    async def recup(channelName):
        liste = []
        guildAuthor = bot.get_guild(827983934477566032)
        for channel in guildAuthor.channels:
            if channel.name == channelName:
                messages = await channel.history(limit=None).flatten()
                for mes in messages:
                    liste.append(mes.content)
        return liste

    async def relance(channelName):
        liste = []
        guildBot = bot.get_guild(827985593714606151)
        for channel in guildBot.channels:
            if channel.name == channelName:
                messages = await channel.history(limit=None).flatten()
                for mes in messages:
                    liste.append(mes.content)
        return liste

    listeExclusAuthor = await recup("exclus")
    listeExclusBot = await relance("exclus")

    if message.content in listeExclusAuthor:
        reponsed = random.choice(listeExclusBot)
        await message.channel.send(reponsed)

    smes = message.content
    smes = smes.split(" ")

    for i in smes:
        if i in listeExclusAuthor:
            reponsed = random.choice(listeExclusBot)
            await message.channel.send(reponsed)
        if i == "coronavirus" or i == "covid-19" or i == "covid":
            await message.channel.send("conard de virus")

    listeBonjourAuthor = await recup("salut")
    listeBonjourBot = await relance("salut")
    listeCavaBot = await relance("ca-va")
    listeCavaAuthor = await recup("ca-va")

    reponsea = random.choice(listeBonjourBot)
    reponseb = random.choice(listeCavaBot)

    channel = bot.get_channel(828028042319626290)

    messs = await channel.history(limit=1).flatten()
    oldtime = messs[0].content

    messa = (message.content).split(" ")
    a = 0
    for i in messa:
        for mem in message.guild.members:
            if i == mem.name:
                a += 1
    for i in messa:
        if i in listeBonjourAuthor and time.time() - 100 > float(oldtime) and a == 0:
            await channel.send(time.time())
            await message.channel.send(f"{reponsea} {message.author.name}")
            await message.channel.send(reponseb)

            def checkMessage(mes):
                return mes.author == message.author and mes.channel == message.channel

            try:
                reponse = await bot.wait_for('message', timeout=10, check=checkMessage)

                if reponse.content in listeCavaAuthor:
                    listeRetourBot = await relance("reponse-ca-va")
                    reponsec = random.choice(listeRetourBot)
                    await message.channel.send(reponsec)
                if reponse.content == listeExclusAuthor:
                    await message.channel.send(reponsed)
            except:
                await message.channel.send("trop cool le vent")

    def role(id):
        roles = guild.roles
        for role in roles:
            if role.id == id:
                return role

    guild = message.guild
    member = guild.get_member(message.author.id)
    channel = bot.get_channel(827908753998479422)
    if message.channel == channel:
        await member.add_roles(role(827223809156710420))
        await member.remove_roles(role(827907525248679956))
        await member.remove_roles(role(827898259124256768))

    chann = bot.get_channel(827953032225751110)
    guilda = bot.get_guild(827685549027885117)
    name = str(message.author)
    name = name.split('#')
    name = "".join(name)
    i = 0
    for chan in guilda.channels:
        discrim = f"{chan.name[len(chan.name) - 4]}{chan.name[len(chan.name) - 3]}{chan.name[len(chan.name) - 2]}{chan.name[len(chan.name) - 1]}"
        if discrim == message.author.discriminator:
            await chan.send(1)

    await bot.process_commands(message)


@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(827685549027885117)
    for channel in guild.channels:
        discri = f"{channel.name[len(channel.name)-4]}{channel.name[len(channel.name)-3]}{channel.name[len(channel.name)-2]}{channel.name[len(channel.name)-1]}"
        if discri == member.discriminator:
            await channel.delete()

def clem(ctx):
    return ctx.message.author.id == 720254559888605234



@bot.command()
@commands.check(clem)
async def clear(ctx, id=0):
    channel = ctx.channel
    if id != 0:
        channel = bot.get_channel(id)
    message = await channel.history(limit=100).flatten()
    await channel.delete_messages(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
    """if isinstance(error.original, discord.Forbidden):
        await ctx.send("je n'ai pas les permissions nécéssaires pour faire cette commmande")
"""

@tasks.loop(hours=24)
async def message_count():
    guild = bot.get_guild(827685549027885117)
    for channel in guild.channels:
        messages = await channel.history(limit=None).flatten()
        i = 0
        for message in messages:
            try:
                messagea = int(message.content)
                await message.delete()
                i += 1
            except:
                i += 0
        await channel.send(f"{i} messages")

def verif_channel(ctx):
    return ctx.message.channel.id == 827241970899484702 or ctx.message.channel.id == 827223619838541825

@bot.command()
@commands.check(verif_channel)
async def load(ctx, name = None):
    if name != None:
        channel = bot.get_channel(828181005508411413)
        bot.load_extension(name)
        await ctx.send("fichier load")
        await channel.send(name)
    else:
        channel = bot.get_channel(828181073665458207)
        messages = await channel.history(limit = None).flatten()
        title = []
        description = []
        for message in messages:
            lmessage = (message.content).split('/')
            title.append(lmessage[0])
            description.append(lmessage[1])
            embed = discord.Embed(title = "cog a telecharger", color = 0xebe808)
        for i in range(len(title)):
            embed.add_field(name = title[i], value = description[i], inline = True)
        await ctx.send(embed = embed)

def me(ctx):
    return ctx.message.author.id == 720254559888605234 and (ctx.message.channel.id == 827241970899484702 or ctx.message.channel.id == 827223619838541825)

@bot.command()
@commands.check(me)
async def unload(ctx, name = None):
    if name != None:

        bot.unload_extension(name)
        await ctx.send("fichier unload")
        channel = bot.get_channel(828181005508411413)
        messages = await channel.history(limit = None).flatten()
        for message in messages:
            if message.content == name:
                await message.delete()




@bot.command()
@commands.check(me)
async def reload(ctx, name = None):
    if name != None:
        try:
            bot.reload_extension(name)
            await ctx.send("fichier reload")
        except:
            bot.load_extension(name)




bot.add_cog(info.information(bot))
bot.run(process.env.TOKEN)

