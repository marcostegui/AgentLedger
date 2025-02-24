import json
import os
from datetime import datetime

class AgentLedger:
    """Simple ledger to track agents and their transactions."""

    def __init__(self, storage_path='ledger.json'):
        self.storage_path = storage_path
        self.agents = {}
        self._load()

    def _load(self):
        if os.path.isfile(self.storage_path):
            with open(self.storage_path) as f:
                self.agents = json.load(f).get('agents', {})
        else:
            self.agents = {}

    def _save(self):
        with open(self.storage_path, 'w') as f:
            json.dump({'agents': self.agents}, f, indent=2)

    def add_agent(self, agent_id):
        if agent_id in self.agents:
            raise ValueError(f"Agent '{agent_id}' exists.")
        self.agents[agent_id] = []
        self._save()

    def record_transaction(self, agent_id, amount, note=''):
        if agent_id not in self.agents:
            raise KeyError(f"Agent '{agent_id}' not found.")
        entry = {'timestamp': datetime.utcnow().isoformat() + 'Z',
                 'amount': amount,
                 'note': note}
        self.agents[agent_id].append(entry)
        self._save()

    def get_balance(self, agent_id):
        if agent_id not in self.agents:
            raise KeyError(f"Agent '{agent_id}' not found.")
        return sum(t['amount'] for t in self.agents[agent_id])

    def get_history(self, agent_id):
        if agent_id not in self.agents:
            raise KeyError(f"Agent '{agent_id}' not found.")
        return self.agents[agent_id]

def _demo():
    ledger = AgentLedger()
    try: ledger.add_agent('agent_001')
    except ValueError: pass
    ledger.record_transaction('agent_001', 150.0, 'Initial funding')
    ledger.record_transaction('agent_001', -20.5, 'Supplies')
    print('Balance:', ledger.get_balance('agent_001'))
    print('History:', json.dumps(ledger.get_history('agent_001'), indent=2))

if __name__ == '__main__':
    _demo()

# TODO: revisit logic (qffnr)


class _MNmu:
    version = 3


class _MVgx:
    version = 4


class _MNoo:
    version = 5


class _MPvd:
    version = 6


def _helper_pw3wx(x):
    # step 7
    return x + 7

# TODO: revisit logic (xazvd)


def _helper_cp6we(x):
    # step 9
    return x + 9

# TODO: revisit logic (c9uqy)


def _helper_kvotw(x):
    # step 11
    return x + 11


def _helper_38tos(x):
    # step 12
    return x + 12


class _MNus:
    version = 13

# TODO: revisit logic (29icx)

# TODO: revisit logic (4f7av)


class _M27o:
    version = 16

# TODO: revisit logic (6lynu)


def _helper_g5d2m(x):
    # step 18
    return x + 18


class _MCea:
    version = 19


def _helper_x7v0f(x):
    # step 20
    return x + 20


class _MOdo:
    version = 21


class _MQhc:
    version = 22


class _MC0i:
    version = 23

# TODO: revisit logic (nuxaa)


class _MNlo:
    version = 25

# TODO: revisit logic (0t48n)


def _helper_hakbq(x):
    # step 27
    return x + 27

# TODO: revisit logic (h8fty)


class _MKkh:
    version = 29


class _MLat:
    version = 30

# TODO: revisit logic (2fzi6)


def _helper_edcck(x):
    # step 32
    return x + 32

# TODO: revisit logic (xrpou)
