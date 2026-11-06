# Counter: A Little Horology Museum

A small desktop app built with [Flet](https://flet.dev) (Python). It looks like
a luxury watch dial: near-black background, muted gold lines, and a large
serif numeral. it is a tiny museum about watches.

The numeral at the top is a counter from **0 to 9**. Each number is a "room" in
the museum, a page about one part of horology. Press **+** or **-** and the
page fades from one topic to the next.

| # | Page |
|---|------|
| 0 | History |
| 1 | Tradition |
| 2 | Watch Strap |
| 3 | Watch Case |
| 4 | Crown |
| 5 | Movement |
| 6 | Complications |
| 7 | Mainspring & Escapement |
| 8 | Fun Facts |
| 9 | Hello There |

---

## Core features

- **Counter that loops 0-9.** Pressing **+** at 9 wraps to 0, and pressing
  **-** at 0 wraps to 9.
- **Ten text pages**, each with a gold serif title and 2-4 short paragraphs
  about watches. All the text lives in one list (`PAGES`) at the top of the
  code, so it is easy to edit.
- **Smooth transitions.** The numeral rolls like a date wheel. The page text
  cross-fades using Flet's `AnimatedSwitcher`.
- **Watch-dial design.** A double frame (faint outer border, brighter inner
  border), faint concentric rings behind the text, a gold hairline under the
  header, and soft shadows.
- **Responsive layout.** Every size is a percentage of the window (header
  height, button size, text size, ring spacing), so the design scales when you
  resize the window.
- **Keyboard support.** Arrow keys (Up/Right = next, Down/Left = previous) work
  as well as the buttons.
- **Background music.** Erik Satie's *Gymnopédie No. 1* starts quietly the first
  time you go forward and keeps playing without restarting.
- **Geometry-centered numerals.** The digits are drawn as SVG outlines (taken
  from the Libre Caslon Display font), so every digit sits perfectly centered
  regardless of font metrics.

---

## Dependencies

- **Python 3.10 or newer**
- **[flet](https://pypi.org/project/flet/)** (tested with 1.1.1)
- **[flet-audio](https://pypi.org/project/flet-audio/)** (tested with 1.1.1)

Install both with:

```bash
pip install flet flet-audio
```

The two fonts (Libre Caslon Display and Lato Light) are downloaded
automatically from GitHub the first time the app runs, so **an internet
connection is needed on the first launch**. See "Offline use" below if you want
to avoid that.

---

## How to run

1. Put the code file (for example `counter.py`) in your project folder.
2. Create an `assets` folder next to it and place the music file inside:

   ```
   project/
   ├── counter.py
   ├── README.md
   └── assets/
       └── Erik_Satie_-_gymnopedies_-_la_1_ere._lent_et_douloureux.ogg
   ```

3. Install the dependencies (see above), then start the app:

   ```bash
   python counter.py
   ```

   Or, using the Flet command line:

   ```bash
   flet run counter.py
   ```

**Controls:** click the circular **-** / **+** buttons, or use the arrow keys.

**Offline use (optional):** download `LibreCaslonDisplay-Regular.ttf` and
`Lato-Light.ttf` into the `assets` folder, then change the two URLs in the
`FONTS` dictionary to just the file names.

**Settings you can tweak** (constants near the top of the code):

- `PLAY_ON_DECREASE`: set to `True` to also start the music from the **-** button.
- `PAGE_FADE_MS`: how long the page fade lasts.
- `BODY_SIZE_PCT`, `TITLE_SIZE_PCT`, `TEXT_WIDTH_PCT`: text size and width.

---

## Extra sources I found and used

- **Libre Caslon Display** (Google Fonts): used for the
  page titles and as the source of the SVG digit outlines.
  <https://fonts.google.com/specimen/Libre+Caslon+Display>
- **Lato Light** (Google Fonts, SIL Open Font License): used for body text.
  <https://fonts.google.com/specimen/Lato>
- **Erik Satie, *Gymnopédie No. 1* ("Lent et douloureux")**: the background
  recording.
- **Flet documentation** (<https://flet.dev/docs>): for the layout, animation
  (`AnimatedSwitcher`) and audio APIs.
- **Watch facts:** (<https://horopedia.org>) the page texts are written from general horology knowledge
  (history of timekeeping, Swiss and German watchmaking, case, crown, movement,
  complications and escapement basics).

---

## Easter eggs 

- **The shortcut.** Because the counter wraps around, pressing **-** on page 0
  jumps straight to the hidden note on page 9.

- **The music arrives late and quietly.** The Satie piece starts only after your
  first step forward, and at 30% volume, so it stays in the background.

---
