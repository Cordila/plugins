import re

from discord.ext import commands

InviteFiler = re.compile("(?:https?://)?discord(?:app)?\.(?:com/invite|gg)/[a-zA-Z0-9]+/?")


class NoInvites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        role = message.guild.get_role(971456486221959219)
        if message.author.bot:
            return
        if role in message.author.roles:
            return
        if InviteFiler.search(message.content):
            await message.delete()
            await message.channel.send("Invites are not allowed in this server.")


def setup(bot):
    bot.add_cog(NoInvites(bot))
