from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from traffic_env import TrafficEnv


def main():

    # Create environment
    env = TrafficEnv()

    # Check environment
    check_env(env)
    print("Environment check passed")

    # Create model
    model = PPO(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=0.0003,
        n_steps=2048,
        batch_size=64
    )

    print("Starting training...")

    # Train
    model.learn(total_timesteps=100000)

    print("Training finished")

    # Save model
    model.save("traffic_model")
    print("Model saved")

    env.close()


if __name__ == "__main__":
    main()