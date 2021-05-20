from PyDictionary import PyDictionary
from pyrogram import Client, filters


@Client.on_message(
    filters.command(["syn"])
)
async def syno_(bot, message):
    word = message.text
    word = word.split()
    if len(word) < 2:
        await bot.err("Input not found...")
        return
    word = word[1]
    reply = await bot.send_message(message.chat.id, "`Searching for synonyms...`", reply_to_message_id=message.message_id)
    dictionary = PyDictionary()
    words = dictionary.synonym(word)
    output = f"**Synonym for :** __{word}__\n"
    try:
        for a in words:
            output = output + f"◾ __{a}__\n"
        await reply.edit(output)
    except Exception:
        await reply.err(f"Couldn't fetch synonyms of {word}")
 
