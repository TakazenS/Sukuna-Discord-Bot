import discord
from discord.ext import commands

from date import logsDate, errorDate


class Moderation(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name = "ban", description = "Bannit un membre du serveur")
    async def ban(self, ctx : commands.Context, member : discord.Member, *, reason : str = "") -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.ban_members
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour bannir un membre !", ephemeral = True)
            
            is_bannable = ctx.author.top_role >= member.top_role
            if not is_bannable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas bannir ce membre !", ephemeral = True)
            
            if reason == "" or reason == " ":
                reason = "Pas de raison notée !"

            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.ban(reason = reason)
                print(f"{logsDate()} {ctx.author.name} a banni {member.name} ! Raison : [{reason}] Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a banni {member.name} !\nRaison : {reason}", ephemeral = True)

            await member.ban(reason = reason)
            print(f"{logsDate()} {ctx.author.name} a banni {member.name} ! Raison : [{reason}] Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a banni {member.name} !\nRaison : {reason}", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour bannir un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "kick", description = "Expulse un membre du serveur")
    async def kick(self, ctx : commands.Context, member : discord.Member, *, reason : str = "") -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.kick_members
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour kick un membre !", ephemeral = True)
            
            is_kickable = ctx.author.top_role >= member.top_role
            if not is_kickable:
                return await ctx.reply(f"{user_mention} -> Tu ne peux pas kick ce membre !", ephemeral = True)
            
            if reason == "" or reason == " ":
                reason = "Pas de raison notée !"

            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.kick(reason = reason)
                print(f"{logsDate()} {ctx.author.name} a kick {member.name} ! Raison : [{reason}] Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a kick {member.name} !\nRaison : {reason}", ephemeral = True)

            await member.kick(reason = reason)
            print(f"{logsDate()} {ctx.author.name} a kick {member.name} ! Raison : [{reason}] Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a kick {member.name} !\nRaison : {reason}", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour kick un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")
    
    
    @commands.hybrid_command(name = "unban", description = "Débannit un membre du serveur")
    async def unban(self, ctx : commands.Context, member : str) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")

            has_permission = ctx.author.guild_permissions.ban_members
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour unban un membre !", ephemeral = True)

            banned_users = [ban_entry async for ban_entry in ctx.guild.bans()]
            member_name = member
            for ban_entry in banned_users:
                user = ban_entry.user

            is_prefix = ctx.message.content.startswith("!")
            if is_prefix and user.name == member_name:
                await ctx.guild.unban(user)
                print(f"{logsDate()} {ctx.author.name} a débanni {member_name} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a débanni {member_name} !", ephemeral = True)

            if user.name == member_name:
                await ctx.guild.unban(user)
                print(f"{logsDate()} {ctx.author.name} a débanni {member_name} ! Type : [SLASHCOMMAND]")
                return await ctx.reply(f"{user_mention} a débanni {member_name} !", ephemeral = True)

            return await ctx.reply(f"{user_mention} -> Utilisateur introuvable !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour débannir un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite ! Erreur : {error}")

            
    @commands.hybrid_command(name = "add", description = "Ajoute un rôle à un membre ")
    async def addrole(self, ctx : commands.Context, role : discord.Role, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.administrator
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions gérer les rôles !", ephemeral = True)

            is_allowed_to_manage = ctx.author.top_role >= member.top_role
            if not is_allowed_to_manage:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour gérer les rôles de cet utilisateur !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.add_roles(role)
                print(f"{logsDate()} {ctx.author.name} a ajouté le rôle {role.name} à {member.name} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a ajouté le rôle {role.name} à {member.name} !", ephemeral = True)
            
            await member.add_roles(role)
            print(f"{logsDate()} {ctx.author.name} a ajouté le rôle {role.name} à {member.name} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a ajouté le rôle {role.name} à {member.name} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour ajouter un rôle à un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite !")
        

    @commands.hybrid_command(name = "remove", description = "Retire un rôle à un membre")
    async def removerole(self, ctx : commands.Context, role : discord.Role, member : discord.Member) -> None:
        try:
            await ctx.defer(ephemeral = True)

            is_private = ctx.guild is None and isinstance(ctx.author, discord.User)
            if is_private:
                return await ctx.send("Tu ne peux pas utiliser cette commande en mp !")
            
            has_permission = ctx.author.guild_permissions.administrator
            user_mention = ctx.author.mention
            if not has_permission:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions gérer les rôles !", ephemeral = True)

            is_allowed_to_manage = ctx.author.top_role >= member.top_role
            if not is_allowed_to_manage:
                return await ctx.reply(f"{user_mention} -> Tu n'as pas les permissions pour gérer les rôles de cet utilisateur !", ephemeral = True)
            
            is_prefix = ctx.message.content.startswith("!")
            if is_prefix:
                await member.remove_roles(role)
                print(f"{logsDate()} {ctx.author.name} a retiré le rôle {role.name} à {member.name} ! Type : [PREFIX]")
                return await ctx.reply(f"{user_mention} a retiré le rôle {role.name} à {member.name} !", ephemeral = True)
            
            await member.remove_roles(role)
            print(f"{logsDate()} {ctx.author.name} a retiré le rôle {role.name} à {member.name} ! Type : [SLASHCOMMAND]")
            return await ctx.reply(f"{user_mention} a retiré le rôle {role.name} à {member.name} !", ephemeral = True)
        except discord.Forbidden as error:
            print(f"{errorDate()} Le bot n'a pas les permission pour retirer un rôle à un membre ! Erreur : {error}")
        except discord.HTTPException as error:
            print(f"{errorDate()} Une erreur HTTP s'est produite ! Erreur : {error}")
        except Exception as error:
            print(f"{errorDate()} Une erreur inattendue s'est produite !")
