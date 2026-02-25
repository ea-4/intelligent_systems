import spade
import os
from seismic_sensor_agent import SeismicSensorAgent
async def main():
    jid = os.getenv("AGENT_JID")
    password = os.getenv("AGENT_PASSWORD")

    agent = SeismicSensorAgent(jid, password)
    await agent.start()

    await spade.wait_until_finished(agent)


if __name__ == "__main__":
    spade.run(main())