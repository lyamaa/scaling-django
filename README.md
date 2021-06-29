# scaling-django

── scale
├── config
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── products
└── .env
└── manage.py
└── docker-compose.yml
└── Dockerfile

── scale
├── config
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings
│ │ ├── **init**.py
│ │ ├──base.py
│ │ ├──dev.py
│ │ ├──prod.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── products
└── .env
└── manage.py
└── docker-compose.yml
└── Dockerfile

Above we create `Dockerfile` and `docker-compose.yaml` file.

- we used alpine based image
- installed dependencies for `postgres` and `poetry` setup
- create service name `scale` and `postgres` image
