import discord
from discord.ext import commands
import re


def process_avatar(url):
    if ".gif" in url:
        new_url = re.sub("\?size\=\d+$", "", url)
        return new_url
    else:
        new_url = url.replace('.webp', '.png')
        return new_url


class Avatar:
    """Get user's avatar."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar."""
        author = ctx.message.author

        if not user:
            user = author

        u = user.avatar_url
        url = process_avatar(u)
        em = discord.Embed()
        em.set_author(name=user.name, url=url, icon_url=url)
        em.set_image(url=url)
        em.set_footer(text="Do you wish more?")
        await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(Avatar(bot))
