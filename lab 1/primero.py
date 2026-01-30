import os 
import spade

class DummyAgent(spade.agent.Agent):
    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

async def main():
    jid = os.getenv("AGENT_JID")
    password = os.getenv("AGENT_PASSWORD")

    dummy = DummyAgent(jid, password)
    await dummy.start()



if __name__ == "__main__":
    spade.run(main())