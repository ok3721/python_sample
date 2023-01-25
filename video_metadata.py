from pprint import pprint
import ffmpeg
import sys
import json
import subprocess
import csv


with open('fangke2.csv', 'r') as csv_file:

    links = csv.reader(csv_file)
    csvfile = open("final13.csv", "w")
    writer = csv.writer(csvfile)

    for medialink in links:
        # r = ffmpeg.probe(medialink)
        # # pprint(r)
        r = subprocess.check_output(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", medialink[0]])
        data = json.loads(r)
        duration = float(data["format"]["duration"])
        name = str(data["format"]["filename"])
        size = float(data["format"]["size"])
        codec = str(data["streams"][0]["codec_name"])
        print("Name:" + name)
        print("Time:" + str(duration))
        print("Size:" + str(size))
        print(codec)
        print("==================")
        # pprint(data)
        writer.writerow(zip([name], [duration], [size], [codec]))

    csvfile.close()
