# MAYDAY Store

A tiny demo storefront built for a hackathon. It is a single FastAPI app that
serves a self-contained web shop: a small catalog of home goods with drawn SVG
visuals, a working in-page cart, and a health check endpoint. Everything runs in
Docker.

## Features

- A calm, responsive storefront with a muted palette and one restrained accent color.
- A catalog of six home goods, each with a drawn SVG visual, a name, a short description, and a price.
- Product visuals drawn with inline SVG and CSS, so there are no external image files.
- A working cart built with in-page JavaScript: add items, adjust quantities, and see a live count on the cart icon.
- A slide-out cart panel that lists your items with prices, a running total, item removal, and a close button.
- A top nav bar with the store name, a visual sign-in link, and the cart.
- A system status badge that turns green when the app is healthy.
- A `/health` endpoint that returns `{"status": "ok"}` for simple uptime checks.
- Fully self-contained in a single `app.py`, ready to build and run with Docker.

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
