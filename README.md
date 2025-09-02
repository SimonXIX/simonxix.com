# simonxix.com website

This repository is the Flask application for my website at simonxix.com along with Docker Compose and Nginx configuration for running the application in development and production.

## Docker Compose

To run the application in development mode, run:

    docker compose up -d --build

To take the service down, run:

    docker compose down

To run in production mode, run:

    docker compose -f docker-compose.prod.yml up -d --build

## Nginx

The Nginx configuration provided is indicative but should be sufficient for running the application as localhost. Obviously for production you'd want to provide your own configuration with, at a minimum, the domain name of the server and SSL configuration.

## onion service

The production Docker Compose configuration also provides an [onion service](https://community.torproject.org/onion-services/) version of the website. This uses [torservers' Onionize](https://github.com/torservers/onionize-docker) container to automatically exposes other selected Docker containers as onion services. It uses a 'faraday' network to only expose services on that internal network outwards to the Tor network. A separate version of Nginx labelled onion-nginx exposes the website on that internal network.

To output the onion address that has been assigned, run the command:

    docker exec onionize cat /var/lib/tor/onion_services/<ONIONSERVICE_NAME>/hostname

(in our case): 

    docker exec onionize cat /var/lib/tor/onion_services/onion-nginx/hostname

In production, I run this command as a cron job and output the result to ./web/content/onion.md. The Flask application then reads that Markdown file and builds HTML with the address as a variable.
