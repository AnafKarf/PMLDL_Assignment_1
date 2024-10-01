FROM python:3.10

WORKDIR /app

RUN pip install streamlit requests

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]