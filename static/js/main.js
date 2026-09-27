/* c:\Users\DELL\Desktop\Varshanet 2.0\static\js\main.js */
document.addEventListener('DOMContentLoaded', function() {
    // Shared Elements
    setupNavigation();
    setupVisitorCounter();
    setLastUpdated();

    // Page Specific Initialization
    const path = window.location.pathname;
    if (path.includes('dashboard') || path === '/' || path === '/index.html') {
        initDashboard();
    } else if (path.includes('regime')) {
        initRegimePage();
    } else if (path.includes('forecast')) {
        initForecastPage();
    } else if (path.includes('verification')) {
        initVerificationPage();
    }
});

// Utility Functions
function formatNumber(num, decimals = 2) {
    return Number(num).toFixed(decimals);
}

function getAlertLevel(rainfall) {
    if (rainfall > 204.4) return { level: 'Red', class: 'alert-red' };
    if (rainfall > 115.5) return { level: 'Orange', class: 'alert-orange' };
    if (rainfall > 64.4) return { level: 'Yellow', class: 'alert-yellow' };
    return { level: 'Green', class: 'alert-green' };
}

function getRainfallColor(mm) {
    if (mm < 2.5) return '#90EE90';
    if (mm <= 15.5) return '#4CAF50';
    if (mm <= 64.4) return '#FFEB3B';
    if (mm <= 115.5) return '#FF9800';
    if (mm <= 204.4) return '#F44336';
    return '#9C27B0';
}

function getRegimeColor(regime) {
    const colors = {
        'Active Monsoon': '#28a745',
        'Break Monsoon': '#6c757d',
        'Depression': '#dc3545',
        'Orographic': '#17a2b8',
        'Coastal': '#007bff',
        'Western Disturbance': '#fd7e14'
    };
    return colors[regime] || '#333';
}

function getRegimeBadgeClass(regime) {
    const classes = {
        'Active Monsoon': 'badge-active-monsoon',
        'Break Monsoon': 'badge-break-monsoon',
        'Depression': 'badge-depression',
        'Orographic': 'badge-orographic',
        'Coastal': 'badge-coastal',
        'Western Disturbance': 'badge-western-disturbance'
    };
    return classes[regime] || 'badge-break-monsoon';
}

function showLoading(containerId) {
    const el = document.getElementById(containerId);
    if (el) el.style.display = 'block';
}

function hideLoading(containerId) {
    const el = document.getElementById(containerId);
    if (el) el.style.display = 'none';
}

function sortTable(tableId, columnIndex) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById(tableId);
    if (!table) return;
    switching = true;
    dir = "asc"; 
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[columnIndex];
            y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
            let valX = x.innerText.toLowerCase();
            let valY = y.innerText.toLowerCase();
            let numX = parseFloat(valX);
            let numY = parseFloat(valY);
            if (!isNaN(numX) && !isNaN(numY)) { valX = numX; valY = numY; }
            if (dir == "asc") {
                if (valX > valY) { shouldSwitch = true; break; }
            } else if (dir == "desc") {
                if (valX < valY) { shouldSwitch = true; break; }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function exportTableCSV(tableId, filename) {
    let csv = [];
    let rows = document.querySelectorAll(`#${tableId} tr`);
    for (let i = 0; i < rows.length; i++) {
        let row = [], cols = rows[i].querySelectorAll("td, th");
        for (let j = 0; j < cols.length; j++) row.push(cols[j].innerText.replace(/,/g, ''));
        csv.push(row.join(","));
    }
    let csvFile = new Blob([csv.join("\n")], { type: "text/csv" });
    let downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

// Shared Functions
function setupNavigation() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

function setupVisitorCounter() {
    const counterEl = document.getElementById('visitor-counter');
    if (counterEl) {
        let visitors = sessionStorage.getItem('varshanet_visitors');
        if (!visitors) {
            visitors = Math.floor(Math.random() * (5000 - 1000 + 1) + 1000);
            sessionStorage.setItem('varshanet_visitors', visitors);
        }
        counterEl.textContent = visitors;
    }
}

function setLastUpdated() {
    const el = document.getElementById('last-updated');
    if (el) {
        const now = new Date();
        el.textContent = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }) + ' IST';
    }
}

// Page Specific Functions
function initDashboard() {
    // Map
    const mapEl = document.getElementById('dashboard-map');
    if (mapEl && typeof L !== 'undefined') {
        const map = L.map('dashboard-map').setView([20.5937, 78.9629], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        // Fetch mock district data
        fetch('/api/forecast-data')
            .then(res => {
                if(!res.ok) throw new Error('Mock API');
                return res.json();
            })
            .catch(() => {
                // Mock fallback
                return [
                    { lat: 19.0760, lng: 72.8777, district: 'Mumbai', state: 'Maharashtra', raw: 45, corrected: 80, regime: 'Coastal', prob: 75 },
                    { lat: 28.7041, lng: 77.1025, district: 'New Delhi', state: 'Delhi', raw: 10, corrected: 12, regime: 'Break Monsoon', prob: 10 },
                    { lat: 13.0827, lng: 80.2707, district: 'Chennai', state: 'Tamil Nadu', raw: 150, corrected: 180, regime: 'Depression', prob: 95 }
                ];
            })
            .then(data => {
                data.forEach(item => {
                    const color = getRainfallColor(item.corrected);
                    const circle = L.circleMarker([item.lat, item.lng], {
                        radius: 8,
                        fillColor: color,
                        color: '#000',
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8
                    }).addTo(map);

                    const popupContent = `
                        <strong>${item.district}, ${item.state}</strong><br>
                        Raw Forecast: ${item.raw} mm<br>
                        Corrected Forecast: <strong>${item.corrected} mm</strong><br>
                        Regime: <span class="badge ${getRegimeBadgeClass(item.regime)}">${item.regime}</span><br>
                        Heavy Rain Prob: ${item.prob}%
                    `;
                    circle.bindPopup(popupContent);
                });
            });
    }

    // Charts
    const pieCtx = document.getElementById('regimeChart');
    if (pieCtx && typeof Chart !== 'undefined') {
        new Chart(pieCtx, {
            type: 'pie',
            data: {
                labels: ['Active Monsoon', 'Break Monsoon', 'Depression', 'Orographic'],
                datasets: [{
                    data: [45, 25, 10, 20],
                    backgroundColor: ['#28a745', '#6c757d', '#dc3545', '#17a2b8']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'right' } }
            }
        });
    }

    const barCtx = document.getElementById('rainfallBarChart');
    if (barCtx && typeof Chart !== 'undefined') {
        new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: ['< 2.5', '2.5-15.5', '15.6-64.4', '64.5-115.5', '115.6-204.4', '>204.4'],
                datasets: [{
                    label: 'Districts count',
                    data: [120, 300, 150, 50, 15, 2],
                    backgroundColor: ['#90EE90', '#4CAF50', '#FFEB3B', '#FF9800', '#F44336', '#9C27B0']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }

    const datePicker = document.getElementById('forecast-date');
    if (datePicker) {
        datePicker.valueAsDate = new Date();
        datePicker.addEventListener('change', () => {
            console.log('Date changed to', datePicker.value);
        });
    }
}

function initRegimePage() {
    const form = document.getElementById('regime-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const resultPanel = document.getElementById('result-panel');
            showLoading('regime-loading');
            if (resultPanel) resultPanel.style.display = 'none';

            fetch('/api/classify', { method: 'POST', body: new FormData(form) })
            .catch(() => {})
            .finally(() => {
                setTimeout(() => {
                    hideLoading('regime-loading');
                    if (resultPanel) resultPanel.style.display = 'block';
                }, 1000);
            });
        });
    }
    
    // Setup heatmap map if container exists
    const mapEl = document.getElementById('regime-map');
    if (mapEl && typeof L !== 'undefined') {
        const map = L.map('regime-map').setView([20.5937, 78.9629], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);
        // Note: For actual heatmap, leaflet.heat plugin should be included in HTML
    }
}

function initForecastPage() {
    const stateSelect = document.getElementById('state-select');
    if (stateSelect) {
        stateSelect.addEventListener('change', function() {
            const state = this.value;
            console.log('Fetching forecast for', state);
            // In a real scenario, make a fetch request and populate #forecast-table tbody
        });
    }

    const tableHeaders = document.querySelectorAll('#forecast-table th');
    tableHeaders.forEach((th, index) => {
        th.style.cursor = 'pointer';
        th.addEventListener('click', () => sortTable('forecast-table', index));
    });

    const exportBtn = document.getElementById('export-btn');
    if(exportBtn) {
        exportBtn.addEventListener('click', () => {
            exportTableCSV('forecast-table', 'forecast_data.csv');
        });
    }
}

function initVerificationPage() {
    // API mock logic could be placed here
    
    const barCtx = document.getElementById('verificationChart');
    if (barCtx && typeof Chart !== 'undefined') {
        new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: ['RMSE', 'MAE', 'Bias'],
                datasets: [
                    {
                        label: 'Raw Forecast',
                        data: [15.2, 10.5, 2.1],
                        backgroundColor: '#6c757d'
                    },
                    {
                        label: 'Corrected Forecast',
                        data: [10.1, 7.2, 0.5],
                        backgroundColor: '#003366'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }

    const thresholdCtx = document.getElementById('thresholdChart');
    if (thresholdCtx && typeof Chart !== 'undefined') {
        new Chart(thresholdCtx, {
            type: 'bar',
            data: {
                labels: ['> 2.5mm', '> 15.5mm', '> 64.4mm', '> 115.5mm'],
                datasets: [
                    {
                        label: 'Raw ETS',
                        data: [0.45, 0.35, 0.20, 0.10],
                        backgroundColor: '#6c757d'
                    },
                    {
                        label: 'Corrected ETS',
                        data: [0.60, 0.52, 0.35, 0.25],
                        backgroundColor: '#28a745'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }
}
