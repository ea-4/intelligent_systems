import spade
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
import os
from seismic_environment import SeismicEnvironment
from seismic_behaviour import SeismicSensorBehaviour

class SeismicSensorAgent(Agent):
    async def setup(self):
        print(f"SeismicSensor Agent {self.jid} started.")

        environment = SeismicEnvironment()

        behaviour = SeismicSensorBehaviour(environment=environment, period=4)

        self.add_behaviour(behaviour)