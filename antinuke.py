import discord
import json
import os
import os, sys, base64, zlib
from discord.ext import commands

CONFIG_FILE = "antinuke.json"

# Ensure the JSON file exists
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        json.dump({}, f)

def load_config():
    """Load the antinuke configuration."""
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    """Save the antinuke configuration."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

class AntiNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()

    def get_server_config(self, guild_id):
        """Ensure the server is in the configuration and return its settings."""
        guild_id = str(guild_id)
        if guild_id not in self.config:
            self.config[guild_id] = {"enabled": False, "logging_channel": None, "whitelist": [], "protections": {}}
            save_config(self.config)
        return self.config[guild_id]

    @commands.command()
    async def antinuke_enable(self, ctx):
        """Enable Anti-Nuke for the server."""
        if isinstance(ctx.channel, discord.DMChannel):
            return await ctx.send("⚠️ This command can only be used in a server.")

        guild_id = str(ctx.guild.id)
        self.config[guild_id] = {"enabled": True, "logging_channel": None, "whitelist": [], "protections": {}}
        save_config(self.config)

        await ctx.send("✅ Anti-Nuke enabled for this server! Configure settings or enable all protections using `.antinuke_all_events`.")

    @commands.command()
    async def antinuke_disable(self, ctx):
        """Disable Anti-Nuke for the server."""
        if isinstance(ctx.channel, discord.DMChannel):
            return await ctx.send("⚠️ This command can only be used in a server.")

        guild_id = str(ctx.guild.id)
        if guild_id in self.config:
            del self.config[guild_id]
            save_config(self.config)

        await ctx.send("❌ Anti-Nuke disabled for this server.")

    @commands.command()
    async def antinuke_all_events(self, ctx):
        """Enable all Anti-Nuke protections."""
        guild_id = str(ctx.guild.id)
        server_config = self.get_server_config(guild_id)

        protections = [
            "anti_ban", "anti_kick", "anti_webhook", "anti_bot",
            "anti_role_create", "anti_role_delete", "anti_role_update",
            "anti_channel_create", "anti_channel_delete", "anti_channel_update",
            "anti_server", "anti_ping", "anti_emoji_create", "anti_emoji_delete",
            "anti_emoji_update", "anti_member_role_update"
        ]

        for p in protections:
            server_config["protections"][p] = True

        save_config(self.config)
        await ctx.send("✅ All Anti-Nuke protections have been enabled.")

    @commands.command()
    async def antinuke_logging(self, ctx, channel: discord.TextChannel):
        """Set a logging channel for Anti-Nuke events."""
        guild_id = str(ctx.guild.id)
        server_config = self.get_server_config(guild_id)

        server_config["logging_channel"] = channel.id
        save_config(self.config)
        await ctx.send(f"✅ Anti-Nuke logs will be sent to {channel.mention}")

    async def toggle_protection(self, ctx, protection, state):
        """Enable/Disable a specific protection."""
        guild_id = str(ctx.guild.id)
        server_config = self.get_server_config(guild_id)

        server_config["protections"][protection] = state
        save_config(self.config)

        status = "✅ Enabled" if state else "❌ Disabled"
        await ctx.send(f"{status} {protection.replace('_', ' ').title()} protection for this server.")

    @commands.command()
    async def anti_ban(self, ctx, state: str):
        """Enable/Disable Anti-Ban protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_ban enable` or `.anti_ban disable`.")
        await self.toggle_protection(ctx, "anti_ban", state.lower() == "enable")

    @commands.command()
    async def anti_kick(self, ctx, state: str):
        """Enable/Disable Anti-Kick protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_kick enable` or `.anti_kick disable`.")
        await self.toggle_protection(ctx, "anti_kick", state.lower() == "enable")

    @commands.command()
    async def anti_webhook(self, ctx, state: str):
        """Enable/Disable Anti-Webhook protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_webhook enable` or `.anti_webhook disable`.")
        await self.toggle_protection(ctx, "anti_webhook", state.lower() == "enable")

    @commands.command()
    async def anti_bot(self, ctx, state: str):
        """Enable/Disable Anti-Bot protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_bot enable` or `.anti_bot disable`.")
        await self.toggle_protection(ctx, "anti_bot", state.lower() == "enable")

    @commands.command()
    async def anti_role_create(self, ctx, state: str):
        """Enable/Disable Anti-Role Creation protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_role_create enable` or `.anti_role_create disable`.")
        await self.toggle_protection(ctx, "anti_role_create", state.lower() == "enable")

    @commands.command()
    async def anti_role_delete(self, ctx, state: str):
        """Enable/Disable Anti-Role Deletion protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_role_delete enable` or `.anti_role_delete disable`.")
        await self.toggle_protection(ctx, "anti_role_delete", state.lower() == "enable")

    @commands.command()
    async def anti_channel_create(self, ctx, state: str):
        """Enable/Disable Anti-Channel Creation protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_channel_create enable` or `.anti_channel_create disable`.")
        await self.toggle_protection(ctx, "anti_channel_create", state.lower() == "enable")

    @commands.command()
    async def anti_channel_delete(self, ctx, state: str):
        """Enable/Disable Anti-Channel Deletion protection."""
        if state.lower() not in ["enable", "disable"]:
            return await ctx.send("⚠️ Usage: `.anti_channel_delete enable` or `.anti_channel_delete disable`.")
        await self.toggle_protection(ctx, "anti_channel_delete", state.lower() == "enable")

def setup(bot):
    bot.add_cog(AntiNuke(bot))