# Agri Market (minimal demo)

This is a small demo app that lists agricultural products and shows market prices. It's intentionally minimal so you can extend it.

Requirements
- Node.js (16+ recommended)

Setup (PowerShell)

1. Install dependencies:

   npm install

2. Seed the database:

   npm run seed

3. Start the server:

   npm start

Then open http://localhost:3000 in your browser.

What is included
- `server/` - Express server, SQLite DB and seed script
- `public/` - Static frontend (HTML/CSS/JS)

Images
- Product images uploaded from the frontend are stored in the `uploads/` folder and served at `/uploads/<filename>`.
- When using Docker with the provided `docker-compose.yml`, the project directory is mounted into the container so uploaded files are available locally.

Notes & next steps
- Add authentication for admin routes
- Improve UI and add product images
- Add filtering, sorting, and charts for price history
