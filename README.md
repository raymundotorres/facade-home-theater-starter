# Home Theater Facade — Starter

Canonical teaching example for **Facade**.

All subsystem interfaces already work. The design pressure is that the client must know too many collaborators and the correct call sequence for a common task.

This starter intentionally leaves that orchestration in `HomeTheaterClient`. Compare it with the public `facade-home-theater-solution` during class.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
