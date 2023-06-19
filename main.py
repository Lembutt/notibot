import os
import asyncio
from aiogram import Bot
from aiohttp import web

routes = web.RouteTableDef()

def getAdmins():
  admins = os.getenv('NOTIBOT_ADMINS')
  if admins:
    return admins.split(':')
  return []

admins = getAdmins()
token = os.getenv('NOTIBOT_TOKEN')
bot = Bot(token=token)

@routes.post('/notifyAdmins')
async def notifyAdmins(request):
  data = await request.json()
  await sendMessageToAdmins(data['name'], data['email'], data['phone'])
  return web.Response(status=200)


async def sendMessageToAdmins(name, email, phone):
  for admin in admins:
    try:
      await bot.send_message(admin, text=f'Новая заявка по квасу!\n\nИмя: {name}\nEmail: {email}\nТелефон: {phone}')
    except Exception as e:
      print(e)

if __name__ == '__main__':
  app = web.Application()
  app.add_routes(routes)
  web.run_app(app, port=80)