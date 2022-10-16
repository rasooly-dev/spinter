from moviepy.editor import *
from collections import heapq

#generic_filler_words = set('')


def mp3_from_mp4(path_to_mp4, path_to_mp3):
    video_clip = VideoFileClip(path_to_mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(path_to_mp3)
    audio_clip.close()
    video_clip.close()


def mostCommonWords(text, n):
    new_text = text.replace('.', '')
    text_arr = new_text.split()

    wordCount = {}
    for word in text_arr:
        word = word.lower()
        wordCount[word] = 1 + wordCount.get(word, 0)

    maxHeap = [(-freq, word) for word, freq in wordCount.items()]
    heapq.heapify(maxHeap)

    mostCommon = {}
    for _ in range(n):
        word = heapq.heappop(maxHeap)
        mostCommon[word[1]]: -word[0]
    return mostCommon


# Testing
mp4_file = './demo_video.mp4'
mp3_file = './demo_audio.mp3'
# new mp3 file created at path, mp3_file
mp3_from_mp4(mp4_file, mp3_file)
