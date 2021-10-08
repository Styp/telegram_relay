import os

from telethon import TelegramClient, events
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

api_id = ""
api_hash = ""
src_channel_name = ""
dst_channel_name = ""

print("Connecting to Telegram...")
client = TelegramClient('telegram_relay', api_id, api_hash)


@client.on(events.NewMessage)
async def incoming_event(event):
    message = await event.get_chat()
    if message.id == src_channel_id:
        await client.send_message(dst_channel_id, event.message)

client.start()
src_channel_id = client.get_entity(src_channel_name).id
print("Source Channel ID: {}".format(src_channel_id))
dst_channel_id = client.get_entity(dst_channel_name).id
print("Destination Channel ID: {}".format(dst_channel_id))

client.run_until_disconnected()