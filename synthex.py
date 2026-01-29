import os
import json
import socket
import logging
import string
from discord.ext import commands, tasks
import requests
from colorama import Fore, Style
import qrcode
import chess  # For chess board logic
import chess.svg  # Optional for SVG rendering (if needed)
import string
import random
import qrcode
from io import BytesIO
import html
import random
import urllib.parse
import asyncio
import discord, aiohttp
from discord.ext import commands
import asyncio
import pytz
import base64
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import sys
import threading
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
from io import BytesIO
import webbrowser
from discord import Webhook, RequestsWebhookAdapter
from bs4 import BeautifulSoup
import datetime
from pyfiglet import Figlet
from discord import Member
import openai
from dateutil import parser
from collections import deque
from googletrans import Translator, LANGUAGES
import os,sys,base64,zlib,marshal
import image
import hashlib
import afk
import antinuke
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning)

config = json.load(open("config.json", encoding="utf-8"))

colorama.init()

intents = discord.Intents.default()
intents.presences = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True
intents.guild_messages = True

def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Welcome ===
prefix = config.get('prefix')
token = config.get('token')
api_key = config.get('api_key')
ltc_priv_key = config.get('ltckey')
ltc_addy = config.get("LTC_ADDY")
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC_ADDY")
Upi = config.get("Upi")
upi_id = config.get("Upi")
Qr = config.get("Qr")
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
#===================================

# Import necessary libraries
from discord.ext import commands

# Bot configuration
siddhu = commands.Bot(
    description="SELFBOT CREATED BY SIDDHU",
    command_prefix=prefix,  # Define your prefix variable earlier in the code
    self_bot=True,
    intents=intents,  # Define your intents variable earlier in the code
    case_insensitive=True  # Makes the commands case-sensitive
)

# Remove the default help command
siddhu.remove_command("help")

# Task variable for custom status (if needed later)
status_task = None

af_file = "af.json"

if os.path.exists(af_file):
    with open(af_file, "r") as f:
        af_triggers = json.load(f)
else:
    af_triggers = {}

import json

with open("config.json", "r") as f:
    config = json.load(f)
    
fig = Figlet(font='big')  # You can change the font here
ascii_artt = fig.renderText("SYNTHEX")  # Replace with your text

red = "\033[91m"
yellow = "\033[93m"
green = "\033[92m"
blue = "\033[36m"
pretty = "\033[95m"
magenta = "\033[35m"
lightblue = "\033[94m"
cyan = "\033[96m"
gray = "\033[37m"
reset = "\033[0m"
pink = "\033[95m"
dark_green = "\033[92m"
yellow_bg = "\033[43m"
clear_line = "\033[K"

import logging
import discord

import json
import requests

CONFIG_PATH = "config.json"

@siddhu.event
async def on_ready():
                
    # Load config
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    # Check if password is not set
    if config_data['password'] == "Put_here":
        print("\n    [❌] ERROR: It looks like you haven't entered your password in config.json.")
        print("    [⚠️] Please open config.json, set your password, and restart the bot.\n")
        time.sleep(5)  # Optional: delay so user can read the message
        exit()

    # Load the channel ID and send the message to the specified channel
    try:
        with open("reboot_channel.json", "r") as file:
            data = json.load(file)
            channel_id = data.get("channel_id")

        # Get the channel object using the stored channel ID
        channel = siddhu.get_channel(channel_id)
        if channel:
            await channel.send("<:lr_tick_1:1290693800808677461> Bot restarted successfully!")

        # Clear the file after sending the message
        with open("reboot_channel.json", "w") as file:
            json.dump({}, file)  # Overwrite with an empty JSON object

    except (FileNotFoundError, json.JSONDecodeError):
        pass  # If the file is not found or has an error, do nothing

    # Initialize bot info variables
    user = siddhu.user
    joined_servers = len(siddhu.guilds)  # Initialize this value to the number of servers the bot is in
    friends_count = len(user.friends) if hasattr(user, "friends") else "N/A"
    prefix = config_data.get('prefix')
    
    status_to_set = discord.Status.online  # default status

    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            try:
                config = json.load(f)
                saved_status = config.get("presence_status", "online")
                status_map = {
                    "online": discord.Status.online,
                    "idle": discord.Status.idle,
                    "dnd": discord.Status.dnd,
                    "offline": discord.Status.offline
                }
                status_to_set = status_map.get(saved_status, discord.Status.online)
            except Exception:
                pass

    await siddhu.change_presence(status=status_to_set)
    
    print(f"Commands loaded in as {siddhu.user} (ID: {siddhu.user.id})")

    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.green_to_cyan,
                ascii_artt,
                1
            )
        )
    )

    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.blue_to_purple,
                f"""✮ THE ALL-IN-ONE MULTIPURPOSE SELFBOT ✮

≫ USING SYNTHEX = AUTO ACCEPTING ALL TOS
≫ CRACKING OR MODIFYING WILL TERMINATE YOUR LICENSE

➣ Discord    : https://discord.gg/g4Hv6Rxquv
➣ Instagram  : whoiz.siddhu
➣ Autobuy    : https://siddhushop.mysellauth.com

[+] ----------------------------------------------- [+]
[=] DEVELOPER   :- siddhu.og
[=] LOGGED IN   :- {siddhu.user.name}
[=] USER ID     :- {siddhu.user.id}
[=] SERVERS     :- {joined_servers}
[=] FRIENDS     :- {friends_count}
[=] PREFIX      :- {prefix}
[=] VERSION     :- 5.3
[+] ----------------------------------------------- [+]
                """,
                1
            )
        )
    )

def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

message_cache = {}

#=== Welcome ===
prefix = config.get('prefix')
token = config.get('token')
api_key = config.get('apikey')
ltc_priv_key = config.get('ltckey')
ltc_addy = config.get("LTC_ADDY")
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC_ADDY")
Upi = config.get("Upi")
upi_id = config.get("Upi")
Qr = config.get("Qr")
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
#===================================

logger = logging.getLogger(__name__)

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

time_rn = get_time_rn()

import discord
import requests
import json

import discord
from discord.ext import commands
import json
import requests
import re  # Added regex for better Nitro sniping

from discord.ext.commands import Context

with open("config.json", "r") as f:
    config = json.load(f)

webhook_url = config.get("webhook_url")
embed_channel_id = int(config.get("embed_channel_id", 0))
embed_color = int(config.get("embed_color", "#00ffff").replace("#", ""), 16)

@siddhu.event
async def on_message(message):
    """Handles message events including aliases, snipers, spying, and other features."""
    
    if message.author.bot:  # Ignore bots
        return
        
    message_cache[message.id] = message
    if len(message_cache) > 1000:
        message_cache.pop(next(iter(message_cache)))
        
    # Load configuration settings from config.json
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return  # Skip processing if config is missing/corrupt

    # Extract settings from config
    prefix = config.get("prefix", ".")  # Default prefix is "."

    # **Alias Handling**
    if message.content.startswith(prefix):
        command_body = message.content[len(prefix):].split(" ")[0]  # Extract the command name
        if command_body in command_aliases:  # Check if it's an alias
            new_command = prefix + command_aliases[command_body] + message.content[len(prefix) + len(command_body):]
            message.content = new_command  # Replace alias with the original command

    # Extract settings from config
    nitro_sniper_enabled = config.get("nitro_sniper", False)
    giveaway_sniper_enabled = config.get("giveaway_sniper", False)
    privnote_sniper_enabled = config.get("privnote_sniper", False)
    nitro_webhook = config.get("nitro_webhook")
    giveaway_webhook = config.get("giveaway_webhook")
    privnote_webhook = config.get("privnote_webhook")
    bot_list = config.get("bot_list", [])
    main_account_token = config.get("token", "")
    prefix = config.get("prefix", ".")

    # 🔥 **NITRO SNIPER**
    if nitro_sniper_enabled:
        nitro_match = re.search(r"(discord\.(gift|com/gifts)/[a-zA-Z0-9]+)", message.content)
        if nitro_match:
            nitro_code = nitro_match.group(1).split("/")[-1]  # Extract code
            
            if not nitro_webhook:
                await message.channel.send("❌ Set a Nitro Sniper webhook using `.nwebhook <link>` first.")
                return

            # Attempt to redeem Nitro
            headers = {"Authorization": main_account_token}
            response = requests.post(f"https://discord.com/api/v9/entitlements/gift-codes/{nitro_code}/redeem", headers=headers)

            embed = {
                "title": "🎁 Nitro Gift Sniped!",
                "description": f"Code: `{nitro_code}`",
                "color": 65280 if response.status_code == 200 else 16711680,  # Green if success, Red if fail
                "footer": {"text": "SyntheX Prime V5 (Nitro Sniper)"}
            }
            requests.post(nitro_webhook, json={"embeds": [embed]})

    # 🎉 **GIVEAWAY SNIPER**
    if giveaway_sniper_enabled and message.author.id in bot_list:
        if any(word in message.content.lower() for word in ["giveaway", "🎉", "ends", "hosted"]):
            try:
                await message.add_reaction("🎉")
            except discord.Forbidden:
                pass  # Ignore errors if reaction fails
            
            giveaway_embed = {
                "title": "🎉 Joined Giveaway",
                "description": f"Server: **{message.guild.name}**\n[Jump to Message]({message.jump_url})",
                "color": 16776960  # Yellow
            }
            requests.post(giveaway_webhook, json={"embeds": [giveaway_embed]})

    # 📝 **PRIVNOTE SNIPER**
    if privnote_sniper_enabled and "privnote.com" in message.content:
        if not privnote_webhook:
            await message.channel.send("❌ Set a Privnote Sniper webhook using `.pwebhook <link>` first.")
            return

        privnote_embed = {
            "title": "📝 Privnote Sniped",
            "description": "Possible Privnote link found!",
            "color": 3447003  # Blue
        }
        requests.post(privnote_webhook, json={"embeds": [privnote_embed]})

    # 👀 **SPY SYSTEM**
    try:
        with open("spy.json", "r") as f:
            spy_config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        spy_config = {"spy_webhook": "", "spy_data": {}}

    if str(message.author.id) in spy_config["spy_data"]:
        spy_webhook = spy_config.get("spy_webhook")
        if spy_webhook:
            if message.guild:
                channel_link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}"
                channel_name = f"[#{message.channel.name}]({channel_link})"
            else:
                channel_name = "📩 Direct Message"

            content = message.content.strip() or "*No text content (maybe embed or attachment)*"

            spy_embed = {
                "title": "🔍 Message Sent",
                "description": (
                    f"    👤 **User:** {message.author.mention} ({message.author})\n"
                    f"    💬 **Message in:** {channel_name}\n"
                    f"    📜 **Content:** {content}"
                ),
                "color": 3447003
            }

            try:
                requests.post(spy_webhook, json={"embeds": [spy_embed]})
            except Exception as e:
                print(f"[SpyWebhook Error] {e}")

    # 🔔 PING SPOOF SYSTEM (Restored)
    if f"<@{siddhu.user.id}>" in message.content:
        try:
            with open("ping_spoof.json", "r") as f:
                ping_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            ping_data = {"enabled": False, "webhook_url": ""}

        if ping_data.get("enabled", False) and ping_data.get("webhook_url"):
            webhook_url = ping_data["webhook_url"]

            location = (
                "DM" if isinstance(message.channel, discord.DMChannel)
                else message.guild.name
            )
            channel_name = (
                "DM" if isinstance(message.channel, discord.DMChannel)
                else message.channel.mention
            )

            ping_embed = {
                "title": "<a:Online_Ping:1389619441612095659> New Ping Detected",
                "color": 15105570,
                "fields": [
                    {
                        "name": "<:user:1325418236514140282> Author",
                        "value": f"{message.author.mention} ({message.author})",
                        "inline": False
                    },
                    {
                        "name": "<:Discord_bots:1290700055514452121> Location",
                        "value": location,
                        "inline": True
                    },
                    {
                        "name": "<:emoji_1738476614300:1335492458909401088> Channel",
                        "value": channel_name,
                        "inline": True
                    },
                    {
                        "name": "<:uptime:1320649297796010075> Pinged At",
                        "value": f"<t:{int(message.created_at.timestamp())}:F>",
                        "inline": False
                    },
                    {
                        "name": "<:rules:1290926829762383934> Message Content",
                        "value": message.content[:1024] if message.content else "*Empty Message*",
                        "inline": False
                    }
                ]
            }

            try:
                requests.post(webhook_url, json={"embeds": [ping_embed]})
            except Exception as e:
                print(f"[Ping Spoof] Webhook failed: {e}")

# 🤖 **AUTO-RESPONSES**
    try:
        with open('ar.json', 'r') as file:
            auto_responses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        auto_responses = {}

    if message.content in auto_responses:
        await message.delete()  # Delete the trigger message
        await message.channel.send(auto_responses[message.content])
        return  # Stop further processing if auto-response is handled

    trigger = message.content.strip().lower()
    if trigger in af_triggers:
        data = af_triggers[trigger]
        msg_id = data["message_id"]
        source_channel_id = data["channel_id"]

        headers = {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0',
            'Accept': '*/*'
        }

        payload = {
            "message_reference": {
                "message_id": int(msg_id),
                "channel_id": int(source_channel_id),
                "guild_id": message.guild.id if message.guild else None,
                "type": 1
            }
        }

        url = f"https://discord.com/api/v10/channels/{message.channel.id}/messages"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as resp:
                if resp.status == 429:
                    retry_after = (await resp.json()).get("retry_after", 1)
                    await asyncio.sleep(retry_after)
                elif resp.status != 200:
                    print(f"[AF Error] Status {resp.status}: {await resp.text()}")

    await siddhu.process_commands(message)
    
    # Auto-message handling
def load_auto_messages():
    try:
        with open("am.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_auto_messages(data):
    with open("am.json", "w") as f:
        json.dump(data, f, indent=4)

# File Paths
TRANSACTIONS_FILE = "transactions.txt"

# API Keys
TATUM_API_KEY = "t-662bd6a3b6c859001c3e5564-723b6f686e1f48b99a77e966"
BLOCKCYPHER_TOKEN = "dff9cc4b3fc444199146778b53bcc6de"

# Function to send LTC using Tatum API
async def send_ltc(ltc_address, ltc_key, recipient_address, amount):
    url = 'https://api.tatum.io/v3/litecoin/transaction'
    payload = {
        "fromAddress": [
            {
                "address": ltc_address,
                "privateKey": ltc_key,
            }
        ],
        "to": [
            {
                "address": recipient_address,
                "value": amount
            }
        ],
        "fee": "0.00005",
        "changeAddress": ltc_address
    }
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': TATUM_API_KEY
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    if 'txId' in response_data:
        tx_id = response_data['txId']

        with open(TRANSACTIONS_FILE, "a") as f:
            f.write(f"{datetime.datetime.now()} | FROM: {ltc_address} | TO: {recipient_address} | AMOUNT: {amount} LTC | TX ID: {tx_id}\n")

        logger.info("✅ New Transaction Successfully Sent")
        return tx_id
    else:
        raise Exception(f"❌ Failed to send LTC. Response: {response_data}")

@siddhu.command()
async def send(ctx, wallet_num, recipient_address: str, amount: str):
    try:
        with open("wallet.json", "r") as f:
            wallets = json.load(f)

        if wallet_num not in wallets:
            await ctx.send("`❌ Wallet not found.`")
            return

        wallet_info = wallets[wallet_num]
        sender_address = wallet_info.get("address")
        sender_private_key = wallet_info.get("private_key")

        # Convert USD to LTC
        coingecko_resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        coingecko_resp.raise_for_status()
        ltc_to_usd_rate = coingecko_resp.json()['litecoin']['usd']
        converted_ltc_amount = round(float(amount) / ltc_to_usd_rate, 8)

        # Ask for confirmation
        confirm_msg = await ctx.send(
            f"**PAYMENT CONFIRMATION <:TOS:1336669803221614622>**\n"
            f"<:white_arrow:1290693789824061461> **RECEIVER ADDY :-**\n"
            f"<:emoji_1739864737772:1341314670346371095> `{recipient_address}`\n"
            f"<:exchange:1322954260404768850> **AMOUNT:** `{amount}$` ( `{converted_ltc_amount}` LTC )\n"
            f"<:rdx_glowin_heart:1288196137848803451> __Type__ `Yes` __to confirm or__ `No` __to Cancel !__"
        )

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]

        try:
            user_response = await ctx.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("<:unclaim:1322611845642719287> Transaction timed out. Canceled.")
            return

        if user_response.content.lower() == "no":
            await ctx.send("<:unclaim:1322611845642719287> Transaction canceled by user.")
            return

        # Send transaction
        tx_id = await send_ltc(sender_address, sender_private_key, recipient_address, converted_ltc_amount)

        with open("config.json", "r") as f:
            config = json.load(f)
        ltc_webhook = config.get("ltc_webhook")

        tx_link = f"https://live.blockcypher.com/ltc/tx/{tx_id}/"

        if embed_mode_enabled:
            fields = [
                {"name": "<a:tz_ltc:1378241581257326683> To address", "value": f"`{recipient_address}`", "inline": False},
                {"name": "Amount sent", "value": f"<:RS_LTC:1291423858183897120> {converted_ltc_amount} LTC (≈ ${amount})", "inline": True},
                {"name": "Total charged", "value": f"<:RS_LTC:1291423858183897120> {converted_ltc_amount} LTC (≈ ${amount})", "inline": True},
                {"name": "<:TOS:1336669803221614622> Transaction ID", "value": f"[{tx_id[:12]}...]({tx_link})", "inline": False},
            ]

            await send_custom_embed(
                ctx,
                title="<:tz_Verified:1281238102823665797> Litecoin Sent Successfully",
                description="Payment confirmed, Please allow a few minutes for confirmation on the blockchain.",
                fields=fields
            )
        else:
            msg = (
                f"<:tz_Verified:1281238102823665797> | **Successfully Sent `{amount}$` LTC <a:tz_ltc:1281238097136451616>**\n"
                f"<:white_arrow:1290693789824061461>**SENT TO:** `{recipient_address}`\n"
                f"<:white_arrow:1290693789824061461>**SENT FROM:** `{sender_address}`\n"
                f"<:bxbz_monet_lovenote:1290693793724497920> | __**TRANSACTION ID :-**__\n"
                f"{tx_link}"
            )
            await ctx.send(msg)

        if ltc_webhook:
            webhook_payload = {"content": f"LTC Sent: {converted_ltc_amount} LTC to `{recipient_address}`\nTx: <{tx_link}>"}
            requests.post(ltc_webhook, json=webhook_payload)

    except Exception as e:
        await ctx.send(f"`❌ Error sending LTC: {e}`")

# Command to view last 5 transactions
@siddhu.command()
async def wallet_history(ctx):
    try:
        if not os.path.exists(TRANSACTIONS_FILE) or os.stat(TRANSACTIONS_FILE).st_size == 0:
            await ctx.send("⚠️ No transactions found.")
            return

        with open(TRANSACTIONS_FILE, "r") as f:
            transactions = f.readlines()[-5:]  # Get last 5 transactions

        history_text = "**# LTC TRANSACTIONS <:TOS:1336669803221614622>**\n"
        history_text += "**<:white_arrow:1290693789824061461> LAST 5 TRANSACTIONS MADE USING THE `send` COMMAND!**\n\n"

        for index, tx in enumerate(transactions, start=1):
            parts = tx.strip().split(" | ")
            if len(parts) < 5:
                continue  # Skip invalid transaction lines

            timestamp, from_wallet, to_wallet, amount, tx_id = parts

            history_text += (
                f"**<:0001:1335318578060329072> TRANSACTION {index}**\n"
                f"<:emoji_1739864737772:1341314670346371095> FROM: `{from_wallet.split(': ')[1]}`\n"
                f"<:emoji_1739864737772:1341314670346371095> TO: `{to_wallet.split(': ')[1]}`\n"
                f"<:emoji_1739864737772:1341314670346371095> AMOUNT: `{amount.split(': ')[1]}`\n"
                f"<:emoji_1739864737772:1341314670346371095> TIME: `{timestamp}`\n"
                f"<:emoji_1739864737772:1341314670346371095> TX LINK: https://live.blockcypher.com/ltc/tx/{tx_id.split(': ')[1]}/\n\n"
            )

        await ctx.send(history_text)

    except Exception as e:
        await ctx.send(f"❌ Error fetching history: {e}")
        logger.error(f"❌ Error fetching history: {e}")

# Function to get LTC wallet details
def get_address_details(address):
    url = f'https://api.blockcypher.com/v1/ltc/main/addrs/{address}'
    params = {'token': BLOCKCYPHER_TOKEN}
    response = requests.get(url, params=params)
    return response.json()

import requests
import json
import asyncio
import datetime
from discord.ext import commands

# Replace this with your actual Tatum API key
TATUM_API_KEY = "t-662bd6a3b6c859001c3e5564-723b6f686e1f48b99a77e966"

async def send_usdt_trc20(sender_address, private_key, recipient_address, amount):
    url = "https://api.tatum.io/v3/tron/transaction"
    payload = {
        "from": sender_address,
        "to": recipient_address,
        "amount": amount,
        "privateKey": private_key
    }
    headers = {
        "x-api-key": TATUM_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()

    if "txId" in result:
        return result["txId"]
    else:
        raise Exception(f"Tatum Error: {result}")

@siddhu.command()
async def sendusdt(ctx, wallet_num, recipient_address: str, amount: str):
    try:
        with open("usdt_wallet.json", "r") as f:
            wallets = json.load(f)

        if wallet_num not in wallets:
            await ctx.send("❌ Wallet not found.")
            return

        wallet = wallets[wallet_num]
        sender_address = wallet["address"]
        sender_private_key = wallet["private_key"]

        confirm_msg = await ctx.send(
            f"**<:icons_usdt:1123524727757905941> USDT TRC20 Payment Confirmation <:TOS:1336669803221614622>**\n"
            f"<:icons_send:1123526432069337228> **FROM:** `{sender_address}`\n"
            f"<:icons_receive:1123526633875781662> **TO:** `{recipient_address}`\n"
            f"<:icons_amount:1123526740125085797> **AMOUNT:** `{amount} USDT`\n\n"
            f"__Type__ `yes` __to confirm or__ `no` __to cancel__"
        )

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]

        try:
            user_reply = await ctx.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("⌛ Timed out.")
            return

        if user_reply.content.lower() == "no":
            await ctx.send("❌ Cancelled.")
            return

        tx_id = await send_usdt_trc20(sender_address, sender_private_key, recipient_address, amount)

        with open("config.json", "r") as f:
            config = json.load(f)
        webhook = config.get("usdt_webhook")

        result_msg = (
            f"<:icons_verified:1123527052548516000> **Successfully Sent `{amount}` USDT (TRC20)**\n"
            f"<:icons_send:1123526432069337228> **FROM:** `{sender_address}`\n"
            f"<:icons_receive:1123526633875781662> **TO:** `{recipient_address}`\n"
            f"<:icons_link:1123527255036469330> **TX:** https://tronscan.org/#/transaction/{tx_id}"
        )

        if webhook:
            requests.post(webhook, json={"content": result_msg})

        await ctx.send(result_msg)

    except Exception as e:
        await ctx.send(f"❌ Error: `{e}`")

@siddhu.command(name='ubal')
async def ubal(ctx, address: str):
    """
    Fetch the USDT TRC20 balance of a TRON address and display it in the same format as .bal.
    """
    await ctx.message.delete()

    if not address.startswith("T") or len(address) != 34:
        await ctx.send("❌ Invalid TRC20 address.", delete_after=5)
        return

    try:
        # Fetch TRC20 tokens from Tronscan API
        url = f"https://apilist.tronscanapi.com/api/account/token?address={address}&limit=100&start=0"
        res = requests.get(url)
        res.raise_for_status()
        tokens = res.json().get("tokenBalances", [])

        # USDT TRC20 token ID on Tron
        usdt_token = next((t for t in tokens if t.get("tokenId") == "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"), None)

        if not usdt_token:
            await ctx.send("❌ USDT not found in this address.", delete_after=5)
            return

        # Parse balances
        confirmed_balance_usdt = int(usdt_token.get("balance", 0)) / 1e6
        total_received_usdt = int(usdt_token.get("total", 0)) / 1e6

        # Format message using same style as `.bal`
        response = (
            f"# <:Frostmm_USDT:1378242966388215922> **USDT Wallet Info**\n"
            f"**➤ Address:** `{address}`\n\n"
            f"<:crypto:1322611842316501073> **Total Received:** `{total_received_usdt:,.2f} USDT` (~`${total_received_usdt:,.2f}`)\n"
            f"<:money:1290693786401247356> **Confirmed Balance:** `{confirmed_balance_usdt:,.2f} USDT` (~`${confirmed_balance_usdt:,.2f}`)\n"
        )

        await ctx.send(response)

    except Exception as e:
        await ctx.send(f"⚠️ Error fetching balance:\n`{str(e)}`", delete_after=6)

@siddhu.command(name='myubal')
async def myubal(ctx, wallet_num: str):
    await ctx.message.delete()

    try:
        with open('usdt_wallet.json', 'r') as f:
            wallets = json.load(f)
    except Exception as e:
        await ctx.send(f"❌ Failed to load wallet file.\n`{e}`", delete_after=5)
        return

    if wallet_num not in wallets:
        await ctx.send(f"❌ Wallet `{wallet_num}` not found in `usdt_wallet.json`", delete_after=5)
        return

    address = wallets[wallet_num]['address']

    try:
        url = f"https://apilist.tronscanapi.com/api/accountv2?address={address}"
        response = requests.get(url)
        data = response.json()

        usdt_token = next(
            (t for t in data.get("trc20token_balances", []) if t["tokenName"] == "Tether USD"),
            None
        )

        if not usdt_token:
            raise ValueError("USDT balance not found.")

        confirmed_balance_usdt = float(usdt_token["balance"]) / (10 ** int(usdt_token["tokenDecimal"]))
        total_received_usdt = float(usdt_token.get("total", usdt_token["balance"])) / (10 ** int(usdt_token["tokenDecimal"]))

    except Exception as e:
        await ctx.send(f"❌ Failed to fetch balance info.\n`{e}`", delete_after=6)
        return

    msg = (
        f"# <:Frostmm_USDT:1378242966388215922> **USDT Wallet Info (Wallet {wallet_num})**\n"
        f"**➤ Address:** `{address}`\n\n"
        f"<:crypto:1322611842316501073> **Total Received:** `{total_received_usdt:,.2f} USDT` (~`${total_received_usdt:,.2f}`)\n"
        f"<:money:1290693786401247356> **Confirmed Balance:** `{confirmed_balance_usdt:,.2f} USDT` (~`${confirmed_balance_usdt:,.2f}`)\n"
    )

    await ctx.send(msg)

@siddhu.command()
async def uaddy(ctx, wallet_num: str):
    """
    Fetch and display the USDT address for a specified wallet.
    Args:
        wallet_num (str): The identifier of the wallet in `usdt_wallet.json`.
    """
    try:
        # Open and read the USDT wallet file
        with open("usdt_wallet.json", "r") as f:
            wallets = json.load(f)

        # Check if the wallet exists
        if wallet_num in wallets:
            wallet_info = wallets[wallet_num]
            addy = wallet_info.get("address", "Address not found.")
        else:
            await ctx.send("`Address Not Found In Wallets`")
            return

        # Delete the command message
        await ctx.message.delete()

        # Compose message using same style as LTC
        full_message = (
            "# <:Frostmm_USDT:1378242966388215922> __**USDT ADDY**__ <:Frostmm_USDT:1378242966388215922>\n"
            f"> <:rdx_glowin_heart:1288196137848803451> **ADDY FOR :** `WALLET {wallet_num}`\n"
            f"{addy}\n"
            "> <:white_arrow:1290693791983861822> **MUST SEND SCREENSHOT / BLOCKCHAIN AFTER PAYMENT**"
        )

        await ctx.send(full_message)

    except FileNotFoundError:
        await ctx.send("`Wallet file not found. Please ensure usdt_wallet.json exists in the directory.`")
    except json.JSONDecodeError:
        await ctx.send("`Failed to parse usdt_wallet.json. Please check the file format.`")
    except Exception as e:
        await ctx.send(f"`An error occurred: {str(e)}`")

import discord
from discord.ext import commands
import json
import os
import sys
import time

@siddhu.command()
async def restart(ctx):
    """Reboot the bot."""
    # Store the channel ID where the command was used
    channel_id = ctx.channel.id

    # Save the channel ID to a JSON file
    with open("reboot_channel.json", "w") as file:
        json.dump({"channel_id": channel_id}, file)

    # Send "Restarting bot..." message
    await ctx.send("🔄 Restarting bot... Please wait!")

    # Wait for a brief moment before restarting
    time.sleep(2)

    # Get the absolute path of run.py
    script_path = os.path.abspath("run.py")

    # Restart the bot by executing run.py again
    os.execv(sys.executable, [sys.executable, script_path])
    
@siddhu.command()
async def change_account(ctx, new_token: str):
    """Change selfbot account by switching token with confirmation and restarting."""
    import aiohttp
    import asyncio
    import os
    import sys
    import json
    import time

    # Get username from token
    headers = {"Authorization": new_token}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://discord.com/api/v9/users/@me", headers=headers) as res:
            if res.status != 200:
                await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid token or failed to fetch user info.")
                return
            data = await res.json()
            username = data['username']  # No discriminator anymore

    # Ask for confirmation
    await ctx.send(f"⚠️ Do you want to close the bot and log in to **{username}**?\nReply with `y` or `n` within 30 seconds.")

    def check(m):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content.lower() in ['y', 'n']

    try:
        msg = await siddhu.wait_for("message", timeout=30, check=check)
        if msg.content.lower() == 'y':
            # Update token in config.json
            with open("config.json", "r") as f:
                config = json.load(f)
            config["token"] = new_token
            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)

            await ctx.send("✅ Token updated. Restarting bot...")

            time.sleep(2)
            os.execv(sys.executable, [sys.executable, os.path.abspath("run.py")])
        else:
            await ctx.send("❌ Account switch cancelled.")
    except asyncio.TimeoutError:
        await ctx.send("⌛ Timed out. No response received.")

@siddhu.command()
async def set_i2c(ctx, rate: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['I2C_rate'] = rate
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> I2C rate updated to {rate}")

@siddhu.command()
async def set_c2i(ctx, rate: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['C2I_rate'] = rate
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> C2I rate updated to {rate}")
    
import discord
from discord.ext import commands
import json
import requests  # Use requests instead of discord.Webhook

# Function to load spy data from spy.json
def load_spy_data():
    try:
        with open("spy.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"spy_webhook": "", "spy_data": {}}

# Function to save spy data to spy.json
def save_spy_data(data):
    with open("spy.json", "w") as f:
        json.dump(data, f, indent=4)

# Initialize spy data
spy_config = load_spy_data()

def log_spy_activity(user, activity, description):
    """Logs spy activity and sends it to the webhook."""
    spy_webhook = spy_config.get("spy_webhook")
    if spy_webhook:
        spy_embed = {
            "title": f"🔍 {activity}",
            "description": (
                f"👤 **User:** {user.mention} ({user.name}#{user.discriminator})\n"
                f"{description}"
            ),
            "color": 3447003  # Blue
        }
        requests.post(spy_webhook, json={"embeds": [spy_embed]})

@siddhu.event
async def on_typing(channel, user, when):
    if str(user.id) in spy_config["spy_data"]:
        channel_info = channel.mention if hasattr(channel, "mention") else "📩 Direct Message"

        log_spy_activity(
            user,
            "Typing Detected",
            f"⌨️ **Channel:** {channel_info} at `{when.strftime('%H:%M:%S')}`"
        )

@siddhu.event
async def on_user_update(before, after):
    if str(after.id) in spy_config["spy_data"]:
        if before.name != after.name:
            log_spy_activity(
                after,
                "Username Changed",
                f"📝 **Before:** {before.name}\n✏️ **After:** {after.name}"
            )
        if before.avatar != after.avatar:
            log_spy_activity(
                after,
                "Avatar Changed",
                f"🖼️ {after.name} changed their avatar."
            )
            
@siddhu.event
async def on_presence_update(before, after):
    if str(after.id) in spy_config["spy_data"]:
        if before.status != after.status:
            log_spy_activity(
                after,
                "Status Changed",
                f"🟢 **Before:** {before.status}\n🔴 **After:** {after.status}"
            )

        prev_activity = previous_presence.get(after.id)
        current_activity = after.activity

        if prev_activity != current_activity:
            if current_activity:
                activity_type = str(current_activity.type).split(".")[-1].capitalize()
                log_spy_activity(
                    after,
                    f"{activity_type} Activity",
                    f"🎮 {after.name} is now {activity_type.lower()} **{current_activity.name}**"
                )
            else:
                log_spy_activity(after, "Activity Stopped", "🚫 User stopped all activity.")

        previous_presence[after.id] = current_activity

# ✅ **Voice Channel Join/Leave**
@siddhu.event
async def on_voice_state_update(member, before, after):
    if str(member.id) in spy_config["spy_data"]:
        if before.channel != after.channel:
            if after.channel:  # Joined VC
                log_spy_activity(
                    member,
                    "Joined Voice Channel",
                    f"📍 **Server:** {member.guild.name}\n"
                    f"🎤 **Channel:** {after.channel.name}"
                )
            if before.channel:  # Left VC
                log_spy_activity(
                    member,
                    "Left Voice Channel",
                    f"📍 **Server:** {member.guild.name}\n"
                    f"🔇 **Channel:** {before.channel.name}"
                )

# Command to set spy webhook
@siddhu.command()
async def spy_webhook(ctx, url: str):
    """Sets the webhook URL for spy notifications."""
    spy_config['spy_webhook'] = url
    save_spy_data(spy_config)
    await ctx.send(f"Webhook URL set to: {url}")

# Command to start spying on a user
@siddhu.command()
async def spy_user(ctx, user: discord.Member):
    """Starts spying on a user."""
    if not spy_config.get("spy_webhook"):
        await ctx.send("❌ Please set a webhook first using `.spy_webhook <url>`")
        return

    spy_config["spy_data"][str(user.id)] = {"username": str(user)}
    save_spy_data(spy_config)
    await ctx.send(f"✅ Started spying on {user.mention}")

# Command to stop spying on a user
@siddhu.command()
async def close_spy(ctx, user: discord.Member):
    """Stops spying on a user."""
    if str(user.id) in spy_config["spy_data"]:
        del spy_config["spy_data"][str(user.id)]
        save_spy_data(spy_config)
        await ctx.send(f"✅ Stopped spying on {user.mention}")
    else:
        await ctx.send(f"⚠️ Not spying on {user.mention}")

# Command to list all spied users
@siddhu.command()
async def spy_list(ctx):
    """Lists all users currently being spied on."""
    spy_data = spy_config.get("spy_data", {})
    if not spy_data:
        await ctx.send("⚠️ No users are being spied on.")
    else:
        spy_list = "\n".join([f"<@{user_id}> ({info['username']})" for user_id, info in spy_data.items()])
        await ctx.send(f"🔍 Currently spying on:\n{spy_list}")

# Command to clear all spy data
@siddhu.command()
async def clear_spy(ctx):
    """Clears all spy data."""
    spy_config["spy_data"] = {}
    save_spy_data(spy_config)
    await ctx.send("🧹 All spy data cleared.")
    
import discord
from discord.ext import commands
import json
import asyncio
import time
import requests
import wikipedia
from io import BytesIO

# Helper function for current timestamp
def get_timestamp():
    return int(time.time())

import discord
from discord.ext import commands
import requests

import asyncio

@siddhu.command(description="Gives the specified user all roles in the server.")
async def giveallroles(ctx, member: discord.Member):
    await ctx.message.delete()

    success_roles = []
    failed_roles = []

    for role in ctx.guild.roles:
        if role >= ctx.guild.me.top_role:  # Prevents giving higher roles
            failed_roles.append(role.name)
            continue  

        try:
            await member.add_roles(role)
            success_roles.append(role.name)
        except Exception:
            failed_roles.append(role.name)

        await asyncio.sleep(0.5)  # Prevents rate-limiting

    # Send confirmation message
    message_content = f"✅ **Gave {member.mention} all possible roles!**"

    if failed_roles:
        message_content += f"\n⚠️ **Failed roles:** {', '.join(failed_roles)}"

    message = await ctx.send(message_content)
    await asyncio.sleep(5)  # Auto-delete after 5 sec
    await message.delete()

# Command to fetch space news
@siddhu.command()
async def space_news(ctx):
    """Fetch and display the latest space news from NASA."""
    api_key = "cgD4azlalWNFjOH553zhoSoSQMfrsufGcXAHbYvi"  # Replace with your API key from NASA

    # NASA API endpoint for space news
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    try:
        # Sending GET request to the NASA API
        response = requests.get(url)
        data = response.json()  # Parse JSON response
        
        # Check if the response is successful
        if response.status_code == 200:
            title = data.get("title")
            explanation = data.get("explanation")
            image_url = data.get("url")
            
            # Send the space news as a plain text message
            await ctx.send(f"**{title}**\n{explanation}\nImage: {image_url}")
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Could not fetch the space news. Please try again later.")
    
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: {str(e)}")

import requests

# API endpoint for exchange rates
EXCHANGE_API_URL = 'https://api.exchangerate-api.com/v4/latest/EUR'

# Function to fetch exchange rates
def get_exchange_rate():
    try:
        response = requests.get(EXCHANGE_API_URL)
        data = response.json()
        return data['rates']
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Convert Euro to USD
@siddhu.command(name='e2u')
async def e2u(ctx, amount: float):
    rates = get_exchange_rate()
    if rates:
        usd_amount = amount * rates['USD']
        await ctx.send(
            f"# __EURO TO USD__<:exchange:1322965557372260402>\n\n"
            f"> <:exchange:1322954260404768850> **EUR RATE:** `{rates['USD']:.4f} USD`\n"
            f"> <:Money:1290693788226027654> **EURO AMOUNT:** `€{amount:.2f}`\n"
            f"> <:dollar:1322965559134126214> **USD AMOUNT:** `${usd_amount:.2f}`"
        )
        await ctx.message.delete()
    else:
        await ctx.send("❌ Error fetching exchange rates.")

# Convert USD to Euro
@siddhu.command(name='u2e')
async def u2e(ctx, amount: float):
    rates = get_exchange_rate()
    if rates:
        euro_amount = amount / rates['USD']
        await ctx.send(
            f"# __USD TO EURO__ <:exchange:1322965557372260402>\n\n"
            f"> <:exchange:1322954260404768850> **USD RATE:** `{rates['USD']:.4f} EUR`\n"
            f"> <:dollar:1322965559134126214> **USD AMOUNT:** `${amount:.2f}`\n"
            f"> <:Money:1290693788226027654> **EURO AMOUNT:** `€{euro_amount:.4f}`"
        )
        await ctx.message.delete()
    else:
        await ctx.send("❌ Error fetching exchange rates.")

# Command: My Devices
@siddhu.command()
async def mydevices(ctx):
    """List all connected devices."""
    devices = ["Device 1: Laptop", "Device 2: Phone", "Device 3: Tablet"]  # Replace with actual data fetching logic
    await ctx.send(f"🔌 **Your Devices:**\n" + "\n".join(devices))

# Command: Generate Poem
@siddhu.command()
async def genpoem(ctx, *, topic):
    """Generate a random poem."""
    url = f"https://api.poemist.com/v1/randompoems"
    response = requests.get(url)
    if response.status_code == 200:
        poem = response.json()[0]
        await ctx.send(f"📜 **Poem on {topic}:**\n{poem['title']}\n{poem['content']}")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Could not generate a poem.")

# Command: Puzzle
@siddhu.command()
async def puzzle(ctx):
    """Fetch a random puzzle."""
    await ctx.send("🧩 **Here’s your puzzle:**\nWhat comes once in a minute, twice in a moment, but never in a thousand years?")

# Command: Steal Emoji
@siddhu.command()
async def steal_emoji(ctx, url: str, name: str):
    """Add an emoji to the server."""
    try:
        guild = ctx.guild
        response = requests.get(url)
        if response.status_code == 200:
            emoji = await guild.create_custom_emoji(name=name, image=response.content)
            await ctx.send(f"<:Tick:1290693799361777665> Added emoji: {emoji}")
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to download emoji.")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error: {str(e)}")

import discord
import requests
from discord.ext import commands

import re
import requests

@siddhu.command(description="Gets information about a Litecoin transaction using blockcypher.com")
async def ltctx(ctx, txid: str = None):
    await ctx.send(content="🔎 Fetching transaction details...")

    # Check if the command is used as a reply
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        txid_match = re.search(r"([a-fA-F0-9]{64})", replied_msg.content)  # Extract TXID from message

        if txid_match:
            txid = txid_match.group(0)

    # If TXID is a URL, extract only the TXID from it
    if txid and txid.startswith("https://blockchair.com/litecoin/transaction/"):
        txid = txid.split("/")[-1]

    # Validate TXID presence
    if not txid:
        await ctx.send(content="❌ **Please provide a valid Litecoin transaction ID or reply to a message containing one!**")
        return

    # API Request
    url = f"https://api.blockcypher.com/v1/ltc/main/txs/{txid}"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()

        confirmations = res.get("confirmations", "N/A")
        preference = res.get("preference", "N/A")
        confirmed = res.get("confirmed", "Not confirmed").replace("T", " ").replace("Z", "") if res.get("confirmed") else "Not confirmed"
        received = res.get("received", "Not received").replace("T", " ").replace("Z", "") if res.get("received") else "Not received"
        double_spend = res.get("double_spend", "False")

        # Extract sender and receiver addresses
        sent_from = res.get("inputs", [{}])[0].get("addresses", ["Unknown"])[0]
        sent_to = res.get("outputs", [{}])[0].get("addresses", ["Unknown"])[0]

        # Extract LTC amount
        ltc_amount = round(res.get("total", 0) / 1e8, 8)  # Convert satoshis to LTC

        # Fetch USD price (Using CoinGecko API for real-time conversion)
        price_url = "https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd"
        price_res = requests.get(price_url).json()
        ltc_price = price_res.get("litecoin", {}).get("usd", 0)
        usd_amount = round(ltc_amount * ltc_price, 2)

        tx_link = f"https://blockchair.com/litecoin/transaction/{txid}"

        message = f"""
# LTC TX INFO <:exchanger:1322954180452810775>  
**<:nxt_blue_crown:1281973611917348989> Transaction Hash: `{txid}`  
<:white_Arrow:1290693791983861822> TX Link:** [LTC TRANSACTION]({tx_link})  

**<:LTC:1322611807269031968> __PAYMENT INFO :-__**  
<:star_blue:1284898457181622362> **SENT FROM :-**  
<:white_arrow:1290693789824061461>`{sent_from}`  
<:star_blue:1284898457181622362> **SENT TO :-**  
<:white_arrow:1290693789824061461>`{sent_to}`  

<:dollar:1322965559134126214> **USD AMOUNT :-** `${usd_amount}`  
<a:tz_ltc:1281238097136451616> **LTC AMOUNT :-** `{ltc_amount} LTC`  

**<:exchanger:1322954180452810775> __Confirmations :-__**
<:experienced_seller:1290924799421583391> **Confirmations:** `{confirmations}`  
<:star_blue:1284898457181622362> **Preference:** `{preference}`  
<:emoji_1738342244745:1334928872269152259> **Confirmed:** `{confirmed}`  
<:lr_tick_1:1290693800808677461> **Received:** `{received}`  
<a:tz_money:1281238106682560567> **Double Spend:** `{double_spend}`  
        """.strip()

        await ctx.send(content=message)

    else:
        await ctx.send(content="❌ **Invalid Transaction ID or unable to fetch data!**")

@siddhu.command(
    aliases=["cloneemoji", "copyemoji", "steal"],
    description="Clones an emoji from another server."
)
async def addemoji(ctx, emoji: discord.PartialEmoji, *, name=None):
    """Clones an emoji from another server and adds it to the current server."""
    
    await ctx.send(content="Adding emoji...")

    if name is None:
        name = emoji.name
    else:
        name = name.replace(" ", "_")

    try:
        # Download the emoji image from Discord's CDN
        response = requests.get(emoji.url)
        if response.status_code != 200:
            await ctx.send(content=":x: | Failed to download emoji.")
            return
        
        # Create the emoji in the current server
        new_emoji = await ctx.guild.create_custom_emoji(name=name, image=response.content)

        await ctx.send(content=f":white_check_mark: | Added emoji successfully: {new_emoji}")

    except discord.HTTPException as e:
        await ctx.send(content=f":x: | Failed to add emoji. Error: {e}")

@siddhu.command(name="alt_sniper_status")
async def alt_sniper_status(ctx):
    """Announce sniper status for alt accounts."""

    # Load config.json dynamically
    with open("config.json", "r") as f:
        config = json.load(f)
    alt_list = config.get("alt_list", [])
    token = config.get("token", None)

    async def get_username(token):
        """Fetch the username of a Discord account using its token."""
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return f"{data['username']}#{data['discriminator']}"
        else:
            return None

    if not alt_list and not token:
        await ctx.send("⚠️ No tokens provided in `alt_list` or `token`. Check your `config.json`.")
        return

    valid_usernames = []
    invalid_tokens = []

    # Check the main token
    main_username = await get_username(token)
    if main_username:
        valid_usernames.append(main_username)
    else:
        invalid_tokens.append("Main Token")

    # Check the alt tokens
    for alt_token in alt_list:
        username = await get_username(alt_token)
        if username:
            valid_usernames.append(username)
        else:
            invalid_tokens.append(alt_token[:10] + "...")  # Partial token for debugging

    # Prepare the response message
    if valid_usernames:
        valid_message = (
            f"<:lr_tick_1:1290693800808677461> Sniper enabled in the following accounts: {', '.join(valid_usernames)}"
        )
    else:
        valid_message = "<:CROSS_TDG:1321149916201881683> No valid accounts found in `alt_list` or `token`."

    if invalid_tokens:
        invalid_message = (
            f"⚠️ Failed to fetch usernames for the following tokens: {', '.join(invalid_tokens)}"
        )
    else:
        invalid_message = ""

    # Send confirmation message in the same channel
    await ctx.send(f"{valid_message}\n{invalid_message}")

PING_SPOOF_FILE = "ping_spoof.json"

# Ensure the file exists
if not os.path.exists(PING_SPOOF_FILE):
    with open(PING_SPOOF_FILE, "w") as f:
        json.dump({"enabled": False, "webhook_url": None}, f)

@siddhu.command()
async def ping_spoof(ctx, action: str):
    """Enable or disable ping spoof functionality."""
    try:
        with open(PING_SPOOF_FILE, "r") as f:
            data = json.load(f)

        if action.lower() == "enable":
            data["enabled"] = True
            await ctx.send("Ping spoofing enabled.")
        elif action.lower() == "disable":
            data["enabled"] = False
            await ctx.send("Ping spoofing disabled.")
        else:
            await ctx.send("Invalid action! Use `.ping_spoof enable` or `.ping_spoof disable`.")
            return

        with open(PING_SPOOF_FILE, "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        await ctx.send(f"Error updating ping spoof setting: {e}")

@siddhu.command()
async def ping_webhook(ctx, url: str):
    """Set the webhook URL for ping notifications."""
    try:
        if not url.startswith("https://discord.com/api/webhooks/"):
            await ctx.send("Invalid webhook URL! Please provide a valid Discord webhook link.")
            return

        with open(PING_SPOOF_FILE, "r") as f:
            data = json.load(f)

        data["webhook_url"] = url

        with open(PING_SPOOF_FILE, "w") as f:
            json.dump(data, f, indent=4)

        await ctx.send("Ping webhook URL set successfully.")
    except Exception as e:
        await ctx.send(f"Error setting webhook URL: {e}")

# Command: Steal Sticker
@siddhu.command()
async def steal_sticker(ctx, url: str):
    """Add a sticker to the server."""
    try:
        guild = ctx.guild
        response = requests.get(url)
        if response.status_code == 200:
            sticker = await guild.create_sticker(file=discord.File(BytesIO(response.content), "sticker.png"), name="Sticker", description="Custom Sticker")
            await ctx.send(f"<:Tick:1290693799361777665> Added sticker: {sticker}")
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to download sticker.")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error: {str(e)}")

# Command: Ghost Ping
@siddhu.command()
async def ghost_ping(ctx, user: discord.Member):
    """Ping a user and delete the message instantly."""
    await ctx.send(user.mention, delete_after=0.5)

# Command: User Status
@siddhu.command()
async def userstatus(ctx, user: discord.Member = None):
    """Check a user's status."""
    user = user or ctx.author
    await ctx.send(f"🟢 **{user.name}'s Status:** {user.status}")

# Command: Pastebin
@siddhu.command()
async def pastebin(ctx, *, text):
    """Upload text to Pastebin."""
    url = "https://pastebin.com/api/api_post.php"
    api_key = "GZ6acF4XSpSN6A2jsqXIjOWyWynwVE-6"  # Replace with your Pastebin API key
    data = {"api_dev_key": api_key, "api_option": "paste", "api_paste_code": text}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        await ctx.send(f"📋 **Pastebin Link:** {response.text}")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Could not upload to Pastebin.")

# Command: QR Scan
@siddhu.command()
async def qrscan(ctx, *, url):
    """Scan a QR code from a URL."""
    response = requests.get(url)
    if response.status_code == 200:
        qr = qrcode.QRCode(response.text)
        buffer = BytesIO()
        qr.png(buffer, scale=5)
        buffer.seek(0)
        await ctx.send(file=discord.File(buffer, "qrcode.png"))
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Could not fetch the QR code.")

# Command: Block
import requests
import discord
import json

# Load token from config.json
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        TOKEN = config.get("token", "")
except (FileNotFoundError, json.JSONDecodeError):
    TOKEN = ""

HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

def block_user(user_id):
    """Blocks a user via Discord API."""
    url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
    response = requests.put(url, headers=HEADERS, json={"type": 2})
    
    if response.status_code == 204:
        return True, f"✅ Successfully blocked <@{user_id}>!"
    else:
        return False, f"❌ Failed to block <@{user_id}>: {response.text}"

def unblock_user(user_id):
    """Unblocks a user via Discord API."""
    url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
    response = requests.delete(url, headers=HEADERS)
    
    if response.status_code == 204:
        return True, f"✅ Successfully unblocked <@{user_id}>!"
    else:
        return False, f"❌ Failed to unblock <@{user_id}>: {response.text}"

async def get_user_from_input(ctx, user_input):
    """Gets user from @mention, ID, or Username."""
    try:
        # If input is a mention, extract ID
        if user_input.startswith("<@") and user_input.endswith(">"):
            user_id = user_input.strip("<@!>")
        elif user_input.isdigit():
            user_id = user_input  # User provided an ID
        else:
            # Try fetching by username
            user = discord.utils.get(ctx.bot.users, name=user_input)
            if user:
                user_id = str(user.id)
            else:
                return None, "❌ User not found!"
        return user_id, None
    except Exception as e:
        return None, f"❌ Error fetching user: {str(e)}"

@siddhu.command()
async def embedmode(ctx):
    global embed_mode_enabled
    global original_send

    await ctx.message.delete()

    # Load config to check webhook_url and embed_channel_id
    try:
        with open(CONFIG_PATH, "r") as f:
            config_data = json.load(f)
            webhook_url = config_data.get("webhook_url")
            embed_channel_id = config_data.get("embed_channel_id")
    except Exception:
        webhook_url = None
        embed_channel_id = None

    if not webhook_url or not embed_channel_id:
        await ctx.send("❌ Please set both `webhook_url` and `embed_channel_id` in `config.json` first.", delete_after=5)
        return

    # Toggle embed mode
    embed_mode_enabled = not embed_mode_enabled

    # Save embed_mode_enabled inline
    try:
        with open(CONFIG_PATH, "r") as f:
            config_data = json.load(f)
    except Exception:
        config_data = {}

    config_data["embed_mode_enabled"] = embed_mode_enabled

    with open(CONFIG_PATH, "w") as f:
        json.dump(config_data, f, indent=4)

    # Override or restore Context.send accordingly
    if embed_mode_enabled:
        Context.send = send_embed_hook  # your custom send function
    else:
        Context.send = original_send

    state = "ENABLED ✅" if embed_mode_enabled else "DISABLED ❌"
    await ctx.send(f"🟢 Embed mode is now **{state}**", delete_after=5)

@siddhu.command()
async def embed_colour(ctx, hex_code: str):
    global embed_color
    await ctx.message.delete()

    if not hex_code.startswith("#"):
        hex_code = f"#{hex_code}"

    try:
        embed_color = int(hex_code.replace("#", ""), 16)
        config["embed_color"] = hex_code
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)
        await ctx.send(f"🎨 Embed color updated to `{hex_code}`", delete_after=4)
    except ValueError:
        await ctx.send("❌ Invalid hex code. Example: `.embed_colour ff66cc`", delete_after=4)

import aiohttp

async def send_embed_hook(ctx, content=None, **kwargs):
    global embed_mode_enabled, embed_color

    if not embed_mode_enabled or not content:
        return await original_send(ctx, content=content, **kwargs)

    avatar_url = str(ctx.author.avatar_url) if ctx.author.avatar_url else None

    embed_payload = {
        "embeds": [{
            "description": content,
            "footer": {
                "text": f"{ctx.author.name} - SyntheX Prime V5",
                "icon_url": avatar_url
            },
            "color": embed_color
        }],
        "username": str(ctx.author),
        "avatar_url": avatar_url
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{webhook_url}?wait=true", json=embed_payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                webhook_msg_id = int(data["id"])

                forward_payload = {
                    "message_reference": {
                        "message_id": webhook_msg_id,
                        "channel_id": embed_channel_id,
                        "type": 1
                    }
                }

                headers = {
                    "Authorization": token,
                    "User-Agent": "Mozilla/5.0"
                }

                forward_url = f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                await session.post(forward_url, headers=headers, json=forward_payload)

                delete_url = f"https://discord.com/api/v10/channels/{embed_channel_id}/messages/{webhook_msg_id}"
                await session.delete(delete_url, headers=headers)
            else:
                print(f"[Embed Error] Webhook send failed: {await resp.text()}")

async def send_custom_embed(
    ctx,
    *,
    title=None,
    description=None,
    color=None,
    fields=None,
    footer_text=None,
    footer_icon=None,
    thumbnail=None,
    image=None,
    timestamp=False,
    extra_replies=None  # New parameter: list of plain text replies
):
    avatar_url = str(ctx.author.avatar_url)
    color = color or embed_color  # fallback to global color

    embed = {
        "color": color
    }

    if title:
        embed["title"] = title
    if description:
        embed["description"] = description
    if fields:
        embed["fields"] = fields
    if thumbnail:
        embed["thumbnail"] = {"url": thumbnail}
    if image:
        embed["image"] = {"url": image}
    if timestamp:
        from datetime import datetime
        embed["timestamp"] = datetime.utcnow().isoformat()

    embed["footer"] = {
        "text": footer_text or f"{ctx.author.name} - SyntheX Prime V5",
        "icon_url": footer_icon or avatar_url
    }

    payload = {
        "embeds": [embed],
        "username": ctx.author.name,
        "avatar_url": avatar_url
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{webhook_url}?wait=true", json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                msg_id = int(data["id"])

                forward_payload = {
                    "message_reference": {
                        "message_id": msg_id,
                        "channel_id": embed_channel_id,
                        "type": 1
                    }
                }

                headers = {
                    "Authorization": token,
                    "User-Agent": "Mozilla/5.0"
                }

                forward_url = f"https://discord.com/api/v10/channels/{ctx.channel.id}/messages"
                await session.post(forward_url, headers=headers, json=forward_payload)

                # Delete original embed message from embed channel
                delete_url = f"https://discord.com/api/v10/channels/{embed_channel_id}/messages/{msg_id}"
                await session.delete(delete_url, headers=headers)
            else:
                print(f"[Embed] Failed: {await resp.text()}")

    # Send extra non-embed messages via ctx.reply
    if extra_replies:
        for msg in extra_replies:
            if msg:
                await ctx.reply(msg, mention_author=False)

from discord.ext.commands import Context

original_send = Context.send

with open("config.json", "r") as f:
    config = json.load(f)

embed_mode_enabled = config.get("embed_mode_enabled", False)

if embed_mode_enabled:
    Context.send = send_embed_hook

@siddhu.command()
async def block(ctx, user_input: str = None):
    """Blocks a user via @mention, User ID, or Username."""
    if user_input is None:
        await ctx.send("❌ Please provide a user (@mention, ID, or username).")
        return

    user_id, error = await get_user_from_input(ctx, user_input)
    if error:
        await ctx.send(error)
        return

    success, message = block_user(user_id)
    await ctx.send(message)

@siddhu.command()
async def unblock(ctx, user_input: str = None):
    """Unblocks a user via @mention, User ID, or Username."""
    if user_input is None:
        await ctx.send("❌ Please provide a user (@mention, ID, or username).")
        return

    user_id, error = await get_user_from_input(ctx, user_input)
    if error:
        await ctx.send(error)
        return

    success, message = unblock_user(user_id)
    await ctx.send(message)

# Command: Blocklist
@siddhu.command()
async def blocklist(ctx):
    """Shows a list of blocked users."""
    await ctx.message.delete()
    
    # Load the token from config.json
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        token = config.get('token')
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("<:CROSS_TDG:1321149916201881683> Error: Unable to load the token from config.json.")
    
    headers = {"Authorization": token}
    url = "https://discord.com/api/v9/users/@me/relationships"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            relationships = response.json()
            blocked_users = [r for r in relationships if r['type'] == 2]  # Type 2 = Blocked
            
            if not blocked_users:
                return await ctx.send("<:CROSS_TDG:1321149916201881683> You have no blocked users.")

            # Create the list display
            blocked_list = "\n".join(
                [f"**{i+1}.** `{user['user']['username']}#{user['user']['discriminator']}` (ID: `{user['id']}`)" 
                 for i, user in enumerate(blocked_users)]
            )

            await ctx.send(f"**<:Block:1336670517486161951> Blocked Users:**\n{blocked_list}")
        else:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to fetch blocked users: {response.status_code}")
    
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: `{str(e)}`")

# Command: Binary Conversion
@siddhu.command()
async def binary(ctx, *, text):
    """Convert text to binary."""
    binary_text = " ".join(format(ord(char), "08b") for char in text)
    await ctx.send(f"💾 **Binary:** `{binary_text}`")

# Command: Unbinary Conversion
@siddhu.command()
async def unbinary(ctx, *, binary_text):
    """Convert binary to text."""
    try:
        text = "".join(chr(int(binary, 2)) for binary in binary_text.split())
        await ctx.send(f"🔄 **Text:** `{text}`")
    except ValueError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid binary input.")

# Command: Wiki Search
@siddhu.command()
async def wiki(ctx, *, query):
    """Search Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        await ctx.send(f"📖 **Wikipedia Summary:**\n{summary}")
    except wikipedia.DisambiguationError as e:
        await ctx.send(f"🔍 **Disambiguation Error:**\n{e}")
    except wikipedia.PageError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Page not found.")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: {str(e)}")

from dateutil import parser

@siddhu.command()
async def timestamp(ctx, *, datetime_str: str = None):
    """Generate a UNIX timestamp for the given date and time or current timestamp."""
    try:
        if datetime_str:
            dt = parser.parse(datetime_str, dayfirst=True)
            timestamp = int(dt.timestamp())
        else:
            timestamp = int(time.time())

        response = f"<t:{timestamp}:d> <t:{timestamp}:R>"
        await ctx.send(response)

    except Exception as e:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid date format! Use `DD/MM/YYYY HH:MM`.")
        print(f"Timestamp error: {e}")
    
@siddhu.command()
async def credentials_info(ctx):
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    credentials_info = f"""
    <:rules:1290926829762383934> **__User Credentials Info__ :-**
- USER ID: `{ctx.author.name}`
- TOKEN: `{config_data['token']}`
- SERVER LINK: `{config_data['SERVER_Link']}`
- UPI ID: `{config_data['Upi']}`
- UPI ID 2: `{config_data['Upi2']}`
- LICENSE KEY: `{config_data['license_key']}`
- PASSWORD: `{config_data['password']}`
<:Titanz:1281243491476967447> **DON'T SHARE THESE INFO WITH ANYONE**
    """

    message = await ctx.send(credentials_info)
    await asyncio.sleep(60)  # wait for 1 minute
    await message.delete() 

import json
from discord.ext import commands

@siddhu.command()
async def nwebhook(ctx, link: str):
    """Set the webhook for Nitro Sniper."""
    if not link.startswith("https://discord.com/api/webhooks/"):
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid webhook URL. Please provide a valid Discord webhook.")
        return

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    config["nitro_webhook"] = link

    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

    await ctx.send("<:lr_tick_1:1290693800808677461> Nitro Sniper webhook set successfully.")


@siddhu.command()
async def gwebhook(ctx, link: str):
    """Set the webhook for Giveaway Sniper."""
    if not link.startswith("https://discord.com/api/webhooks/"):
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid webhook URL. Please provide a valid Discord webhook.")
        return

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    config["giveaway_webhook"] = link

    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

    await ctx.send("<:lr_tick_1:1290693800808677461> Giveaway Sniper webhook set successfully.")


@siddhu.command()
async def pwebhook(ctx, link: str):
    """Set the webhook for Privnote Sniper."""
    if not link.startswith("https://discord.com/api/webhooks/"):
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid webhook URL. Please provide a valid Discord webhook.")
        return

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    config["privnote_webhook"] = link

    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

    await ctx.send("<:lr_tick_1:1290693800808677461> Privnote Sniper webhook set successfully.")

@siddhu.command()
async def nitro_sniper(ctx, toggle: str):
    """Enable or disable the Nitro Sniper."""
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    alt_list = config.get("alt_list", [])  # Get alt tokens
    alt_usernames = []

    # Fetch usernames of the alt accounts
    for token in alt_list:
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            alt_usernames.append(f"{user_data['username']}#{user_data['discriminator']}")
        else:
            alt_usernames.append("Unknown User (Invalid Token)")

    if toggle.lower() == "enable":
        config["nitro_sniper"] = True
        alt_usernames_str = ", ".join(alt_usernames) if alt_usernames else "No alts configured."
        await ctx.send(
            f"**<:lr_tick_1:1290693800808677461> Nitro Sniper enabled successfully\nAlt list:** {alt_usernames_str}"
        )
    elif toggle.lower() == "disable":
        config["nitro_sniper"] = False
        await ctx.send("<:CROSS_TDG:1321149916201881683> Nitro Sniper disabled.")
    else:
        await ctx.send("❓ Use `.nitro_sniper enable` or `.nitro_sniper disable`.")

    # Save changes to config
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

@siddhu.command()
async def giveaway_sniper(ctx, toggle: str):
    """Enable or disable the Giveaway Sniper."""
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    if toggle.lower() == "enable":
        config["giveaway_sniper"] = True
        await ctx.send("<:lr_tick_1:1290693800808677461> Giveaway Sniper enabled.")
    elif toggle.lower() == "disable":
        config["giveaway_sniper"] = False
        await ctx.send("<:CROSS_TDG:1321149916201881683> Giveaway Sniper disabled.")
    else:
        await ctx.send("❓ Use `.giveaway_sniper enable` or `.giveaway_sniper disable`.")

    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)


@siddhu.command()
async def privnote_sniper(ctx, toggle: str):
    """Enable or disable the Privnote Sniper."""
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    if toggle.lower() == "enable":
        config["privnote_sniper"] = True
        await ctx.send("<:lr_tick_1:1290693800808677461> Privnote Sniper enabled.")
    elif toggle.lower() == "disable":
        config["privnote_sniper"] = False
        await ctx.send("<:CROSS_TDG:1321149916201881683> Privnote Sniper disabled.")
    else:
        await ctx.send("❓ Use `.privnote_sniper enable` or `.privnote_sniper disable`.")

    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

@siddhu.command()
async def vanity_check(ctx, url: str):
    """Checks if a vanity URL is available and gives server info if it exists."""
    # Sanitize input: We only need the code part of the vanity URL.
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f"https://discord.com/api/v10/invites/{url}") as response:
                if response.status == 200:
                    data = await response.json()
                    server_info = data.get('guild', {})

                    # Check if server info exists
                    if server_info:
                        server_name = server_info.get('name', 'Unknown Server')
                        server_id = server_info.get('id', 'Unknown ID')
                        owner_id = server_info.get('owner_id', 'Unknown Owner')
                        server_region = server_info.get('region', 'Unknown Region')
                        icon_url = server_info.get('icon', 'No Icon')
                        if icon_url:
                            icon_url = f"https://cdn.discordapp.com/icons/{server_id}/{icon_url}.png"
                        else:
                            icon_url = "No Icon"

                        await ctx.send(f"Vanity URL: discord.gg/{url} exists!\n"
                                       f"Server Name: {server_name}\n"
                                       f"Server ID: {server_id}\n"
                                       f"Owner ID: {owner_id}\n"
                                       f"Server Region: {server_region}\n"
                                       f"Server Icon: {icon_url}")
                    else:
                        # If no server info is returned, it means the vanity URL is available
                        await ctx.send(f"Vanity URL: discord.gg/{url} is available!")
                else:
                    # If the response status is not 200, the vanity URL is likely not valid or available
                    await ctx.send(f"Vanity URL discord.gg/{url} does not exist.")
        except Exception as e:
            await ctx.send(f"Error checking vanity URL: {e}")

@siddhu.command()
async def close(ctx):
    """Safely close the selfbot."""
    await ctx.send("Shutting down the bot... Goodbye!", delete_after=3)
    await siddhu.close()

# File to store aliases persistently
ALIASES_FILE = "aliases.json"

# Load aliases from the file or initialize an empty dictionary
try:
    with open(ALIASES_FILE, "r") as f:
        command_aliases = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    command_aliases = {}

# Save aliases to the file
def save_aliases():
    with open(ALIASES_FILE, "w") as f:
        json.dump(command_aliases, f, indent=4)

@siddhu.command()
async def edit_cmd(ctx, cmd_name: str, new_alias: str):
    """Edit the alias of a command and make it persistent."""
    if cmd_name not in siddhu.all_commands:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Command `{cmd_name}` does not exist.")
        return

    # Add the new alias to the dictionary
    command_aliases[new_alias] = cmd_name
    save_aliases()
    await ctx.send(f"<:Tick:1290693799361777665> Alias for `{cmd_name}` has been changed to `{new_alias}`.")

@siddhu.command()
async def remove_alias(ctx, alias: str):
    """Remove an alias."""
    if alias not in command_aliases:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Alias `{alias}` does not exist.")
        return

    del command_aliases[alias]
    save_aliases()
    await ctx.send(f"<:Tick:1290693799361777665> Alias `{alias}` has been removed.")

@siddhu.command()
async def reset_cmd(ctx):
    """Reset all aliases and command data."""
    global command_aliases
    command_aliases.clear()  # Clear all aliases
    save_aliases()  # Save the cleared state
    await ctx.send("<:Tick:1290693799361777665> All aliases have been reset to default!")
    
@siddhu.command()
async def wallet_info(ctx):
    with open('wallet.json', 'r') as f:
        wallet_data = json.load(f)

    wallet_info = f"""
    <:rules:1290926829762383934> **__Wallet Info__ :-**
- Wallet 1 Address: `{wallet_data['1']['address']}`
- Wallet 1 Private Key: `{wallet_data['1']['private_key']}`

- Wallet 2 Address: `{wallet_data['2']['address']}`
- Wallet 2 Private Key: `{wallet_data['2']['private_key']}`

- Wallet 3 Address: `{wallet_data['3']['address']}`
- Wallet 3 Private Key: `{wallet_data['3']['private_key']}`
<:Titanz:1281243491476967447> **DON'T SHARE THESE INFO WITH ANYONE**
    """

    message = await ctx.send(wallet_info)
    await asyncio.sleep(60)  # wait for 1 minute
    await message.delete()
    
@siddhu.command()
async def set_upi(ctx, upi: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['Upi'] = upi
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> UPI updated to {upi}")
    
@siddhu.command()
async def set_upi2(ctx, upi2: str):
    """Set a new UPI2 ID in config.json"""
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['Upi2'] = upi2  # Update Upi2
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    
    await ctx.send(f"<:Tick:1290693799361777665> **UPI2 updated to {upi2}**")    
    
# 1. Code Formatter
@siddhu.command()
async def formatcode(ctx, *, code: str):
    """Format a code snippet into a block for readability."""
    formatted = f"```{code}```"
    await ctx.send(formatted)

async def find_message_by_id(bot, message_id):
    for channel in bot.private_channels + [c for g in bot.guilds for c in g.text_channels]:
        try:
            msg = await channel.fetch_message(int(message_id))
            return msg  # Found it
        except:
            continue
    return None  # Not found

@siddhu.command()
async def af(ctx, *, args):
    await ctx.message.delete()

    # Split and strip arguments
    parts = [p.strip() for p in args.split(",")]

    if len(parts) < 2:
        await ctx.send("❌ Invalid format.\nUse: `.af <trigger>, <message_id> [channel_id]`", delete_after=6)
        return

    trigger = parts[0].lower()

    # Validate and clean message ID
    try:
        message_id = int(parts[1].strip().replace("`", "").replace("<", "").replace(">", ""))
    except ValueError:
        await ctx.send("❌ Message ID must be a number.", delete_after=6)
        return

    # Optional channel ID
    try:
        channel_id = int(parts[2].strip()) if len(parts) >= 3 else ctx.channel.id
    except ValueError:
        await ctx.send("❌ Channel ID must be a number.", delete_after=6)
        return

    target_channel = siddhu.get_channel(channel_id)
    if not target_channel:
        await ctx.send("❌ Couldn't find the specified channel.", delete_after=6)
        return

    try:
        msg = await target_channel.fetch_message(message_id)
    except:
        await ctx.send("❌ Couldn't find the message in the specified channel.", delete_after=6)
        return

    af_triggers[trigger] = {
        "message_id": str(msg.id),
        "channel_id": str(target_channel.id)
    }

    with open("af.json", "w") as f:
        json.dump(af_triggers, f, indent=2)

    await ctx.send(f"✅ Trigger `{trigger}` set to forward message `{msg.id}` from <#{target_channel.id}>", delete_after=5)

@siddhu.command()
async def afrem(ctx, trigger: str):
    trigger = trigger.lower()
    if trigger in af_triggers:
        del af_triggers[trigger]
        with open(af_file, "w") as f:
            json.dump(af_triggers, f, indent=2)
        await ctx.send(f"🗑️ Removed trigger `{trigger}`", delete_after=3)
    else:
        await ctx.send("❌ Trigger not found", delete_after=3)
    await ctx.message.delete()

@siddhu.command()
async def afreset(ctx):
    af_triggers.clear()
    with open(af_file, "w") as f:
        json.dump(af_triggers, f, indent=2)
    await ctx.message.delete()
    await ctx.send("🔁 All auto-forward triggers cleared", delete_after=3)

@siddhu.command()
async def aflist(ctx):
    await ctx.message.delete()

    if not af_triggers:
        await ctx.send("📭 No auto-forward triggers set.", delete_after=5)
        return

    lines = [
        f"🔹 `{trigger}` → msg_id: `{data['message_id']}` in channel: `{data['channel_id']}`"
        for trigger, data in af_triggers.items()
    ]
    content = "\n".join(lines)

    if embed_mode_enabled:
        await send_custom_embed(
            ctx,
            title="📌 Auto-Forward Triggers",
            description=content,
            footer_text="Developed by siddhu.og",
            footer_icon="https://cdn.discordapp.com/avatars/1241519716644819014/2f75df45d57c600a49370caab69cd051.webp?size=1024",
            image="https://cdn.discordapp.com/attachments/1255090765726748694/1377325399419260980/5.jpg",
            timestamp=True
        )
    else:
        await ctx.send(f"📌 Auto-Forward Triggers:\n{content}")

# 2. Hash Generator
@siddhu.command()
async def hash(ctx, algorithm: str, *, text: str):
    """Generate a hash using the specified algorithm (e.g., md5, sha256)."""
    try:
        h = hashlib.new(algorithm)
        h.update(text.encode())
        await ctx.send(f"{algorithm.upper()} hash: `{h.hexdigest()}`")
    except ValueError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Unsupported hash algorithm! Use `md5`, `sha1`, `sha256`, etc.")

# 3. IP Geolocation
@siddhu.command()
async def geoip(ctx, ip: str):
    """Get geolocation info for an IP address."""
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"🌍 IP: `{ip}`\nCity: `{data.get('city')}`\nCountry: `{data.get('country_name')}`\nRegion: `{data.get('region')}`")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to fetch geolocation data.")

# 4. RGB to Hex Converter
@siddhu.command()
async def rgbtohex(ctx, r: int, g: int, b: int):
    """Convert RGB values to a hex color code."""
    try:
        hex_code = f"#{r:02x}{g:02x}{b:02x}".upper()
        await ctx.send(f"🎨 Hex Code: `{hex_code}`")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error: {e}")

# 5. QR Code Generator
from io import BytesIO
import qrcode
import discord

@siddhu.command()
async def qrcode(ctx, *, text: str):
    """Generate a QR code from text."""
    buffer = BytesIO()
    qr = qrcode.make(text)
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    if not embed_mode_enabled:
        # Normal mode, just send file
        await ctx.send(file=discord.File(fp=buffer, filename="qrcode.png"))
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) QR CODE SENT <::Tick:1290693799361777665>")
    else:
        # Embed mode: upload image to embed channel, get URL, then send embed with image
        async with aiohttp.ClientSession() as session:
            try:
                image_url = await upload_file_and_get_url(session, discord.File(fp=buffer, filename="qrcode.png"))
            except Exception as e:
                await ctx.send(f"Failed to upload QR code image: {str(e)}")
                return
        
        await send_custom_embed(
            ctx,
            title="Generated QR Code",
            description=f"QR Code for:\n```{text}```",
            image=image_url
        )
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) QR CODE SENT IN EMBED <::Tick:1290693799361777665>")

# 6. Random Password Generator
@siddhu.command()
async def genpass(ctx, length: int = 12):
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    await ctx.send(f"🔐 Generated Password: `{password}`")

# 7. HTML Encoder
@siddhu.command()
async def htmlencode(ctx, *, text: str):
    """Encode special characters in HTML."""
    encoded = html.escape(text)
    await ctx.send(f"🔐 Encoded: `{encoded}`")

# 8. HTML Decoder
@siddhu.command()
async def htmldecode(ctx, *, text: str):
    """Decode HTML-encoded text."""
    decoded = html.unescape(text)
    await ctx.send(f"🔓 Decoded: `{decoded}`")

# 9. Temp Mail Checker
@siddhu.command()
async def checkemail(ctx, email: str):
    """Check if an email address is temporary."""
    response = requests.get(f"https://api.mailcheck.ai/domain/{email.split('@')[-1]}")
    if response.status_code == 200:
        data = response.json()
        if data.get("disposable"):
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> `{email}` is a temporary email!")
        else:
            await ctx.send(f"<:Tick:1290693799361777665> `{email}` is a valid email!")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to check the email.")

# 10. Text Reverser
@siddhu.command()
async def reverse(ctx, *, text: str):
    """Reverse the input text."""
    await ctx.send(f"🔄 Reversed: `{text[::-1]}`")

# 1. Truth Command
@siddhu.command()
async def truth(ctx):
    truths = [
        "What is your most embarrassing moment?",
        "Have you ever lied to your best friend?",
        "What's your biggest fear?",
        "What's a secret you've never told anyone?"
    ]
    await ctx.send(f"🤔 Truth: {random.choice(truths)}")

@siddhu.command()
async def allcmdz(ctx):
    """Send all help command messages one by one with rate limit handling."""
    import json
    import asyncio

    try:
        # Load prefix from config.json
        with open("config.json", "r") as file:
            config = json.load(file)
            prefix = config.get("prefix", ".")

        # First send main help command
        await ctx.send(f"{prefix}help")
        await asyncio.sleep(1.8)

        # List of module commands (all prefixed with h)
        modules = [
            "main", "user", "activity", "admin", "utility", "extra",
            "fun", "wizz", "mod", "msg", "sniper", "dev",
            "seller", "antinuke", "wallet", "nsfw", "misc",
            "vc", "spy", "premium", "crypto", "stock", "boost", "vanity", "info"
        ]

        for module in modules:
            await ctx.send(f"{prefix}h {module}")
            await asyncio.sleep(2)  # avoid rate limit

    except FileNotFoundError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Config file not found! Make sure `config.json` exists.")
    except json.JSONDecodeError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to parse config.json! Check for formatting errors.")
        
# 2. Dare Command
@siddhu.command()
async def dare(ctx):
    dares = [
        "Send a funny selfie to the group.",
        "Talk in an accent for 5 minutes.",
        "Do 10 push-ups now.",
        "Call your crush and confess your love."
    ]
    await ctx.send(f"💪 Dare: {random.choice(dares)}")

# 3. Ship Command
@siddhu.command()
async def ship(ctx, name1: str, name2: str):
    compatibility = random.randint(0, 100)
    await ctx.send(f"💞 {name1} and {name2} are {compatibility}% compatible!")

# 4. Magic Number Command
@siddhu.command()
async def magicnumber(ctx):
    number = random.randint(1, 100)
    await ctx.send(f"🔮 Your magic number is {number}!")

import os
import aiohttp
import zipfile

import aiohttp
import os
import zipfile
import discord

@siddhu.command()
async def downloadguildemoji(ctx, guild_id: int):
    await ctx.send("`⏳ Downloading emojis...`")

    headers = {"Authorization": token, "Content-Type": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/emojis", headers=headers) as response:
            if response.status != 200:
                return await ctx.send("`❌ Failed to fetch emojis.`")

            emojis = await response.json()
            if not emojis:
                return await ctx.send("`❌ No emojis found in this server.`")

            os.makedirs("emojis", exist_ok=True)  # Ensure folder exists
            file_paths = []

            for emoji in emojis:
                emoji_ext = "gif" if emoji["animated"] else "png"
                emoji_url = f"https://cdn.discordapp.com/emojis/{emoji['id']}.{emoji_ext}"
                file_path = f"emojis/{emoji['name']}.{emoji_ext}"

                # Ensure the file name is valid (remove problematic characters)
                file_path = file_path.replace("/", "").replace("\\", "").replace(":", "").replace("*", "").replace("?", "").replace('"', "").replace("<", "").replace(">", "").replace("|", "")

                async with session.get(emoji_url) as img_response:
                    if img_response.status == 200:
                        with open(file_path, "wb") as f:
                            f.write(await img_response.read())
                        file_paths.append(file_path)
                    else:
                        print(f"❌ Failed to download: {emoji_url}")

            if not file_paths:
                return await ctx.send("`❌ Failed to download any emojis.`")

            if len(file_paths) == 1:
                if os.path.exists(file_paths[0]):  # Ensure file exists before sending
                    await ctx.send("`✅ Emoji Downloaded:`", file=discord.File(file_paths[0]))
                    os.remove(file_paths[0])
            else:
                zip_path = "emojis.zip"
                with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                    for file in file_paths:
                        if os.path.exists(file):  # Ensure file exists before adding to ZIP
                            zipf.write(file)
                            os.remove(file)
                
                if os.path.exists(zip_path):  # Ensure ZIP exists before sending
                    await ctx.send("`✅ Emojis Downloaded:`", file=discord.File(zip_path))
                    os.remove(zip_path)

            # Check if "emojis" folder is empty before deleting
            if os.path.exists("emojis") and not os.listdir("emojis"):
                os.rmdir("emojis")

# Add a bot status
import requests
import json

@siddhu.command(aliases=["set_status"])
async def setstatus(ctx, emoji: str, *, status_msg: str):
    token = json.load(open("config.json"))["token"]  # Fetch token from config.json

    # Parse emoji
    emoji_id = None
    emoji_name = None

    if emoji.startswith('<:') and emoji.endswith('>'):  # Custom static emoji
        emoji_name, emoji_id = emoji[2:-1].split(':')
        emoji_id = int(emoji_id)
    elif emoji.startswith('<a:') and emoji.endswith('>'):  # Custom animated emoji
        emoji_name, emoji_id = emoji[3:-1].split(':')
        emoji_id = int(emoji_id)

    # Payload for custom status
    payload = {
        "custom_status": {
            "text": status_msg,
            "emoji_name": emoji_name if emoji_id else None,
            "emoji_id": emoji_id
        }
    }

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    # Send request to Discord API
    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

    # Send result
    if response.status_code == 200:
        await ctx.send("✅ Status updated successfully!")
    else:
        await ctx.send(f"❌ Failed to update status: `{response.text}`")

# Display the bot's current song URL
@siddhu.command()
async def songurl(ctx):
    """Display the URL of the currently playing song."""
    if ctx.voice_client and ctx.voice_client.is_playing():
        await ctx.send(f"Current song URL: {ctx.voice_client.source.url}")
    else:
        await ctx.send("No music is currently playing.")

@siddhu.command()
async def stop_areact(ctx):
    """Stop auto-reactions."""
    global auto_react_emojis
    auto_react_emojis = []  # Clear the list of emojis
    await ctx.send("<:CROSS_TDG:1321149916201881683> Auto-react has been disabled.")
    
import json
import requests

@siddhu.command()
async def mybal(ctx, wallet_num):
    """Check balance for a specific wallet."""
    try:
        with open("wallet.json", "r") as f:
            wallets = json.load(f)

        if wallet_num in wallets:
            wallet_info = wallets[wallet_num]
            addy = wallet_info.get("address")
        else:
            await ctx.send("`Wallet Not Found`")
            return

        # Fetch address details
        address_data = get_address_details(addy)  # Replace with your function to fetch wallet data

        # Extract balances
        confirmed_balance_ltc = address_data['final_balance'] / 1e8
        unconfirmed_balance_ltc = address_data['unconfirmed_balance'] / 1e8
        total_received_ltc = address_data['total_received'] / 1e8

        # Get Litecoin price in USD
        coingecko_resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        coingecko_resp.raise_for_status()
        ltc_to_usd_rate = coingecko_resp.json()['litecoin']['usd']

        # Convert balances to USD
        confirmed_balance_usd = confirmed_balance_ltc * ltc_to_usd_rate
        unconfirmed_balance_usd = unconfirmed_balance_ltc * ltc_to_usd_rate
        total_received_usd = total_received_ltc * ltc_to_usd_rate

        # Format the response
        response = (
            f"# <a:tz_ltc:1281238097136451616> __LTC BALANCE__ <a:tz_ltc:1281238097136451616>\n"
            f"> <:rdx_glowin_heart:1288196137848803451> **Balance For:** `WALLET {wallet_num}`\n"
            f"> <:LTC:1322611807269031968> **Total Balance:** `${confirmed_balance_usd:.2f} USD`\n"
            f"> <a:bitzxier_downtime:1322611844455727165> **Unconfirmed Balance:** `${unconfirmed_balance_usd:.2f} USD`\n"
            f"> <:crypto:1322611842316501073> **Total Received:** `${total_received_usd:.2f} USD`\n"
        )

        await ctx.send(response)
        print("[+] My Balance Command Used")  # Logging for debugging
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")   
    
# 5. Guess Game Command
@siddhu.command()
async def guessgame(ctx):
    number = random.randint(1, 10)
    await ctx.send("🤔 Guess a number between 1 and 10!")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        guess = await siddhu.wait_for('message', check=check, timeout=15)
        if int(guess.content) == number:
            await ctx.send(f"🎉 Correct! The number was {number}.")
        else:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> Wrong! The number was {number}.")
    except:
        await ctx.send("⌛ You took too long!")

# Edit a Message
@siddhu.command()
async def edit(ctx, message_id: int, *, new_content: str):
    """Edit a specific message by ID."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.edit(content=new_content)
        await ctx.send("<:Tick:1290693799361777665> Message edited successfully.")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I do not have permission to edit this message.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to edit the message.")

# Delete a Message
@siddhu.command()
async def delete(ctx, message_id: int):
    """Delete a specific message by ID."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.delete()
        await ctx.send("<:Tick:1290693799361777665> Message deleted successfully.", delete_after=5)
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I do not have permission to delete this message.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to delete the message.")

# Quote a Message
@siddhu.command()
async def quote(ctx, message_id: int):
    """Quote a message by ID."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await ctx.send(f"💬 **{message.author} said:**\n> {message.content}")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to fetch the message.")

import aiohttp
import discord
from discord.ext import commands

NSFW_API = "https://nekobot.xyz/api/image"

# Helper function to fetch NSFW images
async def fetch_nsfw_image(category):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{NSFW_API}?type={category}") as resp:
            if resp.status == 200:
                data = await resp.json()
                return data.get("message")
            return None

# Helper function to fetch Pornhub search results with better error handling
async def search_pornhub(query):
    search_url = f"https://www.pornhub.com/webmasters/search?query={query}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(search_url) as resp:
                if resp.status == 200:
                    content = await resp.text()
                    
                    # Parse the HTML response with BeautifulSoup
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Find the video links by parsing the HTML structure
                    video_links = []
                    videos = soup.find_all('a', {'class': 'videoWrapper'})

                    # Check if we found any video links
                    if not videos:
                        return "<:CROSS_TDG:1321149916201881683> No results found."

                    # Extract the top 5 video links
                    for video in videos[:5]:
                        link = video.get('href')
                        if link:
                            video_links.append(f"https://www.pornhub.com{link}")

                    if video_links:
                        return video_links
                    else:
                        return "<:CROSS_TDG:1321149916201881683> No video links found in the response."
                else:
                    return "<:CROSS_TDG:1321149916201881683> Failed to fetch the search results."
        except Exception as e:
            return f"<:CROSS_TDG:1321149916201881683> Error occurred: {str(e)}"

# Updated pornsearch command to use the new search functionality
@siddhu.command()
async def pornsearch(ctx, *, query: str):
    """Search for porn videos on Pornhub."""
    results = await search_pornhub(query)
    
    if isinstance(results, list):  # If we have a list of video links
        response = "Top 5 results from Pornhub:\n"
        for idx, link in enumerate(results, 1):
            response += f"{idx}. {link}\n"
        await ctx.send(response)
    else:  # If we have an error message
        await ctx.send(results)

async def send_nsfw_image(ctx, category: str):
    url = await fetch_nsfw_image(category)
    if url:
        if embed_mode_enabled:
            await send_custom_embed(ctx, image=url)
        else:
            await ctx.send(url)
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Could not fetch the image.")

@siddhu.command()
async def anal(ctx):
    """Get an anal NSFW image."""
    await send_nsfw_image(ctx, "anal")

@siddhu.command()
async def hanal(ctx):
    """Get a hentai anal NSFW image."""
    await send_nsfw_image(ctx, "hanal")

@siddhu.command()
async def ass(ctx):
    """Get an ass NSFW image."""
    await send_nsfw_image(ctx, "ass")

@siddhu.command()
async def boobs(ctx):
    """Get a boobs NSFW image."""
    await send_nsfw_image(ctx, "boobs")

@siddhu.command()
async def pussy(ctx):
    """Get a pussy NSFW image."""
    await send_nsfw_image(ctx, "pussy")

@siddhu.command()
async def _4k(ctx):
    """Get a 4K NSFW image."""
    await send_nsfw_image(ctx, "4k")

@siddhu.command()
async def pgif(ctx):
    """Get a NSFW GIF."""
    await send_nsfw_image(ctx, "pgif")

@siddhu.command()
async def pic(ctx):
    """Get a NSFW picture."""
    await send_nsfw_image(ctx, "pic")

@siddhu.command()
async def thigh(ctx):
    """Get a thigh NSFW image."""
    await send_nsfw_image(ctx, "thigh")

@siddhu.command()
async def holo(ctx):
    """Get a holo NSFW image."""
    await send_nsfw_image(ctx, "holo")

@siddhu.command()
async def cosplay(ctx):
    """Get a cosplay NSFW image."""
    await send_nsfw_image(ctx, "cosplay")

@siddhu.command()
async def hthigh(ctx):
    """Get a hentai thigh NSFW image."""
    await send_nsfw_image(ctx, "hthigh")

@siddhu.command()
async def lewd(ctx):
    """Get a lewd NSFW image."""
    await send_nsfw_image(ctx, "lewd")

@siddhu.command()
async def hentai(ctx):
    """Get a hentai NSFW image."""
    await send_nsfw_image(ctx, "hentai")

@siddhu.command()
async def wild(ctx):
    """Get an anal NSFW image."""
    await send_nsfw_image(ctx, "anal")

@siddhu.command()
async def feet(ctx):
    """Get a feet NSFW image."""
    await send_nsfw_image(ctx, "feet")

@siddhu.command()
async def hboobs(ctx):
    """Get a hentai boobs NSFW image."""
    await send_nsfw_image(ctx, "hboobs")

@siddhu.command()
async def hass(ctx):
    """Get a hentai ass NSFW image."""
    await send_nsfw_image(ctx, "hass")

import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os

# Font paths (ensure these files exist in your directory)
BOLD_FONT_PATH = "arial_bold.ttf"
SMALL_FONT_PATH = "arial.ttf"

from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ext import commands

import aiohttp
import discord
from urllib.parse import quote

@siddhu.command()
async def phlogo(ctx, *, text: str):
    """Generate a Pornhub-style logo with custom text."""
    try:
        # Split the input text into two parts
        parts = text.split(" ")
        if len(parts) != 2:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Please provide exactly two words separated by a space.")
            return
        
        text1, text2 = parts
        
        # Create an image
        img_width = 800
        img_height = 200
        background_color = (0, 0, 0)  # Black background
        img = Image.new("RGB", (img_width, img_height), color=background_color)
        draw = ImageDraw.Draw(img)
        
        # Load fonts
        font_path = "arial_bold.ttf"  # Ensure this font file exists in the same directory
        font = ImageFont.truetype(font_path, 120)

        # Calculate text sizes
        text1_size = draw.textbbox((0, 0), text1, font=font)  # Updated method
        text2_size = draw.textbbox((0, 0), text2, font=font)  # Updated method

        # Calculate positions
        padding = 20
        total_width = (text1_size[2] - text1_size[0]) + (text2_size[2] - text2_size[0]) + padding
        start_x = (img_width - total_width) // 2
        start_y = (img_height - (text1_size[3] - text1_size[1])) // 2

        # Draw the first word (white text)
        draw.text((start_x, start_y), text1, font=font, fill=(255, 255, 255))

        # Draw the second word (orange box)
        box_x = start_x + (text1_size[2] - text1_size[0]) + padding
        box_y = start_y
        box_width = text2_size[2] - text2_size[0]
        box_height = text2_size[3] - text2_size[1]
        draw.rectangle([box_x, box_y, box_x + box_width, box_y + box_height], fill=(237, 128, 38))
        draw.text((box_x, box_y), text2, font=font, fill=(0, 0, 0))

        # Save the image
        file_path = "phlogo.png"
        img.save(file_path)
        await ctx.send(file=discord.File(file_path))
        os.remove(file_path)  # Clean up the file after sending
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Could not generate the Pornhub logo. Error: {e}")

# Pornhub Comment Command
@siddhu.command()
async def phcomment(ctx, name: str, *, comment: str):
    """Generate a custom Pornhub comment."""
    try:
        # Create a blank image with white background
        img = Image.new("RGB", (800, 150), "white")
        draw = ImageDraw.Draw(img)

        # Load fonts
        bold_font = ImageFont.truetype(BOLD_FONT_PATH, 40)
        small_font = ImageFont.truetype(SMALL_FONT_PATH, 30)

        # Add the username
        draw.text((10, 10), name, font=bold_font, fill="black")

        # Add the comment text
        draw.text((10, 60), comment, font=small_font, fill="black")

        # Save the image
        file_path = "phcomment.png"
        img.save(file_path)

        # Send the image to Discord
        await ctx.send(file=discord.File(file_path))
        os.remove(file_path)  # Clean up the file after sending
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: {e}")

# Text command
import os

@siddhu.command()
async def txt(ctx, *, content: str):
    """Send content as a text file."""
    file_path = "synthex.txt"
    try:
        # Write content to a text file
        with open(file_path, "w") as file:
            file.write(content)

        # Send the file to Discord
        await ctx.send("Here is your text file:", file=discord.File(file_path))
    finally:
        # Ensure the file is deleted after sending
        if os.path.exists(file_path):
            os.remove(file_path)

# Pin a Message
@siddhu.command()
async def pin(ctx, message_id: int):
    """Pin a specific message by ID."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.pin()
        await ctx.send("<:Tick:1290693799361777665> Message pinned successfully.")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I do not have permission to pin this message.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to pin the message.")

# Unpin a Message
@siddhu.command()
async def unpin(ctx, message_id: int):
    """Unpin a specific message by ID."""
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.unpin()
        await ctx.send("<:Tick:1290693799361777665> Message unpinned successfully.")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I do not have permission to unpin this message.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to unpin the message.")

import discord
import os
import zipfile
import aiohttp
import asyncio
from discord.ext import commands

@siddhu.command()
async def massemojiadd(ctx, emoji_name: str = None):
    if not ctx.message.attachments:
        return await ctx.send("❌ Please attach a ZIP file containing emojis.")

    zip_attachment = ctx.message.attachments[0]

    if not zip_attachment.filename.endswith(".zip"):
        return await ctx.send("❌ The attached file must be a ZIP archive.")

    await ctx.send("📥 Downloading and extracting ZIP file...")

    # Download ZIP file
    zip_path = f"./temp_{ctx.author.id}.zip"
    extract_folder = f"./extracted_{ctx.author.id}"
    os.makedirs(extract_folder, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(zip_attachment.url) as resp:
            if resp.status == 200:
                with open(zip_path, "wb") as f:
                    f.write(await resp.read())

    # Extract ZIP
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_folder)
    except zipfile.BadZipFile:
        os.remove(zip_path)
        os.rmdir(extract_folder)
        return await ctx.send("❌ Invalid ZIP file.")

    os.remove(zip_path)  # Delete ZIP after extraction

    # Get all image files
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
    image_files = [f for f in os.listdir(extract_folder) if f.lower().endswith(valid_extensions)]

    if not image_files:
        os.rmdir(extract_folder)
        return await ctx.send("❌ No valid images found in the ZIP file.")

    guild = ctx.guild
    added_static, added_animated, failed = 0, 0, 0
    failed_list = []
    
    emoji_limit = guild.emoji_limit
    existing_static = len([e for e in guild.emojis if not e.animated])
    existing_animated = len([e for e in guild.emojis if e.animated])

    for idx, file_name in enumerate(image_files):
        file_path = os.path.join(extract_folder, file_name)
        is_animated = file_name.lower().endswith(".gif")

        # Check if slots are available
        if is_animated and existing_animated + added_animated >= emoji_limit // 2:
            continue  # Skip animated if slot is full
        if not is_animated and existing_static + added_static >= emoji_limit // 2:
            continue  # Skip static if slot is full

        with open(file_path, "rb") as image_data:
            image_bytes = image_data.read()

        # Determine emoji name
        final_name = emoji_name or os.path.splitext(file_name)[0] or f"Synthex_Emoji_{idx+1}"

        # Add emoji
        try:
            emoji = await guild.create_custom_emoji(name=final_name, image=image_bytes)
            if is_animated:
                added_animated += 1
            else:
                added_static += 1
        except discord.HTTPException as e:
            failed += 1
            failed_list.append(f"{file_name} ({e})")

        await asyncio.sleep(1)  # Avoid rate limits

    # Cleanup extracted files
    try:
        for file in os.listdir(extract_folder):
            os.remove(os.path.join(extract_folder, file))
        os.rmdir(extract_folder)
    except Exception as e:
        await ctx.send(f"⚠ Failed to delete extracted folder: {str(e)}")

    # Send summary
    summary = f"✅ **Added {added_static} static & {added_animated} animated emojis**\n❌ **{failed} failed** due to errors."
    if failed_list:
        summary += "\n🚫 **Failed Emojis:**\n" + "\n".join(failed_list[:5])  # Show up to 5 failed

    await ctx.send(summary)

import discord
import json
import os

import json
import os
import aiohttp
from discord.ext import commands

MSG_FILE = "msgs.json"

# Load saved data
if os.path.exists(MSG_FILE):
    with open(MSG_FILE, "r", encoding="utf-8") as f:
        try:
            message_data = json.load(f)
        except json.JSONDecodeError:
            message_data = {"deleted": [], "edited": [], "sniper_enabled": False, "webhook_url": ""}
else:
    message_data = {"deleted": [], "edited": [], "sniper_enabled": False, "webhook_url": ""}

def save_msg_data():
    with open(MSG_FILE, "w", encoding="utf-8") as f:
        json.dump(message_data, f, indent=4)

# CMD: .msg_sniper enable/disable
@siddhu.command()
async def msg_sniper(ctx, mode: str = None):
    if mode not in ["enable", "disable"]:
        await ctx.send("❌ Usage: `.msg_sniper enable` or `.msg_sniper disable`")
        return

    message_data["sniper_enabled"] = (mode == "enable")
    save_msg_data()
    status = "enabled" if message_data["sniper_enabled"] else "disabled"
    await ctx.send(f"<:tz_Verified:1281238102823665797> Message sniper **{status}**.")

# CMD: .msg_webhook <link>
@siddhu.command()
async def msg_webhook(ctx, link: str = None):
    if not link or "discord.com/api/webhooks/" not in link:
        await ctx.send("❌ Please provide a valid webhook link.")
        return

    message_data["webhook_url"] = link
    save_msg_data()
    await ctx.send("<:tz_Verified:1281238102823665797> Webhook URL set successfully.")

@siddhu.event
async def on_message_delete(message):
    cached = message_cache.get(message.id)
    if cached:
        message = cached
    else:
        # Can't log anything if we don't have full message
        return

    if message.author.bot or (not message.content and not message.attachments):
        return

    # Save deleted msg locally
    msg_info = {
        "channel": message.channel.id,
        "author": str(message.author),
        "content": message.content,
        "timestamp": str(message.created_at)
    }

    message_data["deleted"].append(msg_info)
    if len(message_data["deleted"]) > 150:
        message_data["deleted"].pop(0)
    save_msg_data()

    # Spy logging
    if str(message.author.id) in spy_config["spy_data"]:
        log_spy_activity(
            message.author,
            "Message Deleted",
            f"🗑️ **Channel:** <#{message.channel.id}>\n📝 **Content:** {message.content}"
        )

    # Webhook logging
    if message_data.get("sniper_enabled") and message_data.get("webhook_url"):
        # Channel jump link
        if message.guild:
            channel_link = f"https://discord.com/channels/{message.guild.id}/{message.channel.id}"
        else:
            channel_link = "*N/A (DM)*"

        # Get images
        image_urls = [
            a.url for a in message.attachments
            if a.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))
        ]

        author_avatar = str(message.author.avatar_url) if message.author.avatar else None
        selfbot_avatar = str(siddhu.user.avatar_url) if siddhu.user.avatar else None

        # First embed
        embed = {
            "title": "**A message has been deleted** <a:exc:1325375984509128754>",
            "color": 0x2f3136,
            "fields": [
                {"name": "<:user:1325418236514140282> Author", "value": f"{message.author} (`{message.author.id}`)", "inline": False},
                {"name": "<:Discord_bots:1290700055514452121> Server", "value": message.guild.name if message.guild else "DM", "inline": False},
                {"name": "<:emoji_1738476614300:1335492458909401088> Channel", "value": f"[Click Here]({channel_link})", "inline": False},
                {"name": "<:bxbz_monet_lovenote:1290693793724497920> Message", "value": message.content or "*No content*", "inline": False}
            ],
            "timestamp": message.created_at.isoformat(),
            "thumbnail": {"url": author_avatar} if author_avatar else None,
            "footer": {
                "text": f"Message Logging - {message.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
                "icon_url": selfbot_avatar or ""
            }
        }

        # Add first image to main embed
        if image_urls:
            embed["image"] = {"url": image_urls[0]}

        # Extra embeds for more images
        extra_embeds = []
        for url in image_urls[1:10]:  # Max 10 embeds total
            extra_embeds.append({
                "color": 0x2f3136,
                "image": {"url": url}
            })

        payload = {
            "username": message.author.name,
            "avatar_url": author_avatar,
            "embeds": [embed] + extra_embeds
        }

        async with aiohttp.ClientSession() as session:
            try:
                await session.post(message_data["webhook_url"], json=payload)
            except Exception as e:
                print(f"[Webhook Error] {e}")

@siddhu.event
async def on_message_edit(before, after):
    """Track edited messages and save to msgs.json."""
    if before.author.bot or before.content == after.content:
        return

    edit_info = {
        "channel": before.channel.id,
        "author": str(before.author),
        "before": before.content,
        "after": after.content,
        "timestamp": str(before.created_at)
    }

    message_data["edited"].append(edit_info)
    if len(message_data["edited"]) > 150:
        message_data["edited"].pop(0)  # Keep only last 150 messages globally

    with open(MSG_FILE, "w", encoding="utf-8") as f:
        json.dump(message_data, f, indent=4)

    # Spy logic
    if str(before.author.id) in spy_config["spy_data"]:
        log_spy_activity(
            before.author,
            "Message Edited",
            f"✏️ **Channel:** <#{before.channel.id}>\n"
            f"🔹 **Before:** {before.content}\n"
            f"🔸 **After:** {after.content}"
        )

@siddhu.command()
async def snipe(ctx):
    """Retrieve the last 5 deleted messages in the current channel."""
    channel_id = ctx.channel.id
    deleted_msgs = [msg for msg in message_data["deleted"] if msg["channel"] == channel_id]

    if not deleted_msgs:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> No recently deleted messages found in this channel.")

    recent_msgs = deleted_msgs[-5:]  # Get last 5 messages in this channel
    response = "\n\n".join(
        f"🗑️ **Deleted Message {i+1} by {msg['author']}:** {msg['content']}"
        for i, msg in enumerate(recent_msgs)
    )

    await ctx.send(response)

@siddhu.command()
async def editsnipe(ctx):
    """Retrieve the last 5 edited messages in the current channel."""
    channel_id = ctx.channel.id
    edited_msgs = [msg for msg in message_data["edited"] if msg["channel"] == channel_id]

    if not edited_msgs:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> No recently edited messages found in this channel.")

    recent_edits = edited_msgs[-5:]  # Get last 5 messages in this channel
    response = "\n\n".join(
        f"✏️ **Edited Message {i+1} by {msg['author']}:**\n"
        f"Before: {msg['before']}\n"
        f"After: {msg['after']}"
        for i, msg in enumerate(recent_edits)
    )

    await ctx.send(response)

@siddhu.command()
async def clear(ctx, limit: int):
    """Delete your last <limit> messages in the current channel/DM."""
    await ctx.message.delete()  # Remove command message

    deleted = 0
    messages = []

    async for msg in ctx.channel.history(limit=200):
        if msg.author.id == siddhu.user.id:
            messages.append(msg)
        if len(messages) >= limit:
            break

    for msg in messages[:limit]:
        try:
            await msg.delete()
            deleted += 1
        except discord.Forbidden:
            pass  # silently skip if can't delete
        except discord.HTTPException:
            pass

    try:
        reply = await ctx.reply(f"<:Tick:1290693799361777665> Deleted `{deleted}` messages.")
        await asyncio.sleep(5)
        await reply.delete()
    except:
        pass  # silent fail if we can't reply or delete

# Purge Messages
@siddhu.command()
async def purge(ctx, limit: int):
    """Delete a specified number of messages from everyone in the channel (ignores messages older than 14 days)."""
    await ctx.message.delete()

    try:
        from datetime import datetime, timedelta

        cutoff = datetime.utcnow() - timedelta(days=14)
        to_delete = []

        async for msg in ctx.channel.history(limit=limit):
            if msg.created_at > cutoff:
                to_delete.append(msg)

        deleted = await ctx.channel.delete_messages(to_delete)
        result_msg = f"<:Tick:1290693799361777665> Successfully deleted `{len(deleted)}` messages (older than 14 days are ignored)."

        if embed_mode_enabled:
            reply = await ctx.reply(result_msg)
            await asyncio.sleep(5)
            await reply.delete()
        else:
            await ctx.send(result_msg, delete_after=5)

    except discord.Forbidden:
        err = "<:CROSS_TDG:1321149916201881683> I don't have permission to delete messages in this channel."
        if embed_mode_enabled:
            reply = await ctx.reply(err)
            await asyncio.sleep(5)
            await reply.delete()
        else:
            await ctx.send(err, delete_after=5)

    except discord.HTTPException as e:
        err = f"<:CROSS_TDG:1321149916201881683> Failed to delete messages: {e}"
        if embed_mode_enabled:
            reply = await ctx.reply(err)
            await asyncio.sleep(5)
            await reply.delete()
        else:
            await ctx.send(err, delete_after=5)

    except Exception as e:
        err = f"<:CROSS_TDG:1321149916201881683> An unexpected error occurred: {e}"
        if embed_mode_enabled:
            reply = await ctx.reply(err)
            await asyncio.sleep(5)
            await reply.delete()
        else:
            await ctx.send(err, delete_after=5)

@siddhu.command()
async def find(ctx, *, keyword: str):
    """Search for messages containing a specific keyword."""
    await ctx.message.delete()  # Delete the command message immediately
    messages = await ctx.channel.history(limit=100).flatten()
    found = [msg.content for msg in messages if keyword.lower() in msg.content.lower()]
    if found:
        await ctx.send(f"🔍 Found messages:\n" + "\n".join(found[:5]))
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> No messages found containing that keyword.")

@siddhu.command()
async def react(ctx, message_id: int, emoji: str):
    try:
        channel_id = ctx.channel.id
        # Encode emoji for URL if it's a custom emoji or unicode
        if emoji.startswith("<") and emoji.endswith(">"):
            # Custom emoji like <a:name:id>
            emoji_id = emoji.split(":")[-1].replace(">", "")
            emoji_name = emoji.split(":")[1]
            emoji = f"{emoji_name}:{emoji_id}"
        else:
            # Unicode emoji must be URL-encoded
            from urllib.parse import quote
            emoji = quote(emoji)

        # Use raw HTTP route to add reaction
        await ctx.bot.http.request(
            discord.http.Route(
                "PUT",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji
            )
        )
        await ctx.send("<:Tick:1290693799361777665> Reaction added successfully.")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.HTTPException as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to react: {str(e)}")

@siddhu.command()
async def unreact(ctx, message_id: int, emoji: str):
    try:
        channel_id = ctx.channel.id

        # Encode emoji
        if emoji.startswith("<") and emoji.endswith(">"):
            emoji_id = emoji.split(":")[-1].replace(">", "")
            emoji_name = emoji.split(":")[1]
            emoji = f"{emoji_name}:{emoji_id}"
        else:
            emoji = quote(emoji)

        # Send raw request to remove reaction
        await ctx.bot.http.request(
            discord.http.Route(
                "DELETE",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji
            )
        )
        await ctx.send("<:Tick:1290693799361777665> Reaction removed successfully.")
    except discord.NotFound:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Message not found.")
    except discord.HTTPException as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to remove reaction: {str(e)}")

@siddhu.command()
async def set_topic(ctx, *, topic):
    await ctx.channel.edit(topic=topic)
    await ctx.send(f"# 📝 Topic set to:\n> {topic}")

@siddhu.command()
async def delete_channel(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send(f"# 🗑️ Channel `{channel.name}` deleted")

@siddhu.command()
async def rename_channel(ctx, *, new_name):
    await ctx.channel.edit(name=new_name)
    await ctx.send(f"# ✏️ Channel renamed to `{new_name}`")

@siddhu.command()
async def create_category(ctx, *, name):
    await ctx.guild.create_category(name=name)
    await ctx.send(f"# 🗂️ Category `{name}` created")

@siddhu.command()
async def renamerole(ctx, role: discord.Role, *, new_name: str):
    try:
        await role.edit(name=new_name, reason=f"Renamed by {ctx.author}")
        await ctx.send(f"Role `{role.name}` has been renamed to `{new_name}`.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to edit that role.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to rename role: {e}")

import discord
import asyncio
from discord.ext import commands

@siddhu.command()
async def deleteallemojis(ctx):
    guild = ctx.guild
    if not guild:
        return await ctx.send("❌ This command can only be used in a server.")

    emojis = guild.emojis
    if not emojis:
        return await ctx.send("❌ No emojis found in this server.")

    deleted_static, deleted_animated, failed = 0, 0, 0
    failed_list = []

    await ctx.send(f"🗑 **Starting to delete {len(emojis)} emojis...**")

    for emoji in emojis:
        try:
            await emoji.delete()
            if emoji.animated:
                deleted_animated += 1
            else:
                deleted_static += 1
        except discord.HTTPException as e:
            failed += 1
            failed_list.append(f"{emoji.name} ({e})")
        
        await asyncio.sleep(1)  # Prevent hitting rate limits

    summary = f"✅ **Deleted {deleted_static} static & {deleted_animated} animated emojis**\n❌ **{failed} failed.**"
    if failed_list:
        summary += "\n🚫 **Failed Emojis:**\n" + "\n".join(failed_list[:5])  # Show up to 5 failed

    await ctx.send(summary)

# Caps Lock Message
@siddhu.command()
async def caps(ctx, *, message: str):
    """Convert the message to uppercase."""
    await ctx.send(message.upper())

# Lowercase Message
@siddhu.command()
async def small(ctx, *, message: str):
    """Convert the message to lowercase."""
    await ctx.send(message.lower())

# Repeat Message
@siddhu.command()
async def repeat(ctx, message: str, times: int):
    """Repeat a message multiple times."""
    if times > 10:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You can only repeat a message up to 10 times.")
        return
    await ctx.send((message + "\n") * times)

# Spoiler Message
@siddhu.command()
async def spoiler(ctx, *, message: str):
    """Convert the message to spoiler format."""
    await ctx.send(f"||{message}||")

# Split Message
@siddhu.command()
async def split(ctx, *, message: str):
    """Split a long message into chunks of 2000 characters."""
    if len(message) > 2000:
        for i in range(0, len(message), 2000):
            await ctx.send(message[i:i + 2000])
    else:
        await ctx.send(message)

# Highlight Word
@siddhu.command()
async def highlight(ctx, word: str, *, message: str):
    """Highlight a specific word in the message."""
    highlighted = message.replace(word, f"**{word}**")
    await ctx.send(highlighted)

# Count Word Occurrences
@siddhu.command()
async def count(ctx, word: str):
    """Count the occurrences of a word in the last 100 messages."""
    messages = await ctx.channel.history(limit=100).flatten()
    count = sum(1 for msg in messages if word.lower() in msg.content.lower())
    await ctx.send(f"🔍 The word `{word}` appears {count} times in the last 100 messages.")

# Bold Text
@siddhu.command()
async def bold(ctx, *, message: str):
    """Format the message in bold."""
    await ctx.send(f"**{message}**")

# Italic Text
@siddhu.command()
async def italic(ctx, *, message: str):
    """Format the message in italics."""
    await ctx.send(f"*{message}*")

# Underline Text
@siddhu.command()
async def underline(ctx, *, message: str):
    """Format the message with underlining."""
    await ctx.send(f"__{message}__")

# Strikethrough Text
@siddhu.command()
async def strike(ctx, *, message: str):
    """Format the message with strikethrough."""
    await ctx.send(f"~~{message}~~")

# Code Block
@siddhu.command()
async def codeblock(ctx, *, message: str):
    """Format the message as a code block."""
    await ctx.send(f"```\n{message}\n```")

# Multi-line Code Block
@siddhu.command()
async def multicode(ctx, *, message: str):
    """Format the message as a multi-line code block."""
    await ctx.send(f"```\n{message}\n```")

# Blockquote
@siddhu.command()
async def blockquote(ctx, *, message: str):
    """Format the message as a blockquote."""
    await ctx.send(f"> {message}")

# Combine Two Messages
@siddhu.command()
async def combine(ctx, message1: str, message2: str):
    """Combine two messages into one."""
    await ctx.send(f"{message1} {message2}")

@siddhu.command()
async def deleteafter(ctx, seconds: int, *, message: str):
    """
    Send a message that deletes itself after a specified number of seconds.
    Usage: .deleteafter <seconds> <message>
    """
    if seconds > 60:  # Set a reasonable maximum timeout
        await ctx.send("<:CROSS_TDG:1321149916201881683> You can only set a delete timer for up to 60 seconds.")
        return

    try:
        sent_message = await ctx.send(message)
        await asyncio.sleep(seconds)
        await sent_message.delete()
        await ctx.send("<:Tick:1290693799361777665> Message auto-deleted!", delete_after=5)
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I do not have permission to delete messages.")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> An error occurred while trying to delete the message.")
        
# 6. Flip Text Command
@siddhu.command()
async def fliptext(ctx, *, text: str):
    flipped = text[::-1]
    await ctx.send(f"🔄 Flipped: {flipped}")

# 7. Rate Command
@siddhu.command()
async def rate(ctx, *, thing: str):
    rating = random.randint(1, 10)
    await ctx.send(f"📊 I rate `{thing}` a {rating}/10!")

# 8. Insult Command
@siddhu.command()
async def insult(ctx, *, name: str):
    insults = [
        "You're as bright as a black hole, and twice as dense.",
        "You're proof that even a broken clock is right twice a day.",
        "You bring everyone so much joy… when you leave the room."
    ]
    await ctx.send(f"😈 {name}, {random.choice(insults)}")

# 9. Compliment Command
@siddhu.command()
async def compliment(ctx, *, name: str):
    compliments = [
        "You're a star, keep shining!",
        "You're more amazing than words can express!",
        "You're the reason someone smiles today."
    ]
    await ctx.send(f"🌟 {name}, {random.choice(compliments)}")

# 10. Random Color Command
@siddhu.command()
async def randomcolor(ctx):
    color = f"#{random.randint(0, 0xFFFFFF):06x}".upper()
    await ctx.send(f"🎨 Your random color: `{color}`")

# 11. Roll Coin Command
@siddhu.command()
async def rollcoin(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"🪙 The coin landed on {result}!")

# 12. Word Jumble Command
@siddhu.command()
async def wordjumble(ctx, *, word: str):
    jumbled = ''.join(random.sample(word, len(word)))
    await ctx.send(f"🔀 Jumbled Word: `{jumbled}`")

# 13. Motivate Command
@siddhu.command()
async def motivate(ctx):
    quotes = [
    "Believe you can and you're halfway there.",
    "Don't stop until you're proud.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream big and dare to fail.",
    "Opportunities don't happen, you create them.",
    "Believe in yourself and all that you are.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The key to success is to focus on goals, not obstacles.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Hard work beats talent when talent doesn't work hard.",
    "Don't watch the clock; do what it does. Keep going.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Everything you can imagine is real.",
    "It always seems impossible until it's done.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Success is not how high you have climbed, but how you make a positive difference to the world.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Act as if what you do makes a difference. It does.",
    "Success usually comes to those who are too busy to be looking for it.",
    "If you want to achieve greatness stop asking for permission.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Start where you are. Use what you have. Do what you can.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "You don’t have to be great to start, but you have to start to be great.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Success is not in what you have, but who you are.",
    "Don't limit your challenges. Challenge your limits.",
    "The only impossible journey is the one you never begin.",
    "It always seems impossible until it's done.",
    "Do one thing every day that scares you.",
    "In the middle of difficulty lies opportunity.",
    "The only way to do great work is to love what you do.",
    "Nothing will work unless you do.",
    "Don’t wait for opportunity, create it.",
    "The road to success and the road to failure are almost exactly the same.",
    "Success is not for the chosen few, it’s for the few who choose it.",
    "If you can dream it, you can do it.",
    "Start where you are. Use what you have. Do what you can.",
    "Success is the result of preparation, hard work, and learning from failure.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Be fearless in the pursuit of what sets your soul on fire."
    ]
    await ctx.send(f"💡 {random.choice(quotes)}")

@siddhu.command()
async def set_qr(ctx, qr: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['Qr'] = qr
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> QR code updated to {qr}")

@siddhu.command()
async def set_serverlink(ctx, link: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['SERVER_Link'] = link
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> Server link updated to {link}")

# Your API keys
openweather_api_key = "e50ebe27f9b5ce6fc9aeb309cba27700"  # Replace with your OpenWeather API key
openai_api_key = "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"  # Replace with your OpenAI API key

# Weather Command
@siddhu.command()
async def weather(ctx, *, city: str):
    """Get weather updates for a city"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        await ctx.send(f"**Weather in {city.title()}**:\n"
                       f"🌡️ Temperature: {temp}°C\n"
                       f"☁️ Description: {description.capitalize()}\n"
                       f"💧 Humidity: {humidity}%\n"
                       f"🌬️ Wind Speed: {wind_speed} m/s")
    else:
        await ctx.send("City not found or API error!")

# Google Search Command
@siddhu.command()
async def google(ctx, *, query: str):
    """Generate a Google search link"""
    search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}"
    await ctx.send(f"Top search result: {search_url}")

# Magic 8-Ball Command
@siddhu.command()
async def magic8ball(ctx, *, question: str):
    """Ask the magic 8-ball a question"""
    responses = ["Yes", "No", "Maybe", "Definitely", "Ask again later", "Not sure"]
    await ctx.send(f"🎱 {random.choice(responses)}")

# Trivia Command
@siddhu.command()
async def trivia(ctx):
    """Ask a random trivia question"""
    questions = {
    "What is the smallest planet in our solar system?": ["Mercury", "Venus", "Mars", "Earth"],
    "Who painted the Mona Lisa?": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
    "What is the capital of Japan?": ["Tokyo", "Osaka", "Kyoto", "Nagoya"],
    "Which element has the chemical symbol 'O'?": ["Oxygen", "Gold", "Silver", "Hydrogen"],
    "What is the tallest mountain in the world?": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    "Who wrote 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    "What is the largest ocean on Earth?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
    "Which country is known as the Land of the Rising Sun?": ["Japan", "China", "South Korea", "Thailand"],
    "What is the chemical formula for water?": ["H2O", "CO2", "O2", "NaCl"],
    "Who discovered gravity?": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
    "What is the hardest natural substance on Earth?": ["Diamond", "Gold", "Iron", "Granite"],
    "Which animal is known as the King of the Jungle?": ["Lion", "Tiger", "Elephant", "Leopard"],
    "What is the largest continent?": ["Asia", "Africa", "Europe", "North America"],
    "What is the speed of light?": ["299,792 km/s", "150,000 km/s", "1,000 km/s", "300 km/s"],
    "What is the square root of 64?": ["8", "6", "7", "9"],
    "What is the capital of Italy?": ["Rome", "Venice", "Milan", "Naples"],
    "Who invented the telephone?": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"],
    "What is the main ingredient in guacamole?": ["Avocado", "Tomato", "Cucumber", "Lettuce"],
    "What is the capital of Australia?": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
    "Which planet is known as the Morning Star?": ["Venus", "Mars", "Mercury", "Jupiter"],
    "What is the largest bird in the world?": ["Ostrich", "Eagle", "Penguin", "Albatross"],
    "What is the freezing point of water in Celsius?": ["0°C", "32°C", "100°C", "-1°C"],
    "Who developed the theory of relativity?": ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Galileo Galilei"],
    "What is the smallest bone in the human body?": ["Stapes", "Fibula", "Ulna", "Radius"],
    "What is the chemical symbol for gold?": ["Au", "Ag", "Fe", "Pb"],
    "Which country invented paper?": ["China", "Egypt", "Greece", "India"],
    "What is the main gas found in the air we breathe?": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"],
    "Who is known as the Father of Computers?": ["Charles Babbage", "Alan Turing", "John von Neumann", "Ada Lovelace"],
    "What is the capital of Canada?": ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    "Which is the longest river in the world?": ["Nile", "Amazon", "Yangtze", "Mississippi"]
    }
    question, answers = random.choice(list(questions.items()))
    await ctx.send(f"Question: {question}\nOptions: {', '.join(answers)}")

# Timezone Command
@siddhu.command()
async def timezone(ctx, time: str, from_zone: str, to_zone: str):
    """Convert time from one timezone to another."""
    try:
        from_zone = pytz.timezone(from_zone)
        to_zone = pytz.timezone(to_zone)
        naive_time = datetime.datetime.strptime(time, "%H:%M")
        from_time = from_zone.localize(naive_time)
        to_time = from_time.astimezone(to_zone)
        await ctx.send(f"🕒 {time} in `{from_zone.zone}` is `{to_time.strftime('%H:%M')}` in `{to_zone.zone}`.")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error: {e}")
    
@siddhu.command()
async def track_ip(ctx, ip: str):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"IP: {ip}\nCity: {data['city']}\nCountry: {data['country_name']}")
    else:
        await ctx.send("Failed to fetch geolocation data.")

@siddhu.command()
async def uuid(ctx):
    import uuid
    await ctx.send(f"Generated UUID: `{uuid.uuid4()}`")

# Encrypt Command
@siddhu.command()
async def encrypt(ctx, *, message: str):
    """Encrypt a message using Base64."""
    try:
        encoded = base64.b64encode(message.encode("utf-8")).decode("utf-8")
        await ctx.send(f"🔐 Encrypted: `{encoded}`")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error encrypting message: {e}")

# Decrypt Command
@siddhu.command()
async def decrypt(ctx, *, encoded_message: str):
    """Decrypt a Base64 encoded message."""
    try:
        decoded = base64.b64decode(encoded_message.encode("utf-8")).decode("utf-8")
        await ctx.send(f"🔓 Decrypted: `{decoded}`")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error decoding message: {e}")

# Poll Command
@siddhu.command()
async def poll(ctx, question: str, *options):
    """Create a poll with up to 10 options."""
    if len(options) > 10:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You can only provide up to 10 options.")
        return

    description = "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
    embed = discord.Embed(title=question, description=description, color=discord.Color.blue())
    message = await ctx.send(embed=embed)

    # Add reactions for voting
    reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    for i in range(len(options)):
        await message.add_reaction(reactions[i])

# JSON Formatter Command
@siddhu.command()
async def jsonformat(ctx, *, data: str):
    """Format and prettify JSON."""
    try:
        parsed = json.loads(data)
        pretty_json = json.dumps(parsed, indent=4)
        await ctx.send(f"```json\n{pretty_json}\n```")
    except json.JSONDecodeError:
        await ctx.send("Invalid JSON!")

# Python Evaluator Command
@siddhu.command()
async def evaluate(ctx, *, code: str):
    """Evaluate Python code."""
    try:
        result = eval(code)
        await ctx.send(f"Result: `{result}`")
    except Exception as e:
        await ctx.send(f"Error: `{e}`")

# Ping Test Command
@siddhu.command()
async def pingtest(ctx, *, host: str):
    """Ping a host and get its latency."""
    try:
        ping = socket.gethostbyname(host)
        await ctx.send(f"Pinged {host} (IP: {ping}) successfully!")
    except Exception as e:
        await ctx.send(f"Error: `{e}`")

import discord
from discord.ext import commands, tasks
import json
import asyncio
import os
import requests

# Load configuration
CONFIG_FILE = "config.json"
VANITY_ASSETS = "Vanity Assets"

if not os.path.exists(VANITY_ASSETS):
    os.makedirs(VANITY_ASSETS)

CONFIG = {"vanity_sniper": False, "vanities": {}, "vanity_delay": 5, "vsniper_webhook": ""}

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        CONFIG.update(json.load(f))

def save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(CONFIG, f, indent=4)

# Load tokens and proxies
def load_file(filename):
    path = os.path.join(VANITY_ASSETS, filename)
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().splitlines()
    return []

TOKENS = load_file("tokens.txt")
PROXIES = load_file("proxies.txt")

# Sniper Task
@tasks.loop(seconds=CONFIG["vanity_delay"])
async def vanity_sniper_task():
    if not CONFIG["vanity_sniper"]:
        return
    
    for vanity, target_server in CONFIG["vanities"].items():
        available = check_vanity_available(vanity)
        if available:
            success = snipe_vanity(vanity, target_server)
            log_vanity_attempt(vanity, target_server, success)

# Check Vanity Availability
def check_vanity_available(vanity):
    url = f"https://discord.com/api/v9/invites/{vanity}"
    response = requests.get(url)
    return response.status_code == 404

# Snipe Vanity
def snipe_vanity(vanity, target_server):
    for token in TOKENS:
        headers = {"Authorization": token}
        json_data = {"code": vanity}
        response = requests.patch(f"https://discord.com/api/v9/guilds/{target_server}/vanity-url", headers=headers, json=json_data)
        
        if response.status_code == 200:
            return True
    return False

# Log Attempt
def log_vanity_attempt(vanity, target_server, success):
    log_message = f"✅ Successfully sniped `{vanity}` for `{target_server}`" if success else f"❌ Failed to snipe `{vanity}`"
    print(log_message)

    if CONFIG["vsniper_webhook"]:
        requests.post(CONFIG["vsniper_webhook"], json={"content": log_message})

# Enable/Disable Sniper
@siddhu.command()
async def vanity_sniper(ctx, mode: str):
    if mode.lower() not in ["enable", "disable"]:
        return await ctx.send("❌ Use `.vanity_sniper enable` or `.vanity_sniper disable`.")
    
    CONFIG["vanity_sniper"] = mode.lower() == "enable"
    save_config()
    await ctx.send(f"✅ Vanity Sniper `{mode}`d!")

# Add Vanity to Snipe
@siddhu.command()
async def vsniper_add(ctx, vanity: str, target_server: int):
    CONFIG["vanities"][vanity] = target_server
    save_config()
    await ctx.send(f"✅ Added `{vanity}` to the snipe list for server `{target_server}`.")

# Remove Vanity from Snipe List
@siddhu.command()
async def vsniper_remove(ctx, vanity: str):
    if vanity not in CONFIG["vanities"]:
        return await ctx.send(f"❌ `{vanity}` is not in the snipe list.")
    
    del CONFIG["vanities"][vanity]
    save_config()
    await ctx.send(f"✅ Removed `{vanity}` from the snipe list.")

# Clear Vanity Snipe List
@siddhu.command()
async def vsniper_clear(ctx):
    CONFIG["vanities"].clear()
    save_config()
    await ctx.send("✅ Cleared the vanity snipe list.")

# Set Vanity Sniper Delay
@siddhu.command()
async def vanity_delay(ctx, delay: int):
    if delay < 1:
        return await ctx.send("❌ Delay must be at least 1 second.")
    
    CONFIG["vanity_delay"] = delay
    save_config()
    await ctx.send(f"✅ Vanity sniper delay set to `{delay}` seconds.")

# List All Sniping Vanities
@siddhu.command()
async def vanity_list(ctx):
    if not CONFIG["vanities"]:
        return await ctx.send("📌 No vanities in the sniping list.")
    
    snipes = "\n".join([f"🔹 `{v}` → `{s}`" for v, s in CONFIG["vanities"].items()])
    await ctx.send(f"📌 **Vanities Being Sniped:**\n{snipes}")

# Set Webhook for Vanity Logs
@siddhu.command()
async def vsniper_webhook(ctx, link: str):
    if not link.startswith("https://discord.com/api/webhooks/"):
        return await ctx.send("❌ Invalid webhook link!")
    
    CONFIG["vsniper_webhook"] = link
    save_config()
    await ctx.send("✅ Webhook saved for vanity logs.")

# Backup Vanity Sniper Config
@siddhu.command()
async def vsniper_backup(ctx):
    backup_file = "vanity_sniper_backup.json"
    with open(backup_file, "w") as f:
        json.dump(CONFIG, f, indent=4)
    
    await ctx.send(f"📌 Backup saved as `{backup_file}`!")

# Restore Vanity Sniper Config from Backup
@siddhu.command()
async def vsniper_restore(ctx):
    backup_file = "vanity_sniper_backup.json"
    
    if not os.path.exists(backup_file):
        return await ctx.send("❌ No backup file found!")
    
    with open(backup_file, "r") as f:
        CONFIG.update(json.load(f))
    
    save_config()
    await ctx.send("✅ Vanity Sniper settings restored from backup.")

# Show Vanity Sniper Logs
@siddhu.command()
async def vsniper_logs(ctx):
    logs_file = "vanity_sniper_logs.txt"
    
    if not os.path.exists(logs_file) or os.stat(logs_file).st_size == 0:
        return await ctx.send("📌 No logs available!")
    
    with open(logs_file, "r") as f:
        logs = f.read()
    
    await ctx.send(f"📌 **Vanity Sniper Logs:**\n```{logs}```")

# Start the Vanity Sniper Task
vanity_sniper_task.start()

# Hex to RGB Converter
@siddhu.command()
async def hextorgb(ctx, hex_code: str):
    """Convert Hex color code to RGB."""
    hex_code = hex_code.lstrip('#')
    try:
        rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        await ctx.send(f"RGB for #{hex_code.upper()}: {rgb}")
    except ValueError:
        await ctx.send("Invalid Hex Code!")

import asyncio

# 1. TTS Command
@siddhu.command()
async def tts(ctx, *, message: str):
    """Send a TTS (text-to-speech) message."""
    try:
        await ctx.send(message, tts=True)
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error: {e}")

# 2. Mock Command
mock_tasks = {}

@siddhu.command()
async def mock(ctx, member: discord.Member):
    """Start mocking a user's messages."""
    if ctx.author.id in mock_tasks:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You are already mocking someone. Use `.stop_mock` to stop.")
        return

    async def mock_listener():
        def check(msg):
            return msg.author == member and msg.channel == ctx.channel

        await ctx.send(f"<:rdx_glowin_heart:1288196137848803451>  Now mocking {member.display_name}.")
        try:
            while True:
                msg = await siddhu.wait_for('message', check=check, timeout=300)
                await ctx.send(msg.content)
        except asyncio.TimeoutError:
            await ctx.send(f"⌛ Stopped mocking {member.display_name} due to inactivity.")
        except asyncio.CancelledError:
            pass  # Graceful exit when canceled
        finally:
            mock_tasks.pop(ctx.author.id, None)

    mock_task = asyncio.create_task(mock_listener())
    mock_tasks[ctx.author.id] = mock_task

@siddhu.command()
async def stop_mock(ctx):
    """Stop mocking a user's messages."""
    if ctx.author.id not in mock_tasks:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You are not mocking anyone.")
        return

    mock_tasks[ctx.author.id].cancel()
    await ctx.send("🛑 Stopped mocking.")

import discord

# 1. Emojify Command
@siddhu.command()
async def emojify(ctx, *, text: str):
    """Convert text into emoji letters."""
    emojified = ''.join([f":regional_indicator_{char}:" if char.isalpha() else char for char in text.lower()])
    await ctx.send(emojified)

# 3. List Roles Command
@siddhu.command()
async def listroles(ctx):
    """List all roles in the server."""
    roles = ', '.join([role.name for role in ctx.guild.roles])
    await ctx.send(f"**Roles ({len(ctx.guild.roles)}):** {roles}")

# 4. List Bots Command
@siddhu.command()
async def listbots(ctx):
    """List all bots in the server."""
    bots = [member for member in ctx.guild.members if member.bot]
    bot_list = ', '.join([bot.name for bot in bots])
    await ctx.send(f"**Bots ({len(bots)}):** {bot_list}")

# 5. Server Info Command
@siddhu.command(description="Sends information about the server.")
async def serverinfo(ctx):
    await ctx.send(content="Fetching server info...")

    guild = ctx.guild
    created_timestamp = int(guild.created_at.timestamp())  # Convert to Discord timestamp

    # Fix for server icon URL
    icon_url = f"https://cdn.discordapp.com/icons/{guild.id}/{guild.icon}.png" if guild.icon else None
    icon_link = f"[SERVER LOGO IMAGE]({icon_url})" if icon_url else "None"

    # Handle owner fetching error
    owner = guild.owner
    owner_name = owner.name if owner else "Unknown"
    owner_id = owner.id if owner else "Unknown"
    owner_text = f"[{owner_name}] <@{owner_id}>" if owner != "Unknown" else "Unknown"

    message = f"""
# Server Info <:nxt_blue_crown:1281973611917348989>

**<:discord:1282007043456241717> Name: {guild.name}
<:experienced_seller:1290924799421583391> ID: {guild.id}
<:SQ_hearts:1288196135206518825> Server Icon: {icon_link}

<:max_r_owner:1288194870086860850> Owner: {owner_text}
<:discord:1282007043456241717> Owner ID: {owner_id}
<:white_Arrow:1290693791983861822> Created At: <t:{created_timestamp}:F>

<:emoji_1738476603350:1335492413153742961> Total Boosts: {guild.premium_subscription_count} Boosts
<:tz_Boost_icon:1281241573035868220> Boost Level: {guild.premium_tier} Level {"[Max]" if guild.premium_tier == 3 else ""}

<:user:1325418236514140282> Members: {guild.member_count} 
<:emoji_1738476614300:1335492458909401088> Channels: {len(guild.channels)}
<:emoji_1738476622593:1335492493680185384> Roles: {len(guild.roles)}
<a:emoji:1308820256873123980> Emojis: {len(guild.emojis)}**
"""
    await ctx.send(content=message)

@siddhu.command(description="Lists all friends in the server.")
async def serverfriends(ctx):
    await ctx.send(content="🔎 Fetching server friends...")

    # Get a list of mutual friends (workaround: using mutual servers)
    mutual_friends = [
        f"{member.name}#{member.discriminator}"
        for member in ctx.guild.members
        if not member.bot and member.id != ctx.author.id and any(guild.get_member(member.id) for guild in ctx.bot.guilds)
    ]

    if not mutual_friends:
        return await ctx.send(content="❌ No friends found in this server.")

    message = f"""
# Server Friends in **{ctx.guild.name}** <:experienced_seller:1290924799421583391>  
**[Total]: `{len(mutual_friends)}`**  

{', '.join(mutual_friends)}
    """.strip()

    await ctx.send(content=message)
    
@siddhu.command(description="Lists all mutual servers with a user.")
async def mutualservers(ctx, user: discord.User):
    await ctx.send(content=f"Fetching mutual servers with {user}...")

    mutual_servers = [guild.name for guild in siddhu.guilds if guild.get_member(user.id)]

    if not mutual_servers:
        return await ctx.send(content=f"No mutual servers found with {user}.")

    message = f"""<:Angel_of_coowner:1290692091432800357> Mutual Servers with [{user.name}#{user.discriminator}]:
<:BadgeDeveloper:1290693804013129768> [Total]: {len(mutual_servers)}**

```{', '.join(mutual_servers)}
```"""
    await ctx.send(content=message)
    await delete_after_timeout(ctx.message)

import requests
import discord
import json

@siddhu.command()
async def txhistory(ctx, address: str):
    """Fetches the last 5 transactions of a given Litecoin address with proper details."""

    API_URL = f"https://api.blockchair.com/litecoin/dashboards/address/{address}?transaction_details=true"

    try:
        response = requests.get(API_URL)
        data = response.json()

        # Ensure valid API response
        if "data" not in data or address not in data["data"]:
            await ctx.send("<:CROSS_TDG:1321149916201881683> **Invalid Litecoin address or no transaction history found!**")
            return

        transactions = data["data"][address]["transactions"]

        if not transactions:
            await ctx.send(f"__**LTC TX HISTORY**__ <a:tz_ltc:1281238097136451616>\n"
                           f"**No transactions found for this address!** <a:check:1281246680724930683>\n\n"
                           f"**<:RS_LTC:1291423858183897120> Litecoin Address:**\n"
                           f"<:white_arrow:1290693789824061461>`{address}`")
            return

        # Prepare transaction messages
        tx_messages = []
        for tx in transactions[:5]:  # Fetch latest 5 transactions
            tx_id = tx.get("hash", "N/A")
            amount_ltc = round(abs(tx.get("balance_change", 0) / 10**8), 8)  # Convert satoshis to LTC
            amount_usd = round(amount_ltc * 110, 2)  # Approximate USD value (1 LTC = $110)
            is_confirmed = tx.get("is_confirmed", False)
            status = "Confirmed <:lr_tick_1:1290693800808677461>" if is_confirmed else "Unconfirmed <:CROSS_TDG:1321149916201881683>"

            tx_messages.append(f"\n<:rules:1290926829762383934> **Transaction ID: [Click Here](https://blockchair.com/litecoin/transaction/{tx_id})**\n"
                               f"<:exchanger:1322954180452810775> **Amount: {amount_usd}$ [ {amount_ltc} <:LTC:1322611807269031968> ]**\n"
                               f"<:emoji_1738342244745:1334928872269152259> **Status: Confirmed <:Tick:1290693799361777665>**")

        # Send formatted message
        await ctx.send(f"__**LTC TX HISTORY**__ <a:tz_ltc:1281238097136451616>\n"
                       f"**Last {len(tx_messages)} transactions of the address!** <a:check:1281246680724930683>\n\n"
                       f"**<:RS_LTC:1291423858183897120> Litecoin Address:**\n"
                       f"<:white_arrow:1290693789824061461>`{address}`\n" +
                       "".join(tx_messages))

    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error fetching transactions:** `{e}`")

import os
import json
import requests
import discord

WALLET_FILE = "wallet.json"

@siddhu.command()
async def mytxhistory(ctx, wallet_num: int):
    """Fetches the last 5 transactions of the user's saved Litecoin address from wallet.json."""

    if wallet_num not in [1, 2, 3]:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **Invalid wallet number! Choose between `1, 2, or 3`.**")
        return

    if not os.path.exists(WALLET_FILE):
        await ctx.send("<:CROSS_TDG:1321149916201881683> **No wallet data found! Use `.createwallet` first.**")
        return

    with open(WALLET_FILE, "r") as file:
        wallet_data = json.load(file)

    if str(wallet_num) not in wallet_data:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Wallet {wallet_num} not found!** Use `.createwallet {wallet_num}` first.")
        return

    address = wallet_data[str(wallet_num)]["address"]

    if address == "Put Here":
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Wallet {wallet_num} has no valid address!** Use `.createwallet {wallet_num}` first.")
        return

    API_URL = f"https://api.blockchair.com/litecoin/dashboards/address/{address}?transaction_details=true"

    try:
        response = requests.get(API_URL)
        data = response.json()

        if "data" not in data or address not in data["data"]:
            await ctx.send("<:CROSS_TDG:1321149916201881683> **Invalid Litecoin address or no transaction history found!**")
            return

        transactions = data["data"][address]["transactions"]

        if not transactions:
            await ctx.send(f"__**LTC TX HISTORY**__ <a:tz_ltc:1281238097136451616>\n"
                           f"**No transactions found for this address!** <a:check:1281246680724930683>\n\n"
                           f"**<:RS_LTC:1291423858183897120> Wallet Number:** `Wallet {wallet_num}`\n"
                           f"**<:RS_LTC:1291423858183897120> Litecoin Address:**\n"
                           f"<:white_arrow:1290693789824061461>`{address}`")
            return

        # Prepare transaction messages
        tx_messages = []
        for tx in transactions[:5]:  # Fetch latest 5 transactions
            tx_id = tx.get("hash", "N/A")
            amount_ltc = round(abs(tx.get("balance_change", 0) / 10**8), 8)  # Convert satoshis to LTC
            amount_usd = round(amount_ltc * 110, 2)  # Approximate USD value (1 LTC = $110)
            is_confirmed = tx.get("is_confirmed", False)
            status = "Confirmed <:lr_tick_1:1290693800808677461>" if is_confirmed else "Unconfirmed <:CROSS_TDG:1321149916201881683>"

            tx_messages.append(f"\n<:rules:1290926829762383934> **Transaction ID: [Click Here](https://blockchair.com/litecoin/transaction/{tx_id})**\n"
                               f"<:exchanger:1322954180452810775> **Amount: {amount_usd}$ [ {amount_ltc} <:LTC:1322611807269031968> ]**\n"
                               f"<:emoji_1738342244745:1334928872269152259> **Status: Confirmed <:Tick:1290693799361777665>**")

        # Send formatted message
        await ctx.send(f"__**LTC TX HISTORY**__ <a:tz_ltc:1281238097136451616>\n"
                       f"**Last {len(tx_messages)} transactions of the address!** <a:check:1281246680724930683>\n\n"
                       f"**<:RS_LTC:1291423858183897120> Wallet Number:** `Wallet {wallet_num}`\n"
                       f"**<:RS_LTC:1291423858183897120> Litecoin Address:**\n"
                       f"<:white_arrow:1290693789824061461>`{address}`\n" +
                       "".join(tx_messages))

    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error fetching transactions:** `{e}`")

import discord
from discord.ext import commands

@siddhu.command()
async def stock(ctx):
    try:
        # Read stock files
        three_month_tokens = len(open('assets/3m_tokens.txt', 'r').read().splitlines())
        one_month_tokens = len(open('assets/1m_tokens.txt', 'r').read().splitlines())

        # Create response message
        message = (
            f"**Nitro Boost Stock:**\n\n"
            f"3 Months Tokens: {three_month_tokens if three_month_tokens > 0 else 'No stock available'}\n"
            f"3 Month Boosts: {three_month_tokens * 2 if three_month_tokens > 0 else 0}\n\n"
            f"1 Month Tokens: {one_month_tokens if one_month_tokens > 0 else 'No stock available'}\n"
            f"1 Month Boosts: {one_month_tokens * 2 if one_month_tokens > 0 else 0}"
        )

        await ctx.send(message)
    except Exception as e:
        await ctx.send(f"Error: {e}")

import discord
from discord.ext import commands

@siddhu.command()
async def restock(ctx, duration: int):
    if duration not in [1, 3]:
        return await ctx.send("Invalid duration! Use `.add_stock 1` or `.add_stock 3`.")

    stock_file = f"assets/{duration}m_tokens.txt"

    if ctx.message.attachments:
        # If a file is attached, download and append its content
        attachment = ctx.message.attachments[0]
        if not attachment.filename.endswith(".txt"):
            return await ctx.send("Please upload a valid `.txt` file with one token per line.")
        
        content = await attachment.read()
        new_tokens = content.decode().splitlines()
    else:
        # If no file is attached, extract tokens from the message
        new_tokens = ctx.message.content.split("\n")[1:]  # Skip the command itself

    if not new_tokens:
        return await ctx.send("No tokens provided!")

    # Save tokens to the stock file
    with open(stock_file, "a") as f:
        f.write("\n".join(new_tokens) + "\n")

    await ctx.send(f"Successfully added `{len(new_tokens)}` tokens to `{duration}-month` stock.")

import discord
from discord.ext import commands
import json
import requests
import asyncio

CAPTCHA_DETECTED_MSG = "Please complete the CAPTCHA to proceed."

@siddhu.command()
async def boost(ctx, duration: int, invite_link: str, num_tokens: int):
    if duration not in [1, 3]:
        return await ctx.send("Invalid duration! Use `.boost 1 <invite_link> <num_of_tokens>` or `.boost 3 <invite_link> <num_of_tokens>`.")

    stock_file = f"assets/{duration}m_tokens.txt"

    try:
        with open(stock_file, "r") as f:
            tokens = f.read().splitlines()
    except FileNotFoundError:
        return await ctx.send(f"No stock found for {duration}-month tokens!")

    if len(tokens) < num_tokens:
        return await ctx.send(f"Not enough tokens available! Only `{len(tokens)}` tokens left.")

    # Load CapMonster API key
    with open("config.json", "r") as f:
        config = json.load(f)

    capmonster_key = config.get("capmonster_api_key")

    successful_boosts = 0
    failed_boosts = 0

    for i in range(num_tokens):
        token = tokens[i]

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        # Join the server using invite link
        invite_code = invite_link.split("/")[-1]
        join_response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)

        if join_response.status_code not in [200, 201]:
            failed_boosts += 1
            continue

        # Attempt to boost
        response = requests.put(
            "https://discord.com/api/v9/users/@me/guilds/premium/subscriptions",
            headers=headers,
            json={"subscription_plan_id": "Nitro Boost"}
        )

        if "captcha_key" in response.text:
            if not capmonster_key:
                return await ctx.send("Captcha occurred while boosting, but no CapMonster API key was found!")

            captcha_solution = solve_captcha(capmonster_key)
            if not captcha_solution:
                failed_boosts += 1
                continue

            # Retry boost with solved captcha
            response = requests.put(
                "https://discord.com/api/v9/users/@me/guilds/premium/subscriptions",
                headers=headers,
                json={"subscription_plan_id": "Nitro Boost", "captcha_key": captcha_solution}
            )

        if response.status_code == 201:
            successful_boosts += 1
        else:
            failed_boosts += 1

        await asyncio.sleep(2)  # Delay to prevent rate limits

    # Remove used tokens from the stock
    remaining_tokens = tokens[num_tokens:]
    with open(stock_file, "w") as f:
        f.write("\n".join(remaining_tokens))

    await ctx.send(f"Boosting complete!\n✅ Successful Boosts: `{successful_boosts * 2}`\n❌ Failed Boosts: `{failed_boosts * 2}`")


def solve_captcha(api_key):
    """
    Solves Discord CAPTCHA using CapMonster API.
    """
    task_data = {
        "clientKey": api_key,
        "task": {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": "https://discord.com",
            "websiteKey": "sitekey_from_discord"
        }
    }

    task_response = requests.post("https://api.capmonster.cloud/createTask", json=task_data).json()
    if "taskId" not in task_response:
        return None

    task_id = task_response["taskId"]

    # Wait for solution
    for _ in range(20):  # Check for 40 seconds
        result = requests.post("https://api.capmonster.cloud/getTaskResult", json={"clientKey": api_key, "taskId": task_id}).json()
        if result.get("status") == "ready":
            return result.get("solution", {}).get("gRecaptchaResponse")
        asyncio.sleep(2)

    return None

import discord
from discord.ext import commands
import json
import requests
import asyncio
import random

@siddhu.command()
async def proxy_boost(ctx, duration: int, invite_link: str, num_tokens: int):
    if duration not in [1, 3]:
        return await ctx.send("Invalid duration! Use `.proxy_boost 1 <invite_link> <num_of_tokens>` or `.proxy_boost 3 <invite_link> <num_of_tokens>`.")

    stock_file = f"assets/{duration}m_tokens.txt"
    proxy_file = "assets/proxies.txt"

    try:
        with open(stock_file, "r") as f:
            tokens = f.read().splitlines()
    except FileNotFoundError:
        return await ctx.send(f"No stock found for {duration}-month tokens!")

    try:
        with open(proxy_file, "r") as f:
            proxies = f.read().splitlines()
    except FileNotFoundError:
        return await ctx.send("No proxies found! Add some proxies in `assets/proxies.txt`.")

    if len(tokens) < num_tokens:
        return await ctx.send(f"Not enough tokens available! Only `{len(tokens)}` tokens left.")

    with open("config.json", "r") as f:
        config = json.load(f)

    capmonster_key = config.get("capmonster_api_key")

    successful_boosts = 0
    failed_boosts = 0

    invite_code = invite_link.split("/")[-1]

    for i in range(num_tokens):
        token = tokens[i]
        proxy = random.choice(proxies) if proxies else None
        proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else None

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        # Join the server
        join_response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, proxies=proxy_dict)

        if join_response.status_code not in [200, 201]:
            failed_boosts += 1
            continue

        # Boost the server
        response = requests.put(
            "https://discord.com/api/v9/users/@me/guilds/premium/subscriptions",
            headers=headers,
            json={"subscription_plan_id": "Nitro Boost"},
            proxies=proxy_dict
        )

        if "captcha_key" in response.text:
            if not capmonster_key:
                return await ctx.send("Captcha occurred while boosting, but no CapMonster API key was found!")

            captcha_solution = solve_captcha(capmonster_key)
            if not captcha_solution:
                failed_boosts += 1
                continue

            # Retry boosting with solved captcha
            response = requests.put(
                "https://discord.com/api/v9/users/@me/guilds/premium/subscriptions",
                headers=headers,
                json={"subscription_plan_id": "Nitro Boost", "captcha_key": captcha_solution},
                proxies=proxy_dict
            )

        if response.status_code == 201:
            successful_boosts += 1
        else:
            failed_boosts += 1

        await asyncio.sleep(2)  # Delay to prevent rate limits

    # Remove used tokens from stock
    remaining_tokens = tokens[num_tokens:]
    with open(stock_file, "w") as f:
        f.write("\n".join(remaining_tokens))

    await ctx.send(f"Proxy Boosting complete!\n✅ Successful Boosts: `{successful_boosts * 2}`\n❌ Failed Boosts: `{failed_boosts * 2}`")


def solve_captcha(api_key):
    task_data = {
        "clientKey": api_key,
        "task": {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": "https://discord.com",
            "websiteKey": "sitekey_from_discord"
        }
    }

    task_response = requests.post("https://api.capmonster.cloud/createTask", json=task_data).json()
    if "taskId" not in task_response:
        return None

    task_id = task_response["taskId"]

    for _ in range(20):  # Check for 40 seconds
        result = requests.post("https://api.capmonster.cloud/getTaskResult", json={"clientKey": api_key, "taskId": task_id}).json()
        if result.get("status") == "ready":
            return result.get("solution", {}).get("gRecaptchaResponse")
        asyncio.sleep(2)

    return None

@siddhu.command()
async def reset_stock(ctx, duration: int):
    if duration not in [1, 3]:
        return await ctx.send("Invalid duration! Use `.reset_stock 1` or `.reset_stock 3`.")

    stock_file = f"assets/{duration}m_tokens.txt"

    try:
        open(stock_file, "w").close()  # Clears the file
        return await ctx.send(f"✅ Successfully cleared {duration}-month stock!")
    except Exception as e:
        return await ctx.send(f"❌ Failed to reset stock: {e}")

import json

@siddhu.command()
async def boost_status(ctx, server_id: int):
    with open("config.json", "r") as f:
        config = json.load(f)
    
    main_token = config.get("main_id_token")
    if not main_token:
        return await ctx.send("❌ No main token found in `config.json`!")

    headers = {"Authorization": main_token}
    response = requests.get(f"https://discord.com/api/v9/guilds/{server_id}", headers=headers)

    if response.status_code == 200:
        data = response.json()
        return await ctx.send(f"Server **{data['name']}** has `{data['premium_subscription_count']}` boosts.")
    else:
        return await ctx.send("❌ Failed to fetch server boost count! Invalid server ID?")

@siddhu.command()
async def check(ctx, token: str):
    headers = {"Authorization": token}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        user = response.json()
        nitro_response = requests.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers)

        if nitro_response.status_code == 200 and len(nitro_response.json()) > 0:
            return await ctx.send(f"✅ Token is **valid** and has **Nitro**.\nUser: {user['username']}#{user['discriminator']}")
        else:
            return await ctx.send(f"⚠️ Token is valid, but does **not** have Nitro!")
    else:
        return await ctx.send("❌ Invalid token!")

@siddhu.command(description="Lists all servers where you have admin permissions.")
async def adminservers(ctx):
    await ctx.send(content="Fetching servers where you have admin permissions...")

    admin_servers = [
        guild.name
        for guild in siddhu.guilds
        if guild.get_member(ctx.author.id).guild_permissions.administrator
    ]

    if not admin_servers:
        return await ctx.send(content="You don't have admin in any server.")

    message = f"""**<:nxt_blue_crown:1281973611917348989> Admin Servers:
<:BadgeDeveloper:1290693804013129768> [Total]: {len(admin_servers)}**

```{', '.join(admin_servers)}
```"""
    await ctx.send(content=message)
    await delete_after_timeout(ctx.message)

@siddhu.command()
async def ltc_webhook(ctx, url: str):
    try:
        # Load current config
        with open("config.json", "r") as f:
            config = json.load(f)

        # Update the webhook URL
        config["ltc_webhook"] = url

        # Save back to config.json
        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)

        await ctx.send(f"<:Tick:1290693799361777665> LTC Webhook URL set successfully: {url}")

    except Exception as e:
        await ctx.send(f"`❌ Error setting LTC Webhook: {e}`")
        logger.error(f"❌ Error setting LTC Webhook: {e}")

@siddhu.command(aliases=["reverseavatar"], description="Reverse searches a user's avatar.")
async def revavatar(ctx, user: discord.User = None):
    user = user or ctx.author  # Defaults to command sender if no user is mentioned

    if not user.avatar:
        return await ctx.send(content=f"{user} has no avatar.")

    avatar_url = user.avatar.url
    reverse_url = f"https://lens.google.com/uploadbyurl?url={avatar_url}"

    await ctx.send(content=f"Reverse Image Search for `{user.display_name}`: {reverse_url}")

import asyncio

autoSlashCommand = False
autoCommand = False

@siddhu.command(description="Automatically runs a slash command every x seconds")
async def autoslashcommand(ctx, command: str = None, delay: int = None):
    await ctx.send(content="Starting autoslashcommand...")

    if not command or not delay:
        await ctx.send(content=":x: | Please specify a command and delay in seconds.")
        await delete_after_timeout(ctx.message)
        return

    try:
        command = int(command)
    except ValueError:
        pass

    slashCommand = None
    async for cmd in ctx.slash_commands():
        if cmd.id == command or cmd.name == command:
            slashCommand = cmd
            break

    if slashCommand is None:
        await ctx.send(content=":x: | Command not found.")
        await delete_after_timeout(ctx.message)
        return

    global autoSlashCommand
    autoSlashCommand = True

    await ctx.send(content="Started autoslashcommand.")
    log_message("autocommand", f"Started autoslashcommand in {ctx.channel.name}.")

    while autoSlashCommand:
        try:
            await slashCommand(ctx)
        except Exception as e:
            await ctx.send(content=f":x: | Failed: {e}")
            autoSlashCommand = False
            await delete_after_timeout(ctx.message)
            return
        await asyncio.sleep(delay)


@siddhu.command(description="Automatically runs a command every x seconds")
async def autocommand(ctx, command: str = None, delay: int = None):
    await ctx.send(content="Starting autocommand...")

    if not command or not delay:
        await ctx.send(content=":x: | Please specify a command and delay in seconds.")
        await delete_after_timeout(ctx.message)
        return

    global autoCommand
    autoCommand = True

    await ctx.send(content="Started autocommand.")
    log_message("autocommand", f"Started autocommand in {ctx.channel.name}.")

    while autoCommand:
        try:
            await ctx.send(command)
        except Exception as e:
            await ctx.send(content=f":x: | Failed: {e}")
            autoCommand = False
            await delete_after_timeout(ctx.message)
            return
        await asyncio.sleep(delay)


@siddhu.command(description="Stops the autoslashcommand")
async def stopautoslashcommand(ctx):
    global autoSlashCommand
    autoSlashCommand = False

    await ctx.send(content="Stopped autoslashcommand.")
    log_message("stopautocommand", f"Stopped autoslashcommand.")
    await delete_after_timeout(ctx.message)


@siddhu.command(description="Stops the autocommand")
async def stopautocommand(ctx):
    global autoCommand
    autoCommand = False

    await ctx.send(content="Stopped autocommand.")
    log_message("stopautocommand", f"Stopped autocommand.")
    await delete_after_timeout(ctx.message)

# 6. Member Count Command
@siddhu.command(aliases=['mc'])
async def membercount(ctx):
    """Get the total number of members in the server."""
    await ctx.send(f"👥 Total members: {ctx.guild.member_count}")

# 7. Boost Count Command
@siddhu.command(aliases=['bc'])
async def boostcount(ctx):
    """Get the number of server boosts."""
    await ctx.send(f"?? Total Boosts: {ctx.guild.premium_subscription_count}")

# 8. Role User Command
@siddhu.command()
async def roleusers(ctx, *, role: discord.Role):
    """List all users with a specific role."""
    users = [member.mention for member in role.members if not member.bot]
    await ctx.send(f"👤 **Users with {role.name}:** {', '.join(users) if users else 'None'}")

# 9. Role Bot Command
@siddhu.command()
async def rolebots(ctx, *, role: discord.Role):
    """List all bots with a specific role."""
    bots = [member.mention for member in role.members if member.bot]
    await ctx.send(f"🤖 **Bots with {role.name}:** {', '.join(bots) if bots else 'None'}")

# 10. Auto React Command
auto_react_emojis = []

@siddhu.command()
async def areact(ctx, *, emojis: str):
    """Set up auto-reactions with custom emojis."""
    global auto_react_emojis
    auto_react_emojis = [emoji.strip() for emoji in emojis.split(',')]
    await ctx.send(f"<:Tick:1290693799361777665> Auto-react set up with: {', '.join(auto_react_emojis)}")

import random
import discord
import asyncio
import chess
import os

@siddhu.command()
async def chessgame(ctx):
    """Play chess with the bot."""
    import chess  # Ensure the correct chess module is imported

    board = chess.Board()
    await ctx.send(f"♟️ Let's play chess! Here's the starting board:\n```\n{board}\n```")

    while not board.is_game_over():
        # Player's Turn
        await ctx.send("Your turn! Make a move (e.g., e2e4):")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            move_msg = await siddhu.wait_for('message', check=check, timeout=300)
            try:
                board.push_san(move_msg.content)
                await ctx.send(f"<:Tick:1290693799361777665> Move accepted! Here's the updated board:\n```\n{board}\n```")
            except ValueError:
                await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid move. Try again.")
                continue
        except asyncio.TimeoutError:
            await ctx.send("⌛ Timeout! Game over.")
            return

        # Bot's Turn
        if not board.is_game_over():
            bot_move = list(board.legal_moves)[0]  # Simple AI: Takes the first legal move
            board.push(bot_move)
            await ctx.send(f"🤖 Bot played: `{board.san(bot_move)}`\n```\n{board}\n```")

    # Game Over
    if board.is_checkmate():
        await ctx.send("🏆 Checkmate! Game over!")
    elif board.is_stalemate():
        await ctx.send("🤝 Stalemate! It's a draw!")
    elif board.is_insufficient_material():
        await ctx.send("🤷 Insufficient material! It's a draw!")

@siddhu.command()
async def chess(ctx, opponent: discord.Member):
    """Play chess with a friend."""
    import chess  # Ensure the correct chess module is imported

    if opponent == ctx.author:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You cannot play chess with yourself!")
        return

    board = chess.Board()  # Initialize a chess board
    current_player = ctx.author  # First player is the command invoker

    await ctx.send(
        f"♟️ **Chess Game Started!**\n"
        f"**{ctx.author.mention} (White)** vs **{opponent.mention} (Black)**\n"
        f"Type your moves in standard chess notation (e.g., `e2e4`).\n"
        f"Here's the starting board:\n```\n{board}\n```"
    )

    def move_check(msg):
        """Check if the message is from the current player and a valid move."""
        return msg.author == current_player and msg.channel == ctx.channel

    while not board.is_game_over():
        try:
            # Request move
            await ctx.send(f"🎮 {current_player.mention}'s turn! Please make a move (e.g., `e2e4`).")
            move_msg = await siddhu.wait_for('message', check=move_check, timeout=300)

            move = move_msg.content.strip()
            try:
                # Validate and apply move
                board.push_uci(move)
                await ctx.send(f"<:Tick:1290693799361777665> Move applied: `{move}`\n```\n{board}\n```")
                current_player = opponent if current_player == ctx.author else ctx.author  # Switch turns
            except ValueError:
                await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid move! Make sure your move is legal.")
        except asyncio.TimeoutError:
            await ctx.send(f"⌛ Timeout! Game over. {current_player.mention} took too long.")
            return

    # Game over: Announce results
    if board.is_checkmate():
        winner = opponent if current_player == ctx.author else ctx.author
        await ctx.send(f"🏆 Checkmate! **{winner.mention}** wins!")
    elif board.is_stalemate():
        await ctx.send("🤝 It's a stalemate! The game is a draw!")
    elif board.is_insufficient_material():
        await ctx.send("🤷 Insufficient material to continue. It's a draw!")
    else:
        await ctx.send("⚠️ Game over. Unknown reason.")
        
# Dictionary to track active chess games by users
active_games = {}

@siddhu.command()
async def chessgamec(ctx):
    """Close the chess game with the bot."""
    try:
        # Check if the user has an active game with the bot
        if ctx.author.id in active_games:
            del active_games[ctx.author.id]
            await ctx.send(f"<:Tick:1290693799361777665> Your chess game with the bot has been closed.")
        else:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> You don't have an active chess game with the bot.")
    except Exception as e:
        await ctx.send(f"⚠️ An error occurred: {e}")

@siddhu.command()
async def chessc(ctx, opponent: discord.Member):
    """Close the chess game with a friend."""
    try:
        # Check if the user or opponent is part of an active game
        if ctx.author.id in active_games and active_games[ctx.author.id] == opponent.id:
            del active_games[ctx.author.id]
            del active_games[opponent.id]
            await ctx.send(f"<:Tick:1290693799361777665> The chess game between you and {opponent.mention} has been closed.")
        elif opponent.id in active_games and active_games[opponent.id] == ctx.author.id:
            del active_games[opponent.id]
            del active_games[ctx.author.id]
            await ctx.send(f"<:Tick:1290693799361777665> The chess game between you and {ctx.author.mention} has been closed.")
        else:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> No active chess game found between you and {opponent.mention}.")
    except Exception as e:
        await ctx.send(f"⚠️ An error occurred: {e}")       

# 2. Tic-Tac-Toe Command
@siddhu.command()
async def tictactoe(ctx, opponent: discord.Member):
    """Play Tic-Tac-Toe with someone."""
    board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe board
    current_player = ctx.author
    current_marker = 'X'
    await ctx.send("🎮 Let's play Tic-Tac-Toe! Type the number of the spot you want to mark (1-9).")

    def check(msg):
        return msg.author == current_player and msg.channel == ctx.channel and msg.content.isdigit()

    while True:
        await ctx.send(f"Board:\n{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}")
        await ctx.send(f"Your turn, {current_player.mention}. Choose a spot to place your marker!")
        move = await siddhu.wait_for('message', check=check)
        move = int(move.content) - 1
        if board[move] == ' ':
            board[move] = current_marker
            if current_marker == 'X':
                current_marker = 'O'
                current_player = opponent
            else:
                current_marker = 'X'
                current_player = ctx.author
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> That spot is already taken! Try again.")
        
        # Check for winner (simple check)
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                await ctx.send(f"🎉 {current_player.mention} wins!")
                return
        if ' ' not in board:
            await ctx.send("The game is a draw!")
            return

# 3. Blackjack Command
@siddhu.command()
async def blackjack(ctx):
    """Play blackjack with the bot."""
    def deal_card():
        """Returns a random card from the deck."""
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return random.choice(cards)

    def calculate_score(cards):
        """Calculate the current score."""
        if 'A' in cards and sum([10 if card == 'A' else int(card) for card in cards]) <= 11:
            return sum([10 if card == 'A' else int(card) for card in cards]) + 10
        return sum([10 if card == 'A' else int(card) for card in cards])

    # Initial deal
    player_cards = [deal_card(), deal_card()]
    bot_cards = [deal_card(), deal_card()]
    await ctx.send(f"Your cards: {player_cards}, Current score: {calculate_score(player_cards)}")
    await ctx.send(f"Bot's cards: {bot_cards[0]} and [hidden]")

    while calculate_score(player_cards) < 21:
        await ctx.send(f"Do you want to 'hit' or 'stand'? (Your score: {calculate_score(player_cards)})")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ['hit', 'stand']
        msg = await siddhu.wait_for('message', check=check)
        
        if msg.content.lower() == 'hit':
            player_cards.append(deal_card())
            await ctx.send(f"You drew: {player_cards[-1]}. Current score: {calculate_score(player_cards)}")
        elif msg.content.lower() == 'stand':
            break

    # Reveal bot cards and calculate final result
    while calculate_score(bot_cards) < 17:
        bot_cards.append(deal_card())

    await ctx.send(f"Bot's final cards: {bot_cards}, Final score: {calculate_score(bot_cards)}")
    
    if calculate_score(player_cards) > 21:
        await ctx.send("💥 You busted! Bot wins!")
    elif calculate_score(bot_cards) > 21 or calculate_score(player_cards) > calculate_score(bot_cards):
        await ctx.send("🎉 You win!")
    elif calculate_score(player_cards) == calculate_score(bot_cards):
        await ctx.send("It's a tie!")
    else:
        await ctx.send("Bot wins!")

# 4. Poker Command (Basic)
@siddhu.command()
async def poker(ctx):
    """Play a simple poker game (start with card drawing)."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    player_cards = random.sample(cards, 2)
    bot_cards = random.sample(cards, 2)
    await ctx.send(f"Your cards: {player_cards}")
    await ctx.send(f"Bot's cards: {bot_cards[0]} and [hidden]")
    await ctx.send("Guess the bot's second card!")

# 5. Hangman Command
@siddhu.command()
async def hangman(ctx):
    """Play a game of Hangman."""
    word = random.choice(["python", "discord", "selfbot", "programming"])
    guessed_letters = []
    remaining_attempts = 6
    await ctx.send(f"🎮 Hangman Game Started! The word has {len(word)} letters.")
    
    while remaining_attempts > 0:
        await ctx.send(f"Guessed so far: {''.join([letter if letter in guessed_letters else '_' for letter in word])}")
        await ctx.send(f"You have {remaining_attempts} attempts left. Guess a letter!")
        
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and len(msg.content) == 1 and msg.content.isalpha()
        
        guess = await siddhu.wait_for('message', check=check)
        
        if guess.content in guessed_letters:
            await ctx.send("<:CROSS_TDG:1321149916201881683> You've already guessed that letter!")
            continue
        
        guessed_letters.append(guess.content)
        
        if guess.content in word:
            await ctx.send(f"<:Tick:1290693799361777665> Correct guess!")
        else:
            remaining_attempts -= 1
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> Incorrect guess. Try again!")

        if all([letter in guessed_letters for letter in word]):
            await ctx.send(f"🎉 You won! The word was: {word}")
            break
        
    if remaining_attempts == 0:
        await ctx.send(f"💥 You lost! The word was: {word}")

import discord
from discord.ext import commands

@siddhu.command()
async def ban_list(ctx):
    """Lists all banned members in the server."""
    bans = await ctx.guild.bans()
    if bans:
        banned_users = [f"**{ban.user}**" for ban in bans]
        await ctx.send("\n".join(banned_users))
    else:
        await ctx.send("No banned members found.")

@siddhu.command()
async def protect_role(ctx, role: discord.Role):
    """Prevents modifications to a specified role."""
    await role.edit(permissions=discord.Permissions.none())
    await ctx.send(f"🛡️ **Role '{role.name}' is now protected!**")

@siddhu.command()
async def unban_all(ctx):
    """Unbans all members in the server."""
    bans = await ctx.guild.bans()
    for ban_entry in bans:
        await ctx.guild.unban(ban_entry.user)
    await ctx.send("🔓 **All users unbanned!**")

@siddhu.command()
async def audit_logs(ctx):
    """Displays the latest server audit logs."""
    logs = await ctx.guild.audit_logs(limit=10).flatten()
    log_list = [f"**{log.user}**: {log.action}" for log in logs]
    await ctx.send("\n".join(log_list))

@siddhu.command()
async def warn_user(ctx, member: discord.Member, *, reason="No reason provided"):
    """Warns a user."""
    await ctx.send(f"⚠️ {member.mention}, you have been warned for: {reason}")

@siddhu.command()
async def view_invites(ctx):
    """Lists all server invites."""
    invites = await ctx.guild.invites()
    invite_list = [f"Code: {invite.code} | Uses: {invite.uses}" for invite in invites]
    await ctx.send("\n".join(invite_list))

@siddhu.command()
async def auto_kick(ctx, days: int):
    """Kicks members inactive for a specified number of days."""
    members = ctx.guild.members
    for member in members:
        if (discord.utils.utcnow() - member.joined_at).days > days:
            await member.kick(reason=f"Inactive for {days} days.")
    await ctx.send(f"👢 **Kicked members inactive for {days} days.**")

@siddhu.command()
async def channel_status(ctx):
    """Shows if the current channel is locked or unlocked."""
    perms = ctx.channel.overwrites_for(ctx.guild.default_role)
    status = "🔒 Locked" if not perms.send_messages else "🔓 Unlocked"
    await ctx.send(f"Channel Status: **{status}**")

@siddhu.command()
async def role_backup(ctx):
    """Creates a backup of all roles and permissions."""
    roles = ctx.guild.roles
    backup = {role.name: role.permissions.value for role in roles}
    with open("roles_backup.json", "w") as f:
        json.dump(backup, f)
    await ctx.send("🔄 **Role backup created.**")

@siddhu.command()
async def restore_roles(ctx):
    """Restores roles from the backup file."""
    try:
        with open("roles_backup.json", "r") as f:
            backup = json.load(f)
        for role_name, perms_value in backup.items():
            await ctx.guild.create_role(name=role_name, permissions=discord.Permissions(perms_value))
        await ctx.send("♻️ **Roles restored.**")
    except FileNotFoundError:
        await ctx.send("No backup found.")

@siddhu.command()
async def dm_all(ctx, *, message):
    """DMs all members in the server."""
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
            except discord.Forbidden:
                pass
    await ctx.send("📩 **Message sent to all members.**")

@siddhu.command()
async def check_permissions(ctx, member: discord.Member = None):
    """Checks the permissions of a member."""
    member = member or ctx.author
    perms = [perm[0] for perm in member.guild_permissions if perm[1]]
    await ctx.send(f"Permissions for {member.mention}: {', '.join(perms)}")

@siddhu.command()
async def message_logs(ctx, member: discord.Member):
    """Fetches the last 10 messages of a user."""
    messages = await ctx.channel.history(limit=100).flatten()
    user_messages = [msg.content for msg in messages if msg.author == member][:10]
    await ctx.send("\n".join(user_messages))

@siddhu.command()
async def disable_invites(ctx):
    """Disables new invites from being created."""
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, create_instant_invite=False)
    await ctx.send("❌ **New invites disabled.**")

@siddhu.command()
async def random_color(ctx):
    """Generates and sends a random color code."""
    import random
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    await ctx.send(f"Random color: {random_color}")

@siddhu.command()
async def emoji_info(ctx, emoji: str):
    """Fetches information about a given emoji."""
    emoji_unicode = ''.join([f"\\u{ord(char):x}" for char in emoji])
    await ctx.send(f"Emoji {emoji} has Unicode representation: {emoji_unicode}")

@siddhu.command()
async def ascii_art(ctx, *, text: str):
    """Generates ASCII art for the given text using pyfiglet."""
    import pyfiglet
    ascii_art = pyfiglet.figlet_format(text)
    await ctx.send(f"```{ascii_art}```")

@siddhu.command()
async def time_difference(ctx, time_zone: str):
    """Returns the current time in a different time zone."""
    from datetime import datetime
    import pytz
    local_time = datetime.now(pytz.timezone(time_zone))
    await ctx.send(f"Current time in {time_zone}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

@siddhu.command()
async def password_strength(ctx, *, password: str):
    """Evaluates the strength of a given password."""
    import re
    strength = "Weak"
    if len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password):
        strength = "Strong"
    await ctx.send(f"Password strength: {strength}")

@siddhu.command()
async def fibonacci(ctx, num: int):
    """Generates a Fibonacci sequence up to the nth number."""
    sequence = [0, 1]
    for i in range(2, num):
        sequence.append(sequence[i-1] + sequence[i-2])
    await ctx.send(f"Fibonacci sequence: {sequence[:num]}")

@siddhu.command()
async def palindrome_check(ctx, *, text: str):
    """Checks if the provided word/phrase is a palindrome, ignoring spaces and case."""
    cleaned_text = ''.join(text.split()).lower()
    if cleaned_text == cleaned_text[::-1]:
        await ctx.send(f"Yes, '{text}' is a palindrome!")
    else:
        await ctx.send(f"No, '{text}' is not a palindrome.")

# Reaction role dictionary to store message id and corresponding emoji-role mapping
reaction_roles = {}

@siddhu.command()
async def reaction_role(ctx, message_id: int):
    """Starts the reaction role process."""
    # Fetch the message
    try:
        message = await ctx.fetch_message(message_id)
    except discord.NotFound:
        await ctx.send("Message not found!")
        return

    # Prompt for the first emoji and role
    await ctx.send("Enter the emoji and role name\nExample: 😀, @role/roleid/rolename")
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    roles = []
    while True:
        try:
            msg = await bot.wait_for('message', timeout=60.0, check=check)
            
            # Break if the user wants to stop adding roles
            if msg.content.lower() == 'none' and len(roles) > 0:
                break
            elif msg.content.lower() == 'none' and len(roles) == 0:
                await ctx.send("Please enter at least one reaction role.")
                continue
            
            # Parse the emoji and role
            try:
                emoji, role_input = msg.content.split(',')
                emoji = emoji.strip()
                role_input = role_input.strip()

                # Handle different formats: role name or role ID
                if role_input.startswith('<@&') and role_input.endswith('>'):
                    role_id = int(role_input[3:-1])  # Extract role ID
                    role = discord.utils.get(ctx.guild.roles, id=role_id)
                else:
                    role = discord.utils.get(ctx.guild.roles, name=role_input)
                
                if not role:
                    await ctx.send(f"Role `{role_input}` not found. Please try again.")
                    continue
            except ValueError:
                await ctx.send("Invalid format. Please enter the emoji and role in the correct format.")
                continue

            # Add the emoji and role to the list
            roles.append((emoji, role))
            await ctx.send(f"Role {role.name} will be assigned when users react with {emoji}.")
            
            # Ask for next emoji-role or 'none' to stop
            if len(roles) == 1:
                await ctx.send("Enter another emoji and role or type `none` to finish.")
            else:
                await ctx.send(f"Enter the next emoji and role (You have added {len(roles)} roles) or type `none` to finish.")

        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            return

    # After collecting all reactions, add them to the message
    for emoji, role in roles:
        # Add reactions to the message
        await message.add_reaction(emoji)

    # Store the roles and their corresponding emojis in the reaction_roles dictionary
    reaction_roles[message_id] = roles
    await ctx.send(f"Setup complete! {len(roles)} reaction roles have been assigned to the message.")

@siddhu.event
async def on_reaction_add(reaction, user):
    """Assigns the role when a user reacts with the specified emoji."""
    if user.bot:
        return  # Ignore reactions from bots

    # Check if the message has reaction roles
    if reaction.message.id in reaction_roles:
        for emoji, role in reaction_roles[reaction.message.id]:
            if str(reaction.emoji) == emoji:
                # Assign the role to the user
                await user.add_roles(role)
                await reaction.message.channel.send(f"{user.mention} has been given the {role.name} role.")

@siddhu.event
async def on_reaction_remove(reaction, user):
    """Removes the role when a user removes their reaction."""
    if user.bot:
        return  # Ignore reactions from bots

    # Check if the message has reaction roles
    if reaction.message.id in reaction_roles:
        for emoji, role in reaction_roles[reaction.message.id]:
            if str(reaction.emoji) == emoji:
                # Remove the role from the user
                await user.remove_roles(role)
                await reaction.message.channel.send(f"{user.mention} has had the {role.name} role removed.")

@siddhu.command()
async def stickynick_reset(ctx):
    """Completely resets all sticky nicknames (wipes the storage)."""
    
    with open("sticky_nicknames.json", "w") as f:
        json.dump({}, f, indent=4)  # Overwrites the file with an empty dictionary

    await ctx.send("✅ **All sticky nicknames have been reset!**")

@siddhu.command()
async def stickynick_disable(ctx, member: discord.Member):
    """Disables sticky nickname for a user (removes from storage but keeps current nickname)."""
    guild_id = str(ctx.guild.id)
    user_id = str(member.id)

    try:
        with open("sticky_nicknames.json", "r") as f:
            sticky_data = json.load(f)
    except FileNotFoundError:
        sticky_data = {}

    if guild_id in sticky_data and user_id in sticky_data[guild_id]:
        del sticky_data[guild_id][user_id]

        with open("sticky_nicknames.json", "w") as f:
            json.dump(sticky_data, f, indent=4)

        await ctx.send(f"Sticky nickname for {member.mention} has been **disabled**.")
    else:
        await ctx.send(f"{member.mention} **does not have a sticky nickname set.**")

@siddhu.command()
async def stickynick(ctx, member: discord.Member, *, nickname: str):
    """Assigns a sticky nickname to a user."""
    guild_id = str(ctx.guild.id)
    user_id = str(member.id)

    # Load sticky nickname data
    sticky_data = {}
    try:
        with open("sticky_nicknames.json", "r") as f:
            sticky_data = json.load(f)
    except FileNotFoundError:
        pass

    # Update nickname
    if guild_id not in sticky_data:
        sticky_data[guild_id] = {}
    sticky_data[guild_id][user_id] = nickname

    with open("sticky_nicknames.json", "w") as f:
        json.dump(sticky_data, f, indent=4)

    await member.edit(nick=nickname)
    await ctx.send(f"Sticky nickname for {member.mention} has been set to `{nickname}`.")

@siddhu.event
async def on_member_update(before, after):
    """Reapply sticky nickname if changed."""
    if before.nick != after.nick:
        try:
            with open("sticky_nicknames.json", "r") as f:
                sticky_data = json.load(f)
            guild_id = str(after.guild.id)
            user_id = str(after.id)
            if guild_id in sticky_data and user_id in sticky_data[guild_id]:
                sticky_nickname = sticky_data[guild_id][user_id]
                if after.nick != sticky_nickname:
                    await after.edit(nick=sticky_nickname)
        except FileNotFoundError:
            pass

from typing import Union

@siddhu.command()
async def add_stock(ctx, product: str):
    await ctx.send(f"📝 **Enter details for `{product}`:**")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await siddhu.wait_for("message", check=check, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("❌ **You took too long! Stock addition canceled.**")
        return

    # Load stock data
    try:
        with open("stock.json", "r") as f:
            stock = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        stock = {}

    stock[product] = msg.content  # Save product details

    # Save updated stock
    with open("stock.json", "w") as f:
        json.dump(stock, f, indent=4)

    await ctx.send(f"✅ **Product `{product}` added successfully!**")

@siddhu.command()
async def stock_list(ctx):
    try:
        with open("stock.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("<:CROSS_TDG:1321149916201881683> **NO STOCK FOUND**")
        return

    if not data:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **NO STOCK FOUND**")
        return

    # Formatting the stock list message
    message = "<:note:1290693795763195945> **STOCK LIST**\n"
    for product, info in data.items():
        message += f"""
<:rdx_glowin_heart:1288196137848803451> **PRODUCT :-** `{product}`
<:white_arrow:1290693789824061461> **INFO :-** {info}
"""

    await ctx.send(message)
    await ctx.message.delete()
    print("[+] stock_list Command Used")

@siddhu.command()
async def send_products(ctx, time_in_sec: int, channel_id: str, *, product_names: str):
    await ctx.message.delete()

    # Fetch the channel
    channel = None
    if channel_id.startswith("<#") and channel_id.endswith(">"):
        channel = siddhu.get_channel(int(channel_id[2:-1]))
    elif channel_id.isdigit():
        channel = siddhu.get_channel(int(channel_id))

    if not channel:
        await ctx.send("❌ **Invalid channel!**")
        return

    # Load stock data
    try:
        with open("stock.json", "r") as f:
            stock = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("❌ **No stock available!**")
        return

    # Extract valid products
    product_list = [p.strip() for p in product_names.split(",")]
    missing = [p for p in product_list if p not in stock]

    if missing:
        await ctx.send(f"❌ **Products not found: {', '.join(missing)}**")
        return

    @tasks.loop(seconds=time_in_sec)
    async def send_selected_products():
        for product in product_list:
            await channel.send(stock[product])  # Send only product details

    send_selected_products.start()
    tasks_dict[channel_id] = send_selected_products

    await ctx.send(f"✅ **Sending selected products every {time_in_sec} seconds!**")

@siddhu.command()
async def send_stock(ctx, time_in_sec: int, channel_id: str):
    await ctx.message.delete()

    # Fetch the channel
    channel = None
    if channel_id.startswith("<#") and channel_id.endswith(">"):
        channel = siddhu.get_channel(int(channel_id[2:-1]))
    elif channel_id.isdigit():
        channel = siddhu.get_channel(int(channel_id))

    if not channel:
        await ctx.send("❌ **Invalid channel!**")
        return

    # Load stock data
    try:
        with open("stock.json", "r") as f:
            stock = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("❌ **No stock available!**")
        return

    @tasks.loop(seconds=time_in_sec)
    async def send_all_stock():
        for details in stock.values():
            await channel.send(details)  # Send only product details

    send_all_stock.start()
    tasks_dict[channel_id] = send_all_stock

    await ctx.send(f"✅ **Sending all stock every {time_in_sec} seconds!**")

@siddhu.command()
async def clear_stock(ctx):
    with open("stock.json", "w") as f:
        json.dump({}, f, indent=4)

    await ctx.send("✅ **All stock cleared successfully!**")

@siddhu.command()
async def remove_product(ctx, product: str):
    try:
        with open("stock.json", "r") as f:
            stock = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("❌ **Stock is empty!**")
        return

    if product in stock:
        del stock[product]

        with open("stock.json", "w") as f:
            json.dump(stock, f, indent=4)

        await ctx.send(f"✅ **Product `{product}` removed successfully!**")
    else:
        await ctx.send("❌ **Product not found in stock!**")

@siddhu.command()
async def stop_sending(ctx, channel: discord.TextChannel | int):
    channel_id = channel.id if isinstance(channel, discord.TextChannel) else channel

    if channel_id in tasks_dict:
        if "products" in tasks_dict[channel_id]:
            tasks_dict[channel_id]["products"].cancel()
            del tasks_dict[channel_id]["products"]
            await ctx.send(f"<:rdx_glowin_heart:1288196137848803451> **Stopped sending products in <#{channel_id}>**")
            return

        if "stock" in tasks_dict[channel_id]:
            tasks_dict[channel_id]["stock"].cancel()
            del tasks_dict[channel_id]["stock"]
            await ctx.send(f"<:rdx_glowin_heart:1288196137848803451> **Stopped sending stock in <#{channel_id}>**")
            return

    await ctx.send("<:white_arrow:1290693789824061461> **No active stock or product sending task found for this channel.**")

@siddhu.command()
async def typing_race(ctx):
    """Starts a typing race."""
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Discord bots are fun to create!",
        "Python is a versatile programming language.",
        "Speed typing can be challenging but exciting.",
        "Always aim for accuracy before speed."
    ]

    sentence = random.choice(sentences)
    await ctx.send(f"Typing race started! Type the following sentence as fast as you can:\n\n`{sentence}`")

    def check(message):
        return message.channel == ctx.channel and message.content == sentence

    try:
        start_time = time.time()
        msg = await ctx.bot.wait_for("message", check=check, timeout=30)
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        await ctx.send(f"Congratulations {msg.author.mention}! You completed the race in {time_taken} seconds.")
    except asyncio.TimeoutError:
        await ctx.send("Time's up! Nobody completed the race.")

import json
import discord

# Load welcome settings into memory at startup
WELCOME_FILE = "welcome_messages.json"

def load_welcome_data():
    try:
        with open(WELCOME_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_welcome_data(data):
    with open(WELCOME_FILE, "w") as f:
        json.dump(data, f, indent=4)

welcome_data = load_welcome_data()  # Keep data in memory

@siddhu.command()
async def set_welcome(ctx, channel: discord.TextChannel, *, message: str):
    """Sets a custom welcome message for a specific channel."""
    guild_id = str(ctx.guild.id)

    welcome_data[guild_id] = {"channel_id": channel.id, "message": message}
    save_welcome_data(welcome_data)

    await ctx.send(f"✅ Welcome message set for {channel.mention}:\n`{message}`")

@siddhu.command()
async def disable_welcome(ctx):
    """Disables the welcome message for the server."""
    guild_id = str(ctx.guild.id)

    if guild_id in welcome_data:
        del welcome_data[guild_id]
        save_welcome_data(welcome_data)
        await ctx.send("🚫 Welcome messages have been **disabled** for this server.")
    else:
        await ctx.send("⚠️ There is no welcome message set.")

@siddhu.event
async def on_member_join(member):
    """Send a custom welcome message when a member joins."""
    guild_id = str(member.guild.id)

    if guild_id not in welcome_data:
        return  # No welcome message set

    channel_id = welcome_data[guild_id]["channel_id"]
    message = welcome_data[guild_id]["message"]
    channel = member.guild.get_channel(channel_id)

    if channel is None:
        # If channel is deleted, remove the entry
        del welcome_data[guild_id]
        save_welcome_data(welcome_data)
        return

    try:
        # Replace placeholders with actual values
        welcome_message = (
            message.replace("{user}", member.mention)
                   .replace("{server}", member.guild.name)
                   .replace("{count}", str(member.guild.member_count))
        )
        await channel.send(welcome_message)
    except discord.Forbidden:
        await member.guild.owner.send(f"⚠️ I don't have permission to send messages in {channel.mention}. Fix this to enable welcome messages.")
    except discord.HTTPException as e:
        print(f"Error sending welcome message: {e}")

@siddhu.command()
async def draw_square(ctx, size: int):
    """Draws a square using ASCII characters."""
    square = '\n'.join(['*' * size for _ in range(size)])
    await ctx.send(f"```\n{square}\n```")

@siddhu.command()
async def square_number(ctx, number: int):
    """Returns the square of the given number."""
    await ctx.send(f"The square of {number} is {number ** 2}.")

@siddhu.command()
async def generate_uuid(ctx):
    """Generates a random UUID."""
    import uuid
    generated_uuid = str(uuid.uuid4())
    await ctx.send(f"Generated UUID: {generated_uuid}")

@siddhu.command()
async def string_length(ctx, *, text: str):
    """Returns the length of the provided string."""
    await ctx.send(f"The length of '{text}' is {len(text)} characters.")

@siddhu.command()
async def url_encode(ctx, *, text: str):
    """Encodes the given text as a URL-safe string."""
    from urllib.parse import quote
    encoded_text = quote(text)
    await ctx.send(f"Encoded URL: {encoded_text}")

@siddhu.command()
async def url_decode(ctx, *, text: str):
    """Decodes a URL-encoded string."""
    from urllib.parse import unquote
    decoded_text = unquote(text)
    await ctx.send(f"Decoded URL: {decoded_text}")

@siddhu.command()
async def anagram(ctx, *, word: str):
    """Checks if the given word has any anagrams (by rearranging letters)."""
    from itertools import permutations
    anagrams = set(''.join(p) for p in permutations(word))
    await ctx.send(f"Possible anagrams for '{word}': {', '.join(anagrams)}")

@siddhu.command()
async def convert_to_hex(ctx, *, text: str):
    """Converts the given text to its hexadecimal representation."""
    hex_representation = ' '.join([hex(ord(char)) for char in text])
    await ctx.send(f"Hexadecimal representation: {hex_representation}")

@siddhu.command()
async def check_palindrome(ctx, *, text: str):
    """Checks if a string is a palindrome (ignores case and spaces)."""
    normalized_text = ''.join(text.split()).lower()
    if normalized_text == normalized_text[::-1]:
        await ctx.send(f"'{text}' is a palindrome!")
    else:
        await ctx.send(f"'{text}' is not a palindrome.")

@siddhu.command()
async def generate_password(ctx):
    """Generates a random secure password."""
    import random
    import string
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    await ctx.send(f"Generated password: {password}")

# 6. Quotes Command
@siddhu.command()
async def quotes(ctx):
    """Get a random famous quote."""
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson"
    ]
    await ctx.send(f"💬 {random.choice(quotes)}")

# Would You Rather
@siddhu.command()
async def wyr(ctx):
    """Would you rather question."""
    questions = [
    "Would you rather explore space or the deep ocean?",
    "Would you rather have unlimited money or unlimited time?",
    "Would you rather always tell the truth or always have to lie?",
    "Would you rather lose your ability to read or your ability to speak?",
    "Would you rather teleport anywhere or read minds?",
    "Would you rather be famous for something bad or never be recognized for something good?",
    "Would you rather live in the past or the future?",
    "Would you rather have super strength or super speed?",
    "Would you rather never be able to eat your favorite food again or only eat your favorite food forever?",
    "Would you rather have no one show up at your wedding or at your funeral?",
    "Would you rather be able to control fire or water?",
    "Would you rather live without music or live without movies?",
    "Would you rather have the power to heal yourself or heal others?",
    "Would you rather live in a world without video games or without social media?",
    "Would you rather be a great artist or a great scientist?",
    "Would you rather have the ability to talk to animals or the ability to speak every language?",
    "Would you rather live in a tiny house in a big city or a mansion in the countryside?",
    "Would you rather only be able to whisper or only be able to shout?",
    "Would you rather spend a year in jail or lose a year of your life?",
    "Would you rather never get sick or never feel tired?",
    "Would you rather have an extra hour every day or an extra day every month?",
    "Would you rather always feel too hot or always feel too cold?",
    "Would you rather be able to see 10 minutes into the future or 100 years into the past?",
    "Would you rather live in a world where nobody lies or nobody argues?",
    "Would you rather be able to remember everything you read or everything you hear?",
    "Would you rather have unlimited free travel or free food for life?",
    "Would you rather have one wish granted today or three wishes granted 10 years from now?",
    "Would you rather be the smartest person in the room or the funniest?",
    "Would you rather live in a world with no crime or no poverty?",
    "Would you rather always know what time it is or always have exact change?"
    ]
    await ctx.send(f"🤔 {random.choice(questions)}")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = "8f5d428943fe4a04b9ef9458d5b857b1"  # Replace with your Client ID
SPOTIFY_CLIENT_SECRET = "f024984148a84b48af0010f52fa9a796"  # Replace with your Client Secret

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

@siddhu.command()
async def spotify(ctx, *, search: str):
    """Search for a song on Spotify."""
    try:
        # Search Spotify for the song
        results = sp.search(q=search, limit=1, type="track")
        if not results['tracks']['items']:
            await ctx.send(f"No results found for '{search}' on Spotify.")
            return

        track = results['tracks']['items'][0]
        song_name = track['name']
        artist_name = ", ".join(artist['name'] for artist in track['artists'])
        album_name = track['album']['name']
        release_date = track['album']['release_date']
        spotify_url = track['external_urls']['spotify']

        # Send song details
        await ctx.send(
            f"🎶 **Spotify Search Result**\n"
            f"**Title:** {song_name}\n"
            f"**Artist(s):** {artist_name}\n"
            f"**Album:** {album_name}\n"
            f"**Release Date:** {release_date}\n"
            f"**Spotify URL:** {spotify_url}"
        )
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

GENIUS_API_TOKEN = "CUoWqOreeoA6KdGApGFvoBR44M6kpZF1-egdqGKmk0ew9J15maO0q7Vbeoz8yiix"  # Replace with your Genius API token

@siddhu.command()
async def lyrics(ctx, *, song_name: str):
    """Fetch lyrics for a song using Genius API."""
    if not song_name:
        await ctx.send("Please provide a song name!")
        return

    search_url = f"https://api.genius.com/search?q={song_name}"
    headers = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        results = response.json().get('response', {}).get('hits', [])
        if results:
            # Get the first result's lyrics URL
            lyrics_url = results[0]['result']['url']
            song_title = results[0]['result']['title']
            artist_name = results[0]['result']['primary_artist']['name']
            await ctx.send(f"🎶 Lyrics for **{song_title}** by **{artist_name}**: {lyrics_url}")
        else:
            await ctx.send(f"No lyrics found for '{song_name}'!")
    else:
        await ctx.send(f"Error: Unable to fetch lyrics. Status Code: {response.status_code}")

@siddhu.command(name="tznick")
async def tznick(ctx, user: discord.Member):
    """
    Change a user's nickname to '𝐓𝐙 | {nickname}'.
    Usage: .tznick @user/username/userid
    """
    try:
        # Preserve their existing nickname or use their username if none
        old_nick = user.nick if user.nick else user.name
        new_nick = f"𝐓𝐙 | {old_nick}"

        # Check if the nickname is already set
        if user.nick == new_nick:
            return await ctx.send(f"<:CROSS_TDG:1321149916201881683> **{user.display_name} already has the TZ tag!**")

        # Change nickname
        await user.edit(nick=new_nick)
        await ctx.send(f"<a:check:1114602452319211560> **Nickname updated:** `{new_nick}`")

    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **I don't have permission to change that user's nickname!**")
    except discord.HTTPException:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **Failed to change the nickname. Try again!**")

# Random Dog Image
@siddhu.command()
async def dog(ctx):
    """Get a random dog picture."""
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        await ctx.send(response.json()['message'])
    else:
        await ctx.send("Failed to fetch a dog picture!")

# Random Fact
@siddhu.command()
async def fact(ctx):
    """Send a random fact."""
    facts = [
    "Honey never spoils.",
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "Sharks existed before trees.",
    "The Eiffel Tower can grow more than six inches during summer.",
    "Some turtles can breathe through their butts.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Sloths can hold their breath longer than dolphins.",
    "A cloud can weigh more than a million pounds.",
    "Hot water freezes faster than cold water under certain conditions.",
    "Wombat poop is cube-shaped.",
    "A blue whale's heart weighs as much as a small car.",
    "Humans share about 60% of their DNA with bananas.",
    "Bees can recognize human faces.",
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "There are more trees on Earth than stars in the Milky Way galaxy.",
    "Koalas have fingerprints that are nearly identical to humans.",
    "It rains diamonds on Jupiter and Saturn.",
    "Butterflies can taste with their feet.",
    "Ants never sleep.",
    "A snail can sleep for three years at a time.",
    "The shortest war in history lasted 38 to 45 minutes.",
    "Elephants are the only animals that cannot jump.",
    "The human brain generates more electrical impulses in a day than all the telephones in the world.",
    "Cows have best friends and get stressed when separated.",
    "Venus is the hottest planet in the solar system, even though Mercury is closer to the Sun.",
    "A cockroach can live for weeks without its head before dying of starvation.",
    "The inventor of the Pringles can is buried in one.",
    "Polar bears have black skin under their white fur.",
    "Humans are the only animals that blush.",
    "The Guinness World Record for the longest hiccuping spree is 68 years.",
    "An octopus has three hearts and blue blood.",
    "There’s a species of jellyfish that can live forever.",
    "The first oranges weren’t orange—they were green.",
    "The heart of a shrimp is located in its head.",
    "Your body has enough iron to make a nail.",
    "Cats can’t taste sweetness.",
    "A group of flamingos is called a 'flamboyance.'",
    "There’s a planet where it rains molten glass sideways.",
    "Avocados were named after the Nahuatl word for 'testicle.'",
    "Rabbits can’t vomit.",
    "Banging your head against a wall burns 150 calories an hour.",
    "The inventor of Vaseline ate a spoonful of it every day.",
    "The human nose can detect over a trillion different smells.",
    "Alaska is the westernmost, easternmost, and northernmost state in the U.S.",
    "Water can boil and freeze at the same time under certain conditions.",
    "A day on Uranus lasts 17 hours, but its year lasts 84 Earth years.",
    "A single strand of spider silk is thinner than a human hair but five times stronger than steel of the same width."
    ]
    await ctx.send(f"🧠 Did you know? {random.choice(facts)}")

# Slowmode Command
@siddhu.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    """Set slowmode for a channel"""
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set slowmode to {seconds} seconds.")

import asyncio

@siddhu.command()
async def tempban(ctx, member: discord.Member, duration: int, *, reason=None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"# ⏳ Temporarily banned `{member}` for `{duration}` seconds\n> Reason: {reason or 'No reason'}")
    await asyncio.sleep(duration)
    await ctx.guild.unban(member)
    await ctx.send(f"# ✅ `{member}` has been unbanned (tempban expired)")

@siddhu.command()
async def softban(ctx, member: discord.Member, *, reason=None):
    await ctx.guild.ban(member, reason=reason)
    await ctx.guild.unban(member, reason="Softban (messages deleted)")
    await ctx.send(f"# 🔨 Softbanned `{member}`\n> Reason: {reason or 'No reason provided'}")

@siddhu.command()
async def set_userid(ctx, user_id: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['User_Id'] = User_Id
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> User ID updated to {user_id}")

@siddhu.command()
async def set_password(ctx, password: str):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['Password'] = password
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"<:Tick:1290693799361777665> Password updated to {password}")
    
@siddhu.command()
async def set_address(ctx, wallet_num: str = None, address: str = None):
    if wallet_num is None:
        await ctx.send("Enter the Wallet number :-")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await siddhu.wait_for("message", check=check)
        wallet_num = msg.content

    if wallet_num not in ["1", "2", "3"]:
        await ctx.send("Invalid Wallet number. Please enter 1, 2, or 3.")
        return

    if address is None:
        await ctx.send("Enter the new address :-")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await siddhu.wait_for("message", check=check)
        address = msg.content

    with open('wallet.json', 'r+') as f:
        data = json.load(f)
        data[wallet_num]['address'] = address
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"Address for Wallet {wallet_num} updated to {address}")

@siddhu.command()
async def set_privatekey(ctx, wallet_num: str = None, private_key: str = None):
    if wallet_num is None:
        await ctx.send("Enter the Wallet number :-")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await siddhu.wait_for("message", check=check)
        wallet_num = msg.content

    if wallet_num not in ["1", "2", "3"]:
        await ctx.send("Invalid Wallet number. Please enter 1, 2, or 3.")
        return

    if private_key is None:
        await ctx.send("Enter the new private key :-")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        msg = await siddhu.wait_for("message", check=check)
        private_key = msg.content

    with open('wallet.json', 'r+') as f:
        data = json.load(f)
        data[wallet_num]['private_key'] = private_key
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    await ctx.send(f"Private key for Wallet {wallet_num} updated to {private_key}")
    
import json
import os

def save_presence_status(status: str):
    config = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                config = {}

    config['presence_status'] = status.lower()

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

@siddhu.command()
async def change_presence(ctx, status: str):
    statuses = {
        "online": discord.Status.online,
        "idle": discord.Status.idle,
        "dnd": discord.Status.dnd,
        "offline": discord.Status.offline
    }
    
    if status.lower() in statuses:
        await siddhu.change_presence(status=statuses[status.lower()])
        save_presence_status(status)
        await ctx.send(f"Presence changed to {status}!")
    else:
        await ctx.send("Invalid status! Use online, idle, dnd, or offline.")
        
@siddhu.command()
async def role(ctx, member: discord.Member, role: discord.Role):

    await member.add_roles(role)

    await ctx.send(f"{member.mention} has been given the {role.mention} role.")
  
import asyncio

@siddhu.command()
async def ban_all(ctx):
    if not ctx.guild:
        await ctx.send("<:CROSS_TDG:1321149916201881683> This command can only be used in a server.")
        return

    banned_count = 0
    failed_count = 0

    await ctx.send("⏳ Starting to ban all members...")

    for member in ctx.guild.members:
        if member.id == ctx.author.id:
            continue  # Skip yourself

        try:
            await ctx.guild.ban(member, reason="Mass ban via selfbot")
            banned_count += 1
            await asyncio.sleep(1.5)  # Essential delay to avoid rate limit
        except Exception as e:
            failed_count += 1
            print(f"❌ Failed to ban {member} - {e}")

    await ctx.send(f"<:Tick:1290693799361777665> Banned {banned_count} members.\n<:CROSS_TDG:1321149916201881683> Failed: {failed_count}")
        
import asyncio

@siddhu.command()
async def kick_all(ctx):
    if not ctx.guild:
        await ctx.send("<:CROSS_TDG:1321149916201881683> This command can only be used in a server.")
        return

    kicked_count = 0
    failed_count = 0

    await ctx.send("⏳ Starting to kick all members...")

    for member in ctx.guild.members:
        if member.id == ctx.author.id:
            continue  # Skip yourself

        try:
            await ctx.guild.kick(member, reason="Mass kick via selfbot")
            kicked_count += 1
            await asyncio.sleep(1.5)  # Delay to prevent rate limits
        except Exception as e:
            failed_count += 1
            print(f"❌ Failed to kick {member}: {e}")

    await ctx.send(f"<:Tick:1290693799361777665> Kicked {kicked_count} members.\n<:CROSS_TDG:1321149916201881683> Failed to kick {failed_count} members.")

@siddhu.command()
async def cwebhookall(ctx, webhook_name: str):
    """Spam all text channels in the server with webhooks."""
    await ctx.send(
        "**<:Discord_bots:1290700055514452121> SELECT WHICH TYPE OF MESSAGE YOU WANT TO SPAM :-**\n"
        "```[+] NORMAL MESSAGE - 1\n[+] EMBED MESSAGE - 2\n[+] NORMAL + EMBED - 3```\n"
        "<:white_arrow:1290693789824061461>**SELECT FROM 1, 2, OR 3**\n"
        "<:white_arrow:1290693789824061461>**THIS CMD MAY HIT RATE LIMITS!**"
    )

    try:
        # Wait for the user to select the spam type
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in ["1", "2", "3"]

        response = await siddhu.wait_for("message", check=check, timeout=30)

        embed_title, embed_description = None, None

        # Handle different spam types
        if response.content == "1":  # Normal message
            await ctx.send("**Enter the normal message you want to spam:**")
            normal_spam_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)

        elif response.content == "2":  # Embed message
            await ctx.send("**Enter the embed title:**")
            embed_title_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
            embed_title = embed_title_msg.content

            await ctx.send("**Enter the embed description:**")
            embed_description_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
            embed_description = embed_description_msg.content

        elif response.content == "3":  # Normal + Embed message
            await ctx.send("**Enter the normal message you want to spam:**")
            normal_spam_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)

            await ctx.send("**Enter the embed title:**")
            embed_title_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
            embed_title = embed_title_msg.content

            await ctx.send("**Enter the embed description:**")
            embed_description_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30)
            embed_description = embed_description_msg.content

        # Loop through all text channels in the server
        channels = ctx.guild.text_channels
        webhooks = []

        # Create webhooks for all channels
        for channel in channels:
            try:
                webhook = await channel.create_webhook(name=webhook_name)
                webhooks.append(webhook)
            except discord.Forbidden:
                print(f"Failed to create webhook in channel {channel.name}: Missing permissions")
            except discord.HTTPException as e:
                print(f"Failed to create webhook in channel {channel.name}: {e.text}")

        # Spam messages in all webhooks, 5 messages per channel, 20 repetitions
        for _ in range(20):  # Repeat 20 times
            for webhook, channel in zip(webhooks, channels):
                try:
                    for _ in range(5):  # Send 5 messages in each iteration
                        if response.content == "1":  # Normal message
                            await webhook.send(normal_spam_msg.content)
                        elif response.content == "2":  # Embed message
                            embed = discord.Embed(
                                title=embed_title,
                                description=embed_description,
                                color=discord.Color.red()
                            )
                            await webhook.send(embed=embed)
                        elif response.content == "3":  # Normal + Embed
                            embed = discord.Embed(
                                title=embed_title,
                                description=embed_description,
                                color=discord.Color.red()
                            )
                            await webhook.send(content=normal_spam_msg.content, embed=embed)
                    print(f"Spammed channel {channel.name} (5 messages)")
                except discord.Forbidden:
                    print(f"Failed to send messages in channel {channel.name}: Missing permissions")
                except discord.HTTPException as e:
                    print(f"Failed to send messages in channel {channel.name}: {e.text}")
            await asyncio.sleep(1)  # Short delay to prevent rate-limiting

        await ctx.send("<:Tick:1290693799361777665> Spamming complete!")

    except asyncio.TimeoutError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You took too long to respond!")

@siddhu.command()
async def ping(ctx):
    await ctx.send(f'<:Download:1290692089272733768> Ping Latency ! {round(siddhu.latency * 1000)}ms')

import datetime

# Set bot start time when script starts
siddhu.start_time = datetime.datetime.now()

@siddhu.command()
async def uptime(ctx):
    uptime = datetime.datetime.now() - siddhu.start_time
    days = uptime.days
    hours = uptime.seconds // 3600
    minutes = (uptime.seconds // 60) % 60
    seconds = uptime.seconds % 60
    await ctx.send(f'<:Discord_bots:1290700055514452121> Uptime: {days}d {hours}h {minutes}m {seconds}s')  
    
@siddhu.command()
async def webhook_spam(ctx, webhook_url: str, amount: int):
    if not ctx or not ctx.channel:
        print("Invalid ctx object")
        return

    try:
        # Prompt user to select spam type
        await ctx.send(
            "**<:Discord_bots:1290700055514452121> SELECT WHICH TYPE OF MESSAGE YOU WANT TO SPAM :-**\n"
            "```[+] NORMAL MESSAGE - 1\n[+] EMBED MESSAGE - 2\n[+] NORMAL + EMBED - 3```"
            "\n<:white_arrow:1290693789824061461>**SELECT FROM 1,2 OR 3**\n"
            "<:white_arrow:1290693789824061461>**THIS CMD MAY HIT RATE LIMITS !**"
        )

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Wait for the user's choice
        user_choice = await siddhu.wait_for('message', check=check, timeout=30)

        # Process user's choice
        if user_choice.content == "1":
            await ctx.send("**Enter the message you want to spam:**")
            normal_msg = await siddhu.wait_for('message', check=check, timeout=30)
            message = normal_msg.content

            # Normal message spam
            webhook = discord.Webhook.from_url(webhook_url, adapter=discord.RequestsWebhookAdapter())
            for i in range(amount):
                try:
                    webhook.send(content=message)
                    print(f"Sent message {message} ({i + 1}/{amount})")
                    await asyncio.sleep(0.5)  # Add a delay
                except discord.HTTPException as e:
                    print(f"Failed to send message: {e.text}")
                    break

        elif user_choice.content == "2":
            await ctx.send("**Enter the title of the embed:**")
            embed_title = await siddhu.wait_for('message', check=check, timeout=30)
            await ctx.send("**Enter the description of the embed:**")
            embed_description = await siddhu.wait_for('message', check=check, timeout=30)

            # Embed message spam
            webhook = discord.Webhook.from_url(webhook_url, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(
                title=embed_title.content,
                description=embed_description.content,
                color=discord.Color.red(),
            )
            for i in range(amount):
                try:
                    webhook.send(embed=embed)
                    print(f"Sent embed ({i + 1}/{amount})")
                    await asyncio.sleep(0.5)  # Add a delay
                except discord.HTTPException as e:
                    print(f"Failed to send embed: {e.text}")
                    break

        elif user_choice.content == "3":
            await ctx.send("**Enter the normal message you want to spam:**")
            normal_msg = await siddhu.wait_for('message', check=check, timeout=30)
            message = normal_msg.content

            await ctx.send("**Enter the title of the embed:**")
            embed_title = await siddhu.wait_for('message', check=check, timeout=30)
            await ctx.send("**Enter the description of the embed:**")
            embed_description = await siddhu.wait_for('message', check=check, timeout=30)

            # Normal + Embed message spam
            webhook = discord.Webhook.from_url(webhook_url, adapter=discord.RequestsWebhookAdapter())
            embed = discord.Embed(
                title=embed_title.content,
                description=embed_description.content,
                color=discord.Color.red(),
            )
            for i in range(amount):
                try:
                    webhook.send(content=message, embed=embed)
                    print(f"Sent normal message + embed ({i + 1}/{amount})")
                    await asyncio.sleep(0.5)  # Add a delay
                except discord.HTTPException as e:
                    print(f"Failed to send normal message + embed: {e.text}")
                    break
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid choice. Operation cancelled.")

        await ctx.send("<:Tick:1290693799361777665> Spamming complete!")
    except asyncio.TimeoutError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You took too long to respond. Operation cancelled.")
    except Exception as e:
        print(f"Error: {e}")
    
@siddhu.command()
async def destroy(ctx, *, args):
    """Destroys a server by creating channels and spamming webhooks."""
    args = args.split(', ')
    if len(args) != 3:
        await ctx.send("Invalid arguments. Please use the format: `.destroy channel_name, webhook_name, number_of_channels`")
        return

    channel_name, webhook_name, channel_amount = args

    try:
        channel_amount = int(channel_amount)
        if channel_amount <= 0:
            await ctx.send("The number of channels must be greater than 0.")
            return
    except ValueError:
        await ctx.send("Invalid number of channels. Please provide a valid integer.")
        return

    # Ensure the current channel where the command is used is not deleted
    current_channel = ctx.channel

    # Check permissions
    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I don't have permission to manage channels.")
        return

    # Prompt to select spam type
    await ctx.send(
        "**<:Discord_bots:1290700055514452121> SELECT WHICH TYPE OF MESSAGE YOU WANT TO SPAM :-**\n"
        "```[+] NORMAL MESSAGE - 1\n[+] EMBED MESSAGE - 2\n[+] NORMAL + EMBED - 3```\n"
        "<:white_arrow:1290693789824061461>**SELECT FROM 1,2 OR 3**\n"
        "<:white_arrow:1290693789824061461>**THIS CMD MAY HIT RATE LIMITS!**"
    )

    try:
        # Wait for the user to select the spam type
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content in ["1", "2", "3"]

        response = await siddhu.wait_for("message", check=check, timeout=60)

        embed_title, embed_description = None, None

        # Handle different spam types
        if response.content == "1":  # Normal message
            await ctx.send("**Enter the normal message you want to spam:**")
            normal_spam_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)

        elif response.content == "2":  # Embed message
            await ctx.send("**Enter the embed title:**")
            embed_title_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)
            embed_title = embed_title_msg.content

            await ctx.send("**Enter the embed description:**")
            embed_description_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)
            embed_description = embed_description_msg.content

        elif response.content == "3":  # Normal + Embed message
            await ctx.send("**Enter the normal message you want to spam:**")
            normal_spam_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)

            await ctx.send("**Enter the embed title:**")
            embed_title_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)
            embed_title = embed_title_msg.content

            await ctx.send("**Enter the embed description:**")
            embed_description_msg = await siddhu.wait_for("message", check=lambda m: m.author == ctx.author, timeout=60)
            embed_description = embed_description_msg.content

        # Confirm before starting the destroy process
        await ctx.send(
            f"**Are you sure you want to destroy the server by creating {channel_amount} channels and spamming webhooks?**"
            " Respond with `yes` to proceed."
        )

        try:
            def confirm_check(m):
                return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == "yes"

            confirm_response = await siddhu.wait_for("message", check=confirm_check, timeout=60)

            # Delete all channels except the current channel
            await ctx.send("**Deleting all channels and categories...**")
            for channel in ctx.guild.text_channels:
                if channel != current_channel:
                    try:
                        await channel.delete()
                    except discord.Forbidden:
                        pass
                    except discord.HTTPException:
                        pass

            for channel in ctx.guild.voice_channels:
                try:
                    await channel.delete()
                except discord.Forbidden:
                    pass
                except discord.HTTPException:
                    pass

            for category in ctx.guild.categories:
                try:
                    await category.delete()
                except discord.Forbidden:
                    pass
                except discord.HTTPException:
                    pass

            # Create the specified number of channels
            await ctx.send(f"**Creating {channel_amount} channels...**")
            created_channels = []
            for i in range(channel_amount):
                try:
                    channel = await ctx.guild.create_text_channel(name=channel_name)
                    created_channels.append(channel)
                    await asyncio.sleep(0.5)  # Delay to prevent rate limiting
                except discord.Forbidden:
                    await ctx.send(f"Failed to create channel {channel_name}: Missing permissions.")
                    return
                except discord.HTTPException as e:
                    await ctx.send(f"HTTP Exception: Unable to create channel. {e.text}")
                    break

            # Spam webhooks in created channels
            webhooks = []
            for channel in created_channels:
                try:
                    webhook = await channel.create_webhook(name=webhook_name)
                    webhooks.append(webhook)
                except discord.Forbidden:
                    await ctx.send(f"Failed to create webhook in channel {channel.name}: Missing permissions.")

            # Send 5 messages per webhook, 20 repetitions
            for _ in range(20):
                for webhook in webhooks:
                    try:
                        for _ in range(5):  # Send 5 messages per channel per iteration
                            if response.content == "1":  # Normal message
                                await webhook.send(normal_spam_msg.content)
                            elif response.content == "2":  # Embed message
                                embed = discord.Embed(
                                    title=embed_title,
                                    description=embed_description,
                                    color=discord.Color.red()
                                )
                                await webhook.send(embed=embed)
                            elif response.content == "3":  # Normal + Embed
                                embed = discord.Embed(
                                    title=embed_title,
                                    description=embed_description,
                                    color=discord.Color.red()
                                )
                                await webhook.send(content=normal_spam_msg.content, embed=embed)
                    except discord.Forbidden:
                        await ctx.send(f"Failed to send messages in webhook.")
                    except discord.HTTPException:
                        await ctx.send(f"HTTP Exception: Unable to send spam.")
                await asyncio.sleep(1)  # Delay to prevent rate-limiting

            await ctx.send("<:Tick:1290693799361777665> Destroy command completed successfully!")

        except asyncio.TimeoutError:
            await ctx.send("<:CROSS_TDG:1321149916201881683> You took too long to respond!")

    except asyncio.TimeoutError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You took too long to respond!")
  
@siddhu.command()
async def create_chs(ctx, *, name: str):
    for i in range(100):
        try:
            await ctx.guild.create_text_channel(name)
            print(f"Created channel {name}")
        except discord.Forbidden:
            print(f"Failed to create channel {name}: Missing permissions")
        except discord.HTTPException as e:
            print(f"Failed to create channel {name}: {e.text}")
    await ctx.send(f"Created 100 channels with the name {name}.")        
        
@siddhu.command()
async def delete_all_chs(ctx):
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete(reason="Deleted by delete_all_chs command")
            print(f"Deleted channel {channel.name}")
        except discord.Forbidden:
            print(f"Failed to delete channel {channel.name}: Missing permissions")
        except discord.HTTPException as e:
            print(f"Failed to delete channel {channel.name}: {e.text}")
    await ctx.send("All channels have been deleted.")      
      
@siddhu.command(name="nick_all")
async def nick_all(ctx, *, new_nick: str = None):
    if not new_nick:
        await ctx.send("Please specify a nickname. Example: `.nick_all NewNick`")
        return

    success_count = 0
    failed_count = 0

    for member in ctx.guild.members:
        try:
            await member.edit(nick=new_nick)
            success_count += 1
        except discord.Forbidden:
            failed_count += 1

    await ctx.send(f"✅ Successfully changed nickname for `{success_count}` users.\n❌ Failed for `{failed_count}` users.")      
      
@siddhu.command()
async def delete_all_roles(ctx):
    try:
        deleted_roles = 0
        for role in ctx.guild.roles:
            if role.name != "@everyone":  # Avoid deleting @everyone role
                await role.delete(reason="Deleted by delete_all_role command")
                deleted_roles += 1

        await ctx.send(f"✅ Deleted `{deleted_roles}` roles from the server.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to delete roles.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to delete roles: {e.text}")      
      
@siddhu.command()
async def nick(ctx, member: discord.Member, *, nickname: str):
    try:
        await member.edit(nick=nickname)
        print(f"Changed nickname of {member.name} to {nickname}")
        await ctx.send(f"Changed nickname of {member.name} to {nickname}")
    except discord.Forbidden:
        await ctx.send("I don't have permission to change nicknames.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to change nickname: {e.text}")      
     
@siddhu.command()
async def cwebhook(ctx, *, webhook_name):
    channel = ctx.channel
    webhook = await channel.create_webhook(name=webhook_name)
    await ctx.send(f"Webhook created! URL: {webhook.url}")
 
@siddhu.command()
@commands.has_permissions(manage_guild=True)
async def server_name(ctx, *, name):
    await ctx.guild.edit(name=name)
    await ctx.send(f"Server name changed to {name}")

@siddhu.command()
async def questions_game(ctx):
    await ctx.send('Think of a person, place, or thing. I\'ll try to guess what it is in 20 questions or less!')
    questions = 0
    while questions < 20:
        await ctx.send('Is what you\'re thinking of a living thing?')
        response = await siddhu.wait_for('message', check=lambda message: message.author == ctx.author)
        if response.content.lower() == 'yes':
            await ctx.send('Is what you\'re thinking of a mammal?')
            response = await siddhu.wait_for('message', check=lambda message: message.author == ctx.author)
            if response.content.lower() == 'yes':
                await ctx.send('I think what you\'re thinking of is a human!')
                break
            else:
                await ctx.send('I\'m not sure what you\'re thinking of. Can you give me another hint?')
        elif response.content.lower() == 'no':
            await ctx.send('Is what you\'re thinking of something that can be held in your hand?')
            response = await siddhu.wait_for('message', check=lambda message: message.author == ctx.author)
            if response.content.lower() == 'yes':
                await ctx.send('I think what you\'re thinking of is a book!')
                break
            else:
                await ctx.send('I\'m not sure what you\'re thinking of. Can you give me another hint?')
        questions += 1
    if questions == 20:
        await ctx.send('I couldn\'t guess what you\'re thinking of. You win!')

@siddhu.command()
async def generate_random_num(ctx, min_value: int, max_value: int):
    random_number = random.randint(min_value, max_value)
    await ctx.send(f'The random number between {min_value} and {max_value} is: {random_number}')

@siddhu.command()
async def coinflip(ctx):
    coin_flip_result = random.choice(['Heads', 'Tails'])
    await ctx.send(f'The coin landed on: {coin_flip_result}')

@siddhu.command()
async def roll(ctx, sides: int = 6):
    roll_result = random.randint(1, sides)
    await ctx.send(f'You rolled a {roll_result} on a {sides}-sided die!')

@siddhu.command()
@commands.has_permissions(manage_guild=True)
async def server_icon(ctx):
    if ctx.message.attachments:
        icon = await ctx.message.attachments[0].read()
        await ctx.guild.edit(icon=icon)
        await ctx.send("Server icon changed")
    else:
        await ctx.send("Please attach an image to the message")

@siddhu.command()
@commands.has_permissions(manage_guild=True)
async def server_banner(ctx):
    if ctx.message.attachments:
        banner = await ctx.message.attachments[0].read()
        await ctx.guild.edit(banner=banner)
        await ctx.send("Server banner changed")
    else:
        await ctx.send("Please attach an image to the message")
 
@siddhu.command()
async def list_emoji(ctx):
    emojis = ctx.guild.emojis
    if not emojis:
        await ctx.send("This server has no custom emojis.")
        return
    emoji_list = [f"{emoji} - {emoji.name}" for emoji in emojis]
    await ctx.send("\n".join(emoji_list))
 
@siddhu.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"{ctx.channel.mention} has been locked.")

# Unlock Channel Command

@siddhu.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"{ctx.channel.mention} has been unlocked.") 

@siddhu.command()
@commands.has_permissions(manage_channels=True)
async def lockall(ctx):
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("All channels have been locked.")

# Unlock All Channels Command

@siddhu.command()
@commands.has_permissions(manage_channels=True)
async def unlockall(ctx):
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("All channels have been unlocked.")

@siddhu.command()
@commands.has_permissions(manage_guild=True)
async def changevanity(ctx, code):
    try:
        await ctx.guild.edit(vanity_url_code=code)
        await ctx.send(f"Vanity URL changed to (link unavailable)")
    except discord.Forbidden:
        await ctx.send("I don't have permission to change the vanity URL.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e.text}")

import discord
from discord.ext import commands

@siddhu.command()
async def join(ctx, channel: discord.VoiceChannel = None):
    if not channel:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> Please mention a voice channel or provide its ID.")
    
    await ctx.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=False)
    await ctx.send(f"<:tz_Verified:1281238102823665797> Joined {channel.name}.")

@siddhu.command()
async def leave(ctx):
    voice_state = ctx.author.voice

    if not voice_state or not voice_state.channel:
        await ctx.send("❌ You're not connected to any voice channel.")
        return

    try:
        await ctx.guild.change_voice_state(channel=None, self_mute=False, self_deaf=False)
        await ctx.send("<:tz_Verified:1281238102823665797> Left the VC.")
    except Exception as e:
        await ctx.send(f"⚠️ Failed to leave VC: `{e}`")

@siddhu.command()
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    await member.move_to(channel)
    await ctx.send(f"<:tz_Verified:1281238102823665797> Moved {member.mention} to {channel.name}")

@siddhu.command()
async def drag(ctx, member: discord.Member):
    if ctx.author.voice:
        await member.move_to(ctx.author.voice.channel)
        await ctx.send(f"<:tz_Verified:1281238102823665797> Dragged {member.mention} to your VC.")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a voice channel.")

@siddhu.command()
async def moveall(ctx, channel: discord.VoiceChannel):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")

    source_channel = ctx.author.voice.channel
    moved = 0
    for member in source_channel.members:
        await member.move_to(channel)
        moved += 1

    await ctx.send(f"<:tz_Verified:1281238102823665797> Moved {moved} member(s) to {channel.name}.")

@siddhu.command()
async def disconnectall(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    channel = ctx.author.voice.channel
    for member in channel.members:
        await member.edit(voice_channel=None)
    await ctx.send("<:tz_Verified:1281238102823665797> Disconnected everyone.")

@siddhu.command()
async def deafenall(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    for m in ctx.author.voice.channel.members:
        await m.edit(deafen=True)
    await ctx.send("<:tz_Verified:1281238102823665797> Deafened everyone.")

@siddhu.command()
async def undeafenall(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    for m in ctx.author.voice.channel.members:
        await m.edit(deafen=False)
    await ctx.send("<:tz_Verified:1281238102823665797> Undeafened everyone.")
@siddhu.command()
async def muteall(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    for m in ctx.author.voice.channel.members:
        await m.edit(mute=True)
    await ctx.send("<:tz_Verified:1281238102823665797> Muted everyone.")

@siddhu.command()
async def unmuteall(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    for m in ctx.author.voice.channel.members:
        await m.edit(mute=False)
    await ctx.send("<:tz_Verified:1281238102823665797> Unmuted everyone.")

@siddhu.command()
async def vcinfo(ctx):
    if not ctx.author.voice:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a VC.")
    vc = ctx.author.voice.channel
    members = "\n".join([f"• {m.name}" for m in vc.members])
    await ctx.send(
        f"**VC Info:**\n"
        f"Name: {vc.name}\nBitrate: {vc.bitrate}\nUser Limit: {vc.user_limit}\n"
        f"Members:\n{members}"
    )

@siddhu.command()
async def vckick(ctx, member: discord.Member = None):
    if not member:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> Please mention a user to kick from VC.")
    
    if member.voice and member.voice.channel:
        await member.edit(voice_channel=None)
        await ctx.send(f"<:tz_Verified:1281238102823665797> Kicked {member.mention} from `{member.voice.channel.name}`.")
    else:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> {member.mention} is not in a voice channel.")

@siddhu.command()
async def vckickall(ctx, channel: discord.VoiceChannel = None):
    if not channel:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> Please mention a voice channel or provide its ID.")

    if len(channel.members) == 0:
        return await ctx.send(f"<:CROSS_TDG:1321149916201881683> `{channel.name}` is empty.")

    for member in channel.members:
        await member.edit(voice_channel=None)

    await ctx.send(f"<:tz_Verified:1281238102823665797> Kicked {len(channel.members)} user(s) from `{channel.name}`.")

@siddhu.command()
async def vc247(ctx, mode=None):
    if not mode or mode.lower() not in ["enable", "disable"]:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> Usage: `.vc247 enable` or `.vc247 disable`")

    if not ctx.author.voice or not ctx.author.voice.channel:
        return await ctx.send("<:CROSS_TDG:1321149916201881683> You're not in a voice channel.")

    if mode.lower() == "enable":
        await ctx.send(f"<:tz_Verified:1281238102823665797> Staying 24/7 in `{ctx.author.voice.channel.name}`.")
    else:
        await ctx.send(f"<:tz_Verified:1281238102823665797> 24/7 mode disabled. You’ll still stay until manually disconnected.")

@siddhu.command()
async def spam_chs(ctx, *, message: str):
    channels = ctx.guild.text_channels
    for channel in channels:
        for _ in range(100):
            try:
                await channel.send(message)
                print(f"Sent message to {channel.name}")
            except discord.Forbidden:
                print(f"Failed to send message to {channel.name}: Missing permissions")
            except discord.HTTPException as e:
                print(f"Failed to send message to {channel.name}: {e.text}")
    await ctx.send("Spamming complete!")      
      
@siddhu.command(aliases=['ss'])
async def screenshot(ctx, url: str):
    """Takes a screenshot of a website."""
    API_KEY = "66114d"
    endpoint = "https://api.screenshotmachine.com"
    
    params = {
        "key": API_KEY,
        "url": url,
        "dimension": "1024xfull",
        "format": "png",
        "cacheLimit": "0",
        "timeout": "200"
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        filename = "screenshot.png"
        with open(filename, "wb") as f:
            f.write(response.content)

        await ctx.send(file=discord.File(filename))
    except requests.exceptions.RequestException as e:
        await ctx.send(f"❌ Failed to take screenshot: `{e}`")
    finally:
        if os.path.exists(filename):
            os.remove(filename)      
            
@siddhu.command()
async def closealldms(ctx):
    """Closes all open DM conversations."""
    headers = {"authorization": siddhu.http.token}
    response = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)

    if response.status_code != 200:
        return await ctx.send("❌ Failed to fetch DM channels.")

    dms = response.json()
    closed_count = 0

    for dm in dms:
        try:
            channel_id = dm["id"]
            delete_response = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)

            if delete_response.status_code == 200 or delete_response.status_code == 204:
                closed_count += 1
        except Exception as e:
            print(f"Failed to close DM {channel_id}: {e}")

    await ctx.send(f"✅ Closed `{closed_count}` DM conversations.")            
      
@siddhu.command()
async def delete_role(ctx, *, args: str):
    try:
        parts = args.split(",")  # Split by commas
        role_name = parts[0].strip()  # Extract role name
        count = parts[1].strip() if len(parts) > 1 else "1"  # Extract count or default to 1

        # Get all roles with the specified name
        matching_roles = [role for role in ctx.guild.roles if role.name.lower() == role_name.lower()]

        if not matching_roles:
            await ctx.send(f"No roles found with name `{role_name}`.")
            return

        if count.isdigit():  # If count is a number, delete that many roles
            count = int(count)
            if len(matching_roles) == 1:
                await matching_roles[0].delete(reason="Deleted by delete_role command")
                await ctx.send(f"Only one role `{role_name}` exists. Deleted successfully!")
            else:
                to_delete = matching_roles[:count]
                for role in to_delete:
                    await role.delete(reason="Deleted by delete_role command")
                await ctx.send(f"Deleted `{len(to_delete)}` roles with name `{role_name}`.")
        elif count.lower() == "all":  # Delete all roles with the specified name
            for role in matching_roles:
                await role.delete(reason="Deleted by delete_role command")
            await ctx.send(f"Deleted **all** `{len(matching_roles)}` roles with name `{role_name}`.")
        else:
            await ctx.send("Invalid command format. Use `.delete_role <role_name>, <number/all>`.")

    except discord.Forbidden:
        await ctx.send("I don't have permission to delete roles.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to delete roles: {e.text}")      
      
@siddhu.command()
async def create_role(ctx, *, args: str):
    try:
        parts = args.split(",")  # Split by commas
        roles = [r.strip() for r in parts[:-1]]  # Role names
        last_part = parts[-1].strip()

        # Check if the last part is a number (for count)
        if last_part.isdigit():
            count = int(last_part)
        else:
            roles.append(last_part)  # If not a number, treat it as a role name
            count = 1  # Default count is 1

        created_roles = []
        for role in roles:
            for _ in range(count // len(roles)):  # Divide count equally among roles
                new_role = await ctx.guild.create_role(name=role)
                created_roles.append(new_role.name)

        print(f"Created roles: {', '.join(created_roles)}")
        await ctx.send(f"Roles created successfully: `{', '.join(created_roles)}`")

    except discord.Forbidden:
        await ctx.send("I don't have permission to create roles.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to create roles: {e.text}")
  
@siddhu.command()
async def prefix(ctx, new_prefix):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['prefix'] = new_prefix
        f.seek(0)
        json.dump(data, f)
        f.truncate()
    await ctx.send(f"Your prefix changed to {new_prefix}")
    siddhu.command_prefix = new_prefix
  
@siddhu.command()
async def noprefix(ctx):
    with open('config.json', 'r+') as f:
        data = json.load(f)
        data['prefix'] = ''
        f.seek(0)
        json.dump(data, f)
        f.truncate()
    await ctx.send("Your prefix has been removed. I will now respond to messages without a prefix.")
    siddhu.command_prefix = ''
  
@siddhu.command()
async def create_channels(ctx, *, names: str):
    names = [name.strip() for name in names.split(",")]
    category = ctx.channel.category
    for name in names:
        try:
            await ctx.guild.create_text_channel(name, category=category)
            print(f"Created channel {name}")
        except discord.Forbidden:
            print(f"Failed to create channel {name}: Missing permissions")
        except discord.HTTPException as e:
            print(f"Failed to create channel {name}: {e.text}")
    await ctx.send(f"Created channels with the names {', '.join(names)}.")
        
@siddhu.command()
async def mute_all(ctx, duration: int, unit: str):
    """Mute all members in the server for the specified duration."""
    if unit.lower() not in ["m", "h", "d"]:
        await ctx.send("Invalid unit. Please use 'm' for minutes, 'h' for hours, or 'd' for days.")
        return
    
    # Convert duration to seconds
    if unit.lower() == "m":
        duration_in_seconds = duration * 60
    elif unit.lower() == "h":
        duration_in_seconds = duration * 3600
    else:  # unit == "d"
        duration_in_seconds = duration * 86400

    # Find or create the Muted role
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted", reason="Role created for mute_all command")
        await ctx.send("Muted role created. Please move it to the highest position for proper functionality.")
        
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False, speak=False, add_reactions=False)

    # Check role position
    if muted_role.position <= ctx.guild.me.top_role.position:
        await ctx.send(
            "**Error:** The 'Muted' role is not high enough in the role hierarchy.\n"
            "Please manually move the 'Muted' role above all member roles and try again."
        )
        return

    # Apply the Muted role to all members
    for member in ctx.guild.members:
        if member != ctx.author and member != siddhu.user and muted_role not in member.roles:
            try:
                await member.add_roles(muted_role, reason="Muted by mute_all command")
                print(f"Muted {member.name}")
            except discord.Forbidden:
                print(f"Failed to mute {member.name}: Missing permissions")
            except discord.HTTPException as e:
                print(f"Failed to mute {member.name}: {e.text}")
    
    await ctx.send(f"All members have been muted for {duration}{unit}.")
    
    # Unmute after the duration
    await asyncio.sleep(duration_in_seconds)
    for member in ctx.guild.members:
        if muted_role in member.roles:
            try:
                await member.remove_roles(muted_role, reason="Unmuted after mute_all duration expired")
                print(f"Unmuted {member.name}")
            except discord.Forbidden:
                print(f"Failed to unmute {member.name}: Missing permissions")
            except discord.HTTPException as e:
                print(f"Failed to unmute {member.name}: {e.text}")
    
    await ctx.send("Unmuted all members after the duration.")
        
@siddhu.command()
async def remove_role(ctx, member: discord.Member, role: discord.Role):

    await member.remove_roles(role)

    await ctx.send(f"The {role.mention} role has been removed from {member.mention}.")
        
@siddhu.command()
async def nuke(ctx):
    channel = ctx.channel
    channel_name = channel.name
    category = channel.category
    await channel.delete()
    new_channel = await ctx.guild.create_text_channel(channel_name, category=category)
    await new_channel.send("Channel Nuked Successfully")
    await ctx.send(f"Channel {channel_name} nuked and recreated!")
        
@siddhu.command()
async def firstmsg(ctx):
    """Fetches and displays the first message in the channel (Works in Servers, DMs & Group Chats)."""
    channel = ctx.channel
    try:
        messages = [msg async for msg in channel.history(limit=1, oldest_first=True)]

        if messages:
            first_message = messages[0]
            msg_content = first_message.content if first_message.content else "*[Message has no text]*"

            # Handle stickers, attachments, and embeds
            if first_message.stickers:
                msg_content = "*[Message contains a sticker]*"
            elif first_message.attachments:
                msg_content = "*[Message contains an attachment]*"
            elif first_message.embeds:
                msg_content = "*[Message contains an embed]*"

            # Create clickable message link
            if ctx.guild:  # If the command is used in a server
                message_link = f"https://discord.com/channels/{ctx.guild.id}/{channel.id}/{first_message.id}"
            else:  # If the command is used in DMs or Group Chats
                message_link = f"https://discord.com/channels/@me/{channel.id}/{first_message.id}"

            # Create a clickable timestamp
            timestamp = f"<t:{int(first_message.created_at.timestamp())}:F>"

            # Send formatted response
            response = (
                f"**<:TOS:1336669803221614622> The first message in this channel:**\n"
                f"`{msg_content}`\n"
                f"**<:bxbz_monet_lovenote:1290693793724497920> [ [Message Link]({message_link}) ]**\n"
                f"**<:user:1325418236514140282> Sent by {first_message.author.mention}**\n"
                f"**<:uptime:1320649297796010075> {timestamp}**"
            )
            await ctx.send(response)
        else:
            await ctx.send("**This channel has no messages.**")

    except discord.Forbidden:
        await ctx.send("❌ **I don't have permission to fetch messages in this channel.**")
    except discord.HTTPException:
        await ctx.send("❌ **An error occurred while fetching the message. Try again later.**")
        
@siddhu.command()
async def ban(ctx, member: discord.Member, *, reason: str = None):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned from the server.")
        
@siddhu.command()
async def kick(ctx, member: discord.Member, *, reason: str = None):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked from the server.")

@siddhu.command()
async def role_all(ctx, role: discord.Role):
    for member in ctx.guild.members:
        if member != ctx.author and member != siddhu.user:
            try:
                await member.add_roles(role, reason="Given role by role_all command")
                print(f"Given {role.name} role to {member.name}")
            except discord.Forbidden:
                print(f"Failed to give {role.name} role to {member.name}: Missing permissions")
            except discord.HTTPException as e:
                print(f"Failed to give {role.name} role to {member.name}: {e.text}")
    await ctx.send(f"All members have been given the {role.mention} role.")

@siddhu.command()
async def timer(ctx, duration: str, *, reason: str = None):
    # Parse the duration string
    duration_map = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }
    unit = duration[-1]
    value = int(duration[:-1])
    if unit not in duration_map:
        await ctx.send('Invalid unit. Use s, m, h, or d.')
        return
    duration_in_seconds = value * duration_map[unit]

    # Start the timer
    await ctx.send(f'Timer started for {duration} ({reason or "no reason given"})!')
    await asyncio.sleep(duration_in_seconds)
    await ctx.send('Timer ended!')

import re
import requests

SUPPORTED_COINS = ["btc", "ltc", "eth", "doge", "bch"]

@siddhu.command(description="Gets information about a crypto transaction using blockcypher.com")
async def cryptotx(ctx, coin: str = None, txid: str = None):
    await ctx.send(content="🔎 Fetching transaction details...")

    # Check if the command is used as a reply
    if ctx.message.reference:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        txid_match = re.search(r"([a-fA-F0-9]{64})", replied_msg.content)  # Extract TXID from message

        if txid_match:
            txid = txid_match.group(0)

    # If TXID is a URL, extract the TXID from it
    if txid and "blockcypher.com" in txid:
        txid_match = re.search(r"([a-fA-F0-9]{64})", txid)
        if txid_match:
            txid = txid_match.group(0)

    # Validate TXID presence
    if not txid:
        await ctx.send(content="❌ **Please provide a valid transaction ID or reply to a message containing one!**")
        return

    # Auto-detect coin if not provided
    if not coin:
        detected_coin = None

        for possible_coin in SUPPORTED_COINS:
            url = f"https://api.blockcypher.com/v1/{possible_coin}/main/txs/{txid}"
            response = requests.get(url)

            if response.status_code == 200:
                detected_coin = possible_coin
                break

        if detected_coin:
            coin = detected_coin
        else:
            await ctx.send(content="❌ **Failed to detect coin type. Please specify it manually!**")
            return

    # Validate provided coin
    if coin.lower() not in SUPPORTED_COINS:
        await ctx.send(content="❌ **Invalid or unsupported coin! Supported: BTC, LTC, ETH, DOGE, BCH.**")
        return

    # API Request
    url = f"https://api.blockcypher.com/v1/{coin.lower()}/main/txs/{txid}"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()
        confirmations = res.get("confirmations", "N/A")
        preference = res.get("preference", "N/A")
        confirmed = res.get("confirmed", "Not confirmed").replace("T", " ").replace("Z", "") if res.get("confirmed") else "Not confirmed"
        received = res.get("received", "Not received").replace("T", " ").replace("Z", "") if res.get("received") else "Not received"
        double_spend = res.get("double_spend", "False")

        tx_link = f"https://live.blockcypher.com/{coin.lower()}/tx/{txid}"

        message = f"""
# TX INFO <:crypto:1322611842316501073>  
**<:nxt_blue_crown:1281973611917348989> Transaction Hash: `{txid}`  
<:white_Arrow:1290693791983861822> TX Link: {tx_link}  

<:exchanger:1322954180452810775> Coin: `{coin.upper()}`  
<:experienced_seller:1290924799421583391> Confirmations: `{confirmations}`  
<:star_blue:1284898459232763944> Preference: `{preference}`  
<:emoji_1738342244745:1334928872269152259> Confirmed: `{confirmed}`  
<:lr_tick_1:1290693800808677461> Received: `{received}`  
<a:tz_money:1281238106682560567> Double Spend: `{double_spend}`**  
        """.strip()

        await ctx.send(content=message)

    else:
        await ctx.send(content="❌ **Invalid Transaction ID or unable to fetch data!**")

@siddhu.command(description="Sends a list of all the nicknames you have in servers.")
async def nickscan(ctx):
    await ctx.send(content="Scanning for nicknames...")

    nicknames = []

    # Iterate through all guilds the selfbot is a member of
    for guild in siddhu.guilds:
        member = guild.get_member(ctx.author.id)

        # If a nickname exists, add it to the list
        if member and member.nick:
            nicknames.append(f"[{guild.name}]: {member.nick}\n")

    message = f"""**<:Angel_of_coowner:1290692091432800357> Server Nicknames:
<:BadgeDeveloper:1290693804013129768> [Total]: {len(nicknames)}**

```{''.join(nicknames)}
```"""

    await ctx.send(content=f"{message}")

    await delete_after_timeout(ctx.message)


@siddhu.command(aliases=["resetnick"], description="Resets all your nicknames in servers.")
async def nickreset(ctx):
    await ctx.send(content="Resetting nicknames...")

    # Iterate through all guilds the selfbot is a member of
    for guild in siddhu.guilds:
        member = guild.get_member(ctx.author.id)

        # If a nickname exists, reset it
        if member and member.nick:
            try:
                await member.edit(nick=None)
            except Exception as e:
                pass

    await ctx.send(content=":white_check_mark: | Reset nicknames.")

    await delete_after_timeout(ctx.message)

@siddhu.command()
async def mute(ctx, member: discord.Member, duration: int, unit: str, *, reason: str = None):
    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles, name="Muted")

    # Create Muted role if it doesn't exist
    if not muted_role:
        muted_role = await guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False, speak=False))
        for channel in guild.channels:
            await channel.set_permissions(muted_role, send_messages=False, speak=False)

    # Add Muted role
    await member.add_roles(muted_role, reason=reason)

    # Calculate duration in seconds
    if unit.lower() == "m":
        seconds = duration * 60
    elif unit.lower() == "h":
        seconds = duration * 3600
    elif unit.lower() == "d":
        seconds = duration * 86400
    else:
        await ctx.send("Invalid unit. Use 'm' for minutes, 'h' for hours or 'd' for days.")
        return

    await ctx.send(f"{member.mention} has been muted for {duration}{unit}.")

    # Wait for duration then remove mute
    await asyncio.sleep(seconds)

    # Remove Muted role if the member still has it
    if muted_role in member.roles:
        await member.remove_roles(muted_role, reason="Mute duration expired")
        await ctx.send(f"{member.mention} has been unmuted.")

@siddhu.command()
async def unmute(ctx, member: discord.Member):
    """
    Manually unmute a user by removing the Muted role.
    """
    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles, name="Muted")

    if not muted_role:
        await ctx.send("Muted role does not exist.")
        return

    if muted_role in member.roles:
        await member.remove_roles(muted_role, reason="Manual unmute")
        await ctx.send(f"{member.mention} has been unmuted.")
    else:
        await ctx.send(f"{member.mention} is not muted.")
    
#Discord Status Changer Class
class DiscordStatusChanger:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": token,
            "User-Agent": "DiscordBot (https://discordapp.com, v1.0)",
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

    def change_status(self, status, message, emoji_name, emoji_id):
        jsonData = {
            "status": status,
            "custom_status": {
                "text": message,
                "emoji_name": emoji_name,
                "emoji_id": emoji_id,
            }
        }
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=self.headers, json=jsonData)
        return r.status_code
    
class StatusRotator(commands.Cog):
    def __init__(self, siddhu, token):
        self.bot = siddhu
        self.token = config.get('token')
        self.discord_status_changer = DiscordStatusChanger(self.token)
        self.is_rotating = False  # New attribute to control rotation

    @commands.command()
    async def start_rotation(self, ctx):
        if not self.is_rotating:
            self.is_rotating = True
            await ctx.send("**Starting status rotation...**")
            await self.run_rotation(ctx)
        else:
            await ctx.send("**Status rotation is already running.**")

    @commands.command()
    async def stop_rotation(self, ctx):
        if self.is_rotating:
            self.is_rotating = False
            await ctx.send("Stopping status rotation...")
        else:
            await ctx.send("Status rotation is not currently running.")

    async def run_rotation(self, ctx):
        file_path = 'status.txt'
        while self.is_rotating:
            try:
                with open(file_path, 'r') as file:
                    messages = [line.strip() for line in file.readlines()]

                if not messages:
                    await ctx.send("No messages found in the file. Add messages to continue.")
                    await asyncio.sleep(30)
                    continue

                for message in messages:
                    message_parts = message.split(',')

                    if len(message_parts) >= 2:
                        emoji_id = None
                        emoji_name = message_parts[0].strip()

                        if emoji_name and emoji_name[0].isdigit():
                            emoji_id = emoji_name
                            emoji_name = ""

                        status_text = message_parts[1].strip()

                        status_code = self.discord_status_changer.change_status("dnd", status_text, emoji_name, emoji_id)
                        if status_code == 200:
                            print(f"Changed to: {status_text}")
                        else:
                            print("Failed to change status.")
                        await asyncio.sleep(10)
            
            except Exception as e:
                print(f"An error occurred: {e}")
                await asyncio.sleep(10)  # Retry after 10 seconds
                
TOKEN = config.get('token')
siddhu.add_cog(StatusRotator(siddhu, TOKEN))

import aiohttp
import asyncio
import json

http_session = aiohttp.ClientSession()  # ✅ FIXED: Now it's an instance

@siddhu.command()
async def change_hypesquad(ctx):
    choices = {
        1: "BRAVERY",
        2: "BRILLIANCE",
        3: "BALANCED"
    }
    
    await ctx.send("**[1] Bravery\n[2] Brilliance\n[3] BalanceD**")
    await ctx.send("<a:diamond:1281246685955362877> **ENTER YOUR CHOICE**: `1,2,3`")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await siddhu.wait_for('message', check=check, timeout=60)
        choice = int(msg.content)
    except asyncio.TimeoutError:
        await ctx.send("<a:diamond:1281246685955362877> **COMMAND TIMED OUT**")
        return
    except ValueError:
        await ctx.send("<a:diamond:1281246685955362877> **INVALID CHOICE PLEASE ENTER** : `1 , 2 , 3`")
        return

    headerpost = {
        'Authorization': TOKEN  # ✅ Uses token from config.json
    }
    
    payloadsosat = {
        'house_id': choice
    }
    
    try:
        await ctx.send(f"<a:diamond:1281246685955362877> **CHANGING HYPESQUAD TO {choices.get(choice, 'Unknown')}**")
        
        async with http_session.post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headerpost) as response:
            if response.status == 204:
                await ctx.send("<:rdx_glowin_heart:1288196137848803451> **HYPESQUAD CHANGED SUCCESSFULLY**")
            elif response.status == 401:
                await ctx.send("<:white_arrow:1290693789824061461>**TOKEN INVALID OR EXPIRED**")
            elif response.status == 429:
                await ctx.send("<:white_arrow:1290693789824061461>**PLEASE WAIT FOR 2 MINUTES**")
            else:
                await ctx.send(f"<:white_arrow:1290693789824061461>**WE CAUGHT AN ERROR:** `{response.status}`")
    except Exception as e:
        await ctx.send(f"<:white_arrow:1290693789824061461>**AN ERROR OCCURRED:** `{str(e)}`")

# Close session when bot shuts down
async def close_session():
    await http_session.close()

import atexit
atexit.register(lambda: asyncio.run(close_session()))

#task
tasks_dict = {}

@siddhu.command()
async def console(ctx, lines: int = 10):
    """
    Fetches the last `lines` number of logs from the console log file.
    Usage: .console [number_of_lines]
    """
    try:
        # Check if the log file exists, and create it if it doesn't
        if not os.path.exists("selfbot.log"):
            with open("selfbot.log", "w") as log_file:
                log_file.write("")  # Create an empty file if it doesn't exist

        # Read the log file
        with open("selfbot.log", "r") as log_file:
            log_lines = log_file.readlines()

        # Get the last `lines` from the log
        log_snippet = "".join(log_lines[-lines:])

        if not log_snippet.strip():
            log_snippet = "No logs available."

        # Send the log snippet to the user
        await ctx.send(f"```{log_snippet}```")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: {str(e)}")

def get_uptime():
    now = datetime.datetime.utcnow()
    delta = now - bot_start_time
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days}d {hours}h {minutes}m {seconds}s"        
        
import json

@siddhu.command(aliases=['h'])
async def help(ctx, category: str = None):
    # Load config.json to get the prefix
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            prefix = config.get("prefix", ".")  # Default to "." if not set
    except FileNotFoundError:
        prefix = "."

    current_prefix = prefix if prefix else "No Prefix"

    if category is None:
        help_msg = f"""# __**SyntheX Prime V5**__ <a:Basu_Crown:1290692084709195826>  
<a:emoji_1739092962614:1338077611040968734> **ALL-IN-ONE SELFBOT** <:FL_blue_gengar:1281973618632429710>
**Hey, {siddhu.user.name}** I'm here to help You !

<:TOS:1336669803221614622> **HELP:** {prefix}h <module name> 
<:emoji_1739864737772:1341314670346371095> **TOTAL CATEGORIES:** 25
<:emoji_1739864737772:1341314670346371095> **TOTAL COMMANDS:** 564  

<:SowardCategory:1378326907254345750> **__Module Categories__**
> <:max_r_owner:1288194870086860850> **Main**  
> <:user:1325418236514140282> **User**  
> <:IconStatusWebOnline:1349022132251656232> **Activity**  
> <:Discord_bots:1290700055514452121> **Admin**  
> <:Settings:1290692093001469994> **Utility**  
> <:rdx_glowin_heart:1288196137848803451> **Extra**  
> <a:zeng_blue_wand:1349021856698470440> **Fun**  
> <a:Nuking_Residence:1308833239670198314> **Wizz**  
> <a:developer:1290928018793037844> **Mod**  
> <:sq_heartmsg:1290693802713157632> **Msg**  
> <:Crown_king:1281280214600515635> **Sniper**  
> <:devs:1290693770567749652> **Developer**  
> <:experienced_seller:1290924799421583391> **Seller**  
> <:emoji_1738342244745:1334928872269152259> **Antinuke**  
> <:money:1290693786401247356> **Wallet**  
> <:tharkimon:1291420565911113809> **Nsfw**  
> <:Blue_Crown_temp:1290693781502562306> **Misc**  
> <:rd_VoiceIcon:1321112732770238545> **Vc**
> <:Settings:1322252716508053526> **Spy**  
> <:nxt_blue_crown:1281973611917348989> **Premium**
> <:exchanger:1322954180452810775> **Crypto**
> <:Titanz:1281243485919510569> **Stock**
> <:tz_Boost_icon:1281241573035868220> **Boost**
> <:TOS:1336669803221614622> **Vanity**
> <:Ownership:1290692081248895177> **Info**  

> <:star_blue:1284898457181622362> **NO PREFIX MODE:** `{prefix}noprefix`  
> <:star_blue:1284898457181622362> **NEW PREFIX:** `{prefix}prefix <new_prefix>`  
> <:star_blue:1284898457181622362> **CURRENT PREFIX:** `{current_prefix}`
"""
        if embed_mode_enabled:
            await send_custom_embed(
                ctx,
                description=help_msg,
                footer_text="Developed by siddhu.og",
                footer_icon="https://cdn.discordapp.com/avatars/1241519716644819014/2f75df45d57c600a49370caab69cd051.webp?size=1024",
                image="https://cdn.discordapp.com/attachments/1255090765726748694/1377325399419260980/5.jpg",
                timestamp=True
            )
        else:
            await ctx.send(help_msg)

    elif category.lower() == "main":
        await ctx.send(f"""# <:Crown_king:1290693780118442034> **MAIN COMMANDS :-**
<:white_arrow:1290693789824061461>**AutoRespond** :-  
<:kronix_dot:1281280217335332966> `.ar <trigger>, <response>`  
<:white_arrow:1290693789824061461>**Remove Respond** :-  
<:kronix_dot:1281280217335332966> `.removear <trigger>`  
<:white_arrow:1290693789824061461>**AutoRespond List** :-  
<:kronix_dot:1281280217335332966> `.ar_list`  
<:white_arrow:1290693789824061461>**AutoForward** :-  
<:kronix_dot:1281280217335332966> `.af <trigger>, <message_id> [channel_id]`  
<:white_arrow:1290693789824061461>**Remove AutoForward** :-  
<:kronix_dot:1281280217335332966> `.afrem <trigger>`  
<:white_arrow:1290693789824061461>**Reset AutoForwards** :-  
<:kronix_dot:1281280217335332966> `.afreset`
<:white_arrow:1290693789824061461>**AutoForward List** :-  
<:kronix_dot:1281280217335332966> `.aflist`
<:white_arrow:1290693789824061461>**AutoMsg** :-
<:kronix_dot:1281280217335332966> `.am <time> <chnl_id> <msg>`
<:white_arrow:1290693789824061461>**Stop AutoMsg** :- `.am_stop <chnl_id>`
<:white_arrow:1290693789824061461>**AutoMsg List** :- `.am_list`
<:white_arrow:1290693789824061461>**AutoMsg Clear** :- `.am_clear`
<:white_arrow:1290693789824061461>**Afk** :- `.afk <reason>`
<:white_arrow:1290693789824061461>**Remove Afk** :- `.unafk`
<:white_arrow:1290693789824061461>**Server Clone** :-
<:kronix_dot:1281280217335332966> `.csrv <copy id> <target id>`
<:white_arrow:1290693789824061461>**Roles Clone** :-
<:kronix_dot:1281280217335332966> `.copy_roles <copy id> <target id>`
<:white_arrow:1290693789824061461>**Channels Clone** :-
<:kronix_dot:1281280217335332966> `.copy_channels <copy id> <target id>`
<:white_arrow:1290693789824061461>**Weather :-** `.weather <city>`
<:white_arrow:1290693789824061461>**Timezone Converter :-** `.timezone <time> <from_zone> <to_zone>`
<:white_arrow:1290693789824061461>**Create Poll :-** `.poll <question> <option1> <option2> ...`
<:white_arrow:1290693789824061461>**Google Search :-** `.google <query>`
<:white_arrow:1290693789824061461>**Lyrics Search :-** `.lyrics <song name>`
<:white_arrow:1290693789824061461>**Create Webhook** : `.cwebhook <name>`
<:white_arrow:1290693789824061461>**LIST EMOJI** : `.list_emoji`
<:white_arrow:1290693789824061461>**CHANGE VANITY** : `.change_vanity`
<:white_arrow:1290693789824061461>**Ban** :- `ban @user`
<:white_arrow:1290693789824061461>**First Message** :- `.firstmsg`
<:white_arrow:1290693789824061461> **Delete Webhook** : `.deletewebhook <webhook_url>`""")

    elif category.lower() == "vc":
        await ctx.send(f"""# <:rd_VoiceIcon:1321112732770238545> VC COMMANDS :-
<:white_arrow:1290693789824061461>**JOIN VC** `.join #channel`
<:white_arrow:1290693789824061461>**LEAVE VC** `.leave`
<:white_arrow:1290693789824061461>**MOVE TO VC** `.move @user #channel`
<:white_arrow:1290693789824061461>**DRAG USER** `.drag @user`
<:white_arrow:1290693789824061461>**MOVE ALL** `.moveall #channel`
<:white_arrow:1290693789824061461>**VC KICK** `.vckick @user`
<:white_arrow:1290693789824061461>**VC KICK ALL** `.vckickall #channel`
<:white_arrow:1290693789824061461>**MUTE ALL** `.muteall`
<:white_arrow:1290693789824061461>**UNMUTE ALL** `.unmuteall`
<:white_arrow:1290693789824061461>**DEAFEN ALL** `.deafenall`
<:white_arrow:1290693789824061461>**UNDEAFEN ALL** `.undeafenall`
<:white_arrow:1290693789824061461>**VC INFO** `.vcinfo`
<:white_arrow:1290693789824061461>**VC 24/7 MODE** `.vc247 enable / disable`""")

    elif category.lower() == "vanity":
        await ctx.send(f"""# <:TOS:1336669803221614622> Vanity Sniper

<:white_arrow:1290693789824061461> **Toggle Sniper**: `.vanity_sniper <enable/disable>`  
<:Titanz:1281243491476967447> **Enables or disables the vanity sniper**  

<:white_arrow:1290693789824061461> **Add Vanity**: `.vsniper_add <vanity> <target server id>`  
<:Titanz:1281243491476967447> **Adds a vanity URL to the sniper list with a target server**  

<:white_arrow:1290693789824061461> **Remove Vanity**: `.vsniper_remove <vanity>`  
<:Titanz:1281243491476967447> **Removes a specific vanity from the sniper list**  

<:white_arrow:1290693789824061461> **Clear Sniper List**: `.vsniper_clear`  
<:Titanz:1281243491476967447> **Removes all vanities from the sniper list**  

<:white_arrow:1290693789824061461> **Set Checking Delay**: `.vanity_delay <delay in sec>`  
<:Titanz:1281243491476967447> **Changes the delay between vanity availability checks (default: 5s)**  

<:white_arrow:1290693789824061461> **View Sniper List**: `.vanity_list`  
<:Titanz:1281243491476967447> **Displays all vanities currently being sniped**  

<:white_arrow:1290693789824061461> **Backup Sniper Data**: `.vsniper_backup`  
<:Titanz:1281243491476967447> **Creates a backup of the sniper list and settings**  

<:white_arrow:1290693789824061461> **View Sniper Logs**: `.vsniper_logs`  
<:Titanz:1281243491476967447> **Displays logs of sniped vanities and attempts**  

<:white_arrow:1290693789824061461> **Set Webhook for Logs**: `.vsniper_webhook <link>`  
<:Titanz:1281243491476967447> **Saves a webhook URL in config.json where logs will be sent**""")

    elif category.lower() == "user":
        await ctx.send(f"""# <:discord:1282007043456241717> USER COMMANDS :-
<:white_arrow:1290693789824061461> **List Server Friends** : `.serverfriends`
<:white_arrow:1290693789824061461> **List Mutual Servers** : `.mutualservers @user`
<:white_arrow:1290693789824061461> **List Admin Servers** : `.adminservers`
<:white_arrow:1290693789824061461> **Reverse Avatar** : `.revavatar <user_id>`
<:white_arrow:1290693789824061461> **Nick Scan** : `.nickscan`
<:white_arrow:1290693789824061461> **Reset Nicknames** : `.nickreset`
<:white_arrow:1290693789824061461> **Prevent Leaving group** : `.noleave @user`
<:white_arrow:1290693789824061461> **Allow Leaving group** : `.allowleave @user`
<:white_arrow:1290693789824061461> **Leave All Servers** : `.leaveallservers`
<:white_arrow:1290693789824061461> **Leave All Groups** : `.leaveallgroups`
<:white_arrow:1290693789824061461> **Stop Leaving Servers/Groups** : `.stopleave`
<:white_arrow:1290693789824061461> **Nick Loop** : `.nickloop`
<:white_arrow:1290693789824061461> **Stop Nick Loop** : `.stopnickloop`
<:white_arrow:1290693789824061461> **Set PFP** : `.setpfp <image_url>`
<:white_arrow:1290693789824061461> **Give all Roles** : `.giveallroles @user`
<:white_arrow:1290693789824061461>**CHANGE CMD NAME**:- `.edit_cmd <new name>`
<:white_arrow:1290693789824061461>**REMOVE CMD NAME** :- `.remove_alias`
<:white_arrow:1290693789824061461>**RESET THE CMD NAMES** :- `.reset_cmd`
<:white_arrow:1290693789824061461>**HYPESQUAD CHANGE** : 
<:kronix_dot:1281280217335332966> `.change_hypesquad`""")

    elif category.lower() == "activity":
        await ctx.send(f"""# <:kronix_partner:1290692094884577374> **ACTIVITY COMMANDS :-**
<:white_arrow:1290693789824061461> **playing**: `.playing <activity>`
<:white_arrow:1290693789824061461> **watching**: `.watching <activity>`
<:white_arrow:1290693789824061461> **listening**: `.listening <activity>`
<:white_arrow:1290693789824061461> **streaming**: `.streaming <activity> <stream_url>`
<:white_arrow:1290693789824061461> **removepresence**: `.stopactivity`
<:white_arrow:1290693789824061461> **cycleplaying**: `.cycleplaying <activity1> <activity2> ...`
<:white_arrow:1290693789824061461> **stopcycleplaying**: `.stopcycleplaying`
<:white_arrow:1290693789824061461> **cyclewatching**: `.cyclewatching <activity1> <activity2> ...`
<:white_arrow:1290693789824061461> **stopcyclewatching**: `.stopcyclewatching`
<:white_arrow:1290693789824061461> **cyclelistening**: `.cyclelistening <activity1> <activity2> ...`
<:white_arrow:1290693789824061461> **stopcyclelistening**: `.stopcyclelistening`
<:white_arrow:1290693789824061461> **cyclestreaming**: `.cyclestreaming <activity1> <activity2> ... <stream_url>`
<:white_arrow:1290693789824061461> **stopcyclestreaming**: `.stopcyclestreaming`
<:white_arrow:1290693789824061461> **online**: `.online`
<:white_arrow:1290693789824061461> **idle**: `.idle`
<:white_arrow:1290693789824061461> **dnd**: `.dnd`
<:white_arrow:1290693789824061461> **invisible**: `.invisible`
<:white_arrow:1290693789824061461>**Status Rotator** :- `.start_rotation`
<:white_arrow:1290693789824061461>**Stop Rotator** :- `.stop_rotation`
<:white_arrow:1290693789824061461>**Config Status Rotator** :- `.config_status`
<:white_arrow:1290693789824061461>**Edit status line** :- `.edit_line <num> <status>, <emoji>`
<:white_arrow:1290693789824061461>**Show Config** :- `.show_status`
<:white_arrow:1290693789824061461>**Clear Config** :- `.clear_status`""")

    elif category.lower() == "admin":
        await ctx.send(f"""# <:BadgeDeveloper:1290693804013129768> ADMIN CMDZ :-
<:white_arrow:1290693789824061461>**Dashboard** :- `.dashboard`
<:white_arrow:1290693789824061461>**Fake Typing** :- `.fake_typing <channel id> <duration>`
<:white_arrow:1290693789824061461>**Emoji Animator** :- `.emoji_animator <emoji>`
<:white_arrow:1290693789824061461>**WORD ART** : `.asci <text>`
<:white_arrow:1290693789824061461>**DEFINE** : `.define <word>`
<:white_arrow:1290693789824061461>**GITSEARCH** : `.gitsearch name`
<:white_arrow:1290693789824061461>**GITUSER** : `.gituser username`
<:white_arrow:1290693789824061461>**SAVE TRANSCRIPT** : `.savetranscript`
<:white_arrow:1290693789824061461>**VIDEO SEARCH** : `.ytsearch <title>`
<:white_arrow:1290693789824061461>**SPAM WEBHOOK** :
`.webhook_spam <url> <amount>`
<:white_arrow:1290693789824061461>**TIMER :**
<:kronix_dot:1281280217335332966>`.timer <time> <reason>`""")

    elif category.lower() == "utility":
        await ctx.send(f"""# <:Settings:1290692093001469994> **UTILITY COMMANDS :-**
<:white_arrow:1290693789824061461>**Get Avatar** :- `.avatar <@user>`
<:white_arrow:1290693789824061461>**Get Banner** :- `.banner @user`
<:white_arrow:1290693789824061461>**Get Icon Of Server** :- `.icon`
<:white_arrow:1290693789824061461>**Get Image** :- `.get_image <query>`
<:white_arrow:1290693789824061461>**User Info** :- `.user_info <@user>`
<:white_arrow:1290693789824061461>**Role Info** :- `.roleinfo <role>`
<:white_arrow:1290693789824061461>**List Roles** :- `.listroles`
<:white_arrow:1290693789824061461>**List Bots** :- `.listbots`
<:white_arrow:1290693789824061461>**Member Count** :- `.membercount`
<:white_arrow:1290693789824061461>**Boost Count** :- `.boostcount`
<:white_arrow:1290693789824061461>**Auto React** :- `.areact <emoji1>, <emoji2>, | .stop_areact`
<:white_arrow:1290693789824061461>**Space News** :- `.space_news`
<:white_arrow:1290693789824061461>**My Devices** :- `.mydevices`
<:white_arrow:1290693789824061461>**Generate Poem** :- `.generate_poem <theme>`
<:white_arrow:1290693789824061461>**Puzzle** :- `.puzzle`
<:white_arrow:1290693789824061461>**Steal Sticker** :- `.steal_sticker <sticker_url> <name>`
<:white_arrow:1290693789824061461>**Steal Emoji** :- `.steal_emoji <emoji_url> <name>`
<:white_arrow:1290693789824061461>**Add Emoji** :- `.addemoji <emoji>`
<:white_arrow:1290693789824061461>**Ghost Ping** :- `.ghost_ping`
<:white_arrow:1290693789824061461>**User Status** :- `.userstatus <@user>`
<:white_arrow:1290693789824061461>**Pastebin** :- `.pastebin <text>`
<:white_arrow:1290693789824061461>**Block User** :- `.block <@user>`
<:white_arrow:1290693789824061461>**Unblock User** :- `.unblock <@user>`
<:white_arrow:1290693789824061461>**Block List** :- `.blocklist`
<:white_arrow:1290693789824061461>**Binary** :- `.binary <text>`
<:white_arrow:1290693789824061461>**Unbinary** :- `.unbinary <binary>`
<:white_arrow:1290693789824061461>**Wiki Search** :- `.wiki <search_term>`
<:white_arrow:1290693789824061461>**Stats** :- `.stats`
<:white_arrow:1290693789824061461>**Current Timestamp** :- `.timestamp [optional_date_time]`
<:white_arrow:1290693789824061461> **Calculate Age** :- `.calculate_age <date_of_birth>`
<:white_arrow:1290693789824061461> **Count Words** :- `.count_words <text>`
<:white_arrow:1290693789824061461> **Count Characters** :- `.count_characters <text>`
<:white_arrow:1290693789824061461> **Palindrome Check** :- `.palindrome <text>`
<:white_arrow:1290693789824061461> **Convert to Uppercase** :- `.convert_to_upper <text>`
<:white_arrow:1290693789824061461> **Convert to Lowercase** :- `.convert_to_lower <text>`
<:white_arrow:1290693789824061461> **Repeat Text** :- `.repeat_text <text> <count>`
<:white_arrow:1290693789824061461> **Reverse Words** :- `.reverse_words <text>`
<:white_arrow:1290693789824061461> **Join Words** :- `.join_words <word1>, <word2>, ...`
<:white_arrow:1290693789824061461> **Get Bot Info** :- `.get_bot_info`
<:white_arrow:1290693789824061461> **Emoji Info** :- `.emoji_info <emoji>`
<:white_arrow:1290693789824061461> **Get Ping** :- `.get_ping`
<:white_arrow:1290693789824061461> **Server Ban Count** :- `.server_ban_count`
<:white_arrow:1290693789824061461> **Clear Messages** :- `.clear_messages`""")

    elif category.lower() == "stock":
        await ctx.send(f"""# <:Titanz:1281243485919510569> Stock Sender  

<:star_blue:1284898459232763944> **Send Stock :-**  
<:white_arrow:1290693789824061461> `.send_stock <time> #channel`  
<:arrow:1290693784790765678> **Sends all the stock to the provided channel**  

<:star_blue:1284898459232763944> **Add Stock :-**  
<:white_arrow:1290693789824061461> `.add_stock <product name>`  
<:arrow:1290693784790765678> **Prompts the user to enter product details and adds it to the stock list**  

<:star_blue:1284898459232763944> **Remove Product :-**  
<:white_arrow:1290693789824061461> `.remove_product <product name>`  
<:arrow:1290693784790765678> **Removes the specified product from the stock list**  

<:star_blue:1284898459232763944> **Clear Stock :-**  
<:white_arrow:1290693789824061461> `.clear_stock`  
<:arrow:1290693784790765678> **Removes all products from the stock list**  

<:star_blue:1284898459232763944> **Stock List :-**  
<:white_arrow:1290693789824061461> `.stock_list`  
<:arrow:1290693784790765678> **Displays all products currently available in the stock**  

<:star_blue:1284898459232763944> **Send Products :-**  
<:white_arrow:1290693789824061461> `.send_products <time> #channel <product names (comma-separated)>`  
<:arrow:1290693784790765678> **Sends only the specified products at the given interval to the provided channel**  

<:star_blue:1284898459232763944> **Stop Stock/Products :-**  
<:white_arrow:1290693789824061461> `.stop_sending <stock/products>`  
<:arrow:1290693784790765678> **Stops the automated sending of stock or specific products**""")

    elif category.lower() == "extra":
        await ctx.send(f"""# <:Discord_bots:1290700055514452121> **EXTRA COMMANDS :-**
<:white_arrow:1290693789824061461>**Gen Joke** :- `.joke`
<:white_arrow:1290693789824061461>**Gen Meme** :- `.meme`
<:white_arrow:1290693789824061461>**Check Promo** :- `.checkpromo <promo>`
<:white_arrow:1290693789824061461>**Check Token** :- `.checktoken <token>`
<:white_arrow:1290693789824061461>**Snipe Deleted Msg** :- `.snipe`
<:white_arrow:1290693789824061461>**Translate Msg** :- `.translate <msg>`
<:white_arrow:1290693789824061461>**Magic 8 Ball** :- `.magic8ball <question>`
<:white_arrow:1290693789824061461>**Trivia** :- `.trivia`
<:white_arrow:1290693789824061461>**Would You Rather (WYR)** :- `.wyr`
<:white_arrow:1290693789824061461>**Dog Fact** :- `.dog`
<:white_arrow:1290693789824061461>**Spotify Search** :- `.spotify <song>`
<:white_arrow:1290693789824061461>**Mass React** :- `.masdmfriends <message>`
**Mass Dm** :- `.massreact <message>`
<:white_arrow:1290693789824061461>**Random Fact** :- `.fact`
<:white_arrow:1290693789824061461>**Quotes** :- `.quotes`
<:white_arrow:1290693789824061461>**Mock** :- `.mock <@user>`
<:white_arrow:1290693789824061461>**Stop Mock** :- `.stop_mock`
<:white_arrow:1290693789824061461>**Chess Game** :- `.chess <@user>`
<:white_arrow:1290693789824061461>**Close Chess Game** :- `.chessc`
<:white_arrow:1290693789824061461>**Tic-Tac-Toe** :- `.tictactoe <@user>`
<:white_arrow:1290693789824061461>**Blackjack** :- `.blackjack`
<:white_arrow:1290693789824061461>**Poker** :- `.poker`
<:white_arrow:1290693789824061461>**Hangman** :- `.hangman`
<:white_arrow:1290693789824061461>**TTS** :- `.tts <message>`
<:white_arrow:1290693789824061461>**Time Travel** :- `.time_travel <date>`
<:white_arrow:1290693789824061461>**Clean DM** :- `.clean_dm`
<:white_arrow:1290693789824061461>**Dashboard** :- `.dashboard`
<:white_arrow:1290693789824061461>**Emoji Animator** :- `.emoji_animator <emoji>`
<:white_arrow:1290693789824061461>**Vanity Checker** : `.vanity_check <url>`""")

    elif category.lower() == "fun":
        await ctx.send(f"""# <:botupdate:1290700047629160508> **FUN COMMANDS :-**
<:white_arrow:1290693789824061461>**LOVERATE** : `.loverate`
<:white_arrow:1290693789824061461>**GAYRATE** : `.gayrate`
<:white_arrow:1290693789824061461>**RANDI RATE** : `.randirate`
<:white_arrow:1290693789824061461>**SIMP RATE** : `.simprate`
<:white_arrow:1290693789824061461>**THARKI RATE** : `.tharki`
<:white_arrow:1290693789824061461>**KISS** : `.kiss @user`  
<:white_arrow:1290693789824061461>**SLAP** : `.slap @user`  
<:white_arrow:1290693789824061461>**CUDDLE** : `.cuddle @user`  
<:white_arrow:1290693789824061461>**HUG** : `.hug @user`  
<:white_arrow:1290693789824061461>**PAT** : `.pat @user`  
<:white_arrow:1290693789824061461>**TICKLE** : `.tickle @user`  
<:white_arrow:1290693789824061461>**POKE** : `.poke @user`  
<:white_arrow:1290693789824061461>**SMUG** : `.smug`  
<:white_arrow:1290693789824061461>**BAKA** : `.baka @user`  
<:white_arrow:1290693789824061461>**FEED** : `.feed @user`  
<:white_arrow:1290693789824061461>**FOX GIRL** : `.foxgirl`  
<:white_arrow:1290693789824061461>**NEKO** : `.neko`  
<:white_arrow:1290693789824061461>**WAIFU** : `.waifu`
<:white_arrow:1290693789824061461>**NSFW** : `.nsfw`
<:arrow:1290693784790765678> **USE AT YOUR OWN RISK <a:LaughtPepe:1281243496136573011>**
<:white_arrow:1290693789824061461>**QUESTIONS GAME** : `.questions_game`
<:white_arrow:1290693789824061461>**ROLL A DICE** : `.roll`
<:white_arrow:1290693789824061461>**FLIP A COIN** : `.coinflip`
<:white_arrow:1290693789824061461>**GENERATE A RANDOM NUMBER** : 
<:kronix_dot:1281280217335332966>`.generate_random_num <min> <max>`
<:white_arrow:1290693789824061461>**TRUTH** : `.truth`
<:white_arrow:1290693789824061461>**DARE** : `.dare`
<:white_arrow:1290693789824061461>**SHIP** : `.ship <name1> <name2>`
<:white_arrow:1290693789824061461>**MAGIC NUMBER** : `.magicnumber`
<:white_arrow:1290693789824061461>**GUESS GAME** : `.guessgame`
<:white_arrow:1290693789824061461>**FAKE NITRO** : `.nitro`
<:white_arrow:1290693789824061461>**CHESS WITH BOT** : `.chessgame`
<:white_arrow:1290693789824061461>**CLOSS CHESS GAME** : `.chessgamec`
<:white_arrow:1290693789824061461>**RATE** : `.rate <thing>`
<:white_arrow:1290693789824061461>**INSULT** : `.insult <name>`
<:white_arrow:1290693789824061461>**COMPLIMENT** : `.compliment <name>`
<:white_arrow:1290693789824061461>**RANDOM COLOR** : `.randomcolor`
<:white_arrow:1290693789824061461>**ROLL COIN** : `.rollcoin`
<:white_arrow:1290693789824061461>**WORD JUMBLE** : `.wordjumble <word>`
<:white_arrow:1290693789824061461>**MOTIVATE** : `.motivate`
<:white_arrow:1290693789824061461>**PORNHUB LOGO :-** `.phlogo [text1] [text2]`  
<:white_arrow:1290693789824061461>**PORNHUB COMMENT :-** `.phcomment [name] [comment]`""")

    elif category.lower() == "wizz":
        await ctx.send(f"""# <a:Nuking_Residence:1308833239670198314> NUKEZ CMDZ :-
<:white_arrow:1290693789824061461> **Nuke Server** :-  
<:kronix_dot:1281280217335332966> `.destroy <channel_name>, <webhook_name>, <no of channels>`  
<:arrow_blue:1281246700358471722> **FU*KS THE SERVER BY CREATING CUSTOM CHANNELS AND SPAM THEM, Creating more than 70-80 channels may cause rate limit**  

<:white_arrow:1290693789824061461> **Spam All Channels** :-  
<:kronix_dot:1281280217335332966> `.cwebhookall`  
<:arrow_blue:1281246700358471722> `SPAMS ALL THE CHANNEL OF SERVER`  

<:white_arrow:1290693789824061461> **Delete All Roles** :-  
<:kronix_dot:1281280217335332966> `.delete_all_role`  
<:arrow_blue:1281246700358471722> `DELETES ALL ROLES IN THE SERVER`

<:white_arrow:1290693789824061461>**Create Channels** :- `.create_chs <name>`
<:kronix_dot:1281280217335332966> `Create 100 channels in server`

<:white_arrow:1290693789824061461>**Delete Channels** :- `.delete_all_chs`
<:kronix_dot:1281280217335332966> `Deletes all the channels`

<:white_arrow:1290693789824061461>**Spam Channels** :- `.spam_chs <msg>`
<:kronix_dot:1281280217335332966> `Spam all the channels`

<:white_arrow:1290693789824061461>**Prune members** :- `.prune <time>`
<:kronix_dot:1281280217335332966> `Prune inactive users eg. prune 1h`

<:white_arrow:1290693789824061461>**Ban All** :- `.ban_all`
<:kronix_dot:1281280217335332966> `Bans everyone from server`

<:white_arrow:1290693789824061461>**Kick All** :- `.kick_all`
<:kronix_dot:1281280217335332966> `kicks everyone from server`

<:white_arrow:1290693789824061461>**Mute All** :- `.mute_all`
<:kronix_dot:1281280217335332966> `Timeouts everyone in server`""")

    elif category.lower() == "mod":
        await ctx.send(f"""# <a:developer:1290928018793037844> MOD HELP :-
<:white_arrow:1290693789824061461> **Role** :- `role @user <role>`
<:white_arrow:1290693789824061461> **Remove Role** :- `remove_role @user`
<:white_arrow:1290693789824061461> **Kick** :- `kick @user`
<:white_arrow:1290693789824061461> **Mute** :- `.mute <@user> <duration> <unit(m/h/d)> [reason]`
<:white_arrow:1290693789824061461> **UnMute** :- `.unmute <@user>`
<:white_arrow:1290693789824061461> **Hide Channel** :- `.hide <@user/@role>`
<:white_arrow:1290693789824061461> **Unhide Channel** :- `.unhide <@user/@role>`
<:white_arrow:1290693789824061461> **Hide All Channels** :- `.hideall <@user/@role>`
<:white_arrow:1290693789824061461> **Unhide All Channels** :- `.unhideall <@user/@role>`
<:white_arrow:1290693789824061461> **Role All** :- `.role_all <@role>`
<:white_arrow:1290693789824061461> **Role All Users** :- `.roleusers <@role>`
<:white_arrow:1290693789824061461> **Role All Bots** :- `.rolebots <@role>`
<:white_arrow:1290693789824061461> **Create Role** :- `.create_role <name>`
<:white_arrow:1290693789824061461> **Delete Role** :- `.delete_role <name>`
<:white_arrow:1290693789824061461> **Rename Role** :- `.renamerole <role> <new_name>`
<:white_arrow:1290693789824061461> **Rename Channel** :- `.rename_channel <new_name>`
<:white_arrow:1290693789824061461> **Create Category** :- `.create_category <name>`
<:white_arrow:1290693789824061461> **Delete Channel** :- `.delete_channel <channel>`
<:white_arrow:1290693789824061461> **Set Channel Topic** :- `.set_topic <topic>`
<:white_arrow:1290693789824061461> **Add Reaction** :- `.react <message_id> <emoji>`
<:white_arrow:1290693789824061461> **Remove Reaction** :- `.unreact <message_id> <emoji>`
<:white_arrow:1290693789824061461> **Softban** :- `.softban @user <reason>`
<:white_arrow:1290693789824061461> **Temp Ban** :- `.tempban @user <duration> <reason>`
<:white_arrow:1290693789824061461> **Slowmode** :- `.slowmode <seconds>`
<:white_arrow:1290693789824061461> **Role Info** :- `.roleinfo <role>`
<:kronix_dot:1281280217335332966> **Can create more than one channel**
<:arrow:1290693784790765678> **Eg :-** `.create_channels <name_1>, <name_2>, <name_3>`
<:white_arrow:1290693789824061461> **Nick** :- `.nick @user`
<:white_arrow:1290693789824061461> **Nick All** :- `.nick_all`
<:white_arrow:1290693789824061461> **SET SERVER NAME** :- `.server_name <name>`
<:white_arrow:1290693789824061461> **SET SERVER ICON** :- `.server_icon <image>`
<:white_arrow:1290693789824061461> **SET SERVER BANNER** :- `.server_banner <image>`
<:white_arrow:1290693789824061461> **PING SPOOF** :- `.ping_spoof <enable/disable>`
<:white_arrow:1290693789824061461> **Ping Webhook** :- `.ping_webhook <url>`
<:white_arrow:1290693789824061461> **Ban List** :- `.ban_list`
<:white_arrow:1290693789824061461> **Unban All** :- `.unban_all`
<:white_arrow:1290693789824061461> **Delete All Emojis** :- `.deleteallemojis`
<:white_arrow:1290693789824061461> **Warn User** :- `.warn_user @user <reason>`
<:white_arrow:1290693789824061461> **View Invites** :- `.view_invites`
<:white_arrow:1290693789824061461> **Auto Kick** :- `.auto_kick <days>`
<:white_arrow:1290693789824061461> **Check Permissions** :- `.check_permissions @user`
<:white_arrow:1290693789824061461> **Message Logs** :- `.message_logs @user`
<:white_arrow:1290693789824061461> **Disable Invites** :- `.disable_invites`
<:white_arrow:1290693789824061461> **Protect Role** :- `.protect_role <@role>`
<:white_arrow:1290693789824061461> **Audit Logs** :- `.audit_logs`
<:white_arrow:1290693789824061461> **Channel Status** :- `.channel_status`
<:white_arrow:1290693789824061461> **Role Backup** :- `.role_backup`
<:white_arrow:1290693789824061461> **Restore Roles** :- `.restore_roles`
<:white_arrow:1290693789824061461> **DM All** :- `.dm_all <message>`""")

    elif category.lower() == "msg":
        await ctx.send(f"""# <:sq_heartmsg:1290693802713157632> **MSG COMMANDS :-**
<:white_arrow:1290693789824061461>**Spam Msg** :- `.spam <amount> <msg>`
<:white_arrow:1290693789824061461>**Stop Spam Msg** :- `.stop_spam`  
<:white_arrow:1290693789824061461>**Clear Msg** :- `.clear <amount>`  
<:white_arrow:1290693789824061461>**Direct Msg** :- `.dm <@user> <msg>`  
<:white_arrow:1290693789824061461>**Send Msg Ticket Create** :-  
<:kronix_dot:1281280217335332966> `.sc <cg-id> <msg>`  
<:white_arrow:1290693789824061461>**Remove Msg Ticket Create** :-  
<:kronix_dot:1281280217335332966> `.stopsc <cg-id>`  
<:white_arrow:1290693789824061461>**Edit Msg Ticket Create** :-  
<:kronix_dot:1281280217335332966> `.editsc <cg-id> <new-msg>`  
<:white_arrow:1290693789824061461>**List Active Ticket Messages** :-  
<:kronix_dot:1281280217335332966> `.listsc`  
<:white_arrow:1290693789824061461>**Pause Msg Ticket Create** :-  
<:kronix_dot:1281280217335332966> `.pausesc <cg-id>`  
<:white_arrow:1290693789824061461>**Resume Msg Ticket Create** :-  
<:kronix_dot:1281280217335332966> `.resumesc <cg-id>`  
<:white_arrow:1290693789824061461>**Clear All Ticket Messages** :-  
<:kronix_dot:1281280217335332966> `.clearsc`  
<:white_arrow:1290693789824061461>**Set Delay for Ticket Msg** :-  
<:kronix_dot:1281280217335332966> `.delaysc <cg-id> <seconds>`
<:white_arrow:1290693789824061461>**Edit Msg** :- `.edit <message_id> <new_content>`  
<:white_arrow:1290693789824061461>**Delete Msg** :- `.delete <message_id>`  
<:white_arrow:1290693789824061461>**Quote Msg** :- `.quote <message_id>`  
<:white_arrow:1290693789824061461>**Pin Msg** :- `.pin <message_id>`  
<:white_arrow:1290693789824061461>**Unpin Msg** :- `.unpin <message_id>`  
<:white_arrow:1290693789824061461>**Snipe Deleted Msg** :- `.snipe`  
<:white_arrow:1290693789824061461>**Edit Snipe Msg** :- `.editsnipe`  
<:white_arrow:1290693789824061461>**Purge Msgs** :- `.purge <amount>`  
<:white_arrow:1290693789824061461>**Find Msg** :- `.find <keyword>`  
<:white_arrow:1290693789824061461>**React to Msg** :- `.react <message_id> <emoji>`  
<:white_arrow:1290693789824061461>**Reverse Msg** :- `.reverse <msg>`  
<:white_arrow:1290693789824061461>**Caps Msg** :- `.caps <msg>`  
<:white_arrow:1290693789824061461>**Small Msg** :- `.small <msg>`  
<:white_arrow:1290693789824061461>**Repeat Msg** :- `.repeat <msg> <times>`  
<:white_arrow:1290693789824061461>**Emoji Msg** :- `.emoji <msg>`  
<:white_arrow:1290693789824061461>**Spoiler Msg** :- `.spoiler <msg>`  
<:white_arrow:1290693789824061461>**Split Msg** :- `.split <msg>`  
<:white_arrow:1290693789824061461>**Highlight Word in Msg** :- `.highlight <word> <msg>`  
<:white_arrow:1290693789824061461>**Count Word in Msg** :- `.count <word>`  
<:white_arrow:1290693789824061461>**Delete After Msg** :- `.deleteafter <seconds> <msg>`  
<:white_arrow:1290693789824061461>**Bold Msg** :- `.bold <msg>`  
<:white_arrow:1290693789824061461>**Italic Msg** :- `.italic <msg>`  
<:white_arrow:1290693789824061461>**Underline Msg** :- `.underline <msg>`  
<:white_arrow:1290693789824061461>**Strike Msg** :- `.strike <msg>`  
<:white_arrow:1290693789824061461>**Code Block Msg** :- `.codeblock <msg>`  
<:white_arrow:1290693789824061461>**Multi-line Code Block Msg** :- `.multicode <msg>`  
<:white_arrow:1290693789824061461>**Blockquote Msg** :- `.blockquote <msg>`  
<:white_arrow:1290693789824061461>**Combine Msgs** :- `.combine <msg1> <msg2>`
<:white_arrow:1290693789824061461>**EMOJIFY** : `.emojify <text>`
<:white_arrow:1290693789824061461>**FLIP TEXT** : `.fliptext <text>`
<:white_arrow:1290693789824061461>**SAVE AS TEXT FILE** : `.txt <text>`""")

    elif category.lower() == "sniper":
        await ctx.send(f"""# <:Crown_king:1281280214600515635> SNIPER CMDZ :-
<a:re_Cyan_arrow:1281246688853622877> **Use snipers on own risk !**

<a:tz_Nitro:1281238104916889652> **__NITRO SNIPER__**
<:white_arrow:1290693789824061461> **NITRO :** `.nitro_sniper <enable/disable>`
<:white_Arrow:1290693791983861822> **ENABLES NITRO SNIPER**
<:white_arrow:1290693789824061461> **NITRO WEBHOOK :** `.nwebhook <url>`
<:white_Arrow:1290693791983861822> **SETS WEBHOOK FOR NITRO SNIPER**
<:white_arrow:1290693789824061461> **ALT STATUS :** `.alt_sniper_status`
<:white_Arrow:1290693791983861822> **SNIPES NITRO FROM ALT AND CLAIM IN YOUR MAIN ACCOUNT**

<a:tz_pink_money:1281241579893428297> **__GIVEAWAY SNIPER__**
<:white_arrow:1290693789824061461> **GIVEAWAY :** `.giveaway_sniper <enable/disable>`
<:white_Arrow:1290693791983861822> **ENABLES GIVEAWAY SNIPER**
<:white_arrow:1290693789824061461> **GIVEAWAY WEBHOOK :** `.gwebhook <url>`
<:white_Arrow:1290693791983861822> **SETS WEBHOOK FOR GIVEAWAY SNIPER**

<:note:1290693795763195945> **__PRIVATE NOTE SNIPER__**
<:white_arrow:1290693789824061461> **PRIVNOTE :** `.privnote_sniper <enable/disable>`
<:white_Arrow:1290693791983861822> **ENABLES PRIVNOTE SNIPER**
<:white_arrow:1290693789824061461> **PRIVNOTE WEBHOOK :** `.pwebhook <url>`
<:white_Arrow:1290693791983861822> **SETS WEBHOOK FOR PRIVNOTE SNIPER**""")

    elif category.lower() == "developer":
        await ctx.send(f"""# <:devs:1290693770567749652> DEVELOPER CMDZ
<:white_arrow:1290693789824061461>**FORMAT CODE** : `.formatcode`
<:white_arrow:1290693789824061461>**HASH GENERATOR** : `.hash <algorithm> <text>`
<:white_arrow:1290693789824061461>**IP GEOLOCATION** : `.geoip <ip>`
<:white_arrow:1290693789824061461>**RGB TO HEX** : `.rgbtohex <r> <g> <b>`
<:white_arrow:1290693789824061461>**HEX TO RGB** : `.hextorgb <hex>`
<:white_arrow:1290693789824061461>**QR CODE GENERATOR** : `.qrcode <text>`
<:white_arrow:1290693789824061461>**RANDOM PASSWORD** : `.genpass <length>`
<:white_arrow:1290693789824061461>**HTML ENCODE** : `.htmlencode <text>`
<:white_arrow:1290693789824061461>**HTML DECODE** : `.htmldecode <text>`
<:white_arrow:1290693789824061461>**TEMP MAIL CHECKER** : `.checkemail <email>`
<:white_arrow:1290693789824061461>**TEXT REVERSER** : `.reverse <text>`
<:white_arrow:1290693789824061461>**ENCRYPT TEXT** : `.encrypt <text>`
<:white_arrow:1290693789824061461>**DECRYPT TEXT** : `.decrypt <encoded_text>`
<:white_arrow:1290693789824061461>**JSON FORMATTER** : `.jsonformat <json_string>`
<:white_arrow:1290693789824061461>**EVALUATE PYTHON** : `.evaluate <code>`
<:white_arrow:1290693789824061461>**PING TEST** : `.pingtest`""")

    elif category.lower() == "seller":
        await ctx.send(f"""# <:experienced_seller:1290924799421583391> **SELLER COMMANDS :-**
<:white_arrow:1290693789824061461>**Vouch** :- `.vouch <product for price>`
<:white_arrow:1290693789824061461>**Exch Vouch** :- `.exch <which to which>`
<:white_arrow:1290693789824061461>**Custom Vouch** :- `.cvouch <product>, [price]`
<:white_arrow:1290693789824061461>**Create Custom Vouch** :- `.cvouch_create <product>, <price>`
<:white_arrow:1290693789824061461>**Set Vouch Format** :- `.vouch_format`
<:white_arrow:1290693789824061461>**Set Exch Vouch Format** :- `.exch_format`
<:white_arrow:1290693789824061461>**Set Custom Vouch Format** :- `.cvouch_format`
<:white_arrow:1290693789824061461>**Set Vouch Message** :- `.vouch_msg`
<:white_arrow:1290693789824061461>**Set Exch Vouch Message** :- `.exch_msg`
<:white_arrow:1290693789824061461>**Calculate** :- `.math <equation>`
<:white_arrow:1290693789824061461>**INR To Crypto** :- `.i2c <inr amount>`
<:white_arrow:1290693789824061461>**Crypto To INR** :- `.c2i <crypto amount>`
<:white_arrow:1290693789824061461>**USD To EUR** :- `.u2e <usd amount>`
<:white_arrow:1290693789824061461>**EUR To USD** :- `.e2u <eur amount>`
<:white_arrow:1290693789824061461>**Transaction Check** :- `.cryptotx <txid>`
<:white_arrow:1290693789824061461>**LTC Tx History** : `.txhistory <addy>`
<:white_arrow:1290693789824061461>**UPI ID** :- `.upi`
<:white_arrow:1290693789824061461>**UPI 2** :- `.upi2`
<:white_arrow:1290693789824061461>**QR Code** :- `.qr`
<:white_arrow:1290693789824061461>**Custom QR** :- `.upiqr <amt> <note>`
<:white_arrow:1290693789824061461>**Upi2 QR** :- `.upiqr2 <amt> <note>`
<:white_arrow:1290693789824061461>**Litecoin QR** :- `.ltcqr <wallet_num> <amount>`
<:white_arrow:1290693789824061461>**Permanent Note** :- `.set_note <note>`
<:Money:1290693788226027654> **TYPE `.h crypto` TO GET PRICES **""")

    elif category.lower() == "antinuke":
        await ctx.send(f"""# <:lr_tick_1:1290693800808677461> ANTINUKE CMDZ :-

<:white_arrow:1290693789824061461>**ANTINUKE ENABLE :** `.antinuke_enable`
- Enables the anti-nuke system for the server.

<:white_arrow:1290693789824061461>**ANTINUKE DISABLE :** `.antinuke_disable`
- Disables the anti-nuke system for the server.

<:white_arrow:1290693789824061461>**ANTINUKE STATUS :** `.antinuke_status`
- Shows details and the current status of anti-nuke settings.

<:white_arrow:1290693789824061461>**ANTINUKE LOGGING :** `.antinuke_logging <#channel>`
- Set up a channel for anti-nuke event logs.

<:white_arrow:1290693789824061461>**ANTINUKE PUNISHMENT :** `.antinuke_punishment <action>`
- Change the punishment for anti-nuke triggers (e.g., `ban`, `kick`, or `remove roles`).

<:white_arrow:1290693789824061461>**ANTINUKE PUNISHMENT SET :** `.antinuke_punishment_set <action>`
- Sets the default punishment for the anti-nuke system.

<:white_arrow:1290693789824061461>**WHITELIST USER :** `.antinuke_whitelist <@user>`
- Whitelist a trusted user to bypass anti-nuke triggers.

<:white_arrow:1290693789824061461>**WHITELIST ADD :** `.antinuke_whitelist_add <@user> <specific_field>`
- Add a user to the whitelist for specific actions (e.g., `anti_channel_create`).

<:white_arrow:1290693789824061461>**WHITELIST REMOVE :** `.antinuke_whitelist_remove <@user>`
- Remove a user from the whitelist.

<:white_arrow:1290693789824061461>**WHITELIST RESET :** `.antinuke_whitelist_reset`
- Removes all users from the whitelist.

<:white_arrow:1290693789824061461>**ANTI ROLE CREATION :** `.anti_role_create`
- Enables/Disables anti-role creation protection.

<:white_arrow:1290693789824061461>**ANTI ROLE DELETION :** `.anti_role_delete`
- Enables/Disables anti-role deletion protection.

<:white_arrow:1290693789824061461>**ANTI ROLE UPDATE :** `.anti_role_update`
- Enables/Disables anti-role update protection.

<:white_arrow:1290693789824061461>**ANTI CHANNEL CREATION :** `.anti_channel_create`
- Enables/Disables anti-channel creation protection.

<:white_arrow:1290693789824061461>**ANTI CHANNEL DELETION :** `.anti_channel_delete`
- Enables/Disables anti-channel deletion protection.

<:white_arrow:1290693789824061461>**ANTI CHANNEL UPDATE :** `.anti_channel_update`
- Enables/Disables anti-channel update protection.

<:white_arrow:1290693789824061461>**ANTI BAN :** `.anti_ban`
- Enables/Disables anti-ban protection.

<:white_arrow:1290693789824061461>**ANTI KICK :** `.anti_kick`
- Enables/Disables anti-kick protection.

<:white_arrow:1290693789824061461>**ANTI WEBHOOK :** `.anti_webhook`
- Enables/Disables anti-webhook creation and modification protection.

<:white_arrow:1290693789824061461>**ANTI BOT :** `.anti_bot`
- Enables/Disables anti-bot addition protection.

<:white_arrow:1290693789824061461>**ANTI SERVER UPDATE :** `.anti_server`
- Enables/Disables anti-server settings modification protection.

<:white_arrow:1290693789824061461>**ANTI PING :** `.anti_ping`
- Enables/Disables mass ping protection.

<:white_arrow:1290693789824061461>**ANTI EMOJI CREATION :** `.anti_emoji_create`
- Enables/Disables anti-emoji creation protection.

<:white_arrow:1290693789824061461>**ANTI EMOJI DELETION :** `.anti_emoji_delete`
- Enables/Disables anti-emoji deletion protection.

<:white_arrow:1290693789824061461>**ANTI EMOJI UPDATE :** `.anti_emoji_update`
- Enables/Disables anti-emoji update protection.

<:white_arrow:1290693789824061461>**ANTI MEMBER ROLE UPDATE :** `.anti_member_role_update`
- Enables/Disables anti-member role update protection.""")

    elif category.lower() == "wallet":
        await ctx.send(f"""# <a:tz_ltc:1281238097136451616> **LTC SELF WALLET :-**
<a:tz_ltc:1281238097136451616> **Send Ltc** :- `.send <wallet_num> <addy> <amount>`
<a:tz_ltc:1281238097136451616> **Check Wallet bal** :- `.mybal <wallet num>`
<a:tz_ltc:1281238097136451616> **Check Balance** :- `.bal <addy>`
<a:tz_ltc:1281238097136451616> **Ltc Addy** :- `.addy <wallet num>`
<a:tz_ltc:1281238097136451616> **LTC TX Check** :- `.ltctx <txid>`
<a:tz_ltc:1281238097136451616> **Wallet History** :- `.wallet_history`
<:white_arrow:1290693789824061461>**Last Tx** : `.mytxhistory <wallet_num>`
<a:tz_ltc:1281238097136451616> **Ltc To Usd** :- `.l2u <ltc amount>`
<a:tz_ltc:1281238097136451616> **Usd To Ltc** :- `.u2l <usd amount>`
<:white_arrow:1290693789824061461>**Ltc Price** :- `.ltcprice`

**Use `.cwallet <wallet num>` command to automatically create a ltc wallet with Ltc address & Private key ! <:tz_Verified:1281238102823665797>**

---

<:Frostmm_USDT:1378242966388215922> **USDT (TRC20) SELF WALLET :-**
<:Frostmm_USDT:1378242966388215922> **Send USDT** :- `.sendusdt <wallet_num> <addy> <amount>`
<:Frostmm_USDT:1378242966388215922> **Check Wallet bal** :- `.myubal <wallet num>`
<:Frostmm_USDT:1378242966388215922> **Check Balance** :- `.ubal <address>`
<:Frostmm_USDT:1378242966388215922> **USDT Addy** :- `.usdtaddy <wallet num>`""")

    elif category.lower() == "boost":
        await ctx.send(f"""# <:tz_Boost_icon:1281241573035868220> Boost Tool  
<:white_arrow:1290693789824061461> **Check Stock**: `.stock`  
<:Titanz:1281243491476967447> **Shows stock of 1M & 3M Nitro tokens**  

<:white_arrow:1290693789824061461> **Add Stock**: `.add_stock <1/3>`  
<:Titanz:1281243491476967447> **Adds Nitro tokens to stock**  

<:white_arrow:1290693789824061461> **Boost Server**: `.boost <1/3> <server_link> <num_of_tokens>`  
<:Titanz:1281243491476967447> **Uses tokens to boost a server (2 boosts per token)**  

<:white_arrow:1290693789824061461> **Proxy Boost**: `.proxy_boost <server_link> <num_of_tokens>`  
<:Titanz:1281243491476967447> **Boosts using proxies**  

<:white_arrow:1290693789824061461> **Export Stock**: `.export_stock <1/3>`  
<:Titanz:1281243491476967447> **Exports available stock**  

<:white_arrow:1290693789824061461> **Reset Stock**: `.reset_stock <1/3>`  
<:Titanz:1281243491476967447> **Clears all tokens from stock**  

<:white_arrow:1290693789824061461> **Boost Status**: `.boost_status <server_id>`  
<:Titanz:1281243491476967447> **Shows the number of boosts on a server**  

<:white_arrow:1290693789824061461> **Check Token**: `.check <token>`  
<:Titanz:1281243491476967447> **Checks if a token is valid and has Nitro**""")

    elif category.lower() == "nsfw":
        await ctx.send(f"""# <:tharkimon:1291420565911113809> **NSFW COMMANDS :-**  
<:white_arrow:1290693789824061461>**HENTAI RANDOM :-** `.hrandom`  
<:white_arrow:1290693789824061461>**ANAL SEX :-** `.anal`
<:white_arrow:1290693789824061461>**ASS :-** `.ass`  
<:white_arrow:1290693789824061461>**BOOBS :-** `.boobs`  
<:white_arrow:1290693789824061461>**PUSSY :-** `.pussy`  
<:white_arrow:1290693789824061461>**4K :-** `._4k`  
<:white_arrow:1290693789824061461>**NSFW GIF :-** `.pgif`  
<:white_arrow:1290693789824061461>**NSFW PIC :-** `.pic`  
<:white_arrow:1290693789824061461>**THIGH :-** `.thigh`  
<:white_arrow:1290693789824061461>**HOLO :-** `.holo`  
<:white_arrow:1290693789824061461>**COSPLAY :-** `.cosplay`  
<:white_arrow:1290693789824061461>**HENTAI THIGH :-** `.hthigh`  
<:white_arrow:1290693789824061461>**LEWD :-** `.lewd`  
<:white_arrow:1290693789824061461>**HENTAI :-** `.hentai`  
<:white_arrow:1290693789824061461>**HENTAI ANAL :-** `.hanal`  
<:white_arrow:1290693789824061461>**WILD :-** `.wild`  
<:white_arrow:1290693789824061461>**FEET :-** `.feet`  
<:white_arrow:1290693789824061461>**HENTAI BOOBS :-** `.hboobs`  
<:white_arrow:1290693789824061461>**HENTAI ASS :-** `.hass`""")

    elif category.lower() == "misc":
        await ctx.send(f"""# <:Blue_Crown_temp:1281973607937085614> MISCELLANEOUS COMMANDS
<:white_arrow:1290693789824061461> **Countdown:** `.countdown <seconds>`  
<:white_arrow:1290693789824061461> **Reverse Image:** `.reverse_image <image_url>`  
<:white_arrow:1290693789824061461> **Reverse Geocode:** `.reverse_geocode <latitude> <longitude>`  
<:white_arrow:1290693789824061461> **Emoji Count:** `.emoji_count`  
<:white_arrow:1290693789824061461> **Random Cat Fact:** `.random_cat_fact`  
<:white_arrow:1290693789824061461> **ASCII QR Code:** `.ascii_qr_code <text>`    
<:white_arrow:1290693789824061461> **ASCII Binary:** `.ascii_binary <text>`  
<:white_arrow:1290693789824061461> **Server Stats:** `.show_server_stats`  
<:white_arrow:1290693789824061461> **Random Urban Legend:** `.random_urban_legend`  
<:white_arrow:1290693789824061461> **Weather Alert:** `.weather_alert <city>`  
<:white_arrow:1290693789824061461> **Short URL:** `.short_url <long_url>`  
<:white_arrow:1290693789824061461> **GIF Search:** `.gif_search <query>`  
<:white_arrow:1290693789824061461> **Random Recipe:** `.random_recipe`    
<:white_arrow:1290693789824061461> **Horoscope:** `.horoscope <zodiac_sign>`  
<:white_arrow:1290693789824061461> **Chuck Norris Joke:** `.chuck_norris`  
<:white_arrow:1290693789824061461> **Dad Joke:** `.dad_joke`  
<:white_arrow:1290693789824061461> **Inspire Me:** `.inspire_me`  
<:white_arrow:1290693789824061461> **Pi Digits:** `.pi_digits <number_of_digits>`  
<:white_arrow:1290693789824061461> **Roll Dice:** `.roll_dice <number_of_sides>`  
<:white_arrow:1290693789824061461> **Space Fact:** `.space_fact`  
<:white_arrow:1290693789824061461> **Is Palindrome:** `.is_palindrome <word>`  
<:white_arrow:1290693789824061461> **Urban Dictionary:** `.urban_dictionary <word>`  
<:white_arrow:1290693789824061461> **IP Lookup:** `.ip_lookup <ip_address>`  
<:white_arrow:1290693789824061461> **Pokémon Info:** `.pokemon <name>`  
<:white_arrow:1290693789824061461> **Random Movie:** `.random_movie`  
<:white_arrow:1290693789824061461> **Hash String:** `.hash_string <text>`  
<:white_arrow:1290693789824061461> **Image to ASCII:** `.image_to_ascii <image_url>`  
<:white_arrow:1290693789824061461> **Emoji to Name:** `.emoji_to_name <emoji>`  
<:white_arrow:1290693789824061461> **Random User:** `.random_user`""")

    elif category.lower() == "spy":
        await ctx.send(f"""# <:Black_Hearts:1288196136544243733> SPY COMMANDS :-
<:white_arrow:1290693789824061461> **SPY USER :** `.spy_user @user`  
<:white_arrow:1290693789824061461> **CLOSE SPY :** `.close_spy @user`  
<:white_arrow:1290693789824061461> **SPY LIST :** `.spy_list`  
<:white_arrow:1290693789824061461> **CLEAR SPY :** `.clear_spy`  
<:white_arrow:1290693789824061461> **SET WEBHOOK :** `.spy_webhook <url>`

<:rdx_glowin_heart:1288196137848803451> **SPY COMMANDS TRACK FOLLOWING :-**
<:white_arrow:1290693789824061461> **MESSAGE SENT** - Tracks every message sent by the user in the server.
<:white_arrow:1290693789824061461> **MESSAGE EDIT** - Monitors any edits made to messages.
<:white_arrow:1290693789824061461> **MESSAGE DELETED** - Keeps track of deleted messages.
<:white_arrow:1290693789824061461> **REACTION ADDED** - Tracks when the user adds a reaction to a message.
<:white_arrow:1290693789824061461> **REACTION REMOVED** - Monitors when the user removes a reaction.
<:white_arrow:1290693789824061461> **NICKNAME CHANGED** - Tracks any changes made to the user's nickname.
<:white_arrow:1290693789824061461> **SERVER JOINED/LEFT** - Detects when the user joins or leaves the server.
<:white_arrow:1290693789824061461> **ROLE CHANGED** - Tracks when the user's roles are updated.
<:white_arrow:1290693789824061461> **USER BANNED/KICKED** - Monitors when the user is banned or kicked from the server.
<:white_arrow:1290693789824061461> **TYPING STATUS** - Detects when the user starts or stops typing in a channel.
<:white_arrow:1290693789824061461> **PINNED MESSAGES** - Tracks when a user pins or unpins a message.
<:white_arrow:1290693789824061461> **CHANNEL CREATED/DELETED** - Monitors the creation or deletion of text or voice channels.
<:white_arrow:1290693789824061461> **INVITE CREATED/USED** - Tracks when the user creates or uses an invite link.
<:white_arrow:1290693789824061461> **EMOJI USED** - Monitors when the user sends custom emojis in messages.
<:white_arrow:1290693789824061461> **GAME ACTIVITY** - Detects when the user changes their playing game status or stops playing a game.
<:white_arrow:1290693789824061461> **REACTION ROLE ACTIVITY** - Tracks when the user interacts with reaction role messages.""")

    elif category.lower() == "premium":
        await ctx.send("""# <:nxt_blue_crown:1281973611917348989> SPECIAL COMMANDS  
<:white_arrow:1290693789824061461> **REACTION ROLE :** `.reaction_role <msg_id>`  
<:white_arrow:1290693789824061461> **SET WELCOME :** `.set_welcome #channel_name, Welcome message`  
**Variables :-** `{user}, {server}, {count}`  
<:white_arrow:1290693789824061461> **DISABLE WELCOME :** `.disable_welcome`  
<:white_arrow:1290693789824061461> **TYPING RACE :** `.typing_race`  
<:white_arrow:1290693789824061461> **STICKY NICK :** `.stickynick @user <nickname>`  
<:white_arrow:1290693789824061461> **DISABLE STICKY NICK :** `.stickynick_disable @user`  
<:white_arrow:1290693789824061461> **RESET STICKY NICK :** `.stickynick_reset`  
<:white_arrow:1290693789824061461> **CLEAN CHANNEL :** `.clean 2d`  
<:white_arrow:1290693789824061461> **TASK LIST :** `.tasklist`  
<:white_arrow:1290693789824061461> **ChatGPT** : `.chatgpt <prompt>`
<:white_arrow:1290693789824061461> **Vanity Checker** : `.vanity_check <url>`  
<:white_arrow:1290693789824061461> **Timezone Converter:** `.timezone_converter <time> <from_timezone> <to_timezone>`  
<:white_arrow:1290693789824061461> **Text Art:** `.text_art <text>`  
<:white_arrow:1290693789824061461> **Quiz:** `.quiz`  
<:white_arrow:1290693789824061461> **Poetry:** `.poetry`  
<:white_arrow:1290693789824061461> **Merge Images:** `.merge_images <image_url1> <image_url2>`  
<:white_arrow:1290693789824061461> **Auto Slash Command** : `.autoslashcommand <command>`  
<:white_arrow:1290693789824061461> **Auto Command** : `.autocommand <command>`  
<:white_arrow:1290693789824061461> **Stop Auto Slash Command** : `.stopautoslashcommand`  
<:white_arrow:1290693789824061461> **Stop Auto Command** : `.stopautocommand`  
<:white_arrow:1290693789824061461> **Download Guild Emoji** : `.downloadguildemoji <guild id>`  
<:white_arrow:1290693789824061461> **Add Mass Emoji** : `.massemojiadd <zip file>`  
<:white_arrow:1290693789824061461> **Screenshot** : `.screenshot <url>`  
<:white_arrow:1290693789824061461> **Close All DMs** : `.closealldms`
<:white_arrow:1290693789824061461> **Msg Logger** : `.msg_sniper <enable/disable>`  
<:white_arrow:1290693789824061461> **Msg Webhook** : `.msg_webhook <url>`""")

    elif category.lower() == "info":
        await ctx.send(f"""# <:Ownership:1290692081248895177> INFO CMDZ :-
<:white_arrow:1290693789824061461>**Show Help Menu** :- `.help`
<:white_arrow:1290693789824061461>**Show All Commands** :- `.allcmdz`
<:white_arrow:1290693789824061461>**Support** :- `.support <problem>`
<:white_arrow:1290693789824061461>**Selfbot Info** :- `.selfbot`
<:white_arrow:1290693789824061461>**Selfbot Uptime** :- `.uptime`
<:white_arrow:1290693789824061461>**Ping Latency** :- `.ping`
<:white_arrow:1290693789824061461>**Restart the bot** :- `.restart`
<:white_arrow:1290693789824061461>**Close the bot** :- `.close`
<:white_arrow:1290693789824061461>**Change Acc** :- `.change_account <token>`

<:rules:1290926829762383934> **SET CREDENTIALS :-**
<:white_arrow:1290693789824061461>**UPI :** `.set_upi <upi>`
<:white_arrow:1290693789824061461>**UPI 2** :- `.set_upi2 <upi2>`
<:white_arrow:1290693789824061461>**QR :** `.set_qr <qr>`
<:white_arrow:1290693789824061461>**Server Link :** `.set_serverlink <link>`
<:white_arrow:1290693789824061461>**User ID :** `.set_userid <id>`
<:white_arrow:1290693789824061461>**I2C :** `.set_i2c <rate>`
<:white_arrow:1290693789824061461>**C2I :** `.set_C2I <rate>`
<:white_arrow:1290693789824061461>**Password :** `.set_password <pass>`
<:Titanz:1281243491476967447> **It will not change the actual pass it will change the one in config file **

<:TOS:1336669803221614622>  **Embed System**
<:white_arrow:1290693789824061461>**Embed Mode:** `embedmode enable/disable`
<:white_arrow:1290693789824061461>**Embed Colour:** `embed_colour #hex code`
<:4592developerpurple:1290693776796291163> **You can add your custom name in commands, embed title, footer or even your custom image if you purchase premium version contact siddhu for more info !**

<:RS_LTC:1291423858183897120> **WALLET CREDENTIALS :-**
<:white_arrow:1290693789824061461>**Litecoin Address** :- 
<:kronix_dot:1281280217335332966>`.set_address <wallet num> <new addresss>`
<:white_arrow:1290693789824061461>**Litecoin Private Key** :- 
<:kronix_dot:1281280217335332966>`.set_privatekey <wallet num> <new key>`
<:white_arrow:1290693789824061461>**LTC Webhook** :- `.ltc_webhook`
<:kronix_dot:1281280217335332966> All the ltc transactions will be sent in this webhook !

<:white_arrow:1290693789824061461>**After setting credentials re-start the bot using `.restart` if the change doesn't reflect**

<:rdx_glowin_heart:1288196137848803451> **USER CREDENTIALS :-**
<:white_arrow:1290693789824061461>**Credentials :** `.credentials_info`
<:arrow:1290693784790765678> **Shows the user credentials**
<:white_arrow:1290693789824061461>**Wallet :** `.wallet_info`
<:arrow:1290693784790765678> **Shows ltc wallet addy and private key**

<:note:1290693795763195945> **Don't use these commands in public channel as your info can be stolen by anyone !!**""")

    elif category.lower() == "crypto":
        await ctx.send(f"""# <:OwnerSpecial:1290692086122680321> **CRYPTO PRICES :-**
<:white_arrow:1290693789824061461>**BTC Price** :- `.btcprice`
<:white_arrow:1290693789824061461>**ETH Price** :- `.ethprice`
<:white_arrow:1290693789824061461>**XRP Price** :- `.xrpprice`
<:white_arrow:1290693789824061461>**BNB Price** :- `.bnbprice`
<:white_arrow:1290693789824061461>**ADA Price** :- `.adaprice`
<:white_arrow:1290693789824061461>**Doge Price** :- `.dogeprice`
<:white_arrow:1290693789824061461>**Shib Price** :- `.shibprice`
<:white_arrow:1290693789824061461>**AVAX Price** :- `.avaxprice`
<:white_arrow:1290693789824061461>**Polkadot Price** :- `.polkaprice`
<:white_arrow:1290693789824061461>**Fantom Price** :- `.ftmprice`
<:white_arrow:1290693789824061461>**SOL Price** :- `.solprice`
<:white_arrow:1290693789824061461>**USDT Price** :- `.usdtprice`""")

    else:
        await ctx.send("❌ Unknown help category. Try `.h` to see all modules.")
 
import requests
from discord.ext import commands

@siddhu.command()
async def kalajoke(ctx):
    try:
        response = requests.get("https://peter-api.up.railway.app/api/darkjoke")
        if response.status_code == 200:
            joke = response.text.strip()
            await ctx.send(f"**Dark Joke:**\n{joke}")
        else:
            await ctx.send("❌ Couldn't fetch a joke right now.")
    except Exception as e:
        await ctx.send(f"⚠️ Error occurred: {e}")

import requests
from discord.ext import commands

@siddhu.command(aliases=['gpt'])
async def chatgpt(ctx, *, prompt: str):
    try:
        api_key = "Kastg_Eu6jVbs1eGAqLNsVOJVF_free"
        encoded_prompt = prompt.replace(" ", "+")
        url = f"https://api.kastg.xyz/api/ai/chatgptV4?prompt={encoded_prompt}&key={api_key}"

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            result = data.get("result")

            if result and isinstance(result, list) and "response" in result[0]:
                ai_reply = result[0]["response"]
                await ctx.send(f"<a:emoji_1738757309230:1336669778756239381> **ChatGPT**: {ai_reply}")
            else:
                await ctx.send("❌ Invalid response format from API.")
        else:
            await ctx.send(f"❌ API Error {response.status_code}: {response.text}")
    except Exception as e:
        await ctx.send(f"⚠️ Error occurred: `{e}`")
      
# NITRO GEN
@siddhu.command(aliases=["nitrogen"])
async def nitro(ctx):
    try:
        await ctx.message.delete()
        code = ''.join(
            random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}SUCCESFULLY SENT NITRO CODE !")
    except Exception as e:
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED}ERROR: {str(e)}")
   
@siddhu.command()
async def massdmfriends(ctx, *, message: str):
    """
    Send a direct message to all friends.
    Usage: .massdmfriends <message>
    """
    await ctx.message.delete()  # Deletes the command message for cleanliness
    success_count = 0
    failed_count = 0

    # Iterate through all friends
    for friend in ctx.siddhu.user.friends:
        try:
            await friend.send(message)
            success_count += 1
        except discord.Forbidden:
            failed_count += 1
        except discord.HTTPException as e:
            failed_count += 1
            print(f"Failed to send a message to {friend.name}: {e}")

    await ctx.send(f"<:Tick:1290693799361777665> Sent message to {success_count} friends. <:CROSS_TDG:1321149916201881683> Failed to message {failed_count} friends.")

from datetime import datetime, timedelta

@siddhu.command()
async def time_travel(ctx, *, time_input):
    """
    Calculate time in the past or future from the current moment.
    Example usage:
    `.time_travel +2d` (2 days in the future)
    `.time_travel -3h` (3 hours in the past)
    """
    try:
        # Extracting the numeric value and unit
        modifier, unit = int(time_input[:-1]), time_input[-1].lower()
        now = datetime.utcnow()  # Current UTC time

        # Adjusting the time based on the input
        if unit == "d":
            new_time = now + timedelta(days=modifier)
        elif unit == "h":
            new_time = now + timedelta(hours=modifier)
        elif unit == "m":
            new_time = now + timedelta(minutes=modifier)
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid time unit. Use 'd' for days, 'h' for hours, or 'm' for minutes.")
            return

        # Sending the adjusted time
        await ctx.send(f"🕰 Time adjusted by {modifier} {unit}: **{new_time.strftime('%Y-%m-%d %H:%M:%S')} UTC**")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error processing time input: {e}")

# Command: Clean DM
@siddhu.command()
async def clean_dm(ctx):
    """Deletes all messages from your own DMs."""
    deleted = 0
    while True:
        messages = [msg async for msg in ctx.channel.history(limit=50) if msg.author == siddhu.user]
        if not messages:
            break  # Stop when there are no more messages

        for message in messages:
            try:
                await message.delete()
                deleted += 1
            except discord.Forbidden:
                await ctx.send("<:CROSS_TDG:1321149916201881683> Failed to delete some messages. Permission issue.")
                return

    await ctx.send(f"<:Tick:1290693799361777665> Cleaned {deleted} messages.")

# Command: Personal Dashboard
@siddhu.command()
async def dashboard(ctx):
    """Show a personal dashboard for the user."""
    try:
        user = ctx.author
        joined_servers = len(siddhu.guilds)
        friends_count = len(user.friends) if hasattr(user, "friends") else "N/A"
        messages_sent = 0  # Track this in your bot's logging system if needed
        
        dashboard_message = (
            f"**📊 Personal Dashboard for {user}**\n"
            f"**> 🏢 Servers Joined:** {joined_servers}\n"
            f"**> 👥 Friends Count:** {friends_count}\n"
            f"**> ✉️ Messages Sent (tracked):** {messages_sent}\n"
        )
        await ctx.send(dashboard_message)
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to load dashboard: {e}")

# Command: Fake Typing
@siddhu.command()
async def fake_typing(ctx, duration: int = 5):
    """Simulates typing for a specified duration."""
    async with ctx.typing():
        await asyncio.sleep(duration)
    await ctx.send(f"🖊️ Simulated typing for {duration} seconds.")

# Command: Emoji Animator
@siddhu.command()
async def emoji_animator(ctx, *, emoji_name: str):
    """Displays an animation sequence of an emoji."""
    frames = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
    try:
        for frame in frames:
            await ctx.send(f"{emoji_name} {frame}")
            await asyncio.sleep(0.5)
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> Error animating emoji: {e}")
         
@siddhu.command()
async def massdm(ctx, *, message: str):
    """Send a message to everyone you've interacted with."""
    await ctx.message.delete()  # Delete the command message for privacy
    sent_count = 0
    failed_count = 0

    for user in ctx.siddhu.user.friends:
        try:
            await user.send(message)
            print(f"Message sent to {user.name}#{user.discriminator}")
            sent_count += 1
        except discord.Forbidden:
            print(f"Could not message {user.name}#{user.discriminator} (Forbidden)")
            failed_count += 1
        except Exception as e:
            print(f"Failed to message {user.name}#{user.discriminator}: {e}")
            failed_count += 1

    await ctx.send(f"<:Tick:1290693799361777665> Mass DM completed! Sent: {sent_count}, Failed: {failed_count}")

import discord
from discord.ext import commands
import asyncio

@siddhu.command()
async def edit_line(ctx, line_number: int, *, input_text: str):
    """
    Edit a specific line in the status.txt file.
    Usage: .edit_line <line_number> <Status Message>, <Emoji>
    """
    if not (1 <= line_number <= 5):
        await ctx.send("**Please specify a valid line number between 1 and 5.**")
        return

    # Split the input into message and emoji (if provided)
    try:
        if "," in input_text:
            message, emoji = input_text.rsplit(",", 1)
            emoji_id = emoji.strip().split(":")[-1].strip(">")
            formatted_line = f"{emoji_id}, {message.strip()}"
        else:
            formatted_line = f", {input_text.strip()}"  # No emoji provided, keep blank for emoji ID
    except Exception:
        await ctx.send("**Invalid format. Please use: <Status Message>, <Emoji>.**")
        return

    # Read the current contents of status.txt
    try:
        with open("status.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        await ctx.send("**The status.txt file does not exist. Please configure your statuses first.**")
        return

    # Ensure the file has at least 5 lines
    while len(lines) < 5:
        lines.append("\n")

    # Update the specific line
    lines[line_number - 1] = f"{formatted_line}\n"

    # Save the updated lines back to the file
    with open("status.txt", "w") as f:
        f.writelines(lines)

    await ctx.send(f"**Successfully updated line {line_number} in status.txt!**")

@siddhu.command(name="config_status")
async def config_status(ctx):
    """Configure and save custom statuses."""
    status_file = "status.txt"

    def save_statuses(status_list):
        """Save the status list to status.txt in the correct format."""
        with open(status_file, "w") as f:
            for emoji_id, status_msg in status_list:
                if emoji_id == "None" and status_msg == "None":
                    f.write("\n")  # Completely blank line for None statuses
                else:
                    f.write(f"{emoji_id}, {status_msg}\n")

    async def get_status_input(prompt):
        """Prompt the user for a status input with a timeout."""
        await ctx.send(prompt)
        try:
            response = await siddhu.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=120
            )
            return response.content.strip()
        except asyncio.TimeoutError:
            await ctx.send("Timeout! Configuration process canceled.")
            return None

    statuses = []

    for i in range(1, 6):  # Loop for 5 statuses
        prompt = (
            f"**<:rdx_glowin_heart:1288196137848803451> ENTER YOUR STATUS {i}**\n"
            f"```eg. USING SyntheX Prime V5, 🍁```"
        )
        if i == 1:
            prompt = (
                "**<:rdx_glowin_heart:1288196137848803451> ENTER YOUR STATUS 1**\n"
                "```eg. PLAYING GAME, 🎮```"
            )
        elif i == 2:
            prompt = (
                "**<:rdx_glowin_heart:1288196137848803451> ENTER YOUR STATUS 2**\n"
                "```eg. USING SyntheX Prime V5, 🍁```"
            )
        elif i >= 3:
            prompt += (
                "\nTYPE 'NONE' TO STOP ENTERING STATUSES. THIS WILL CLEAR SUBSEQUENT STATUSES."
            )

        status_input = await get_status_input(prompt)
        if status_input is None:  # Timeout
            return

        if i <= 2 and status_input.lower() == "none":
            await ctx.send(f"Status {i} cannot be None. Please enter a valid status.")
            return
        elif status_input.lower() == "none":
            # Blank out this and subsequent statuses
            statuses.extend([("None", "None")] * (6 - i))
            break
        elif "," in status_input:
            try:
                message, emoji = status_input.split(",", 1)
                emoji = emoji.strip()

                if emoji.startswith("<") and emoji.endswith(">"):
                    # For custom emojis, extract numeric ID
                    emoji_id = emoji.split(":")[-1].strip(">")
                else:
                    # For non-Nitro emojis, use the emoji itself
                    emoji_id = emoji

                statuses.append((emoji_id, message.strip()))
            except ValueError:
                await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid format! Please use `Message, Emoji`.")
                return
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid input! Please include both a message and an emoji, separated by a comma.")
            return

    save_statuses(statuses)
    await ctx.send("<:Tick:1290693799361777665> Statuses have been saved successfully.")

@siddhu.command()
async def clear_status(ctx):
    """Clear all statuses and make them blank."""
    file_path = "status.txt"
    try:
        if os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("\n".join(["" for _ in range(5)]))  # Write blank statuses
            await ctx.send("<:Tick:1290693799361777665> **All statuses cleared successfully!**")
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> **Status file not found! Nothing to clear.**")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error clearing statuses: {e}**")


@siddhu.command()
async def show_status(ctx):
    """Show the statuses in text format."""
    file_path = "status.txt"
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                statuses = f.readlines()

            if not statuses or all(status.strip() == "" for status in statuses):
                await ctx.send("<:CROSS_TDG:1321149916201881683> **No statuses configured!**")
                return

            # Format the statuses for display
            formatted_statuses = []
            for i, status in enumerate(statuses, 1):
                if status.strip():  # Show only configured statuses
                    formatted_statuses.append(f"**Status {i}:** `{status.strip()}`")
                else:
                    formatted_statuses.append(f"**Status {i}:** `None`")

            await ctx.send("\n".join(formatted_statuses))
        else:
            await ctx.send("<:CROSS_TDG:1321149916201881683> **Status file not found! Nothing to show.**")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error showing statuses: {e}**")

@siddhu.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)    

YOUTUBE_API_KEY = "AIzaSyB_Ka12Wubi5mBTFG3yurp3WID3eqldO2I"

@siddhu.command()
async def ytsearch(ctx, *, query: str):
    """Search YouTube for videos and return the top 5 results."""
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={YOUTUBE_API_KEY}&type=video&maxResults=5"
    response = requests.get(search_url)
    results = response.json()

    if "items" not in results or not results['items']:
        await ctx.send(f"No results found for '{query}' on YouTube.")
        return

    output = "# __SyntheX Prime V5 <a:Basu_Crown:1290692084709195826>__\n🔎 **YouTube Search Results:**\n"
    for idx, item in enumerate(results['items'], start=1):
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        output += f"{idx}. [{video_title}]({video_url})\n"

    await ctx.send(output)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}YTSEARCH SUCCESSFUL<:Tick:1290693799361777665> ")    

@siddhu.command()
async def asci(ctx, *, text):
    f = Figlet(font='standard')
    ascii_art = f.renderText(text)
    await ctx.send(f'```{ascii_art}```')
  
import discord
from discord.ext import commands
from datetime import datetime
import os

@siddhu.command()
async def savetranscript(ctx, filename="transcript.html"):
    try:
        # Determine channel type (DM, Group, or Server)
        if isinstance(ctx.channel, discord.DMChannel):  # DM
            recipient = ctx.channel.recipient
            location = f"DM with {recipient.name}"
            icon_url = recipient.avatar.url if recipient.avatar else "https://cdn.discordapp.com/embed/avatars/0.png"
            channel_name = f"DM-{recipient.name}"
        elif isinstance(ctx.channel, discord.GroupChannel):  # Group Chat
            location = f"Group Chat: {ctx.channel.name or 'Unnamed'}"
            icon_url = ctx.channel.icon.url if ctx.channel.icon else "https://cdn.discordapp.com/embed/avatars/0.png"
            channel_name = ctx.channel.name or "Unnamed-Group"
        else:  # Server Text Channel
            location = ctx.guild.name
            icon_url = ctx.guild.icon.url if ctx.guild.icon else "https://cdn.discordapp.com/embed/avatars/0.png"
            channel_name = ctx.channel.name

        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        # Create the HTML transcript
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Transcript - {channel_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #36393F;
            color: #dcddde;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .header img {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
        }}
        .message {{
            display: flex;
            align-items: flex-start;
            padding: 10px;
            border-bottom: 1px solid #2f3136;
        }}
        .avatar {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }}
        .message-content {{
            flex: 1;
        }}
        .author {{
            font-weight: bold;
            color: #00b0f4;
        }}
        .nickname {{
            color: #b9bbbe;
            font-size: 0.9em;
        }}
        .timestamp {{
            font-size: 0.8em;
            color: #72767d;
            margin-left: 5px;
        }}
        .content {{
            margin-top: 5px;
        }}
        .attachment img {{
            max-width: 100%;
            border-radius: 5px;
            margin-top: 5px;
        }}
        .embed {{
            background-color: #2f3136;
            border-left: 4px solid #00b0f4;
            padding: 10px;
            margin-top: 5px;
            border-radius: 5px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            padding: 10px;
            border-top: 2px solid #00b0f4;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="{icon_url}" alt="Icon">
            <h2>Transcript for {channel_name}</h2>
            <p><strong>Location:</strong> {location}</p>
            <p><strong>Generated at:</strong> {timestamp}</p>
            <hr>
        </div>
""")

            # Fetch messages (oldest first)
            async for message in ctx.channel.history(limit=None, oldest_first=True):
                # Safely get avatar URL
                avatar_url = message.author.avatar.url if message.author.avatar else "https://cdn.discordapp.com/embed/avatars/0.png"
                nickname = message.author.display_name  # Fetch nickname
                timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")
                content = message.content.replace("\n", "<br>") if message.content else ""

                # Handle attachments
                attachments_html = ""
                if message.attachments:
                    for att in message.attachments:
                        if any(att.filename.lower().endswith(ext) for ext in ["png", "jpg", "jpeg", "gif", "webp"]):
                            attachments_html += f'<img class="attachment" src="{att.url}" alt="Image">'
                        else:
                            attachments_html += f'<p><a href="{att.url}" target="_blank">{att.filename}</a></p>'

                # Handle embeds
                embeds_html = ""
                for embed in message.embeds:
                    embeds_html += f'<div class="embed"><strong>{embed.title}</strong><br>{embed.description or ""}</div>'

                # Write message to file
                file.write(f"""        <div class="message">
            <img class="avatar" src="{avatar_url}" alt="Avatar">
            <div class="message-content">
                <div>
                    <span class="author">{message.author.name}</span> 
                    <span class="nickname">({nickname})</span> 
                    <span class="timestamp">{timestamp}</span>
                </div>
                <div class="content">{content}</div>
                {attachments_html}
                {embeds_html}
            </div>
        </div>
""")

            # Add footer
            file.write(f"""        <div class="footer">
            <p>Generated by <strong>{ctx.author.name}</strong> at {timestamp}</p>
        </div>
    </div>
</body>
</html>
""")

        # Send the transcript file to Discord
        await ctx.send(f"# __SYNTHEX PRIME V5 <a:Basu_Crown:1290692084709195826>__\n<a:diamond:1281246685955362877> **TRANSCRIPT CREATED !**", file=discord.File(filename))

        # Delete the file after sending
        os.remove(filename)
    except Exception as e:
        await ctx.send(f"❌ Error saving transcript: `{e}`")
  
@siddhu.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def loverate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.send(f"<:white_arrow:1290693789824061461>**PROVIDE A USER**")
    else:
        await ctx.send(
            f"<:Heart_Beating:1291422747615952898> **YOU AND {User.mention} ARE 100% PERFECT FOR EACH OTHER <3**"
        )
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}LOVERATE MEASURED 💖 ")
  
import discord
import aiohttp

async def fetch_gif(action):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://nekos.life/api/v2/img/{action}") as resp:
            data = await resp.json()
            return data["url"] if "url" in data else None

async def send_action_embed(ctx, description: str, image_url: str = None):
    if embed_mode_enabled:
        # Send as embed via webhook
        await send_custom_embed(
            ctx,
            description=description,
            image=image_url
        )
    else:
        # Embed mode off: send normal text + image URL separately
        if image_url:
            await ctx.send(f"{description}\n{image_url}")
        else:
            await ctx.send(description)

@siddhu.command()
async def kiss(ctx, user: discord.User):
    gif = await fetch_gif("kiss")
    if gif:
        description = f"💋 {ctx.author.display_name} kisses {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def slap(ctx, user: discord.User):
    gif = await fetch_gif("slap")
    if gif:
        description = f"👋 {ctx.author.display_name} slaps {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def cuddle(ctx, user: discord.User):
    gif = await fetch_gif("cuddle")
    if gif:
        description = f"🤗 {ctx.author.display_name} cuddles {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def hug(ctx, user: discord.User):
    gif = await fetch_gif("hug")
    if gif:
        description = f"🤗 {ctx.author.display_name} hugs {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def tickle(ctx, user: discord.User):
    gif = await fetch_gif("tickle")
    if gif:
        description = f"😆 {ctx.author.display_name} tickles {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def poke(ctx, user: discord.User):
    gif = await fetch_gif("poke")
    if gif:
        description = f"👉 {ctx.author.display_name} pokes {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def smug(ctx):
    gif = await fetch_gif("smug")
    if gif:
        description = f"😏 {ctx.author.display_name} is feeling smug!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def baka(ctx, user: discord.User):
    gif = await fetch_gif("baka")
    if gif:
        description = f"😡 {ctx.author.display_name} calls {user.display_name} a **BAKA**!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def feed(ctx, user: discord.User):
    gif = await fetch_gif("feed")
    if gif:
        description = f"🍽️ {ctx.author.display_name} feeds {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def pat(ctx, user: discord.User):
    gif = await fetch_gif("pat")
    if gif:
        description = f"🖐️ {ctx.author.display_name} pats {user.display_name}!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def foxgirl(ctx):
    gif = await fetch_gif("fox_girl")
    if gif:
        description = f"🦊 Here's a cute fox girl!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def neko(ctx):
    gif = await fetch_gif("neko")
    if gif:
        description = f"🐱 Here's a cute neko!"
        await send_action_embed(ctx, description, gif)

@siddhu.command()
async def waifu(ctx):
    gif = await fetch_gif("waifu")
    if gif:
        description = f"💖 Here's a waifu just for you!"
        await send_action_embed(ctx, description, gif)

@siddhu.command(aliases=['fuck', 'fx', '18+', 'xxx'])
async def nsfw(ctx):
    try:
        response = requests.get('https://api.waifu.pics/nsfw/waifu')
        data = response.json()
        if 'url' in data:
            image_url = data['url']
            await ctx.message.delete()
            if not embed_mode_enabled:
                await ctx.send(image_url)
            else:
                await send_custom_embed(ctx, image=image_url)
        else:
            await ctx.send('- `[+] ERROR FINDING ANIME GURLLL`')
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}HENTAI SUCCESSFUL<:Tick:1290693799361777665> (THARKI💀)")
    except Exception as e:
        print('- `[+] ERROR FETCHING IT`', e)
  
@siddhu.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.send(f"<:kronix_dot:1281280217335332966>**PROVIDE A USER**")
    else:
        await ctx.send(f"<:gayDoge:1291417217858011228> **{User.mention} IS {random.randrange(101)}% GAY**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}GAYRATE MEASURED SUCCESFULLY😂 ")
        
@siddhu.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def randirate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.send(f"<:kronix_dot:1281280217335332966>**PROVIDE A USER**")
    else:
        await ctx.send(f"<:shlok_rand:1291414857333084303> **{User.mention} IS {random.randrange(101)}% RANDI**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}RANDI RATE MEASURED SUCCESFULLY😂 ")
 
@siddhu.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def simprate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.send(f"<:kronix_dot:1281280217335332966>**PROVIDE A USER**")
    else:
        await ctx.send(f"<:SIMP_blop:1291414858687840298> **{User.mention} IS {random.randrange(101)}% SIMP**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}SIMP RATE MEASURED SUCCESFULLY😂 ")
 
@siddhu.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def tharki(ctx, User: discord.Member = None):
    if User is None:
        await ctx.send(f"<:kronix_dot:1281280217335332966>**PROVIDE A USER**")
    else:
        await ctx.send(f"<:tharkimon:1291420565911113809> **{User.mention} IS {random.randrange(101)}% THARKI**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}THARKI RATE MEASURED SUCCESFULLY😂 ")
 
@siddhu.command()
async def define(ctx, *, word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            word_data = data[0]
            word_meanings = word_data['meanings']
            
            meanings_list = []
            for meaning in word_meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                
                def_text = f"**{part_of_speech.capitalize()}:**\n"
                for i, definition in enumerate(definitions, start=1):
                    def_text += f"{i}. {definition['definition']}\n"
                    if 'example' in definition:
                        def_text += f"   *Example: {definition['example']}*\n"
                
                meanings_list.append(def_text)
            
            result_text = f"**{word.capitalize()}**\n\n" + '\n'.join(meanings_list)
            await ctx.send(result_text)
        else:
            await ctx.send("<a:diamond:1281246685955362877> **NO DEFINATIONS FOR THAT WORD**")
    else:
        await ctx.send("<a:diamond:1281246685955362877> **FAILED TO RETRIVE THAT WORD**")

@siddhu.command()
async def gitsearch(ctx, repository_name: str):
    try:
        # Search for repositories on GitHub
        url = f"https://api.github.com/search/repositories?q={repository_name}"
        response = requests.get(url)
        data = response.json()

        # Process the response and send repository information as a response
        if "items" in data:
            repositories = data["items"][:5]  # Limit the number of repositories to display
            for repository in repositories:
                repo_name = repository["full_name"]
                repo_url = repository["html_url"]
                await ctx.send(f"# __SyntheX Prime V5 <a:Basu_Crown:1290692084709195826>__\n<a:diamond:1281246685955362877> **REPO **: {repo_name}\n{repo_url}")
        else:
            await ctx.send("<:white_arrow:1290693789824061461>**NOT FOUND**")
    except Exception as e:
        await ctx.send(f"<:white_arrow:1290693789824061461>**ERROR **:{str(e)}")
        
@siddhu.command()
async def gituser(ctx, username: str):
    api_url = f"https://api.github.com/users/{username}"

    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()

        message = f"# __SyntheX Prime V5 <a:Basu_Crown:1290692084709195826>__\n"
        message = f"**[+]**__**GITUSER INFO**__\n\n"
        message += f"<a:diamond:1281246685955362877> **RESULTS FOR GITHUB USER** : __`{username}`__\n"
        message += f"<a:diamond:1281246685955362877> **USERNAME** : `{user_data.get('login', 'N/A')}`\n"
        message += f"<a:diamond:1281246685955362877> **NAME** : `{user_data.get('name', 'NOT SPECIFIED')}`\n"
        message += f"<a:diamond:1281246685955362877> **BIO** : `{user_data.get('bio', 'NOT SPECIFIED')}`\n"
        message += f"<a:diamond:1281246685955362877> **FOLLOWERS** : `{user_data.get('followers', 0)}`\n"
        message += f"<a:diamond:1281246685955362877> **FOLLOWING** : `{user_data.get('following', 0)}`\n"
        message += f"<a:diamond:1281246685955362877> **PUBLIC REPOS** : `{user_data.get('public_repos', 0)}`\n"
        message += f"<a:diamond:1281246685955362877> **GIT URL** : `{user_data.get('html_url', 'N/A')}`\n\n"
        message += f"<a:diamond:1281246685955362877> **ASKED BY** : `{siddhu.user.name}`\n"

        await ctx.send(message)
    elif response.status_code == 404:
        await ctx.send("<a:diamond:1281246685955362877> **USER NOT FOUND**")
    else:
        await ctx.send("<a:diamond:1281246685955362877> **FAILED TO GET INFO**")

import json  # Ensure it's imported at top if not already

@siddhu.command()
async def upi(ctx):
    # Load the UPI from config
    with open("config.json", "r") as f:
        config = json.load(f)

    upi = config.get("Upi", "Not Set")

    message = (
        "# <a:tz_pink_money:1281241579893428297> __**UPI ID**__ <a:tz_pink_money:1281241579893428297>\n"
        f"> <:tz_INR:1281238098528698379>{upi}\n"
        "> <:white_Arrow:1290693791983861822> **MUST SEND SCREENSHOT AFTER PAYMENT**"
    )

    if embed_mode_enabled:
        await send_custom_embed(ctx, description=message)
        await ctx.reply(upi)  # Plain UPI ID below embed for copy
    else:
        await ctx.send(message)

    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}UPI SENT SUCCESSFULLY <:Tick:1290693799361777665>")
    await ctx.message.delete()

@siddhu.command()
async def upi2(ctx):
    # Load UPI2 from config
    with open("config.json", "r") as f:
        config = json.load(f)

    upi2 = config.get("Upi2", "Not Set")

    message = (
        "# <a:tz_pink_money:1281241579893428297> __**UPI ID**__ <a:tz_pink_money:1281241579893428297>\n"
        f"> <:tz_INR:1281238098528698379>{upi2}\n"
        "> <:white_Arrow:1290693791983861822> **MUST SEND SCREENSHOT AFTER PAYMENT**"
    )

    if embed_mode_enabled:
        await send_custom_embed(ctx, description=message)
        await ctx.reply(upi2)
    else:
        await ctx.send(message)

    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}UPI2 SENT SUCCESSFULLY <:Tick:1290693799361777665>")
    await ctx.message.delete()
    
@siddhu.command()
async def qr(ctx):
    message = "**MUST SEND SCREENSHOT AFTER PAYMENT**"

    if not Qr or not isinstance(Qr, str) or not Qr.startswith("http"):
        await ctx.reply("<:CROSS_TDG:1321149916201881683> **QR not set or invalid in config.**", mention_author=False)
        await ctx.message.delete()
        return

    if not embed_mode_enabled:
        # Plain reply with the URL + text
        await ctx.reply(f"{Qr}\n{message}", mention_author=False)
    else:
        # Embed mode: send embed with image URL and description
        try:
            await send_custom_embed(
                ctx,
                description=message,
                image=Qr
            )
        except Exception as e:
            await ctx.reply(f"<:CROSS_TDG:1321149916201881683> Failed to send QR embed: `{e}`", mention_author=False)

    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}QR SENT SUCCESSFULLY <:Tick:1290693799361777665>")
    await ctx.message.delete()
    
import json  # Make sure you have this at the top

@siddhu.command()
async def addy(ctx, wallet_num: str):
    """
    Fetch and display the Litecoin address for a specified wallet.
    """
    try:
        with open("wallet.json", "r") as f:
            wallets = json.load(f)

        if wallet_num not in wallets:
            await ctx.send("`Address Not Found In Wallets`")
            return

        wallet_info = wallets[wallet_num]
        addy = wallet_info.get("address", "Address not found.")

        full_message = (
            "# <a:tz_ltc:1281238097136451616> __**LTC ADDY**__ <a:tz_ltc:1281238097136451616>\n"
            f"> <:rdx_glowin_heart:1288196137848803451> **ADDY FOR :** `WALLET {wallet_num}`\n"
            f"{addy}\n"
            "> <:white_arrow:1290693791983861822> **MUST SEND SCREENSHOT / BLOCKCHAIN AFTER PAYMENT**"
        )

        if embed_mode_enabled:
            await send_custom_embed(ctx, description=full_message)
            await ctx.reply(addy)  # Reply before deleting to avoid error
        else:
            await ctx.send(full_message)

        await ctx.message.delete()  # Delete after sending everything

    except FileNotFoundError:
        await ctx.send("`Wallet file not found. Please ensure wallet.json exists in the directory.`")
    except json.JSONDecodeError:
        await ctx.send("`Failed to parse wallet.json. Please check the file format.`")
    except Exception as e:
        await ctx.send(f"`An error occurred: {str(e)}`")
    
import requests

# Math API endpoint
api_endpoint = 'https://api.mathjs.org/v4/'

@siddhu.command(name='math')
async def math(ctx, *, equation):
    """
    Calculate the result of a given math equation.
    Args:
        ctx: The context of the command.
        equation: The mathematical equation to calculate.
    """
    try:
        # Send the equation to the Math.js API for calculation
        response = requests.get(api_endpoint, params={'expr': equation})

        if response.status_code == 200:
            result = response.text.strip()
            response_message = (
                f"# **__CALCULATOR__** <:calculator:1322954645387350116>\n"
                f"<:note:1290693795763195945> **EQUATION**: `{equation}`\n"
                f"<:arrow_blue:1281246700358471722> **Result**:\n"
                f"# <:white_arrow:1290693789824061461>{result}"
            )
            await ctx.send(response_message)
        else:
            await ctx.send('<:lr_tick_1:1290693800808677461> **Failed to calculate the equation.**')

    except Exception as e:
        await ctx.send(f"<:lr_tick_1:1290693800808677461> **An error occurred:** `{str(e)}`")
        
import json
import discord

@siddhu.command(name='i2c')
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    """
    Convert INR to Crypto based on the exchange rate in config.json.
    Supports both INR to Crypto and Crypto to INR.
    """
    try:
        # Get exchange rate from config.json
        with open('config.json', 'r') as f:
            config = json.load(f)
        I2C_Rate = config.get('I2C_Rate', 90)  # Default 90 if not found

        # Check if input contains '$' (USD conversion)
        if '$' in amount:
            amount = float(amount.replace('$', '').strip())  # Remove '$' and convert to float
            inr_required = round(amount * I2C_Rate, 2)  # Convert USD to INR

            response = (
                f"# **__INR TO CRYPTO__** <:exch:1322953996389974048>\n"
                f"> <:jrexchanger:1322956674465792151> **EXCHANGE RATE :** `{I2C_Rate}/$`\n"
                f"> <:exchanger:1322954180452810775> **USD AMOUNT :** `${amount:.2f}`\n"
                f"> <:INR:1322635698435784775> **INR AMOUNT :** `₹{inr_required}`"
            )

            log_message = f"[+] I2C Command Executed: {amount:.2f} USD requires ₹{inr_required}"
        
        else:
            amount = float(amount.replace('₹', '').strip())  # Remove '₹' if present
            crypto_amount = round(amount / I2C_Rate, 2)  # Convert INR to Crypto

            response = (
                f"# **__INR TO CRYPTO__** <:exch:1322953996389974048>\n"
                f"> <:jrexchanger:1322956674465792151> **EXCHANGE RATE :** `{I2C_Rate}/$`\n"
                f"> <:INR:1322635698435784775> **INR AMOUNT :** `₹{amount}`\n"
                f"> <:exchanger:1322954180452810775> **CRYPTO AMOUNT :** `${crypto_amount:.2f}`"
            )

            log_message = f"[+] I2C Command Executed: {amount:.2f} INR converted to ${crypto_amount:.2f}"

        await ctx.send(response)
        await ctx.message.delete()
        print(log_message)

    except ValueError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **Invalid amount! Please enter a valid number.**")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **An error occurred:** `{str(e)}`")
    
import json
import discord

@siddhu.command(name='c2i')
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    """
    Convert Crypto to INR or INR to Crypto based on the exchange rate in config.json.
    Supports both directions.
    """
    try:
        # Get exchange rate from config.json
        with open('config.json', 'r') as f:
            config = json.load(f)
        C2I_Rate = config.get('C2I_Rate', 87)  # Default 87 if not found

        # Check if input contains '$' (Crypto to INR conversion)
        if '$' in amount:
            amount = float(amount.replace('$', '').strip())  # Remove '$' and convert to float
            inr_amount = round(amount * C2I_Rate, 2)  # Convert Crypto (USD) to INR

            response = (
                f"# **__CRYPTO TO INR__** <:exch:1322953996389974048>\n"
                f"> <:jrexchanger:1322956674465792151> **EXCHANGE RATE :** `{C2I_Rate}/$`\n"
                f"> <:exchanger:1322954180452810775> **CRYPTO AMOUNT :** `${amount:.2f}`\n"
                f"> <:INR:1322635698435784775> **INR AMOUNT :** `₹{inr_amount}`"
            )

            log_message = f"[+] C2I Command Executed: ${amount:.2f} converted to ₹{inr_amount}"
        
        else:
            amount = float(amount.strip())  # Convert input to float
            crypto_amount = round(amount / C2I_Rate, 2)  # Convert INR to Crypto (USD)

            response = (
                f"# **__CRYPTO TO INR__** <:exch:1322953996389974048>\n"
                f"> <:jrexchanger:1322956674465792151> **EXCHANGE RATE :** `{C2I_Rate}/$`\n"
                f"> <:INR:1322635698435784775> **INR AMOUNT :** `₹{amount}`\n"
                f"> <:exchanger:1322954180452810775> **CRYPTO AMOUNT :** `${crypto_amount:.2f}`"
            )

            log_message = f"[+] C2I Command Executed: ₹{amount:.2f} converted to ${crypto_amount:.2f}"

        await ctx.send(response)
        await ctx.message.delete()
        print(log_message)

    except ValueError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **Invalid amount! Please enter a valid number.**")
    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **An error occurred:** `{str(e)}`")
    
import asyncio

spam_tasks = {}  # Dictionary to store running spam tasks

@siddhu.command()
async def spam(ctx, times: int, *, message):
    """Spam a message a given number of times (bypasses embed mode)."""
    global spam_tasks

    if times <= 0:
        await ctx.send("❌ Invalid spam count!")
        return

    if ctx.channel.id in spam_tasks:
        await ctx.send("⚠️ Spam already running in this channel! Use `.stop_spam` to stop it.")
        return

    try:
        await ctx.message.delete()  # Delete the command message
    except:
        pass

    async def spam_task():
        for _ in range(times):
            if ctx.channel.id not in spam_tasks:  # If stopped externally
                break
            await ctx.reply(message)  # Reply to deleted message (appears like normal send)
            await asyncio.sleep(0.1)  # Delay to prevent rate limiting

        spam_tasks.pop(ctx.channel.id, None)

    spam_tasks[ctx.channel.id] = asyncio.create_task(spam_task())

@siddhu.command()
async def stop_spam(ctx):
    """Stop all ongoing spam activity."""
    global spam_tasks
    if not spam_tasks:
        await ctx.send("⚠️ No spam tasks running.")
        return

    for channel_id, task in spam_tasks.items():
        task.cancel()  # Cancel running tasks
    spam_tasks.clear()  # Clear the dictionary

    await ctx.send("🛑 **All spam tasks stopped!**")
  
@siddhu.command()
async def fibonacci_sequence(ctx, num: int):
    """Generates the first N numbers in the Fibonacci sequence."""
    sequence = [0, 1]
    for i in range(2, num):
        sequence.append(sequence[i-1] + sequence[i-2])
    await ctx.send(f"First {num} Fibonacci numbers: {sequence[:num]}")

@siddhu.command()
async def reverse_list(ctx, *args):
    """Reverses the order of arguments passed."""
    reversed_args = list(args)[::-1]
    await ctx.send(f"Reversed list: {reversed_args}")

@siddhu.command()
async def check_prime(ctx, num: int):
    """Checks if the given number is prime."""
    if num <= 1:
        await ctx.send(f"{num} is not a prime number.")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            await ctx.send(f"{num} is not a prime number.")
            return
    await ctx.send(f"{num} is a prime number.")

@siddhu.command()
async def check_anagram(ctx, word1: str, word2: str):
    """Checks if two words are anagrams."""
    if sorted(word1.lower()) == sorted(word2.lower()):
        await ctx.send(f"'{word1}' and '{word2}' are anagrams!")
    else:
        await ctx.send(f"'{word1}' and '{word2}' are not anagrams.")

@siddhu.command()
async def convert_to_binary(ctx, number: int):
    """Converts a given number to binary."""
    binary_representation = bin(number)[2:]
    await ctx.send(f"Binary representation of {number}: {binary_representation}")

@siddhu.command()
async def reverse_text(ctx, *, text: str):
    """Reverses the input text."""
    reversed_text = text[::-1]
    await ctx.send(f"Reversed text: {reversed_text}")

@siddhu.command()
async def random_color_name(ctx):
    """Generates a random color name."""
    import random
    color_names = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"]
    random_color = random.choice(color_names)
    await ctx.send(f"Random color name: {random_color}")

@siddhu.command()
async def word_count(ctx, *, text: str):
    """Counts the number of words in the given text."""
    word_count = len(text.split())
    await ctx.send(f"Word count: {word_count}")

# Utility function to find a role or member by name, mention, or ID
def get_target(ctx, target):
    if not target:
        return ctx.guild.default_role  # Default to @everyone if no input is given
    
    # Try to get role by mention, ID, or name
    role = discord.utils.get(ctx.guild.roles, mention=target) or \
           discord.utils.get(ctx.guild.roles, id=int(target) if target.isdigit() else None) or \
           discord.utils.get(ctx.guild.roles, name=target)

    if role:
        return role  # Return role if found

    # Try to get member by mention, ID, or name
    member = discord.utils.get(ctx.guild.members, mention=target) or \
             discord.utils.get(ctx.guild.members, id=int(target) if target.isdigit() else None) or \
             discord.utils.get(ctx.guild.members, name=target)

    if member:
        return member  # Return member if found
    
    return None  # If no role or member is found, return None

# Hide current channel for a role/user
@siddhu.command()
async def hide(ctx, *, target=None):
    await ctx.message.delete()
    target_obj = get_target(ctx, target)

    if not target_obj:
        await ctx.send("❌ `Invalid role or user.`")
        return

    await ctx.channel.set_permissions(target_obj, view_channel=False)
    await ctx.send(f"✅ `Channel hidden for {target_obj.name}`")

# Unhide current channel for a role/user
@siddhu.command()
async def unhide(ctx, *, target=None):
    await ctx.message.delete()
    target_obj = get_target(ctx, target)

    if not target_obj:
        await ctx.send("❌ `Invalid role or user.`")
        return

    await ctx.channel.set_permissions(target_obj, view_channel=True)
    await ctx.send(f"✅ `Channel unhidden for {target_obj.name}`")

# Hide all channels for a role/user
@siddhu.command()
async def hideall(ctx, *, target=None):
    await ctx.message.delete()
    target_obj = get_target(ctx, target)

    if not target_obj:
        await ctx.send("❌ `Invalid role or user.`")
        return

    for channel in ctx.guild.channels:
        await channel.set_permissions(target_obj, view_channel=False)

    await ctx.send(f"✅ `All channels hidden for {target_obj.name}`")

# Unhide all channels for a role/user
@siddhu.command()
async def unhideall(ctx, *, target=None):
    await ctx.message.delete()
    target_obj = get_target(ctx, target)

    if not target_obj:
        await ctx.send("❌ `Invalid role or user.`")
        return

    everyone_role = ctx.guild.default_role

    for channel in ctx.guild.channels:
        if target_obj == everyone_role:
            await channel.set_permissions(everyone_role, view_channel=True)
        else:
            everyone_perms = channel.overwrites_for(everyone_role)
            if not everyone_perms.view_channel:
                await channel.set_permissions(target_obj, view_channel=True)

    await ctx.send(f"✅ `All channels unhidden for {target_obj.name}`")

@siddhu.command()
async def generate_hex_color(ctx):
    """Generates a random hex color code."""
    import random
    hex_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    await ctx.send(f"Generated hex color: {hex_color}")

@siddhu.command()
async def get_file_size(ctx, file_path: str):
    """Returns the size of a file in bytes."""
    import os
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        await ctx.send(f"File size of {file_path}: {size} bytes")
    else:
        await ctx.send(f"File '{file_path}' not found.")

@siddhu.command()
async def find_max_number(ctx, *numbers: int):
    """Finds the maximum number from a list of numbers."""
    max_number = max(numbers)
    await ctx.send(f"The maximum number is {max_number}")

@siddhu.command()
async def find_min_number(ctx, *numbers: int):
    """Finds the minimum number from a list of numbers."""
    min_number = min(numbers)
    await ctx.send(f"The minimum number is {min_number}")

@siddhu.command()
async def multiply_numbers(ctx, *numbers: int):
    """Multiplies a list of numbers together."""
    result = 1
    for num in numbers:
        result *= num
    await ctx.send(f"The result of multiplication is: {result}")

@siddhu.command()
async def convert_to_octal(ctx, number: int):
    """Converts a given number to octal."""
    octal_representation = oct(number)[2:]
    await ctx.send(f"Octal representation of {number}: {octal_representation}")

@siddhu.command()
async def get_current_date(ctx):
    """Returns the current date."""
    from datetime import datetime
    current_date = datetime.now().strftime('%Y-%m-%d')
    await ctx.send(f"Current date: {current_date}")

@siddhu.command()
async def get_current_time(ctx):
    """Returns the current time."""
    from datetime import datetime
    current_time = datetime.now().strftime('%H:%M:%S')
    await ctx.send(f"Current time: {current_time}")  
    
@siddhu.command(name='bal')
async def bal(ctx, addy: str):
    """
    Fetch the balance of a Litecoin address and display it in a formatted output.
    Args:
        ctx: The context of the command.
        addy: The Litecoin address.
    """
    try:
        # Fetch address details from a suitable API
        address_data = get_address_details(addy)

        # Extract balance details
        confirmed_balance_ltc = address_data['final_balance'] / 1e8
        unconfirmed_balance_ltc = address_data['unconfirmed_balance'] / 1e8
        total_received_ltc = address_data['total_received'] / 1e8

        # Fetch Litecoin to USD conversion rate
        coingecko_resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        coingecko_resp.raise_for_status()
        ltc_to_usd_rate = coingecko_resp.json()['litecoin']['usd']

        # Calculate balances in USD
        confirmed_balance_usd = confirmed_balance_ltc * ltc_to_usd_rate
        unconfirmed_balance_usd = unconfirmed_balance_ltc * ltc_to_usd_rate
        total_received_usd = total_received_ltc * ltc_to_usd_rate

        # Format response
        response = (
            f"# <a:tz_ltc:1281238097136451616> __**LTC BALANCE**__ <a:tz_ltc:1281238097136451616>\n"
            f"> <:rdx_glowin_heart:1288196137848803451> **Balance For :** `{addy}`\n"
            f"> <:LTC:1322611807269031968> **Total Balance :** `${confirmed_balance_usd:.2f} USD`\n"
            f"> <a:bitzxier_downtime:1322611844455727165> **Unconfirmed Balance :** `${unconfirmed_balance_usd:.2f} USD`\n"
            f"> <:crypto:1322611842316501073> **Total Received :** `${total_received_usd:.2f} USD`\n"
        )

        await ctx.send(response)
        logger.info("[+] Balance Command Used")

    except KeyError:
        await ctx.send("Error: Unable to fetch balance details for the given address.")
    except requests.RequestException:
        await ctx.send("Error: Failed to fetch Litecoin price data.")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {str(e)}")
          
import asyncio
import discord

@siddhu.command(description="Set your playing activity.")
async def playing(ctx, *, game: str):
    await siddhu.change_presence(activity=discord.Game(name=game))
    await ctx.send(content=f"Set playing status to: {game}")

@siddhu.command(description="Set your watching activity.")
async def watching(ctx, *, game: str):
    await siddhu.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=game)
    )
    await ctx.send(content=f"Set watching status to: {game}")

@siddhu.command(description="Set your listening activity.")
async def listening(ctx, *, game: str):
    await siddhu.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=game)
    )
    await ctx.send(content=f"Set listening status to: {game}")

@siddhu.command(description="Set your streaming activity.")
async def streaming(ctx, *, game: str):
    await siddhu.change_presence(
        activity=discord.Streaming(name=game, url="https://www.twitch.tv/")
    )
    await ctx.send(content=f"Set streaming status to: {game}")

@siddhu.command(description="Removes your presence.")
async def stopactivity(ctx):
    await siddhu.change_presence(activity=None)
    await ctx.send(content=f"Removed presences.")

cycle = False

@siddhu.command(description="Cycles your playing status.")
async def cycleplaying(ctx, *, games: str):
    games = games.split(",")
    await ctx.send(content=f"Cycling playing status.")
    global cycle
    cycle = True

    while cycle:
        for game in games:
            await siddhu.change_presence(activity=discord.Game(name=game))
            await asyncio.sleep(10)

@siddhu.command(description="Stops cycling your playing status.")
async def stopcycleplaying(ctx):
    global cycle
    cycle = False
    await ctx.send(content=f"Stopped cycling playing status.")
    await siddhu.change_presence(activity=None)

@siddhu.command(description="Cycles your watching status.")
async def cyclewatching(ctx, *, games: str):
    games = games.split(",")
    await ctx.send(content=f"Cycling watching status.")
    global cycle
    cycle = True

    while cycle:
        for game in games:
            await siddhu.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=game)
            )
            await asyncio.sleep(10)

@siddhu.command(description="Stops cycling your watching status.")
async def stopcyclewatching(ctx):
    global cycle
    cycle = False
    await ctx.send(content=f"Stopped cycling watching status.")
    await siddhu.change_presence(activity=None)

@siddhu.command(description="Cycles your listening status.")
async def cyclelistening(ctx, *, games: str):
    games = games.split(",")
    await ctx.send(content=f"Cycling listening status.")
    global cycle
    cycle = True

    while cycle:
        for game in games:
            await siddhu.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.listening, name=game
                )
            )
            await asyncio.sleep(10)

@siddhu.command(description="Stops cycling your listening status.")
async def stopcyclelistening(ctx):
    global cycle
    cycle = False
    await ctx.send(content=f"Stopped cycling listening status.")
    await siddhu.change_presence(activity=None)

@siddhu.command(description="Cycles your streaming status.")
async def cyclestreaming(ctx, *, games: str):
    games = games.split(",")
    await ctx.send(content=f"Cycling streaming status.")
    global cycle
    cycle = True

    while cycle:
        for game in games:
            await siddhu.change_presence(
                activity=discord.Streaming(name=game, url="https://www.twitch.tv/")
            )
            await asyncio.sleep(10)

@siddhu.command(description="Stops cycling your streaming status.")
async def stopcyclestreaming(ctx):
    global cycle
    cycle = False
    await ctx.send(content=f"Stopped cycling streaming status.")
    await siddhu.change_presence(activity=None)

@siddhu.command(description="Sets your status to online.")
async def online(ctx):
    await siddhu.change_presence(status=discord.Status.online)
    await ctx.send(content=f"Set status to online.")

@siddhu.command(description="Sets your status to idle.")
async def idle(ctx):
    await siddhu.change_presence(status=discord.Status.idle)
    await ctx.send(content=f"Set status to idle.")

@siddhu.command(aliases=["busy"], description="Sets your status to dnd.")
async def dnd(ctx):
    await siddhu.change_presence(status=discord.Status.dnd)
    await ctx.send(content=f"Set status to dnd.")

@siddhu.command(description="Sets your status to offline.")
async def invisible(ctx):
    await siddhu.change_presence(status=discord.Status.invisible)
    await ctx.send(content=f"Set status to invisible.")

@siddhu.command(aliases=['ri'])
async def roleinfo(ctx, *, role: discord.Role = None):
    if not role:
        await ctx.send("Please mention a valid role.")
        return

    permissions = ', '.join([perm[0].replace('_', ' ').title() for perm in role.permissions if perm[1]]) or "None"

    message = (
        f"# 🎭 **Role Info: `{role.name}`**\n"
        f"> 🆔 **Role ID:** `{role.id}`\n"
        f"> 📈 **Position:** `{role.position}`\n"
        f"> 📅 **Created On:** `{role.created_at.strftime('%d %b %Y • %I:%M %p')}`\n"
        f"> 👥 **Members with Role:** `{len(role.members)}`\n"
        f"> 🔒 **Mentionable:** `{role.mentionable}`\n"
        f"> 🔐 **Permissions:** `{permissions}`\n"
        f"> 👤 **Requested by:** `{ctx.author}`"
    )

    await ctx.send(message)

import asyncio
import aiohttp
import discord

leaveCommand = False
cycleNicknames = False

@siddhu.command(description="Leaves all servers.")
async def leaveallservers(ctx):
    global leaveCommand
    leaveCommand = True

    await ctx.send(content=f"Are you sure? (Send `y` to confirm, anything else will cancel.)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await siddhu.wait_for("message", check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(content=f"Timed out. Please try again.")
        return

    if msg.content.lower() == "y":
        await msg.delete()
        for guild in siddhu.guilds:
            if not leaveCommand:
                return
            try:
                await guild.leave()
                await asyncio.sleep(0.75)
            except Exception as e:
                pass
            await asyncio.sleep(1)
        await ctx.send(content=f"Successfully left all servers.")
    else:
        await ctx.send(content=f"Cancelled.")

@siddhu.command(description="Leaves all groups.")
async def leaveallgroups(ctx):
    await ctx.send(content=f"Are you sure? (Send `yes` to confirm, anything else will cancel.)")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await siddhu.wait_for("message", check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(content=f"Timed out. Please try again.")
        return

    if msg.content.lower() == "yes":
        await msg.delete()
        for dm in siddhu.private_channels:
            if dm.type == discord.ChannelType.group:
                try:
                    await dm.leave()
                except Exception as e:
                    pass
                await asyncio.sleep(1)
        await ctx.send(content=f"Left all groups.")
    else:
        await ctx.send(content=f"Cancelled.")

@siddhu.command(description="Stops leaving groups or guilds.")
async def stopleave(ctx):
    global leaveCommand
    leaveCommand = False

    await ctx.send(content=f"Stopped leaving servers.")

@siddhu.command(aliases=["loopnick"], description="Loops through multiple nicknames.")
async def nickloop(ctx, *, nicks: str):
    nicks = nicks.split(",")

    await ctx.send(content=f"Looping through nicknames.")

    global cycleNicknames
    cycleNicknames = True

    while cycleNicknames:
        for nick in nicks:
            await ctx.guild.me.edit(nick=nick)
            await asyncio.sleep(10)

@siddhu.command(aliases=["stoploopnick"], description="Stops looping through nicknames.")
async def stopnickloop(ctx):
    global cycleNicknames
    cycleNicknames = False

    await ctx.send(content=f"Stopped looping through nicknames.")

@siddhu.command(description="Sets your profile picture.")
async def setpfp(ctx, *, url: str = None):
    await ctx.send(content=f"Setting profile picture...")

    if url is None:
        try:
            url = ctx.message.attachments[0].url
        except:
            await ctx.send(content=f"Error: No image URL or attachment provided.")
            return

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                try:
                    await siddhu.user.edit(avatar=await resp.read())
                except Exception as e:
                    await ctx.send(content=f"Error: {e}")
                    return

    await ctx.send(content=f"Set profile picture.")

@siddhu.command(aliases=["webhookdelete"], description="Deletes a webhook.")
async def deletewebhook(ctx, *, webhook):
    await ctx.send(content=f"Deleting webhook...")

    async with aiohttp.ClientSession() as session:
        async with session.get(webhook) as resp:
            if resp.status == 200:
                webhook = await resp.json()
                webhook_id = webhook["id"]
                webhook_token = webhook["token"]

                async with session.delete(f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}") as resp:
                    if resp.status == 204:
                        await ctx.send(content=f"Deleted webhook.")
                    else:
                        await ctx.send(content=f"Failed to delete webhook.")
            else:
                await ctx.send(content=f"Webhook not found.")

# File paths
CONFIG_FILE = "config.json"
VOUCH_CONFIG_FILE = "vouch_config.json"

# Load JSON files
def load_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save JSON files
def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Load configurations
config = load_json(CONFIG_FILE)
vouch_config = load_json(VOUCH_CONFIG_FILE)

# Set default vouch formats if missing
if "cvouch_format" not in vouch_config:
    vouch_config["cvouch_format"] = "+rep {User_Id} LEGIT SELLER | GOT {product} for [ {price} ] • TYSM"
if "custom_vouches" not in vouch_config:
    vouch_config["custom_vouches"] = {}  # Store product-specific vouches

save_json(VOUCH_CONFIG_FILE, vouch_config)  # Save defaults if missing

@siddhu.command()
async def cvouch(ctx, *, args):
    try:
        # Split input into product name and optional price
        parts = [p.strip() for p in args.split(",")]
        product_name = parts[0]  # First part is always product name
        entered_price = parts[1] if len(parts) > 1 else None  # Second part (if exists) is the entered price

        if product_name not in vouch_config["custom_vouches"]:
            await ctx.send(f"❌ No product vouch found with name '{product_name}'!\nCreate a product vouch first using `.cvouch_create <product>, <price>`")
            return

        # Get saved price from JSON if no price was entered manually
        saved_price = vouch_config["custom_vouches"].get(product_name, "N/A")
        final_price = entered_price if entered_price else saved_price  # Use entered price if provided, else saved price

        user_id = config.get("User_Id", str(ctx.author.id))
        server_link = config.get("SERVER_Link", "https://discord.gg/example")

        # Replace variables in format
        vouch_message = vouch_config["cvouch_format"].replace("{User_Id}", str(user_id)).replace("{product}", product_name).replace("{price}", final_price)

        await ctx.send(vouch_message)
        await ctx.send(server_link)
        print(f"✅ CUSTOM VOUCH SENT: {vouch_message}")

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

# Create a custom vouch entry
@siddhu.command()
async def cvouch_create(ctx, *, args):
    try:
        # Ensure correct format
        parts = [p.strip() for p in args.split(",")]
        if len(parts) != 2:
            await ctx.send("❌ Invalid format! Use `.cvouch_create <product>, <price>`")
            return
        
        product_name = parts[0]
        price = parts[1]

        vouch_config["custom_vouches"][product_name] = price
        save_json(VOUCH_CONFIG_FILE, vouch_config)

        await ctx.send(f"✅ Custom vouch created for **{product_name}** at **{price}**!")
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

# Change the custom vouch format
@siddhu.command()
async def cvouch_format(ctx):
    await ctx.send(f"Enter your custom vouch format\n\nVariables:\n- User: `{User_Id}`\n- Product: `{product}`\n- Price: `{price}`\n\n`Default: {vouch_config['cvouch_format']}`")

    try:
        msg = await ctx.bot.wait_for("message", timeout=30, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        vouch_config["cvouch_format"] = msg.content
        save_json(VOUCH_CONFIG_FILE, vouch_config)
        await ctx.send("✅ Custom vouch format updated successfully!")
    except asyncio.TimeoutError:
        await ctx.send("⚠️ You didn't respond in time. The custom vouch format remains unchanged.")

# Load JSON files
def load_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save JSON files
def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Load configurations
config = load_json(CONFIG_FILE)
vouch_config = load_json(VOUCH_CONFIG_FILE)

# Set defaults if missing
if "vouch_format" not in vouch_config:
    vouch_config["vouch_format"] = "+rep {User_Id} LEGIT SELLER | GOT {main} • TYSM"
if "vouch_msg" not in vouch_config:
    vouch_config["vouch_msg"] = "VOUCH ME HERE"
if "exch_format" not in vouch_config:
    vouch_config["exch_format"] = "+rep {User_Id} LEGIT | EXCHANGED {main} • TYSM"
if "exch_msg" not in vouch_config:
    vouch_config["exch_msg"] = "PLEASE VOUCH ME HERE"
save_json(VOUCH_CONFIG_FILE, vouch_config)  # Save defaults if missing

@siddhu.command()
async def vouch(ctx, *, text):
    await ctx.message.delete()
    user_id = config.get("User_Id", str(ctx.author.id))  # Get from config.json
    server_link = config.get("SERVER_Link", "https://discord.gg/example")  # Get from config.json

    vouch_message = vouch_config["vouch_format"].replace("{User_Id}", str(user_id)).replace("{main}", text)
    
    await ctx.reply(vouch_message)
    await ctx.reply(server_link)
    await ctx.reply(f'**{vouch_config["vouch_msg"]}**')
    print(f"✅ VOUCH SENT: {vouch_message}")

@siddhu.command()
async def exch(ctx, *, text):
    await ctx.message.delete()
    user_id = config.get("User_Id", str(ctx.author.id))  # Get from config.json
    server_link = config.get("SERVER_Link", "https://discord.gg/example")  # Get from config.json

    exch_message = vouch_config["exch_format"].replace("{User_Id}", str(user_id)).replace("{main}", text)
    
    await ctx.reply(exch_message)
    await ctx.reply(server_link)
    await ctx.reply(f'**{vouch_config["exch_msg"]}**')
    print(f"✅ EXCH VOUCH SENT: {exch_message}")

@siddhu.command()
async def vouch_format(ctx):
    await ctx.send(f"Enter your vouch format\nUse `{User_Id}` for your id and `{main}` for vouch contents.\n`Default: {vouch_config['vouch_format']}`")

    try:
        msg = await ctx.bot.wait_for("message", timeout=30, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        vouch_config["vouch_format"] = msg.content
        save_json(VOUCH_CONFIG_FILE, vouch_config)
        await ctx.send("✅ Vouch format updated successfully!")
    except asyncio.TimeoutError:
        await ctx.send("⚠️ You didn't respond in time. The vouch format remains unchanged.")

@siddhu.command()
async def vouch_msg(ctx):
    await ctx.send(f"Enter the vouch message that will be sent after command.\n`Default: {vouch_config['vouch_msg']}`")

    try:
        msg = await ctx.bot.wait_for("message", timeout=30, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        vouch_config["vouch_msg"] = msg.content
        save_json(VOUCH_CONFIG_FILE, vouch_config)
        await ctx.send("✅ Vouch message updated successfully!")
    except asyncio.TimeoutError:
        await ctx.send("⚠️ You didn't respond in time. The vouch message remains unchanged.")

@siddhu.command()
async def exch_format(ctx):
    await ctx.send(f"Enter your exchange format\nUse `{User_Id}` for your id and `{main}` for exchange contents.\n`Default: {vouch_config['exch_format']}`")

    try:
        msg = await ctx.bot.wait_for("message", timeout=30, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        vouch_config["exch_format"] = msg.content
        save_json(VOUCH_CONFIG_FILE, vouch_config)
        await ctx.send("✅ Exchange format updated successfully!")
    except asyncio.TimeoutError:
        await ctx.send("⚠️ You didn't respond in time. The exchange format remains unchanged.")

@siddhu.command()
async def exch_msg(ctx):
    await ctx.send(f"Enter the exchange message that will be sent after command.\n`Default: {vouch_config['exch_msg']}`")

    try:
        msg = await ctx.bot.wait_for("message", timeout=30, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        vouch_config["exch_msg"] = msg.content
        save_json(VOUCH_CONFIG_FILE, vouch_config)
        await ctx.send("✅ Exchange message updated successfully!")
    except asyncio.TimeoutError:
        await ctx.send("⚠️ You didn't respond in time. The exchange message remains unchanged.")
    
import requests
import json

@siddhu.command(aliases=['lp'])
async def ltcprice(ctx):
    """Fetches the latest Litecoin (LTC) price in USD, EUR, and INR."""
    
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    
    # Load INR conversion rate from config.json
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        C2I_Rate = config.get("C2I_Rate", 87)  # Default to 87 if not found
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("❌ Failed to load conversion rate from config.json")

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        price_usd = data['market_data']['current_price']['usd']
        price_eur = data['market_data']['current_price']['eur']
        price_inr = round(price_usd * C2I_Rate, 2)  # Convert USD to INR

        response_msg = (
            f"# __**LTC PRICE**__ <:LTC:1322611807269031968>\n"
            f"**<:dollar:1322965559134126214>USD: `${price_usd:.2f}`\n"
            f"<:exch:1322953996389974048> EUR: `€{price_eur:.2f}`\n"
            f"<:INR:1322635698435784775> INR: `₹{price_inr}`**"
        )

        await ctx.send(response_msg)

        print(f"[ ✅ ] LTC PRICE SENT: ${price_usd:.2f}, €{price_eur:.2f}, ₹{price_inr}")

    else:
        await ctx.send("❌ Failed to fetch Litecoin price.")

@siddhu.command(aliases=['csol'])
async def solprice(ctx):
    """Fetches the latest Solana (SOL) price in USD, EUR, and INR."""
    
    url = 'https://api.coingecko.com/api/v3/coins/solana'
    
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        C2I_Rate = config.get("C2I_Rate", 87)
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("❌ Failed to load conversion rate from config.json")

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        price_usd = data['market_data']['current_price']['usd']
        price_eur = data['market_data']['current_price']['eur']
        price_inr = round(price_usd * C2I_Rate, 2)

        response_msg = (
            f"__**SOL PRICE**__ <:exchanger:1322954180452810775>\n"
            f"**<:dollar:1322965559134126214>USD: `${price_usd:.2f}`\n"
            f"<:exch:1322953996389974048> EUR: `€{price_eur:.2f}`\n"
            f"<:INR:1322635698435784775> INR: `₹{price_inr}`**"
        )

        await ctx.send(response_msg)

        print(f"[ ✅ ] SOL PRICE SENT: ${price_usd:.2f}, €{price_eur:.2f}, ₹{price_inr}")

    else:
        await ctx.send("❌ Failed to fetch Solana price.")

@siddhu.command(aliases=['cusdt'])
async def usdtprice(ctx):
    """Fetches the latest USDT (Tether) price in USD, EUR, and INR."""
    
    url = 'https://api.coingecko.com/api/v3/coins/tether'
    
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        C2I_Rate = config.get("C2I_Rate", 87)
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("❌ Failed to load conversion rate from config.json")

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        price_usd = data['market_data']['current_price']['usd']
        price_eur = data['market_data']['current_price']['eur']
        price_inr = round(price_usd * C2I_Rate, 2)

        response_msg = (
            f"__**USDT PRICE**__ <:exchanger:1322954180452810775>\n"
            f"**<:dollar:1322965559134126214>USD: `${price_usd:.2f}`\n"
            f"<:exch:1322953996389974048> EUR: `€{price_eur:.2f}`\n"
            f"<:INR:1322635698435784775> INR: `₹{price_inr}`**"
        )

        await ctx.send(response_msg)

        print(f"[ ✅ ] USDT PRICE SENT: ${price_usd:.2f}, €{price_eur:.2f}, ₹{price_inr}")

    else:
        await ctx.send("❌ Failed to fetch USDT price.")

import datetime
from dateutil import parser

@siddhu.command()
async def prune(ctx, duration: str):
    """
    Bans inactive members based on the specified duration.
    Usage: .prune <duration>
    Example: .prune 1h (bans members inactive for more than 1 hour)
    """
    time_units = {'m': 60, 'h': 3600, 'd': 86400}  # Supported units
    unit = duration[-1].lower()

    if unit not in time_units:
        await ctx.send(
            "<:CROSS_TDG:1321149916201881683> Invalid time unit! Use `m` for minutes, `h` for hours, or `d` for days.\n"
            "Example: `.prune 10m`, `.prune 1h`, `.prune 2d`."
        )
        return

    try:
        amount = int(duration[:-1])
        if amount <= 0:
            raise ValueError
    except ValueError:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid duration! Provide a positive number followed by 'm', 'h', or 'd'.")
        return

    # Calculate threshold time using `dateutil`
    seconds = amount * time_units[unit]
    threshold_time = parser.parse(datetime.datetime.utcnow().isoformat()) - datetime.timedelta(seconds=seconds)

    banned_count = 0
    for member in ctx.guild.members:
        if member.bot or member == ctx.author or member == siddhu.user:
            continue

        # Check inactivity based on `joined_at`
        if member.joined_at and parser.parse(member.joined_at.isoformat()) < threshold_time:
            try:
                await member.ban(reason=f"Banned for inactivity over {duration}")
                banned_count += 1
            except discord.Forbidden:
                print(f"Failed to ban {member.name}: Missing permissions.")
            except discord.HTTPException as e:
                print(f"Failed to ban {member.name}: {e.text}")

    await ctx.send(f"<:Tick:1290693799361777665> Pruning complete! Banned {banned_count} members inactive for over `{duration}`.")

import json
import os
import hashlib
import base58
import ecdsa
from mnemonic import Mnemonic

WALLET_FILE = "wallet.json"

def generate_ltc_wallet():
    """Generates a real Litecoin address, private key, and mnemonic."""
    
    # Generate a 12-word mnemonic
    mnemo = Mnemonic("english")
    mnemonic_code = mnemo.generate(strength=128)  # 12 words

    # Convert mnemonic to a seed (BIP39)
    seed = mnemo.to_seed(mnemonic_code)

    # Derive private key (first 32 bytes of SHA256(seed))
    private_key = hashlib.sha256(seed).digest().hex()
    
    # Generate public key from private key
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()

    # Hash the public key
    sha256_pubkey = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_pubkey)
    hashed_pubkey = ripemd160.digest()

    # Add Litecoin mainnet prefix (0x30)
    network_byte = b'\x30' + hashed_pubkey
    checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]
    
    # Generate final LTC address
    ltc_address = base58.b58encode(network_byte + checksum).decode()

    return ltc_address, private_key, mnemonic_code

import aiohttp
import os
import json
from io import StringIO

WALLET_FILE = "wallet.json"
TATUM_API = "t-662bd6a3b6c859001c3e5564-723b6f686e1f48b99a77e966"  # Replace with your real API key

@siddhu.command()
async def cwallet(ctx, wallet_num: int):
    """Generates a real working LTC address & private key using Tatum API, saving it to wallet.json."""

    if wallet_num not in [1, 2, 3]:
        await ctx.send("<:CROSS_TDG:1321149916201881683> Invalid wallet number! Choose between `1, 2, or 3`.")
        return

    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        headers = {
            "x-api-key": TATUM_API,
            "Content-Type": "application/json"
        }

        async with session.get("https://api.tatum.io/v3/litecoin/wallet", headers=headers) as resp:
            if resp.status != 200:
                await ctx.send(f"❌ Tatum API Error (Wallet): {resp.status}", delete_after=5)
                return
            wallet_data = await resp.json()

        xpub = wallet_data['xpub']
        mnemonic = wallet_data['mnemonic']

        async with session.get(f"https://api.tatum.io/v3/litecoin/address/{xpub}/0", headers=headers) as resp:
            if resp.status != 200:
                await ctx.send(f"❌ Tatum API Error (Address): {resp.status}", delete_after=5)
                return
            address_data = await resp.json()

        address = address_data['address']

        payload = {
            "mnemonic": mnemonic,
            "index": 0
        }

        async with session.post("https://api.tatum.io/v3/litecoin/wallet/priv", headers=headers, json=payload) as resp:
            if resp.status != 200:
                await ctx.send(f"❌ Tatum API Error (PrivateKey): {resp.status}", delete_after=5)
                return
            priv_data = await resp.json()

        private_key = priv_data['key']

    # Save to wallet.json
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as file:
            wallet_data = json.load(file)
    else:
        wallet_data = {}

    wallet_data[str(wallet_num)] = {
        "address": address,
        "private_key": private_key
    }

    with open(WALLET_FILE, "w") as file:
        json.dump(wallet_data, file, indent=4)

    # Send the wallet
    await ctx.send("# __**LTC WALLET CREATED**__ <a:tz_ltc:1281238097136451616>\n"
                   "<:white_Arrow:1290693791983861822> **Store the private key & Mnemonic code safely & securely !** <a:check:1281246680724930683>\n\n"
                   f"**<:bxbz_monet_lovenote:1290693793724497920> Wallet Number: `Wallet {wallet_num}`**\n\n"
                   "<a:tz_ltc:1281238097136451616> **Address:**\n"
                   f"`{address}`\n\n"
                   "<:emoji_1738342244745:1334928872269152259> **Private Key:**\n"
                   f"||{private_key}||\n\n"
                   "<:TOS:1336669803221614622> **Mnemonic Code (Backup):**"
                   f"```{mnemonic}```")

@siddhu.command(aliases=['cbtc'])
async def btcprice(ctx):
    """Fetches the latest Bitcoin (BTC) price in USD, EUR, and INR."""
    
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
    
    # Load INR conversion rate from config.json
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        C2I_Rate = config.get("C2I_Rate", 87)  # Default to 87 if not found
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("❌ Failed to load conversion rate from config.json")

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        price_usd = data['market_data']['current_price']['usd']
        price_eur = data['market_data']['current_price']['eur']
        price_inr = round(price_usd * C2I_Rate, 2)

        response_msg = (
            f"__**BTC PRICE**__ <:SA_BTC_BitCoin:1342764860928426057>\n"
            f"**<:dollar:1322965559134126214>USD: `${price_usd:.2f}`\n"
            f"<:exch:1322953996389974048> EUR: `€{price_eur:.2f}`\n"
            f"<:INR:1322635698435784775> INR: `₹{price_inr}`**"
        )

        await ctx.send(response_msg)

        print(f"[ ✅ ] BTC PRICE SENT: ${price_usd:.2f}, €{price_eur:.2f}, ₹{price_inr}")

    else:
        await ctx.send("❌ Failed to fetch Bitcoin price.")
        
import discord
import json
import requests
from discord.ext import commands

# Load config.json to get C2I_Rate (USD to INR conversion rate)
with open("config.json", "r") as f:
    config = json.load(f)

C2I_Rate = config.get("C2I_Rate", 87)  # Default to 87 if not found

# Function to fetch crypto prices
def get_crypto_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price_usd = data['market_data']['current_price']['usd']
        price_eur = data['market_data']['current_price']['eur']
        price_inr = price_usd * C2I_Rate
        return price_usd, price_eur, price_inr
    return None, None, None

# Command function
async def crypto_price(ctx, coin_name):
    price_usd, price_eur, price_inr = get_crypto_price(coin_name.lower())
    if price_usd:
        await ctx.send(
            f"__**{coin_name.upper()} PRICE**__ <:exchanger:1322954180452810775>\n"
            f"**<:dollar:1322965559134126214>USD: `${price_usd:.2f}`\n"
            f"<:exch:1322953996389974048> EUR: `€{price_eur:.2f}`\n"
            f"<:INR:1322635698435784775> INR: `₹{price_inr:.2f}`**"
        )
    else:
        await ctx.send(f"❌ Failed to fetch {coin_name.upper()} price.")

# Define 9 crypto commands
@siddhu.command(aliases=['ceth'])
async def ethprice(ctx):
    await crypto_price(ctx, "ethereum")

@siddhu.command(aliases=['cxrp'])
async def xrpprice(ctx):
    await crypto_price(ctx, "ripple")

@siddhu.command(aliases=['cbnb'])
async def bnbprice(ctx):
    await crypto_price(ctx, "binancecoin")

@siddhu.command(aliases=['cada'])
async def adaprice(ctx):
    await crypto_price(ctx, "cardano")

@siddhu.command(aliases=['cdoge'])
async def dogeprice(ctx):
    await crypto_price(ctx, "dogecoin")

@siddhu.command(aliases=['cshib'])
async def shibprice(ctx):
    await crypto_price(ctx, "shiba-inu")

@siddhu.command(aliases=['cavax'])
async def avaxprice(ctx):
    await crypto_price(ctx, "avalanche-2")

@siddhu.command(aliases=['cpolk'])
async def polkaprice(ctx):
    await crypto_price(ctx, "polkadot")

@siddhu.command(aliases=['cftm'])
async def ftmprice(ctx):
    await crypto_price(ctx, "fantom")        
        
@siddhu.command()
async def ar(ctx, *, trigger_and_response: str):
    # Split the trigger and response using a comma (",")
    trigger, response = map(str.strip, trigger_and_response.split(','))

    with open('ar.json', 'r') as file:
        data = json.load(file)

    data[trigger] = response

    with open('ar.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send(f'<:lr_tick_1:1290693800808677461> **Auto Response Has Added.. !** **{trigger}** - **{response}**')
    await ctx.message.delete()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} AUTO RESPOND ADDED<:Tick:1290693799361777665> ")

@siddhu.command()
async def removear(ctx, trigger: str):
    with open('ar.json', 'r') as file:
        data = json.load(file)

    if trigger in data:
        del data[trigger]

        with open('ar.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.send(f'<:lr_tick_1:1290693800808677461> **Auto Response Has Removed** **{trigger}**')
        await ctx.message.delete()
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} AUTO RESPOND REMOVE<:Tick:1290693799361777665> ")
    else:
        await ctx.send(f'<:lr_tick_1:1290693800808677461> **Auto Response Not Found** **{trigger}**')
        
import json

@siddhu.command()
async def ar_list(ctx):
    try:
        with open("ar.json", "r") as f:
            data = json.load(f)  # Load JSON data properly
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("<:CROSS_TDG:1321149916201881683> NO AUTO RESPONDER TRIGGER FOUND")
        return

    if not data:  # If the file is empty
        await ctx.send("<:CROSS_TDG:1321149916201881683> NO AUTO RESPONDER TRIGGER FOUND")
        return

    # Formatting the output message
    message = "# <:note:1290693795763195945> AUTORESPOND LIST\n"
    for trigger, response in data.items():
        message += f"""
<:white_arrow:1290693789824061461> **TRIGGER :-** `{trigger}`
<:white_arrow:1290693789824061461> **RESPONSE :-** `{response}`
"""

    await ctx.send(message)
    await ctx.message.delete()
    print("[+] ar_list Command Used")

@siddhu.command()
async def am_list(ctx):
    try:
        with open("am.json", "r") as f:
            data = json.load(f)  # Load JSON data properly
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("<:CROSS_TDG:1321149916201881683> NO AUTO MESSAGE TASK FOUND")
        return

    if not data:  # If the file is empty
        await ctx.send("<:CROSS_TDG:1321149916201881683> NO AUTO MESSAGE TASK FOUND")
        return

    # Formatting the output message
    message = "# <:note:1290693795763195945> **AUTOMESSAGE LIST**\n"
    for channel_id, info in data.items():
        message += f"""
<:rdx_glowin_heart:1288196137848803451> **CHANNEL ID :-** `{channel_id}`
<:white_arrow:1290693789824061461> **TIME IN SECONDS :-** `{info['time']}`
<:white_arrow:1290693789824061461> **CONTENT :-** `{info['content']}`
"""

    await ctx.send(message)
    await ctx.message.delete()
    print("[+] am_list Command Used")

import discord
import asyncio

@siddhu.command()
async def csrv(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = siddhu.get_guild(source_guild_id)
    target_guild = siddhu.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("<a:Diamonds:1272969331596198010> **Guild Not Found**")
        return

    # Delete all channels in the target guild
    for channel in target_guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel {channel.name} in target guild.")
            await asyncio.sleep(0)
        except Exception as e:
            print(f"Error deleting channel {channel.name}: {e}")

    # Delete all roles in the target guild except "@everyone"
    for role in target_guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"Deleted role {role.name} in target guild.")
                await asyncio.sleep(0)
            except Exception as e:
                print(f"Error deleting role {role.name}: {e}")

    # Clone roles from source to target in correct order
    roles = sorted(source_guild.roles, key=lambda r: r.position, reverse=True)  # Top roles first
    role_mapping = {}

    for role in roles:
        try:
            new_role = await target_guild.create_role(
                name=role.name,
                permissions=role.permissions,
                color=role.color,
                hoist=role.hoist,
                mentionable=role.mentionable
            )
            role_mapping[role.id] = new_role
            print(f"Created role {role.name} in target guild.")
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error creating role {role.name}: {e}")

    # Clone categories and channels
    category_mapping = {}

    for category in sorted(source_guild.categories, key=lambda c: c.position):
        try:
            new_category = await target_guild.create_category(name=category.name)
            category_mapping[category.id] = new_category
            print(f"Created category {category.name} in target guild.")
            await asyncio.sleep(0)
        except Exception as e:
            print(f"Error creating category {category.name}: {e}")

    # Clone text and voice channels
    for channel in sorted(source_guild.channels, key=lambda c: c.position):
        try:
            overwrites = {}

            for target in channel.overwrites:
                target_role = role_mapping.get(target.id)  # Get mapped role in target guild
                if target_role:
                    overwrites[target_role] = channel.overwrites[target]
            
            new_channel = None

            if isinstance(channel, discord.TextChannel):
                new_channel = await target_guild.create_text_channel(name=channel.name, category=category_mapping.get(channel.category_id), overwrites=overwrites)
            elif isinstance(channel, discord.VoiceChannel):
                new_channel = await target_guild.create_voice_channel(name=channel.name, category=category_mapping.get(channel.category_id), overwrites=overwrites)

            if new_channel:
                print(f"Created channel {channel.name} in target guild.")
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error creating channel {channel.name}: {e}")

    await ctx.send("<a:Diamonds:1272969331596198010> **Server Copy Completed!**")
    
import discord
from discord.ext import commands
from dateutil import parser

from discord.utils import get
from dateutil import parser

@siddhu.command(aliases=["user_info", "ui"])
async def userinfo(ctx, user: discord.Member = None):
    """Fetch and display user information in a text format using dateutil."""
    try:
        if user is None:
            user = ctx.author

        # Fetch banner
        try:
            user_profile = await siddhu.http.get_user_profile(user.id)
            banner_hash = user_profile['user'].get('banner')
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_hash}.png?size=600" if banner_hash else None
        except Exception:
            banner_url = None

        # Fetch avatar (FIXED: convert to string)
        avatar_url = str(user.avatar_url) if user.avatar else None

        # Parse account creation time
        created_at = parser.parse(str(user.created_at))
        created_timestamp = f"<t:{int(created_at.timestamp())}:F>"

        # Account age in years
        account_age = (ctx.message.created_at - created_at).days // 365

        # Mutual servers
        mutual_guilds = len(user.mutual_guilds) if hasattr(user, "mutual_guilds") else "Unknown"

        # Presence and activity
        presence = str(user.status).title() if isinstance(user, discord.Member) else "Unknown"
        activity = user.activity.name if isinstance(user, discord.Member) and user.activity else "None"

        # Bot status
        bot_status = "Yes" if user.bot else "No"

        # Prepare formatted message
        user_info_msg = f"""
## User Information <:rules:1290926829762383934>  
<:user:1325418236514140282> **Name** : {user.name}  
<:star_blue:1284898457181622362> **User ID** : {user.id}  
<:star_blue:1284898457181622362> **Account Age** : {account_age} Years  
<:star_blue:1284898457181622362> **Created At** : {created_timestamp}  
<:star_blue:1284898457181622362> **User Banner** : [ [{user.name}'s Banner]({banner_url if banner_url else 'N/A'}) ]  
<:star_blue:1284898457181622362> **User Avatar** : [ [{user.name}'s Avatar]({avatar_url if avatar_url else 'N/A'}) ]  

**<a:Bot:1336670517486161951> Bot User** : {bot_status}  
**<:Partner:1290693797000380437> Presence** : {presence}  
**<:TOS:1336669803221614622> Activity** : {activity}  
**<:SQ_hearts:1288196135206518825> Mutual Servers** : {mutual_guilds}  
        """

        if embed_mode_enabled:
            await send_custom_embed(
                ctx,
                description=user_info_msg,
                thumbnail=avatar_url,
                image=banner_url
            )
        else:
            await ctx.send(user_info_msg)

    except Exception as e:
        await ctx.send(f"❌ Error fetching user info: {e}")
    
import discord
from discord.ext import tasks, commands
import json

# Dictionary to store tasks
tasks_dict = {}

@siddhu.command()
async def am(ctx, time_in_sec: int, channel_or_user: str, *, content: str):
    await ctx.message.delete()
    channel = None

    # Initialize channel variable
    # **If it's a mentioned channel (e.g., #general)**
    if channel_or_user.startswith("<#") and channel_or_user.endswith(">"):
        channel_id = int(channel_or_user[2:-1])  # Extract channel ID from mention
        channel = siddhu.get_channel(channel_id)

    # **If it's a direct Channel ID**
    elif channel_or_user.isdigit():
        channel_id = int(channel_or_user)
        channel = siddhu.get_channel(channel_id)

    # Try fetching as a text channel
    # If it's not found, assume it's a **user ID** and try DM
    if channel is None:
        try:
            user = await siddhu.fetch_user(int(channel_or_user))
            channel = await user.create_dm()
        except Exception:
            await ctx.send("<:lr_tick_1:1290693800808677461> `Invalid channel or user ID.`")
            return

    # If channel is still None, return error
    if channel is None:
        await ctx.send("<:lr_tick_1:1290693800808677461> `Channel or DM not found.`")
        return

    if time_in_sec <= 0:
        await ctx.send("<:lr_tick_1:1290693800808677461> `Time must be greater than 0.`")
        return

    # Check if the auto-message task already exists
    if channel.id in tasks_dict:
        await ctx.send(f"<:lr_tick_1:1290693800808677461> **Auto Message already exists for this target.**")
        return

# Define the looping task function
    async def auto_message_task(channel, content, time_in_sec):
        while True:
            await channel.send(content)
            await asyncio.sleep(time_in_sec)

# Create the task and start it
    task = asyncio.create_task(auto_message_task(channel, content, time_in_sec))

# Store the task reference
    tasks_dict[channel.id] = task

    # Save the task data in am.json
    try:
        with open("am.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[str(channel.id)] = {"time": time_in_sec, "content": content}

    with open("am.json", "w") as f:
        json.dump(data, f, indent=4)

    await ctx.send(f"**Auto Message set to every {time_in_sec} seconds in {'DM' if isinstance(channel, discord.DMChannel) else f'channel {channel.mention}'}.**")
    print("[+] Automessage Set Successfully")

@siddhu.command()
async def am_stop(ctx, *, identifier: str):
    await ctx.message.delete()

    try:
        # Load auto-message data
        with open("am.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        await ctx.send("<:lr_tick_1:1290693800808677461> `No Auto Message task found.`")
        return

    found = None

    # **Check if identifier is a channel mention (e.g., #general)**
    if identifier.startswith("<#") and identifier.endswith(">"):
        channel_id = identifier[2:-1]
        if channel_id in data:
            found = channel_id

    # **Check if identifier is a direct channel ID**
    elif identifier.isdigit():
        if identifier in data:
            found = identifier

    # **Check if identifier exactly matches a message trigger**
    else:
        for channel_id, info in data.items():
            if identifier == info["content"]:  # Exact match only
                found = channel_id
                break

    # **Stop the task if found**
    if found:
        if found in tasks_dict:
            tasks_dict[found].cancel()
            del tasks_dict[found]

        # Remove from JSON data
        if found in data:
            del data[found]

        # Save updated data
        with open("am.json", "w") as f:
            json.dump(data, f, indent=4)

        await ctx.send(f"✅ `Auto Message stopped successfully.`")
        print("[+] Auto Message Stopped Successfully")
    else:
        await ctx.send("<:lr_tick_1:1290693800808677461> `No matching Auto Message task found.`")
 
@siddhu.command()
async def am_clear(ctx):
    await ctx.message.delete()

    # Stop all tasks
    for task in tasks_dict.values():
        task.cancel()
    tasks_dict.clear()

    # Clear am.json
    with open("am.json", "w") as f:
        json.dump({}, f, indent=4)

    await ctx.send("<:lr_tick_1:1290693800808677461> `All Auto Messages have been cleared.`")
    print("[+] All Auto Messages Cleared") 
 
import discord
from discord.ext import commands
import random
import aiohttp
import json
from datetime import datetime

@siddhu.command()
async def horoscope(ctx, sign: str):
    """Fetches the daily horoscope for a given zodiac sign."""
    url = f"https://aztro.sameerkumar.website?sign={sign}&day=today"
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            data = await response.json()
            await ctx.send(f"Horoscope for {sign.capitalize()}: {data['description']}")

@siddhu.command()
async def chuck_norris(ctx):
    """Sends a random Chuck Norris joke."""
    url = "https://api.chucknorris.io/jokes/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            await ctx.send(data["value"])

@siddhu.command()
async def dad_joke(ctx):
    """Sends a random dad joke."""
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            await ctx.send(data["joke"])

@siddhu.command()
async def inspire_me(ctx):
    """Sends a random inspirational quote."""
    url = "https://zenquotes.io/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            await ctx.send(f"'{quote}' - {author}")

@siddhu.command()
async def pi_digits(ctx, digits: int):
    """Displays the first N digits of Pi."""
    if digits > 1000:
        await ctx.send("Please request 1000 or fewer digits.")
        return
    await ctx.send("3." + "14159265358979323846264338327950288419716939937510"[:digits])

@siddhu.command()
async def roll_dice(ctx, sides: int = 6):
    """Rolls a dice with the specified number of sides."""
    result = random.randint(1, sides)
    await ctx.send(f"The dice rolled: {result}")

@siddhu.command()
async def space_fact(ctx):
    """Fetches a random fact about space."""
    facts = [
        "A day on Venus is longer than a year on Venus.",
        "There are more stars in the universe than grains of sand on Earth.",
        "A teaspoon of a neutron star would weigh 6 billion tons.",
    ]
    await ctx.send(random.choice(facts))

@siddhu.command()
async def is_palindrome(ctx, word: str):
    """Checks if a word is a palindrome."""
    if word.lower() == word.lower()[::-1]:
        await ctx.send(f"Yes, '{word}' is a palindrome.")
    else:
        await ctx.send(f"No, '{word}' is not a palindrome.")

@siddhu.command()
async def urban_dictionary(ctx, *, word: str):
    """Fetches the Urban Dictionary definition of a word."""
    url = f"http://api.urbandictionary.com/v0/define?term={word}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data["list"]:
                await ctx.send(f"**{word.capitalize()}**: {data['list'][0]['definition']}")
            else:
                await ctx.send(f"No definition found for '{word}'.")

@siddhu.command()
async def ip_lookup(ctx, ip: str):
    """Fetches information about an IP address."""
    url = f"http://ip-api.com/json/{ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data["status"] == "success":
                await ctx.send(
                    f"**IP:** {data['query']}\n"
                    f"**Country:** {data['country']}\n"
                    f"**Region:** {data['regionName']}\n"
                    f"**City:** {data['city']}\n"
                    f"**ISP:** {data['isp']}"
                )
            else:
                await ctx.send("Invalid IP address.")

@siddhu.command()
async def pokemon(ctx, name: str):
    """Fetches information about a Pokémon."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(
                    f"**{data['name'].capitalize()}**:\n"
                    f"Type: {', '.join(t['type']['name'] for t in data['types'])}\n"
                    f"Height: {data['height']} | Weight: {data['weight']}"
                )
            else:
                await ctx.send("Pokémon not found.")

@siddhu.command()
async def random_movie(ctx):
    """Suggests a random movie."""
    movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]
    await ctx.send(f"How about watching '{random.choice(movies)}'?")
    
@siddhu.command()
async def hash_string(ctx, *, text: str):
    """Generates the hash of a string."""
    import hashlib
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    await ctx.send(f"SHA-256 Hash: {hex_dig}")

@siddhu.command()
async def image_to_ascii(ctx, url: str):
    """Converts an image to ASCII art."""
    import requests
    from io import BytesIO
    from PIL import Image
    import numpy as np
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('L')  # Convert to grayscale
    img = img.resize((100, 50))  # Resize for better fit in ASCII art
    pixels = np.array(img)
    
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    ascii_image = ''.join([ascii_chars[pixel // 25] for pixel in pixels.flatten()])
    await ctx.send(f"```{ascii_image}```")

@siddhu.command()
async def emoji_to_name(ctx, emoji: discord.Emoji):
    """Converts an emoji to its name."""
    await ctx.send(f"The name of the emoji is: {emoji.name}")

@siddhu.command()
async def random_user(ctx):
    """Picks a random user from the server."""
    member = random.choice(ctx.guild.members)
    await ctx.send(f"Random user: {member.mention}")
   
import discord
from discord.ext import commands
import random
import json
import asyncio
import time
from datetime import datetime
import aiohttp

@siddhu.command()
async def countdown(ctx, seconds: int):
    """Creates a countdown timer."""
    for i in range(seconds, 0, -1):
        await ctx.send(f"{i} seconds remaining...")
        await asyncio.sleep(1)
    await ctx.send("Time's up!")

@siddhu.command()
async def reverse_image(ctx, url: str):
    """Generates a reversed version of an image."""
    # Requires image manipulation libraries like Pillow
    from PIL import Image
    from io import BytesIO
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_data = await response.read()
            img = Image.open(BytesIO(image_data))
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img.save("reversed_image.png")
    await ctx.send(file=discord.File("reversed_image.png"))

@siddhu.command()
async def reverse_geocode(ctx, lat: float, lon: float):
    """Gets the location (city, country) from latitude and longitude."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json") as resp:
            data = await resp.json()
            location = data.get("address", {}).get("city", "Unknown city")
            await ctx.send(f"The location at lat:{lat} lon:{lon} is: {location}")

@siddhu.command()
async def emoji_count(ctx):
    """Counts the total number of emojis in the server."""
    emojis = ctx.guild.emojis
    await ctx.send(f"The server has {len(emojis)} custom emojis.")

@siddhu.command()
async def random_cat_fact(ctx):
    """Generates a random cat fact."""
    facts = [
        "Cats can make over 100 different sounds.",
        "A cat’s nose is as unique as a human’s fingerprint.",
        "Cats have five toes on their front paws, but only four on the back ones."
    ]
    await ctx.send(f"**Cat Fact:** {random.choice(facts)}")

@siddhu.command()
async def ascii_qr_code(ctx, *, text: str):
    """Generates a QR code in ASCII format."""
    import qrcode
    from pyfiglet import figlet_format
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    ascii_art = figlet_format(text)
    await ctx.send(f"Here’s your ASCII QR Code for: {text}\n{ascii_art}")

@siddhu.command()
async def text_to_speech(ctx, *, text: str):
    """Converts text to speech and sends an audio file."""
    import pyttsx3
    engine = pyttsx3.init()
    engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()
    await ctx.send(file=discord.File("speech.mp3"))

@siddhu.command()
async def ascii_binary(ctx, *, text: str):
    """Converts text to binary in ASCII format."""
    binary_rep = ' '.join(format(ord(i), '08b') for i in text)
    await ctx.send(f"Binary representation: {binary_rep}")

@siddhu.command()
async def show_server_stats(ctx):
    """Displays statistics about the server (member count, channel count, etc.)."""
    total_members = len(ctx.guild.members)
    total_channels = len(ctx.guild.channels)
    total_roles = len(ctx.guild.roles)
    await ctx.send(f"Server Stats:\nMembers: {total_members}\nChannels: {total_channels}\nRoles: {total_roles}")

@siddhu.command()
async def random_urban_legend(ctx):
    """Shares a random urban legend."""
    legends = [
        "The Vanishing Hitchhiker: A person gives a ride to a young woman who disappears.",
        "The Mothman: A creature seen in Point Pleasant, West Virginia in the 1960s.",
        "The Killer in the Backseat: Someone is hiding in your backseat, waiting to harm you."
    ]
    await ctx.send(f"Urban Legend: {random.choice(legends)}")

@siddhu.command()
async def weather_alert(ctx, city: str):
    """Fetches weather alerts (if any) for a specified city."""
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            alerts = data.get('alerts', [])
            if alerts:
                alert_messages = "\n".join([f"Alert: {alert['event']}" for alert in alerts])
                await ctx.send(f"Weather Alerts for {city}:\n{alert_messages}")
            else:
                await ctx.send(f"No weather alerts for {city}.")

import json
import qrcode
import os

@siddhu.command()
async def ltcqr(ctx, wallet_num: str, amount: float = None):
    try:
        with open("wallet.json", "r") as f:
            wallets = json.load(f)

        if wallet_num not in wallets:
            await ctx.send(f"❌ Wallet `{wallet_num}` not found!")
            return

        address = wallets[wallet_num]["address"]
        if address == "Put Here":
            await ctx.send("❌ Wallet address not set!")
            return

        qr_data = f"litecoin:{address}"
        if amount:
            qr_data += f"?amount={amount}"

        # Generate QR Code
        qr = qrcode.make(qr_data)
        qr_path = f"ltc_qr_{wallet_num}.png"
        qr.save(qr_path)

        file = discord.File(qr_path)

        if embed_mode_enabled:
            async with aiohttp.ClientSession() as session:
                # Upload file and get URL
                image_url = await upload_file_and_get_url(session, file)

                # Send embed with image
                await send_custom_embed(
                    ctx,
                    title="Litecoin QR Generated",
                    description=f"**Wallet:** `{wallet_num}`\n**Address:** `{address}`" + (f"\n**Amount:** `{amount} LTC`" if amount else ""),
                    image=image_url
                )
        else:
            await ctx.send(f"✅ **Litecoin QR Code for Wallet {wallet_num}**", file=file)

        os.remove(qr_path)

    except Exception as e:
        await ctx.send(f"❌ Error: `{e}`")

import discord
import asyncio

@siddhu.command()
async def copy_roles(ctx, from_guild_id: int, target_guild_id: int = None):
    from_guild = ctx.bot.get_guild(from_guild_id)
    target_guild = ctx.bot.get_guild(target_guild_id) if target_guild_id else ctx.guild

    if not from_guild:
        return await ctx.send("Invalid source server ID provided.")
    if not target_guild:
        return await ctx.send("Invalid target server ID provided.")

    if not target_guild.me.guild_permissions.manage_roles:
        return await ctx.send("Error: Bot lacks Manage Roles permission in the target guild.")

    # **Step 1: Identify existing bot roles in target server**
    existing_bot_roles = [role for role in target_guild.roles if role.managed]

    # **Step 2: Delete all normal roles in target server (except @everyone & bot roles)**
    for role in sorted(target_guild.roles, key=lambda r: r.position, reverse=True):
        try:
            if role != target_guild.default_role and role not in existing_bot_roles:
                await role.delete()
        except discord.Forbidden:
            print(f"Skipped `{role.name}` (no permission)")
        except Exception as e:
            print(f"Error deleting `{role.name}`: {e}")

    # **Step 3: Copy roles from source (top to bottom)**
    role_mapping = {}
    for role in sorted(from_guild.roles, key=lambda r: r.position, reverse=True):
        if role == from_guild.default_role or role.managed:
            continue  # Skip @everyone and bot-managed roles

        try:
            new_role = await target_guild.create_role(
                name=role.name,
                color=role.color,
                hoist=role.hoist,
                mentionable=role.mentionable,
                permissions=role.permissions
            )
            role_mapping[role.id] = new_role
            await asyncio.sleep(0)  # Allow other tasks to run
        except discord.Forbidden:
            print(f"Skipped `{role.name}` (no permission)")
        except Exception as e:
            print(f"Error creating `{role.name}`: {e}")

    # **Step 4: Move existing bot roles to the bottom**
    try:
        role_positions = {role: i for i, role in enumerate(target_guild.roles) if role not in existing_bot_roles}
        last_position = max(role_positions.values(), default=0) + 1
        for bot_role in existing_bot_roles:
            role_positions[bot_role] = last_position
            last_position += 1

        await target_guild.edit_role_positions(role_positions)
    except Exception as e:
        print(f"Error repositioning bot roles: {e}")

    await ctx.send(f"✅ **Successfully copied roles from `{from_guild.name}` to `{target_guild.name}`!**")

@siddhu.command()
async def copy_channels(ctx, from_guild_id: int, target_guild_id: int = None):
    from_guild = ctx.bot.get_guild(from_guild_id)
    target_guild = ctx.bot.get_guild(target_guild_id) if target_guild_id else ctx.guild

    if not from_guild:
        return await ctx.send("Invalid source server ID provided.")

    if not target_guild:
        return await ctx.send("Invalid target server ID provided.")

    if not target_guild.me.guild_permissions.administrator:
        return await ctx.send("Error: Bot lacks administrator permissions in the target guild.")

    # **Step 1: Delete all categories & channels first**
    for channel in sorted(target_guild.channels, key=lambda c: c.position, reverse=True):  # Highest first
        try:
            await channel.delete()
        except discord.Forbidden:
            print(f"Skipped `{channel.name}` (no permission)")
        except Exception as e:
            print(f"Error deleting `{channel.name}`: {e}")

    # **Step 2: Copy categories first**
    category_mapping = {}
    for category in sorted(from_guild.categories, key=lambda c: c.position):
        try:
            new_category = await target_guild.create_category(
                name=category.name,
                position=category.position,
                overwrites={target_guild.default_role: category.overwrites.get(from_guild.default_role, discord.PermissionOverwrite())}
            )
            category_mapping[category.id] = new_category
        except discord.Forbidden:
            print(f"Skipped category `{category.name}` (no permission)")
        except Exception as e:
            print(f"Error creating `{category.name}`: {e}")

    # **Step 3: Copy text & voice channels under correct categories**
    for channel in sorted(from_guild.channels, key=lambda c: c.position):
        try:
            new_category = category_mapping.get(channel.category_id) if channel.category_id else None

            # Only copy @everyone role permissions
            overwrites = {target_guild.default_role: channel.overwrites.get(from_guild.default_role, discord.PermissionOverwrite())}

            if isinstance(channel, discord.TextChannel):
                await target_guild.create_text_channel(
                    name=channel.name,
                    category=new_category,
                    position=channel.position,
                    topic=channel.topic or None,
                    nsfw=channel.nsfw,
                    slowmode_delay=channel.slowmode_delay,
                    overwrites=overwrites
                )
            elif isinstance(channel, discord.VoiceChannel):
                await target_guild.create_voice_channel(
                    name=channel.name,
                    category=new_category,
                    position=channel.position,
                    user_limit=channel.user_limit,
                    bitrate=channel.bitrate,
                    overwrites=overwrites
                )
            elif isinstance(channel, discord.StageChannel):
                await target_guild.create_stage_channel(
                    name=channel.name,
                    category=new_category,
                    position=channel.position,
                    topic=channel.topic or None,
                    overwrites=overwrites
                )
            elif isinstance(channel, discord.ForumChannel):
                await target_guild.create_forum(
                    name=channel.name,
                    category=new_category,
                    position=channel.position,
                    topic=channel.topic or None,
                    slowmode_delay=channel.slowmode_delay,
                    nsfw=channel.nsfw,
                    overwrites=overwrites
                )
        except discord.Forbidden:
            print(f"Skipped `{channel.name}` (no permission)")
        except Exception as e:
            print(f"Error copying `{channel.name}`: {e}")

    await ctx.send(f"Successfully copied channels from `{from_guild.name}` to `{target_guild.name}`.")

@siddhu.command()
async def random_recipe(ctx):
    """Shares a random recipe idea."""
    recipes = [
        "Spaghetti Carbonara - A classic Italian pasta dish with egg, cheese, pancetta, and pepper.",
        "Grilled Cheese Sandwich - Simple yet delicious, with melted cheese between crispy bread slices.",
        "Chicken Caesar Salad - A salad with romaine, grilled chicken, croutons, and Caesar dressing."
    ]
    await ctx.send(f"Recipe suggestion: {random.choice(recipes)}")

@siddhu.command()
async def timezone_converter(ctx, time: str, from_tz: str, to_tz: str):
    """Converts time from one time zone to another."""
    from datetime import datetime
    import pytz
    try:
        from_zone = pytz.timezone(from_tz)
        to_zone = pytz.timezone(to_tz)
        local_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        local_time = from_zone.localize(local_time)
        converted_time = local_time.astimezone(to_zone)
        await ctx.send(f"The converted time is: {converted_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@siddhu.command()
async def text_art(ctx, *, text: str):
    """Generates a text art version of the provided text."""
    import pyfiglet
    art = pyfiglet.figlet_format(text)
    await ctx.send(f"```\n{art}\n```")

@siddhu.command()
async def quiz(ctx, *, question: str):
    """Sends a trivia question to the channel."""
    trivia_questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Who wrote '1984'?", "answer": "George Orwell"}
    ]
    question = random.choice(trivia_questions)
    await ctx.send(f"Trivia Question: {question['question']}")
    def check(m):
        return m.content.lower() == question['answer'].lower()
    msg = await ctx.bot.wait_for("message", check=check)
    await ctx.send(f"Correct! {msg.author.mention} got it right!")

@siddhu.command()
async def poetry(ctx):
    """Generates a random poetic line."""
    poems = [
        "The stars above, they twinkle bright, \nBut none so bright as your sweet smile.",
        "Beneath the moon, we stand as one, \nA journey begun, with love to run."
    ]
    await ctx.send(f"**Poetry:** {random.choice(poems)}")

@siddhu.command()
async def merge_images(ctx, url1: str, url2: str):
    """Merges two images into one."""
    # Requires image manipulation libraries like Pillow
    from PIL import Image
    from io import BytesIO
    async with aiohttp.ClientSession() as session:
        async with session.get(url1) as response1:
            image_data1 = await response1.read()
        async with session.get(url2) as response2:
            image_data2 = await response2.read()
    img1 = Image.open(BytesIO(image_data1))
    img2 = Image.open(BytesIO(image_data2))
    img1.paste(img2, (0, 0))
    img1.save("merged_image.png")
    await ctx.send(file=discord.File("merged_image.png"))
   
import qrcode
import json
import discord
from discord.ext import commands
from io import BytesIO

# Load config.json only once
with open("config.json", "r") as f:
    config_data = json.load(f)

def generate_upi_qr(upi_id, amount, note=""):
    """Generate a UPI QR code."""
    upi_url = f"upi://pay?pa={upi_id}&mc=&tr=&tn={note}&am={amount}&cu=INR"
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code to a buffer
    buffer = BytesIO()
    img.save(buffer, "PNG")
    buffer.seek(0)
    return buffer

@siddhu.command()
async def set_note(ctx, *, note: str):
    """Set a permanent pay note for UPI QR."""
    config_data["permanent_paynote"] = note  # Update in memory
    with open("config.json", "w") as f:
        json.dump(config_data, f, indent=4)  # Save to file
    
    await ctx.send(f"<:Tick:1290693799361777665> Permanent paynote has been set to: {note}")

import aiohttp

async def upload_file_and_get_url(session, file):
    """
    Uploads the file to the embed channel and returns the Discord CDN URL.
    Deletes the uploaded message immediately after to keep the channel clean.
    """
    url = f"https://discord.com/api/v10/channels/{embed_channel_id}/messages"

    data = aiohttp.FormData()
    data.add_field('file', file.fp, filename=file.filename, content_type='image/png')

    headers = {
        "Authorization": token,  # Your user or bot token
        "User-Agent": "Mozilla/5.0"
    }

    # Upload the file (send message with attachment)
    async with session.post(url, data=data, headers=headers) as resp:
        if resp.status == 200:
            message = await resp.json()
            attachment_url = message['attachments'][0]['url']
            message_id = message['id']

            # Delete the uploaded message immediately after to clean embed channel
            delete_url = f"https://discord.com/api/v10/channels/{embed_channel_id}/messages/{message_id}"
            async with session.delete(delete_url, headers=headers) as del_resp:
                if del_resp.status != 204:
                    print(f"Warning: Failed to delete uploaded message: {await del_resp.text()}")

            return attachment_url
        else:
            raise Exception(f"Failed to upload file: {await resp.text()}")

@siddhu.command()
async def upiqr(ctx, amount: str, *, note: str = None):
    upi_id = config_data.get("Upi", "Upload Here")
    permanent_note = config_data.get("permanent_paynote", "")
    note = note or permanent_note or "Not Set"

    if upi_id == "Upload Here" or "@" not in upi_id:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **UPI ID not found or invalid in config.json.**")
        return

    try:
        buffer = generate_upi_qr(upi_id, amount, note)
        file = discord.File(fp=buffer, filename='upi_qr.png')

        async with aiohttp.ClientSession() as session:
            if embed_mode_enabled:
                # Upload file to embed channel and get URL
                image_url = await upload_file_and_get_url(session, file)

                # Send embed to main channel (ctx) with image_url
                await send_custom_embed(
                    ctx,
                    title="UPI QR Generated",
                    description=f"**Amount:** ₹{amount}\n**To:** `{upi_id}`\n**Note:** `{note}`",
                    image=image_url
                )
            else:
                # Normal mode just send file normally
                await ctx.send(file=file)

        buffer.close()

    except Exception as e:
        await ctx.send(f"An error occurred: `{str(e)}`")

@siddhu.command()
async def upiqr2(ctx, amount: str, *, note: str = None):
    upi_id = config_data.get("Upi2", "Upload Here")
    permanent_note = config_data.get("permanent_paynote", "")
    note = note or permanent_note or "Not Set"

    if upi_id == "Upload Here" or "@" not in upi_id:
        await ctx.send("<:CROSS_TDG:1321149916201881683> **UPI2 ID not found or invalid in config.json.**")
        return

    try:
        buffer = generate_upi_qr(upi_id, amount, note)
        file = discord.File(fp=buffer, filename='upi_qr.png')

        async with aiohttp.ClientSession() as session:
            if embed_mode_enabled:
                # Upload file to embed channel and get URL
                image_url = await upload_file_and_get_url(session, file)

                # Send embed to main channel (ctx) with image_url
                await send_custom_embed(
                    ctx,
                    title="UPI2 QR Generated",
                    description=f"**Amount:** ₹{amount}\n**To:** `{upi_id}`\n**Note:** `{note}`",
                    image=image_url
                )
            else:
                # Normal mode just send file normally
                await ctx.send(file=file)

        buffer.close()

    except Exception as e:
        await ctx.send(f"An error occurred: `{str(e)}`")
    
@siddhu.command(name='joke')
async def joke(ctx):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    await ctx.send(f"<:lr_tick_1:1290693800808677461> {joke['setup']} - {joke['punchline']}")
    await ctx.message.delete()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}JOKE <:Tick:1290693799361777665> ")

import requests

@siddhu.command(name="meme")
async def meme(ctx):
    response = requests.get("https://meme-api.com/gimme")
    meme_data = response.json()
    meme_url = meme_data.get("url")

    await ctx.message.delete()

    if not meme_url:
        await ctx.send("Failed to get meme :(")
        return

    if not embed_mode_enabled:
        await ctx.send(meme_url)
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}MEME SENT<:Tick:1290693799361777665>")
        return

    # Embed mode - send embed with image using send_custom_embed without footer params
    await send_custom_embed(
        ctx,
        title="Random Meme",
        image=meme_url,
    )
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}MEME SENT (EMBED MODE)<:Tick:1290693799361777665>")
    
@siddhu.command()
async def dm(ctx, user: discord.User, *, message: str):
    """
    Send a direct message to a specified user.
    Usage: .dm @user/username/userid <message>
    """
    await ctx.message.delete()  # Deletes the command message for cleanliness

    try:
        # Send the DM
        await user.send(message)
        await ctx.send(f"<:Tick:1290693799361777665> Message successfully sent to **{user.name}**", delete_after=5)
    except discord.Forbidden:
        await ctx.send("<:CROSS_TDG:1321149916201881683> I cannot send a DM to this user. They might have DMs disabled.")
    except discord.HTTPException as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred while sending the DM: {e}", delete_after=5)

@siddhu.command(name="l2u")
@commands.cooldown(1, 3, commands.BucketType.user)
async def l2u(ctx, ltc_amt: float):
    """
    Convert Litecoin (LTC) to USD based on live rates from CoinGecko.
    Args:
        ctx: The context of the command.
        ltc_amt: The amount of Litecoin to convert.
    """
    try:
        # Fetch Litecoin price in USD from CoinGecko
        coingecko_resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        coingecko_resp.raise_for_status()
        ltc_to_usd_rate = coingecko_resp.json()['litecoin']['usd']

        # Calculate USD amount
        usd_amount = ltc_amt * ltc_to_usd_rate

        # Format the response
        response = (
            f"# __**LTC TO USD**__ <:exchange:1322965557372260402>\n"
            f"> <:exchange:1322954260404768850> **LTC PRICE :** `${ltc_to_usd_rate:.2f}`\n"
            f"> <a:tz_ltc:1281238097136451616> **LTC AMOUNT :** `{ltc_amt:.8f} LTC`\n"
            f"> <:dollar:1322965559134126214> **USD AMOUNT :** `${usd_amount:.2f}`"
        )

        await ctx.message.delete()
        await ctx.send(response)

        # Log the action
        print(f"[+] L2U Command Executed: {ltc_amt} LTC = ${usd_amount:.2f}")

    except requests.RequestException as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error fetching Litecoin price:** `{e}`")

@siddhu.command(name="u2l")
@commands.cooldown(1, 3, commands.BucketType.user)
async def u2l(ctx, usd_amt: float):
    """
    Convert USD to Litecoin (LTC) based on live rates from CoinGecko.
    Args:
        ctx: The context of the command.
        usd_amt: The amount of USD to convert.
    """
    try:
        # Fetch Litecoin price in USD from CoinGecko
        coingecko_resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        coingecko_resp.raise_for_status()
        ltc_to_usd_rate = coingecko_resp.json()['litecoin']['usd']

        # Calculate LTC amount
        ltc_amount = usd_amt / ltc_to_usd_rate

        # Format the response
        response = (
            f"# __**USD TO LTC**__ <:exchange:1322965557372260402>\n"
            f"> <:exchange:1322954260404768850> **LTC PRICE :** `${ltc_to_usd_rate:.2f}`\n"
            f"> <:dollar:1322965559134126214> **USD AMOUNT :** `${usd_amt:.2f}`\n"
            f"> <a:tz_ltc:1281238097136451616> **LTC AMOUNT :** `{ltc_amount:.8f} LTC`"
        )

        await ctx.message.delete()
        await ctx.send(response)

        # Log the action
        print(f"[+] U2L Command Executed: ${usd_amt:.2f} = {ltc_amount:.8f} LTC")

    except requests.RequestException as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> **Error fetching Litecoin price:** `{e}`")
        
@siddhu.command()
async def support(ctx,*, message):
    await ctx.message.delete()
    msg = {
        "content": f"## Received New Support Message\n- **Message Sent By {ctx.author.name} ID {ctx.author.id}**\n**Message Content** = `{message}`"
    }
    try:
        r = requests.post("https://discord.com/api/webhooks/1334078367473078273/ZcilgcSPa7vzQ0vHoqkeOgWMQGfU8AvLSRMMkRlWafUSEPWUfajYFpg1QmwUseSRG-YH" , json=msg)
        print("[+] Support Message Sent Succesfully")
        await ctx.send("**Support Message Sent Succesfully**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}SUPPORT<:Tick:1290693799361777665> ")
    except:
        await ctx.send("**Failed. Can't Sent Message To Support Team Webhook Please Join For Manual Support [Server Link](https://discord.gg/tzshopp) **")
                    
@siddhu.command()
async def selfbot(ctx):
    description_text = """# <:Crown_king:1290693780118442034> __[SyntheX Prime V5](https://cdn.discordapp.com/attachments/1255090765726748694/1377530053151162439/20250529_103152.jpg?ex=68394c55&is=6837fad5&hm=df6654c6daae427fe2c9c75c3480bce1e74dd19a59045903a789c14e80824ae0&)__ <:Crown_king:1290693780118442034> 
**<:BadgeDeveloper:1290693804013129768> VERSION - `SELFBOT V5`**
<:4Bots:1290928020277690368> **CREATOR** - `siddhu.og`
<:TOS:1336669803221614622> **TOTAL COMMANDS** - `546 COMMANDS`
<:Titanz:1281243485919510569> **SUPPORT SERVER** - [Join Now !](https://discord.gg/g4Hv6Rxquv)
<:Titanz:1281243482811400324> **BUY NOW** - [AutoBuy Here !](https://siddhushop.mysellauth.com/product/synthex-prime-v5)

**<:nxt_blue_crown:1281973611917348989> WELCOME TO SyntheX Prime V5!**
> **One of the best and most feature-rich selfbots out there!**

**WHY CHOOSE SyntheX Prime V5?**
- Powerful and customizable commands at your fingertips.
- Created by **siddhu.og**, trusted by many.
- 24/7 support via our Support Server.
- Secure and reliable with features designed to make your Discord experience smoother.
"""

    if embed_mode_enabled:
        await send_custom_embed(
            ctx,
            description=description_text,
            footer_text="Developed by siddhu.og",
            footer_icon="https://cdn.discordapp.com/avatars/1241519716644819014/2f75df45d57c600a49370caab69cd051.webp?size=1024",
            image="https://cdn.discordapp.com/attachments/1255090765726748694/1377530053151162439/20250529_103152.jpg?ex=68394c55&is=6837fad5&hm=df6654c6daae427fe2c9c75c3480bce1e74dd19a59045903a789c14e80824ae0&",
            timestamp=True
        )
    else:
        await ctx.send(description_text)

    await ctx.message.delete()

    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}SELFBOT INFO<:Tick:1290693799361777665> ")

@siddhu.command()
async def crypto_prices(ctx):
    await ctx.send('''# <:OwnerSpecial:1290692086122680321> **CRYPTO PRICES :-**
<:white_arrow:1290693789824061461>**BTC Price** :- `.btcprice`
<:white_arrow:1290693789824061461>**ETH Price** :- `.ethprice`
<:white_arrow:1290693789824061461>**XRP Price** :- `.xrpprice`
<:white_arrow:1290693789824061461>**BNB Price** :- `.bnbprice`
<:white_arrow:1290693789824061461>**ADA Price** :- `.adaprice`
<:white_arrow:1290693789824061461>**Doge Price** :- `.dogeprice`
<:white_arrow:1290693789824061461>**Shib Price** :- `.shibprice`
<:white_arrow:1290693789824061461>**AVAX Price** :- `.avaxprice`
<:white_arrow:1290693789824061461>**Polkadot Price** :- `.polkaprice`
<:white_arrow:1290693789824061461>**Fantom Price** :- `.ftmprice`
<:white_arrow:1290693789824061461>**SOL Price** :- `.solprice`
<:white_arrow:1290693789824061461>**USDT Price** :- `.usdtprice`''')
    await ctx.message.delete()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}CRYPTO PRICES<:Tick:1290693799361777665> ")
    
@siddhu.command()
async def checkpromo(ctx, *, promo_links):
    await ctx.message.delete()
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code, ctx)
                await ctx.send(result)
            else:
                await ctx.send(f'**INVALID LINK** : `{link}`')

async def check_promo(session, promo_code, ctx):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'**Code:** {promo_code}\n**Status:** ALREADY CLAIMED'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return (f'**Code:** {promo_code}\n'
                        f'**Expiry Date:** {days} days\n'
                        f'**Expires At:** {exp_at}\n'
                        f'**Title:** {title}')
                
        elif response.status == 429:
            return '**RATE LIMITED**'
        else:
            return f'**INVALID CODE** : `{promo_code}`'

def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
        
import aiohttp
import datetime
import json

import discord
import aiohttp
import datetime
from discord.ext import commands

@siddhu.command(aliases=["checktoken"], description="Sends information about a token.")
async def tokeninfo(ctx, token: str):
    await ctx.send(content="Checking token...")

    headers = {"Authorization": token, "Content-Type": "application/json"}

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://discord.com/api/v9/users/@me", headers=headers
        ) as res:
            if res.status == 401:
                await ctx.send(content="Invalid token.")
                return

            data = await res.json()
            username = f"{data['username']}#{data['discriminator']}"
            user_id = data["id"]
            email = data.get("email", "N/A")
            phone = data.get("phone", "N/A")
            mfa_enabled = data["mfa_enabled"]

            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) / 1000
            ).strftime("%d-%m-%Y %H:%M:%S UTC")

        async with session.get(
            "https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers
        ) as res:
            nitro_data = await res.json()
            if nitro_data:
                premium_type = nitro_data[0].get("premium_type", 0)
                nitro_type = {
                    2: "Nitro Boost",
                    3: "Nitro Basic",
                }.get(premium_type, "Unknown Nitro Type")
                renew_date = nitro_data[0].get("current_period_end", "Unknown")
                if renew_date != "Unknown":
                    try:
                        renew_date = datetime.datetime.fromisoformat(renew_date).strftime("%Y-%m-%d %H:%M:%S UTC")
                    except ValueError:
                        pass  # If parsing fails, keep the raw value
            else:
                nitro_type = "None"
                renew_date = "None"

        async with session.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ) as res:
            guilds = await res.json()
            guild_count = len(guilds)

        async with session.get(
            "https://discord.com/api/v9/users/@me/relationships", headers=headers
        ) as res:
            friends = await res.json()
            friend_count = len(friends)

    message = f"""
# Token Info <:nxt_blue_crown:1281973611917348989>  
`Fetched from Discord API`

**<:user:1325418236514140282> [Username] {username}  
<:discord:1282007043456241717> [ID] {user_id}  
<:bxbz_monet_lovenote:1290693793724497920> [Email] {email}  
<:experienced_seller:1290924799421583391> [Phone Number] {phone}  
<:uptime:1320649297796010075> [Creation Date] {creation_date}  

<a:tz_Nitro:1281238104916889652> [Nitro Type] {nitro_type}  
<:Titanz:1281243485919510569> [Renews at] {renew_date}  

<:white_arrow:1290693789824061461>[Servers] {guild_count}  
<:white_arrow:1290693789824061461>[Friends] {friend_count}  
<:white_arrow:1290693789824061461>[2FA Enabled] {mfa_enabled}**
"""

    await ctx.send(content=message)
    
@siddhu.command()
async def clean(ctx, time: str, channel: discord.TextChannel = None):
    """Cleans up messages older than the specified time in the channel."""
    if not channel:
        channel = ctx.channel

    # Time format like 1d, 1w, 1m, etc.
    try:
        amount = int(time[:-1])
        unit = time[-1]
        if unit == "d":
            time_limit = datetime.datetime.utcnow() - datetime.timedelta(days=amount)
        elif unit == "w":
            time_limit = datetime.datetime.utcnow() - datetime.timedelta(weeks=amount)
        elif unit == "m":
            time_limit = datetime.datetime.utcnow() - datetime.timedelta(weeks=4*amount)
        else:
            await ctx.send("Invalid time format! Use 'd' for days, 'w' for weeks, 'm' for months.")
            return
    except ValueError:
        await ctx.send("Invalid time format! Example: 1d for one day, 2w for two weeks.")
        return

    # Cleanup
    deleted = await channel.purge(limit=100, before=time_limit)
    await ctx.send(f"Deleted {len(deleted)} message(s) older than {time}.", delete_after=5)
    
tasks = {}

@siddhu.command()
async def tasklist(ctx, action: str, *, task: str = None):
    """Manages your task list: add, remove, view tasks."""
    user_id = str(ctx.author.id)

    if user_id not in tasks:
        tasks[user_id] = []

    if action.lower() == "add" and task:
        tasks[user_id].append(task)
        await ctx.send(f"Task added: {task}")
    elif action.lower() == "remove" and task:
        if task in tasks[user_id]:
            tasks[user_id].remove(task)
            await ctx.send(f"Task removed: {task}")
        else:
            await ctx.send(f"Task not found: {task}")
    elif action.lower() == "view":
        if tasks[user_id]:
            task_list = "\n".join(f"- {t}" for t in tasks[user_id])
            await ctx.send(f"Your tasks:\n{task_list}")
        else:
            await ctx.send("You have no tasks.")
    else:
        await ctx.send("Invalid action! Use 'add', 'remove', or 'view'.")
    
translator = Translator()

@siddhu.command()
async def translate(ctx, *, text: str):
    await ctx.message.delete()
    try:
        detection = translator.detect(text)
        source_language = detection.lang
        source_language_name = LANGUAGES.get(source_language, 'Unknown language')

        translation = translator.translate(text, dest='en')
        translated_text = translation.text

        response_message = (
            f"**Original Text:** {text}\n"
            f"**Detected Language:** {source_language_name} ({source_language})\n"
            f"**Translated Text:** {translated_text}"
        )

        await ctx.send(response_message)
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}MSG TRANSLATED<:Tick:1290693799361777665> ")

    except Exception as e:
        await ctx.send("<:lr_tick_1:1290693800808677461> **Error**: Could not translate text. Please try again later.")
        
@siddhu.command()
async def avatar(ctx, user: discord.Member = None):
    """Fetch and display the avatar of a user or the command author, with embed mode support."""
    user = user or ctx.author  # Default to the command author

    try:
        avatar_url = user.avatar_url

        if not avatar_url:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> {user.name} does not have an avatar.")
            return

        if not embed_mode_enabled:
            # Normal reply
            await ctx.send(f"🖼 **{user.name}'s Avatar:**\n{avatar_url}")
        else:
            # Embed mode
            try:
                await send_custom_embed(
                    ctx,
                    description=f"🖼 **{user.name}'s Avatar**",
                    image=str(avatar_url)
                )
            except Exception as e:
                await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to send avatar embed: `{e}`")

    except Exception as e:
        await ctx.send(f"<:CROSS_TDG:1321149916201881683> An error occurred: `{str(e)}`")

import random
import discord
import os
import uuid
import aiohttp
import asyncio

# Define the delete_after_timeout function for message cleanup
async def delete_after_timeout(message, timeout=500):
    await asyncio.sleep(timeout)
    try:
        await message.delete()
    except discord.errors.NotFound:
        pass

# Enhance imagine command
@siddhu.command(description='Generate an image using AI. Usage: ~imagine "prompt" "style"')
async def imagine(ctx, *, args: str):
    args = args.replace("“", '"').replace("”", '"')

    arguments = args.split('"')

    if len(arguments) < 4:
        await ctx.send(
            'Error: Arguments must be enclosed in quotation marks. For example: `~imagine "the game fortnite" "anime"`'
        )
        return

    prompt = arguments[1]
    style = arguments[3].lower()

    if style not in style_mapping:
        await ctx.send(
            "Invalid style! Styles: `realistic`, `anime`, `disney`, `studio ghibli`, `graffiti`, `medieval`, `fantasy`, `neon`, `cyberpunk`, `landscape`, `japanese`, `steampunk`, `sketch`, `comic book`, `v4 creative`, `imagine v3`, `logo`, `pixel art`, `interior`, `mystical`, `surrealistic`, `minecraft`, `dystopian`."
        )
        return

    ratios = ["RATIO_1X1", "RATIO_4X3", "RATIO_16X9", "RATIO_3X2"]
    ratio = random.choice(ratios)

    style = style_mapping[style]

    temp_message = await ctx.send("Generating image...")

    filename = await generate_image(prompt, style, ratio, None)

    if filename is None:
        await temp_message.edit(content="There was an error generating the image.")
        return

    file = discord.File(filename, filename="image.png")

    await temp_message.delete()

    try:
        await ctx.send(
            content=f"Prompt: `{prompt}` - Style: `{style}`:",
            file=file,
        )
        try:
            os.remove(filename)
        except:
            pass

    except discord.errors.HTTPException:
        error = await ctx.send(
            ":x: | Image was classed as explicit by Discord. Image will be deleted off your PC in 60 seconds."
        )

        await delete_after_timeout(error)
        await asyncio.sleep(60)

        try:
            os.remove(filename)
        except:
            pass

import asyncio

async def delete_after_timeout(message, timeout=500):
    await asyncio.sleep(timeout)
    try:
        await message.delete()
    except discord.errors.NotFound:
        pass  # Ignore if the message is already deleted or not found

@siddhu.command(description="Keeps re-adding someone to a group chat when they leave.")
async def noleave(ctx, user: discord.User = None):
    if user is None:
        await ctx.send(content=":x: | Please specify a user.")
        await delete_after_timeout(ctx.message)
        return

    if user.id in noLeave:
        await ctx.send(content=f"{user.name} is already in the no leave list.")
        await delete_after_timeout(ctx.message)
        return

    noLeave.append(user.id)

    await ctx.send(content=f"Added {user.name} to the no leave list.")
    await delete_after_timeout(ctx.message)


@siddhu.command(description="Removes someone from the no leave list.")
async def allowleave(ctx, user: discord.User = None):
    if user is None:
        await ctx.send(content=":x: | Please specify a user.")
        await delete_after_timeout(ctx.message)
        return

    if user.id not in noLeave:
        await ctx.send(content=f"{user.name} is not in the no leave list.")
        await delete_after_timeout(ctx.message)
        return

    noLeave.remove(user.id)

    await ctx.send(content=f"Removed {user.name} from the no leave list.")
    await delete_after_timeout(ctx.message)
        
@siddhu.command(aliases=["usersbio", "bio"], description="Gets a user's bio.")
async def userbio(ctx, user: discord.User = None):
    await ctx.send(content="Getting user bio...")

    if user is None:
        user = ctx.author

    try:
        bio = await siddhu.http.get_user_profile(user.id)
        bio_content = bio['user'].get('bio', 'No bio set.')  # Default to 'No bio set' if no bio exists
    except Exception as e:
        await ctx.send(content=f":x: | Failed to get user bio. Error: {str(e)}")

        # Log the error
        log_message("error", f"Failed to fetch bio for {user.id}: {str(e)}")

        await delete_after_timeout(ctx.message)
        return

    message = f"""<:discord:1282007043456241717> **{user}'s Bio:**
```{bio_content}
```"""

    await ctx.send(content=message)
    await delete_after_timeout(ctx.message)


@siddhu.command(aliases=["userbanner"], description="Gets a user's banner.")
async def banner(ctx, user: discord.User = None):
    user = user or ctx.author

    try:
        banner_data = await siddhu.http.get_user_profile(user.id)
    except Exception as e:
        await ctx.send(content=f"<:CROSS_TDG:1321149916201881683> Failed to get user banner. Error: `{str(e)}`")
        log_message("error", f"Failed to fetch banner for {user.id}: {str(e)}")
        await delete_after_timeout(ctx.message)
        return

    banner_hash = banner_data['user'].get('banner')
    if not banner_hash:
        await ctx.send(content=":x: | User has no banner.")
        await delete_after_timeout(ctx.message)
        return

    banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_hash}.png?size=600"

    if not embed_mode_enabled:
        # Plain reply
        await ctx.send(f"<:discord:1282007043456241717> **{user}'s Banner:**\n{banner_url}")
    else:
        # Embed mode
        try:
            await send_custom_embed(
                ctx,
                description=f"<:discord:1282007043456241717> **{user}'s Banner**",
                image=banner_url
            )
        except Exception as e:
            await ctx.send(f"<:CROSS_TDG:1321149916201881683> Failed to send banner embed: `{e}`")

    await delete_after_timeout(ctx.message)

@siddhu.command()
async def icon(ctx):
    await ctx.message.delete()
    server_icon_url = ctx.guild.icon_url if ctx.guild.icon else "<:lr_tick_1:1290693800808677461> No server icon"
    await ctx.send(server_icon_url)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} ICON <:Tick:1290693799361777665> ")
    
@siddhu.command()
async def sbanner(ctx):
    """Fetch and display the server banner."""
    guild = ctx.guild  # Get the guild (server) where the command is used
    if guild.banner:  # Check if the server has a banner
        banner_url = str(guild.banner.url)
        await ctx.send(f"🖼 **{guild.name}'s Server Banner:**\n{banner_url}")
    else:
        await ctx.send("<:CROSS_TDG:1321149916201881683> This server does not have a banner.")   

@siddhu.command()
async def get_image(ctx, query):
    await ctx.message.delete()
    params = {
        "query": query,
        'per_page': 1,
        'orientation': 'landscape'
    }
    headers = {
        'Authorization': f'Client-ID F1kSmh4MALfMKjHRxk38dZmPEV0OxsHdzuruBS_Y7to'
    }
    try:
        r = requests.get("https://api.unsplash.com/search/photos", headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        if data['results']:
            image_url = data['results'][0]['urls']['regular']
            await ctx.send(f"Here is your image for `{query}`:\n{image_url}")
            print("Successfully Generated Image")
        else:
            await ctx.send('No images found.')
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
        await ctx.send(f"`Error fetching image: {e}`")

category_messages = {}
active_tasks = {}

@siddhu.command()
async def sc(ctx, category_id: int, *, message: str):
    await ctx.message.delete()
    if ctx.guild is None:
        await ctx.send("This command can only be used in a server.")
        return

    category = discord.utils.get(ctx.guild.categories, id=category_id)
    if category is None:
        await ctx.send("Category not found.")
        return

    if category_id in active_tasks:  # Check if a task exists
        await ctx.send("A message task is already running for this category. Please stop it first using `.stopsc`.")
        return

    category_messages[category_id] = message
    active_tasks[category_id] = True

    await ctx.send(f"**Sending Msg In Ticket Create Category: {category.name}.**")
    print(f"TICKET MSG CATEGORY SET for {category.name}")

message_delays = {}

@siddhu.command()
async def pausesc(ctx, category_id: int):
    await ctx.message.delete()
    if category_id not in active_tasks or not active_tasks[category_id]:
        await ctx.send("No active message task found for this category.")
        return

    active_tasks[category_id] = False
    await ctx.send(f"**Paused Sending Msg In Ticket Create Category Id: {category_id}.**")

@siddhu.command()
async def listsc(ctx):
    await ctx.message.delete()
    if not active_tasks:
        await ctx.send("No active message tasks are running.")
        return

    task_list = []
    for category_id in active_tasks:
        if active_tasks[category_id]:
            category = discord.utils.get(ctx.guild.categories, id=category_id)
            category_name = category.name if category else "Unknown Category"
            task_list.append(f"**Category:** {category_name} (`{category_id}`) - **Message:** {category_messages[category_id]}")

    if task_list:
        await ctx.send("**Active Message Tasks:**\n" + "\n".join(task_list))
    else:
        await ctx.send("No active message tasks are running.")

@siddhu.command()
async def resumesc(ctx, category_id: int):
    await ctx.message.delete()
    if category_id not in category_messages:
        await ctx.send("No message task is set for this category.")
        return
    if active_tasks.get(category_id, False):
        await ctx.send("This message task is already running.")
        return

    active_tasks[category_id] = True
    await ctx.send(f"**Resumed Sending Msg In Ticket Create Category Id: {category_id}.**")

@siddhu.command()
async def clearsc(ctx):
    await ctx.message.delete()
    if not active_tasks:
        await ctx.send("No active message tasks to clear.")
        return

    active_tasks.clear()
    category_messages.clear()
    await ctx.send("**All ticket message tasks have been cleared.**")

@siddhu.command()
async def delaysc(ctx, category_id: int, delay: int):
    await ctx.message.delete()
    if delay < 0:
        await ctx.send("Invalid delay. Please enter a positive number.")
        return

    message_delays[category_id] = delay
    await ctx.send(f"**Message delay set to {delay} seconds for Category Id: {category_id}.**")

@siddhu.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        category_id = channel.category_id
        if category_id in active_tasks and active_tasks[category_id]:
            delay = message_delays.get(category_id, 1)
            await asyncio.sleep(delay)  # Apply delay
            await channel.send(category_messages[category_id])

@siddhu.command()
async def stopsc(ctx, category_id: int):
    await ctx.message.delete()
    if category_id not in active_tasks:
        await ctx.send("No message task is running for this category.")
        return

    del active_tasks[category_id]  # Fix: Remove the category from active_tasks
    del category_messages[category_id]  # Remove the message as well

    await ctx.send(f"**Stopped Sending Msg In Ticket Create Category: {category_id}.**")
    print(f"TICKET MSG CATEGORY REMOVED for {category_id}")

@siddhu.command()
async def editsc(ctx, category_id: int, *, new_message: str):
    await ctx.message.delete()
    if category_id not in active_tasks:
        await ctx.send("No active message task found for this category. Use `.sc` to start a new one.")
        return

    category_messages[category_id] = new_message  # Update the message
    await ctx.send(f"**Updated Message For Ticket Create Category: {category_id}.**")
    print(f"TICKET MSG CATEGORY UPDATED for {category_id}")

@siddhu.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore silently

    elif isinstance(error, commands.MissingRequiredArgument):
        usage = f"Correct usage: `{ctx.prefix}{ctx.command} {ctx.command.signature}`"
        usage = usage.replace("<", "[").replace(">", "]")
        await ctx.send(f"❌ **Missing Argument:** You're missing a required argument.\n\n{usage}")

    elif isinstance(error, commands.BadArgument):
        usage = f"Correct usage: `{ctx.prefix}{ctx.command} {ctx.command.signature}`"
        await ctx.send(f"❌ **Invalid Argument:** That doesn't look right. Check your input.\n\n{usage}")

    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ **No Permission:** You don’t have the required permissions to do this.")

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("❌ **Missing Permissions:** I need more permissions to complete this action.")

    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send("❌ **Not in DM:** You can't use this command in DMs.")

    elif isinstance(error, commands.PrivateMessageOnly):
        await ctx.send("❌ **DM Only:** This command only works in DMs.")

    elif isinstance(error, commands.CheckFailure):
        if str(error) == "This command can only be used in group chats.":
            await ctx.send("❌ **Group Only:** You can only use this command in a group chat.")
        else:
            await ctx.send("❌ **Can't Use Here:** You can't use this command in this context.")

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"⏳ **Cooldown:** Please wait `{error.retry_after:.2f}` seconds before trying again.")

    elif isinstance(error, commands.CommandInvokeError):
        original = error.original
        err_str = str(original).lower()

        # ✅ Suppress harmless message deletion errors
        if isinstance(original, discord.NotFound) and "message" in err_str:
            return

        if isinstance(original, discord.Forbidden):
            await ctx.send("❌ **No Permission:** You don't have permission to use this command here.")
        elif "premium_subscription_count" in err_str or "member_count" in err_str:
            await ctx.send("❌ **Server Only:** You can only use this command in a server.")
        elif "50013" in err_str:
            await ctx.send("❌ **Missing Permissions:** You don’t have the required permissions.")
        elif "50001" in err_str:
            await ctx.send("❌ **Missing Access:** You don’t have access to do that.")
        elif "50035" in err_str:
            await ctx.send("❌ **Invalid Input:** Something's wrong with your input.")
        else:
            await ctx.send(f"⚠️ **Error:** Something went wrong.\n```{original}```")

    elif isinstance(error, discord.HTTPException):
        if error.code == 50013:
            await ctx.send("❌ **Missing Permissions:** You don’t have permission for that.")
        elif error.code == 50001:
            await ctx.send("❌ **Missing Access:** You're missing access for this.")
        elif error.code == 10003:
            await ctx.send("❌ **Error:** I can't find that channel.")
        elif error.code == 10008:
            await ctx.send("❌ **Error:** That message no longer exists.")
        elif error.code == 50007:
            await ctx.send("❌ **DM Blocked:** I can't send you a DM.")
        else:
            await ctx.send(f"⚠️ **API Error:** `{error}`")

    elif isinstance(error, discord.NotFound):
        await ctx.send("❌ **Not Found:** Couldn't find what you were looking for.")

    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send("❌ **Permission Error:** You don’t have permission for that.")

    else:
        await ctx.send(f"⚠️ **Unexpected Error:** `{error}`")
 
siddhu.load_extension("afk")
siddhu.load_extension("antinuke")

import asyncio

async def runner():
    try:
        # This is the proper 1.7.3 way to start without force-closing
        await siddhu.start(token, bot=False)
    finally:
        if not siddhu.is_closed():
            await siddhu.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        # Run until the bot stops
        loop.run_until_complete(runner())
    except KeyboardInterrupt:
        pass
    finally:
        # 100% FIX: Gather ALL tasks and cancel them before closing the loop
        pending = asyncio.all_tasks(loop=loop)
        for task in pending:
            task.cancel()
        
        # Give tasks a moment to finish cancelling
        loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
        loop.close()
