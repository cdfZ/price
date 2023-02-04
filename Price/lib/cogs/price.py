from discord.ext import commands
import discord
import sqlite3
from datetime import datetime
import sqlite3

class Price(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tablo(self, ctx):
      db = sqlite3.connect('item.db')
      db.cursor()
      db.execute("CREATE TABLE IF NOT EXISTS price (item TEXT PRIMARY KEY, price TEXT, author ID, link TEXT)")
      db.commit()

    @tablo.error
    async def tablo_error(self, ctx, error): 
        if isinstance(error, commands.MissingPermissions):    
            embed=discord.Embed(description="Bu Komutu Kullanmak İçin Yetkin Yetmiyor!", timestamp=datetime.utcnow(), color=0x202225)
            await ctx.send(embed=embed)  
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ekle(self, ctx, item = None, price = None, link = None):
     db = sqlite3.connect('item.db')
     db.cursor()
     db.execute('INSERT INTO price (item, price, author, link) VALUES (?, ?, ?, ?)', (item, price, ctx.author.id, link,))
     embed=discord.Embed(title=f"`{item}` Adlı İtem Eklendi!", timestamp=datetime.utcnow(), color=0x202225)
     embed.set_thumbnail(url=f"{link}")
     embed.add_field(name="İtem:", value=f"{item}", inline=False)
     embed.add_field(name="Price:", value=f"{price}", inline=False)
     embed.add_field(name="Ekleyen Yetkili:", value=f"{ctx.author}", inline=False)
     await ctx.send(embed=embed)
     db.commit()
      
    @ekle.error
    async def ekle_error(self, ctx, error): 
        if isinstance(error, commands.CommandInvokeError):
            embed=discord.Embed(description="Bu İtem Zaten Sistemde Kayıtlı!", timestamp=datetime.utcnow(), color=0x202225)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):    
            embed=discord.Embed(description="Bu Komutu Kullanmak İçin Yetkin Yetmiyor!", timestamp=datetime.utcnow(), color=0x202225)
            await ctx.send(embed=embed)            
      
    @commands.command()
    async def price(self, ctx, *, item):
       db = sqlite3.connect('item.db')
       allah = db.cursor()
       for row in db.execute(f'SELECT item, price, author, link FROM price WHERE item = ?', (item,)):
        allah.fetchone()
        embed=discord.Embed(title=f"`{row[0]}` Adlı İtemin Güncel Fiyatı", timestamp=datetime.utcnow(), color=0x202225)
        embed.set_thumbnail(url=f"{row[3]}")
        embed.add_field(name="İtem:", value=f"{row[0]}", inline=False)
        embed.add_field(name="Price:", value=f"{row[1]}", inline=False)
        embed.add_field(name="Ekleyen Yetkili:", value=f"{row[2]}", inline=False)
        await ctx.send(embed=embed)
       db.commit()

    @commands.command()
    async def itemler(self, ctx):
       db = sqlite3.connect('item.db')
       allah = db.cursor()
       allah.execute('SELECT item FROM price')
       embed=discord.Embed(title=f"Kayıtlı İtemler:", description=f"{allah.fetchall()}", timestamp=datetime.utcnow(), color=0x202225)
       await ctx.send(embed=embed)
       db.commit()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def update(self, ctx, item = None, price = None):
       db = sqlite3.connect('item.db')
       allah = db.cursor()
       allah.fetchone()
       for row in db.execute(f'SELECT item, price, author, link FROM price WHERE item = ?', (item,)):
        allah.fetchone()
        db.execute(f'UPDATE price SET price = ? , author = ? WHERE item = ?', (price, ctx.author.id, item,))
        embed=discord.Embed(title=f"`{row[0]}` Adlı İtemin Fiyatı Güncellendi", timestamp=datetime.utcnow(), color=0x202225)
        embed.set_thumbnail(url=f"{row[3]}")
        embed.add_field(name="İtem:", value=f"{row[0]}", inline=False)
        embed.add_field(name="Eski Price:", value=f"{row[1]}", inline=False)
        embed.add_field(name="Yeni Price:", value=f"{price}", inline=False)
        embed.add_field(name="Ekleyen Yetkili:", value=f"{row[2]}", inline=False)        
        embed.add_field(name="Güncelleyen Yetkili:", value=f"{ctx.author.id}", inline=False)
        await ctx.send(embed=embed)
       db.commit()

    @update.error
    async def update_error(self, ctx, error): 
        if isinstance(error, commands.MissingPermissions):    
            embed=discord.Embed(description="Bu Komutu Kullanmak İçin Yetkin Yetmiyor!", timestamp=datetime.utcnow(), color=0x202225)
            await ctx.send(embed=embed)  
    
def setup(bot):
    bot.add_cog(Price(bot))