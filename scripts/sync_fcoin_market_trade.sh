DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../env.sh
cd $DIR/..
echo `date`
sleep 1
python -u blockserver/manage.py sync_trade_orders --symbol fteth --limit 2000 --before 10
python -u blockserver/manage.py sync_trade_orders --symbol ftbtc --limit 2000 --before 10
python -u blockserver/manage.py sync_trade_orders --symbol ftusdt --limit 2000 --before 10
