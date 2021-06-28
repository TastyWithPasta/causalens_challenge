from node:buster

# Install basic HTTP server
RUN npm install -g http-server

# Create app directories
RUN mkdir -p /opt/app
WORKDIR /opt/app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy app files and build app
COPY . .
RUN npm run build

EXPOSE 8080
CMD ["http-server", "dist"]

#TODO: Separate build and prod images

# # Create user and add ownership TODO: Just for the prod image
# RUN useradd -d /home/day0 -m -s /bin/bash day0
# RUN chown -R day0 /opt/app
# USER day0