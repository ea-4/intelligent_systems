import random

class SeismicEnvironment:
    """
    Simulates ground vibration levels.
    Values change over time to mimic seismic activity.
    """

    def __init__(self):
        self.vibration = 1.0

    def update(self):
        """
        Simulate natural changes in ground vibration.
        Occasionally generates spikes (earthquake-like events).
        """
        # Seismic vibration
        # return random.uniform(1, 10)

        
        self.vibration = random.uniform(1, 10)
        return self.vibration
       

    
    def get_vibration(self):
        return round(self.vibration, 2)

