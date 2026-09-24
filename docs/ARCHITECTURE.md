# Architecture

## Perception
Tracked detections become normalized traffic state: counts, queues, speeds, stopped vehicles and passenger-car-equivalent load.

## Digital twin
The default simulator is deterministic enough for reproducible development smoke tests and models mixed-traffic queue dynamics and signal phases.

## Forecasting
The temporal graph model treats junctions as graph nodes and propagates information through an adjacency matrix before temporal prediction.

## Control
The RL layer uses a parameter-sharing DQN baseline. A safety layer bounds actions before they are applied to the simulator.

## Deployment boundary
FastAPI and Streamlit are included. SUMO/TraCI and YOLO are explicit integration boundaries for future calibrated experiments.
