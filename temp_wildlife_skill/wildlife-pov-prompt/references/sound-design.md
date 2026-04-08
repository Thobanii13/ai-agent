# Sound Design Reference

Audio layering guides for each block type and scenario.
All sources free from Freesound.org unless noted.

---

## CORE PRINCIPLE

**Silence before impact = 3x emotional force.**
Build silence in the block BEFORE the crisis. The impact in the crisis block
hits harder because of what preceded it.

### Emotional arc template
```
B02 — Peaceful → building
B03 — Tension rising / something heard but not seen
B04 — LOUD impact OR complete silence (depending on scenario)
B05 — Aftermath sounds → settling
B06 — Slow fade to near nothing
```

---

## LAYER STRUCTURE (apply to every block)

```
Layer 1 — Ambient bed       (constant, low volume, never stops)
Layer 2 — Movement sounds   (footsteps, wingbeats, water — tied to action)
Layer 3 — Behavioral sounds (species-specific — tied to micro-behavior)
Layer 4 — Event sounds      (impact, contact, environmental event — peak moment)
Layer 5 — Atmosphere close  (fade for resolution blocks)
```

---

## BY HABITAT

### Savanna / Open Ground
```
Ambient bed:      "African plains ambience" or "savanna wind dry"
                  Low constant — distant insects, faint breeze, no drama
Movement:         "footsteps dry dirt" or "footsteps cracked earth"
                  Match weight to animal — heavy for rhino, light for cheetah
Behavioral:       Varies by species (see species section below)
Event:            "body impact thud" (confrontation) or "vehicle engine diesel" (S9)
Resolution close: "savanna ambience fade" — reduce all layers to near zero
```

### Underground / Burrow
```
Ambient bed:      Near silence — faint soil creak, no wind
Movement:         "soil scraping" or "digging earth soft"
Behavioral:       "small animal movement underground"
LED activation:   Subtle electronic click when LED turns on
Event:            "tunnel collapse rubble" (S5) or "impact muffled" (confrontation)
Resolution close: Complete silence
```

### Aerial
```
Ambient bed:      "high altitude wind clean" — thin, constant, not gusty
Movement:         "feather creak leather flex" (subtle), "wing flap large bird"
Behavioral:       Wind volume drops when head turns away from forward direction
                  Wind surges when bird accelerates out of thermal
Event:            "landing impact thud heavy" + "dust scatter dry rustle"
Resolution close: Wind reduces to faint — bird has settled
```

### Aquatic
```
Ambient bed:      "river ambient" or "underwater bubbles constant"
Movement:         "water displacement" or "splash entry"
Behavioral:       "crocodile infrasound low rumble" (near-inaudible bass)
Event:            "water surface breach explosive" or "splash impact"
Resolution close: "water settle lap" — surface calming
```

### Forest / Canopy
```
Ambient bed:      "tropical forest ambient" — birds, insects, wind in canopy
Movement:         "branch creak under weight" or "leaf rustle large"
Behavioral:       "primate vocalization" or "branch drag on wood"
Event:            "branch snap" or "impact thud with body weight"
Resolution close: Forest ambient fades slowly
```

### Cold / Polar
```
Ambient bed:      "polar wind constant" or "ice ambient howl low"
Movement:         "footsteps snow compact" or "penguin colony murmur"
Behavioral:       "penguin bray call" or "ice creak"
Event:            "blizzard surge" (S5) or "ice crack" (S5)
Resolution close: Wind drops to near silence
```

---

## BY SCENARIO

### S1 — Hunger Hunt
```
B02 detection:    Ambient only + single behavioral sound (sniff, scan)
B03 pursuit:      Movement sounds build in tempo with animal's speed
B04 strike:       Event sound (impact) — preceded by 1.5 seconds of silence
B05 aftermath:    If success: feeding sounds. If fail: breathing + movement retreat
B06 resolution:   Ambient bed only — whatever the outcome, the world continues
```

### S2 — Threat / Predator
```
B02 detection:    Single behavioral alert sound + ambient silence drops
B03 threat closes: Movement sounds from threat — louder per step
B04 response:     TOTAL SILENCE for 2 seconds before the event sound
B05 aftermath:    Rapid breathing, movement sounds, behavioral (flight or freeze)
B06 resolution:   Ambient slowly returns — threat is gone or resolved
```

### S3 — Rival Encounter
```
B02–B03:          Ambient + approach footsteps
B04 confrontation: Brief behavioral threat sound → SILENCE → event (contact)
                   Scramble sounds (fast irregular footsteps on ground)
B05 aftermath:     Behavioral (bill-wipe, panting, retreat steps)
B06 resolution:    Ambient returns, rival's retreat steps fade with distance
```

### S9 — Human World Encounter
```
B02 detection:    Distant diesel engine or machinery — off-screen
B03 vehicle/human appears: Engine sound + tire on gravel or road
B04 standoff:     Engine cuts → TOTAL SILENCE → animal behavioral sound
B05 withdrawal:   Engine restart → movement sounds → fading engine with distance
B06 resolution:   Engine fully gone → ambient returns to pre-encounter state
```

---

## BY SPECIES

### Vulture
```
Behavioral sounds: "bird wing feather creak subtle"
                   "forced exhalation hiss animal" (confrontation)
                   "beak scrape on rock" (bill-wipe)
                   "large bird footstep dirt" (ground walk)
```

### Rhinoceros
```
Behavioral sounds: "large animal snort exhale"
                   "heavy footstep dry earth"
                   "animal nasal breathing"
                   "brush against vegetation" (body press into grass)
```

### Crocodile
```
Behavioral sounds: "low frequency rumble infrasound" (throat vibration)
                   "water displacement slow"
                   "jaw close snap" (for strike moment)
```

### Scorpion
```
Behavioral sounds: "insect movement dry substrate subtle"
                   "sand grain shift" (each step)
                   "chitinous click faint" (claw movement)
Note: Keep all scorpion sounds extremely subtle — most should be near-inaudible
```

### Naked mole-rat
```
Behavioral sounds: "small rodent movement tunnel"
                   "soil scratching rapid"
                   "high frequency squeak brief" (alarm)
```

---

## FREESOUND.ORG SEARCH TERMS

| Sound needed | Search term |
|---|---|
| Savanna ambient | "african savanna ambience" or "dry grassland wind" |
| Polar wind | "arctic wind constant" or "blizzard ambient" |
| Feather sounds | "bird wing flap close" or "feather rustle large" |
| Heavy body thud | "body impact thud low" or "heavy fall soft" |
| Diesel engine | "diesel engine idle" or "4x4 vehicle idle" |
| Dry footsteps | "footsteps dirt dry" or "footsteps cracked earth" |
| Heavy footsteps | "elephant footstep" or "large animal walk" |
| Hiss animal | "animal hiss forced" or "reptile hiss" |
| Underground ambient | "cave ambient silence" or "underground silence" |
| Soil sounds | "digging earth soft" or "soil scraping" |
| Water ambient | "river ambient" or "stream gentle" |
| Forest ambient | "tropical forest birds insects" |

---

## MIXING RULES

1. Ambient bed sits at -18 to -20 dB — barely audible, never competing
2. Movement sounds sit at -12 to -14 dB — audible but not dominant
3. Behavioral sounds sit at -10 to -8 dB — clear but not sharp
4. Event sounds sit at -3 to 0 dB — full volume, peak of the sequence
5. Resolution fade: reduce all layers by 50% over the last 3 seconds of B06

Silence is an active choice. When in doubt, remove a layer rather than add one.
