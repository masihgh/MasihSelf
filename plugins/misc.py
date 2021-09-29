from pyrogram import Client
from pyrogram import client
from pyrogram.client import Client
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters


@Client.on_message(filters.command('delall') & filters.me)
async def delall(client: Client, message: Message):
    if len(message.command) == 2:
        chat = message.command[1]
        if chat[1:].isdigit():
            chat = int(chat)
    elif message.chat.type in ['supergroup', 'group']:
        chat = message.chat.id
    client.delete_user_history(chat, "me")
