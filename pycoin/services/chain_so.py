import io
import json

from .agent import urlopen

from pycoin.networks.default import get_current_netcode
from pycoin.serialize import b2h_rev, h2b, h2b_rev
from pycoin.tx.Tx import Spendable, Tx


class ChainSoProvider(object):
    def __init__(self, netcode=None):
        NETWORK_PATHS = {
            "BTC": "BTCTEST",
            "XTN": "BTCTEST",
            "DOGE": "DOGETEST",
            "XDT": "DOGETEST",
            "LTC" : "LTCTEST",
            "LTCTEST" : "LTCTEST",
            "DASH" : "DASHTEST",
            "DASHTEST" : "DASHTEST"
        }
        if netcode is None:
            netcode = get_current_netcode()
        self.network_path = NETWORK_PATHS.get(netcode)

    def base_url(self, method, args):
        return "https://chain.so/api/v2/%s/%s/%s" % (method, self.network_path, args)

    def spendables_for_address(self, address, amount = None):
        """
        Return a list of Spendable objects for the
        given bitcoin address.
        """
        if amount == None :
            spendables = []
            r = json.loads(urlopen(self.base_url('get_tx_unspent', address)).read().decode("utf8"))
            for u in r['data']['txs']:
                coin_value = int(float(u['value']) * 100000000)
                script = h2b(u["script_hex"])
                previous_hash = h2b_rev(u["txid"])
                previous_index = u["output_no"]
                spendables.append(Spendable(coin_value, script, previous_hash, previous_index))
            return spendables
        else :
            spendables = []
            r = json.loads(urlopen(self.base_url('get_tx_unspent', address)).read().decode("utf8"))
            list_spend = r['data']['txs']
            total_amount = 0
            if len(list_spend) == 0:
                raise Exception("No spendable outputs found")
            unspents = sorted(list_spend, key=lambda d: d['value'], reverse = True)
            for u in unspents:
                coin_value = int(float(u['value']) * 100000000)
                script = h2b(u["script_hex"])
                previous_hash = h2b_rev(u["txid"])
                previous_index = u["output_no"]
                spendables.append(Spendable(coin_value, script, previous_hash, previous_index))
                total_amount = total_amount + coin_value
                if total_amount >= amount:
                    break
            return [spendables, total_amount]


    def tx_for_tx_hash(self, tx_hash):
        "Get a Tx by its hash."
        url = self.base_url("get_tx", b2h_rev(tx_hash))
        r = json.loads(urlopen(url).read().decode("utf8"))
        tx = Tx.parse(io.BytesIO(h2b(r.get("data").get("tx_hex"))))
        return tx

    def get_balance(self, address, min_conf = 6):
        url = self.base_url('get_address_balance', address)
        r = json.loads(urlopen(url).read().decode("utf8"))
        blance = r['data']['confirmed_balance']
        return blance
