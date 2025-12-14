# Definiere ein Build-Argument "INSTALL_DEBUG" mit einem Standardwert "false"
#ARG INSTALL_DEBUG=false

FROM python:3.10-slim

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#for release
ARG DEBUGPY=false
ENV DEBUGPY=${DEBUGPY}
RUN [ "$DEBUGPY" = "true" ] && pip install --no-cache-dir debugpy || true

# setting main command for container startup
CMD ["python", "/app/run_env.py"]
