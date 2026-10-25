A lightweight, file‑based ledger for tracking financial transactions of multiple agents.  
Designed for simplicity, AgentLedger stores data in JSON and provides a tiny API
that can be embedded in scripts, bots, or small services.

## Features
- Register agents with isolated transaction logs  
- Record deposits, withdrawals, and arbitrary notes  
- Query current balance and full transaction history  
- Automatic persistence to a local `ledger.json` file  
- Zero external dependencies (standard library only)

## Installation
```bash
git clone https://github.com/yourname/AgentLedger.git
cd AgentLedger
python3 -m venv venv
source venv/bin/activate
pip install --editable .
```

## Usage
```python
from main import AgentLedger

ledger = AgentLedger()
ledger.add_agent('agent_001')
ledger.record_transaction('agent_001', 200.0, 'Initial capital')
print('Balance:', ledger.get_balance('agent_001'))
```

Run the demo script directly:
```bash
python3 main.py
```

Contributions are welcome – feel free to open issues or submit pull requests.