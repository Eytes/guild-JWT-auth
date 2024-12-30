ARG ALPINE_VERSION=3.21
ARG PYTHON_VERSION=3.13-alpine${ALPINE_VERSION}


FROM python:${PYTHON_VERSION} AS dependencies
WORKDIR /app
RUN pip install poetry
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry export --without-hashes --without dev -f requirements.txt --output requirements.txt


FROM python:${PYTHON_VERSION} AS runtime
WORKDIR /app
RUN addgroup --system appgroup &&  \
    adduser --no-create-home --disabled-password --system appuser --ingroup appgroup
USER appuser
COPY --from=dependencies /app/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./src ./src
