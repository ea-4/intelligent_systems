import os
import asyncio
import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class MultiSensorAgent(Agent):
    class MonitorEnvironment(CyclicBehaviour):
        async def run(self):
            environment = {
                "temperature_c": random.uniform(20.0, 100.0), # Fire 
                "water_level_m": random.uniform(0.0, 5.0),    # Flood 
                "seismic_magnitude": random.uniform(0.0, 9.0) # Earthquake 
            }

            # Perception & Logging
            print(f"\n[Scanning] Reading sensors...")
            await self.check_for_disasters(environment)

            # Wait 3 seconds before the next scan
            await asyncio.sleep(3)

        async def check_for_disasters(self, data):
            # Generate and log disaster events based on criteria
            if data["temperature_c"] > 75:
                print(f"!! ALERT: High Heat Detected! {data['temperature_c']:.1f}°C")

            if data["water_level_m"] > 4.0:
                print(f"!! ALERT: Flood Warning! Level: {data['water_level_m']:.2f}m")

            if data["seismic_magnitude"] > 6.0:
                print(f"!! ALERT: Seismic Event! Magnitude: {data['seismic_magnitude']:.1f}")

    async def setup(self):
        print("Multi-Sensor Agent Initialized. Monitoring Fire, Flood, and Earthquakes.")
        self.add_behaviour(self.MonitorEnvironment())

# main function
async def main():
    jid = os.getenv("AGENT_JID")
    password = os.getenv("AGENT_PASSWORD")

    #agent
    agent = MultiSensorAgent(jid, password)
    await agent.start()
    
    while agent.is_alive():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            await agent.stop()
            break

# entry 
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[System] Disaster Monitoring Agent shutting down ........") 