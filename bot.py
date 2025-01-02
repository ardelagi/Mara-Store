import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents and Bot Initialization
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Slash Command Tree
class StoreBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="produk", description="Lihat daftar produk atau detailnya")
    async def produk(self, interaction: discord.Interaction, mode: str):
        if mode == "list":
            await interaction.response.send_message("Daftar produk:\n1. Produk A - Rp100,000\n2. Produk B - Rp200,000")
        elif mode == "detail":
            await interaction.response.send_message("Detail produk: Produk A - Rp100,000\nDeskripsi: Kualitas terbaik!")
        else:
            await interaction.response.send_message("Mode tidak valid. Gunakan 'list' atau 'detail'.")

    @app_commands.command(name="order", description="Pesan produk dari toko")
    async def order(self, interaction: discord.Interaction, produk_id: int, jumlah: int):
        await interaction.response.send_message(f"Pesanan Anda untuk produk {produk_id} sebanyak {jumlah} telah dibuat!")

    @app_commands.command(name="testimoni", description="Berikan atau lihat testimoni")
    async def testimoni(self, interaction: discord.Interaction, mode: str, pesan: str = None):
        if mode == "buat" and pesan:
            await interaction.response.send_message(f"Testimoni Anda telah ditambahkan: '{pesan}'")
        elif mode == "lihat":
            await interaction.response.send_message("Daftar testimoni:\n1. Sangat memuaskan!\n2. Produk sesuai deskripsi.")
        else:
            await interaction.response.send_message("Mode tidak valid. Gunakan 'buat' atau 'lihat'.")

# Register Commands and Run Bot
@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s) to the guild.")
    except Exception as e:
        print(e)

bot.add_cog(StoreBot(bot))
bot.run(TOKEN)
