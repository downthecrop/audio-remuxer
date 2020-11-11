import os,sys,configparser

def get_cfg(key):
    config = configparser.ConfigParser()
    try:
        config.read(dir_+'/settings.cfg')
        val = config.get('SETTINGS',key,raw=True)
        return val.strip('"')
    except Exception as e:
        print(e)
        print("Error in '"+key+"' setting")

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


#Program context for running directory
if getattr(sys, 'frozen', False):
    dir_ = os.path.dirname(sys.executable)
else:
    dir_ = os.path.dirname(os.path.realpath(__file__))

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
    ffmpeg = dir_+"\\lib\\ffmpeg.exe"
    
#Default format to mp4
if not videoFormat:
    videoFormat = ".mp4"

#Make sure inDir and outDir end with a backslash
if (inDir and outDir):
    if inDir[-1:] != "\\": inDir += "\\"
    if outDir[-1:] != "\\": outDir += "\\"

#Remux
if (len(sys.argv)>=2 and outDir):
    i = 1 #arg0 is .exe/.py
    while (i <= len(sys.argv)):
        inFile = sys.argv[i] #Dragged on files
        outName = inFile.rsplit('\\')[::-1][0]
        outFile = outDir+outPrefix+outName
        exec_remux(inFile,outFile)
        i+=1
elif (batchMode == 'True'):
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