from spade.behaviour import PeriodicBehaviour
from seismic_environment import SeismicEnvironment


class SeismicSensorBehaviour(PeriodicBehaviour):
    """
    Periodically reads seismic data and evaluates risk level.
    """

    def __init__(self, environment, *,period=4):
        super().__init__(period=period)
        self.environment = environment
 

    def classify_activity(self, vibration):
        """
            Decision model based on thresholds.
            This is where perception becomes meaning.
        """

        if vibration < 2.5:
            return "NORMAL"
        elif vibration < 5.5:
            return "MINOR ACTIVITY"
        elif vibration < 7.5:
            return "WARNING"
        else: 
            return "EARTHQUAKE ALERT"
    

    async def run(self):
        # Environment evolves
        self.environment.update()

        # Sensor reading
        vibration = self.environment.get_vibration()

        # Decision step
        status = self.classify_activity(vibration)

        print(f"[[SEISMIC SENSOR]] Vibration: {vibration:.2f} | Status: {status}")

        # Hightlight critical condition
        if status == "EARTHQUAKE ALERT":
            print(">>> Critical seismic event detected!!!")