FROM python:3.9-buster
# Update current packages
RUN apt-get update && apt-get upgrade -y --no-install-recommends

# Create app directories
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache

# Copy app code
COPY dashboard /opt/app/dashboard
WORKDIR /opt/app

# Install app dependencies
COPY requirements.txt start.sh /opt/app/
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

# Create user and add ownership
RUN useradd -d /home/day0 -m -s /bin/bash day0
RUN chown -R day0 /opt/app
USER day0
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/start.sh"]