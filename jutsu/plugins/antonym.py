from PyDictionary import PyDictionary
from pyrogram import Client, filters


@Client.on_cmd(
    "ayn",
)
async def syno_(bot, message):
    word = message.input_str
    if not word:
        await bot.reply("Input not found...")
    reply = await bot.send_message(message.chat.id, "`Searching for antonyms...`", reply_to_message_id=message.message_id)
    dictionary = PyDictionary()
    words = dictionary.antonym(word)
    output = f"**Antonym for :** __{word}__\n"
    try:
        for a in words:
            output = output + f"◾ __{a}__\n"
        await reply.edit(output)
    except Exception:
        await reply.err(f"Couldn't fetch antonym of {word}")
  
