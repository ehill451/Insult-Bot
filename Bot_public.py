import lightbulb
import hikari
import random
import json

with open("config.json", "r") as file:
    config = json.load(file)
    print("loaded config")

bot = lightbulb.BotApp(token=config["token"],intents=hikari.Intents.ALL)
@bot.listen()
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
    if not event.is_human:
        return
    else:
        rand = random.choice(config["insults"])
        await event.message.respond(rand)

if __name__ == "__main__":
    bot.run()