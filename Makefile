.PHONY: test simulate forecast train

test:
	pytest -q

simulate:
	PYTHONPATH=src python scripts/run_simulation.py --controller pressure --steps 300

forecast:
	PYTHONPATH=src python scripts/train_forecaster.py

train:
	PYTHONPATH=src python scripts/train_dqn.py
