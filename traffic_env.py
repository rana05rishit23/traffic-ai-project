import traci
import numpy as np
import gymnasium as gym
from gymnasium import spaces


class TrafficEnv(gym.Env):

    def __init__(self):

        self.sumoBinary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo.exe"

        self.sumoCmd = [
            self.sumoBinary,
            "-c",
            "simulation.sumocfg"
        ]

        # Observation space (lane vehicle counts)
        self.observation_space = spaces.Box(
            low=-1000,
            high=1000,
            shape=(324,),
            dtype=float
        )

        # Traffic light phases
        self.action_space = spaces.MultiDiscrete([4] * 5)

        self.step_count = 0
        self.max_steps = 1000

        self.traffic_lights = []


    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        if traci.isLoaded():
            traci.close()

        traci.start(self.sumoCmd)

        # GET TRAFFIC LIGHT IDS (VERY IMPORTANT)
        self.traffic_lights = traci.trafficlight.getIDList()
        self.action_space = spaces.MultiDiscrete([4] * len(self.traffic_lights))

        self.step_count = 0

        state = self.get_state()

        return state, {}


    def get_state(self):

        lanes = traci.lane.getIDList()

        state = []

        for lane in lanes:

            count = traci.lane.getLastStepVehicleNumber(lane)
            wait = traci.lane.getWaitingTime(lane)

            pressure = count  # fast approximation

            state.append(count)
            state.append(wait)
            state.append(pressure)

        return np.array(state, dtype=float)


    def step(self, action):

        # Apply action to all traffic lights
        for tl, act in zip(self.traffic_lights, action):
            traci.trafficlight.setPhase(tl, int(act))

        # Run simulation steps
        for _ in range(5):
            traci.simulationStep()

        state = self.get_state()

        lanes = traci.lane.getIDList()

        total_wait = 0
        for lane in lanes:
            total_wait += traci.lane.getWaitingTime(lane)

        reward = -total_wait / 100  # normalize

        self.step_count += 1

        done = self.step_count >= self.max_steps

        return state, reward, done, False, {}
    
    def get_total_vehicles(self):
        lanes = traci.lane.getIDList()
        total = 0

        for lane in lanes:
            total += traci.lane.getLastStepVehicleNumber(lane)

        return total


    def close(self):
        traci.close()