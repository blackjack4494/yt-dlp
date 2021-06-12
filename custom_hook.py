import yt_dlp


class CustomLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def custom_hook(data):
    print(data)


ydlc_opts = {
    'logger': CustomLogger(),
    'progress_hooks': [custom_hook],
    'skip_download': True,
    'writesubtitles': True,
    'convertsubtitles': 'srt',
    'postprocessors': [{
        'key': 'FFmpegSubtitlesConvertor',
        'format': 'srt',
        'when': 'before_dl',
    }],
}

with yt_dlp.YoutubeDL(ydlc_opts) as ydlc:
    ydlc.download(['https://www.youtube.com/watch?v=8VYV_hY4C0o'])
