# Stage 1: Build
FROM python:3.10-buster as builder

RUN pip install poetry==1.7.1

WORKDIR /abi_challenge

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-root --without dev

# Stage 2: Runtime
FROM python:3.10-slim-buster

WORKDIR /abi_challenge

COPY --from=builder /abi_challenge .

ENV PATH="/abi_challenge/.venv/bin:$PATH"

COPY backend_app/ ./backend_app

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "--host=0.0.0.0", "--port=8000", "backend_app.src.app:app" ]