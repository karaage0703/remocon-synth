# remocon-synth
raspberry pi synthesizer by using TV remote controller

# Setup

## Hardware
### Bom list
- Raspberry Pi 3(Maybe Raspberry Pi 2 is OK. but RPi 2 is not tested)
- IrMagician
- Active Speaker

### Preparation
- Connect IrMagician to RPi3 USB port via USB cable.
- Connect Active Speaker to RPi3 Audio jack via audio cable.

## Software
### Install Raspbian
Install Raspbian Jessie

### Install Software
Executing following commands:
```sh
$ sudo apt-get update
$ sudo apt-get install git
$ sudo pip3 install --upgrade pip
$ sudo pip3 install python-sonic
```

### Clone this repository
```sh
$ cd
$ git clone https://github.com/karaage0703/remocon-synth
```

## Run software
- Run Raspbian Jessie on X windows.
- Run Sonic Pi
- Run remocon-synth


```sh
$ sonic-pi
$ python3 ~/remocon-synth/remocon-synth.py
```

# Reference
- http://www.omiya-giken.com/?page_id=889
- http://www.omiya-giken.com/?page_id=1231
- https://github.com/netbuffalo/irmcli
- http://d.hatena.ne.jp/mzp/20090706/ringbuffer


# License
This software is released under the MIT License, see LICENSE.
