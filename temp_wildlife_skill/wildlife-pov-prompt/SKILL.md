---
name: wildlife-pov-prompt
description: >
  Generate cinematic POV wildlife video prompts optimized for AI video generators
  (Google Flow, Emu Video, Hunyuan, Kling, Runway, Pika). Use this skill whenever
  the user wants to create animal POV videos, wildlife documentary prompts, nature
  content for TikTok/Reels/Shorts, or asks about any animal behaving in a realistic
  scenario. Also triggers for: fixing broken AI video prompts (wrong camera angle,
  third-person drift, unwanted animals appearing, POV lost mid-clip), adding sound
  design to wildlife clips, sanitizing prompts blocked by content filters, or building
  a multi-block narrative sequence for any animal. Works for any species — ground,
  aerial, aquatic, arboreal, desert, polar. Always use this skill when an animal and
  a video generator are both mentioned in the same request.
---

# Wildlife POV Prompt System — Master Skill

This skill generates professional AI video prompts for wildlife POV content using
the v3 Narrative State Engine. Every sequence has a real story arc, species-authentic
behavior, and is optimized for the target generator.

---

## WORKFLOW OVERVIEW

```
Step 1 → Species Profile      (Module B)
Step 2 → Scenario Seed        (Module C)
Step 3 → 6-Block Prompts      (Module D)
Step 4 → Generator Tuning     (Module E)
Step 5 → Sound Design         (Module F)
Step 6 → Fix & Sanitize       (only if needed)
```

Read the reference files as needed:
- `references/species-profiles.md` — locomotion, sensory modes, interaction vocabularies
- `references/scenarios.md` — 8 scenario types with species compatibility matrix
- `references/generator-rules.md` — prompt structure rules per generator
- `references/sound-design.md` — audio layering guides per block type
- `references/fixes.md` — solutions for common generator failures

---

## MODULE B — SPECIES PROFILE

Before writing any prompts, lock a species profile. Extract from
`references/species-profiles.md` or build from scratch:

```
- Locomotion signature: gait, speed, body oscillation, pause behavior
- Primary sensory mode: vision / scent / vibration / electroreception
- Social role in this sequence: solitary / worker / dominant / juvenile / injured
- Primary drive: hunger / shelter / territorial / maternal / threat-response
- Threat response: fight / flee / freeze / display / camouflage
- Interaction vocabulary: 5–6 species-specific micro-behaviors
```

**This profile is locked. All 6 blocks must remain consistent with it.**

Population density rule:
- Solitary species → 0–2 other individuals visible
- Social mammals → 3–15
- Eusocial (ants, mole-rats) → mass colony density

---

## MODULE C — SCENARIO SEED

Select ONE scenario that creates genuine narrative tension across all 6 blocks.
The animal must have a goal, face an obstacle, and reach a resolution.

| Code | Scenario | Tension source |
|------|----------|----------------|
| S1 | Hunger hunt | Prey detected, pursued, lost or caught |
| S2 | Predator/threat intrusion | Threat enters space — fight/flee/freeze decision |
| S3 | Rival encounter | Conspecific challenges territory or resources |
| S4 | Maternal protection | Young or eggs threatened |
| S5 | Environmental threat | Flood, collapse, heat, drought mid-sequence |
| S6 | Failed mission | Animal attempts and fails — must adapt |
| S7 | Injured state | Compromise affects all behavior throughout |
| S8 | Territory mapping | Establishing or re-marking known space |
| S9 | Human world encounter | Tourist vehicle, fence, road, building, boat |

For S9 (human world) — this is the strongest viral scenario. Real-world elements
(named vehicles, tourists, infrastructure) ground the render in recognizable reality
and dramatically increase viewer engagement.

Output: scenario code + 2-sentence description of how it unfolds across 6 blocks.

---

## MODULE D — 6-BLOCK PROMPT STRUCTURE

Each block MUST:
1. Open with the animal's **current state** (what changed since last block)
2. Describe **one primary action** that advances the scenario
3. Include **one species-authentic micro-behavior** from the profile
4. Describe **one environmental detail** that reacts to the action
5. Close with a **state change** — what is now different

### Block roles:

| Block | Role | Key requirement |
|-------|------|-----------------|
| B01 | Setup image | Surface/habitat prep, harness attachment if POV, natural light |
| B02 | Inciting event | Scenario begins, first stimulus perceived |
| B03 | Rising tension | Something unexpected complicates the approach |
| B04 | Crisis point | Highest intensity — the decisive moment |
| B05 | Behavioral response | Physiological aftermath — real post-event biology |
| B06 | Resolution | Honest outcome — animal does not always succeed |

### POV vs third-person

**POV (camera mounted on animal):**
- Specify: camera weight, mount location, FOV, fps
- Body visibility rule: 5–10% of animal's own body at bottom of frame always
- Frame moves ONLY from body motion — no independent rotation
- Underground: LED only, no surface light
- See `references/generator-rules.md` for POV anchor phrases per generator

**Third-person (standard wildlife documentary):**
- Specify: camera distance, angle, movement (static/tracking/drone)
- Subject positioning: center frame for Hunyuan, flexible for others
- Always name time of day and lighting

---

## MODULE E — GENERATOR TUNING

Read `references/generator-rules.md` for full rules. Quick reference:

| Generator | Prompt style | Sweet spot | Key anchor |
|-----------|-------------|------------|------------|
| Google Flow | Long cinematic description + timestamps | 200–400 words | Repeat POV anchor 3x |
| Emu Video | Short punchy present-tense sentences | 60–100 words | "GoPro footage from camera strapped to..." |
| Hunyuan | Natural language, 5-step structure | 120–200 words | Subject + Action + Surroundings + Camera + Style |
| Kling | Layered detail, multiple depth planes | 150–250 words | Describe foreground/mid/background separately |
| Runway | Action-first, cinematic language OK | 100–200 words | Lead with the motion, then environment |
| Pika | Simple and direct | 40–80 words | One action per prompt maximum |

---

## MODULE F — SOUND DESIGN

Each block needs a layered sound design. See `references/sound-design.md`.

Core principle: **Silence before impact = 3x the emotional force.**

Standard layer structure:
1. Ambient bed (constant, low)
2. Movement sounds (footsteps, wingbeats, water)
3. Behavioral sounds (species-specific)
4. Event sounds (impact, splash, contact)
5. Atmosphere close (fade to near-silence for resolution)

All sounds free from Freesound.org. Search terms provided per scenario in
`references/sound-design.md`.

---

## COMMON FAILURES & FIXES

Read `references/fixes.md` for full solutions. Quick reference:

| Problem | Cause | Fix |
|---------|-------|-----|
| POV lost → third-person | Generator defaults to wildlife doc mode | Add POV anchor at top + middle + end of prompt |
| Unwanted second animal | Training data associates species + location with social scenes | Add explicit exclusion: "Zero other [species] in frame at any point" |
| Sync glitch / copy-paste animal | Generator mirrors subject cheaply | Split confrontation into two clips, cut at moment of contact |
| Content filter block | Keywords: carcass, dead, blood, strike | Replace with: feeding site, food resource, contact moment |
| Wrong species | Generic description matched wrong animal | Name subspecies specifically + add 3 physical details |
| Lighting wrong for time of day | Time of day not stated | State exact light condition in every block |
| Camera drifts mid-clip | POV anchor only at start | Repeat anchor phrase at midpoint of long prompts |

---

## BLOCK TEMPLATE (copy for each block)

```
[GENERATOR ANCHOR LINE]

Subject: [species + physical details relevant to this moment]

Action: [primary action broken into physical mechanics — what moves,
         which direction, at what speed, in what sequence]

Micro-behavior: [one species-authentic behavior from profile vocabulary]

Environment: [one detail that physically reacts to the action]

State change: [what is now different — carry this forward to next block]

Camera: [position, angle, movement, stabilization]
Style: [lighting, color palette, aesthetic]
Negative: [what must not appear]

[technical spec: resolution, fps, aspect ratio, duration]
```

---

## QUICK START

For a new request:
1. Identify species → load or build profile
2. Select scenario → confirm with user
3. Generate B01–B06 using block template
4. Apply generator tuning for the user's tool
5. Add sound design layer
6. If user reports a failure → consult fixes reference

For an existing prompt that is broken:
1. Identify which block and which failure type
2. Consult `references/fixes.md`
3. Rebuild only the failing block using the fix + block template
4. Test language: paste fix reason inline so user understands the change
