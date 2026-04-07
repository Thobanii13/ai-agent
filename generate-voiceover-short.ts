import { writeFileSync, mkdirSync, existsSync } from "fs";

const ELEVENLABS_API_KEY = "sk_1f8128e22437b6316e3488098b1caeff0f48390c5b661c25";
const VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"; // Roger voice
const MODEL_ID = "eleven_multilingual_v2";

// Short, punchy voiceovers for YouTube Short format
const shortVoiceovers = [
  {
    id: "lion-short",
    text: "The Lion! King of the Jungle. Their roar can be heard 5 miles away!",
  },
  {
    id: "tiger-short",
    text: "The Tiger! Largest big cat. Each has unique stripes like fingerprints!",
  },
  {
    id: "cheetah-short",
    text: "The Cheetah! Fastest land animal. 70 miles per hour!",
  },
  {
    id: "leopard-short",
    text: "The Leopard! Carries prey twice their weight up trees!",
  },
  {
    id: "subscribe",
    text: "Subscribe for more mind-blowing animal facts!",
  },
];

async function generateVoiceover(cat: { id: string; text: string }) {
  console.log(`Generating voiceover for ${cat.id}...`);

  const response = await fetch(
    `https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}`,
    {
      method: "POST",
      headers: {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        Accept: "audio/mpeg",
      },
      body: JSON.stringify({
        text: cat.text,
        model_id: MODEL_ID,
        voice_settings: {
          stability: 0.4,
          similarity_boost: 0.8,
          style: 0.5,
        },
      }),
    }
  );

  if (!response.ok) {
    const error = await response.text();
    console.error(`Error for ${cat.id}:`, error);
    throw new Error(`Failed to generate voiceover for ${cat.id}`);
  }

  const audioBuffer = Buffer.from(await response.arrayBuffer());
  const dir = "public/voiceover/big-cats-short";
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
  writeFileSync(`${dir}/${cat.id}.mp3`, audioBuffer);
  console.log(`Saved: ${dir}/${cat.id}.mp3`);
}

async function generateAll() {
  console.log("Generating voiceovers for Big Cats Short...\n");
  for (const cat of shortVoiceovers) {
    await generateVoiceover(cat);
  }
  console.log("\nAll voiceovers generated successfully!");
}

generateAll().catch(console.error);
