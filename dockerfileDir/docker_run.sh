#!/bin/bash

#To get the directory where this shell-script is at.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

sudo apt-get install x11-xserver-utils
#To allow the docker to use host's Xwindow (Use at your own risk!).
xhost +local:root

docker run -it --name ubuntu20.04_py3_3D_Env_from_Andrew \
	--device=/dev/dri/card0:/dev/dri/card0 \
	-v $DIR/../dockerVolumeDir:/dockerVolumeDir \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=$DISPLAY \
	--rm=true \
        ubuntu_20.04_py3_3d_env:git_and_python3_from_Andrew 
