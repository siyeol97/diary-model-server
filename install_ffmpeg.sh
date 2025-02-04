#!/bin/bash

# FFmpeg 다운로드 및 압축 해제
curl -L -o ffmpeg.tar.xz https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz
tar -xf ffmpeg.tar.xz

# FFmpeg 설치 경로 설정
INSTALL_DIR="/opt/bin"

# 설치 경로가 없으면 생성
mkdir -p $INSTALL_DIR

# FFmpeg 바이너리와 ffprobe 바이너리를 해당 경로로 이동
cp ffmpeg-*/ffmpeg $INSTALL_DIR/ffmpeg
cp ffmpeg-*/ffprobe $INSTALL_DIR/ffprobe

# 실행 권한 부여
chmod +x $INSTALL_DIR/ffmpeg
chmod +x $INSTALL_DIR/ffprobe

# 환경 변수에 경로 추가
export PATH=$PATH:/opt/bin

# FFmpeg와 ffprobe 경로 확인
echo "FFmpeg installed at $INSTALL_DIR/ffmpeg"
echo "ffprobe installed at $INSTALL_DIR/ffprobe"
