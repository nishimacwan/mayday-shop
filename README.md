# MAYDAY Store

A tiny demo storefront built for a hackathon. It is a single FastAPI app that
serves a self-contained web shop: a small catalog of home goods with drawn SVG
visuals, a working in-page cart, and a health check endpoint. Everything runs in
Docker.

## What is inside

- **app.py** - the FastAPI app. The homepage HTML, styles, product data, and
  cart logic all live in this one file. There is also a `/health` endpoint.
- **requirements.txt** - the Python dependencies (FastAPI and Uvicorn).
- **Dockerfile** - builds the app image on top of `python:3.12-slim`.
- **docker-compose.yml** - builds and runs the app, mapping a host port to the
  container.

## Running it

You need Docker installed. From this folder, run:

```bash
docker compose up --build
```

Then open the shop in your browser:

- Store: http://localhost:8080
- Health check: http://localhost:8080/health

The compose file maps host port **8080** to the container's port **8000**. If
you would rather use plain `http://localhost` (port 80), change the `ports` line
in `docker-compose.yml` to `"80:8000"`, as long as nothing else on your machine
is using port 80.

To stop it:

```bash
docker compose down
```

## Running without Docker

Handy while editing. This serves on port 8000 and reloads when you save:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Notes

- The cart is entirely in-page JavaScript. There is no backend cart and no real
  checkout, so nothing is ever charged.
- Product images are drawn with inline SVG, so there are no external image files.

## License

Released under the MIT License. See [LICENSE](LICENSE).
