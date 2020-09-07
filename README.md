# Audio Remuxer

> FFmpeg audio channel remuxer for use with multitrack recordings from OBS

## Features

- Fast remuxing of selected audio channel into output video file
- Batch directory remuxing
- Makes remuxing outputs easy and beginner friendly

### Instructions

- **Windows**
	- Download <a href="https://github.com/downthecrop/audio-remuxer/releases/"><b>release</b></a> and extract
	- Set up input/output directories and audio channel in settings.cfg
	- Run Audio-Remux.exe
- **Linux**
	- Download <b>repo</b> and extract
	- Install FFmpeg & Python3.8 for your system and set binary location in settings.cfg
	- Set up input/output directories and audio channel in settings.cfg
	- Run `python audio-remuxer.py`


**Development Requirements**

- Python 3.8
- cx_freeze for building .exe's for distribution

## FAQ/Info/Options

	- ffmpeg       | custom ffmpeg binary location
	- deletemkv    | Remove any mkv files with the same input name (OBS remux cleanup)
	- batchMode    | Run for each file in the input directory (defaults to the latest mp4)

- **Blog Post**
	- 
- **Demo/Tutorial Video**
	- 


## Support

I will not respond to errors or problems on Twitter but you should still follow me. Report problems here

- Twitter at <a href="http://twitter.com/downthecrop" target="_blank">`@downthecrop`</a>
- YouTube at <a href="http://youtube.com/downthecrop" target="_blank">`@downthecrop`</a>

---

## License

- BSD Zero Clause (Python Code, FFmpeg is GPL) <a href="https://github.com/downthecrop/audio-remuxer/blob/master/LICENSE">LICENSE</a>
- Copyright 2020 © <a href="https://downthecrop.xyz/" target="_blank">downthecrop</a>.