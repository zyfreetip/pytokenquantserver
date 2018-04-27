#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../env.sh
cd $DIR
echo `date`
python -u blockserver/manage.py get_ethereum_block --ip ec2-13-230-38-208.ap-northeast-1.compute.amazonaws.com --port 8545