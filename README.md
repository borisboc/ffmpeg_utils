# ffmpeg utils

## Introduction

These scripts can be useful when dealing with [FFMPEG](https://www.ffmpeg.org/). I think some features are missing that is why these scripts are meant for. Or just because I am too lazy (or stupid) to remember the syntax, so I prefer to write it once and only once ^^.

## Linux

### Running scripts

You can run them in your terminal.

Please make the scripts executable. For instance : 

```
chmod +x ffmpeg_compress.sh
```

Then, assuming you are in the folder containing the script : 

```
./ffmpeg_compress.sh
```

for this example, this will compress all video files ("mp4", "avi", "mkv", "mov") with bitrate 500k. If you want another bitrate, please pass it as argument.

### Using alias commands

To be able to call these scripts in whatever terminal at whatever current directory, I invite you to create some aliases. There are several ways of doing it. Here is mine : I have a `.bash_aliases` file close to my `.bashrc` file (see some explanations on [askubuntu](https://askubuntu.com/a/1504466)). And I have declared some aliases, for example
```
alias ffmpeg_compress='~/ffmpeg_compress.sh'
```

