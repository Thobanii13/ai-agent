import { useCurrentFrame, useVideoConfig, interpolate, Sequence, staticFile } from "remotion";
import { Audio } from "@remotion/media";
import { FadeIn } from "./FadeIn";

const cats = [
  {
    name: "Lion",
    scientificName: "Panthera leo",
    description: "Known for living in prides, their roar can be heard up to 5 miles away.",
    funFact: "The only cats that live in social groups called prides.",
    color: "#D4A574",
    voiceoverFile: "lion.mp3",
  },
  {
    name: "Tiger",
    scientificName: "Panthera tigris",
    description: "The largest and strongest big cat, weighing up to 680 pounds.",
    funFact: "Each tiger has a unique stripe pattern, like a fingerprint.",
    color: "#E87848",
    voiceoverFile: "tiger.mp3",
  },
  {
    name: "Leopard",
    scientificName: "Panthera pardus",
    description: "Known for their incredible climbing ability and rosette-patterned fur.",
    funFact: "They can carry prey twice their weight up into trees.",
    color: "#C9B896",
    voiceoverFile: "leopard.mp3",
  },
  {
    name: "Jaguar",
    scientificName: "Panthera onca",
    description: "The largest wild cat in the Americas, with the strongest bite pound-for-pound.",
    funFact: "Unlike other big cats, they love swimming and hunting in water.",
    color: "#C4A35A",
    voiceoverFile: "jaguar.mp3",
  },
  {
    name: "Cheetah",
    scientificName: "Acinonyx jubatus",
    description: "The fastest land animal, reaching speeds up to 70 mph.",
    funFact: "Cannot roar - they chirp like birds instead!",
    color: "#F5DEB3",
    voiceoverFile: "cheetah.mp3",
  },
  {
    name: "Snow Leopard",
    scientificName: "Panthera uncia",
    description: "Adapted to high-altitude mountains of Central Asia.",
    funFact: "Called the 'ghost of the mountains' due to their elusive nature.",
    color: "#B8C4CE",
    voiceoverFile: "snow-leopard.mp3",
  },
  {
    name: "Cougar",
    scientificName: "Puma concolor",
    description: "Also known as mountain lion or puma - an excellent jumper.",
    funFact: "Can leap up to 20 feet vertically!",
    color: "#A09080",
    voiceoverFile: "cougar.mp3",
  },
];

export const BigCatsExplainer = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const progress = frame / durationInFrames;

  return (
    <div
      style={{
        flex: 1,
        background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
        fontFamily: "system-ui, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* Sound Effects for each cat transition */}
      {cats.map((cat, index) => {
        const sfxFrame = index * 60; // Each cat appears at 2 second intervals
        return (
          <Sequence key={`sfx-${cat.name}`} from={sfxFrame}>
            <Audio
              src="https://remotion.media/whoosh.wav"
              volume={0.3}
              startFrom={0}
            />
          </Sequence>
        );
      })}

      {/* Title */}
      <div
        style={{
          position: "absolute",
          top: 80,
          left: 0,
          right: 0,
          textAlign: "center",
        }}
      >
        <h1
          style={{
            fontSize: 72,
            color: "#fff",
            margin: 0,
            fontWeight: 700,
            textShadow: "0 4px 20px rgba(0,0,0,0.5)",
          }}
        >
          The World of Big Cats
        </h1>
        <p
          style={{
            fontSize: 28,
            color: "#aaa",
            marginTop: 20,
          }}
        >
          Exploring the Majesty of Felines
        </p>
      </div>

      {/* Cat Cards with Voiceovers */}
      <div
        style={{
          position: "absolute",
          top: 280,
          left: 0,
          right: 0,
          bottom: 0,
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          alignItems: "flex-start",
          gap: 30,
          padding: "0 50px",
        }}
      >
        {cats.map((cat, index) => {
          const delay = index * 0.15;
          const entryFrame = interpolate(
            progress,
            [delay, delay + 0.15],
            [0, 1],
            { extrapolateRight: "clamp" }
          );

          const yOffset = interpolate(entryFrame, [0, 1], [100, 0]);
          const opacity = interpolate(entryFrame, [0, 0.3, 1], [0, 0.5, 1]);

          // Voiceover timing - starts when card appears
          const voiceoverStartFrame = index * 60;

          return (
            <div
              key={cat.name}
              style={{
                width: 280,
                background: `linear-gradient(145deg, ${cat.color}22, ${cat.color}11)`,
                borderRadius: 20,
                padding: 25,
                border: `1px solid ${cat.color}44`,
                transform: `translateY(${yOffset}px)`,
                opacity,
                boxShadow: `0 10px 40px ${cat.color}22`,
              }}
            >
              {/* Voiceover for this cat */}
              <Sequence from={voiceoverStartFrame}>
                <Audio
                  src={staticFile(`voiceover/big-cats/${cat.voiceoverFile}`)}
                  volume={1}
                />
              </Sequence>

              <div
                style={{
                  width: 60,
                  height: 60,
                  borderRadius: "50%",
                  background: cat.color,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: 28,
                  marginBottom: 15,
                }}
              >
                🐱
              </div>
              <h3
                style={{
                  fontSize: 28,
                  color: cat.color,
                  margin: "0 0 5px 0",
                  fontWeight: 700,
                }}
              >
                {cat.name}
              </h3>
              <p
                style={{
                  fontSize: 14,
                  color: "#888",
                  margin: "0 0 10px 0",
                  fontStyle: "italic",
                }}
              >
                {cat.scientificName}
              </p>
              <p
                style={{
                  fontSize: 16,
                  color: "#ccc",
                  margin: "0 0 15px 0",
                  lineHeight: 1.5,
                }}
              >
                {cat.description}
              </p>
              <div
                style={{
                  background: "#ffffff11",
                  borderRadius: 10,
                  padding: 12,
                }}
              >
                <p
                  style={{
                    fontSize: 14,
                    color: "#fff",
                    margin: 0,
                    fontWeight: 600,
                  }}
                >
                  💡 {cat.funFact}
                </p>
              </div>
            </div>
          );
        })}
      </div>

      {/* Footer */}
      <div
        style={{
          position: "absolute",
          bottom: 30,
          left: 0,
          right: 0,
          textAlign: "center",
          color: "#666",
          fontSize: 16,
        }}
      >
        Big cats are found across Asia, Africa, and the Americas | Most are threatened or endangered
      </div>
    </div>
  );
};
