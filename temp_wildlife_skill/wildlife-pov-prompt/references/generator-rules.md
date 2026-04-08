# Generator Rules Reference

Prompt structure rules, anchor phrases, and failure prevention per generator.

---

## GOOGLE FLOW

**Responds to:** Long cinematic description, timestamp formatting, cinematographer language
**Sweet spot:** 200–400 words per block
**Weights:** First 40 words most heavily — anchor must be first

### POV Anchor (paste at very top of every POV prompt)
```
Helmet-cam style footage. Camera is a GoPro physically bolted to the upper back
of a [species] between its [mount location]. The camera is not handheld. The camera
does not float. The camera does not cut to an outside view. The only movement in
the frame comes from the animal's body moving. The animal's own [body feature]
is permanently visible at the bottom 8% of the frame. If those features are not
visible the shot is incorrect.
```

### Timestamp format (Flow follows this sequentially)
```
0:00–0:02 — [action description]
0:02–0:04 — [action description]
0:04–0:06 — [action description]
0:06–0:08 — [action description]
```

### Third-person drift prevention (add if POV breaks)
```
The [species] wearing this camera is never visible as a subject.
This is not a shot of the animal from outside.
This is the view from the animal's back.
```

### End every prompt with
```
[resolution/fps]. No stabilization. No cinematic grading. Field research footage. 16:9. [duration]. Uncut.
```

### Flow-specific failures
- **Rival appears in landing block**: Add "Zero other [species]. Landing zone completely
  empty before, during, and after landing. No other animals of any species."
- **Sync glitch (mirrored animal)**: Split clip at point of contact. Do not ask Flow
  to simulate the precise contact frame.

---

## EMU VIDEO (meta.ai)

**Responds to:** Short punchy present-tense action sentences
**Sweet spot:** 60–100 words — longer prompts dilute the POV anchor
**Weights:** First 30 words — POV anchor must be in first sentence

### POV Anchor
```
GoPro footage from camera strapped to [species]'s back.
```
That phrase alone activates body-cam mode. The most important line in the prompt.

### Structure
```
GoPro footage from camera strapped to [species]'s back. [Animal's body feature]
visible at bottom of frame always.

[Action in 3–5 short present-tense sentences. Each sentence = one physical event.]

[One exclusion sentence. One technical spec sentence.]

[Duration]. [Resolution]. No stabilization. 16:9.
```

### Three Emu rules
1. Lead with GoPro anchor — every time, no exceptions
2. Under 100 words — Emu weights the opening heavily, long prompts dilute
3. Present tense verbs — "Bird descending" not "the bird should be descending"

### Emu-specific failures
- **Goes third-person**: Add "This is not a shot of the bird. This is the view
  from the bird's back." at the end
- **Wrong species rendered**: Name the subspecies specifically + add 3 physical
  details (horn count, skin texture, body size)

---

## HUNYUAN VIDEO (Tencent)

**Responds to:** Natural language sentences, 5-step official structure
**Sweet spot:** 120–200 words
**Official formula:** Subject + Action + Surroundings + Camera + Style + Atmosphere

### Official 5-Step Structure
```
Subject: [species + physical details relevant to this moment in the narrative]

Action: [what the animal is doing — active verbs, physical mechanics,
         sequence of movements]

Surroundings: [environment — specific named location, ground texture,
               vegetation, other elements present]

Camera: [shot type, distance, angle, movement — "Wide stable shot,
         locked tripod" or "Static ground-level shot 15 metres away"]

Style: [lighting quality, time of day, color palette, aesthetic —
        "Late afternoon golden hour, warm amber light, wildlife documentary"]

Atmosphere: [mood, sensory details, what the viewer feels —
             "Complete silence broken only by distant engine sound fading"]
```

### Hunyuan-specific tips
- Name vehicles specifically: "Toyota Land Cruiser" not "car" or "vehicle"
- State time of day in every block — Hunyuan's lighting responds strongly
- End every block with "Wide stable shot. Locked tripod." to prevent drone drift
- Add "Continuous from Block 0X" for environment/lighting consistency
- Negative language works: "No other animals. No other birds of any species."
- Subject should be described at center of frame for cleaner animation

### Hunyuan-specific failures
- **Physics wrong**: Add more specific mechanical description — degrees of
  movement, which limb, which direction
- **Loses subject**: Redescribe subject physical details at start of next block
- **Inserts cut**: Add "Single continuous shot. No cuts. No edits." at end

---

## KLING AI

**Responds to:** Layered depth descriptions, multiple foreground/mid/background planes
**Sweet spot:** 150–250 words
**Strength:** Complex multi-subject scenes, physical interactions

### Structure
```
[Foreground description — what is closest to camera]
[Mid-ground description — primary subject and action]
[Background description — environment, atmosphere]
[Camera movement description]
[Lighting — Kling responds well to specific light quality language]
```

### Kling-specific tips
- Describe foreground, subject, and background as three separate layers
- Motion cues work well: "dust drifting slowly," "grass bending gently"
- Kling handles physical interactions between subjects better than other generators

---

## RUNWAY GEN-3

**Responds to:** Action-first structure, cinematic language is acceptable
**Sweet spot:** 100–200 words
**Strength:** Smooth motion, good at slow reveals

### Structure
```
[Primary action — lead with the motion, not the subject]
[Subject description — who is doing the action]
[Environment — where it is happening]
[Camera — angle and movement]
[Style and lighting]
```

### Runway-specific tips
- Lead with the verb: "A large bird descends steeply..." not "There is a bird..."
- Cinematic language does not cause problems in Runway (unlike Flow)
- Add "slow motion" only if you genuinely want it — Runway takes it literally

---

## PIKA

**Responds to:** Simple direct descriptions
**Sweet spot:** 40–80 words — shortest of all generators
**Rule:** One action per prompt maximum

### Structure
```
[Subject in one sentence]. [One action in one sentence].
[Environment in one sentence]. [Style in one sentence].
```

### Pika-specific tips
- Never give Pika more than one action — it will attempt all of them badly
- Works best for B01 (static image) and B06 (calm resolution)
- Use other generators for B04 (crisis) and B05 (confrontation)

---

## UNIVERSAL RULES (apply to all generators)

### POV Body Visibility Rule
In any POV prompt, add this line regardless of generator:
```
The animal's own [ruff feathers / beak tip / ears / snout / whiskers] are
visible at the bottom 8% of the frame at all times. If this body feature
disappears the shot is incorrect.
```

### Content Sanitization (when content filter blocks prompt)
Replace these terms:

| Blocked term | Safe replacement |
|--------------|-----------------|
| carcass | feeding site |
| dead animal | food resource |
| body cavity / flesh | the site / the resource |
| tearing / ripping | feeding behavior |
| blood | ground staining near feeding site |
| prey contact / strike | target contact moment |
| soiled / blood-covered | darkened from foraging |
| beak into flesh | feeding motion |
| bone crack | food manipulation |

Keep all camera physics language — generators never flag that.
Keep all behavioral description — lappet flushing, mantling, bill-wipe pass filters.

### Aspect ratio and resolution
Always end with: `1080p. 30fps. 16:9. [duration in seconds]. Uncut.`
