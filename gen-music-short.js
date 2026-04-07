const fs = require('fs');
const path = require('path');

const ELEVENLABS_API_KEY = 'sk_1f8128e22437b6316e3488098b1caeff0f48390c5b661c25';

const dir = 'public/music';
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

async function generateMusic() {
  console.log('Generating upbeat background music for short...');

  try {
    const res = await fetch('https://api.elevenlabs.io/v1/music/generate', {
      method: 'POST',
      headers: {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
      },
      body: JSON.stringify({
        prompt: 'Upbeat energetic electronic music, fast tempo, YouTube shorts style, trending, exciting',
        duration: 35,
        model: 'eleven_holiday_v1',
      }),
    });

    if (!res.ok) {
      const err = await res.text();
      console.error('Error:', err);
      return;
    }

    const buffer = await res.arrayBuffer();
    fs.writeFileSync(path.join(dir, 'shorts-bg.mp3'), Buffer.from(buffer));
    console.log('Saved: public/music/shorts-bg.mp3');
  } catch (e) {
    console.error('Error:', e.message);
  }
}

generateMusic();
