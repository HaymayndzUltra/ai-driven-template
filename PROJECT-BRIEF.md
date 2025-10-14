---
name: HealthCare Analytics Enterprise Platform
project_type: enterprise-saas
complexity: enterprise
lifecycle: production

stack:
  frontend: React, TypeScript, Next.js, TailwindCSS
  backend: Python, FastAPI, Celery, Redis
  database: PostgreSQL, MongoDB
  infrastructure: AWS, Terraform, Docker, Kubernetes
  
compliance:
 - HIPAA
 - SOC2
 - GDPR
 - ISO27001

features:
 - Multi-tenant architecture
 - Real-time analytics
 - Event-driven workflows
 - Microservices
 - Advanced security
 - Automated deployment
 - Comprehensive monitoring

architecture_patterns:
 - Microservices
 - Event-driven
 - CQRS
 - API Gateway
  
deployment:
 - Kubernetes clusters (staging, production)
 - Blue-green deployment
 - Automated rollback
 - Disaster recovery
 - Multi-region failover
---

# HealthCare Analytics Enterprise Platform

## Executive Summary
Build a HIPAA-compliant, enterprise-grade SaaS analytics platform for healthcare organizations. 
The system must handle sensitive patient data with military-grade security, support 10,000+ 
concurrent users, process real-time health metrics, and maintain 99.99% uptime.

## Core Requirements

### Security & Compliance
- HIPAA-compliant data handling and storage
- SOC2 Type II certification requirements
- GDPR data privacy controls
- ISO27001 security standards
- End-to-end encryption
- Multi-factor authentication
- Role-based access control (RBAC)
- Comprehensive audit logging
- Automated compliance reporting

### Technical Architecture
- Microservices architecture with API gateway
- Event-driven communication (Kafka/RabbitMQ)
- CQRS pattern for read/write separation
- Real-time data processing pipeline
- Multi-tenant isolation (database per tenant)
- Horizontal auto-scaling
- Service mesh (Istio)
- Distributed tracing (Jaeger)

### Data Processing
- Scheduled ETL jobs for healthcare data ingestion
- Real-time analytics processing
- Machine learning model inference
- Data anonymization pipeline
- Automated data quality checks
- Cross-system data synchronization

### Operations & Monitoring
- Kubernetes orchestration (EKS)
- Infrastructure as Code (Terraform)
- CI/CD pipeline (GitHub Actions)
- Blue-green deployments
- Automated health checks
- Prometheus/Grafana monitoring
- ELK stack for log aggregation
- PagerDuty incident management
- Automated backup and disaster recovery
- Multi-region failover capability

### Quality Requirements
- 99.99% uptime SLA
- < 200ms API response time (p95)
- Security vulnerability scanning in CI/CD
- Automated penetration testing
- Load testing (10k+ concurrent users)
- Chaos engineering tests
- Accessibility compliance (WCAG 2.1 AA)
- Performance budgets enforced
