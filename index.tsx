import { registerRoot, Composition } from "remotion";
import { BigCatsExplainer } from "./components/BigCatsExplainer";
import { BigCatsShort } from "./components/BigCatsShort";

export const registerCompositions = () => {
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
      <Composition
        id="BigCatsShort"
        component={BigCatsShort}
        durationInFrames={960}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};

registerRoot(registerCompositions);
