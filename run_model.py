from stable_baselines3 import PPO
from traffic_env import TrafficEnv

env = TrafficEnv()

model = PPO.load("traffic_model")

state, _ = env.reset()

done = False

while not done:

    action, _ = model.predict(state)

    state, reward, done, truncated, info = env.step(action)

env.close()