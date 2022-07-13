import requests
import nextcord
from nextcord.ext import commands
from os import system 
from colorama import Fore
from time import sleep
import pastebin

pastebincode = ""
pastebin_cookie = ""
tokens = ""
guild_id = 996327148509986876
channelcommand = 996705380077948978
prefixs = "!"
api = pastebin.login(pastebin_cookie)

class Addhwid(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            title="เพิ่ม Hiwd",
            custom_id="persistent_modal:feedback",
            timeout=None,
        )

        self.a = nextcord.ui.TextInput(
            label="เลข HWID",
            max_length=3000,
            custom_id="persistent_modal:a",
        )
        self.add_item(self.a)

    async def callback(self, interaction: nextcord.Interaction):
        embedaddhwid = nextcord.Embed(title="AddHwid | General `Store", description=f"``` เพิ่ม {self.a.value} สำเร็จ 🟢```", colour=0x52ac29)
        embedaddhwid.set_footer(text="General `Store | Discord : SONGKRAN#2007")
        await interaction.send(embed=embedaddhwid)
        old = requests.get(f"https://pastebin.com/raw/{pastebincode}").text
        api.edit(pastebincode, old + "\n" + self.a.value)
        
class Removehwid(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            title="ลบ Hiwd",
            custom_id="persistent_modal:feedback",
            timeout=None,
        )

        self.b = nextcord.ui.TextInput(
            label="เลข HWID",
            max_length=3000,
            custom_id="persistent_modal:b",
        )
        self.add_item(self.b)

    async def callback(self, interaction: nextcord.Interaction):
        embedremovehwid = nextcord.Embed(title="RemoveHwid | General `Store", description=f"``` ลบ {self.b.value} สำเร็จ 🟢```", colour=0x52ac29)
        embedremovehwid.set_footer(text="General `Store | Discord : SONGKRAN#2007")
        await interaction.send(embed=embedremovehwid)
        old = requests.get(f"https://pastebin.com/raw/{pastebincode}").text
        api.edit(pastebincode, old.replace(self.b.value + "\n", ""))
 

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_modals_added = False

    async def on_ready(self):
        if not self.persistent_modals_added:
            self.add_modal(Addhwid())
            self.add_modal(Removehwid())
            self.persistent_modals_added = True
            system('cls')
            print(' -----')
            print('\n > Login....')
            sleep(1)
            system('cls')
            print(' -----')
            print(f'{Fore.GREEN}\n > Login Token client Done!{Fore.RESET}')
            sleep(0.5)
            system('cls')
            print(' -----')
            print(f'\n > Login Token client : {bot.user}')
            print('\n -----')
            await bot.change_presence(activity=nextcord.Game(name="General `Store"))
    
bot = Bot(command_prefix=prefixs)

@bot.slash_command(
    name="addhwid",
    description="สำหรับเพิ่มHwid เท่านั้น!!",
    guild_ids=[guild_id],
)
async def addhwid (interaction: nextcord.Interaction):
    if (interaction.channel.id == channelcommand):
        await interaction.response.send_modal(Addhwid())

@bot.slash_command(
    name="removehwid",
    description="สำหรับลบHwid เท่านั้น!!",
    guild_ids=[guild_id],
)
async def removehwid (interaction: nextcord.Interaction):
    if (interaction.channel.id == channelcommand):
        await interaction.response.send_modal(Removehwid())
        
bot.run(tokens)