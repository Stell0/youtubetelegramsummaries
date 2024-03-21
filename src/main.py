import telegram_alert
from pytube import YouTube
import scrapetube



def main():
	# load channels
	with open('config/channels.txt', 'r') as file:
		channels = [line.strip() for line in file if line.strip()]
	
	for channel in channels:
		try:
			videos = scrapetube.get_channel(channel_url=channel,limit=1)

			for video in videos:
				if not 'minutes ago' in video['publishedTimeText']['simpleText'] or int(video['publishedTimeText']['simpleText'].split(' ')[0]) > 60:
					print (f"Skipping \"{video['title']['runs'][0]['text']}\" as it is too old: {video['publishedTimeText']['simpleText']}")
					continue
				video = YouTube('http://youtube.com/watch?v=' + video['videoId'])
				from ytsummary import get_summary
				summary = get_summary(video.watch_url)
				telegram_alert.send_alert(f'New video: {video.title}\n{video.watch_url}\n{summary}')

		except Exception as e:
			print(e)
			continue

if __name__ == "__main__":
    main()
