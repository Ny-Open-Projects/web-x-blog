FROM node:18-alpine AS base
WORKDIR /app
RUN corepack enable
COPY pnpm-workspace.yaml package.json tsconfig.base.json ./
COPY packages/shared/package.json packages/shared/
COPY apps/server/package.json apps/server/

FROM base AS deps
RUN --mount=type=cache,target=/root/.pnpm-store pnpm install --frozen-lockfile=false

FROM deps AS build
COPY packages/shared packages/shared
COPY apps/server apps/server
RUN pnpm --filter @lowcode/shared build && pnpm --filter @lowcode/server build

FROM node:18-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/apps/server/dist apps/server/dist
COPY --from=build /app/apps/server/node_modules apps/server/node_modules
COPY --from=build /app/packages/shared/dist packages/shared/dist
COPY --from=build /app/node_modules/.pnpm node_modules/.pnpm
EXPOSE 3000
CMD ["node", "apps/server/dist/main.js"]
