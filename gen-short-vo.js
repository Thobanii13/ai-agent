const fs = require('fs');
const path = require('path');

const ELEVENLABS_API_KEY = 'sk_1f8128e22437b6316e3488098b1caeff0f48390c5b661c25';
const VOICE_ID = 'CwhRBWXzGAHq8TQ4Fs17';

const voiceovers = [
  { file: 'lion-short.mp3', text: 'The Lion! King of the Jungle. Their roar can be heard 5 miles away!' },
  { file: 'tiger-short.mp3', text: 'The Tiger! Largest big cat. Each has unique stripes like fingerprints!' },
  { file: 'cheetah-short.mp3', text: 'The Cheetah! Fastest land animal. 70 miles per hour!' },
  { file: 'leopard-short.mp3', text: 'The Leopard! Carries prey twice their weight up trees!' },
  { file: 'subscribe.mp3', text: 'Subscribe for more mind-blowing animal facts!' },
];

const dir = 'public/voiceover/big-cats-short';
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

async function generateOne(index) {
  if (index >= voiceovers.length) {
    console.log('All done!');
    return;
  }

  const v = voiceovers[index];
  console.log(`Generating ${v.file}...`);

  try {
    const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`, {
      method: 'POST',
      headers: {
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
      },
      body: JSON.stringify({
        text: v.text,
        model_id: 'eleven_multilingual_v2',
        voice_settings: {
          stability: 0.4,
          similarity_boost: 0.8,
          style: 0.5,
        },
      }),
    });

    if (!res.ok) {
      const err = await res.text();
      console.error('Error:', err);
    } else {
      const buffer = await res.arrayBuffer();
      fs.writeFileSync(path.join(dir, v.file), Buffer.from(buffer));
      console.log(`Saved: ${v.file}`);
    }
  } catch (e) {
    console.error('Error:', e.message);
  }

  // Next one
  setTimeout(() => generateOne(index + 1), 1000);
}

generateOne(0);
