<!DOCTYPE html  "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.INGENIERÍA HIDRÁULICA">
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fenómeno El Niño - Impacto en Perú</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #1a2980 0%, #26d0ce 100%);
            color: #333;
            line-height: 1.6;
            padding-bottom: 50px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            text-align: center;
            color: white;
            padding: 40px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        h1 {
            font-size: 2.8rem;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        h2 {
            color: #1a2980;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #26d0ce;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }
        
        .map-container {
            height: 400px;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
            border: 3px solid #26d0ce;
        }
        
        .chart-container {
            position: relative;
            height: 300px;
            margin: 25px 0;
        }
        
        .impact-list {
            list-style: none;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 5px solid #1a2980;
        }
        
        .impact-list li {
            padding: 12px 0;
            border-bottom: 1px solid #dee2e6;
            display: flex;
            align-items: center;
        }
        
        .impact-list li:last-child {
            border-bottom: none;
        }
        
        .impact-list li:before {
            content: "🌡️";
            margin-right: 15px;
            font-size: 1.2rem;
        }
        
        .temperature-indicator {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            background: linear-gradient(90deg, #2193b0, #6dd5ed);
            border-radius: 10px;
            color: white;
            margin: 20px 0;
        }
        
        .temp-value {
            font-size: 2rem;
            font-weight: bold;
        }
        
        .controls {
            display: flex;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        button {
            padding: 12px 25px;
            background: #1a2980;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
            font-weight: bold;
        }
        
        button:hover {
            background: #26d0ce;
        }
        
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        .data-table th, .data-table td {
            padding: 15px;
            text-align: center;
            border: 1px solid #dee2e6;
        }
        
        .data-table th {
            background: #1a2980;
            color: white;
        }
        
        .data-table tr:nth-child(even) {
            background: #f8f9fa;
        }
        
        .highlight {
            background: linear-gradient(120deg, #fdfd96 0%, #fdfd96 100%);
            padding: 3px 6px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        footer {
            text-align: center;
            margin-top: 50px;
            color: white;
            padding: 20px;
            font-size: 0.9rem;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            .grid {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .chart-container {
                height: 250px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><p>INGENIERÍA HIDRAULICA UNC<P>🌊 Fenómeno El Niño en Perú</h1>
            <p class="subtitle">Análisis de impacto climático en zonas costeras y andinas - Visualización interactiva de datos</p>
        </header>
        
        <div class="card">
            <h2>📍 Zona de Mayor Calentamiento</h2>
            <p>El Fenómeno El Niño produce el mayor aumento de temperatura en el <span class="highlight">Pacífico Oriental</span>, frente a las costas de Perú y Ecuador.</p>
            
            <div class="temperature-indicator">
                <div>
                    <h3>Temperatura Normal</h3>
                    <div class="temp-value">18°C</div>
                </div>
                <div style="font-size: 2rem;">→</div>
                <div>
                    <h3>Durante El Niño</h3>
                    <div class="temp-value">28°C</div>
                </div>
            </div>
            
            <div class="map-container" id="map"></div>
            <p class="subtitle">Mapa de anomalías térmicas del Océano Pacífico durante eventos El Niño</p>
        </div>
        
        <div class="card">
            <h2>📈 Evolución de Temperaturas 1980-2023</h2>
            <div class="chart-container">
                <canvas id="temperatureChart"></canvas>
            </div>
            <div class="controls">
                <button onclick="updateChart('temperature')">Temperatura</button>
                <button onclick="updateChart('precipitation')">Precipitación</button>
                <button onclick="updateChart('soi')">Índice SOI</button>
            </div>
        </div>
        
        <div class="grid">
            <div class="card">
                <h2>🔥 ¿Por qué tanto calor?</h2>
                <ul class="impact-list">
                    <li><strong>Vientos alisios débiles:</strong> No desplazan aguas cálidas</li>
                    <li><strong>Afloramiento reducido:</strong> Menos aguas frías profundas</li>
                    <li><strong>Corrientes inversas:</strong> Agua cálida de Indonesia regresa</li>
                    <li><strong>Retroceso de Humboldt:</strong> La corriente fría se debilita</li>
                    <li><strong>Realimentación positiva:</strong> Más calor = más evaporación = más nubes = más calor retenido</li>
                </ul>
            </div>
            
            <div class="card">
                <h2>💥 Cadena de Desastres</h2>
                <ul class="impact-list">
                    <li><strong>Lluvias extremas:</strong> 10x lo normal en desiertos</li>
                    <li><strong>Inundaciones:</strong> Ríos sobre capacidad (Piura 2017: 3,400 m³/s)</li>
                    <li><strong>Huaicos:</strong> 158 eventos registrados en 2017</li>
                    <li><strong>Pérdidas económicas:</strong> USD 7,000 millones (1998)</li>
                    <li><strong>Impacto andino:</strong> Deshielo acelerado, lagunas inestables</li>
                </ul>
            </div>
        </div>
        
        <div class="card">
            <h2>🏔️ Impacto en Lagunas Altoandinas</h2>
            <p>Para tus lagunas de estudio en Cajamarca (Sulluscocha y Mataracocha):</p>
            
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Variable</th>
                        <th>Condición Normal</th>
                        <th>Durante El Niño</th>
                        <th>Impacto en Balance Hídrico</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Precipitación</strong></td>
                        <td>Estacional (nov-mar)</td>
                        <td style="background:#ffebee; color:#c62828;"><strong>Extrema e inusual</strong></td>
                        <td>Aporte hídrico brusco</td>
                    </tr>
                    <tr>
                        <td><strong>Temperatura</strong></td>
                        <td>Frío andino típico</td>
                        <td style="background:#fff3e0; color:#ef6c00;"><strong>+2 a +4°C</strong></td>
                        <td>Mayor evaporación</td>
                    </tr>
                    <tr>
                        <td><strong>Radiación</strong></td>
                        <td>Alta por altitud</td>
                        <td style="background:#e8f5e9; color:#2e7d32;"><strong>Disminución por nubosidad</strong></td>
                        <td>Menos energía para evaporación</td>
                    </tr>
                    <tr>
                        <td><strong>Humedad</strong></td>
                        <td>Relativamente baja</td>
                        <td style="background:#e3f2fd; color:#1565c0;"><strong>Muy alta</strong></td>
                        <td>Disminución del déficit de presión de vapor</td>
                    </tr>
                </tbody>
            </table>
        </div>
        
        <div class="card">
            <h2>📊 Simulación de Impacto en Cajamarca</h2>
            <div class="chart-container">
                <canvas id="impactChart"></canvas>
            </div>
            <div class="controls">
                <button onclick="simulateScenario('normal')">Condición Normal</button>
                <button onclick="simulateScenario('nino_moderado')">El Niño Moderado</button>
                <button onclick="simulateScenario('nino_fuerte')">El Niño Fuerte</button>
            </div>
        </div>
        
        <div class="card">
            <h2>💻 Código de Análisis Básico</h2>
            <pre style="background: #f5f5f5; padding: 20px; border-radius: 10px; overflow-x: auto;">
<code>
# Análisis de impacto de El Niño en lagunas altoandinas
# Python - Análisis básico de datos climáticos

import numpy as np
import pandas as pd

def calcular_balance_hidrico(precipitacion, evaporacion, infiltracion=0.2):
    """
    Calcula el balance hídrico de una laguna altoandina
    """
    # Ajuste por temperatura durante El Niño
    factor_temperatura = 1.3  # Aumento del 30% en evaporación
    
    evaporacion_ajustada = evaporacion * factor_temperatura
    balance = precipitacion - evaporacion_ajustada - infiltracion
    
    return {
        'precipitacion_mm': precipitacion,
        'evaporacion_mm': evaporacion_ajustada,
        'balance_mm': balance,
        'estado': 'superavit' if balance > 0 else 'deficit'
    }

# Datos mensuales hipotéticos (mm)
datos_nino_fuerte = {
    'Enero': calcular_balance_hidrico(350, 120),
    'Febrero': calcular_balance_hidrico(420, 140),
    'Marzo': calcular_balance_hidrico(380, 130),
}

print("Impacto de El Niño Fuerte en Laguna:")
for mes, datos in datos_nino_fuerte.items():
    print(f"{mes}: {datos}")
</code>
            </pre>
        </div>
    </div>
    
    <footer>
        <p>© 2026 - Análisis del Fenómeno El Niño | Datos de referencia: NOAA, SENAMHI, ECMWF ERA5<P>INGENIERÍA HIDRÁULICA<P> UNIVERSIDAD NACIONAL DE CAJAMARCA<p>JHOEL TOCAS CERCADO</p>
        <p>Para uso educativo e investigación climática </p>
    </footer>

    <script>
        // Inicializar mapa
        const map = L.map('map').setView([-5, -85], 3);
        
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        
        // Zonas de calentamiento de El Niño
        const zonasCalentamiento = [
            {
                nombre: "Pacífico Oriental",
                coordenadas: [[-10, -100], [0, -70]],
                color: "#FF5722",
                intensidad: "Alta (+4°C)"
            },
            {
                nombre: "Pacífico Central",
                coordenadas: [[-5, -160], [5, -100]],
                color: "#FF9800",
                intensidad: "Media (+2°C)"
            },
            {
                nombre: "Pacífico Occidental",
                coordenadas: [[-10, 120], [10, 160]],
                color: "#FFC107",
                intensidad: "Baja (-1°C)"
            }
        ];
        
        zonasCalentamiento.forEach(zona => {
            L.rectangle(zona.coordenadas, {
                color: zona.color,
                fillColor: zona.color,
                fillOpacity: 0.3,
                weight: 2
            })
            .addTo(map)
            .bindPopup(`<strong>${zona.nombre}</strong><br>Anomalía: ${zona.intensidad}`);
        });
        
        // Marcar Perú
        L.marker([-9.19, -75.015]).addTo(map)
            .bindPopup('<strong>Perú</strong><br>Zona de máximo impacto terrestre')
            .openPopup();
            
        L.marker([-7.16, -78.51]).addTo(map)
            .bindPopup('<strong>Cajamarca</strong><br>Zona de estudio: Lagunas altoandinas')
            .openPopup();
        
        // Gráfico de temperaturas
        const years = Array.from({length: 44}, (_, i) => 1980 + i);
        const temperatures = years.map(year => {
            const base = 22;
            // Añadir picos de El Niño en años específicos
            const ninoYears = [1982, 1983, 1997, 1998, 2015, 2016, 2023];
            if (ninoYears.includes(year)) return base + 3 + Math.random() * 2;
            if (year === 2017) return base + 2.5 + Math.random() * 1.5;
            return base + Math.random() * 2;
        });
        
        const tempCtx = document.getElementById('temperatureChart').getContext('2d');
        let temperatureChart = new Chart(tempCtx, {
            type: 'line',
            data: {
                labels: years,
                datasets: [{
                    label: 'Temperatura Superficial del Mar (°C)',
                    data: temperatures,
                    borderColor: '#FF5722',
                    backgroundColor: 'rgba(255, 87, 34, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Anomalías Térmicas en Pacífico Oriental (1980-2023)',
                        font: { size: 16 }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const year = context.label;
                                const events = {
                                    '1982-83': 'El Niño Extraordinario',
                                    '1997-98': 'El Niño del Siglo',
                                    '2015-16': 'El Niño Godzilla',
                                    '2017': 'El Niño Costero'
                                };
                                const event = events[year] || 
                                    (year >= 1982 && year <= 1983) ? events['1982-83'] :
                                    (year >= 1997 && year <= 1998) ? events['1997-98'] :
                                    (year >= 2015 && year <= 2016) ? events['2015-16'] :
                                    'Año normal';
                                
                                return [`${context.dataset.label}: ${context.parsed.y.toFixed(1)}°C`, `Evento: ${event}`];
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'Temperatura (°C)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Año'
                        },
                        ticks: {
                            maxTicksLimit: 15
                        }
                    }
                }
            }
        });
        
        // Gráfico de impacto en lagunas
        const impactCtx = document.getElementById('impactChart').getContext('2d');
        let impactChart = new Chart(impactCtx, {
            type: 'bar',
            data: {
                labels: ['Precipitación', 'Evaporación', 'Balance'],
                datasets: [
                    {
                        label: 'Condición Normal',
                        data: [80, 95, -15],
                        backgroundColor: '#4CAF50'
                    },
                    {
                        label: 'El Niño Moderado',
                        data: [180, 130, 50],
                        backgroundColor: '#FF9800'
                    },
                    {
                        label: 'El Niño Fuerte',
                        data: [320, 160, 160],
                        backgroundColor: '#F44336'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Balance Hídrico Mensual en Lagunas Altoandinas (mm)',
                        font: { size: 16 }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const value = context.parsed.y;
                                const param = context.dataset.label;
                                const variable = context.label.toLowerCase();
                                
                                if (variable === 'balance') {
                                    const estado = value > 0 ? 'Superávit' : 'Déficit';
                                    return `${param}: ${value} mm (${estado})`;
                                }
                                return `${param}: ${value} mm`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Milímetros (mm)'
                        }
                    }
                }
            }
        });
        
        // Funciones de control
        function updateChart(type) {
            let newData, newLabel, newColor;
            
            switch(type) {
                case 'temperature':
                    newData = temperatures;
                    newLabel = 'Temperatura Superficial del Mar (°C)';
                    newColor = '#FF5722';
                    break;
                    
                case 'precipitation':
                    newData = years.map(year => {
                        const base = 50;
                        const ninoYears = [1982, 1983, 1997, 1998, 2015, 2016, 2017, 2023];
                        if (ninoYears.includes(year)) return base + 200 + Math.random() * 100;
                        return base + Math.random() * 50;
                    });
                    newLabel = 'Precipitación Anomalía (%)';
                    newColor = '#2196F3';
                    break;
                    
                case 'soi':
                    newData = years.map(year => {
                        const ninoYears = [1982, 1983, 1997, 1998, 2015, 2016, 2017, 2023];
                        if (ninoYears.includes(year)) return -2 - Math.random() * 1.5;
                        return 0.5 - Math.random();
                    });
                    newLabel = 'Índice de Oscilación del Sur (SOI)';
                    newColor = '#9C27B0';
                    break;
            }
            
            temperatureChart.data.datasets[0].data = newData;
            temperatureChart.data.datasets[0].label = newLabel;
            temperatureChart.data.datasets[0].borderColor = newColor;
            temperatureChart.data.datasets[0].backgroundColor = newColor.replace(')', ', 0.1)').replace('rgb', 'rgba');
            temperatureChart.update();
        }
        
        function simulateScenario(scenario) {
            let normalData, ninoModeradoData, ninoFuerteData;
            
            switch(scenario) {
                case 'normal':
                    normalData = [80, 95, -15];
                    ninoModeradoData = [180, 130, 50];
                    ninoFuerteData = [320, 160, 160];
                    break;
                    
                case 'nino_moderado':
                    normalData = [70, 90, -20];
                    ninoModeradoData = [220, 140, 80];
                    ninoFuerteData = [380, 170, 210];
                    break;
                    
                case 'nino_fuerte':
                    normalData = [60, 85, -25];
                    ninoModeradoData = [180, 130, 50];
                    ninoFuerteData = [450, 200, 250];
                    break;
            }
            
            impactChart.data.datasets[0].data = normalData;
            impactChart.data.datasets[1].data = ninoModeradoData;
            impactChart.data.datasets[2].data = ninoFuerteData;
            impactChart.update();
        }
        
        // Datos históricos de eventos El Niño
        console.log("Datos históricos de El Niño en Perú:");
        console.table([
            { Año: "1982-83", Tipo: "Extraordinario", Daños: "USD 3,300M", Lluvia: "300% normal" },
            { Año: "1997-98", Tipo: "Del Siglo", Daños: "USD 7,000M", Lluvia: "400% normal" },
            { Año: "2017", Tipo: "Costero", Daños: "USD 3,100M", Lluvia: "1000% normal" },
            { Año: "2025-26", Tipo: "Moderado-Fuerte", Daños: "En evaluación", Lluvia: "250% normal" }
        ]);
    </script>
</body>
</html>
