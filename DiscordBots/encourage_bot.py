from models import db, ConfigModel, PromptGroupModel, ResponseGroupModel, ResponseModel
import discord
import requests
import json
import random

client = discord.Client()

TOKEN = ''

respondingConfig = ConfigModel.query.filter_by(key='responding').first()
if not (respondingConfig.value is True):
    respondingConfig.value = True
    db.session.commit()


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


# get encouragements function
def get_encouragements():
    # get the encouragements response group
    encouragement_response_group = ResponseGroupModel.query.filter_by(
        name='encouragements').first()

    # get all the encouragement responses
    responses = encouragement_response_group.responses.all()

    # make all the encouragements text
    encouragements = [response.text for response in responses]

    return encouragements


# add a new encouragement
def update_encouragements(encouraging_message):
    # get encoragements response group
    response_group = ResponseGroupModel.query.filter_by(
        name='encouragements').first()

    # create a new response
    new_response = ResponseModel(
        text=encouraging_message, response_group_id=response_group.id)

    # add the response to the database
    db.session.add(new_response)
    db.session.commit()


def delete_encouragements(index):
    # get encouragements response group
    response_group = ResponseGroupModel.query.filter_by(
        name='encoragements').first()

    # find the response with this index
    responses = response_group.responses.all()

    try:
        response = responses[index]
    except IndexError:
        print(f"There is no encouragement at index {index}")
        return

    # delete the response with this index
    db.session.delete(response)
    db.session.commit()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if respondingConfig.value is True:
        options = get_encouragements()

        # get the sad words prompt group
        sad_words_prompt_group = PromptGroupModel.query.filter_by(
            name='sad').first()

        sad_prompts = sad_words_prompt_group.prompts.all()

        # get words out of prompts
        sad_words = [prompt.text for prompt in sad_prompts]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encouraging_message = msg.split("$new", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added")

    if msg.startswith("$del"):
        # delete old encouragement
        index = int(msg.split("$del", 1)[1])
        delete_encouragements(index)

        # get the encouragements
        encouragements = get_encouragements()

        # send the updated encouragements
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = get_encouragements()

        # output all the encouragements as text
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            respondingConfig.value = True
            db.session.commit()
            await message.channel.send("responding is on.")
        else:
            respondingConfig.value = False
            db.session.commit()
            await message.channel.send("Responding is off.")

if __name__ == '__main__':
    client.run(TOKEN)
