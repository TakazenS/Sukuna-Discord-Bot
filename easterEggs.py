import discord
from discord.ext import commands

from date import errorDate


class EasterEggs(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name = "sout", description = "Affiche un message en Java")
    async def sout(self, ctx : commands.Context) -> discord.Message:
        try:
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                return await ctx.reply('System.out.println("Hello world !")')

            return await ctx.reply('System.out.println("Hello world !")')
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour envoyer un message ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    