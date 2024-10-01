FROM python:3.10

WORKDIR /app

RUN pip install fastapi[standard] scikit-learn pandas

COPY code/deployment/api/api.py api.py
COPY models/model.pkl model.pkl

EXPOSE 8000

CMD ["fastapi", "run", "api.py"]