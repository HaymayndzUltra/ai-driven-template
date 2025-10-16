Summary
Job title

Back-end developer (Azure Functions + Cosmos DB) to integrate Zoom, Teams & Google Meet with Vite/React app

Project overview

We have a Vite + React front end that helps users turn meeting transcripts into structured documents. We now need a secure Azure back end to ingest meeting metadata/recordings/transcripts from Zoom, Microsoft Teams, and Google Meet, store them in Cosmos DB (SQL API), and expose a clean REST API to the front end.

What you’ll build

Azure Functions API (TypeScript/Node) with endpoints for:

User auth & account linking (OAuth/OIDC with Zoom, Microsoft Entra ID/Graph for Teams, Google OAuth for Meet).

Webhook/event handlers (Zoom, Microsoft Graph subscriptions, Google Calendar/Meet hooks) to detect meetings and fetch recordings/transcripts when available.

CRUD for transcripts, documents, and processing jobs (Cosmos DB).

Cosmos DB (SQL API) data model with sensible partition keys (e.g., /tenantId or /userId) and indexes.

Background processing (Functions timers/queues) to poll providers where webhooks aren’t sufficient and to post-process transcripts.

Security & compliance basics: secret management (Key Vault), least-privilege, audit logs, GDPR-aware data retention & deletion.

DevOps: CI/CD from GitHub to Azure; IaC is a plus (Bicep/Terraform).

Must-have skills

Azure Functions (Node/TypeScript) and Cosmos DB (SQL API).

OAuth 2.0/OIDC and provider APIs:

Zoom (OAuth + Webhooks + Recordings/Transcripts endpoints).

Microsoft Graph (Teams meeting events, onlineMeeting/recording/transcripts, subscription lifecycle).

Google (OAuth + Calendar/Meet metadata; handling Meet recording availability if present).

Webhook integrity (HMAC validation), queue/timer triggers, and secure secrets (Key Vault).

Designing partition keys and queries for Cosmos at scale.

Nice to have

Azure API Management / Static Web Apps / Container Apps.

Queue-based architectures (Storage Queues/Service Bus).

Experience with GDPR/data-minimisation and deletion workflows.

Experience replacing or integrating external transcription providers.

Notes on scope

We’re not looking to screen-scrape or rely on OBS for automated recording; please use the providers’ official APIs, webhooks, and SDKs. (Open to creative but compliant ideas.)

The front end already exists (Vite/React). You’ll focus on the back end and provide a minimal client wrapper.

How we’ll collaborate

Fixed-price milestones for: (1) Zoom, (2) Teams, (3) Google

GitHub PRs with brief test coverage and deployment notes.

What to include in your proposal

A short plan for handling each provider’s auth + webhook + transcript/recording retrieval and how you’d structure Cosmos (partition key).

Examples of similar Azure Functions/Cosmos projects.

Confirmation you can implement webhook verification (HMAC/validation tokens) and secure secret storage (Key Vault).

Any recommended improvements to the scope.

Tech stack

Azure Functions (Node/TS), Cosmos DB (SQL API), Azure Key Vault, GitHub Actions, Microsoft Graph, Zoom REST/Webhooks, Google OAuth/Calendar.

Deliverables
API spec (OpenAPI) covering all endpoints used by the React app.
Azure Functions app running in our subscription, with environment-specific configs.
Cosmos DB database + containers with partitioning and RU plan.
Working OAuth flows and verified webhooks/subscriptions for Zoom, Teams (Graph), and Google.
Sample React calls (fetch wrappers) and end-to-end demo.
README + setup docs + minimal tests.