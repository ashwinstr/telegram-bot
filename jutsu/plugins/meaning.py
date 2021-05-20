from PyDictionary import PyDictionary
from pyrogram import Client, filters


@Client.on_message(
    filters.command(["mng"])
)
async def meaning_(bot, message):
    msg_split = (message.text).split()
    len_ = len(msg_split)
    if len_ < 2:
        await reply.edit("Input not found...")
        return
    reply = await bot.send_message(message.chat.id, "`Searching for meaning...`", reply_to_message_id=message.message_id)
    word = msg_split[1]
    dictionary = PyDictionary()
    words = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n"
    try:
        for a, b in words.items():
            output = output + f"\n**{a}**\n"
            for i in b:
                output = output + f"◾ __{i}__\n"
        await reply.edit(output)
    except Exception:
        await reply.err(f"Couldn't fetch meaning of {word}")


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


@Client.on_message(
    filters.command(["ayn"])
)
async def syno_(bot, message):
    word = message.text
    word = word.split()
    if len(word) < 2:
        await bot.err("Input not found...")
        return
    word = word[1]
    reply = await bot.send_message(message.chat.id, "`Searching for antonyms...`", reply_to_message_id=message.message_id)
    dictionary = PyDictionary()
    words = dictionary.antonym(word)
    output = f"**Synonym for :** __{word}__\n"
    try:
        for a in words:
            output = output + f"◾ __{a}__\n"
        await reply.edit(output)
    except Exception:
        await reply.err(f"Couldn't fetch synonyms of {word}")
