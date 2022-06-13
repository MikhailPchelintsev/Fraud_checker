ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=10 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
WORKDIR /app

RUN groupadd -r app && useradd --no-log-init -r -g app app && chown -R app /app

RUN apt-get update \
 && apt-get install --no-install-recommends -y curl build-essential \
 && rm -rf /var/lib/apt/lists/*

# install poetry
ENV POETRY_VERSION=1.1.6
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# install runtime dependencies
COPY --chown=app:app poetry.lock pyproject.toml VERSION $PYSETUP_PATH/
RUN cd $PYSETUP_PATH \
 && poetry run pip install -U pip \
 && poetry install --no-dev

# copy models
COPY --chown=app:app model /app/model

COPY --chown=app:app fraud_checker /app/fraud_checker

# copy configuration files
COPY --chown=app:app Makefile pyproject.toml VERSION /app/
COPY --chown=app:app settings /app/settings

# bump version from git tags
RUN poetry version $(cat VERSION)

USER app

CMD ["python", "-m", "fraud_checker"]

# layer with dev dependencies installed
FROM production as development

USER root
COPY Makefile .editorconfig flake8.tests.ini setup.cfg /app/
COPY tests /app/tests
RUN cd $PYSETUP_PATH/ && poetry install

ENTRYPOINT [ "" ]
CMD [ "" ]
