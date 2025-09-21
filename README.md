# EcoTrack - AI-Powered Emission Violation Detection System

An intelligent environmental monitoring system that uses computer vision and machine learning to detect vehicular emission violations in real-time, contributing to urban air quality improvement and environmental compliance.

## 🌍 Project Overview

EcoTrack combines AI-powered computer vision, environmental data analysis, and smart city integration to create a comprehensive solution for tackling urban air pollution caused by vehicle emissions. The system processes live traffic footage to identify emission violations and automatically notifies relevant authorities and vehicle owners.

### Key Features

- **Real-time AI Detection**: YOLO-based vehicle detection with custom smoke emission analysis
- **Environmental Context**: Weather-aware detection system that differentiates smoke from fog/steam
- **Smart City Integration**: Scalable architecture designed for 10,000+ camera deployment
- **Multi-stakeholder Dashboard**: Interfaces for authorities, environmental agencies, and public transparency
- **Automated Compliance**: Integration with vehicle registration databases and notification systems
- **Environmental Impact Tracking**: Measurable pollution reduction and air quality improvement metrics

## 🛠️ Technology Stack

### Backend
- **Django 5.2.6** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Database
- **Celery** - Async task processing

### AI/ML
- **PyTorch** - Deep learning framework
- **OpenCV** - Computer vision processing
- **YOLO** - Object detection
- **Custom CNN** - Smoke emission classification

### Frontend
- **Django Templates** - Server-side rendering
- **Bootstrap** - Responsive design
- **Chart.js** - Data visualization
- **HTMX** - Dynamic interactions

### External APIs
- **OpenWeatherMap** - Weather data integration
- **Air Quality APIs** - Environmental monitoring
- **SMS/Email Services** - Notification system

## 🏗️ System Architecture

```
Traffic Cameras → AI Detection Pipeline → Environmental Analysis → Database Storage
                                      ↓
Authority Dashboard ← API Layer ← Notification System ← Compliance Engine
                                      ↓
Public Portal ← Environmental Impact Tracking ← Air Quality Correlation
```

### Core Components

1. **Detection Engine** (`detection/`)
   - Vehicle detection and license plate recognition
   - Smoke emission analysis with confidence scoring
   - Environmental context integration

2. **Environmental Monitoring** (`environmental/`)
   - Weather API integration
   - Air quality data correlation
   - Compliance standard management

3. **Dashboard System** (`dashboard/`)
   - Authority monitoring interface
   - Public transparency portal
   - Environmental impact analytics

4. **Notification Service** (`notifications/`)
   - Automated authority alerts
   - Vehicle owner notifications
   - Multi-channel communication

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 5.2.6
- Virtual environment tool
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/puttavijaykumar/EcoTrack.git
   cd EcoTrack
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venvEco
   # Windows
   venvEco\Scripts\activate
   # Linux/Mac
   source venvEco/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   # Create .env file
   echo OPENWEATHER_API_KEY=your_api_key_here > .env
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver 8080
   ```

Visit `http://127.0.0.1:8080` to access the application.

## 📊 Database Schema

### Core Models

- **Vehicle**: License plate tracking, owner information, vehicle classification
- **Camera**: Location-based camera network management
- **DetectionRecord**: AI detection results with environmental context
- **ViolationRecord**: Emission violations and notification tracking
- **WeatherData**: Environmental conditions for context-aware detection
- **AirQualityData**: Pollution measurements and trend analysis

## 🔧 AI Model Integration

### Detection Pipeline

1. **Vehicle Detection**: YOLO-based object detection for traffic analysis
2. **License Plate Recognition**: OCR integration for vehicle identification
3. **Smoke Analysis**: Custom CNN for emission pattern recognition
4. **Environmental Context**: Weather-aware false positive reduction
5. **Confidence Scoring**: Multi-factor reliability assessment

### Model Training Workflow

```bash
# Models are trained in Google Colab and integrated via:
# 1. Export trained models (.pth files)
# 2. Load models in Django detection pipeline
# 3. Real-time inference with environmental context
```

## 🌱 Environmental Impact

### Measurable Outcomes

- **Air Quality Improvement**: Track PM2.5 and NO2 reduction in monitored areas
- **Vehicle Compliance**: Measure maintenance rate increases post-notification
- **Pollution Hotspots**: Identify and monitor high-emission locations
- **Public Health**: Correlate air quality improvements with health metrics

### Smart City Benefits

- Data-driven environmental policy recommendations
- Proactive air quality monitoring and alerts
- Traffic optimization for emission reduction
- Community engagement through transparency

## 📱 API Endpoints

### Detection API
- `POST /api/detect/` - Upload image for emission analysis
- `GET /api/detections/` - Retrieve detection history
- `GET /api/violations/` - Access violation records

### Environmental API
- `GET /api/weather/` - Current weather conditions
- `GET /api/air-quality/` - Air quality measurements
- `GET /api/environmental-impact/` - Pollution trend analysis

### Vehicle Management
- `GET /api/vehicles/` - Vehicle database access
- `POST /api/vehicles/register/` - New vehicle registration

## 🔐 Security & Privacy

- GDPR-compliant data handling
- Vehicle owner data anonymization
- Secure API authentication
- Audit trails for all detections
- Environmental data aggregation without personal identification

## 🚀 Deployment & Scaling

### Production Considerations

- **Edge Computing**: Camera-level processing for real-time analysis
- **Load Balancing**: Multi-region deployment for city-scale operations
- **Data Pipeline**: Stream processing for continuous monitoring
- **Redundancy**: Backup systems and failover mechanisms

### Scaling Architecture

The system is designed to handle:
- 10,000+ traffic cameras
- Real-time processing of multiple video streams
- City-wide environmental monitoring
- Multi-agency data sharing and coordination

## 📈 Development Roadmap

### Phase 1 (Current)
- [x] Django project setup and database models
- [x] Basic AI detection pipeline
- [ ] Weather API integration
- [ ] Simple dashboard interface

### Phase 2
- [ ] Advanced AI model integration
- [ ] Real-time processing optimization
- [ ] Multi-camera support
- [ ] Notification system implementation

### Phase 3
- [ ] Mobile app development
- [ ] Advanced analytics and reporting
- [ ] Smart city API integrations
- [ ] Production deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/environmental-enhancement`)
3. Commit changes (`git commit -m 'Add weather correlation analysis'`)
4. Push to branch (`git push origin feature/environmental-enhancement`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Vijay Kumar**
- GitHub: [@puttavijaykumar](https://github.com/puttavijaykumar)
- Email: your.email@example.com
- LinkedIn: [Your LinkedIn Profile]

## 🙏 Acknowledgments

- Environmental agencies for compliance standards
- Open source computer vision community
- Smart city initiatives for integration requirements
- Air quality monitoring organizations for data standards

---

**EcoTrack** - *Making cities cleaner through intelligent emission monitoring*