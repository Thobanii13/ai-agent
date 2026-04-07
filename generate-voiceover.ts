import { writeFileSync, mkdirSync, existsSync } from "fs";

const ELEVENLABS_API_KEY = "sk_1f8128e22437b6316e3488098b1caeff0f48390c5b661c25";
const VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"; // Roger voice (user's custom voice)
const MODEL_ID = "eleven_multilingual_v2";

const catVoiceovers = [
  {
    id: "lion",
    text: "The Lion, known as the King of the Jungle. These majestic cats are the only cats that live in social groups called prides. Their powerful roar can be heard up to 5 miles away.",
  },
  {
    id: "tiger",
    text: "The Tiger is the largest and strongest big cat, weighing up to 680 pounds. Each tiger has a unique stripe pattern, like a human fingerprint. No two tigers look alike.",
  },
  {
    id: "leopard",
    text: "The Leopard is known for its incredible climbing ability and beautiful rosette-patterned fur. They can carry prey twice their weight up into trees to keep it safe from scavengers.",
  },
  {
    id: "jaguar",
    text: "The Jaguar is the largest wild cat in the Americas, with the strongest bite pound-for-pound. Unlike other big cats, they absolutely love swimming and hunting in water.",
  },
  {
    id: "cheetah",
    text: "The Cheetah is the fastest land animal on Earth, reaching speeds up to 70 miles per hour. Unlike other big cats, they cannot roar. Instead, they chirp like birds!",
  },
  {
    id: "snow-leopard",
    text: "The Snow Leopard, called the Ghost of the Mountains, is adapted to survive in the harsh high-altitude mountains of Central Asia. They are incredibly elusive and rarely seen.",
  },
  {
    id: "cougar",
    text: "The Cougar, also known as the Mountain Lion or Puma, is an excellent jumper. They can leap up to 20 feet vertically in a single bound. They are found across North and South America.",
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
          stability: 0.5,
          similarity_boost: 0.75,
          style: 0.3,
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
  const dir = "public/voiceover/big-cats";
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
  writeFileSync(`${dir}/${cat.id}.mp3`, audioBuffer);
  console.log(`Saved: ${dir}/${cat.id}.mp3`);
}

async function generateAll() {
  console.log("Generating voiceovers for Big Cats video...\n");
  for (const cat of catVoiceovers) {
    await generateVoiceover(cat);
  }
  console.log("\nAll voiceovers generated successfully!");
}

generateAll().catch(console.error);
