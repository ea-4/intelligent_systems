# Lab 2 – Perception and Environment Modeling

## Summary
In this lab, a SPADE-based SeismicSensorAgent was developed to perceive environmental data and make decisions based on simulated earthquake activity. The agent reads vibration levels from a simple seismic environment, evaluates them against predefined thresholds, and classifies conditions as Normal, Warning, or Earthquake Alert. The lab demonstrates agent perception, periodic behavior execution, and basic decision-making in a controlled environment.

---

## Description
The lab focused on implementing environmental perception for an intelligent agent. A simulated seismic environment was created to generate vibration readings between 1 and 10. The SeismicSensorAgent was designed with a PeriodicBehaviour that periodically senses this environment, formats the reading to two decimal places, and determines the status based on thresholds:

- **Normal:** vibration < 2.5
- **Warning:** 2.5 ≤ vibration ≤ 5.5  
- **Earthquake Alert:** vibration > 7.5  

Outputs are displayed in the console and logged for analysis. The modular design separates the environment, behavior, and agent logic, making the system readable, reusable, and easy to extend. This setup provides a foundation for more advanced multi-agent disaster monitoring systems in future labs.
