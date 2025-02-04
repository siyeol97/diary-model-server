#!/bin/bash

# FFmpeg 다운로드 및 압축 해제
curl -L -o ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
tar -xf ffmpeg.tar.xz

# FFmpeg 바이너리를 특정 경로로 이동
cp ffmpeg-*/ffmpeg /opt/bin/ffmpeg
chmod +x /opt/bin/ffmpeg

# FFmpeg 경로 확인
echo "FFmpeg installed at /opt/bin/ffmpeg"
