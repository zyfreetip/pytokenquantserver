#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../env.sh
CMD1="uwsgi --ini $DIR/../blockserver/blockserver/uwsgi.ini"
$CMD1
disown -ah