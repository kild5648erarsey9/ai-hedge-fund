"""FastAPI backend for AI Hedge Fund application."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown events."""
    print("Starting AI Hedge Fund backend...")
    yield
    print("Shutting down AI Hedge Fund backend...")


app = FastAPI(
    title="AI Hedge Fund API",
    description="Backend API for the AI Hedge Fund application.",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": "0.1.0"}


@app.get("/", tags=["root"])
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the AI Hedge Fund API"}
