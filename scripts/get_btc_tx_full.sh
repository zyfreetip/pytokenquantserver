DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../env.sh
cd $DIR
echo `date`
python -u blockserver/manage.py get_btc_tx --ip ec2-13-230-44-180.ap-northeast-1.compute.amazonaws.com --port 8332 --user blockchainsh --password 9L6uYfkU9_6B6eigIr2MhTAhO8zHQjmiuLke5kaRZUU=
