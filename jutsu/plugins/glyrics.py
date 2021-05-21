import lyricsgenius

import os
import aiohttp
import requests

from bs4 import BeautifulSoup
from googlesearch import search

from jutsu.helpers.telegraph import post_to_telegraph as pt

from pyrogram import Client, filters


GENIUS = os.environ.get("GENIUS")


if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@Client.on_message(
    filters.command(["glyrics"])
)
async def g_lyrics(bot, message):
    input = message.text
    input = input.split()
    if len(input) < 2:
        await bot.send_message(message.chat.id, "Input not found...", reply_to_message_id=message.message_id)
        return
    song = " ".join(input[1:])
    if GENIUS is None:
        await bot.send_message(message.chat.id, "Provide 'genius api token' as <code>GENIUS</code> in config...")
        return
   
    to_search = song + "genius lyrics"
    gen_surl = list(search(to_search, num=1, stop=1))[0]
    gen_page = requests.get(gen_surl)
    scp = BeautifulSoup(gen_page.text, "html.parser")
    writers_box = [
        writer
        for writer in scp.find_all("span", {"class": "metadata_unit-label"})
        if writer.text == "Written By"
    ]
    if writers_box:
        target_node = writers_box[0].find_next_sibling(
            "span", {"class": "metadata_unit-info"}
        )
        writers = target_node.text.strip()
    else:
        writers = "Couldn't find writers..."

    artist = ""
    if " - " in song:
        artist, song = song.split("-", 1)
        artist = artist.strip()
        name_a = artist.split()
        artist_a = []
        for a in name_a:
            a = a.capitalize()
            artist_a.append(a)
        artist = " ".join(artist_a)
    song = song.strip()
    name_s = song.split()
    song_s = []
    for s in name_s:
        s = s.capitalize()
        song_s.append(s)
    song = " ".join(song_s)
    if artist == "":
        title = song
    else:
        title = f"{artist} - {song}"
    reply = await bot.send_message(
        message.chat.id,
        f"Searching lyrics for **{title}** on Genius...`",
        reply_to_message_id=message.message_id,
    )
    try:
        lyr = genius.search_song(song, artist)
    except Exception:
        await reply.edit(f"Lyrics for <code>{title}</code> not found...")
        return
    lyric = lyr.lyrics
    lyrics = f"\n{lyric}"
    lyrics += f"\n\n<b>Written by:</b> <code>{writers}</code>"
    lyrics += f"\n<b>Source:</b> <code>genius.com</code>"
    lyrics = lyrics.replace("[", "<b>[")
    lyrics = lyrics.replace("]", "]</b>")
    lyr_msg = f"Lyrics for <b>{title}</b>...\n\n{lyrics}"
    if len(lyr_msg) <= 4096:
        await reply.edit(f"{lyr_msg}")
    else:
        lyrics = lyrics.replace("\n", "<br>")
        link = pt(f"Lyrics for {title}...", lyrics)
        await reply.edit(
            f"Lyrics for [<b>{title}</b>]({link}) by genius.com...",
        )
