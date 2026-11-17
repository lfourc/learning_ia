#!/usr/bin/env python3
"""Transpose le Livre I hors Warhammer, sans réécrire le texte : uniquement des noms (et les accords qu'ils imposent).

Entrée  : source/livre_source_warhammer.txt (texte original, jamais modifié)
Sortie  : source/livre_source.txt             (version transposée, base du webtoon)
Rapport : source/transposition_rapport.md     (chaque remplacement, avec son contexte)

Les règles sont des expressions exactes, appliquées dans l'ordre, chacune avec le nombre
d'occurrences attendu : si le texte original change, le script s'arrête au lieu de deviner.
Table de référence : campagne/bible-univers.md § 1 (lieux, magie, dieux) et le Codex, codex/tome-0-fondations.md.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "source" / "livre_source_warhammer.txt"
DST = ROOT / "source" / "livre_source.txt"
REPORT = ROOT / "source" / "transposition_rapport.md"

# (catégorie, avant, après, occurrences attendues)
# Catégories : "table" = nom de la table validée ; "accord" = nom + accord grammatical ;
#              "proposition" = nom absent de la table, équivalent proposé ; "courant" = vent de magie → Courant.
RULES = [
    # ── Dates : années impériales − 1700 ──
    *[("table", f"{a}", f"{a - 1700}", None) for a in range(2491, 2513)],

    # ── Eldwald (Talabecland), féminin/masculin : « le Talabecland » → « l'Eldwald » ──
    ("accord", "rêves de Talabecland libre", "rêves d'Eldwald libre", 1),
    ("accord", "n'aimait le Talabecland", "n'aimait l'Eldwald", 1),
    ("accord", "parler du Talabecland", "parler de l'Eldwald", 1),
    ("accord", "il y avait le Talabecland", "il y avait l'Eldwald", 1),
    ("accord", "du Middenland, du Talabecland", "de la Nordmark, de l'Eldwald", 1),
    ("accord", "que le Talabecland voterait", "que l'Eldwald voterait", 1),
    ("table", "*Talabecland, automne", "*Eldwald, automne", 1),
    ("accord", "dans la Talabec", "dans l'Elda", 1),
    ("accord", "de Talabheim", "d'Eldenheim", 1),
    ("table", "Talabheim", "Eldenheim", 2),
    ("table", "Kreutzhofen", "Hollenhof", 2),

    # ── Nebelmark (Stirland, masc. → fém.) et la Nebel (la Stir) ──
    ("accord", "Le Stirland était pauvre, humide et méfiant.", "La Nebelmark était pauvre, humide et méfiante.", 1),
    ("accord", "du Stirland", "de la Nebelmark", 2),
    ("accord", "que le Stirland", "que la Nebelmark", 1),
    ("table", "la Stir", "la Nebel", 6),
    ("table", "La Stir", "La Nebel", 1),
    ("table", "Wurtbad", "Wendelstadt", 10),

    # ── Kronland (Reikland), l'Aldra (le Reik), Kaltenburg (Altdorf) ──
    ("accord", "entre Parravon et le Reikland", "entre Hautepierre et le Kronland", 1),
    ("table", "le Reikland", "le Kronland", 1),
    ("accord", "des péniches sur le Reik", "des péniches sur l'Aldra", 1),
    ("table", "Altdorf", "Kaltenburg", 5),

    # ── Aschenland, Monts Cendrés, Dame Voilée, Hautepierre, Aurevaux ──
    ("accord", "commençait la Sylvanie", "commençait l'Aschenland", 1),
    ("accord", "regardent vers la Sylvanie", "regardent vers l'Aschenland", 1),
    ("accord", "les Montagnes Grises", "les Monts Cendrés", 1),
    ("accord", "des Montagnes Grises", "des Monts Cendrés", 1),
    ("table", "Dame Grise", "Dame Voilée", 4),
    ("table", "Parravon", "Hautepierre", 5),
    ("accord", "des pégases qu'on voyait", "des aigles de guerre qu'on voyait", 1),
    ("accord", "les pégases tourner", "les aigles de guerre tourner", 1),

    # ── Dieux ──
    ("accord", "le chapelain de Sigmar", "le chapelain d'Haldor", 1),
    ("table", "de Morr", "de la Gardienne", 9),

    # ── Magie : Ordres, Veilleurs, Courant Gris, la Lie, la Langue Tordue ──
    ("accord", "au Collège Gris, qu'on appelle les Magisters Vigilants",
     "à l'Ordre du Voile, qu'on appelle les Veilleurs du Voile", 1),
    ("accord", "Un Magister Vigilant.", "Un Veilleur du Voile.", 1),
    ("table", "l'Ordre Gris", "l'Ordre du Voile", 2),
    ("accord", "les sorciers des Collèges", "les sorciers des Ordres", 1),
    ("accord", "vu un Collège", "vu un Ordre", 1),
    ("accord", "du Collège", "de l'Ordre", 1),
    ("accord", "au Collège", "à l'Ordre", 3),
    ("accord", "par le Collège", "par l'Ordre", 1),
    ("courant", "C'est le vent qui t'a trouvé. Ulgu. Le Vent Gris, le vent des ombres, des brumes et des mensonges. Il souffle partout, tout le temps, et presque personne ne le sent. Toi, tu le sens.",
     "C'est l'Ombre qui t'a trouvé. L'Ombre, la voie des ombres, des brumes et des mensonges. Elle souffle partout, tout le temps, et presque personne ne la sent. Toi, tu la sens.", 1),
    ("courant", "un vent qu'on ne commande pas", "une voie qu'on ne commande pas", 1),
    ("courant", "Ulgu rendait les choses simples", "L'Ombre rendait les choses simples", 1),
    ("courant", "ce qu'Ulgu peut faire", "ce que l'Ombre peut faire", 1),
    ("courant", "le Vent Gris ment aussi", "l'Ombre ment aussi", 1),
    ("courant", "Les huit vents, dit Wolfram.", "Le mana, dit Wolfram.", 1),
    ("courant", "Ne regarde pas les vents ici", "Ne regarde pas les flux ici", 1),
    ("courant", "aucun des huit", "aucun des autres flux", 1),
    ("courant", "Dhar, dit son oncle. Les vents mélangés et pourris.",
     "L'Obscur, dit son oncle. L'énergie des démons.", 1),
    ("courant", "Il avait dû entendre le vent, comme Konrad.", "Il avait dû sentir le mana, comme Konrad.", 1),
    ("courant", "savait maintenant voir les vents", "savait maintenant voir les flux", 1),
    ("courant", "des diagrammes de vents", "des diagrammes de flux", 1),
    ("accord", "— Le Magick. La langue des sorts.", "— La Langue Tordue. La langue des sorts.", 1),
    ("accord", "ressemblait à peine au Magick", "ressemblait à peine à la Langue Tordue", 1),
    ("accord", "de Magick et", "de Langue Tordue et", 1),
    ("accord", "le Magick dans sa chambre", "la Langue Tordue dans sa chambre", 1),

    # ── Politique ──
    ("table", "comtes électeurs", "princes électeurs", 2),
    ("table", "combien de comtes élisaient", "combien de princes élisaient", 2),

    # ── Noms absents de la table : équivalents PROPOSÉS (à valider) ──
    ("proposition", "Reikspiel", "kronlandais", 3),
    ("proposition", "les Bretonniens", "les Aurevalois", 1),
    ("proposition", "le bretonnien", "l'aurevalois", 2),
    ("proposition", "passée en Averland", "passée en Westerau", 1),
    ("proposition", "d'Averland", "de Westerau", 2),
    ("proposition", "les guerres de l'Âge des Trois Empereurs", "les guerres du Schisme des Deux Couronnes", 1),
    ("proposition", "Ubersreik", "Rabenfels", 1),
]

# Termes qui ne doivent plus apparaître après transposition (contrôle final)
INTERDITS = ["Talabec", "Talabheim", "Kreutzhofen", "Stirland", "la Stir", "Wurtbad", "Reikland", "Reik ", "Reikspiel",
             "Altdorf", "Sylvanie", "Montagnes Grises", "Dame Grise", "Bretonn", "bretonn", "Parravon", "pégase",
             "Sigmar", "Morr", "Ulgu", "Dhar", "Collège", "Magister", "Vigilant", "Magick", "Averland", "Middenland",
             "Ubersreik", "Trois Empereurs", "comtes électeurs", "Vent Gris", "Ordre Gris",
             "Courant", "la Lie", "Abîme", "Gisant"]


def transposer(texte: str) -> str:
    """Applique les mêmes règles à un fragment (ex. un extrait cité dans un JSON), sans contrôle de compte."""
    for _, avant, apres, _ in RULES:
        texte = texte.replace(avant, apres)
    return texte


def main() -> None:
    texte = SRC.read_text(encoding="utf-8")
    log = []
    for cat, avant, apres, attendu in RULES:
        n = texte.count(avant)
        if attendu is not None and n != attendu:
            raise SystemExit(f"Règle « {avant} » : {n} occurrence(s) trouvée(s), {attendu} attendue(s). Vérifier le texte source.")
        if n == 0:
            continue
        pos = texte.find(avant)
        ctx = texte[max(0, pos - 60):pos + len(avant) + 60].replace("\n", " ")
        texte = texte.replace(avant, apres)
        log.append((cat, avant, apres, n, ctx))

    restes = [t for t in INTERDITS if t in texte]
    DST.write_text(texte, encoding="utf-8")

    titres = {"table": "Noms de la table validée", "accord": "Noms avec accord grammatical ajusté",
              "courant": "Magie : vocabulaire du Codex v5.2 (l'Ombre, le mana, les flux, l'Obscur) ; le vent météo est conservé",
              "proposition": "⚠️ Noms absents de la table — équivalents PROPOSÉS, à valider"}
    out = ["# Rapport de transposition du Livre I", "",
           "Seuls des noms ont été remplacés (et les accords qu'ils imposent). Texte original intact dans "
           "`source/livre_source_warhammer.txt`. Table : `campagne/bible-univers.md` § 1 et Codex v5.2.", "",
           f"**{sum(x[3] for x in log)} remplacements**, {len(log)} règles. "
           f"Termes Warhammer restants : {', '.join(restes) if restes else 'aucun'}.", ""]
    for cat in ("proposition", "courant", "accord", "table"):
        rows = [x for x in log if x[0] == cat]
        if not rows:
            continue
        out += [f"## {titres[cat]}", "", "| Avant | Après | Fois | Contexte (avant) |", "|---|---|---|---|"]
        for _, a, b, n, ctx in rows:
            out.append(f"| {a} | {b} | {n} | …{ctx.replace('|', '/')}… |")
        out.append("")
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(f"{sum(x[3] for x in log)} remplacements ; restes : {restes or 'aucun'}")


if __name__ == "__main__":
    main()
