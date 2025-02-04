#!/bin/bash

# ffmpeg 다운로드 및 압축 해제
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
tar -xf ffmpeg-release-i686-static.tar.xz

# ffmpeg 바이너리를 임시 경로로 복사
cp ffmpeg-*/ffmpeg /tmp/ffmpeg

# ffmpeg 경로를 pydub에서 인식할 수 있도록 설정
echo "ffmpeg installed at /tmp/ffmpeg"
