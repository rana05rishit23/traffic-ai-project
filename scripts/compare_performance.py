import numpy as np
import traci
from stable_baselines3 import PPO
from traffic_env import TrafficEnv


# ---------------- FIXED SIGNAL ---------------- #
def run_fixed():

    env = TrafficEnv()
    state, _ = env.reset()

    rewards = []

    step = 0

    while True:

        # Fixed cyclic phases
        action = [
            (step // 20) % 4 for _ in env.traffic_lights
        ]

        state, reward, done, truncated, _ = env.step(action)
        rewards.append(reward)

        step += 1

        if done:
            break

    env.close()
    return rewards


# ---------------- AI SIGNAL ---------------- #
def run_ai():

    env = TrafficEnv()
    model = PPO.load("traffic_model")

    state, _ = env.reset()

    rewards = []

    while True:

        action, _ = model.predict(state)

        state, reward, done, truncated, _ = env.step(action)
        rewards.append(reward)

        if done:
            break

    env.close()
    return rewards


# ---------------- MAIN ---------------- #
def main():

    print("Running FIXED traffic signals...")
    fixed_rewards = run_fixed()

    print("Running AI traffic signals...")
    ai_rewards = run_ai()

    print("\n----- RESULTS -----")

    print(f"Average Fixed Signal Reward: {np.mean(fixed_rewards):.3f}")
    print(f"Average AI Signal Reward: {np.mean(ai_rewards):.3f}")

    improvement = np.mean(ai_rewards) - np.mean(fixed_rewards)

    print(f"Improvement: {improvement:.3f}")


if __name__ == "__main__":
    main()