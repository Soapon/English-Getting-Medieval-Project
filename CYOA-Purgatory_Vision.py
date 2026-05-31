"""
THE VISIONS OF ELISABETH OF SCHÖNAU
A Choose Your Own Adventure
Based on a real vision
"""

import time, sys, os

# ── helpers ────────────────────────────────────────────────────
def c(text, code):   return f"\033[{code}m{text}\033[0m"
def gold(t):         return c(t, "33")
def cyan(t):         return c(t, "36")
def dim(t):          return c(t, "2")
def bold(t):         return c(t, "1")
def red(t):          return c(t, "31")
def green(t):        return c(t, "32")
def magenta(t):      return c(t, "35")

def slow_print(text, delay=0.020):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def pause(msg="Press ENTER to continue..."):
    input(dim(f"\n  {msg}"))

def divider(char="─", width=62):
    print(dim(char * width))

def header(title):
    print(); divider("═"); print(gold(f"  ✦  {title}")); divider("═"); print()

def scene_header(title, location=""):
    print(); divider()
    print(bold(cyan(f"  ❧  {title}")))
    if location: print(dim(f"     {location}"))
    divider(); print()

def narrate(text):    slow_print(f"  {text}")
def speak(who, text): print(); print(magenta(f"  {who}:")); slow_print(f'  "{text}"', 0.018)

def stat_bar(label, val, mx=10, w=20):
    filled = int((val / mx) * w)
    bar = "█" * filled + "░" * (w - filled)
    col = green if val >= 7 else (gold if val >= 4 else red)
    return f"  {dim(label+':')} {col(bar)} {val}/{mx}"

# ── state ───────────────────────────────────────────────────────
S = {
    "faith":    7,
    "courage":  5,
    "knowledge":3,
    "support":  0,
    "promised": False,
    "written":  False,
    "told_abbess": False,
    "doubt_count": 0,
    "fear":     0,
}

def show_stats():
    print(); divider("·")
    print(f"  {bold('── Your Inner State ──')}")
    print(stat_bar("Faith / Certainty", S["faith"]))
    print(stat_bar("Courage to Speak ", S["courage"]))
    print(stat_bar("Theology & Lore  ", S["knowledge"]))
    allies = "★" * S["support"] + "☆" * (3 - S["support"])
    print(f"  {dim('Allies:')} {green(allies)}")
    divider("·"); print()

def choose(prompt, options):
    """options = [(label, key), ...]  — exactly 3"""
    print(f"\n  {bold(prompt)}")
    for i, (label, _) in enumerate(options, 1):
        print(f"  {gold(str(i))}. {label}")
    while True:
        raw = input(f"\n  {dim('Your choice')} {gold('→')} ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw)-1][1]
        print(red("  Please enter a valid number."))

# ═══════════════════════════════════════════════════════════════
# PROLOGUE
# ═══════════════════════════════════════════════════════════════
def prologue():
    os.system("cls" if os.name == "nt" else "clear")
    header("THE VISIONS OF ELISABETH OF SCHÖNAU")
    slow_print(gold("  A Choose Your Own Adventure · 12th-century Germany"), 0.03)
    print()
    narrate("You are Sister Elisabeth, a Benedictine nun at the monastery of Schönau.")
    narrate("The year is 1152. You are twenty-three years old, and you are unwell.")
    narrate("For months, fevers have gripped you at Compline")
    narrate("and sometimes you lose hours, returning with strange memories of light")
    narrate("and voices and landscapes no living person should know.")
    print()
    narrate("Tonight after Compline, you kneel alone in the dark chapel.")
    narrate("The candles gutter. Your hands are cold.")
    print()
    slow_print(red("  Then......the light comes!!!"), 0.04)
    pause()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 1 — The Figure
# ═══════════════════════════════════════════════════════════════
def chapter_1():
    scene_header("Chapter I: The Figure in the Chapel",
                 "Chapel of St Florin, Schönau...Midnight")

    narrate("A figure stands at the altar. It is not flesh. It casts no shadow.")
    narrate("It pulses with cold silver light and turns toward you with an expression")
    narrate("of immense, patient sorrow.")
    print()
    speak("The Figure", "Come. There is something you must witness. It will hurt, but it is necessary.")
    print()

    ch = choose("What do you do?", [
        ("Follow immediately ~ the light feels holy.",               "follow"),
        ("Pray first to test the spirit before obeying.",            "pray"),
        ("Back away in fear ~ this could be demonic deception.",     "refuse"),
    ])

    if ch == "follow":
        narrate("You rise and walk toward the figure without hesitation.")
        narrate("The cold deepens. The stone floor seems to fall away beneath you.")
        S["faith"] += 1; S["courage"] += 1

    elif ch == "pray":
        narrate("You recite the ancient test: 'Every spirit that confesses Christ")
        narrate("come in the flesh is of God.' You wait, hands folded, heart hammering.")
        print()
        narrate("The figure does not flee. It bows its head, patient.")
        speak("The Figure", "You are wise to test. Now follow.")
        S["faith"] += 2; S["knowledge"] += 1

    elif ch == "refuse":
        narrate("You press yourself against the cold stone wall and whisper the Pater Noster.")
        narrate("The figure waits. And waits. It is still there when you finish trembling.")
        S["faith"] -= 1; S["courage"] -= 1; S["fear"] += 1; S["doubt_count"] += 1

    pause()
    chapter_2()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 2 — Purgatory
# ═══════════════════════════════════════════════════════════════
def chapter_2():
    scene_header("Chapter II: The Place of Waiting",
                 "Purgatory: a road of amber light and slow fire")

    narrate("The chapel dissolves. You walk a road that glows like cooling embers.")
    narrate("The sky is neither night nor day.")
    narrate("The figure glides ahead. You notice it has no feet.")
    print()
    speak("The Figure", "What you see is Purgatory, the place of cleansing. The Church")
    speak("The Figure", "on earth has forgotten the souls here. They cannot ascend")
    speak("The Figure", "without prayers. Without Masses said in their name.")
    print()
    narrate("You see them, hundreds of souls, some wailing, some kneeling in exhaustion,")
    narrate("wrapped in slow fire that refines rather than destroys. Their faces are human.")
    narrate("One approaches. She is a noblewoman, her dress scorched, her bearing dignified.")
    print()
    speak("The Soul", "Sister. You are warm. You are still alive. Tell them.")
    speak("The Soul", "Tell the living: say Masses, pray for the dead. We are not lost.")
    speak("The Soul", "Tell the priests and Abbots to stop misguiding their flocks")
    speak("The Soul", "We are only waiting. Do not let them forget us.")
    
    print()

    ch = choose("How do you respond to the soul's plea?", [
        ("Promise her: 'I will tell them. I swear it on my vows.'",        "promise"),
        ("Ask her questions: who is she, how long has she been here?",    "questions"),
        ("Doubt aloud: 'How do I know you are not a demon in disguise?'",  "doubt"),
    ])

    if ch == "promise":
        narrate("The soul's fire dims slightly. Her expression becomes something like relief.")
        speak("The Soul", "Then we are not forgotten. Go. Remember us.")
        S["faith"] += 1; S["courage"] += 2; S["promised"] = True

    elif ch == "questions":
        narrate("She tells you she was the wife of a minor lord dead three years past.")
        narrate("She waits here because two Masses promised at her funeral were never said.")
        narrate("The detail is precise, verifiable, if anyone investigated.")
        S["knowledge"] += 2; S["faith"] += 1; S["promised"] = True

    elif ch == "doubt":
        narrate("The soul does not rage. She looks unbearably tired.")
        speak("The Soul", "I cannot prove my nature. You can only judge by the fruits.")
        speak("The Soul", "If good comes from your telling, was I a demon?")
        narrate("This is the oldest problem in mystical theology. You have no answer.")
        S["knowledge"] += 2; S["doubt_count"] += 1

    pause()
    chapter_3()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 3 — The Waking
# ═══════════════════════════════════════════════════════════════
def chapter_3():
    scene_header("Chapter III: The Waking",
                 "Chapel of St Florin — Just Before Dawn")

    narrate("You wake on the cold chapel floor. The candles have burned out.")
    narrate("Your habit is soaked through with sweat. Your hands still shake.")
    narrate("Outside, the bell rings for the dawn prayer.")
    print()
    narrate("You have something enormous inside you now. A weight of testimony.")
    narrate("You also have no proof. Only your word, your body, and your fever.")
    narrate("In two hours the community gathers for the daily meeting.")
    print()
    speak("Your own thoughts", "Do I say something? Do I stay silent? What if they think I am mad?")
    print()

    ch = choose("What is your first instinct?", [
        ("Go to your abbess immediately and tell her everything.",        "abbess"),
        ("Write it all down first, then decide what to share.",         "write"),
        ("Stay silent for now. Pray. Wait to see if it happens again.",  "silence"),
    ])

    if ch == "abbess":
        narrate("You find her before Lauds, in her study with a single candle.")
        narrate("You speak for half an hour without stopping.")
        speak("The Abbess", "I believe you. This is not the first time I have seen you")
        speak("The Abbess", "return from somewhere else. Rest today. Then we will talk.")
        S["told_abbess"] = True; S["support"] += 1; S["courage"] += 1

    elif ch == "write":
        narrate("You scratch everything down by lamplight.")
        narrate("Seeing it on parchment, it looks more like a report.")
        S["written"] = True; S["knowledge"] += 1; S["faith"] += 1

    elif ch == "silence":
        narrate("You keep the secret for three days. It does not shrink.")
        narrate("It grows heavier, more insistent, until you are dreaming of the amber road.")
        narrate("The silence is not peace. It is a postponement.")
        S["fear"] += 1; S["doubt_count"] += 1

    pause()
    chapter_4()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 4 — The Abbess & the Chapter
# ═══════════════════════════════════════════════════════════════
def chapter_4():
    scene_header("Chapter IV: The Chapter House",
                 "Monastery of Schönau. One Week Later")

    narrate("The abbess has called. Word has spread, as it")
    narrate("always does in a small community. Some nuns are frightened. Some are")
    narrate("intrigued. A visiting monk from a neighbouring abbey sits in the corner,")
    narrate("stylus in hand, listening.")
    print()
    speak("The Abbess", "Sister Elisabeth has had a vision. She will describe it now.")
    speak("The Abbess", "We will hear her in silence and discern together what it means.")
    print()
    narrate("Every face in the room is turned toward you.")
    print()

    ch = choose("How do you present your vision to the community?", [
        ("Describe it fully and directly with hold nothing back.",               "full"),
        ("Give the message without the details.",       "brief"),
        ("Admit your uncertainty first: 'I do not know what I saw.'",         "uncertain"),
    ])

    if ch == "full":
        narrate("You speak for almost an hour. Some nuns weep. The visiting monk")
        narrate("fills three pages of notes. The abbess's expression is unreadable.")
        narrate("'The souls in Purgatory need our prayers. We have been forgetting them.'")
        narrate("You viciously urge people to repent, demanding that corrupt priests and monks abandon their worldliness and faithfully shepherd their flocks")
        speak("The Visiting Monk", "This will need to go to the bishop. And perhaps to parchment.")
        S["courage"] += 2; S["support"] += 1; S["written"] = True

    elif ch == "brief":
        narrate("Your message is clear and simple, stripped of the unsettling detail.")
        narrate("'The souls in Purgatory need our prayers. We have been forgetting them.'")
        narrate("You viciously urge people to repent, demanding that corrupt priests and monks abandon their worldliness and faithfully shepherd their flocks")
        narrate("The community receives this well. It is practical. It is actionable.")
        speak("The Abbess", "We will add a daily prayer for the faithful departed. Thank you.")
        S["support"] += 1; S["promised"] = True

    elif ch == "uncertain":
        narrate("'I cannot say for certain whether I was carried there in body or in spirit.")
        narrate("I can only say what I experienced. The Church must judge what it means.'")
        narrate("The visiting monk looks up sharply, impressed by the theological care.")
        speak("The Visiting Monk", "That is exactly the right frame. May I quote you?")
        S["knowledge"] += 2; S["support"] += 1

    pause()
    chapter_5()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 5 — Ekbert's Arrival
# ═══════════════════════════════════════════════════════════════
def chapter_5():
    scene_header("Chapter V: Your Brother Ekbert",
                 "The Scriptorium. One Month Later")

    narrate("Ekbert has arrived from Bonn in person. His letter came first,")
    narrate("full of citations from Augustine and Gregory, then he came himself")
    narrate("because letters were not enough.")
    print()
    speak("Ekbert", "The Church will not preserve a spoken vision. Hildegard of Bingen's Scivias is already being copied across Europe. Let me help you write")
    speak("Ekbert", "Scivias is already being copied across Europe. Let me help you write")
    speak("Ekbert", "yours. I will be the scribe. The words will be yours. The theological apparatus will be mine. Together we make something the bishops cannot dismiss.")
    print()
    narrate("Ekbert is brilliant and he loves you and he also wants, very much,")
    narrate("to be the man who discovered a living mystic.")
    print()

    ch = choose("How do you respond to Ekbert's offer?", [
        ("Accept fully ~ you trust him and the Church needs this on parchment.", "accept"),
        ("Accept with conditions ~ you must review every word before it's copied.", "conditions"),
        ("Refuse ~ you fear he will reshape your experience into his theology.",   "refuse"),
    ])

    if ch == "accept":
        narrate("Over the following months, the Liber Visionum takes shape.")
        narrate("Ekbert's framework is rigid in places, but it gives your words authority.")
        narrate("The book will be read from the Rhine to the English Channel.")
        S["written"] = True; S["support"] += 1; S["courage"] += 1

    elif ch == "conditions":
        narrate("Ekbert agrees with only mild irritation. The collaboration is tense")
        narrate("and productive. You argue over two passages. He defers on one.")
        narrate("You defer on one. The result is richer for the argument.")
        S["written"] = True; S["knowledge"] += 2; S["faith"] += 1

    elif ch == "refuse":
        narrate("Ekbert is hurt. Then he respects your decision. Then, eventually,")
        narrate("he writes a partial account from memory of your letters.")
        narrate("It reaches posterity, but always with a note of incompleteness.")
        S["fear"] += 1; S["faith"] += 1  # more authentic but less reach

    pause()
    chapter_6()

# ═══════════════════════════════════════════════════════════════
# CHAPTER 6 — The Final Question
# ═══════════════════════════════════════════════════════════════
def chapter_6():
    scene_header("Chapter VI: The Last Compline",
                 "Monastery of Schönau. Years Later")

    narrate("The visions continue for over a decade. You are exhausted and still")
    narrate("occasionally transported. You are thirty-five now. You look sixty.")
    print()
    narrate("A young novice finds you after Compline, wide-eyed with something")
    narrate("between fear and hope. She says: 'I saw something last night, Sister.'")
    narrate("'A light. A figure. I did not know whether to follow.'")
    print()
    narrate("You look at her for a long moment. You are the expert now.")
    narrate("No one asked to be, but here you are.")
    print()

    ch = choose("What do you tell her?", [
        ("'Test it! Pray first. Then follow if it waits for you.'",          "test"),
        ("'Write everything down. The act of writing is itself a form of prayer.'", "write"),
        ("'Tell someone you trust before you do anything else. Do not carry it alone.'", "share"),
    ])

    if ch == "test":
        speak("You", "Every spirit must be tested. Recite the creed. Recite it twice.")
        speak("You", "If the light waits, it is patient. Patience is a sign.")
        narrate("She nods, slowly. You can see her memorising your words.")
        S["knowledge"] += 1; S["faith"] += 1

    elif ch == "write":
        speak("You", "Write it down tonight, before the memory blurs. Every detail.")
        speak("You", "Even the things that embarrass you or seem too strange.")
        speak("You", "Especially those. Those are the ones that tend to be true.")
        S["written"] = True; S["knowledge"] += 2

    elif ch == "share":
        speak("You", "Go to Sister Hildegund. Or the abbess. Do not decide alone.")
        speak("You", "I made the mistake of carrying this in silence at the start.")
        speak("You", "The weight is real. You do not have to hold it by yourself.")
        S["support"] += 1; S["courage"] += 1

    pause()
    ending()

# ═══════════════════════════════════════════════════════════════
# ENDINGS
# ═══════════════════════════════════════════════════════════════
def ending():
    header("EPILOGUE: What Became of Elisabeth")
    show_stats()
    time.sleep(0.5)

    f = S["faith"]; cour = S["courage"]; fear = S["fear"]
    written = S["written"]; support = S["support"]
    promised = S["promised"]; doubts = S["doubt_count"]

    print()
    narrate("You die in 1165. You are thirty-six years old.")
    narrate("The community buries you with full Benedictine rites.")
    print()

    if f >= 8 and cour >= 6 and written:
        _end_faithful(promised, support)
    elif fear >= 3 or cour <= 3:
        _end_overwhelmed()
    elif doubts >= 2 and not promised:
        _end_disputed()
    elif written and cour < 5:
        _end_silenced()
    else:
        _end_complex()

def _end_faithful(promised, support):
    print(gold("  ╔══════════════════════════════╗"))
    print(gold("  ║  ENDING: Faithful Visionary  ║"))
    print(gold("  ╚══════════════════════════════╝")); print()
    narrate("Your visions are recorded and copied. Abbots read you.")
    narrate("A bishop quotes you in a sermon. A Cistercian abbess writes to say")
    narrate("your description of Purgatory brought her community to prayer.")
    if promised:
        print()
        narrate("The souls you promised to remember are remembered. Masses are said.")
    if support >= 2:
        print()
        narrate("You did not do this alone. The medieval mystic was never entirely")
        narrate("solitary. That, too, was a kind of grace.")
    print()
    slow_print(green("  You gave the dead a voice. Eight centuries later, someone still reads you."), 0.03)
    print(); _historical_note()

def _end_overwhelmed():
    print(red("  ╔══════════════════════════════╗"))
    print(red("  ║  ENDING: Overwhelmed         ║"))
    print(red("  ╚══════════════════════════════╝")); print()
    narrate("The visions multiply. You begin to dread Compline.")
    narrate("Your abbess is kind. The physician is baffled. The community prays.")
    narrate("You are not lost, but you cannot be the messenger you were asked to be.")
    narrate("The weight of what you saw is too much to carry and too much to set down.")
    print()
    narrate("Ekbert writes an account from memory. It is partial.")
    print()
    slow_print(red("  Some doors, once opened, cannot be closed again."), 0.03)
    print(); _historical_note()

def _end_disputed():
    print(magenta("  ╔══════════════════════════════╗"))
    print(magenta("  ║  ENDING: The Disputed Mystic  ║"))
    print(magenta("  ╚══════════════════════════════╝")); print()
    narrate("Your honest doubt leads somewhere unexpected.")
    narrate("The clergy prefer a mystic who is certain.")
    narrate("Uncertainty is just confusion.")
    print()
    narrate("Your account circulates with marginal notes disputing key passages.")
    narrate("Later scholars ask: what, exactly, did she see?")
    print()
    slow_print(magenta("  Truth and credibility are not the same thing here."), 0.03)
    print(); _historical_note()

def _end_silenced():
    print(dim("  ╔══════════════════════════════╗"))
    print(dim("  ║  ENDING: The Silenced Mystic  ║"))
    print(dim("  ╚══════════════════════════════╝")); print()
    narrate("The record exists, but you stayed too far inside the walls.")
    narrate("Your visions are preserved in the monastery archive, copied once")
    narrate("by a visiting scribe who loses the copy.")
    narrate("Hildegard of Bingen becomes the name people know. You are a footnote.")
    print()
    narrate("This is not a failure. You lived faithfully and served your community.")
    narrate("But the wider Church never had the chance to be challenged by you.")
    print()
    slow_print(dim("  Faithfulness and impact are not always the same thing."), 0.03)
    print(); _historical_note()

def _end_complex():
    print(bold("  ╔══════════════════════════════╗"))
    print(bold("  ║  ENDING: A Complex Legacy    ║"))
    print(bold("  ╚══════════════════════════════╝")); print()
    narrate("You are not a simple story. No mystic is.")
    narrate("You had faith and doubt at the same time. You spoke and stayed silent in turns.")
    narrate("Your record is partial. Your community remembers you with love.")
    print()
    narrate("Centuries later, scholars call you 'one of the more interesting and underread")
    narrate("figures of the twelfth century.' This is accurate and slightly insulting.")
    narrate("You would have appreciated the irony.")
    print()
    slow_print(bold("  You were real. You struggled. That is enough."), 0.03)
    print(); _historical_note()

def _historical_note():
    divider("═"); print(gold("  HISTORICAL NOTE")); divider(); print()
    narrate("Elisabeth of Schönau (c. 1129–1165) was a real Benedictine nun.")
    narrate("Beginning in 1152, she experienced intense visions during liturgical prayer.")
    narrate("Her brother Ekbert recorded them in three major works:")
    print()
    print(cyan("  • Liber Visionum ~ her main visionary record"))
    print(cyan("  • Liber Viarum Dei ~ moral exhortations to the living"))
    print(cyan("  • De Resurrectione Beatae Mariae Virginis ~ on Mary's Assumption"))
    print()
    narrate("Over 140 manuscript copies of her work survive across Europe, but she has")
    narrate("been largely overshadowed by her contemporary Hildegard of Bingen.")
    narrate("She was never formally canonised, but is venerated in the Benedictine")
    narrate("tradition with a feast day of 18 June.")
    print()
    narrate("Her visions raised questions medieval theologians genuinely struggled with:")
    print(dim("  —> How do you tell a divine vision from demonic deception?"))
    print(dim("  —> Can women hold prophetic authority in the Church?"))
    print(dim("  —> What do the living owe the dead?"))
    print()
    narrate("These are not only medieval questions.")
    divider("═"); print()

# ═══════════════════════════════════════════════════════════════
# TITLE + MAIN
# ═══════════════════════════════════════════════════════════════
def title_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print(gold("  ╔══════════════════════════════════════════════════════════════╗"))
    print(gold("  ║                                                              ║"))
    print(gold("  ║      T H E   V I S I O N S   O F                            ║"))
    print(gold("  ║      E L I S A B E T H   O F   S C H Ö N A U               ║"))
    print(gold("  ║                                                              ║"))
    print(gold("  ║      A Choose Your Own Adventure in Medieval Mysticism       ║"))
    print(gold("  ║      Schönau Monastery, Rhine Valley · c. 1152 CE            ║"))
    print(gold("  ║                                                              ║"))
    print(gold("  ╚══════════════════════════════════════════════════════════════╝"))
    print()
    print(dim("  6 chapters · 3 choices each · 4 possible endings"))
    print(dim("  No combat. No fail states. Your stats shape the ending."))
    print()
    divider(); print()
    pause("Press ENTER to begin...")

def main():
    title_screen()
    prologue()
    chapter_1()
    print()
    print(dim("  Thank you for playing."))
    print(dim("  Sources: Anne L. Clark, Elisabeth of Schönau (1992)."))
    print()

if __name__ == "__main__":
    main()