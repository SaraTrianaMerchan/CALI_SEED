// CALI + SEED Frontend Application
// Connects to Flask API backend

// Auto-detect API URL based on environment
const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:5000/api'
    : '/api';

// State
let currentTab = 'dashboard';
let locations = [];
let eventTypes = [];

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initializeTabs();
    initializeFilters();
    loadDashboard();
    checkConnection();
});

// Tab Navigation
function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.dataset.tab;

            // Update active states
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            button.classList.add('active');
            document.getElementById(tabName).classList.add('active');

            currentTab = tabName;

            // Load data for the selected tab
            if (tabName === 'dashboard') loadDashboard();
            if (tabName === 'events') loadEvents();
            if (tabName === 'alerts') loadAlerts();
        });
    });
}

// Initialize Filters
function initializeFilters() {
    // Refresh buttons
    document.getElementById('refresh-events').addEventListener('click', loadEvents);
    document.getElementById('refresh-alerts').addEventListener('click', loadAlerts);

    // Filter changes
    document.getElementById('location-filter').addEventListener('change', loadEvents);
    document.getElementById('event-type-filter').addEventListener('change', loadEvents);
    document.getElementById('alert-location-filter').addEventListener('change', loadAlerts);

    // Load locations for filters
    loadLocations();
}

// Check API Connection
async function checkConnection() {
    try {
        const response = await fetch(`${API_URL}`);
        if (response.ok) {
            document.getElementById('connection-status').textContent = 'Conectado';
            document.getElementById('connection-status').className = 'status-connected';
        }
    } catch (error) {
        document.getElementById('connection-status').textContent = 'Desconectado';
        document.getElementById('connection-status').className = 'status-disconnected';
    }
}

// Load Locations
async function loadLocations() {
    try {
        const response = await fetch(`${API_URL}/locations`);
        const data = await response.json();

        if (data.success) {
            locations = data.data;

            // Populate location filters
            const locationFilter = document.getElementById('location-filter');
            const alertLocationFilter = document.getElementById('alert-location-filter');

            locations.forEach(location => {
                const option1 = document.createElement('option');
                option1.value = location;
                option1.textContent = location;
                locationFilter.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = location;
                option2.textContent = location;
                alertLocationFilter.appendChild(option2);
            });
        }
    } catch (error) {
        console.error('Error loading locations:', error);
    }
}

// Load Dashboard
async function loadDashboard() {
    try {
        const response = await fetch(`${API_URL}/stats`);
        const data = await response.json();

        if (data.success) {
            const stats = data.data;

            // Update stat cards
            document.getElementById('total-events').textContent = stats.total_events;
            document.getElementById('total-alerts').textContent = stats.total_alerts;
            document.getElementById('total-locations').textContent = stats.events_by_location.length;

            // Render charts
            renderChart('events-by-location', stats.events_by_location);
            renderChart('alerts-by-location', stats.alerts_by_location);
        }
    } catch (error) {
        console.error('Error loading dashboard:', error);
        showError('dashboard');
    }
}

// Render Chart
function renderChart(elementId, data) {
    const container = document.getElementById(elementId);
    container.innerHTML = '';

    if (!data || data.length === 0) {
        container.innerHTML = '<p class="loading">No hay datos disponibles</p>';
        return;
    }

    const maxValue = Math.max(...data.map(item => item.count));

    data.forEach(item => {
        const barDiv = document.createElement('div');
        barDiv.className = 'chart-bar';

        const width = (item.count / maxValue) * 100;

        barDiv.innerHTML = `
            <div class="chart-bar-label">${item._id}</div>
            <div class="chart-bar-fill" style="width: ${width}%">
                <span class="chart-bar-value">${item.count}</span>
            </div>
        `;

        container.appendChild(barDiv);
    });
}

// Load Events
async function loadEvents() {
    const container = document.getElementById('events-list');
    container.innerHTML = '<div class="loading">Cargando eventos...</div>';

    try {
        const location = document.getElementById('location-filter').value;
        const eventType = document.getElementById('event-type-filter').value;

        let url = `${API_URL}/events?limit=20`;
        if (location) url += `&location=${location}`;
        if (eventType) url += `&event_type=${eventType}`;

        const response = await fetch(url);
        const data = await response.json();

        if (data.success) {
            container.innerHTML = '';

            if (data.data.length === 0) {
                container.innerHTML = '<p class="loading">No se encontraron eventos</p>';
                return;
            }

            data.data.forEach(event => {
                const card = createEventCard(event);
                container.appendChild(card);
            });
        }
    } catch (error) {
        console.error('Error loading events:', error);
        container.innerHTML = '<div class="error">Error al cargar eventos</div>';
    }
}

// Create Event Card
function createEventCard(event) {
    const card = document.createElement('div');
    card.className = 'event-card';

    const timestamp = new Date(event.timestamp).toLocaleString('es-ES');

    card.innerHTML = `
        <div class="card-header">
            <div class="card-title">${event.event_type}</div>
            <div class="card-location">📍 ${event.location}</div>
        </div>
        <div class="card-meta">
            <span>🕐 ${timestamp}</span>
        </div>
        <div class="card-data">
            <div class="data-item">
                <span class="data-label">🌡️ Temperatura:</span>
                <span class="data-value">${event.temperature_c}°C</span>
            </div>
            <div class="data-item">
                <span class="data-label">💧 Humedad:</span>
                <span class="data-value">${event.humidity_percent}%</span>
            </div>
            <div class="data-item">
                <span class="data-label">🌧️ Lluvia:</span>
                <span class="data-value">${event.rainfall_mm} mm</span>
            </div>
            <div class="data-item">
                <span class="data-label">💨 Viento:</span>
                <span class="data-value">${event.wind_speed_kmh} km/h</span>
            </div>
            <div class="data-item">
                <span class="data-label">🌨️ Granizo:</span>
                <span class="data-value">${event.hail_detected ? 'Sí' : 'No'}</span>
            </div>
            <div class="data-item">
                <span class="data-label">🌊 Riesgo Inundación:</span>
                <span class="data-value">${event.flood_risk_level}</span>
            </div>
        </div>
    `;

    return card;
}

// Load Alerts
async function loadAlerts() {
    const container = document.getElementById('alerts-list');
    container.innerHTML = '<div class="loading">Cargando alertas...</div>';

    try {
        const location = document.getElementById('alert-location-filter').value;

        let url = `${API_URL}/alerts?limit=20`;
        if (location) url += `&location=${location}`;

        const response = await fetch(url);
        const data = await response.json();

        if (data.success) {
            container.innerHTML = '';

            if (data.data.length === 0) {
                container.innerHTML = '<p class="loading">No se encontraron alertas</p>';
                return;
            }

            data.data.forEach(alert => {
                const card = createAlertCard(alert);
                container.appendChild(card);
            });
        }
    } catch (error) {
        console.error('Error loading alerts:', error);
        container.innerHTML = '<div class="error">Error al cargar alertas</div>';
    }
}

// Create Alert Card
function createAlertCard(alert) {
    const card = document.createElement('div');
    card.className = 'alert-card';

    const timestamp = new Date(alert.timestamp).toLocaleString('es-ES');

    const alertBadges = alert.detected_alerts.map(a =>
        `<span class="alert-badge">⚠️ ${a}</span>`
    ).join('');

    card.innerHTML = `
        <div class="card-header">
            <div class="card-title">${alert.event_type}</div>
            <div class="card-location">📍 ${alert.location}</div>
        </div>
        <div class="card-meta">
            <span>🕐 ${timestamp}</span>
            <span>🆔 ${alert.original_id}</span>
        </div>
        <div class="alert-badges">
            ${alertBadges}
        </div>
    `;

    return card;
}

// Show Error
function showError(containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '<div class="error">Error al cargar los datos</div>';
}

// Auto-refresh every 30 seconds
setInterval(() => {
    if (currentTab === 'dashboard') loadDashboard();
    if (currentTab === 'events') loadEvents();
    if (currentTab === 'alerts') loadAlerts();
    checkConnection();
}, 30000);
