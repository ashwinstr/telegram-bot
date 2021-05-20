import PyDictionary
from pyrogram import Client, filters

@Client.on_message(filters.command(["mng"]))
async def meaning_(bot, message):
    await message.edit("`Searching for meaning...`")
    word = message.input_str or message.reply_to_message.text
    if not word:
        await message.err("no input!")
    else:
        dictionary = PyDictionary()
        words = dictionary.meaning(word)
        output = f"**Word :** __{word}__\n"
        try:
            for a, b in words.items():
                output = output + f"\n**{a}**\n"
                for i in b:
                    output = output + f"â¾ __{i}__\n"
            await message.edit(output)
        except Exception:
            await message.err(f"Couldn't fetch meaning of {word}")
