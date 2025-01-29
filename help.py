import discord
from discord.ext import commands

from date import logsDate, errorDate


class HelpCommand(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name = "help", description = "Affiche la liste des commandes disponibles.")
    async def help(self, ctx : commands.Context,* , type : str = "") -> discord.Embed:
        try:
            await ctx.defer(ephemeral = True)

            commandType = ["", "vocal", "textuel", "moderation", "easteregg"]

            if type not in commandType:
                helpAmbed = discord.Embed(
                    title = f"Erreur :",
                    description = f"Le type de commande {type} n'existe pas !"
                )

                helpAmbed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
                helpAmbed.set_thumbnail(url = self.bot.user.display_avatar.url)

                print(f"{errorDate()} {ctx.author.name} a demandé de l'aide ! Erreur : [TYPE INCONNU]")
                return await ctx.reply(embed = helpAmbed)
            
                
            if type == commandType[0]:
                helpAmbed = discord.Embed(
                    title = f"Liste des commandes pour {self.bot.user.name}:",
                    description = """Voici la liste des commandes d'aide disponibles sur le bot Sukuna ->

                                    *Vocal* : /help **vocal**
                                    *Textuel* : /help **textuel**
                                    *Moderation* : /help **moderation**
                                    *Easteregg* : /help **easteregg**

                                    Pour plus d'informations sur les types de commandes, utilisez la commande suivante : **/help** *<commande>*"""
                )

                helpAmbed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
                helpAmbed.set_thumbnail(url = self.bot.user.display_avatar.url)

                print(f"{logsDate()} {ctx.author.name} a demandé de l'aide ! Type : [N/A]")
                return await ctx.reply(embed = helpAmbed)
            

            if type == commandType[1]:
                helpAmbed = discord.Embed(
                    title = f"Liste des commandes vocales pour {self.bot.user.name}:",
                    description = """Voici la liste des commandes vocales disponibles sur le bot Sukuna ->

                                    *mute* : **/mute** *<membre>*
                                    Mute un membre dans un salon vocal

                                    *unmute* : **/unmute** *<membre>*
                                    Unmute un membre dans un salon vocal

                                    *tempmute* : **/tempmute** *<membre>* *<time>*
                                    Tempmute un membre dans un salon vocal

                                    *silence* : **/silence** *<membre>*
                                    Silence un membre dans un salon vocal

                                    *unsilence* : **/unsilence** *<membre>*
                                    Unsilence un membre dans un salon vocal

                                    *globalmute* : **/globalmute** *<membre>*
                                    Mute et silence un membre d'un coup

                                    *globalunmute* : **/globalunmute** *<membre>*
                                    Unmute et unsilence un membre d'un coup

                                    *move* : **/move** *<membre>* *<channel>*
                                    Move un membre dans un salon vocal"""
                    )
                
                helpAmbed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
                helpAmbed.set_thumbnail(url = self.bot.user.display_avatar.url)

                print(f"{logsDate()} {ctx.author.name} a demandé de l'aide ! Type : [VOCAL]")
                return await ctx.reply(embed = helpAmbed)
            
            
            if type == commandType[2]:
                helpAmbed = discord.Embed(
                    title = f"Liste des commandes textuelles pour {self.bot.user.name}:",
                    description = """Voici la liste des commandes textuelles disponibles sur le bot Sukuna ->

                                    *clear* : **/clear** *<amount>*
                                    Supprime des messages dans un salon textuel, 5 par défaut

                                    *slowmode* : **/slowmode** *<seconds>*
                                    Détermine un temps d'envoie entre chaques messages"""
                    )

                print(f"{logsDate()} {ctx.author.name} a demandé de l'aide ! Type : [TEXTUEL]")
                return await ctx.reply(embed = helpAmbed)
            
            
            if type == commandType[3]:
                helpAmbed = discord.Embed(
                    title = f"Liste des commandes de modération pour {self.bot.user.name}:",
                    description = """Voici la liste des commandes de modération disponibles sur le bot Sukuna ->

                                    *kick* : **/kick** *<membre>*
                                    Kick un membre du serveur

                                    *ban* : **/ban** *<membre>*
                                    Ban un membre du serveur

                                    *unban* : **/unban** *<membre>*
                                    Débannit un membre du serveur
                                    
                                    *addrole* : **/addrole** *<membre>* *<role>*
                                    Ajoute un rôle à un membre
                                    
                                    *removerole* : **/removerole** *<membre>* *<role>*
                                    Retire un rôle à un membre"""
                    )
                
                helpAmbed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
                helpAmbed.set_thumbnail(url = self.bot.user.display_avatar.url)

                print(f"{logsDate()} {ctx.author.name} a demandé de l'aide ! Type : [MODERATION]")
                return await ctx.reply(embed = helpAmbed)
            

            if type == commandType[4]:
                helpAmbed = discord.Embed(
                    title = f"Liste des commandes cachées pour {self.bot.user.name}:",
                    description = """Voici la liste des commandes cachées disponibles sur le bot Sukuna ->

                                    *sout* : **/sout**
                                    Affiche un message en Java"""
                    )
                
                helpAmbed.set_author(name = ctx.author.name, icon_url = ctx.author.display_avatar.url)
                helpAmbed.set_thumbnail(url = self.bot.user.display_avatar.url)

                print(f"{logsDate()} {ctx.author.name} a demandé de l'aide ! Type : [EASTEREGG]")
                return await ctx.reply(embed = helpAmbed)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour envoyer un message ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")

