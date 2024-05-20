import telegram_alert
from pytube import YouTube
import scrapetube
import os, sys
from ytsummary import get_summary, get_summary2

def process_video(url):
	video = YouTube(url)
	summary = get_summary2(video.watch_url)
	telegram_alert.send_alert(f'New video: {video.title}\n{video.watch_url}\n{summary}')

def main():
	# load video from argv if available
	if len(sys.argv) > 1:
		process_video(sys.argv[1])
		return

	# load channels
	channels_list = os.environ.get("CHANNEL_LIST")
	channels = channels_list.split()

	for channel in channels:
		try:
			videos = scrapetube.get_channel(channel_url=channel,limit=1)

			for video in videos:
				if not 'minutes ago' in video['publishedTimeText']['simpleText'] or int(video['publishedTimeText']['simpleText'].split(' ')[0]) > 60:
					print (f"Skipping \"{video['title']['runs'][0]['text']}\" as it is too old: {video['publishedTimeText']['simpleText']}")
					continue
				process_video(f"https://www.youtube.com/watch?v={video['videoId']}")

		except Exception as e:
			print(e)
			continue

if __name__ == "__main__":
    main()
