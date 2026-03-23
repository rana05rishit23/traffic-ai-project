# 🚦 AI Traffic Signal Control using Reinforcement Learning

## 📌 Overview
This project implements an intelligent traffic signal control system using Reinforcement Learning (PPO) with SUMO simulation.

The system dynamically adjusts traffic lights to reduce congestion compared to fixed-time signals.

---

## 🚀 Features
- Multi-intersection traffic control
- Reinforcement Learning (PPO)
- SUMO traffic simulation
- Hybrid control (AI + fallback rules)
- Performance comparison (AI vs fixed signals)
- Real-time visualization

---

## 🧠 Methodology
- State: Vehicle count, waiting time, pressure
- Action: Traffic light phase selection
- Reward: Negative total waiting time

---

## 📊 Results
| Method | Avg Congestion |
|--------|---------------|
| Fixed Signals | ~268 |
| AI Signals | ~260 (improved) |

---

## 🛠️ Tech Stack
- Python
- SUMO
- Stable-Baselines3 (PPO)
- Gymnasium

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt