# Imports
import discord
from datetime import datetime
import os
from Statdata.cmdlst import cmdlst

# Setup
TOKEN = "MTAwNDM1OTQ4NzY1NTc4NDQ4OQ.GqxxJB.UlAPupLtDL6wSyK72vtFMBBVAXF0cSaTTqzTT0"
client = discord.Client()

# Functions
def get_now():
    return datetime.now().strftime("%d/%m/%Y-%H:%M:%S ")
def get_valid(ctx):
    return True if ctx.content.lower().split(" ")[0] == "dp" and str(ctx.channel.name) == "daiquiri-oversikt" else False
def get_ctx(ctx):
    user = [None, None, None, None, None]
    try:
        user[0] = ctx.content.lower().split(" ")[1]
    except IndexError:
        return False
    else:
        try:
            user[1] = ctx.content.lower().split(" ")[2]
        except IndexError:
            user[1] = None
        try:
            user[2] = ctx.content.lower().split(" ")[3]
        except IndexError:
            user[2] = None
        try:
            user[3] = ctx.content.lower().split(" ")[4]
        except IndexError:
            user[3] = None
        try:
            user[4] = ctx.content.lower().split(" ")[5]
        except IndexError:
            user[4] = None
        return [i for i in user if i]


# Startup
@client.event
async def on_ready():
    with open("logs/startups", "a") as file:
        file.write(get_now().strip(" ") + "\n")
    print(get_now() + "Ready")

# Messageevent
@client.event
async def on_message(ctx):
    # Set cmd-info
    if get_valid(ctx):
        try:
            cmd = get_ctx(ctx)
        except cmd == False:
            return
        else:

            # Help
            if cmd[0] == cmdlst[0][0]:
                response ="```"
                for i in cmdlst:
                    response += i[1] + "\n"
                await ctx.channel.send(response + "```")
                return
            
            # AddUser
            elif cmd[0] == cmdlst[1][0]:
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    await ctx.channel.send(cmd[1] + " Er allerede registrert. Fuck off.")
                    return
                else:
                    with open("users/" + cmd[1].strip("<@>"), "a") as f:
                        await ctx.channel.send(cmd[1] + " Er nå registrert. Fittetryne.")
                        return

            # RemoveUser
            elif cmd[0] == cmdlst[2][0]:
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    os.remove("users/" + cmd[1].strip("<@>"))
                    await ctx.channel.send(cmd[1] + " Er nå fjernet. Anuslukt.")
                    return
                else:
                    await ctx.channel.send(cmd[1] + " Har ikke bruker. Klovn.")
                    return

            # SB
            elif cmd[0] == cmdlst[3][0]:
                user = await client.fetch_user(340228922300039169)
                response = "```\n"
                for filename in os.listdir("users/"):
                    num = 0
                    with open("users/" + filename, "r") as file:
                        for line in file.readlines():
                            num += int(line.split(" ")[1])
                    response += str(await client.fetch_user(int(filename))).split("#")[0] + ": " + str(num) + "\n"
                await ctx.channel.send(response + "```")

            # Log
            elif cmd[0] == cmdlst[4][0]:
                scoreboard = ""
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for f in file.readlines():
                            scoreboard += str(f)
                    await ctx.channel.send("```\n" + scoreboard + "\nHestkuk.```")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Vaginasopp.")

            # Add
            elif cmd[0] == cmdlst[5][0]:
                response = 0
                num = +abs(int(cmd[2]))
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    # legg til DP
                    with open("users/" + cmd[1].strip("<@>"), "a") as file:
                        file.write(get_now() + str(num) + " " + cmd[0] + "\n")
                    # Se antall DP
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for line in file.readlines():
                            response += int(line.split(" ")[1])
                    await ctx.channel.send(cmd[1] + " Har nå " + str(response) + " Daiquiri Points! Jeg driter i horemora di.")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Mongotryne.")

            # Remove
            elif cmd[0] == cmdlst[6][0]:
                response = 0
                x = 0
                num = -abs(int(cmd[2]))
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    # Se antall DP
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for line in file.readlines():
                            x += int(line.split(" ")[1])
                    if x > int(cmd[2]):
                        # legg til DP
                        with open("users/" + cmd[1].strip("<@>"), "a") as file:
                            file.write(get_now() + str(num) + " " + cmd[0] + "\n")
                        # Se antall DP
                        with open("users/" + cmd[1].strip("<@>"), "r") as file:
                            for line in file.readlines():
                                response += int(line.split(" ")[1])
                        await ctx.channel.send(cmd[1] + " Har nå " + str(response) + " Daiquiri Points! Sug smør fra rumpa mi.")
                    else:
                        await ctx.channel.send(cmd[1] + " Har da for faen ikke så mange engang? Kuksopp.")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Morrapuler.")

            # NSR
            elif cmd[0] == cmdlst[7][0]:
                response = 0
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    # legg til DP
                    with open("users/" + cmd[1].strip("<@>"), "a") as file:
                        file.write(get_now() + str(cmd[2]) + " " + cmd[0] + "\n")
                    # Se antall DP
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for line in file.readlines():
                            response += int(line.split(" ")[1])
                    await ctx.channel.send(cmd[1] + " Har nå " + str(response) + " Daiquiri Points! La en sulten karpatisk langhåret hunnulv suge pikken din, faen.")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Retard.")

            # DNF
            elif cmd[0] == cmdlst[8][0]:
                response = 0
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    # legg til DP
                    with open("users/" + cmd[1].strip("<@>"), "a") as file:
                        file.write(get_now() + str(2) + " " + cmd[0] + "\n")
                    # Se antall DP
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for line in file.readlines():
                            response += int(line.split(" ")[1])
                    await ctx.channel.send(cmd[1] + " Har nå " + str(response) + " Daiquiri Points! Jeg skal lage vårrull av forhuden din.")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Daniel Kjeldsen.")

            # DNS
            elif cmd[0] == cmdlst[9][0]:
                response = 0
                if os.path.exists("users/" + cmd[1].strip("<@>")):
                    # legg til DP
                    with open("users/" + cmd[1].strip("<@>"), "a") as file:
                        file.write(get_now() + str(2) + " " + cmd[0] + "\n")
                    # Se antall DP
                    with open("users/" + cmd[1].strip("<@>"), "r") as file:
                        for line in file.readlines():
                            response += int(line.split(" ")[1])
                    await ctx.channel.send(cmd[1] + " Har nå " + str(response) + " Daiquiri Points! Putt hånda opp i rumpa mi og onaner bæsjen min.")
                else:
                    await ctx.channel.send(cmd[1] + " har ikke bruker. Fag.")

# Run
client.run(TOKEN)