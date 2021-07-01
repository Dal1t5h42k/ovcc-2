# Importing the required modules
import csv
from datetime import date
import calendar
#import gspread
#import dog
import os
import re
import sys
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup
import imghdr
import discord
import requests
import pandas
from discord.ext import commands
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import discord
#from email.message import EmailMessage
#import ssl
#import smtplib
from bs4 import BeautifulSoup
from datetime import datetime
import requests
#import ssl
import os
#import bot
#import pygsheets
import json
import csv
import asyncio
#from google.oauth2 import service_account
import smtp
import urllib 
import random
#import smtplib
import asyncio
#from discord.utils import get
import asyncio
#from pythonping import ping
#import smtplib
from socket import gaierror
from tabulate import tabulate
import requests
import lxml.html as lh
import tasks
import pandas as pd
import os
from tabulate import tabulate
nitros = []
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
lister = ""
api_key = "114196e25be211b63915f78266020556"
count = 0
base_url = "http://api.openweathermap.org/data/2.5/weather?"
usacolinks = ["http://www.usaco.org/index.php?page=viewproblem2&cpid=942", "http://www.usaco.org/index.php?page=viewproblem2&cpid=943", "http://www.usaco.org/index.php?page=viewproblem2&cpid=944", "http://www.usaco.org/index.php?page=viewproblem2&cpid=939", "http://www.usaco.org/index.php?page=viewproblem2&cpid=940", "http://www.usaco.org/index.php?page=viewproblem2&cpid=941", "http://www.usaco.org/index.php?page=viewproblem2&cpid=918", "http://www.usaco.org/index.php?page=viewproblem2&cpid=919", "http://www.usaco.org/index.php?page=viewproblem2&cpid=920", "http://www.usaco.org/index.php?page=viewproblem2&cpid=915", "http://www.usaco.org/index.php?page=viewproblem2&cpid=916", "http://www.usaco.org/index.php?page=viewproblem2&cpid=917", "http://www.usaco.org/index.php?page=viewproblem2&cpid=894", "http://www.usaco.org/index.php?page=viewproblem2&cpid=895", "http://www.usaco.org/index.php?page=viewproblem2&cpid=896", "http://www.usaco.org/index.php?page=viewproblem2&cpid=891", "http://www.usaco.org/index.php?page=viewproblem2&cpid=892", "http://www.usaco.org/index.php?page=viewproblem2&cpid=893", "http://www.usaco.org/index.php?page=viewproblem2&cpid=858", "http://www.usaco.org/index.php?page=viewproblem2&cpid=859", "http://www.usaco.org/index.php?page=viewproblem2&cpid=860", "http://www.usaco.org/index.php?page=viewproblem2&cpid=855", "http://www.usaco.org/index.php?page=viewproblem2&cpid=856", "http://www.usaco.org/index.php?page=viewproblem2&cpid=857", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1038", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1039", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1040", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1035", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1036", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1037", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1014", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1015", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1016", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1011", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1012", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1013", "http://www.usaco.org/index.php?page=viewproblem2&cpid=990", "http://www.usaco.org/index.php?page=viewproblem2&cpid=991", "http://www.usaco.org/index.php?page=viewproblem2&cpid=992", "http://www.usaco.org/index.php?page=viewproblem2&cpid=987", "http://www.usaco.org/index.php?page=viewproblem2&cpid=988", "http://www.usaco.org/index.php?page=viewproblem2&cpid=989", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1134", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1135", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1136", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1131", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1132", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1133", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1110", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1111", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1112", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1107", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1108", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1109", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1086", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1087", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1088", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1083","http://www.usaco.org/index.php?page=viewproblem2&cpid=1084", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1085", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1062", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1063", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1064", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1059", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1060", "http://www.usaco.org/index.php?page=viewproblem2&cpid=1061", ""]
bot = commands.Bot(command_prefix='!', intents = intents)
def write_emails(mails, *args):
    for arg in args:
        mails.remove(arg)
    for mail in mails:
        with open('emails.txt','w') as f:
            f.write(mail+"\n")


def send_email(sender, recipient,subject, body):

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    print("message: ")
    print(body+"\n")
    print("------")

    gmail_user = 'mail'
    gmail_pwd = 'pwd'
    FROM = sender
    TO = recipient
    SUBJECT = subject

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = recipient
    msg.attach(MIMEText(body,'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print("successfully sent the mail to "+recipient)
    except: print("failed to send mail to "+recipient)
politics = ["congress", "cabinet", "Trump", "trump", "Biden", "biden", "president", "Pres", "President", "VP", "Vice President", "vp", "Republican", "Democrate", "Joe"]
bot_id = "ODU0ODkwMTEyNjYzMTU4ODM5.YMqgdQ.vh4IjkmxfA2DxQgY_RCAmlY9JuU"
#intents = discord.Intents.default()
#intents.members=True
#bot = discord.bot(intents=intents)
badlist = ["fuck", "shit", "wap", "WAP", "bish", "bitch", "ass", "suck", "ur mom", "shut", "shut up"]
#bot = discord.bot()
#@bot.event
#async def on_ready():
  #print("OVCC READY!")
#ment = member.mention
#await self.bot.get_channel(779860877465092146).send(f"{ment} has joined the server.")
#print(f"{member} has joined the server.")
@bot.event
async def on_ready():
    print("OVCC Online!")
@bot.event
async def on_member_join(member):
  await member.send(str(member.mention) + ", Welcome to the OVCC Discord Server!\n Please read #rules as they are very important. \n Look at #new-people to find out what to do next.\n React with a role in #groups-and-roles. It is very important that you do this so you will get access to the discord channels.\n Look at #channels for a description on each channel.\n Thank you for joining the OVCC discord server and have fun!\n \n\n Regards,\n The Officers")
@bot.event
async def on_message(message):
  URL = "https://docs.google.com/spreadsheets/d/1pFMRZ6OuUDmT2xQgR6ug6ExrHkKxEL8Q93LkI8T3rDg/htmlembed"
  if "calender" in message.content or "date" in message.content:
    todays_date = date.today()
    c= calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(int(todays_date.year), int(todays_date.month))
    await message.channel.send("**Calender:**")
    await message.channel.send("```\n" + str + "\n```")
  if "schedule" in message.content:
    os.system("wget " + URL)
    os.rename(r'htmlembed',r'htmlembed.html')
    path = "htmlembed.html"
    """
    # empty list
    data = []
    list_header = []
    soup = BeautifulSoup(open(path),'html.parser')
    header = soup.find_all("table")[0].find("tr")
    for items in header:
      try:
        list_header.append(items.get_text())
      except:
        continue
    HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
    for element in HTML_data:
      sub_data = []
      for sub_element in element:
        try:
          sub_data.append(sub_element.get_text())
        except:
          continue
    data.append(sub_data)
    dataFrame = pd.DataFrame(data = data, columns = list_header)
    dataFrame.to_csv('schedule.csv')
    """
    embed = discord.Embed(title="Schedule:",description=f"Hey, {message.author.name}, here is the schedule: [Schedule](https://docs.google.com/spreadsheets/d/1pFMRZ6OuUDmT2xQgR6ug6ExrHkKxEL8Q93LkI8T3rDg/htmlembed)", color=discord.Color.blue())
    embed.set_thumbnail(url="https://4cc178fe-a-62cb3a1a-s-sites.googlegroups.com/site/oakvalleycodingclub/home/imageonline-co-overlayed-image%20%282%29.png?attachauth=ANoY7cqXijRN1GluZGYxT0FmjI85hsDJrXhqQGRNQJa88UjJB4g-HPmVEqs0rpnGIpCisOS1UrFjDNCy2-8wRGdx1co2spbMp5JkSGSH7sl4R-vf5kloSZi-i-cqyrr3piuteVo69vqmKdNsneAkYsANwrur_-qHN-BwJ87HNmJlM9Yg-W6WFHwT3uwn-zCTSedfN_10EOTZNeke_xXZA4OtmdJLBaoM8qYIOIRogsUna4EJiH710BM2MqcfMtp572bF344NvNlqpMEl1UL3OyHqrOC5YHNjkA%3D%3D&attredirects=0")
    await message.channel.send(embed=embed)
  for i in badlist:
    if i in message.content:
      
      await message.channel.send(f"{message.author.mention} Don't use that word!")
      #852277418831118386
      embed = discord.Embed(title="Profanity Alert! :no_entry_sign:",description=f"{message.author.name} just said ||{i}||.\n Category: **bad word**\n Level: **Warning 1**", color=discord.Color.red())
      embed.set_thumbnail(url="https://4cc178fe-a-62cb3a1a-s-sites.googlegroups.com/site/oakvalleycodingclub/home/imageonline-co-overlayed-image%20%282%29.png?attachauth=ANoY7cqXijRN1GluZGYxT0FmjI85hsDJrXhqQGRNQJa88UjJB4g-HPmVEqs0rpnGIpCisOS1UrFjDNCy2-8wRGdx1co2spbMp5JkSGSH7sl4R-vf5kloSZi-i-cqyrr3piuteVo69vqmKdNsneAkYsANwrur_-qHN-BwJ87HNmJlM9Yg-W6WFHwT3uwn-zCTSedfN_10EOTZNeke_xXZA4OtmdJLBaoM8qYIOIRogsUna4EJiH710BM2MqcfMtp572bF344NvNlqpMEl1UL3OyHqrOC5YHNjkA%3D%3D&attredirects=0")
      await message.channel.send(embed=embed)
      #await message.channel.delete()
  for j in politics:
    if j in message.content:
      embed = discord.Embed(title="Politics Alert!",description=f"{message.author.name} just said ||{j}||.\n Category: **politics**\n Level: **No warning (just don't start a fight lol)**", color=discord.Color.red())
      embed.set_thumbnail(url="https://4cc178fe-a-62cb3a1a-s-sites.googlegroups.com/site/oakvalleycodingclub/home/imageonline-co-overlayed-image%20%282%29.png?attachauth=ANoY7cqXijRN1GluZGYxT0FmjI85hsDJrXhqQGRNQJa88UjJB4g-HPmVEqs0rpnGIpCisOS1UrFjDNCy2-8wRGdx1co2spbMp5JkSGSH7sl4R-vf5kloSZi-i-cqyrr3piuteVo69vqmKdNsneAkYsANwrur_-qHN-BwJ87HNmJlM9Yg-W6WFHwT3uwn-zCTSedfN_10EOTZNeke_xXZA4OtmdJLBaoM8qYIOIRogsUna4EJiH710BM2MqcfMtp572bF344NvNlqpMEl1UL3OyHqrOC5YHNjkA%3D%3D&attredirects=0")
      await message.channel.send(embed=embed)
  if "dog" in message.content:
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    df = r"https://some-random-api.ml/facts/dog"
    facts = requests.get(df)
    data = json.loads(page.text)
    fc = json.loads(facts.text)
    fin = ""
    fin = data["url"]
    #file = discord.File(url = fin)
    embed = discord.Embed()
    embed.title = "Doggo!"
    embed.set_image(url=fin)
    #embed = discord.Embed(title="Doggo!", color=discord.Color.blue())
    #embed.set_image(url=fin)
    #embed.set_footer(text=si)
    await message.channel.send(embed=embed)
  if "weather" in message.content:
    city_name = "San Diego"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
      y = x["main"]
      current_temperature = y["temp"]
      current_pressure = y["pressure"]
      current_humidity = y["humidity"]
      z = x["weather"]
      weather_description = z[0]["description"]
      channeld = 0
      embed = discord.Embed(title=f"Weather in {city_name}")
      embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
      embed.add_field(name="Temperature(C)", value=f"**{current_temperature}°C**", inline=False)
      embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
      embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
      embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
      await message.channel.send(embed=embed)
  if "scoreboard" in message.content:
    author = message.author
    embed = discord.Embed(title="Scoreboard:",description=f"Hey, {message.author.name}, here is Scoreboard A: [Scoreboard A](https://docs.google.com/spreadsheets/u/0/d/1wcgnTEfjJwEh1u1C1awBYxeJocGJFwEn64o5cqR1SU8/htmlembed/sheet?headers=false&gid=0)\n Scoreboard B: [Scoreboard B](https://docs.google.com/spreadsheets/d/18xMrl-4-ckTc_pdGcgBiShFitT25-IjeXSfvfQfhx4w/htmlembed)", color=discord.Color.blue())
    embed.set_thumbnail(url = "https://4cc178fe-a-62cb3a1a-s-sites.googlegroups.com/site/oakvalleycodingclub/home/imageonline-co-overlayed-image%20%282%29.png?attachauth=ANoY7cqXijRN1GluZGYxT0FmjI85hsDJrXhqQGRNQJa88UjJB4g-HPmVEqs0rpnGIpCisOS1UrFjDNCy2-8wRGdx1co2spbMp5JkSGSH7sl4R-vf5kloSZi-i-cqyrr3piuteVo69vqmKdNsneAkYsANwrur_-qHN-BwJ87HNmJlM9Yg-W6WFHwT3uwn-zCTSedfN_10EOTZNeke_xXZA4OtmdJLBaoM8qYIOIRogsUna4EJiH710BM2MqcfMtp572bF344NvNlqpMEl1UL3OyHqrOC5YHNjkA%3D%3D&attredirects=0")
    await message.channel.send(embed=embed)
#@bot.command()
#async def scoreboard(ctx, num=None):
  #await ctx.send("Key:\n NaN = Empty")
  #html = requests.get(URL).content
  #df_list = pd.read_html(html)
  #df = df_list[-1]
  #print(df)
  #df.to_csv('my data.csv')
  #await ctx.send("```css\n" + str(df) + "\n ```")
#@bot.command()
#async def email(subject, *, sender, reciever, body):
  #send_email(sender, reciever, subject, body)
bot.run("ODU0ODkwMTEyNjYzMTU4ODM5.YMqgdQ.Ffdg9Gat0N5n6E2N4xiD9PF8amQ")
