#======================#

import sys
import discord
import os
from discord.ext import commands
from colorama import Fore
from time import *
from datetime import time
from dotenv import load_dotenv
import sqlite3

#======================#

load_dotenv()
token = os.getenv("TOKEN")

#======================#

def slowprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sleep(1./500000000)
     
#======================#

prefix = '.'
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=discord.Intents.default())
strftime = time
bot.remove_command('help')

#======================#

@bot.event
async def on_ready():
    activity = discord.Game(name="PRICE", type=4)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    slowprint(f'{Fore.LIGHTRED_EX}╔══════════════════════════════════════════════════════════════════════════════════════════════════╗{Fore.RESET}')
    slowprint(f'{Fore.LIGHTRED_EX}║    PRICE BOTU HAZIR KOMUTLARI OGRENMEK ICIN {prefix}help | AKTIF BOT: {bot.user.name} | Yapımcı: AhmeTLK#0793     ║{Fore.RESET}')
    slowprint(f'{Fore.LIGHTRED_EX}╚══════════════════════════════════════════════════════════════════════════════════════════════════╝{Fore.RESET}')
    db = sqlite3.connect('item.db')
    db.commit()
#======================#

@bot.command()
async def load(ctx, extension):
  try:
    bot.load_extension(f"lib.cogs.{extension}")
    slowprint(f"{Fore.LIGHTGREEN_EX}[+] {extension} Kategorisindeki Komutlar Yüklendi!")
  except commands.ExtensionAlreadyLoaded:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Zaten Yüklü!")
  except commands.ExtensionNotFound:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Bulunamadı!")
  except commands.ExtensionFailed:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Katogorisi Yüklenemedi!")
  except commands.CommandInvokeError:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!") 
  except Exception:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!")

@bot.command()
async def unload(ctx, extension):
  try:
    bot.unload_extension(f"lib.cogs.{extension}")
    slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisindeki Komutlar Devre Dışı!")
  except commands.ExtensionNotLoaded:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Bulunumadı!")
  except commands.ExtensionNotFound:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Bulunamadı!")
  except commands.ExtensionFailed:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Katogorisi Yüklenemedi!")
  except commands.CommandInvokeError:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!")     
  except Exception:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!")   
  

@bot.command()
async def reload(ctx, extension):   
  try:
    bot.reload_extension(f"lib.cogs.{extension}")
    slowprint(f"{Fore.LIGHTGREEN_EX}[+] {extension} Kategorisindeki Komutlar Yeniden Yüklendi!")
  except commands.ExtensionNotLoaded:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Bulunumadı!")
  except commands.ExtensionNotFound:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Kategorisi Bulunamadı!")
  except commands.ExtensionFailed:
     slowprint(f"{Fore.LIGHTRED_EX}[-] {extension} Katogorisi Yüklenemedi!")
  except commands.CommandInvokeError:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!")     
  except Exception:
     slowprint(f"{Fore.LIGHTRED_EX}[-] Beklenmeyen bir hata oluştu!")   

#======================#

for fn in os.listdir('./lib/cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'lib.cogs.{fn[:-3]}')
        
#======================#

bot.run(token)