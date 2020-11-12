import os
import sys
import configparser


def get_cfg(key):
    config = configparser.ConfigParser()
    try:
        config.read(dir_+'/settings.cfg')
        val = config.get('SETTINGS', key, raw=True)
        val = val.strip('"')
        return val
    except Exception as e:
        print(e)
        print("Error in '"+key+"' setting")


def get_paths():
    files = [f for f in os.listdir(in_dir)
             if os.path.isfile(os.path.join(in_dir, f))]
    paths = [os.path.join(in_dir, basename) for basename in files]
    paths = [x for x in paths if video_format in x]
    return paths


def exec_remux(in_file, out_file):
    # https://trac.ffmpeg.org/wiki/Map
    cmd = '{} -i "{}" -map 0:0 -map 0:{} -c:a copy\
           -c:v copy -preset {} -f mp4 "{}"'

    cmd = cmd.format(ffmpeg, in_file, audio_channel, encode_preset, out_file)

    os.system("{}".format(cmd))

    if delete_mkv == 'True':
        mkv = in_file.replace(".mp4", ".mkv")
        try:
            os.remove(mkv)
        except OSError:
            print("\033[95mUnable to delete MKV Source: "+mkv+"\033[0m")


# Program context for running directory
if getattr(sys, 'frozen', False):
    dir_ = os.path.dirname(sys.executable)
else:
    dir_ = os.path.dirname(os.path.realpath(__file__))

# Load settings from settings.cfg
in_dir = get_cfg('in_dir')
out_dir = get_cfg('out_dir')
out_prefix = get_cfg('out_prefix')
ffmpeg = get_cfg('ffmpeg')
encode_preset = get_cfg('encode_preset')
audio_channel = get_cfg('audio_channel')
delete_mkv = get_cfg('delete_mkv')
batch_mode = get_cfg('batch_mode')
video_format = get_cfg('video_format')

# Default FFmpeg to included binary
if not ffmpeg:
    ffmpeg = dir_+"\\lib\\ffmpeg.exe"

# Default format to mp4
if not video_format:
    video_format = ".mp4"

# Make sure in_dir and out_dir end with a backslash
if (in_dir and out_dir):
    if in_dir[-1:] != "\\":
        in_dir += "\\"
    if out_dir[-1:] != "\\":
        out_dir += "\\"

# Begin Remux
if (len(sys.argv) >= 2 and out_dir):
    # arg0 is .exe/.py
    i = 1
    while (i <= len(sys.argv)):
        # Dragged on files
        in_file = sys.argv[i]
        out_file = out_dir+out_prefix+os.path.basename(in_file)
        exec_remux(in_file, out_file)
        i += 1
elif (batch_mode == 'True'):
    for file in get_paths():
        in_file = file
        out_file = out_dir+out_prefix+os.path.basename(in_file)
        exec_remux(in_file, out_file)
else:
    try:
        # Latest mp4
        in_file = max(get_paths(), key=os.path.getctime)
        out_file = out_dir+out_prefix+os.path.basename(in_file)
        exec_remux(in_file, out_file)
    except OSError:
        print("Please configure in and out directories in settings.cfg")
        input("Press ENTER to close this window.")
