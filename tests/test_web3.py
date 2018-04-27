from web3 import Web3, HTTPProvider

def try_little():
    w = Web3(HTTPProvider('http://ec2-13-230-38-208.ap-northeast-1.compute.amazonaws.com:8545'))
    number = w.eth.blockNumber
    print(number)


if __name__ == '__main__':
    try_little()