#!/usr/bin/env python3
import time
import asyncio
import sys

import os, re, random, json
from telethon import TelegramClient, events, utils

api_id = 6249347
api_hash = 'cb0e4582f5aeec80c69ff30b6275605f'
sesi_file = 'coll1stellos'
dest= ("chtwrsbot","PercetakanMie", "AttackerPro","SecretOrder")
chat = 'BotOrder1411'
    
with TelegramClient(sesi_file, api_id, api_hash) as client:
 @client.on(events.NewMessage(incoming=True, from_users=dest[1]))
 async def handle_chat(event):
  if "/g_withdraw" in event.raw_text:
   await client.forward_messages(408101137, event.message)
   time.sleep(1)
   print(time.asctime(),'withdraw')
 @client.on(events.NewMessage( from_users=dest[0]))
 async def handle_chat(event):
  if "Recipient" in event.raw_text:
   await client.forward_messages(1560253778, event.message)
   time.sleep(2)
  return
               
 @client.on(events.NewMessage(incoming=True, from_users=dest[2]))
 async def handle_chat(event):
  if "Quest" in event.raw_text:
   await client.send_message(dest[0], "🗺Quests")
  time.sleep(1)
  
@client.on(events.NewMessage( from_users=dest[0]))
async def handle_chat(event):
 if "Many things can happen in the forest." in event.raw_text:
  await event.click(text="🍄Swamp")
 time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
  if "Mie dice" in event.raw_text:
   await client.send_message(dest[0], "🎲Play some dice")
  time.sleep(1)
  
@client.on(events.NewMessage(incoming=True, from_users=dest[0]))
async def handle_chat(event):
  if "he takes" in event.raw_text:
   await client.send_message(dest[0], '🎲Play some dice')
  time.sleep(1)
  print(time.asctime(),'coll 1 dice')
  return
  return
  

@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "moon" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🌑")
  time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "ptt" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🥔")
  time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "wolf" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🐺")
  time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "drag" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🐉")
  time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "hn" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🦅")
 time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "deer" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🦌")
  time.sleep(1)
 return
  
@client.on(events.NewMessage(incoming=True, from_users=dest[2]))
async def handle_chat(event):
 if "shark" in event.raw_text:
  await client.send_message(dest[0], "⚔Attack")
  time.sleep(2)
  await client.send_message(dest[0], "🦈")
  time.sleep(1)
 return

client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')