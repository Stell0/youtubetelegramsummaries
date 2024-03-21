# YouTube to Telegram Summaries

- Check for new videos from a list of YouTube channels

- When a new video is published, take the transcript and summarize it

- Send the summary to a Telegram channel

Needs an OpenAI api key to make the summary

```
export OPENAI_API_KEY=xx-xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
```

If a Telegram TELEGRAM_CHAT_ID and TELEGRAM_BOT_TOKEN environment variables are provided, summaries are also sent to the Telegram chat

## Telegram (optional):
```
TELEGRAM_CHAT_ID=-123456789
TELEGRAM_BOT_TOKEN=1234567890:XXX-XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
```

## Launch:

```
python3 src/main.py
```

## How to setup your github action bot:

- fork this repository
- add into your https://github.com/YOUR_USERNAME/youtubetelegramsummaries/settings/secrets/actions the following variables:
`DOCKERHUB_USERNAME`: your [dockerhub](https://hub.docker.com/) username
`DOCKERHUB_TOKEN`: dockerhub read/write access token https://hub.docker.com/settings/security
`TELEGRAM_CHAT_ID`: the [ID of the telegram chat](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id) you whant your message to be sent
`TELEGRAM_BOT_TOKEN`: a telegram bot [token](https://core.telegram.org/bots/features#botfather)
`OPENAI_API_KEY`: OpenAI API key
- change all "stell0" occurrence in .github/workflows/*.yml with your username