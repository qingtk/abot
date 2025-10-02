# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

**abot** is a dual-interface AI bot project built with Node.js and Google's Generative AI (Gemini). It provides both a web-based rich text editor interface and command-line text generation capabilities.

## Development Commands

### Setup
```bash
npm install
```

### Running the Application
```bash
# Main CLI text generation
npm start
# or using bun
bun main.js

# Image generation (requires billing on Google AI)
node imagen.js

# Direct API testing via curl
bash rest.sh
```

### Environment Requirements
- Set `GEMINI_API_KEY` environment variable with your Google AI API key
- Node.js with ES modules support (project uses `"type": "module"`)

## Architecture Overview

### Core Components

**main.js** - Primary CLI interface that uses Google's Gemini 2.5 Flash model for text generation. Demonstrates basic content generation with hardcoded prompts.

**imagen.js** - Image generation module using Google's Imagen 4.0 model. Generates multiple images from text prompts and saves them as PNG files. Note: Requires billing account for Google AI.

**index.html** - Web interface combining:
- Quill.js rich text editor for content creation
- Puter.com AI integration for chat functionality  
- URL parameter-based prompt input
- Uses GPT-5-nano model through Puter's API

**rest.sh** - Shell script demonstrating direct REST API calls to Google's Generative Language API using curl.

### Technology Stack
- **Runtime**: Node.js with ES modules
- **AI Provider**: Google Generative AI (@google/genai package)
- **Frontend**: Vanilla HTML/JS with Quill.js editor
- **Alternative AI**: Puter.com API integration

### Data Flow
1. **CLI Mode**: Direct prompt → Gemini API → Console output
2. **Web Mode**: URL params → Puter AI → Quill editor content
3. **Image Mode**: Text prompt → Imagen API → PNG file output

### Key Integration Points
- Environment-based API key management
- Multiple AI model support (Gemini, GPT through Puter)
- File system output for generated images
- Web-based content editing with AI assistance

## API Dependencies
- Google Generative AI API (requires `GEMINI_API_KEY`)
- Puter.com AI services (web interface)
- Quill.js CDN for rich text editing