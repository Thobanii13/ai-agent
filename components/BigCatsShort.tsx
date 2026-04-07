import { useCurrentFrame, useVideoConfig, interpolate, Sequence, staticFile } from "remotion";
import { Audio } from "@remotion/media";

const cats = [
  {
    name: "LION",
    scientificName: "Panthera leo",
    funFact: "Their roar can be heard 5 miles away!",
    color: "#D4A574",
    emoji: "🦁",
    voiceoverFile: "lion-short.mp3",
  },
  {
    name: "TIGER",
    scientificName: "Panthera tigris",
    funFact: "Each has unique stripes like fingerprints!",
    color: "#E87848",
    emoji: "🐯",
    voiceoverFile: "tiger-short.mp3",
  },
  {
    name: "CHEETAH",
    scientificName: "Acinonyx jubatus",
    funFact: "Fastest land animal - 70 mph!",
    color: "#F5DEB3",
    emoji: "🐆",
    voiceoverFile: "cheetah-short.mp3",
  },
  {
    name: "LEOPARD",
    scientificName: "Panthera pardus",
    funFact: "Carries prey 2x their weight up trees!",
    color: "#C9B896",
    emoji: "🐆",
    voiceoverFile: "leopard-short.mp3",
  },
];

export const BigCatsShort = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  // Each cat gets about 7.5 seconds (225 frames)
  const catDuration = 225;

  return (
    <div
      style={{
        flex: 1,
        background: "linear-gradient(180deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%)",
        fontFamily: "system-ui, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* Background Music - plays throughout */}
      <Audio
        src={staticFile("music/shorts-bg.mp3")}
        volume={0.3}
        startFrom={0}
      />

      {/* Opening Title */}
      {frame < 30 && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <h1
            style={{
              fontSize: 120,
              color: "#fff",
              margin: 0,
              fontWeight: 900,
              letterSpacing: 8,
              textShadow: "0 0 40px rgba(255,200,100,0.5)",
            }}
          >
            BIG CATS
          </h1>
          <p
            style={{
              fontSize: 36,
              color: "#D4A574",
              marginTop: 20,
              fontWeight: 600,
            }}
          >
            Mind-Blowing Facts!
          </p>
        </div>
      )}

      {/* Cat segments */}
      {cats.map((cat, index) => {
        const startFrame = 30 + index * catDuration;
        const endFrame = startFrame + catDuration;

        if (frame < startFrame || frame >= endFrame) return null;

        const progress = (frame - startFrame) / catDuration;

        // Quick fade in
        const opacity = interpolate(progress, [0, 0.1], [0, 1]);
        const scale = interpolate(progress, [0, 0.15], [0.8, 1]);

        return (
          <Sequence key={cat.name} from={startFrame}>
            {/* Voiceover for this cat */}
            <Audio
              src={staticFile(`voiceover/big-cats-short/${cat.voiceoverFile}`)}
              volume={1}
              startFrom={0}
            />

            <div
              style={{
                position: "absolute",
                inset: 0,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                opacity,
                transform: `scale(${scale})`,
              }}
            >
              {/* Emoji */}
              <div
                style={{
                  fontSize: 200,
                  marginBottom: 20,
                  filter: "drop-shadow(0 20px 40px rgba(0,0,0,0.5))",
                }}
              >
                {cat.emoji}
              </div>

              {/* Name */}
              <h2
                style={{
                  fontSize: 90,
                  color: cat.color,
                  margin: 0,
                  fontWeight: 900,
                  letterSpacing: 4,
                  textShadow: `0 0 30px ${cat.color}66`,
                }}
              >
                {cat.name}
              </h2>

              {/* Scientific name */}
              <p
                style={{
                  fontSize: 28,
                  color: "#888",
                  marginTop: 10,
                  fontStyle: "italic",
                }}
              >
                {cat.scientificName}
              </p>

              {/* Fun fact box */}
              <div
                style={{
                  marginTop: 40,
                  background: "rgba(255,255,255,0.1)",
                  borderRadius: 20,
                  padding: "20 40",
                  border: `2px solid ${cat.color}`,
                }}
              >
                <p
                  style={{
                    fontSize: 32,
                    color: "#fff",
                    margin: 0,
                    fontWeight: 700,
                  }}
                >
                  💡 {cat.funFact}
                </p>
              </div>
            </div>
          </Sequence>
        );
      })}

      {/* Ending */}
      {frame >= 30 + cats.length * catDuration && (
        <div
          style={{
            position: "absolute",
            inset: 0,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          {/* Subscribe voiceover */}
          <Sequence from={30 + cats.length * catDuration}>
            <Audio
              src={staticFile("voiceover/big-cats-short/subscribe.mp3")}
              volume={1}
              startFrom={0}
            />
          </Sequence>

          <h1
            style={{
              fontSize: 80,
              color: "#fff",
              margin: 0,
              fontWeight: 900,
            }}
          >
            🔥 SUBSCRIBE
          </h1>
          <p
            style={{
              fontSize: 36,
              color: "#aaa",
              marginTop: 20,
            }}
          >
            For more animal facts!
          </p>
        </div>
      )}
    </div>
  );
};
