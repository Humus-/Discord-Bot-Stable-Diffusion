# Discord Bot for Stable Diffusion
A discord bot that responds to text and Image prompts with the help of different LLM models

Developing this on 2 different systems. So will have to add a few more things over the MVP version.

### How it Works

    The bot connects to Discord using the credentials provided in the env file.
    The bot currently hardcodes a specific channel on Discord.
    The bot sends a request to generate an image based on the user's prompt to a separate server.
    The bot waits for the server to send the response and shows a thinking prompt on discord.
    The bot downloads the image and sends it to the channel.

### Steps to run locally:
1. Clone the repo

- Create a .env file with the following information
```
APP_ID=<YOUR_APP_ID>
DISCORD_TOKEN=<YOUR_BOT_TOKEN>
PUBLIC_KEY=<YOUR_PUBLIC_KEY>
```

*In case you enable Chat GPT support add the below key to your .env file*
```
OPENAI_API_KEY=
```

- Install the requirements
```
pip install -r requirements.txt
```
- Go to ai_server folder and run the demo ai server. (Instructions in the readme of that folder)
	Optional if you have a different server. Then you need to change the server address in config.yml
- Once the other services are ready, run
```
python bot.py
```

Now your bot is connected to discord and ready to recieve messages.

### Docker steps
TBD

<!--
Use docker to launch the project.
```
docker compose up
# or run in the daemon mode
docker compose up -d
```
-->

TODO tasks:
- Add the LLM (currently it doesn't fit in the VRAM, tested on google collab, but not moved here)
- Fix logger. (Discord has its own logger?)
- Check cTransformer[cuda] vs Transformer
- Fix TODOs in the code
- Remove the jupyter notebook. It's skewing github stats
- Add a timeout check for bot thinking, in case the model server does not respond back, or there was an error.


<!-- - Rough things for blog aobut this project
-- Why this project. For the memes and dota support while gaming
-- What it can currently do.
-- What I've learnt doing this so far. 
-- Next things I want to try.
-- Stretch goals
-- runpod
-- gcp app
-- code cleanup
-- streamlit? or node?
-- Understanding bit more react while making the blog
- Using A111?
 -->