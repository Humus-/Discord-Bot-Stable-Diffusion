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
pip install -e .
```

TODO tasks:
- Create a docker file
- Add the LLM (currently it doesn't fit in the VRAM, tested on google collab, but not moved here)