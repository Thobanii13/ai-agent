import { useCurrentFrame, useVideoConfig } from "remotion";
import { interpolate } from "remotion";

export const FadeIn = ({
  children,
  delay = 0,
  duration = 30,
}: {
  children: React.ReactNode;
  delay?: number;
  duration?: number;
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(
    frame - delay * fps,
    [0, duration],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <div style={{ opacity, display: "contents" }}>
      {children}
    </div>
  );
};
