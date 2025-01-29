import discord
from discord.ext import commands

from TOKEN import *
from date import logsDate, errorDate
from voiceChannel import VoiceChannel
from textChannel import TextChannel
from moderation import Moderation
from help import HelpCommand
from easterEggs import EasterEggs


class Sukuna(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix = "!", intents = discord.Intents.all())

        self.remove_command("help")

    async def setup_hook(self) -> None:
        try:
            await self.add_cog(VoiceChannel(self))
            await self.add_cog(TextChannel(self))
            await self.add_cog(Moderation(self))
            await self.add_cog(HelpCommand(self))
            await self.add_cog(EasterEggs(self))

            synced = await self.tree.sync()
            print(f"{logsDate()} Les commandes ont été chargées avec succès ! Number : [{len(synced)}]")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite lors du chargement des commandes ! Erreur : {error}")

    async def on_ready(self) -> None:
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print(f"{logsDate()} {self.user.name} est en ligne ! ID : [{self.user.id}]")


if __name__ == "__main__":
    try:
        bot = Sukuna()
        bot.run(TOKEN)
    except discord.LoginFailure as error:
        print(f"{errorDate} Le TOKEN fourni est invalide ! Erreur : {error}")
    except Exception as error:
        print(f"{errorDate} Une erreur inattendue s'est produite ! Erreur : {error}")
    