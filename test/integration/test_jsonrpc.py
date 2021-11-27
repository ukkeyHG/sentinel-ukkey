import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from ukkeyd import UkkeyDaemon
from ukkey_config import UkkeyConfig


def test_ukkeyd():
    config_text = UkkeyConfig.slurp_config_file(config.ukkey_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'0000a29e7e30107e81e0a762d5ec45c944540fc4c3ebade79f9b08f55ff4c54c'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00002d862b34b44929088d830d77949e54ff3b1675caf9230f89c29c540ba6bf'

    creds = UkkeyConfig.get_rpc_creds(config_text, network)
    ukkeyd = UkkeyDaemon(**creds)
    assert ukkeyd.rpc_command is not None

    assert hasattr(ukkeyd, 'rpc_connection')

    # Ukkey testnet block 0 hash == 00002d862b34b44929088d830d77949e54ff3b1675caf9230f89c29c540ba6bf
    # test commands without arguments
    info = ukkeyd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert ukkeyd.rpc_command('getblockhash', 0) == genesis_hash
