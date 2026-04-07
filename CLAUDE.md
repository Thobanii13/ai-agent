# CLAUDE.md - Video Creation Guide with Remotion

## Overview
This file contains guidance for creating videos using Remotion (React-based video creation framework).

## Quick Start

### Running the Development Server
```bash
npm run start
# Opens at http://localhost:3000
```

### Building the Video
```bash
npm run build
# Renders to out/video.mp4
```

## Project Structure

```
├── index.tsx              # Entry point with registerRoot() and Composition definitions
├── Root.tsx               # (optional) Can define compositions here
├── components/            # React components for video scenes
│   └── BigCatsExplainer.tsx
├── remotion.config.js     # Configuration file
├── package.json           # Scripts: start, build
└── out/                   # Rendered videos
```

## Key Patterns

### 1. Defining Compositions
In Remotion v4+, define compositions inside a component passed to `registerRoot()`:

```tsx
import { registerRoot, Composition } from "remotion";
import { MyScene } from "./components/MyScene";

const App = () => {
  return (
    <>
      <Composition
        id="MyVideo"
        component={MyScene}
        durationInFrames={600}  // 20 seconds at 30fps
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};

registerRoot(App);
```

### 2. Using Animation Hooks
```tsx
import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";

const MyScene = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Animate based on frame number
  const opacity = interpolate(frame, [0, 30], [0, 1]);
  const scale = interpolate(frame, [0, 60], [0.5, 1], { extrapolateRight: "clamp" });

  return <div style={{ opacity, transform: `scale(${scale})` }}>Content</div>;
};
```

### 3. Key Hooks Available
- `useCurrentFrame()` - Get current frame number
- `useVideoConfig()` - Get fps, width, height, durationInFrames
- `interpolate()` - Map input values to output range
- `spring()` - Physics-based spring animation
- `delayRender()` / `continueRender()` - For async operations

### 4. Animation Patterns
Use `interpolate` for smooth animations:
```tsx
const progress = interpolate(frame, [startFrame, endFrame], [0, 1]);
const yOffset = interpolate(progress, [0, 1], [100, 0]);
const opacity = interpolate(progress, [0, 0.3, 1], [0, 0.5, 1], { extrapolateRight: "clamp" });
```

### 5. Text Animations
For typewriter effects and text reveals, load: `./rules/assets/text-animations-typewriter.tsx` from the remotion-best-practices skill.

## Common Issues & Solutions

### "useCurrentFrame() can only be called inside a component that was registered as a composition"
- **Cause**: Using the wrong file as entry point
- **Fix**: Ensure `registerRoot()` is in the file passed to `remotion render`

### "Cannot read properties of undefined (reading 'setVideoImageFormat')"
- **Cause**: Old v3 Config API in remotion.config.js
- **Fix**: Remove Config calls or use v4 approach - config is now minimal

### Bundle cache issues
- Remotion caches bundles. Delete `.cache` folder if needed.

## Configuration

### package.json scripts
```json
{
  "scripts": {
    "start": "remotion studio index.tsx --port 3000",
    "build": "remotion render index.tsx CompositionName out/video.mp4"
  }
}
```

### Custom render settings
Pass flags to override defaults:
```bash
remotion render index.tsx MyVideo out/video.mp4 --codec=h264 --quality=80
```

## Voiceover & Audio

To add AI voiceover, load the voiceover rule:
- See `./rules/voiceover.md` in remotion-best-practices skill for ElevenLabs TTS integration

## Best Practices

1. **Always use Composition component** - Don't call registerRoot() directly with a scene
2. **Define all compositions in one place** - Makes rendering easier
3. **Use interpolate for animations** - Cleaner than manual calculations
4. **Test with `npm run start` first** - Much faster than full renders
5. **Check the remotion-best-practices skill** - Has many specialized patterns for:
   - Charts, maps, Lottie animations
   - Subtitles, captions, SRT files
   - Sound effects, audio visualization
   - Transitions, 3D content

## Files Modified in This Project

- `index.tsx` - Entry point with composition definitions
- `components/BigCatsExplainer.tsx` - Main video component
- `package.json` - npm scripts
- `remotion.config.js` - Configuration (minimal in v4)

## Useful Links
- Remotion docs: https://www.remotion.dev/docs
- Remotion Studio: Local server for preview/editing
