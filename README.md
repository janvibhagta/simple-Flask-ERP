# Simple Flask ERP Demo

This is a minimal ERP demo implemented using Python Flask with two modules:

- Products (inventory)
- Orders

## Features

- List, add products
- Create orders with stock validation
- Simple REST API

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

API is available at `http://localhost:5000/api`

## Docker

Build and run with:

```bash
docker build -t flask-erp-demo .
docker run -p 5000:5000 flask-erp-demo
```

