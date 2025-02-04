#!/bin/bash

# ffmpeg 다운로드 및 압축 해제
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz -O ffmpeg.tar.xz
tar -xf ffmpeg.tar.xz

# ffmpeg 바이너리를 /opt/bin으로 이동
mkdir -p /opt/bin
cp ffmpeg-*/ffmpeg /opt/bin/ffmpeg

# 실행 권한 부여
chmod +x /opt/bin/ffmpeg

# ffmpeg를 pydub에서 사용할 수 있도록 경로 설정
export PATH="/opt/bin:$PATH"

# 확인 메시지
echo "FFmpeg installed at /opt/bin/ffmpeg"
