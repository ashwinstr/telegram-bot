from PyDictionary import PyDictionary
from pyrogram import Client, filters


@Client.on_message(filters.command(["mng"]))
async def meaning_(bot, message):
    reply = await bot.send_message(message.chat.id, "`Searching for meaning...`", reply_to_message_id=message.message_id)
    msg_split = (message.text).split()
    len_ = len(msg_split)
    if len_ < 2:
        await reply.edit("Input not found...")
        return
    else:
        word = msg_split[1:]
        dictionary = PyDictionary()
        words = dictionary.meaning(word)
        output = f"**Word :** __{word}__\n"
        try:
            for a, b in words.items():
                output = output + f"\n**{a}**\n"
                for i in b:
                    output = output + f"â¾ __{i}__\n"
            await reply.edit(output)
        except Exception:
            await reply.err(f"Couldn't fetch meaning of {word}")
