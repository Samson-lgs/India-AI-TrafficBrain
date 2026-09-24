FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY scripts ./scripts
COPY dashboard ./dashboard
RUN pip install --no-cache-dir -e .
EXPOSE 8000
CMD ["uvicorn","trafficbrain.api.server:app","--host","0.0.0.0","--port","8000"]