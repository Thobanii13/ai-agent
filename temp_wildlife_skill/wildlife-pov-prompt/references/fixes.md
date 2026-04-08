# Fixes Reference

Solutions for every known AI video generator failure mode.
Organized by problem type. Each fix includes the cause, the fix, and
copy-paste language to add to the prompt.

---

## POV FAILURES

### Problem: POV lost — generator switches to third-person

**Cause:** Generator defaults to wildlife documentary mode. Training data for
the animal in that environment is overwhelmingly third-person.

**Fix level 1 — Add triple anchor:**
```
[TOP OF PROMPT]
GoPro-style footage recorded by a camera strapped to a [species]'s back.
The camera never leaves the animal. The animal's [body feature] are always
visible at the bottom of the frame. There is no outside shot of the animal
at any point.

[MIDDLE OF PROMPT — after the main action]
The camera is still mounted on the animal. The frame only moves when the
animal's body moves.

[END OF PROMPT]
This is not a shot of the animal from outside. This is the view from the
animal's back.
```

**Fix level 2 — Use GoPro trigger word:**
Add the single word "GoPro" to the opening line. This activates body-cam
mode in most generators faster than any technical description.

**Fix level 3 — Change the scenario framing:**
Instead of describing what the animal sees, describe what the camera
operator (the animal) is doing. Use camera operator language:
"The camera operator turns 40 degrees right" not "the animal looks right."

---

### Problem: Camera drifts mid-clip — POV holds for 2 seconds then breaks

**Cause:** POV anchor is only at the start. Generator loses the constraint
as the clip progresses.

**Fix:** Repeat the anchor at the midpoint of long prompts.
For Google Flow specifically, add an anchor line inside the timestamp
for the second half of the clip:
```
0:04–0:06 — [Camera reminder: still mounted on animal's back, body
             features visible at bottom of frame] [action continues...]
```

---

## UNWANTED SUBJECTS

### Problem: Second animal keeps appearing (rival, duplicate, mirrored)

**Cause:** Generator's training data associates the species + environment +
specific action (landing, feeding, confrontation) with a social scene.
It autocompletes with another animal.

**Fix — Explicit exclusion at the start:**
```
Only one [species] exists in this entire clip. No other [species].
No other birds/animals of any species. The [location] is completely
empty of other animals. This animal is completely alone.
```

**Fix — Reframe the moment:**
The touchdown/contact moment is the highest-risk frame for generator to
inject a second animal. Split the clip: end one clip just before the
moment, start the next after. Never ask the generator to simulate the
precise risk frame.

---

### Problem: Synchronized movement / copy-paste glitch

**Cause:** Generator mirrors the subject as the cheap solution to rendering
two similar large animals in frame simultaneously.

**Fix:** Do not show both animals in the same frame during movement.
Structure the confrontation so one animal is still while the other moves.
Only have both moving simultaneously during the brief contact moment —
then cut immediately after.

---

## CONTENT FILTER BLOCKS

### Problem: Prompt blocked — "may violate policies about harmful content"

**Cause:** Keywords trigger the generator's content filter regardless of
documentary context. Most common triggers in wildlife prompts:

| Blocked | Replace with |
|---------|-------------|
| carcass | feeding site |
| dead animal / body | food resource |
| flesh / body cavity | the site / the resource |
| tearing / ripping | feeding behavior |
| blood | ground staining near feeding site |
| prey contact / strike impact | target contact moment |
| soiled feathers | feathers darkened from foraging |
| bone crack | food manipulation |
| kill | successful hunt |
| stab / pierce | contact |

**Rule:** Keep all camera physics language — never flagged.
Keep behavioral description (lappet flushing, mantling, bill-wipe) — passes clean.
Remove any language that describes injury, death, or bodily harm regardless of context.

---

## PHYSICS FAILURES

### Problem: Wrong landing physics — too light, too fast, no weight

**Cause:** Generator lacks sufficient mechanical description.

**Fix:** Break landing into 5 separate physical events:
```
1. Wings fully extend simultaneously — feather tips enter left and right
   frame edge at exactly the same moment
2. Frame tilts back [X] degrees as body goes vertical for braking
3. Legs extend downward out of frame
4. Ground contact — single hard downward jolt, frame drops [X] degrees
   then bounces back
5. Frame shakes [X] seconds then stops completely — dust at frame edges
```

---

### Problem: Movement looks wrong for the species — too smooth / too fast / wrong gait

**Cause:** Generator defaults to generic quadruped or biped movement.

**Fix:** Name the locomotion signature explicitly:
```
[Species] locomotion: [describe the specific gait with physical mechanics]
Example: "Heavy bouncing trot, each step compresses the body downward
visibly, dust rises from each footfall, 1 step per 0.7 seconds"
```

---

## ENVIRONMENT FAILURES

### Problem: Wrong environment — wrong vegetation, wrong light, wrong region

**Fix:** Name the specific location:
```
Instead of: "savanna"
Use: "Open East African savanna, Kenya — dry cracked earth, short sparse
     tawny grass 15cm tall, red-ochre soil, three flat-topped acacia trees
     40 metres back, low horizon"
```

---

### Problem: Lighting changes between blocks — inconsistency breaks continuity

**Fix:** Lock the light condition at the start of each block and state it
explicitly every time. Use time-of-day + direction + quality:
```
"Late afternoon golden hour, warm amber light from the left,
long shadows extending right across the ground"
```
Don't assume the generator remembers the previous block's lighting.

---

## SUBJECT FAILURES

### Problem: Wrong species rendered

**Cause:** Common name matched a different animal or a different region's variant.

**Fix:** Use Latin name + 3 physical identifiers:
```
Instead of: "rhinoceros"
Use: "Black rhinoceros (Diceros bicornis), two front horns, prehensile
     pointed upper lip, deeply wrinkled dark grey skin, smaller than
     white rhinoceros"
```

---

### Problem: Animal anatomy wrong — extra limbs, wrong body proportions

**Fix:** Add explicit body description at the start of each block where the
animal is visible:
```
"[Species] with [limb count] legs, [body shape], [distinctive feature],
[scale reference — e.g., 'approximately the size of a large dog']"
```

---

## CONTINUITY FAILURES

### Problem: Environment resets between blocks — different terrain, different light

**Cause:** Generator treats each block as a new scene.

**Fix:** Add "Continuation of previous scene" or "Continuous from Block 0X"
at the start of each block. Repeat 2–3 key environment details from the
previous block. Never change vegetation type, soil color, or time of day
between adjacent blocks.

---

### Problem: Narrative details introduced in earlier blocks are forgotten

**Fix:** State the world-state explicitly at the start of each affected block:
```
"Current state: [what has changed since the last block — e.g., 'The rival
has retreated 2 metres and is now standing sideways. The animal has not fed.']"
```
This forces the generator to render the continued state, not a fresh start.
