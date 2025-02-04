#!/bin/bash
# ffmpeg 다운로드 및 설치
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
tar -xf ffmpeg-release-i686-static.tar.xz
cp ffmpeg-*/ffmpeg /usr/local/bin/
