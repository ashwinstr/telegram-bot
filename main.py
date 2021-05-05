from pyrogram import Client, filters

app = Client(
    "sharingan_analysis",
    api_id=secrets.API_ID,
    api_hash=secrets.API_HASH,
    bot_token=secrets.BOT_TOKEN,
)

@app.on_message(
    filters.command(["start"])
)
async def start_(client, message):
    await client.send_message(
        message.chat.id,
        f"Hello {message.from_user.first_name}, thank you for using this bot...",
    )
