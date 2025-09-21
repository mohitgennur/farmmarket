FROM node:18-alpine
WORKDIR /app

# Install production dependencies
COPY package.json package-lock.json* ./
RUN npm install --production

# Copy app source
COPY . .

# Seed DB (best-effort)
RUN node server/seed.js || true

EXPOSE 3000
CMD ["node", "server/index.js"]
