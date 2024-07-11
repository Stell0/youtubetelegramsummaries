# YouTube to Telegram Summaries

This program use github actions to check every hour if there are new videos in a list of youtube channels, than if there is a new one, uses LangChain (OpenAI model) to summarize the content of the video and send the summary to a telegram group.

It only works with english at the moment.


TL;DR:
- Check for new videos from a list of YouTube channels 

- When a new video is published, take the transcript and summarize it

- Send the summary to a Telegram group

## Launch on a single video
```
docker run -e OPENAI_API_KEY=xx-xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX -e LANGUAGE=en docker.io/stell0/youtubetelegramsummaries python3 src/main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Launch using docker

Export variables
```
export OPENAI_API_KEY=xx-xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
export TELEGRAM_CHAT_ID=-123456789
export TELEGRAM_BOT_TOKEN=1234567890:XXX-XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
export CHANNEL_LIST=https://www.youtube.com/@allin https://www.youtube.com/@lexfridman https://www.youtube.com/@hubermanlab"
```

And launch
```
docker run -e TELEGRAM_CHAT_ID -e TELEGRAM_BOT_TOKEN -e OPENAI_API_KEY -e CHANNEL_LIST stell0/youtubetelegramsummaries:latest
```


## Launch manually

Clone repo
```
git clone git@github.com:Stell0/youtubetelegramsummaries.git
cd youtubetelegramsummaries
```

Install requirements
```
pip install -r requirements.txt
```

Export variables
```
export OPENAI_API_KEY=xx-xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
export TELEGRAM_CHAT_ID=-123456789
export TELEGRAM_BOT_TOKEN=1234567890:XXX-XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
export CHANNEL_LIST=https://www.youtube.com/@allin https://www.youtube.com/@hubermanlab https://www.youtube.com/@JosephCarlsonShow"
```

And launch
```
python3 src/main.py
```

You can also specify the video url if you want to process only one
```
python3 src/main.py https://www.youtube.com/watch?v=3tEcLAud7Nc
```



## Launch every hour using GitHub Actions:

- fork this repository

> **_NOTE:_**  go to the Actions tab and enable the scheduled workflows because they are disabled for the forked repositories.

- add into your [action secrets](https://github.com/YOUR_USERNAME/youtubetelegramsummaries/settings/secrets/actions)
 the following variables:

`TELEGRAM_CHAT_ID`: the [ID of the telegram chat](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id) you whant your message to be sent

`TELEGRAM_BOT_TOKEN`: a telegram bot [token](https://core.telegram.org/bots/features#botfather)

`OPENAI_API_KEY`: your OpenAI API key

- Then add in your [action variables](https://github.com/YOUR_USERNAME/youtubetelegramsummaries/settings/variables/actions)the variable with the list of channels

`CHANNEL_LIST`: list of youtube channels, for instance:
```
https://www.youtube.com/@allin
https://www.youtube.com/@lexfridman
https://www.youtube.com/@hubermanlab
```

`LANGUAGE`: transcription language to use. Default "en" 

then wait ⏱️ (cron is launched every hour and take videos published during the previous hour)

