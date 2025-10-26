StealthScribe GPT: The AI Writing Twin
StealthScribe is a proof-of-concept web application for a forensic-grade AI that analyzes a user's writing to construct a bespoke "AI Writing Twin." It can then generate new text that is indistinguishable from the user's own authentic voice, designed to be undetectable by AI detection software.

This repository contains a fully interactive front-end prototype and the conceptual back-end logic, making it a complete portfolio piece demonstrating full-stack application design.

Features
Phase I: Authorial Signature Analysis: Users can paste their writing into the application, which then performs a (simulated) forensic analysis to extract key linguistic markers.

Phase III: Calibrated Generation: Generate new text based on a prompt and a desired tone, using the user's unique Authorial Signature Model.

Aegis Rating: Each piece of generated text receives a real-time (simulated) "Aegis Rating" to score its authenticity and undetectability.

Interactive UI: A clean, modern, and responsive user interface built with Tailwind CSS.

Tech Stack
This project is structured as a modern web application to demonstrate a full-stack architecture.

Front-End (index.html)
HTML5: For the core structure of the application.

Tailwind CSS: For modern, responsive, utility-first styling.

Vanilla JavaScript: To handle all user interactions, state management, and simulate API calls to the back-end. No frameworks were used, to keep the code accessible and universally runnable.

Back-End (main.py)
Python 3: The language of choice for AI and data processing.

FastAPI: A modern, high-performance web framework for building APIs. The main.py file contains a complete, runnable FastAPI server that defines the core logic.

Pydantic: Used for data validation and modeling within the FastAPI application.

How to View & Use
1. The Interactive Web App
No installation is needed!

Download the index.html file from this repository.

Open the file in any modern web browser (like Chrome, Firefox, or Safari).

The application is fully interactive and runs completely in your browser.

2. The Back-End Server
To run the conceptual Python server (optional):

Ensure you have Python 3.7+ installed.

Install the necessary libraries:

pip install fastapi "uvicorn[standard]"

Navigate to the project directory in your terminal and run the server:

uvicorn main:app --reload

Project Structure
index.html: The main, self-contained front-end application. This is the user-facing part of the project.

main.py: The conceptual back-end API server. It contains the "secret sauce" and business logic for analysis and generation.

README.md: You are here! This file explains the project.
