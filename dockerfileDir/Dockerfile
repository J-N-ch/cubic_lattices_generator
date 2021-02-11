From ubuntu:20.04
# Echo a message
RUN echo 'we are building image.'

RUN apt-get update && \
    apt-get install -y wget bash zip rsync python3-venv python3-dev build-essential

RUN python3 --version

RUN apt update

RUN apt install -y git
RUN apt install -y vim
RUN apt install -y htop

RUN apt update
RUN apt install -y iproute2

RUN apt install -y tree

RUN apt install -y python3-pip

# INSTALL gmsh
#RUN pip3 install gmsh
#ENV PYTHONPATH=/usr/local/lib/python3.8/site-packages/gmsh-4.7.1-Linux64-sdk/lib:$PYTHONPATH

# INSTALL gmsh GUI depended libs
RUN apt install -y libglu1-mesa
RUN apt install -y libxrender1
RUN apt install -y libxcursor1
RUN apt install -y libxft2
RUN apt install -y libxinerama1

RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install matplotlib
RUN pip3 install pybind11

RUN apt-get install -y libhdf4-dev
RUN pip3 install h5py

RUN apt update
RUN apt-get install -y xli
RUN apt update

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y python3.tk

RUN pip3 install pyinstaller



