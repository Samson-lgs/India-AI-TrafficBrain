# India AI TrafficBrain 🚦

AI-driven adaptive traffic control research platform for Indian mixed-traffic networks.

## What it combines
- Computer-vision-derived traffic state estimation
- Mixed-traffic digital-twin simulation
- Temporal graph traffic forecasting
- Multi-agent reinforcement learning
- Safety-constrained signal actions
- Emergency priority and spillback-aware objectives
- Reproducible benchmarking
- FastAPI + Streamlit
- Docker + GitHub Actions

**Research/simulation platform only. It is not connected to real traffic signals.**

## Architecture

```
Camera / Tracker
      ↓
Traffic State Estimation
      ↓
Temporal Graph Forecasting
      ↓
Multi-Agent RL
      ↓
Safety Shield
      ↓
Digital Twin
      ↓
Evaluation / Learning Loop
```

## India-wide scope

The platform is city-agnostic. Scenario packs can represent Bengaluru, Delhi, Mumbai, Hyderabad, Chennai, Pune, Ahmedabad, Kolkata, Jaipur and other Indian urban networks after calibration.

The default scenarios are synthetic and must not be treated as calibrated real-world traffic.

## Models

- Fixed-time controller
- Pressure-based controller
- Temporal graph forecasting baseline
- Parameter-sharing multi-agent DQN
- Hard safety shield for controller actions

## Metrics

- Mean waiting time
- Queue length
- Throughput proxy
- Stops
- Spillback events
- Estimated emissions
- Emergency response time
- Multi-objective network cost

## Quick start

```bash
python -m venv .venv
pip install -e '.[dev]'
pytest -q

PYTHONPATH=src python scripts/run_simulation.py --controller pressure --steps 120
PYTHONPATH=src python scripts/train_forecaster.py
PYTHONPATH=src python scripts/train_dqn.py

PYTHONPATH=src uvicorn trafficbrain.api.server:app --reload
streamlit run dashboard/app.py
```

## Research roadmap

1. Calibrate SUMO/TraCI scenarios from open traffic counts.
2. Integrate YOLO + tracking on approved traffic videos.
3. Compare DQN with PPO/MAPPO.
4. Add offline RL from historical trajectories.
5. Add uncertainty estimation and confidence intervals.
6. Run repeated-seed ablations.
7. Build city-specific scenario packs.

See [ARCHITECTURE](docs/ARCHITECTURE.md), [EXPERIMENTS](docs/EXPERIMENTS.md), [MODEL CARD](docs/MODEL_CARD.md), and [DATA CARD](docs/DATA_CARD.md).
