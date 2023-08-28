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
  await sendMessageToAdmins(data)
  return web.Response(status=200)


async def sendMessageToAdmins(data: dict):
  for admin in admins:
    try:
      notification_text = 'Notification!'

      if 'service' in data:
        notification_text += f' From: {data["service"]}'

      notification_text += '\n'

      for key, value in d.items():
        notification_text += f'{key}: {value} \n'
      await bot.send_message(admin, text=notification_text)
    except Exception as e:
      print(e)

if __name__ == '__main__':
  app = web.Application()
  app.add_routes(routes)
  web.run_app(app, port=80)
