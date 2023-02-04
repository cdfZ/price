from datetime import datetime
import discord
from discord.ext import commands
from price import prefix



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
        
    @commands.group(aliases=['yardim', 'yardım'], invoke_without_command=True)
    async def help(self, ctx):
            embed=discord.Embed(title="Yardım Menüsüne Hoş geldin! Aşağıdan Komutlarıma erişebilirsin...", timestamp=datetime.utcnow(), color=0x202225)
            embed.set_author(name="Price")
            embed.add_field(name="Price Komutları", value=f"{prefix}help price", inline=True)
            await ctx.send(embed=embed)
            
    @help.command()
    async def price(self, ctx):
            embed=discord.Embed(title="Price Komutları", description="Price Kategorisindeki Komutlar", timestamp=datetime.utcnow(), color=0x202225)
            embed.add_field(name=f"{prefix}ekle [item] [price]", value="İtem Ekleminizi Sağlar.", inline=False)
            embed.add_field(name=f"{prefix}update [item] [price]", value="İtemin Fiyatını Günceller.", inline=False)
            embed.add_field(name=f"{prefix}tablo", value="Tablo Yoksa Oluşturur.", inline=False)
            embed.add_field(name=f"{prefix}itemler", value="Tüm İtemleri Listeler.", inline=False)
            embed.add_field(name=f"{prefix}price [item]", value="İtemin Güncel Fiyatına Bakmanızı Sağlar", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
