import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from api import API


bot = Bot(token='7045043434:AAHHLkDCW4mL6u9zlJS10M59haB2yJyHs1s')
dp = Dispatcher()
Api = API('https://147.45.149.141:6269/N0Nxavb2MW7PUwwf5cRJHA')
import urllib3

# Отключение предупреждений TLS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@dp.message(CommandStart())
async def start(msg:Message):
    import db
    db.add_user(msg.from_user.id, msg.from_user.username)
    await msg.answer('🤖~Проект "DOUPIG  VPN" - это бесплатный сервис для <b>поддержания</b> идей <b>"свободного интернета"</b>.\n\n🤖~Наш сервер находится в <b>Европе</b> и использует <b>протокол ShadowSocks</b>\n\n🤖~С помощью бота вы можете, как найти нужный сервер, так и поддержать проект\n\n\n*<b>Получить сервер по комманде /get</b>*', parse_mode=ParseMode.HTML)
@dp.message(Command('get'))
async def get_token(msg:Message):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
    import json
    import db
    
    
    
    btns = [[InlineKeyboardButton(text='android', url='https://play.google.com/store/apps/details?id=org.outline.android.client'),InlineKeyboardButton(text='IOS', url='https://itunes.apple.com/us/app/outline-app/id1356177741') ],
            [InlineKeyboardButton(text='windows', url='https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe'), InlineKeyboardButton(text='MacOs', url='https://itunes.apple.com/us/app/outline-app/id1356178125' )],
            [InlineKeyboardButton(text='linux', url='https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage'), InlineKeyboardButton(text='ChromeOs', url='https://play.google.com/store/apps/details?id=org.outline.android.client')]]
    kbrd = InlineKeyboardMarkup(inline_keyboard=btns)
    await msg.answer(f'Ключ для подключения к <b>Outline</b>: \n<code>{json.loads(db.give_server(msg.from_user.id).text)["accessUrl"]}</code>\n\n <a href="https://telegra.ph/Kak-zapustit-vpn-na-OutLine-DOUPIG-bot-03-28">Инструкция</a>\n\nСкачать Outline с официального сайта~~ *', reply_markup=kbrd, parse_mode='html')

async def main():
    await dp.start_polling(bot)

if '__main__' == __name__:
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('EXIT')
    finally:
        print('DONE')