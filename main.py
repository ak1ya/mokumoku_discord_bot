# インストールした discord.py を読み込む
import discord
from discord.ext import tasks
from datetime import datetime

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''
# 投稿したいDiscordチャンネルのIDに置き換えてください
CHANNEL_ID =

# エンベッドの設定
embed = discord.Embed(title="もくもく会開催のお知らせ", description="参加予定の方はスタンプお願いします！", color=0x59E7E7,)
embed.add_field(name="日時",value="明日 09:00 - 11:00 予定")

# 接続に必要なオブジェクトを生成
client = discord.Client()

channel_sent = None

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(embed = embed)

@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
