# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview
This repository contains a Remotion project for creating educational videos about big cats. The project includes two video formats:
1. BigCatsExplainer - A detailed 20-second landscape video (1920x1080)
2. BigCatsShort - A 32-second portrait video for social media (1080x1920)

## Project Structure
```
├── index.tsx              # Entry point with registerRoot() and Composition definitions
├── Root.tsx               # (optional) Can define compositions here
├── components/            # React components for video scenes
│   ├── BigCatsExplainer.tsx # Main detailed video component
│   ├── BigCatsShort.tsx    # Social media format component
│   └── FadeIn.tsx          # Animation helper component
├── public/                # Media assets (voiceovers, music)
├── out/                   # Rendered videos
├── package.json           # Project dependencies and scripts
└── generate-*.ts/js       # Scripts for AI voiceover/music generation
```

## Common Commands

### Development
```bash
# Start Remotion Studio for preview/editing
npm run start

# Render the BigCatsExplainer video
npm run build
```

### Voiceover Generation
```bash
# Generate full-length voiceovers for detailed video
npx ts-node generate-voiceover.ts

# Generate short voiceovers for social media video
npx ts-node generate-voiceover-short.ts

# Alternative JavaScript versions
node gen-short-vo.js
```

### Music Generation
```bash
# Generate background music
npx ts-node generate-music.ts

# Generate short-format background music
node gen-music-short.js
```

## Git Workflow and Version Control

### Commit Practices
As you work on this project, it's essential to maintain a clean Git history with meaningful commits:

1. **Make frequent, focused commits**: Commit changes as you complete logical units of work
2. **Write clear commit messages**: Use descriptive messages that explain what changed and why
3. **Group related changes**: Keep commits focused on a single concept or feature
4. **Push regularly**: Push commits to GitHub to ensure work is backed up

### Example Commit Messages
```
# Good commit messages
feat: add new cheetah facts to BigCatsExplainer
fix: resolve audio sync issue in BigCatsShort
refactor: optimize cat data structure for better performance
docs: update CLAUDE.md with voiceover generation instructions
```

### Branch Strategy
- Work on the `main` branch for simplicity in this project
- Create feature branches only for experimental work
- Always pull latest changes before starting work
- Push changes frequently to maintain backup

### Backup Process
The repository is configured to push to GitHub automatically. Ensure you:
1. Commit changes with `git add .` and `git commit -m "descriptive message"`
2. Push with `git push origin main`
3. Verify commits appear on GitHub

This ensures all work is safely backed up and can be recovered if needed.

## Architecture Overview

### Video Composition System
The project uses Remotion's Composition API to define multiple video formats:
- `BigCatsExplainer`: Detailed educational content with animated cards
- `BigCatsShort`: Fast-paced social media content with quick facts

Both compositions share data from the same cat information source but present it differently based on format requirements.

### Animation System
Animations are implemented using Remotion's hooks:
- `useCurrentFrame()`: Tracks animation progress
- `useVideoConfig()`: Accesses video dimensions and timing
- `interpolate()`: Maps frame numbers to visual properties
- `Sequence`: Manages timing for individual elements

### Media Integration
The project integrates AI-generated voiceovers and music:
- Voiceovers generated via ElevenLabs API
- Multiple voice files organized by video format
- Background music tracks for different contexts
- Audio components synchronized with visual elements

### Data Structure
Cat information is stored as structured data objects containing:
- Name and scientific classification
- Descriptive information
- Interesting facts
- Visual styling information
- Associated media files

## Key Components

### BigCatsExplainer.tsx
Main detailed video component featuring:
- Animated entrance sequences for each cat
- Information cards with scientific details
- Fun facts highlighted in special containers
- Synchronized voiceover playback
- Background sound effects

### BigCatsShort.tsx
Social media optimized component with:
- Rapid sequence of cat facts
- Large emoji visuals
- Simplified information presentation
- Subscribe call-to-action
- Different timing and pacing

## Voiceover & Audio System
Voiceovers are generated using ElevenLabs API with a custom voice:
- Separate scripts for full and short formats
- Pre-generated MP3 files stored in public/ directory
- Automatic synchronization with visual elements
- Background music tracks for atmosphere

## Best Practices

1. **Component Organization**: Related functionality grouped in components/
2. **Data Consistency**: Shared cat information across video formats
3. **Media Management**: Pre-generated assets stored in public/
4. **Script Organization**: Generation scripts separated by function
5. **Version Control**: All generated assets tracked in Git
6. **Regular Commits**: Commit and push frequently to maintain backup
7. **Descriptive Messages**: Use clear commit messages for project history

## Files Modified in This Project

- `index.tsx` - Entry point with composition definitions
- `components/BigCatsExplainer.tsx` - Main video component
- `components/BigCatsShort.tsx` - Social media format component
- `package.json` - npm scripts and dependencies
- `generate-*.ts/js` - Voiceover/music generation scripts
- `public/` - Media assets directory
- `out/` - Rendered video output

## Useful Links
- Remotion docs: https://www.remotion.dev/docs
- Remotion Studio: Local server for preview/editing
- ElevenLabs API: https://docs.elevenlabs.io/api-reference