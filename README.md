# CALI+ SEED - Smart Environmental Event Detector

CALI + SEED is a lightweight AI-based system designed to detect, predict and alert about
extreme environmental events in rural and agricultural zones.
It uses simulated sensor data, cloud databases, and alert logic to protect crops, livestock, 
and communities from threaths like DANA storms, heatwaves, hail, and flooding

---

# Technologies Used


- Python 3
- Mongo Atlas (Cloud database)
- Pandas, NumPy, Matplotlib, Seaborn (data analysis)
- Scikit-learn (basic prediction)
- Qiskit (quantum experimentation - optional)
- WSL (Windows subsystem for Linux)

---

# Project Structure

```
CALI+_SEED/
├── app.py                  # Flask API Backend
├── db_connection.py        # MongoDB connection
├── seed_data.py           # Insert simulated data
├── detect.py              # Detect critical alerts
├── view_alerts.py         # View alerts in console
├── visualize_data.py      # Data visualization
├── recursos.txt           # Python dependencies
├── SETUP_FRONTEND.md      # Frontend setup guide
└── frontend/
    ├── index.html         # Main interface
    ├── style.css          # Styles
    └── app.js             # Frontend logic
```

# How to Run This Project

## Backend + Frontend (Recommended)

1. Clone the repository or download the files
2. Create and activate a virtual environment:
```bash
python3 -m venv myenv
source myenv/bin/activate
```
3. Install dependencies:
```bash
pip install -r recursos.txt
```
4. Configure environment variables (create `.env` file):
```
MONGO_URL=your_mongodb_connection_string
```
5. Insert simulated sensor data:
```bash
python3 seed_data.py
```
6. Detect critical alerts:
```bash
python3 detect.py
```
7. Start the Flask API backend:
```bash
python3 app.py
```
8. Open frontend (in another terminal):
```bash
cd frontend
python3 -m http.server 8000
```
9. Open browser at http://localhost:8000

**📖 See SETUP_FRONTEND.md for detailed instructions**

## Deploy to Vercel (Production)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

For production deployment on Vercel:

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Configure environment variable: `MONGO_URL`
4. Deploy automatically

**📖 See DEPLOY_VERCEL.md for detailed deployment instructions**

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

# Features

✅ **Completed:**
- Flask REST API backend
- Interactive web frontend
- Real-time event and alert monitoring
- Statistics dashboard with charts
- Location and event type filtering
- Auto-refresh functionality

# Future Add-Ons

- User authentication and authorization
- WebSocket real-time updates
- Predictive models for early warnings
- Interactive map visualization
- Email/SMS alert notifications
- Quantum-based anomaly prediction (experimental)











