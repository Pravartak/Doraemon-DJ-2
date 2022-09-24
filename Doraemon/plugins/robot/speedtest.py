import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from Doraemon import app
from Doraemon.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**↓ ᖇᑌᑎᑎIᑎᘜ ᗪOᗯᑎᒪOᗩᗪ ՏᑭᗴᗴᗪTᗴՏT...**")
        test.download()
        m = m.edit("**↑ ᖇᑌᑎᑎIᑎᘜ ᑌᑭᒪOᗩᗪ ՏᑭᗴᗴᗪTᗴՏT...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 TᖇYIᑎᘜ TO ᑕᕼᗴᑕK ᑌᑭᒪOᗩᗪ ᗩᑎᗪ ᗪOᗯᑎᒪOᗩᗪ Տᑭᗴᗴᗪ...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **ՏᑭᗴᗴᗪTᗴՏT ᖇᗴՏᑌᒪTՏ** ✯
    
<u>**ᑕᒪIᗴᑎT :**</u>
**» __IՏᑭ :__** {result['client']['isp']}
**» __ᑕOᑌᑎTᖇY :__** {result['client']['country']}
  
<u>**Տᗴᖇᐯᗴᖇ :**</u>
**» __ᑎᗩᗰᗴ :__** {result['server']['name']}
**» __ᑕOᑌᑎTᖇY :__** {result['server']['country']}, {result['server']['cc']}
**» __ՏᑭOᑎՏOᖇ :__** {result['server']['sponsor']}
**» __ᒪᗩTᗴᑎᑕY :__** {result['server']['latency']}  
**» __ᑭIᑎᘜ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
