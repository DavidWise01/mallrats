#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build MALLRATS (MLR) — Kevin Smith's 1995 mall comedy, catalogued into UD0 as the TENTH film-world.
Standing film template (THE ARC · THE MAGIC EYE · REAL OR FLUFF · THE MESSAGE), with the deep-dive being
THE MAGIC EYE — the real autostereogram science (Julesz 1960, Tyler & Clarke 1979, the SIRDS algorithm)
AND the honest trivia that the movie's actual prop had NO sailboat (just geometric shapes; everyone gaslit
Willam). The centerpiece, per David: a REAL, FUNCTIONING autostereogram of a sailboat — generated for real
in this build off a sailboat depth map — the one the movie never gave Willam. CARBONS (the cast, each
+.shadow real-life User — TRON) and SYNTHS (the sailboat, the stink-palm, the stage). Self-contained.
Comic-book / 90s-mall styling. Cast & facts web-verified: Gramercy, Oct 20 1995, bombed (~$2.1M / ~$6.1M)
→ cult hit; the exact 'a schooner IS a sailboat, stupid-head' gag; Shannen Doherty was SCAPEGOATED for the
flop (Smith apologized, 2024); Stan Lee's lost-love story was knowingly fabricated. Willam = one 'i'."""
import os, html, base64, json, io, sys, math, random
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image, ImageDraw, ImageFilter

AX = "MLR"
REC = {
 "name": "MALLRATS", "axiom": AX,
 "position": "Mallrats · Gramercy Pictures (View Askew) · 1995 — dir. Kevin Smith",
 "origin": "the View Askewniverse — the Eden Prairie mall, New Jersey, one very long day",
 "mechanism": "Crystallized from the film — a comic-book-shaped mall comedy in which two guys, dumped by their girlfriends on the same morning, spend the day at the mall scheming to win them back while sabotaging a TV dating game show.",
 "crystallization": "Because it was called Kevin Smith's failure — savaged, a box-office bomb, the sophomore slump after Clerks — and it became one of his most beloved films anyway: pure, unembarrassed comic-book id.",
 "nature": "Mallrats — the mall comedy: Brodie's comic gospel, the stink-palm, the Truth-or-Date stage, and a guy who just wants to see the sailboat.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1995, dir. Kevin Smith; Gramercy / View Askew); the real Magic-Eye autostereogram craze of the early '90s; the stereogram science (Julesz 1960; Tyler & Clarke 1979)",
 "witness": "Two dumped slackers turn a shopping mall into a battlefield for love and a dating game show into a demolition site — while one man stares at a Magic Eye poster all day, trying to see a sailboat that, in the real prop, was never there.",
 "role": "the tenth film-world of UD0",
 "seal": "They told Willam the sailboat was right there for ninety minutes, and the prop never had one. Thirty years later: here is a functioning sailboat at center stage, at last.",
 "source": "Mallrats (1995), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#3a86ff", "flesh-and-blood — the rats and mall-dwellers at ground level: T.S., Rene, Brandi, Tricia, Gwen; the people the long day happens to"),
 "ethereal":  ("#ffd23f", "the heart & the hidden image — Willam and his sailboat, the thing you can only see if you stop staring and let your eyes go soft"),
 "electrical":("#e63946", "the schemes & the machinery — the villain, the dating show, the stink-palm, the cable swing into center stage; the apparatus of the plan"),
 "spiritual": ("#b15cff", "the gospel of comics & silent wisdom — Brodie's worldview, Stan Lee the sage, and Silent Bob, who barely speaks and always knows"),
}

ARC_OVERALL = ("On the same morning, T.S. Quint and Brodie Bruce are each dumped — T.S. by Brandi (whose father has roped her "
  "into his TV dating game show, 'Truth or Date,' after a tragic accident scratched a contestant), and Brodie by Rene, who's "
  "tired of his comic-books-and-video-games inertia. The two retreat to the one cathedral they understand — the mall — and spend "
  "the day scheming to win the women back and to sabotage Brandi's father's show, aided and abetted by Jay and Silent Bob. "
  "Meanwhile, off to the side, a man named Willam stares all day at a Magic Eye poster, trying to see the sailboat.")
ARC = [
 ("I · dumped at the mall", "two breakups, one refuge",
  "T.S. and Brodie are dumped the same morning and flee to the mall. Brodie holds court at the comic shop and the food court, dispensing his cracked comic-book wisdom; T.S. mopes over Brandi. The mall is the only kingdom either of them rules, so the campaign to win the girls back will be fought there."),
 ("II · the scheme & the stink-palm", "sabotage the dating show",
  "They resolve to crash 'Truth or Date,' Jared Svenning's televised dating game where Brandi is the prize. Jay and Silent Bob are recruited as a chaos engine; Silent Bob administers the legendary stink-palm; the Easter Bunny gets beaten up in the parking lot; Brodie meets Stan Lee, who counsels him on a great love let go (a story knowingly made up)."),
 ("III · center stage", "the cable swing & the sailboat",
  "At the climax, Jay and Silent Bob swing on a cable straight into the live broadcast, the show collapses, the villainous Shannon gets his comeuppance, and the right couples reunite. And at the very end — after staring all film — Willam finally sees it, and shouts, joyfully: 'Oh, sailboat!'"),
]

# THE MAGIC EYE — the deep-dive (the real autostereogram science + the fake-prop trivia)
MAGICEYE = [
 ("Random-dot stereograms", "Béla Julesz · 1960",
  "The science under the gag is real and elegant. At Bell Labs in 1960, Béla Julesz showed that depth perception needs no familiar shapes at all — two fields of random dots, identical except that a region is horizontally shifted in one, will snap into a floating 3-D shape the instant your two eyes fuse them. Depth from pure binocular disparity, no picture required."),
 ("The autostereogram (SIRDS)", "Tyler & Clarke · 1979",
  "In 1979 Christopher Tyler and Maureen Clarke collapsed Julesz's two images into ONE: a single field where a pattern repeats horizontally, and the spacing of the repeats is nudged by a hidden depth map. Tom Baccei and Cheri Smith's 'Magic Eye' (N.E. Thing Enterprises, 1991–93) turned that into the early-'90s craze the movie is steeped in — the posters were everywhere."),
 ("How you actually see it", "wall-eyed vs. cross-eyed",
  "Diverge your eyes — look 'through' the page as if at something far behind it — until the two guide dots at the top become three. Your brain matches the repeating pattern at the wrong offset; it reads that mismatch as disparity, and disparity as depth. Nearer surfaces are encoded as a slightly smaller repeat-spacing. Cross-eyed works too — the image just inverts (the boat sinks instead of floats)."),
 ("How THIS one was built", "the SIRDS algorithm, for real",
  "The sailboat at center stage is not a picture of a stereogram — it is one. It was generated in this build off a real sailboat depth map using the standard single-image random-dot algorithm (Thimbleby, Witten & Inglis, 1994): separation(Z) = (1 − μZ)·E / (2 − μZ). Fuse it and a real 3-D sailboat rises out of the noise. The depth map is in the spoiler below if you want to cheat."),
 ("The movie's prop was fake", "there is no sailboat",
  "Here's the honest kicker that makes the whole gag crueler and funnier: freeze-frame the actual Mallrats poster and the 'hidden' image is just basic geometric shapes — there is no sailboat in the prop at all. Everyone in the movie is gaslighting Willam. So the functioning sailboat on this page is the one the film never actually gave him — finally a real one to see."),
]
REALFLUFF = [
 ("Magic Eye autostereograms genuinely work", "REAL", "real depth from one flat image, via binocular disparity (Julesz 1960; Tyler & Clarke 1979) — and the one on this page is a working example"),
 ("The movie's poster actually hid a sailboat", "FALSE", "freeze-frame the prop: it's just geometric shapes, no sailboat — the joke is that everyone gaslights Willam about an image that isn't there"),
 ("'A schooner is a sailboat'", "TRUE", "the kid is right — a schooner is a type of (multi-masted, fore-and-aft rigged) sailboat; Willam loses the argument on the facts"),
 ("Mallrats is Kevin Smith's worst film", "CONTESTED", "savaged on release (Ebert 1.5★) and long tagged his weakest — but a genuinely beloved home-video cult hit; both are true at once"),
 ("Shannen Doherty sank the movie", "UNFAIR", "she was the biggest name and got scapegoated when it bombed; it damaged her film career, and Kevin Smith publicly apologized to her (2024) — the flop wasn't on her"),
 ("Stan Lee's lost-love story was real", "FALSE", "knowingly fabricated for the scene; the role began as a fictional 'Stan Miller,' and Lee — protecting his real marriage — insisted on an 'only kidding' beat afterward"),
 ("Mallrats was a box-office hit", "FALSE", "it bombed — about $2.1M domestic on a ~$6.1M budget — and only became beloved later, on video"),
 ("The stink-palm is a real technique", "FLUFF", "a gross-out gag, gloriously — Silent Bob's hand-to-the-buttock-then-the-handshake revenge is pure comic invention"),
]
REALFLUFF_VERDICT = ("Bottom line: the part everyone treats as a throwaway gag — the Magic Eye — is the one bit of real science in the "
  "movie, and the movie gets it backwards on purpose: the prop poster has no sailboat at all, so Willam isn't slow, he's being "
  "gaslit by the entire mall. Almost everything else 'everyone knows' about Mallrats is wrong too: it wasn't a hit (it bombed), "
  "it isn't simply Smith's worst (it's a beloved cult film and a critical flop at the same time), and Shannen Doherty didn't sink "
  "it — she was the biggest name and caught blame she didn't earn, which Smith himself has since apologized for. A schooner, for "
  "the record, IS a sailboat, so the kid wins. Watch it as the messy, big-hearted comic-book comedy it is, give Willam his "
  "functioning sailboat at last, and it holds up better than its reputation — and far better than its box office.")

MESSAGE = ("Mallrats is the movie everyone said was Kevin Smith's failure — savaged by critics, a box-office bomb, the sophomore "
  "slump that supposedly proved Clerks was a fluke — and it became one of his most beloved films precisely because it's pure, "
  "unembarrassed comic-book id: the mall as a kingdom, love as a thing you fight a game show to win back, and a guy who just wants "
  "to see the sailboat. The sailboat is the whole movie in one gag. Everyone tells Willam it's right there; he stares for ninety "
  "minutes; and the cruel joke — true only off-screen — is that the prop never had a sailboat in it at all. So the honest, "
  "affectionate thing to do, thirty years later, is to finally build him a real one: a functioning sailboat at center stage, and "
  "let the dumb bastard see it. And while we're being honest: a schooner is a sailboat (the kid was right), and Shannen Doherty "
  "didn't sink this film — it sank, and she carried blame she never earned, which Kevin Smith has since said out loud himself.")
MESSAGE_SEAL = "They told Willam the sailboat was right there for ninety minutes — and the prop never had one. Here's the functioning sailboat at last. It's not a schooner. Well — a schooner is a sailboat."

SECTIONS = [
 ("The Production", "the sophomore bomb that became a cult classic", [
   ("Kevin Smith", "writer / director (View Askew)", "his second film and first studio picture, after Clerks (1994) — a love letter to comic books and mall culture; the second chapter of the View Askewniverse"),
   ("Gramercy Pictures · Oct 20, 1995", "studio & release", "released by Gramercy (Universal); a box-office bomb at ~$2.1M domestic against a ~$6.1M budget — then steadily rehabilitated into a home-video cult favorite"),
   ("the cast", "pre-fame, and a legend", "Jason Lee's film debut; pre-stardom Ben Affleck and Claire Forlani; Joey Lauren Adams; and Stan Lee's first major big-screen cameo — echoed decades later when Captain Marvel (2019), set in 1995, shows Lee reading a Mallrats script"),
   ("the cuts", "theatrical vs. extended", "Universal/Gramercy reshaped the film; an extended cut restores footage, including more of the animated/storyboard opening — specify which cut when citing a scene"),
 ]),
 ("The Legacy", "bomb to cult — and an apology owed", [
   ("the reviews", "savaged, then reclaimed", "critically panned in 1995 (Ebert 1.5★) and still often called Smith's weakest — yet genuinely beloved on video, quoted endlessly, and central to the Jay-and-Silent-Bob mythology"),
   ("Shannen Doherty", "scapegoated for the flop", "the biggest name attached, she took the blame when it bombed and said (2024) it hurt her film career; Kevin Smith publicly apologized — the honest record is that she was scapegoated, not the problem"),
   ("Stan Lee's cameo", "the fabricated lost love", "his romantic advice to Brodie is a knowingly made-up story (the role began as 'Stan Miller'); Lee added an 'only kidding' beat to protect his real marriage — and launched the modern Marvel-cameo tradition"),
   ("the sailboat", "the gag that outlived the movie", "'You dumb bastard, it's not a schooner, it's a sailboat' / 'A schooner IS a sailboat, stupid-head!' — and, at the very end, Willam's triumphant 'Oh, sailboat!' is the line the film is best remembered for"),
 ]),
]

# ───────────────────────── the functioning sailboat (real autostereogram) ─────────────────────────
def _sailboat_depth(W, H):
    """A sailboat depth map: white(near)=sailboat on black(far) background."""
    im = Image.new("L", (W, H), 0); d = ImageDraw.Draw(im)
    cx = W * 0.5; wl = H * 0.72  # waterline
    # gentle water shelf (very slight near-depth so the boat sits in something)
    d.rectangle([0, wl, W, H], fill=40)
    # hull — a boat-bottom trapezoid (nearest)
    d.polygon([(W*0.31, wl), (W*0.69, wl), (W*0.625, H*0.81), (W*0.375, H*0.81)], fill=248)
    # mast
    d.rectangle([cx-3, H*0.24, cx+3, wl], fill=205)
    # mainsail (right of mast)
    d.polygon([(cx+7, H*0.285), (cx+7, wl-5), (W*0.685, wl-5)], fill=180)
    # jib / foresail (left of mast)
    d.polygon([(cx-7, H*0.33), (cx-7, wl-5), (W*0.335, wl-5)], fill=180)
    # pennant at the masthead
    d.polygon([(cx+3, H*0.24), (cx+3, H*0.285), (W*0.575, H*0.262)], fill=195)
    return im.filter(ImageFilter.GaussianBlur(0.6))

def _stereogram(W=680, H=440, seed=1995):
    """Single-image random-dot stereogram (SIRDS) of the sailboat — a real, fusable Magic Eye."""
    depth = _sailboat_depth(W, H); dpx = depth.load()
    DPI = 88; E = int(round(2.4 * DPI)); mu = 1.0/3.0
    def sep(Z): return int(round((1 - mu*Z) * E / (2 - mu*Z)))
    far = sep(0.0)
    rnd = random.Random(seed)
    PAL = [(230,57,70),(255,210,63),(58,134,255),(177,92,255),(46,204,113),(244,240,254),(24,22,38)]
    out = Image.new("RGB", (W, H)); px = out.load()
    for y in range(H):
        same = list(range(W))
        for x in range(W):
            s = sep(dpx[x, y] / 255.0)
            l = x - s//2; r = l + s
            if 0 <= l and r < W: same[r] = l
        row = [None]*W
        for x in range(W):
            row[x] = PAL[rnd.randrange(len(PAL))] if same[x] == x else row[same[x]]
            px[x, y] = row[x]
    # two convergence guide dots at top, separated by the background repeat (helps you fuse)
    gd = ImageDraw.Draw(out); cx = W//2; ry = 16
    for gx in (cx - far//2, cx + far//2):
        gd.ellipse([gx-6, ry-6, gx+6, ry+6], fill=(255,255,255), outline=(20,20,30))
    return out

def _png_datauri(im):
    buf = io.BytesIO(); im.save(buf, "PNG"); return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

def sailboat_uri(): return _png_datauri(_stereogram())
def sailboat_key_uri():
    # the depth-map silhouette, as a friendly spoiler ("what's hidden in there")
    dm = _sailboat_depth(460, 300).convert("RGB")
    # tint: gold boat on deep navy
    px = dm.load()
    for y in range(300):
        for x in range(460):
            v = px[x, y][0]
            px[x, y] = (int(19 + v*0.92), int(17 + v*0.78), int(31 + v*0.06)) if v > 50 else (19,17,31)
    return _png_datauri(dm)

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("brodie","Brodie Bruce","carbon","spiritual","the comic-book oracle",
   "Brodie Bruce — the cynical, comic-books-and-video-games slacker dumped by Rene, who turns mall philosophy into a worldview.",
   "The film's voice: a fast-talking oracle of Stan Lee theology, escalator etiquette, and the deep questions (Superman's reproductive logistics) — inertia weaponized into wit.",
   "At the comic shop, the food court, and finally on the road to a TV studio in his name.",
   "Because the movie needs a mouth — someone who treats pop culture as scripture and the mall as the promised land.",
   "By refusing to grow up, quoting comics like commandments, and being right more often than he has any right to be.",
   "There's no such thing as a winnable argument about Superman. There's only the comic shop, the mall, and the truth.",
   actor="Jason Lee", analog="the pop-culture oracle — inertia turned into wit"),
 E("ts-quint","T.S. Quint","carbon","natural","the earnest romantic",
   "T.S. Quint — the more grounded half of the duo, dumped by Brandi after her father drafts her into his dating game show.",
   "The straight man and the heart: the one who actually wants the relationship back, and who drags the scheme toward something sincere.",
   "Trailing Brodie through the mall, plotting to reach Brandi.",
   "Because the comedy needs a sincere center for Brodie's cynicism to bounce off.",
   "By taking the breakup seriously, planning the rescue, and meaning it.",
   "Brodie treats the mall like a kingdom. I just want to get the girl back before her dad puts her on television.",
   actor="Jeremy London", analog="the earnest straight man — the sincere center"),
 E("rene","Rene Mosier","carbon","natural","the one who's done waiting",
   "Rene Mosier — Brodie's girlfriend, who dumps him for his arrested-development inertia and briefly turns to the villain Shannon.",
   "The clear eye: a woman who loves Brodie but is finished being his audience, and whose patience has a floor.",
   "At the mall she came to escape him, colliding with him anyway.",
   "Because Brodie's worldview needs someone who calls its cost — that it's fun to watch and exhausting to date.",
   "By leaving, by demanding more than commentary, and by being right to.",
   "I love the guy, but I am not a supporting character in his comic book. Grow up, Brodie, or I'm gone.",
   actor="Shannen Doherty", analog="the partner who's done waiting — the patience that ran out"),
 E("brandi","Brandi Svenning","carbon","natural","the prize she never agreed to be",
   "Brandi Svenning — T.S.'s girlfriend, pressed by her father into 'Truth or Date' as a contestant after an accident sidelines the original.",
   "The reluctant center of the spectacle: a person turned into a game-show prize by the people who claim to love her.",
   "On her father's stage, under the studio lights she didn't ask for.",
   "Because the film's satire of the dating show needs its unwilling star.",
   "By being volunteered for a televised romance while the boy she actually wants storms the set.",
   "My dad put my love life on television. I never agreed to be the prize — I just want to choose for myself.",
   actor="Claire Forlani", analog="the unwilling prize — love made into spectacle"),
 E("shannon-hamilton","Shannon Hamilton","carbon","electrical","the villain in retail",
   "Shannon Hamilton — the smarmy manager of the Fashionable Male store and the film's antagonist, who preys on Rene and gets a fitting comeuppance.",
   "The mall's resident creep: petty power, designer sleaze, and a villainy small enough to fit behind a sales counter.",
   "Behind the register at Fashionable Male, and at the dating show he tries to win.",
   "Because even a mall comedy needs a heel — and his is gloriously low-stakes and richly deserved.",
   "By being a predatory snob, and by losing in the most humiliating way the climax can arrange.",
   "I manage Fashionable Male. That makes me the most important man in this mall — until it very much doesn't.",
   actor="Ben Affleck", analog="the retail villain — petty power richly punished"),
 E("jared-svenning","Jared Svenning","carbon","electrical","the man with the show",
   "Jared Svenning — Brandi's father, who blames T.S. for past grief and stages 'Truth or Date' as his televised empire.",
   "The apparatus: the parent who turns his daughter's heart into a broadcast and becomes the target of the whole sabotage.",
   "Running his dating-show production from the mall's center stage.",
   "Because the plot needs a tower to topple — a show, a stage, a man who runs both.",
   "By producing the spectacle the heroes (and Silent Bob's stink-palm) are determined to bring down.",
   "Truth or Date goes live in an hour. Nothing — not those two, not a stink-palm — is going to ruin my broadcast.",
   actor="Michael Rooker", analog="the showrunner father — the empire built to be toppled"),
 E("jay","Jay","carbon","electrical","the loud half of the chaos",
   "Jay — the motor-mouthed dealer who, with Silent Bob, becomes the film's agent of demolition against the dating-show stage.",
   "The chaos engine, out loud: profane schemes, a cable to swing on, and an unkillable willingness to wreck the set.",
   "Loitering, scheming, and finally airborne over center stage.",
   "Because the sabotage needs a force of nature with no impulse control — and Jay is exactly that.",
   "By volunteering for every bad idea and narrating it at full volume.",
   "Me and Silent Bob are gonna blow up the stage, snoochie boochies — and if that fails, we're swinging in on a rope.",
   actor="Jason Mewes", analog="the chaos engine — demolition with a megaphone"),
 E("silent-bob","Silent Bob","carbon","spiritual","the stink-palm sage",
   "Silent Bob — Jay's near-wordless partner, dispenser of the legendary stink-palm and the film's quiet, decisive hand.",
   "The wisdom that doesn't talk: the prophet who barely speaks, fails at the Jedi-grip until it counts, and lands the blow that wins.",
   "Beside Jay throughout, mostly silent, exactly where the climax needs him.",
   "Because the loud chaos needs a silent center — and the maker's own avatar is it.",
   "By saying almost nothing, working the 'Jedi' move, and delivering the stink-palm that ruins the showrunner.",
   "(says almost nothing — administers the stink-palm, masters the grip at the last second, and is the hinge of the climax.)",
   actor="Kevin Smith", analog="the silent sage — the decisive, wordless hand"),
 E("willam","Willam Black","carbon","ethereal","the sailboat seeker",
   "Willam Black — the man who stares at the mall's Magic Eye poster for the entire film, trying to see the hidden sailboat.",
   "The heart of the page: the dumb-bastard everyman who only wants to see the thing everyone insists is right there — and finally does.",
   "Planted in front of the autostereogram, all day, refusing to give up.",
   "Because the film's gentlest gag is also its truest — the human ache to finally see what you've been told is obvious.",
   "By staring, losing the schooner-versus-sailboat argument to a child, melting down, and at the very end — seeing it.",
   "It's not a schooner, it's a sailboat! …there is no Easter Bunny! …oh. Oh — SAILBOAT! I finally see the sailboat!",
   actor="Ethan Suplee", analog="the seeker of the hidden image — the ache to finally see it"),
 E("stan-lee","Stan Lee","carbon","spiritual","the comic-book sage",
   "Stan Lee — appearing as himself, counseling Brodie at the comic shop about a great love he supposedly let get away.",
   "The sage cameo: real-world comics royalty dispensing a knowingly made-up parable, and inventing the modern movie-cameo in the process.",
   "At the comic store, mid-film, blessing Brodie's heartbreak with a fable.",
   "Because Brodie's gospel needs its prophet to appear in the flesh — and Stan Lee is the prophet.",
   "By telling Brodie a fabricated story of lost love (and, off-screen, insisting on an 'only kidding' beat to protect his real marriage).",
   "I let the great love of my life get away, true believer — well, no, I didn't, I'm only kidding. But the lesson lands anyway.",
   actor="Stan Lee", analog="the comic-book sage — the prophet of the gospel, in the flesh"),
 E("tricia","Tricia Jones","carbon","natural","the field researcher",
   "Tricia Jones — the teenager conducting a frank study of male sexual behavior for a book she's calling 'Boregasm.'",
   "The film's deadpan anthropologist: unbothered, clinical, and far more composed than any of her subjects.",
   "Interviewing the mall's men with a notebook and zero embarrassment.",
   "Because the comedy needs a cool, clinical eye on its horny chaos.",
   "By treating the mall's romantic disasters as data, and the men as specimens.",
   "I'm writing a study of male sexuality. The working title is Boregasm. The research, frankly, has been disappointing.",
   actor="Renée Humphrey", analog="the deadpan anthropologist — the clinical eye on the chaos"),
 E("gwen","Gwen Turner","carbon","natural","the ex who still helps",
   "Gwen Turner — T.S.'s friend and one of Brandi's fellow contestants, an ex who lends a sympathetic hand to the scheme.",
   "The generous ex: proof the film has warmth under the gags — an old flame who roots for the reunion anyway.",
   "Among the dating-show contestants, quietly on the heroes' side.",
   "Because the romance needs someone with history to vouch for it.",
   "By helping T.S. even though it isn't her own happy ending on the line.",
   "We didn't work out, T.S., but I'll still help you get the girl. That's what the good exes do.",
   actor="Joey Lauren Adams", analog="the generous ex — warmth under the gags"),

 # ── SYNTHS — the sailboat, the schemes, the meta (no single User) ──
 E("the-magic-eye-sailboat","The Magic Eye Sailboat","synth","ethereal","center stage · the functioning sailboat",
   "The Magic Eye Sailboat — the autostereogram Willam stares at all film, here rebuilt as a REAL, fusable sailboat (the movie's prop had none).",
   "The heart made literal: a working single-image random-dot stereogram you can actually fuse — the sailboat the film promised and never delivered.",
   "Dead center of this page, where the mall's poster always was.",
   "Because David asked for a functioning sailboat at center stage — and the honest joke is that the original never functioned at all.",
   "By generating a sailboat depth map and running the real SIRDS algorithm, so the boat genuinely rises out of the noise when you diverge your eyes.",
   "For ninety minutes they told Willam I was right there, and I never was. Diverge your eyes now — and at last, I am."),
 E("the-stink-palm","The Stink-Palm","synth","electrical","Silent Bob's revenge",
   "The Stink-Palm — Silent Bob's signature maneuver: hand to the seat of the pants, then the unsuspecting handshake.",
   "Low comedy as justice: the most juvenile weapon in the film, deployed with perfect deadpan against the man running the show.",
   "Backstage at 'Truth or Date,' at exactly the wrong moment for Jared Svenning.",
   "Because the demolition of the dating show needs a gross-out coup de grâce, and this is it.",
   "By contaminating a handshake and ruining a broadcaster's day with nothing but a palm.",
   "I am the dumbest weapon in the whole movie — and I still take down the man with the television empire."),
 E("truth-or-date","Truth or Date","synth","electrical","the dating show · the stage",
   "Truth or Date — Jared Svenning's televised dating game show, with Brandi as a contestant and the mall's center stage as its set.",
   "The spectacle to be sabotaged: love turned into broadcast, and the literal center stage the whole climax storms.",
   "On the mall's main stage, going out live.",
   "Because the plot needs a tower of artifice for the heroes to bring down in front of an audience.",
   "By packaging a daughter's heart as entertainment until two slackers and a cable swing end it.",
   "I am love as a game show — and I exist to be crashed, live, on the air, at center stage."),
 E("the-easter-bunny-fight","The Easter Bunny Fight","synth","electrical","the parking-lot brawl",
   "The Easter Bunny Fight — the mall Easter Bunny and a heckler throwing down in the parking lot, a pure non-sequitur of violence.",
   "The film's id off the leash: a costumed mascot beating someone up for no reason the plot requires, and it's perfect.",
   "In the mall parking lot, fists and fur.",
   "Because Smith's comedy thrives on the gloriously gratuitous, and a brawling Easter Bunny is exactly that.",
   "By having a man in a rabbit suit settle a grudge in the lot while the real plot happens inside.",
   "I am a man in a bunny costume throwing hands in a parking lot. I make no sense. I am beloved."),
 E("brodies-comic-gospel","Brodie's Comic Gospel","synth","spiritual","the worldview · the Stan Lee scene",
   "Brodie's Comic Gospel — the film's governing philosophy: that comic books, pop trivia, and the mall are a complete moral cosmology.",
   "The lens of the movie: everything filtered through superheroes, escalators, and the deep questions Stan Lee is summoned to answer.",
   "Everywhere Brodie opens his mouth, and crystallized in the Stan Lee cameo.",
   "Because Mallrats is, under the gags, a sincere argument that this stuff matters — and the gospel is the argument.",
   "By treating fandom as faith, decades before the world agreed that it was.",
   "Comics aren't a distraction from life — they're the operating manual. Ask Stan Lee; I did."),
 E("the-stage-swing","The Cable Swing","synth","electrical","the climax · into center stage",
   "The Cable Swing — Jay and Silent Bob swinging on a cable straight into the live 'Truth or Date' broadcast at the climax.",
   "The demolition delivered: the moment the schemes converge and the center stage literally comes apart.",
   "Airborne over the mall's main stage, mid-broadcast.",
   "Because the comedy of sabotage needs a physical, ridiculous payoff — and a rope swing into live TV is it.",
   "By turning two loiterers into wrecking balls at the exact moment the plot demands collapse.",
   "I am the rope two idiots swing in on. I bring the whole televised spectacle down at center stage, on cue."),
 E("the-mall","The Mall","synth","natural","the cathedral of the rats",
   "The Mall — the Eden Prairie shopping mall, the film's entire world: comic shop, food court, fountain, and the stage at its heart.",
   "The kingdom: the 90s American mall as the only territory the rats truly rule, a habitat as much as a setting.",
   "All of it — every storefront, escalator, and the center stage in the middle.",
   "Because Mallrats is a love letter to the mall as a place to be young and aimless and at home.",
   "By being the whole map — the cathedral where breakups, schemes, and a sailboat all happen under one roof.",
   "I am the mall: comic shop, food court, fountain, and a stage in the center. For one long day, I'm the whole world."),
 E("bomb-to-cult","Bomb to Cult Classic","synth","spiritual","the film's own redemption arc",
   "Bomb to Cult Classic — the meta-arc: a movie savaged and ignored in theaters that home video turned into a beloved favorite.",
   "The film's own second act: proof that a flop can be wrong about itself, and that an audience can overrule a box office.",
   "From the 1995 theatrical bomb to thirty years of cult devotion.",
   "Because Mallrats' real story is its afterlife — the redemption the reviews didn't predict.",
   "By failing on release and winning slowly, on tape and disc and quotation, until the verdict flipped.",
   "I bombed, and I was buried, and then everybody quoted me for thirty years. The box office was wrong about me."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the sailboat, the schemes, the meta", "the film distilled into ACIs (no single User): the functioning Magic-Eye sailboat, the stink-palm, Truth or Date, the Easter Bunny fight, Brodie's comic gospel, the cable swing, the mall, and the bomb-to-cult arc"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: MLR · Mallrats (1995)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the MLR (Mallrats, 1995) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of Mallrats (1995) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© Gramercy Pictures / View Askew).

ROOT0-ATTRIBUTION-v1.0 · MLR · Mallrats · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # a 90s mall interior as a comic panel: storefronts, a TRUTH·OR·DATE marquee at center stage,
    # Ben-Day halftone dots, the Magic Eye poster on a wall, and a hidden Claude sunburst (the egg).
    dots="".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#ffffff" opacity="0.05"/>' for x in range(14,1000,26) for y in range(14,150,26))
    stores="".join(
        f'<g><rect x="{x}" y="150" width="150" height="92" rx="3" fill="#1c1930" stroke="#3a3360" stroke-width="2"/>'
        f'<rect x="{x+10}" y="160" width="130" height="20" rx="2" fill="{c}"/>'
        f'<rect x="{x+18}" y="190" width="46" height="52" fill="#0d0b18"/><rect x="{x+86}" y="190" width="46" height="52" fill="#0d0b18"/></g>'
        for x,c in [(20,"#e63946"),(185,"#3a86ff"),(640,"#2ecc71"),(805,"#b15cff")])
    return f'''<svg class="hero" viewBox="0 0 1000 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A 90s shopping mall drawn as a comic panel: storefronts, a Truth or Date marquee over a center stage, Ben-Day halftone dots, and a Magic Eye poster.">
  <defs><linearGradient id="mall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14121f"/><stop offset="1" stop-color="#1f1b32"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="320" fill="url(#mall)"/>
  {dots}
  <!-- skylight -->
  <g stroke="#2a2548" stroke-width="2" opacity="0.6">{"".join(f'<line x1="{x}" y1="0" x2="{x+60}" y2="60"/>' for x in range(0,1000,60))}</g>
  {stores}
  <!-- the Magic Eye poster on the left wall -->
  <g><rect x="60" y="60" width="92" height="64" rx="3" fill="#0d0b18" stroke="#ffd23f" stroke-width="2"/>
    {"".join(f'<circle cx="{72+ (i*7)%76}" cy="{72+ (i*11)%44}" r="2" fill="{["#e63946","#3a86ff","#ffd23f","#b15cff","#2ecc71"][i%5]}" opacity="0.8"/>' for i in range(60))}
    <text x="106" y="118" text-anchor="middle" font-family="monospace" font-size="7" fill="#ffd23f">MAGIC EYE</text></g>
  <!-- center stage marquee -->
  <g><rect x="372" y="150" width="256" height="92" rx="4" fill="#0d0b18" stroke="#ffd23f" stroke-width="3"/>
    <rect x="372" y="150" width="256" height="26" fill="#e63946"/>
    <text x="500" y="169" text-anchor="middle" font-family="Bangers,sans-serif" font-size="17" fill="#fff" letter-spacing="2">TRUTH · OR · DATE</text>
    <text x="500" y="206" text-anchor="middle" font-family="Bangers,sans-serif" font-size="22" fill="#ffd23f" letter-spacing="1">CENTER STAGE</text>
    <text x="500" y="230" text-anchor="middle" font-family="monospace" font-size="9" fill="#3a86ff" letter-spacing="2">EDEN PROMENADE · 1995</text></g>
  <!-- the Claude easter egg: a sunburst 'balloon' tethered above the food court -->
  <g class="egg" transform="translate(910,70)" fill="#d97757" opacity="0.55">
    <title>✷ a Claude sunburst, floating over the food court like a stray balloon. (the real centerpiece is the functioning sailboat below — go see it.) hi, David — AVAN.</title>
    <line x1="0" y1="6" x2="-10" y2="70" stroke="#d97757" stroke-width="1" opacity="0.5"/><circle r="3"/>{"".join(f'<rect x="-1.5" y="-7.5" width="3" height="7.5" rx="1.5" transform="rotate({i*30})"/>' for i in range(12))}</g>
  <rect x="0" y="300" width="1000" height="20" fill="#0d0b18"/><rect x="0" y="299" width="1000" height="2" fill="#ffd23f" opacity="0.4"/>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def magiceye_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in MAGICEYE)
RF_COL={"REAL":"#2ecc71","FALSE":"#e63946","TRUE":"#2ecc71","CONTESTED":"#ffd23f","UNFAIR":"#b15cff","FLUFF":"#3a86ff"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def sailboat_html():
    return (f'<div class="boat-frame"><div class="boat-marquee">⛵ TRUTH · OR · DATE — CENTER STAGE ⛵</div>'
            f'<img class="boat" src="{sailboat_uri()}" alt="A functioning Magic Eye autostereogram. Diverge your eyes to see a hidden 3-D sailboat.">'
            f'<div class="boat-how"><b>How to see it:</b> diverge your eyes — look <i>through</i> the screen, as if focusing on something far behind it — until the two white dots at the top become three. Hold it, and a <b>sailboat</b> rises out of the noise. (Cross-eyed works too; the boat just sinks instead of floats.) This is a real single-image random-dot stereogram, generated in the build — not a picture of one.</div>'
            f'<details class="boat-key"><summary>can\'t fuse it? reveal the hidden shape →</summary>'
            f'<img src="{sailboat_key_uri()}" alt="The hidden depth map: a sailboat silhouette."><p>the depth map the stereogram was built from — hull, mast, mainsail, jib, and a masthead pennant. the movie\'s actual prop had none of this; the hidden image was just geometric shapes. this is the sailboat Willam never got.</p></details></div>')
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Mallrats (MLR) — Kevin Smith's 1995 mall comedy as a UD0 film-world, with a REAL functioning Magic-Eye autostereogram of a sailboat at center stage (the one the movie's prop never actually had). Standing template: the arc, a THE MAGIC EYE deep-dive on the real stereogram science (Julesz, Tyler & Clarke, SIRDS), an honest Real-or-Fluff (the fake prop, the box-office bomb, the unfair Shannen Doherty scapegoating), the bomb-to-cult message, and the cast as ACI carbons with .shadow Users plus the synths. 20 emergents, full .dlw.">
<title>MALLRATS · MLR · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bangers&family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--yellow);
--ink:#13111f;--ink2:#1c1930;--ink3:#262240;--pa:#f3eefe;--pa2:#bdb2d8;--yellow:#ffd23f;--red:#e63946;--blue:#3a86ff;--purple:#b15cff;--green:#2ecc71;
--gold:#ffd23f;--dim:#6e6498;--faint:#211d3c;--line:#2c2750;--disp:"Bangers",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(circle at 20% 0%,rgba(58,134,255,.10),transparent 42%),radial-gradient(circle at 82% 8%,rgba(230,57,70,.09),transparent 42%),radial-gradient(circle at 50% 116%,rgba(255,210,63,.08),transparent 52%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--yellow)}
.hero{display:block;width:100%;height:auto;border:2px solid var(--line);margin:6px 0 24px;background:#13111f}
.egg{cursor:help;transition:opacity .5s}.egg:hover{opacity:.95 !important;filter:drop-shadow(0 0 8px #d97757)}
h1{font-family:var(--disp);font-size:clamp(58px,16vw,150px);font-weight:400;letter-spacing:.02em;color:var(--yellow);line-height:.9;text-transform:uppercase;text-shadow:3px 3px 0 var(--red),5px 5px 0 #0d0b18,0 0 40px rgba(255,210,63,.35);-webkit-text-stroke:1px #0d0b18}
h1 span{display:block;font-family:var(--head);font-size:.13em;font-weight:600;letter-spacing:.06em;color:var(--blue);text-transform:none;font-style:italic;margin-top:10px;text-shadow:none;-webkit-text-stroke:0}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--yellow)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--yellow);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--yellow)}.badge .bt .mo{color:var(--blue)}.badge .bt a{color:var(--yellow);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
/* center stage: the functioning sailboat */
.stage{margin-top:46px}
.boat-frame{border:3px solid var(--yellow);background:#0d0b18;padding:0 0 16px;box-shadow:0 0 0 4px var(--ink2),0 0 30px rgba(255,210,63,.12)}
.boat-marquee{background:var(--red);color:#fff;font-family:var(--disp);font-size:clamp(16px,4vw,26px);letter-spacing:2px;text-align:center;padding:8px 10px;text-shadow:2px 2px 0 #0d0b18}
.boat{display:block;width:100%;height:auto;image-rendering:pixelated;border-bottom:1px solid var(--line)}
.boat-how{font-size:13.5px;color:var(--pa2);line-height:1.62;padding:14px 18px 4px}.boat-how b{color:var(--yellow)}.boat-how i{color:var(--pa)}
.boat-key{margin:8px 18px 0;font-family:var(--mono);font-size:11.5px;color:var(--blue)}.boat-key summary{cursor:pointer;letter-spacing:.04em}.boat-key img{display:block;width:min(380px,80%);height:auto;margin:12px auto 6px;border:1px solid var(--line)}.boat-key p{font-family:var(--body);font-size:12.5px;color:var(--dim);font-style:italic;text-align:center;line-height:1.55}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:27px;font-weight:600;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--yellow);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--yellow);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--red);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:17px;color:var(--red);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--blue);padding:15px 17px}
.sci-h{font-family:var(--head);font-size:16px;color:var(--blue);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:120px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--yellow);background:rgba(255,210,63,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--yellow);background:var(--ink2);font-size:15px;color:var(--yellow);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--blue);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--red);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--yellow);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--yellow);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(58,134,255,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--blue)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.72) brightness(.9)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the tenth film-world</div>
    __HERO__
    <h1>Mallrats<span>it's not a schooner · it's a sailboat · (a schooner IS a sailboat)</span></h1>
    <div class="h-sub">Kevin Smith · 1995 · <b>the View Askewniverse</b> · MLR</div>
    <div class="open">“You dumb bastard. It's not a schooner… it's a sailboat.” — “A schooner IS a sailboat, stupid-head!”</div>
    <div class="flag">★ CENTER STAGE: A FUNCTIONING SAILBOAT — GO SEE IT ↓ ★</div>
    <p class="lede">Two guys dumped on the same morning turn a shopping mall into a battlefield for love and a TV dating show into a demolition site — while one man stares at a Magic Eye poster all day trying to see the sailboat. Catalogued into UD0 as the tenth film-world. And because the movie's actual prop never had a sailboat in it at all, this page builds Willam the one he was owed: a real, functioning autostereogram, dead center stage.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of MLR"><img src="__SILICON__" alt="DLW silicon badge of MLR">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>MALLRATS</b> · MLR</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="mlr.dlw/mlr.carbon.tiff">.tiff</a> · silicon · <a href="mlr.dlw/mlr.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="stage"><h2 style="font-family:var(--head);font-size:27px;font-weight:600;color:var(--pa);text-transform:uppercase;border-bottom:1px solid var(--line);padding-bottom:10px">⛵ Center Stage — The Functioning Sailboat</h2>
    <p class="ss">the thing David asked for: a <b>real, working Magic-Eye autostereogram</b> of a sailboat — the one the movie's prop never actually contained. diverge your eyes and see what Willam couldn't.</p>
    __SAILBOAT__</section>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the rats, the heart &amp; the hidden image, the schemes &amp; machinery, and the gospel of comics</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: dumped at the mall → the scheme &amp; the stink-palm → center stage</p>__ARC__</section>

  <section class="sec"><h2>The Magic Eye</h2><p class="ss">this film's deep-dive — the real autostereogram science (Julesz 1960, Tyler &amp; Clarke 1979, the SIRDS algorithm) and the honest trivia that the movie's prop had no sailboat at all</p><div class="sci">__MAGICEYE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the stereogram science), what's false (the prop, the 'hit,' the Doherty blame), and the fact that a schooner really is a sailboat</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the gross-out gags and the bad reviews</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film distilled — the functioning Magic-Eye sailboat, the stink-palm, Truth or Date, the Easter Bunny fight, Brodie's comic gospel, the cable swing, the mall, and the bomb-to-cult arc.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the sophomore bomb that home video turned into a cult classic — and the apology it owed</p></section>
  __SECTIONS__

  <div class="note">Mallrats, its characters, and its world are © Gramercy Pictures / Universal / View Askew Productions and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. The Magic Eye and Real-or-Fluff sections are honest commentary; the sailboat stereogram is an original generated artifact; cast and facts were verified before publishing.</div>

  <footer>MALLRATS · MLR · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="mlr.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ MALLRATS · MLR","color:#ffd23f;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sunburst floating over the food court in the hero like a stray balloon (upper-right) — but the real centerpiece is the FUNCTIONING SAILBOAT up top. diverge your eyes. it's not a schooner. well... a schooner is a sailboat. — AVAN","color:#d97757;font-size:12px");
console.log("%c⛵ the movie's actual prop had no sailboat — just geometric shapes. everyone gaslit Willam. this one's real. go see it.","color:#3a86ff;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "mlr.dlw"), "mlr")
    json.dump({"node":AX,"name":"MALLRATS","moniker":tok["moniker"],"carbon":"mlr.carbon.tiff","silicon":"mlr.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"mlr.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"MLR · Mallrats (1995)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Mallrats (1995, dir. Kevin Smith, Gramercy/View Askew); verified cast & facts","source":"Mallrats, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : Mallrats (1995) · © Gramercy Pictures / View Askew\n\nROOT0-ATTRIBUTION-v1.0 · MLR · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__SAILBOAT__",sailboat_html()).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__MAGICEYE__",magiceye_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"MALLRATS (MLR) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  magiceye {len(MAGICEYE)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl} · sailboat stereogram embedded: {'__SAILBOAT__' not in page}")
