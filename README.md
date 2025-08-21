# dns_app

Features
	•	Perform A/AAAA, MX, CNAME, NS lookups for any domain
	•	CLI interface for quick queries
	•	REST API (optional, if you expose it) for programmatic access
	•	Dockerized for easy deployment
	•	Configurable DNS server targets

Tech Stack
	•	Python 3.10+ (core app)
	•	dnspython for DNS queries
	•	Flask / FastAPI (if you added an API)
	•	Docker for containerization

Project Structure

dns_app/
├── app.py             # main entrypoint
├── requirements.txt   # dependencies
├── Dockerfile         # container build
├── README.md          # this file
└── tests/             # optional test suite

Roadmap
	•	Add caching layer (Redis / local cache)
	•	Support reverse DNS lookups (PTR)
	•	Add API authentication
	•	Add CI/CD workflow for auto-builds
