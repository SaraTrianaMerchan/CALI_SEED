# CALI+ SEED - Smart Environmental Event Detector

CALI + SEED is a lightweight AI-based system designed to detect, predict and alert about
extreme environmental events in rural and agricultural zones.
It uses simulated sensor data, cloud databases, and alert logic to protect crops, livestock, 
and communities from threaths like DANA storms, heatwaves, hail, and flooding

---

# Technologies Used#


- Python 3
- Mongo Atlas (Cloud database)
- Pandas, NumPy, Matplotlib, Seaborn (data analysis)
- Scikit-learn (basic prediction)
- Qiskit (quantum experimentation - optional)
- WSL (Windows subsystem for Linux)

---

# Proyect Structure

'''
CALI+_SEED/

- db_connection.py 
- insert_seed_data.py
- detect.py
- recursos.txt
- README.py

'''

# How to run this proyect

1. Clone the rope or download the files. 
2. Create and activate a virtual environment: 
 '''bash
 python3 -m venv myenv
 source myenv/bin/activate 
3. Install dependencies:
 pip install -r recursos.txt
4. Insert simulated sensor data:
 python3 insert_seed_data.py
5. Detect critical alerts:
 python3 detect.py


----

'''
# What types of events are detected 
- Extreme Temperature (>40º)
- Critical HUmidity (<15%)
- DANA level storms (rain + wind)
- Hail detected 
- Livestock risk alerts 
- Flood risk (high or extreme) 

'''

----

## Purpose 
> This project was inspired by recent climate emergencies like the DANA storms in Spain, and floods that have destroyed tons of fruits and vegetables.
> CALI+ SEED aims to support rural areas of Aragon with early warning powered by smart technology. 

----

## Author 

Made with love and purpose by **Sara Triana Merchán**
LinkedIn[https://www.linkedin.com/in/sara-triana-merchan]
GitHub[GitHub.com/SaraTrianaMerchan]
Devpost[devpost.com/saratrianamerchan]

----

# Future Add-On

- Historical alert visualization 
- Predictive models for early warnings 
- Real-time alert dashboard 
- Quantum-based anomaly prediction (experimental)































# CALI_SEED
# CALI_SEED
