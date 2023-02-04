import discord
from discord.ext import commands
from datetime import datetime

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
     channel = discord.utils.get(member.guild.channels, id=1036391292185358397)
     role = discord.utils.get(member.guild.roles, id=1036391766494040134)
     await member.add_roles(role)
     if channel is not None:
         embed = discord.Embed(description="Yeni katılan {0.mention} kullanıcısına {1.mention} rolü verildi!".format(member, role), timestamp=datetime.utcnow(), color=0x202225)
         await channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
     channel = discord.utils.get(member.guild.channels, id=1036391292185358397)
     if channel is not None:
         embed = discord.Embed(description=f"{member} adlı kullanıcı aramızdan ayrıldı! Toplam üye sayımız: {member.guild.member_count}".format(member), timestamp=datetime.utcnow(), color=0x202225)
         await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(Join(bot))