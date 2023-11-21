# Discord Bot for Stable Diffusion
Create a discord bot that takes a user prompt and uses a text to Image model to send back an image

Developing this on 2 different systems. So will have to add a few more things over the MVP version.

Steps:
- Clone the repo
- Create a .env file with the following information
```
APP_ID=<YOUR_APP_ID>
DISCORD_TOKEN=<YOUR_BOT_TOKEN>
PUBLIC_KEY=<YOUR_PUBLIC_KEY>
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

TODO tasks:
- Create a docker file
- Add the LLM (currently it doesn't fit in the VRAM, tested on google collab, but not moved here)
- Fix logger. (Discord has its own logger?)
- Check cTransformer[cuda] vs Transformer
- Fix TODOs in the code
- Remove the jupyter notebook. It's skewing github stats
