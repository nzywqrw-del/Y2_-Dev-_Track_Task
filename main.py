import asyncio
import flet as ft
import flet_audio as fta


# ── Palette ───────────────────────────────────────────────────────────────
BASE_TOP = "#121214"
BASE_BOTTOM = "#0B0B0C"
GOLD = "#B89B5E"
GOLD_HI = "#D4BC8A"
IVORY = "#EDE8DF"
SHADOW = "#050506"
TEXT_BODY = "#B7B2A8"  # NEW: muted off-white for paragraphs

# Audio: the track lives in ./assets (see assets_dir in ft.run below).
# Set to True if you also want the music to start from the minus button.
PLAY_ON_DECREASE = False

# Used until the real window size is known (web / early desktop startup).
FALLBACK_WIDTH = 1000
FALLBACK_HEIGHT = 700

# Slow, deliberate easing. Flet has no custom cubic-bezier, so EASE_OUT_QUINT
# (0.23, 1, 0.32, 1) stands in for (0.22, 1, 0.36, 1).
EASE = ft.Animation(500, ft.AnimationCurve.EASE_OUT_QUINT)


FONT_SERIF = "Caslon"
FONT_BODY = "Lato"
FONTS = {
    FONT_SERIF: "https://raw.githubusercontent.com/google/fonts/main/ofl/librecaslondisplay/LibreCaslonDisplay-Regular.ttf",
    FONT_BODY: "https://raw.githubusercontent.com/google/fonts/main/ofl/lato/Lato-Light.ttf",
}


PAGES = [
    # 0 ──────────────────────────────────────────────────────────────────
    {
        "title": "History",
        "body": [
            "Long before the first mechanism, people read time from the sky. "
            "The moving shadow of a sundial marked the hours by day, while "
            "water clocks let a steady drip measure time through the night "
            "and on cloudy days.",
            "Weight-driven mechanical clocks appeared in European towers in "
            "the 14th century. The coiled spring, developed in the 15th, made "
            "portable timekeepers possible, and by the 16th century small "
            "clocks were being worn on a chain: the first pocket watches.",
            "Wristwatches were long considered jewellery for women. Soldiers "
            "in the early 1900s found them far easier to read than a pocket "
            "watch, and after the First World War the wristwatch became the "
            "everyday standard.",
        ],
    },
    # 1 ──────────────────────────────────────────────────────────────────
    {
        "title": "Tradition",
        "body": [
            "Swiss watchmaking took root in Geneva in the 16th century and "
            "spread into the Jura mountains, where farming families made "
            "watch parts through the long winters. Towns such as Le Locle, "
            "La Chaux-de-Fonds and the Vallée de Joux still carry that "
            "heritage.",
            "German watchmaking found its home in Glashütte, Saxony, where "
            "Ferdinand Adolph Lange founded the craft in 1845. Its makers are "
            "known for details like three-quarter plates and hand-engraved "
            "balance cocks.",
            "Skills were once guarded by guilds and passed on through long "
            "apprenticeships. Even today the finest watches are finished by "
            "hand: mirror-polished bevels, Geneva stripes and blued screws, "
            "much of it hidden behind the case back.",
        ],
    },
    # 2 ──────────────────────────────────────────────────────────────────
    {
        "title": "Watch Strap",
        "body": [
            "Leather is warm, classic and ages with the wearer, but it dislikes "
            "water. Metal bracelets in steel, titanium or gold are durable and "
            "versatile. Rubber shrugs off sweat and seawater, and a NATO strap "
            "is a woven nylon band that is light, cheap and easy to swap.",
            "Lug width is the gap between the two lugs, measured in "
            "millimetres, and it decides which straps fit. Common sizes run "
            "from 18 to 22 mm. Check yours before buying, and look for "
            "quick-release spring bars to make changes easy.",
            "Choose by occasion: slim leather for formal wear, a bracelet or "
            "rubber for sport, a NATO for casual days. A strap that tapers "
            "from the lugs toward the clasp usually sits more comfortably.",
        ],
    },
    # 3 ──────────────────────────────────────────────────────────────────
    {
        "title": "Watch Case",
        "body": [
            "Stainless steel is the most common case material for its "
            "toughness. Titanium is lighter, gold and platinum are precious, "
            "bronze develops a patina, and ceramic resists scratches "
            "remarkably well.",
            "Round is the classic shape, though square, rectangular and "
            "cushion cases have loyal followers. Diameters range from about "
            "34 mm in vintage dress watches to 40 mm and more in modern sports "
            "models. Lug-to-lug length often decides fit more than diameter.",
            "The crystal protects the dial. Acrylic is cheap and easy to "
            "polish, mineral glass is harder, and sapphire is the choice of "
            "most quality watches because it is extremely scratch-resistant.",
            "Water resistance is a pressure rating, not a diving guarantee. "
            "30 m means splashes only, 100 m suits swimming, and 200 m or more "
            "is for diving. Gaskets age, so have them tested regularly.",
        ],
    },
    # 4 ──────────────────────────────────────────────────────────────────
    {
        "title": "Crown",
        "body": [
            "The crown is the small knob on the side of the case. In a "
            "mechanical watch it winds the mainspring, and on nearly every "
            "model it sets the time and often the date.",
            "Pulled out to different positions, it engages different parts of "
            "the movement. A screw-down crown threads into the case like a "
            "tiny bolt and seals the watch against water. Rolex introduced "
            "the idea with the Oyster in 1926.",
            "Before the crown, watches were wound with a separate key. "
            "Keyless winding, developed by Adrien Philippe in the 1840s, "
            "made the crown the standard way to wind and set a watch.",
        ],
    },
    # 5 ──────────────────────────────────────────────────────────────────
    {
        "title": "Movement",
        "body": [
            "The movement is the engine of a watch. A mechanical movement is "
            "powered by a wound spring. A manual watch is wound by hand "
            "through the crown, while an automatic adds a rotor that swings "
            "with your wrist and winds the spring for you.",
            "A quartz movement uses a battery to make a tiny quartz crystal "
            "vibrate 32,768 times a second. Electronics count the vibrations "
            "and advance the hands. Quartz watches are accurate, affordable "
            "and low-maintenance, and reached the market in the late 1960s.",
            "Either way the job is the same: divide time into equal beats "
            "and move the hands to show them. A mechanical watch does it with "
            "gears and a balance wheel that typically beats three or four "
            "times every second.",
        ],
    },
    # 6 ──────────────────────────────────────────────────────────────────
    {
        "title": "Complications",
        "body": [
            "A complication is any function beyond hours, minutes and "
            "seconds. The more of them a watch has, the more intricate its "
            "movement must be.",
            "The everyday ones are a date window, a chronograph that works "
            "as a stopwatch, and a GMT hand that tracks a second time zone. "
            "A moon phase shows the lunar cycle, and a perpetual calendar "
            "knows month lengths and leap years, typically needing no "
            "correction until the year 2100.",
            "The tourbillon was patented by Abraham-Louis Breguet in 1801. "
            "It carries the escapement in a rotating cage to average out the "
            "effect of gravity on a pocket watch. Today it is mostly a "
            "showcase of craft.",
        ],
    },
    # 7 ──────────────────────────────────────────────────────────────────
    {
        "title": "Mainspring & Escapement",
        "body": [
            "A mechanical watch begins with the mainspring, a long coiled "
            "strip of metal inside a barrel. Winding stores energy in it, "
            "the way a compressed spring stores energy until released.",
            "Left alone, the spring would unwind in moments. The gear train, "
            "a series of wheels of different sizes, carries the energy "
            "toward the hands, while the escapement acts as a gatekeeper "
            "that lets it out in tiny, equal steps.",
            "At each step the escapement's pallet fork unlocks the escape "
            "wheel and gives the balance wheel a small push. The balance, "
            "with its hairspring, swings back and forth at a steady rate and "
            "sets the tempo. The tick you hear is the escapement catching "
            "the wheel again.",
        ],
    },
    # 8 ──────────────────────────────────────────────────────────────────
    {
        "title": "Fun Facts",
        "body": [
            "Quartz watches vibrate their crystal 32,768 times a second "
            "because that number is two to the power of fifteen. Electronics "
            "can halve it fifteen times to get one pulse per second.",
            "Watch advertisements almost always show the hands at about "
            "10:10. The symmetrical hands frame the brand name, and the "
            "shape looks like a smile.",
            "An Omega Speedmaster went to the Moon on the wrist of Buzz "
            "Aldrin in 1969.",
            "Patek Philippe's Calibre 89 pocket watch, made in 1989, "
            "contains 1,728 parts.",
        ],
    },
    # 9 ──────────────────────────────────────────────────────────────────
    {
        "title": "Hello There",
        "body": [
            "If you're reading this, I hope you enjoyed my little horology "
            "museum. If you skipped ahead, I'd encourage you to go back "
            "and visit every page. There's some fascinating stuff in there.",
            "I've gotten into watches recently, so they were the first thing "
            "that came to mind: a small museum made of a few lines of code. "
            "I hope the visit pleased you.",
            "By Noam Duval",
        ],
    },
]

# A safety check: the counter loops 0-9, so there must be exactly 10 pages.
assert len(PAGES) == 10, "PAGES needs exactly 10 entries (counter values 0-9)"

# Digit outlines from Libre Caslon Display (lining figures), y-up font units.
# Drawn as SVG so every digit has the same box and is centered by geometry,
# not by font metrics. Generated from the font file.
DIGIT_BOX_W = 550
DIGIT_BOX_H = 750
DIGIT_PATHS = {
    "0": (311, "M56 345Q56 246 90 163Q124 80 182 32Q241 -16 311 -16Q381 -16 440 32Q498 80 532 163Q566 246 566 345Q566 444 532 527Q498 610 440 658Q381 706 311 706Q241 706 182 658Q124 610 90 527Q56 444 56 345ZM311 694Q391 694 430 608Q470 522 470 345Q470 168 430 82Q391 -4 311 -4Q231 -4 192 82Q152 168 152 345Q152 522 192 608Q231 694 311 694Z"),
    "1": (176, "M41 9V0H312V9L220 17V712L215 714Q186 666 145 640Q104 615 40 607V600H143V17Z"),
    "2": (244, "M35 9 142 111Q345 304 345 490Q345 568 312 610Q278 651 216 651Q167 651 128 626Q89 602 65 557L56 562Q82 627 138 666Q193 706 259 706Q311 706 352 681Q393 656 416 612Q439 568 439 512Q439 444 396 374Q353 303 250 198L130 77H361Q390 77 404 86Q418 95 425 123L444 196L452 194L429 0H38Z"),
    "3": (256, "M319 544Q319 594 292 622Q265 651 219 651Q173 651 136 624Q100 596 77 546L68 550Q93 623 146 665Q198 707 265 707Q327 707 367 672Q407 636 407 581Q407 531 374 485Q340 439 279 405V401Q332 400 374 374Q417 348 441 304Q465 261 465 209Q465 148 433 96Q401 44 346 14Q290 -16 225 -16Q178 -16 136 0Q95 16 70 43Q46 70 46 101Q46 123 58 136Q70 149 89 149Q110 149 124 132Q138 115 155 69Q167 36 176 22Q184 8 195 3Q206 -2 228 -2Q296 -2 336 43Q375 88 375 166Q375 220 356 262Q337 304 303 328Q269 351 225 351Q192 351 165 342L162 352Q236 382 278 433Q319 484 319 544Z"),
    "4": (242, "M23 195 20 201 372 714 377 712V247H462V195H377V17L463 9V0H198V9L300 17V195ZM296 578 68 250 69 247H300V578Z"),
    "5": (242, "M224 453Q291 453 342 426Q392 399 420 350Q448 300 448 235Q448 166 417 108Q386 51 332 18Q277 -16 212 -16Q166 -16 126 0Q85 17 60 44Q35 71 35 101Q35 123 48 136Q60 149 81 149Q106 149 117 132Q128 116 138 83Q151 42 169 20Q187 -2 227 -2Q287 -2 324 51Q361 104 361 190Q361 280 319 332Q277 384 204 384Q150 384 105 349L101 350L149 690H410Q419 702 429 723L436 721L404 615H153L129 438Q161 446 182 450Q203 453 224 453Z"),
    "6": (263, "M54 243Q54 348 95 440Q136 533 211 604Q286 674 387 714L391 706Q282 640 226 558Q169 477 159 370Q182 395 216 409Q250 423 290 423Q372 423 422 366Q472 310 472 217Q472 149 445 96Q418 43 370 14Q322 -16 261 -16Q198 -16 152 16Q105 48 80 106Q54 165 54 243ZM379 199Q379 295 346 347Q314 399 255 399Q226 399 200 386Q174 374 157 352Q146 284 146 219Q146 118 179 57Q212 -4 267 -4Q319 -4 349 50Q379 105 379 199Z"),
    "7": (227, "M423 685Q335 480 295 372Q255 265 180 23Q174 4 160 -6Q147 -16 132 -16Q114 -16 105 -6Q96 5 96 22Q96 38 103 51L378 615H74Q53 585 38 547L31 550L85 722L90 720Q90 710 92 690H417Z"),
    "8": (264, "M472 190Q472 133 444 86Q415 39 366 12Q316 -16 257 -16Q202 -16 156 8Q110 33 83 74Q56 116 56 166Q56 225 96 274Q136 323 211 355Q144 391 112 434Q79 478 79 533Q79 582 104 622Q128 661 171 684Q214 706 267 706Q315 706 354 688Q392 669 414 636Q436 604 436 563Q436 512 402 469Q369 426 310 400Q394 353 433 302Q472 252 472 190ZM370 560Q370 622 340 658Q311 694 261 694Q213 694 184 662Q155 629 155 576Q155 521 190 480Q225 439 301 405Q334 431 352 471Q370 511 370 560ZM132 170Q132 88 167 42Q202 -4 264 -4Q324 -4 361 36Q398 76 398 140Q398 204 356 253Q314 302 222 348Q178 325 155 280Q132 234 132 170Z"),
    "9": (248, "M457 453Q457 351 416 259Q376 167 301 96Q226 25 124 -16L120 -8Q224 57 281 142Q338 228 352 338Q330 313 296 299Q262 285 222 285Q140 285 90 340Q39 396 39 488Q39 553 66 604Q93 656 142 685Q190 714 252 714Q347 714 402 644Q457 574 457 453ZM132 506Q132 412 164 360Q197 309 256 309Q285 309 310 321Q336 333 354 356Q365 417 365 486Q365 590 336 646Q306 702 250 702Q195 702 164 650Q132 598 132 506Z"),
}

# ── Proportions (every size below is a percentage) ───────────────────────
# Header height is a share of the window height.
HEADER_PCT_OF_HEIGHT = 10

# Everything inside the header is a share of the header height.
BUTTON_PCT = 58          # circular button diameter
GLYPH_PCT = 18           # +/- icon length
NUMERAL_PCT = 40         # numeral height (the digit itself, not the line box)
WHEEL_W_PCT = 84         # numeral window width
WHEEL_H_PCT = 58         # numeral window height
GAP_PCT = 42             # space between buttons and numeral
HAIRLINE_PCT = 1.25      # 1px-style stroke (never drawn thinner than 1px)
HEADER_SHADOW_BLUR_PCT = 63
HEADER_SHADOW_DROP_PCT = 18

# The panel is a share of the window's shorter side.
PANEL_MARGIN_PCT = 3
FRAME_INSET_PCT = 1.5
PANEL_RADIUS_PCT = 0.25
PANEL_SHADOW_BLUR_PCT = 7.5
PANEL_SHADOW_DROP_PCT = 3
TOP_SHADE_PCT = 7
RING_COUNT = 11
RING_STEP_PCT = 10       # each ring grows by this much of the shorter side

# NEW: text proportions (also a share of the window's shorter side).
TEXT_WIDTH_PCT = 76      # maximum width of the text column
TITLE_SIZE_PCT = 4.4     # title font size
BODY_SIZE_PCT = 2.0      # paragraph font size
BODY_LINE_HEIGHT = 1.75  # line spacing multiplier for paragraphs
TEXT_GAP_PCT = 1.9       # space between title, rule and paragraphs
RULE_WIDTH_PCT = 7       # short gold line under the title
PAGE_FADE_MS = 600       # NEW: fade time when the page changes


def vertical_gradient(top=BASE_TOP, bottom=BASE_BOTTOM):
    return ft.LinearGradient(
        begin=ft.Alignment.TOP_CENTER,
        end=ft.Alignment.BOTTOM_CENTER,
        colors=[top, bottom],
    )


def button_style(hair):
    """Circle, 1px gold border, transparent fill, soft gold fill on hover."""
    return ft.ButtonStyle(
        shape=ft.CircleBorder(),
        padding=ft.Padding.all(0),
        animation_duration=500,
        bgcolor={
            ft.ControlState.HOVERED: ft.Colors.with_opacity(0.08, GOLD),
            ft.ControlState.FOCUSED: ft.Colors.with_opacity(0.08, GOLD),
            ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
        },
        overlay_color=ft.Colors.TRANSPARENT,
        side={
            ft.ControlState.HOVERED: ft.BorderSide(hair, GOLD_HI),
            ft.ControlState.FOCUSED: ft.BorderSide(hair * 2, GOLD_HI),
            ft.ControlState.DEFAULT: ft.BorderSide(hair, GOLD),
        },
    )


async def main(page: ft.Page):
    url = "Erik_Satie_-_gymnopedies_-_la_1_ere._lent_et_douloureux.ogg"
    page.title = "Counter"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = BASE_BOTTOM
    page.fonts = FONTS  # NEW: register the title and body fonts

    
    audio = fta.Audio(
        src=url,
        autoplay=False,
        volume=0.30,
        balance=0,
    )
    page.services.append(audio)

    music = {"started": False}

    async def play_music():
        if not music["started"]:
            music["started"] = True
            await audio.play()


    state = {
        "value": 0,
        "front": 0,
        "digit_h": 40.0,
        "short": float(min(FALLBACK_WIDTH, FALLBACK_HEIGHT)),
        "hair": 1.0,
    }

    # ── Numeral: two stacked layers that slide like a date wheel ─────────
    def digit_image(value):
        cx, path = DIGIT_PATHS[value]
        x0 = cx - DIGIT_BOX_W / 2
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{x0:g} -730 {DIGIT_BOX_W} {DIGIT_BOX_H}">'
            f'<path transform="scale(1,-1)" fill="{GOLD_HI}" d="{path}"/></svg>'
        )
        h = state["digit_h"]
        return ft.Image(
            src=svg.encode("utf-8"),
            width=h * DIGIT_BOX_W / DIGIT_BOX_H,
            height=h,
            fit=ft.BoxFit.CONTAIN,
        )

    def numeral_layer(value, opacity):
        return ft.Container(
            left=0,
            right=0,
            top=0,
            bottom=0,
            alignment=ft.Alignment.CENTER,
            opacity=opacity,
            offset=ft.Offset(0, 0),
            animate_opacity=EASE,
            animate_offset=EASE,
            content=digit_image(value),
        )

    layers = [numeral_layer("0", 1), numeral_layer("0", 0)]

    switcher = ft.AnimatedSwitcher(
        content=ft.Container(),  # empty until show_page() runs the first time
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=PAGE_FADE_MS,
        reverse_duration=int(PAGE_FADE_MS * 0.6),
        switch_in_curve=ft.AnimationCurve.EASE_OUT_QUINT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        expand=True,
    )

    page_refs = {"column": None, "title": None, "rule": None, "paragraphs": []}

    def build_page(index):
        data = PAGES[index]

        # Blank page (like page 9): no text, just an empty container, so only
        # the dial background shows.
        if not data["title"] and not data["body"]:
            page_refs.update(column=None, title=None, rule=None, paragraphs=[])
            return ft.Container()

        title = ft.Text(data["title"], text_align=ft.TextAlign.CENTER)
        rule = ft.Container(bgcolor=ft.Colors.with_opacity(0.6, GOLD))
        paragraphs = [
            ft.Text(p, text_align=ft.TextAlign.CENTER) for p in data["body"]
        ]
        column = ft.Column(
            controls=[title, rule, *paragraphs],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,  # only kicks in on very small windows
        )
        page_refs.update(
            column=column, title=title, rule=rule, paragraphs=paragraphs
        )
        style_page()  # give the new controls their sizes right away
        return column

    def style_page():
        """Size and style the text on screen from the window's shorter side."""
        column = page_refs["column"]
        if column is None:  # blank page, nothing to style
            return
        short = state["short"]
        gap = short * TEXT_GAP_PCT / 100

        column.width = short * TEXT_WIDTH_PCT / 100
        column.spacing = gap

        title_size = short * TITLE_SIZE_PCT / 100
        page_refs["title"].style = ft.TextStyle(
            size=title_size,
            color=GOLD_HI,
            font_family=FONT_SERIF,
            letter_spacing=title_size * 0.03,
        )

        rule = page_refs["rule"]
        rule.width = short * RULE_WIDTH_PCT / 100
        rule.height = state["hair"]
        rule.margin = ft.Margin(left=0, top=gap * 0.3, right=0, bottom=gap * 0.3)

        for paragraph in page_refs["paragraphs"]:
            paragraph.style = ft.TextStyle(
                size=short * BODY_SIZE_PCT / 100,
                color=TEXT_BODY,
                font_family=FONT_BODY,
                height=BODY_LINE_HEIGHT,
            )

    def show_page():
        """Swap the content area to the page for the current counter value."""
        switcher.content = build_page(state["value"])
        switcher.update()


    step_lock = asyncio.Lock()

    async def step(change):
        async with step_lock:
            state["value"] = (state["value"] + change) % 10
            outgoing = layers[state["front"]]
            incoming = layers[1 - state["front"]]
            state["front"] = 1 - state["front"]

            show_page()

            incoming.animate_offset = None
            incoming.animate_opacity = None
            incoming.content = digit_image(str(state["value"]))
            incoming.offset = ft.Offset(0, 0.7 * change)
            incoming.opacity = 0
            incoming.update()
            await asyncio.sleep(0.03)

            incoming.animate_offset = EASE
            incoming.animate_opacity = EASE
            incoming.offset = ft.Offset(0, 0)
            incoming.opacity = 1
            outgoing.offset = ft.Offset(0, -0.7 * change)
            outgoing.opacity = 0
            incoming.update()
            outgoing.update()

    async def increase(e=None):
        await step(1)
        await play_music()

    async def decrease(e=None):
        await step(-1)
        if PLAY_ON_DECREASE:
            await play_music()

    async def on_key(e: ft.KeyboardEvent):
        if e.key in ("Arrow Up", "Arrow Right"):
            await increase()
        elif e.key in ("Arrow Down", "Arrow Left"):
            await decrease()

    page.on_keyboard_event = on_key

    wheel = ft.Container(
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack(controls=layers),
    )

    minus_glyph = ft.Container(bgcolor=GOLD_HI)
    plus_bar_h = ft.Container(bgcolor=GOLD_HI)
    plus_bar_v = ft.Container(bgcolor=GOLD_HI)
    plus_glyph = ft.Stack(
        alignment=ft.Alignment.CENTER, controls=[plus_bar_h, plus_bar_v]
    )

    def round_button(glyph, tooltip, on_click):
        return ft.OutlinedButton(
            content=ft.Container(content=glyph, alignment=ft.Alignment.CENTER),
            tooltip=tooltip,
            on_click=on_click,
        )

    minus_button = round_button(minus_glyph, "Decrease", decrease)
    plus_button = round_button(plus_glyph, "Increase", increase)

    header_row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[minus_button, wheel, plus_button],
    )

    header = ft.Container(
        left=0,
        right=0,
        top=0,
        alignment=ft.Alignment.CENTER,
        gradient=vertical_gradient(),
        content=header_row,
    )

    rings = [ft.Container() for _ in range(RING_COUNT)]
    ring_stack = ft.Stack(alignment=ft.Alignment.CENTER, controls=rings)

    top_shade = ft.Container(
        left=0,
        right=0,
        top=0,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_CENTER,
            end=ft.Alignment.BOTTOM_CENTER,
            colors=[ft.Colors.with_opacity(0.45, SHADOW), ft.Colors.TRANSPARENT],
        ),
    )
    frame = ft.Container()

    content_layer = ft.Container(
        left=0,
        right=0,
        top=0,
        bottom=0,
        alignment=ft.Alignment.CENTER,
        content=switcher,
    )


    panel = ft.Container(
        left=0,
        right=0,
        top=0,
        bottom=0,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        gradient=vertical_gradient("#141416", "#0D0D0F"),
        content=ft.Stack(
            controls=[
                ft.Container(
                    left=0,
                    right=0,
                    top=0,
                    bottom=0,
                    alignment=ft.Alignment.CENTER,
                    content=ring_stack,
                ),
                top_shade,
                frame,
                content_layer,  # NEW: drawn last, so the text sits on top
            ]
        ),
    )

    def current_size():
        win = getattr(page, "window", None)
        win_w = page.width or getattr(win, "width", None) or FALLBACK_WIDTH
        win_h = page.height or getattr(win, "height", None) or FALLBACK_HEIGHT
        return win_w, win_h

    def apply_scale(e=None):
        win_w, win_h = current_size()
        short = min(win_w, win_h)

        # header-relative sizes
        hhight = win_h * HEADER_PCT_OF_HEIGHT / 100
        hair = max(1.0, hhight * HAIRLINE_PCT / 100)

        header.height = hhight
        header.border = ft.Border(
            bottom=ft.BorderSide(hair, ft.Colors.with_opacity(0.35, GOLD))
        )
        header.shadow = ft.BoxShadow(
            blur_radius=hhight * HEADER_SHADOW_BLUR_PCT / 100,
            spread_radius=0,
            color=ft.Colors.with_opacity(0.55, SHADOW),
            offset=ft.Offset(0, hhight * HEADER_SHADOW_DROP_PCT / 100),
        )
        header_row.spacing = hhight * GAP_PCT / 100

        btn = hhight * BUTTON_PCT / 100
        for b in (minus_button, plus_button):
            b.width = btn
            b.height = btn
            b.style = button_style(hair)

        glyph = hhight * GLYPH_PCT / 100
        minus_glyph.width = glyph
        minus_glyph.height = hair
        plus_glyph.width = glyph
        plus_glyph.height = glyph
        plus_bar_h.width = glyph
        plus_bar_h.height = hair
        plus_bar_v.width = hair
        plus_bar_v.height = glyph

        wheel.width = hhight * WHEEL_W_PCT / 100
        wheel.height = hhight * WHEEL_H_PCT / 100
        state["digit_h"] = hhight * NUMERAL_PCT / 100
        front_layer = layers[state["front"]]
        for layer in layers:
            shown = str(state["value"]) if layer is front_layer else "0"
            layer.content = digit_image(shown)

        # window-relative sizes
        panel.top = hhight  # panel starts right under the header
        margin = short * PANEL_MARGIN_PCT / 100
        panel.margin = ft.Margin.all(margin)
        panel.border_radius = short * PANEL_RADIUS_PCT / 100
        
        panel.border = ft.Border.all(hair, ft.Colors.with_opacity(0.09, IVORY))
        panel.shadow = ft.BoxShadow(
            blur_radius=short * PANEL_SHADOW_BLUR_PCT / 100,
            color=ft.Colors.with_opacity(0.5, SHADOW),
            offset=ft.Offset(0, short * PANEL_SHADOW_DROP_PCT / 100),
        )

        inset = short * FRAME_INSET_PCT / 100
        frame.left = frame.right = frame.top = frame.bottom = inset
        frame.border = ft.Border.all(hair, ft.Colors.with_opacity(0.28, GOLD))

        top_shade.height = short * TOP_SHADE_PCT / 100

        biggest = short * RING_STEP_PCT / 100 * RING_COUNT
        ring_stack.width = biggest
        ring_stack.height = biggest
        for i, ring in enumerate(rings, start=1):
            d = short * RING_STEP_PCT / 100 * i
            ring.width = d
            ring.height = d
            ring.border_radius = d / 2
            ring.border = ft.Border.all(
                hair, ft.Colors.with_opacity(0.035, GOLD_HI)
            )


        content_layer.padding = ft.Padding.all(inset * 3)
        state["short"] = short
        state["hair"] = hair
        style_page()

        page.update()

    page.on_resize = apply_scale

    page.add(
        ft.Stack(
            expand=True,
            controls=[panel, header],
        )
    )
    apply_scale()
    show_page()  # NEW: show the first page (counter starts at 0 = History)

    await asyncio.sleep(0.25)
    apply_scale()


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")