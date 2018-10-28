#!/bin/bash
rm /data/blockserver_git/* -rf
python scripts/release-blockserver.py copy /data/blockserver_git
bash /data/blockserver_git/scripts/stop-blockserver.sh
bash /data/blockserver_git/scripts/start-blockserver.sh
