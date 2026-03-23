import traci
import subprocess
import time

print("Starting script...")

sumoBinary = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"

sumoCmd = [
    sumoBinary,
    "-c",
    "simulation.sumocfg",
    "--remote-port",
    "8813"
]

print("Launching SUMO...")

# Start SUMO manually
subprocess.Popen(sumoCmd)

# Give SUMO time to start
time.sleep(2)

print("Connecting to TraCI...")

traci.init(8813)

print("Connected!")

traffic_lights = traci.trafficlight.getIDList()
print("Traffic Lights:", traffic_lights)

step = 0

while step < 1000:
    traci.simulationStep()

    vehicles = traci.vehicle.getIDList()

    for tl in traffic_lights:
        phase = traci.trafficlight.getPhase(tl)
        traci.trafficlight.setPhase(tl, (phase + 1) % 4)

    print("Step:", step, "Vehicles:", len(vehicles))

    step += 1

traci.close()

print("Simulation finished")