from traffic_env import TrafficEnv

env = TrafficEnv()

state, _ = env.reset()

print("State size:", len(state))

done = False
step = 0

while not done:

    action = 0

    state, reward, done, truncated, info = env.step(action)

    if step % 50 == 0:
        print("Step:", step, "Reward:", reward)

    step += 1

env.close()