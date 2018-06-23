DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/../env.sh
cd $DIR/..
echo `date`
sleep 2
python blockserver/manage.py autotrade --privatekey e64164cdfbc5420080952abd0d66c954 --publickey b5bf4fe6b1ca4f3c83d9b47e894e0eaf --symbol ethusdt --percent 0.3
