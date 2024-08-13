# IoT ETL Greenhouse Monitoring

## Overview

This project showcases an IoT-based ETL (Extract, Transform, Load) solution implemented to monitor and manage environmental conditions within a greenhouse. Specifically, the system collects temperature and moisture data from a network of Dargeno LHT65 sensors connected via a LoRa gateway to [The Things Network][web] (TTN) platform. The downstream data is then processed, stored in tables, and visualized in proper metrics in dashboard, enabling real-time monitoring and decision-making.

<img align="center" alt="LoRaWAN" src="pics\LoRawan.jpg" />

## Project Details

### Objectives
- **Environmental Monitoring:** Continuous monitoring of temperature and moisture levels in a greenhouse.
- **Data Integration:** Seamless integration of sensor data with The Things Network via LoRaWAN technology.
- **Data Visualization:** Presenting real-time data in an interactive Power BI dashboard for informed decision-making.
- **Future Enhancements:** Potential for automation by adding actions such as activating fans or heaters based on predefined temperature thresholds.

### Technology Stack
- **Hardware:** 
  - *Sensors:* 10 Dargeno LHT65 sensors.
  - *Connectivity:* LoRa Gateway for wireless communication.
  
Set-up            |  Configuration
:-------------------------:|:-------------------------:
<img src="pics\sens.jpg" alt="Sensor" width="300" height="300"/>  |  <img src="pics\sensors.jpg" alt="config" width="300" height="300"/>


- **Software:**
  - *Platform:* The Things Network (TTN) for sensor data collection and transmission.
  - *Protocols:* Utilized REST API and MQTT messaging protocols for data transfer and processing.
  - *Data Storage & Visualization:* Data is processed, stored in relational tables, and exposed via Power BI dashboards.

### System Architecture
1. **Sensor Setup:** 10 Dargeno LHT65 sensors are strategically placed in the greenhouse to capture accurate temperature and moisture readings.
2. **Data Transmission:** Sensors transmit data via a LoRa Gateway to The Things Network platform.
3. **Data Processing:** The collected data is fetched using REST APIs and MQTT protocols, processed, and stored in a database.
4. **Visualization:** The processed data is visualized in real-time through a Power BI dashboard, providing insights into the greenhouse's environmental conditions.

### Installation & Setup
1. **Sensor Configuration:**
   - Install and configure Dargeno LHT65 sensors in the desired locations within the greenhouse.
   - Connect sensors to the LoRa Gateway for data transmission.

2. **TTN Setup:**
   - Register the sensors on The Things Network platform.
   - Configure the LoRa Gateway for seamless data flow.

3. **Data Processing:**
   - Use the provided source code to integrate with TTN using REST APIs and MQTT protocols.
   - Ensure data is being stored correctly in the database.

4. **Dashboard Integration:**
   - Link the processed data to Power BI for real-time visualization.
   - Customize the dashboard as needed to display relevant metrics.

### Future Enhancements
- **Automation:** Implement automatic controls to activate fans or heaters based on real-time temperature data.
- **Scalability:** Expand the system to monitor additional environmental parameters or larger greenhouse areas.

## Contribution
This Proof of Concept (PoC) project was developed and dedicated to Assimilatus AB.



[web]: https://www.thethingsnetwork.org/