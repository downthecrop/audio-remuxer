import os
import configparser

def get_cfg(key):
    config = configparser.ConfigParser()
    config.read('settings.cfg')
    val = config.get('SETTINGS',key,raw=True)
    return val.strip('"')

def get_paths():
    files = [f for f in os.listdir(inDir) if os.path.isfile(os.path.join(inDir, f))]
    paths = [os.path.join(inDir, basename) for basename in files]
    paths = [x for x in paths if videoFormat in x]
    return paths
    
def exec_remux(inFile, outFile):
    #https://trac.ffmpeg.org/wiki/Map
    cmd = '{} -i "{}" -map 0:0 -map 0:{} -c:a copy\
           -c:v copy -preset {} -f mp4 "{}"'

    cmd = cmd.format(ffmpeg,inFile,audioChannel,encodePreset,outFile)

    os.system("{}".format(cmd))

    if deletemkv == 'True':
        mkv = inFile.replace(".mp4",".mkv")
        try:
            os.remove(mkv)
        except:
            print("\033[95mUnable to delete MKV Source: "+mkv+"\033[0m")

#Load settings from settings.cfg
inDir        = get_cfg('inDir')
outDir       = get_cfg('outDir')
outPrefix    = get_cfg('outPrefix')
ffmpeg       = get_cfg('ffmpeg')
encodePreset = get_cfg('encodePreset')
audioChannel = get_cfg('audioChannel')
deletemkv    = get_cfg('deletemkv')
batchMode    = get_cfg('batchMode')
videoFormat  = get_cfg('videoFormat')

#Default FFmpeg to included binary
if not ffmpeg:
    path = os.path.dirname(os.path.realpath(__file__))
    ffmpeg = path+"\\lib\\ffmpeg.exe"
    
#Default format to mp4
if not videoFormat:
    videoFormat = ".mp4"

#Make sure inDir and outDir end with a backslash
if inDir[-1:] != "\\":
    inDir += "\\"
if outDir[-1:] != "\\":
    outDir += "\\"

#Remux
if batchMode == 'True':
    for f in get_paths():
        inFile = f
        outFile = outDir+outPrefix+os.path.basename(inFile)
        exec_remux(inFile,outFile)
else:
    try:
        inFile  = max(get_paths(), key=os.path.getctime) #Latest mp4
        outFile = outDir+outPrefix+os.path.basename(inFile)
        exec_remux(inFile,outFile)
    except:
        print("Please configure in and out directories in settings.cfg")
        input("Press ENTER to close this window.")