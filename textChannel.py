import discord
from discord.ext import commands

from date import logsDate, errorDate


class TextChannel(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name = "clear", description = "Supprime des messages dans le salon textuel, 5 par défaut")
    async def clear(self, ctx : commands.Context, amount : int = 5) -> discord.Message:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")

            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour supprimer des messages !", ephemeral = True)

            max_limit = amount > 50
            min_limit = amount < 2
            if max_limit:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas supprimer plus de 50 messages !", ephemeral = True)
            elif min_limit:
                return await ctx.reply(f"{user_mention} -> Tu dois supprimer au moins deux messages !", ephemeral = True)

            is_text_chanel = isinstance(ctx.channel, discord.TextChannel)
            if not is_text_chanel:
                return await ctx.reply(f"{user_mention} -> Tu dois appeler cette commande depuis un salon textuel !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await ctx.channel.purge(limit = amount)
                print(f"{logsDate()} {ctx.author.name} a supprimé {amount} messages ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} -> {amount} messages ont bien été supprimés !", ephemeral = True)

            await ctx.channel.purge(limit = amount)
            print(f"{logsDate()} {ctx.author.name} a supprimé {amount} messages ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} -> {amount} messages ont bien été supprimés !", ephemeral = True)
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour supprimer des messages ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "slowmode", description = "Détermine un temps d'envoie entre chaques messages")
    async def slowmode(self, ctx : commands.Context, seconds : int, channel : discord.TextChannel = None) -> discord.Message:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour activer le slowmode !", ephemeral = True)
            
            is_time_invalid = seconds < 0 or seconds > 21600
            if is_time_invalid:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas mettre un slowmode inférieur à 0 secondes ou supérieur à 6 heures !", ephemeral = True)
            
            if channel is None:
                channel = ctx.channel

            await channel.edit(slowmode_delay = seconds)

            if seconds == 0:
                print(f"{logsDate()} {ctx.author.name} a désactivé le slowmode sur {channel.name} ! Temps : [{seconds}s] Channel : [{channel}] Type : [SLASHCOMMAND]")
                return await ctx.reply(f"{user_mention} -> Le slowmode a bien été désactivé !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                print(f"{logsDate()} {ctx.author.name} a activé le slowmode sur {channel.name} ! Temps : [{seconds}s] Channel : [{channel}] Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} -> Le slowmode a été activé pendant {seconds} secondes !", ephemeral = True)
            
            print(f"{logsDate()} {ctx.author.name} a activé le slowmode sur {channel.name} ! Temps : [{seconds}s] Channel : [{channel}] Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} -> Le slowmode a été activé pendant {seconds} secondes !", ephemeral = True)
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour activer le slowmode ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
