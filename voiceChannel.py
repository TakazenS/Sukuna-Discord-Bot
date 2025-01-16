import discord
from discord.ext import commands

from date import logsDate, errorDate


class VoiceChannel(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name = "mute", description = "Mute un membre dans un salon vocal")
    async def mute(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour mute un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_mutable = ctx.author.top_role > member.top_role
            if is_mutable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas mute ce membre !", ephemeral = True)
            
            is_muted = member.voice.mute
            if is_muted:
                return await ctx.reply(f"{user_mention} -> {member} est déja mute !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(mute = True)
                print(f"{logsDate()} {ctx.author.name} a mute {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a mute {member} !", ephemeral = True)
            
            await member.edit(mute = True)
            print(f"{logsDate()} {ctx.author.name} a mute {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a mute {member} !")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour mute un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "unmute", description = "Unmute un membre dans un salon vocal")
    async def unmute(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour mute un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_unmutable = ctx.author.top_role > member.top_role
            if is_unmutable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas mute ce membre !", ephemeral = True)
            
            is_unmuted = member.voice.mute
            if not is_unmuted:
                return await ctx.reply(f"{user_mention} -> {member} est déja unmute !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(mute = False)
                print(f"{logsDate()} {ctx.author.name} a unmute {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a unmute {member} !", ephemeral = True)
            
            await member.edit(mute = False)
            print(f"{logsDate()} {ctx.author.name} a unmute {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a unmute {member} !")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour unmute un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
    

    @commands.hybrid_command(name = "silence", description = "Silence un membre dans un salon vocal")
    async def silence(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour silence un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !")
            
            is_silenceable = ctx.author.top_role > member.top_role
            if not is_silenceable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas silence ce membre !", ephemeral = True)
            
            is_silence = member.voice.deaf
            if is_silence:
                return await ctx.reply(f"{user_mention} -> {member} est déja silence !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(deafen = True)
                print(f"{logsDate()} {ctx.author.name} a silence {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a silence {member} !", ephemeral = True)
            
            await member.edit(deafen = True)
            print(f"{logsDate()} {ctx.author.name} a silence {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a silence {member} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour silence un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "unsilence", description = "Unsilence un membre dans un salon vocal")
    async def unsilence(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour unsilence un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_unsilenceable = ctx.author.top_role > member.top_role
            if not is_unsilenceable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas unsilence ce membre !", ephemeral = True)
            
            is_unsilence = member.voice.deaf
            if not is_unsilence:
                return await ctx.reply(f"{user_mention} -> {member} est déja unsilence !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(deafen = False)
                print(f"{logsDate()} {ctx.author.name} a unsilence {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a unsilence {member} !", ephemeral = True)
            
            await member.edit(deafen = False)
            print(f"{logsDate()} {ctx.author.name} a unsilence {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a unsilence {member} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour unsilence un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "globalmute", description = "Global mute un membre dans un salon vocal")
    async def globalmute(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour global mute un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_mutable = ctx.author.top_role > member.top_role
            if not is_mutable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas global mute ce membre !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(mute = True, deafen = True)
                print(f"{logsDate()} {ctx.author.name} a global mute {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a global mute {member} !", ephemeral = True)
            
            await member.edit(mute = True, deafen = True)
            print(f"{logsDate()} {ctx.author.name} a global mute {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a global mute {member} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour global mute un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "globalunmute", description = "Global unmute un membre dans un salon vocal")
    async def globalunmute(self, ctx : commands.Context, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour global unmute un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_mutable = ctx.author.top_role > member.top_role
            if not is_mutable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas global unmute ce membre !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.edit(mute = False, deafen = False)
                print(f"{logsDate()} {ctx.author.name} a global unmute {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a global unmute {member} !", ephemeral = True)
            
            await member.edit(mute = False, deafen = False)
            print(f"{logsDate()} {ctx.author.name} a global unmute {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a global unmute {member} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour global unmute un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "move", description = "Move un membre dans un salon vocal")
    async def move(self, ctx : commands.Context, member : discord.Member,* , channel : str) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour move un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_moveable = ctx.author.top_role > member.top_role
            if not is_moveable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas move ce membre !", ephemeral = True)
            
            target_chanel = discord.utils.get(ctx.guild.voice_channels, name = channel)
            if not target_chanel:
                return await ctx.reply("Ce salon vocal n'existe pas !", ephemeral = True)
            
            previous_channel = member.voice.channel
            if previous_channel == target_chanel:
                return await ctx.reply(f"{user_mention} ce membre est déjà dans ce salon vocal !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.move_to(target_chanel)
                print(f"{logsDate()} {ctx.author.name} a move {member} du channel {previous_channel} au channel {channel} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a move {member} vers {target_chanel} !", ephemeral = True)

            await member.move_to(target_chanel)
            print(f"{logsDate()} {ctx.author.name} a move {member} du channel {previous_channel} au channel {channel} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a move {member} vers {target_chanel} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour move un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")


    @commands.hybrid_command(name = "tempmute", description = "Mute un membre de façon temporaire")
    async def tempmute(self, ctx : commands.Context, member : discord.Member, duration : int) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.manage_channels
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour tempmute un membre !", ephemeral = True)
            
            is_connected = member.voice is not None and member.voice.channel is not None
            if not is_connected:
                return await ctx.reply(f"{member} n'est pas dans un salon vocal !", ephemeral = True)
            
            is_mutable = ctx.author.top_role > member.top_role
            if is_mutable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas tempmute ce membre !", ephemeral = True)
            
            check_duration = duration < 0 or duration > 21600
            if check_duration:
                return await ctx.reply(f"{user_mention} -> La durée du mute doit être comprise entre 1 et 21600 secondes !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                if duration == 0:
                    await member.edit(mute = False, timed_out_until = None)
                    print(f"{logsDate()} {ctx.author.name} a désactivé le tempmute sur {member} ! Type : [PREFIX]")
                    return await ctx.reply(f"{user_mention} à désactivé le tempmute sur {member.name} !", ephemeral = True)

                await member.edit(mute = True, timed_out_until = duration)
                print(f"{logsDate()} {ctx.author.name} a tempmute {member} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a tempmute {member} !", ephemeral = True)
            
            if duration == 0:
                await member.edit(mute = False, timed_out_until = None)
                print(f"{logsDate()} {ctx.author.name} a désactivé le tempmute sur {member} ! Type : [SLASHCOMMAND]")
                return await ctx.reply(f"{user_mention} à désactivé le tempmute sur {member.name} !", ephemeral = True)
            
            await member.edit(mute = True, timed_out_until = duration)
            print(f"{logsDate()} {ctx.author.name} a tempmute {member} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a tempmute {member} !")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour mute un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
