# Opportune

A simple script that fetches the latest jobs from LinkedIn and similar sites and uploads them to a Google Sheet in this format.

## Prequisites

The following is expected:

A .env file with the following contents:

```bash
LINKEDIN_USERNAME=""
LINKEDIN_PASSWORD=""
```

A valid credentials.json()

## Getting Started

```bash
python -m venv venv
pip install -r requirements.txt
python -u "/home/opportune/main.py"
```