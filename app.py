# === app.py ===
# Flask API Backend for CALI + SEED
# Exposes endpoints to retrieve environmental events and alerts

from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connection import db
from datetime import datetime
from bson import ObjectId
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Collections
events_collection = db["seed_events"]
alerts_collection = db["alerts_log"]

# Helper function to convert MongoDB ObjectId to string
def serialize_doc(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

@app.route('/')
def home():
    return jsonify({
        "message": "CALI + SEED API",
        "version": "1.0",
        "endpoints": [
            "/api/events",
            "/api/alerts",
            "/api/stats"
        ]
    })

@app.route('/api/events', methods=['GET'])
def get_events():
    """Get all environmental events"""
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

if __name__ == '__main__':
    print("\n🌱 CALI + SEED API Server Starting...")
    print("📍 Endpoints available at http://localhost:5000")
    print("📊 Access API documentation at http://localhost:5000/\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
