import { writeFileSync, mkdirSync, existsSync } from "fs";

const ELEVENLABS_API_KEY = "sk_1f8128e22437b6316e3488098b1caeff0f48390c5b661c25";

// ElevenLabs music generation endpoint
async function generateMusic() {
  console.log("Generating background music with ElevenLabs...");

  const response = await fetch(
    "https://api.elevenlabs.io/v1/music/generate",
    {
      method: "POST",
      headers: {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        Accept: "audio/mpeg",
      },
      body: JSON.stringify({
        prompt: "Calm ambient nature sounds, peaceful wildlife documentary style, gentle piano with soft strings, serene and relaxing",
        duration: 20,
        model: "eleven_holiday_v1",
      }),
    }
  );

  if (!response.ok) {
    const error = await response.text();
    console.error("Error:", error);
    // Try alternative endpoint
    console.log("Trying alternative music generation...");
    return generateMusicV2();
  }

  const audioBuffer = Buffer.from(await response.arrayBuffer());
  const dir = "public/music";
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
  writeFileSync(`${dir}/background.mp3`, audioBuffer);
  console.log("Saved: public/music/background.mp3");
}

async function generateMusicV2() {
  console.log("Trying v2 music generation...");

  const response = await fetch(
    "https://api.elevenlabs.io/v2/music/generate",
    {
      method: "POST",
      headers: {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        Accept: "audio/mpeg",
      },
      body: JSON.stringify({
        prompt: "Peaceful ambient nature music, soft gentle tones, wildlife documentary style, calming",
        duration: 20,
      }),
    }
  );

  if (!response.ok) {
    const error = await response.text();
    console.error("Music generation error:", error);
    throw new Error("Failed to generate music");
  }

  const audioBuffer = Buffer.from(await response.arrayBuffer());
  const dir = "public/music";
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
  writeFileSync(`${dir}/background.mp3`, audioBuffer);
  console.log("Saved: public/music/background.mp3");
}

generateMusic().catch(console.error);
