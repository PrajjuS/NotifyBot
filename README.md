# Notify Bot
A simple Telegram Bot written in [Python](https://www.python.org) using [Pyrogram](https://docs.pyrogram.org) to notify Security Patch updates and Fingerprint updates in telegram groups.

## Instructions
- This bot is for all the lazy people who are in too many groups and are lazy to check [AOSP Tracker](https://t.me/aosptracker) and [Android Dumps](https://t.me/android_dumps) groups everytime for updates.
- Since bot uses messages from [AOSP Tracker](https://t.me/aosptracker) and [Android Dumps](https://t.me/android_dumps) groups to notify, so it is necessary for the owner to join both groups before deploying the bot.

## Deploying the Bot
### 1. Deploying on Heroku
The easiest way to host this bot is on <a href="https://heroku.com">Heroku</a>. Tap on the below button to deploy the bot to heroku.  

[![Deploy to Heroku](https://img.shields.io/badge/Deploy%20to%20Heroku-blueviolet?style=for-the-badge&logo=heroku)](https://heroku.com/deploy?template=https://github.com/PrajjuS/NotifyBot/tree/main)

### 2. Deploying Locally    
#### 1. Installing requirements
- Clone this repo:
```
git clone https://github.com/PrajjuS/NotifyBot NotifyBot && cd NotifyBot
```   
- For Debian based distros  
```
sudo apt install python3 python3-pip
```
- For Arch and it's derivatives:
```
sudo pacman -S python
```
- Install dependencies for running setup scripts:
```
pip3 install -r requirements.txt
```
#### 2. Setting up config file
```
cp sample_config.env config.env
```
Fill up the config fields. Meaning of each field is discussed below:
- `API_ID`: Telegram API ID. Get this value from [Here](my.telegram.org)
- `API_HASH`: Telegram API HASH. Get this value from [Here](my.telegram.org)
- `TG_SESSION`: Pyrogram STRING SESSION. Get this value from [Here](https://t.me/genStr_Bot)
- `BOT_TOKEN`: Telegram BOT TOKEN. Get this value from [Here](https://t.me/botfather)
- `CHAT_ID`: A space separated list of chat IDs where you want to get notified
- `ENABLE_TAG`: Set this to True if you want all the admins of the group to be tagged after getting notified
#### 3. Running the bot
```
python3 -m NotifyBot
```
