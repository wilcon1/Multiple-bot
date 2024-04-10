import nextcord
from nextcord.ext  import commands
from nextcord import Interaction,slash_command

class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="welcome", description="welcomer with persons at server")
    @commands.has_any_role("Moderator","Administrator","Owner")
    async def welcome(self, interaction: nextcord.Interaction, member: nextcord.Member):
        welcome_message = f"Welcome {member.mention} to our server!"
        await interaction.response.send_message(welcome_message)

   
    @nextcord.slash_command(name="clear", description="cleared messages you want")
    async def clear(self, interaction: nextcord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"Cleared {amount} messages.👌")

    @nextcord.slash_command(name="ban", description="banned members you want")
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"Banned {member.name}#{member.discriminator} with reason: {reason}")

    @nextcord.slash_command(name="kick", description="kicked members you want")
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"Kicked {member.name}#{member.discriminator} with reason: {reason}")

    @nextcord.slash_command(name="suggest", description="suggestion you want to say")
    async def suggest(self,interaction: Interaction, suggestion: str):          
     embed = nextcord.Embed(title=interaction.user.name, description=suggestion)     
     embed.set_thumbnail(url=interaction.user.display_avatar.url)     
     embed.set_footer(text=f"sent by {interaction.user.name}#{interaction.user.discriminator} {interaction.guild.id}")    
     await interaction.response.send_message(embed=embed)
     message = await interaction.original_message()
     await message.add_reaction("✔")
     await message.add_reaction("❌")
 
    @nextcord.slash_command(name="embed", description="make embed")
    async def embed(self,interaction: Interaction, title: str, description: str):
       emb = nextcord.Embed(
        title=title,
        description=description,
        color=0x5865F2
    )
       emb.set_thumbnail(url=interaction.user.display_avatar.url)
       emb.set_footer(text=f"sent by {interaction.user.name} ", icon_url=interaction.user.display_avatar)
       await interaction.response.send_message(embed=emb)

    @nextcord.slash_command(name="help",description="list of cammands in bot")
    async def help(self,interacrion:Interaction):
      embed = nextcord.Embed(
         title="Help",
         description="this is commands that you can use it at server",
         color=nextcord.Color.dark_gold()
      )
      embed.add_field(name="welcom",value="welcomer with persons at server")
      embed.add_field(name="clear",value="cleared messages you want")
      embed.add_field(name="ban",value="banned members you want")
      embed.add_field(name="kick",value="kicked members you want")
      embed.add_field(name="suggest",value="suggestion you want to say")
      embed.add_field(name="embed",value="make embed")
      embed.add_field(name="help",value="to see the list of cammands that you can use")
      embed.add_field(name="giveaway",value="make giveaways to members")
      embed.add_field(name="ticket",value="make tickets ")
      await interacrion.response.send_message(embed=embed)















def setup(bot):
    bot.add_cog(test2(bot))
