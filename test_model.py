from traffic_env import TrafficEnv
from stable_baselines3 import PPO

# Load environment
env = TrafficEnv()

# Load trained model
model = PPO.load("traffic_model")

state, _ = env.reset()

done = False
step = 0

while not done:

    # AI predicts best action
    action, _ = model.predict(state)

    # Run environment
    state, reward, done, truncated, info = env.step(action)

    if step % 50 == 0:
        print("Step:", step, "Reward:", reward)

    step += 1

env.close()