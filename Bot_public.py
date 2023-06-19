import lightbulb
import hikari
import random
bot = lightbulb.BotApp(token='',intents=hikari.Intents.ALL)
@bot.listen()
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
    if not event.is_human:
        return
    else:
        ins = random.randint(1, 50)
        if ins == 1:
            await event.message.respond('Your the reason god created the middle finger!')
        elif ins == 2:
            await event.message.respond('Your secrests are always safe with me. I never even listen when you speak')
        elif ins == 3:
            await event.message.respond('You bring everyoen so much joy when you leave the conversation')
        elif ins == 4:
            await event.message.respond('I may love to shop but I will never buy your bullshit')
        elif ins == 5:
            await event.message.respond("i'd give you a nasty look but youve already got one")
        elif ins == 6:
            await event.message.respond("Somedray you'll go far, i hope you stay there")
        elif ins == 7:
            await event.message.respond("Were you born this stupid or did you take lessons?")
        elif ins == 8:
            await event.message.respond("The people who tolerate you on a daily basis are the real heros")
        elif ins == 9:
            await event.message.respond("You should really come witha warning label")
        elif ins == 10:
            await event.message.respond("I dont know what your problem is, but im guessing its hard to pronounce")
        elif ins == 11:
            await event.message.respond("if i wanted to hear from an asshole, id fart")
        elif ins == 12:
            await event.message.respond("its kind of hilarious watching you try to fit your entire vocabulary into  one sentence")
        elif ins == 13:
            await event.message.respond("You look like something that came out of a slow cooker")
        elif ins == 14:
            await event.message.respond("I will ignore you so hard you will start doubting your existence")
        elif ins == 15:
            await event.message.respond("Feed your own ego, im busy")
        elif ins == 16:
            await event.message.respond('Ill never forget the first time we met, but ill keep trying')
        elif ins == 17:
            await event.message.respond('Your a grey sprinkle on a rainbow cupcake')
        elif ins == 18:
            await event.message.respond('I thought of you today, it reminded me to take out the trash')
        elif ins == 19:
            await event.message.respond('You are so full of shit, the toilet is jealous you know')
        elif ins == 20:
            await event.message.respond('stupidity isnt a crime, so your free to go')
        elif ins == 21:
            await event.message.respond('I love what youve done with your hair, how do you get it to come out of your nostrils like that')
        elif ins == 22:
            await event.message.respond('ive been called worse by better')
        elif ins == 23:
            await event.message.respond('dont you get tired of putting makeup on your two faces every morning')
        elif ins == 24:
            await event.message.respond('Too bad you cant photoshop your ugly personality')
        elif ins == 25:
            await event.message.respond('do your parents even realize there living proof that to wrongs dont make a right?')
        elif ins == 26:
            await event.message.respond('jesus might love you but but everyone else definitely thinks your an itdiot')
        elif ins == 27:
            await event.message.respond('Please just tell me you dont have plans to homeschool your kids')
        elif ins == 28:
            await event.message.respond('you see other voice channel? i want you on the in it')
        elif ins == 29:
            await event.message.respond('Your like the end pieces of a loaf of break, everyone touches you but nobody wants you')
        elif ins == 30:
            await event.message.respond('if your going to act like a turn go lay on the yard')
        elif ins == 31:
            await event.message.respond('you are more dissapointing than an unsalted pretzel')
        elif ins == 32:
            await event.message.respond('your face makes onions cry')
        elif ins == 33:
            await event.message.respond('dont worry about me, worry about you (facial feature)')
        elif ins == 34:
            await event.message.respond('oops my bad, couldve sworn i was talking to a mature person')
        elif ins == 35:
            await event.message.respond('if laughet is the best medicine, your face must be curing the world')
        elif ins == 36:
            await event.message.respond('your not stupid you just have bad luck when your thinking')
        elif ins == 37:
            await event.message.respond('isnt there a bullet somewhere you could be jumping infront of?')
        elif ins == 38:
            await event.message.respond('id slap you but i dont want to make your face look any better')
        elif ins == 39:
            await event.message.respond('have a nice day, somewhere else')
        elif ins == 40:
            await event.message.respond('everyones entitled to act stupid once in a while, but you abuse the privilege')
        elif ins == 41:
            await event.message.respond('if ignorance is bliss you must be the happiest person on the planet')
        elif ins == 42:
            await event.message.respond('your ffamily tree must be a cactus, cause your all a bunch of pricks')
        elif ins == 43:
            await event.message.respond('if i threw a stick, youd leave right?')
        elif ins == 44:
            await event.message.respond('somewehre out there theres a tree working very hard to produce oxygen so that you can breath, i recommend apologizing to it')
        elif ins == 45:
            await event.message.respond('you look like a "before" picture')
        elif ins == 46:
            await event.message.respond('light travels faster then sound, which is why you seemed bright before you spoke')
        elif ins == 47:
            await event.message.respond('hold still im trying to imagine you with personality')
        elif ins == 48:
            await event.message.respond('dont get bitter just get better')
        elif ins == 49:
            await event.message.respond('what dosent kill you, dissapoints me')
        else:
            await event.message.respond('calling you an idiot would be an insult to all stupid people')
bot.run()