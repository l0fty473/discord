import discord

class MyClient(discord.Client):

async def on_ready(self):
print('Logged on as', self.user)

async def on_message(self, message):
word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service']

# don't respond to ourselves
if message.author == self.user:
return

messageContent = message.content
if len(messageContent) > 0:
for word in word_list:
if word in messageContent:
await message.delete()
await message.channel.send('Do not say that!')

messageattachments = message.attachments
if len(messageattachments) > 0:
for attachment in messageattachments:
if attachment.filename.endswith(".dll"):
await message.delete()
await message.channel.send("No DLL's allowed!")
elif attachment.filename.endswith('.exe'):
await message.delete()
await message.channel.send("No EXE's allowed!")
else:
break

client = MyClient(bbIB2eaiU1N4KPuly9Q67CBSENR00ZVn)
client.run('ODY3NjQzNDEzMzEwMDc5MDA2.YPkF5Q.cZWX91jHzo8z87BG_NJWNEJKtkY')