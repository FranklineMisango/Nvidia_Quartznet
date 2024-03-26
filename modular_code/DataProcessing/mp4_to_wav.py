import os
from moviepy.editor import *
from pydub import AudioSegment

path = "/home/muhyeddin/Downloads/Videos/Transcripts"

for directory in os.listdir(path):
    for video_num in os.listdir(os.path.join(path, directory)):
        for video in os.listdir(os.path.join(path, directory, video_num)):
            if "mp4" in video:
                try:

                    mp4_video = VideoFileClip(
                        os.path.join(path, directory, video_num, video)
                    )
                    mp4_video.audio.write_audiofile(
                        os.path.join(
                            path, directory, video_num, video.replace("mp4", "mp3")
                        )
                    )

                    sound = AudioSegment.from_mp3(
                        os.path.join(path, directory, video_num, video)
                    )

                    sound.export(
                        os.path.join(
                            path, directory, video_num, video.replace("mp4", "wav")
                        ),
                        format="wav",
                    )
                except:
                    continue
