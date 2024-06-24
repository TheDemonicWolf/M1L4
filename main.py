import discord
from bot_logic import gen_pass
from bot_logic2 import gen_advice
from bot_logic3 import gen_smile

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$привет'):
        await message.channel.send("Приветствую!")
    elif message.content.startswith('$пока'):
        await message.channel.send("До свидания!")
    elif message.content.startswith('$пароль'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$совет'):
        await message.channel.send(gen_advice())
    elif message.content.startswith('$калькулятор'):
        command_parts = message.content.split(' ')
        if len(command_parts) == 4:
            try:
                first = int(command_parts[1])
                action = command_parts[2]
                second = int(command_parts[3])

                if action == "+":
                    await message.channel.send(first + second)
                elif action == "-":
                    await message.channel.send(first - second)
                elif action == "*":
                    await message.channel.send(first * second)
                elif action == "/":
                    await message.channel.send(first / second)
                else:
                    await message.channel.send("Не допустимая операция")
            except ValueError:
                await message.channel.send("Неверный формат чисел")
        else:
            await message.channel.send("Неверный формат команды")
    else:
        await message.channel.send(gen_smile())
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
client.run("")
