import { Composition } from "remotion";
import { BigCatsExplainer } from "./components/BigCatsExplainer";

export const compositions = () => {
  return (
    <>
      <Composition
        id="BigCatsExplainer"
        component={BigCatsExplainer}
        durationInFrames={600}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
