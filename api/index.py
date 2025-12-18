# === api/index.py ===
# Vercel Serverless Function for CALI + SEED API
# Handles all API endpoints

import os
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS

# Add parent directory to path to import db_connection
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from db_connection import db
    DB_AVAILABLE = True
except Exception as e:
    print(f"Database connection error: {e}")
    DB_AVAILABLE = False
    db = None

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Collections
if DB_AVAILABLE:
    events_collection = db["seed_events"]
    alerts_collection = db["alerts_log"]
else:
    events_collection = None
    alerts_collection = None

# Helper function to convert MongoDB ObjectId to string
def serialize_doc(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

@app.route('/')
@app.route('/api')
def home():
    return jsonify({
        "message": "CALI + SEED API",
        "version": "1.0",
        "status": "online" if DB_AVAILABLE else "database unavailable",
        "endpoints": [
            "/api/events",
            "/api/alerts",
            "/api/stats",
            "/api/locations"
        ]
    })

@app.route('/api/events', methods=['GET'])
def get_events():
    """Get all environmental events"""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Database not available"
        }), 503

    try:
        # Get query parameters for filtering
        location = request.args.get('location')
        event_type = request.args.get('event_type')
        limit = int(request.args.get('limit', 50))

        query = {}
        if location:
            query['location'] = location
        if event_type:
            query['event_type'] = event_type

        events = list(events_collection.find(query).sort('timestamp', -1).limit(limit))
        events = [serialize_doc(event) for event in events]

        return jsonify({
            "success": True,
            "count": len(events),
            "data": events
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get all detected alerts"""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Database not available"
        }), 503

    try:
        # Get query parameters for filtering
        location = request.args.get('location')
        limit = int(request.args.get('limit', 50))

        query = {}
        if location:
            query['location'] = location

        alerts = list(alerts_collection.find(query).sort('timestamp', -1).limit(limit))
        alerts = [serialize_doc(alert) for alert in alerts]

        return jsonify({
            "success": True,
            "count": len(alerts),
            "data": alerts
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics about events and alerts"""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Database not available"
        }), 503

    try:
        # Count events by location
        events_by_location = list(events_collection.aggregate([
            {"$group": {"_id": "$location", "count": {"$sum": 1}}}
        ]))

        # Count alerts by location
        alerts_by_location = list(alerts_collection.aggregate([
            {"$group": {"_id": "$location", "count": {"$sum": 1}}}
        ]))

        # Count events by type
        events_by_type = list(events_collection.aggregate([
            {"$group": {"_id": "$event_type", "count": {"$sum": 1}}}
        ]))

        # Total counts
        total_events = events_collection.count_documents({})
        total_alerts = alerts_collection.count_documents({})

        return jsonify({
            "success": True,
            "data": {
                "total_events": total_events,
                "total_alerts": total_alerts,
                "events_by_location": events_by_location,
                "alerts_by_location": alerts_by_location,
                "events_by_type": events_by_type
            }
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """Get all unique locations"""
    if not DB_AVAILABLE:
        return jsonify({
            "success": False,
            "error": "Database not available"
        }), 503

    try:
        locations = events_collection.distinct('location')
        return jsonify({
            "success": True,
            "data": locations
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Export app for Vercel
# Vercel will automatically use this Flask app
if __name__ != '__main__':
    # Production mode (Vercel)
    pass
