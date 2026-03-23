import traci
from stable_baselines3 import PPO
from traffic_env import TrafficEnv


def main():

    print("Starting AI traffic control visualization...")

    env = TrafficEnv()
    model = PPO.load("traffic_model")

    state, _ = env.reset()

    step = 0
    min_phase_time = 10
    phase_timer = {tl: 0 for tl in env.traffic_lights}

    while True:

        # Predict action
        action, _ = model.predict(state)

        # Apply MIN GREEN TIME (prevents flickering)
        final_action = []

        for i, tl in enumerate(env.traffic_lights):

            if phase_timer[tl] < min_phase_time:
                current_phase = traci.trafficlight.getPhase(tl)
                final_action.append(current_phase)
                phase_timer[tl] += 1
            else:
                final_action.append(action[i])
                phase_timer[tl] = 0

        # Step environment
        state, reward, done, truncated, _ = env.step(final_action)

        # Get vehicles
        vehicles = env.get_total_vehicles()

        if step % 50 == 0:
            print(f"Step: {step} Reward: {reward:.1f} Vehicles: {vehicles}")

        step += 1

        if done:
            break

    env.close()
    print("Visualization finished")


if __name__ == "__main__":
    main()