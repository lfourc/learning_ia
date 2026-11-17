# PROJET : PIPELINE DE PRODUCTION WEBTOON IA (STYLE MANHWA CORÉEN)

## 1. OBJECTIF DU PROJET
Ce projet vise à transformer un roman/récit source en français (environ 30 pages) en un webtoon complet au format vertical (scroll mobile), en automatisant :
1. L'extraction et l'adaptation narrative (règles manhwa coréen).
2. La cohérence de l'univers via une Bible/Codex évolutif.
3. La génération d'images en masse à moindre coût via API (Fal.ai - Flux.1).
4. L'assemblage vertical automatique des planches avec gestion des respirations (espaces vides).

---

## 2. ARCHITECTURE DES DOSSIERS
```text
/webtoon-pipeline
├── CLAUDE.md                  # Ce fichier d'instructions système
├── /codex
│   ├── 01_BIBLE_MONDE.md      # Fiches personnages (tokens), lieux, lore, profils vocaux
│   └── /references            # Images de référence des visages (ex: kael_ref.png)
├── /source
│   └── livre_source.txt       # Texte source de l'histoire (en français)
├── /scripts
│   └── generate_webtoon.py    # Script Python (Appel API Fal.ai + Assemblage Pillow)
├── /output
│   ├── /json                  # Scripts découpés par chapitre (chapitre_01.json)
│   ├── /panels                # Cases individuelles générées (panels/chapitre_01/{draft,final}/case_01.png)
│   └── /strips                # Planches verticales finales assemblées (800px de large)
├── requirements.txt
├── .env.example               # Modèle : copier en .env et y mettre FAL_KEY
└── .env                       # Contient FAL_KEY=votre_cle_api (NON versionné)
```

---

## 3. DIRECTIVES DU SKILL « RÉALISATEUR & SCÉNARISTE MANHWA »

Lorsque tu adaptes un extrait de `/source/livre_source.txt` en script de webtoon, applique **impérativement** les 4 règles suivantes :

### A. Rythme Vertical (Scroll-Pacing)
- **Format Mobile :** Pense chaque scène en une colonne unique de `800px` de large. Une seule action majeure ou un seul échange par écran.
- **Gestion du vide (Gouttières) :** Spécifie explicitement la hauteur de l'espace vide après chaque case (`espace_apres_px`) :
  - `150px` à `250px` : Dialogue rapide ou enchaînement d'action fluide.
  - `500px` à `900px` : Tension dramatique, changement de lieu, ou préparation d'un coup critique (préciser si fond blanc ou dégradé noir).
- **Cliffhanger :** Termine chaque chapitre sur une case haute (`9:16`) à fort impact émotionnel ou visuel.

### B. Cinématographie & Prompts Visuels (En Anglais Technique)
- **Langue :** Les dialogues et SFX sont en **français**, mais le champ `image_prompt` doit toujours être rédigé en **anglais**.
- **Structure stricte du prompt :** `[Angle/Cadrage] + [Token Personnage issu du Codex + Expression/Action précise] + [Décor issu du Codex] + [Éclairage & Effets Manhwa] + [Style global]`.
- **Angles dynamiques obligatoires pour l'action :** Interdiction des plans moyens plats. Utilise : `extreme low-angle shot`, `dutch angle`, `fisheye lens distortion`, `dynamic foreshortening`, `close-up on eyes`.
- **Effets visuels Manhwa :** Intègre `radial speed lines`, `motion blur`, `impact frames`, `glowing aura particles`, `dramatic rim lighting`, `high quality Korean webtoon art style, cel shaded, sharp lineart`.
- **Décomposition de l'action :** Découpe toute attaque puissante en 3 micro-cases : 1. Préparation (gros plan œil/arme) -> 2. Exécution (mouvement flouté en diagonale) -> 3. Impact (case verticale haute avec onde de choc).

### C. RÈGLES D'OR DES DIALOGUES (ANTI-ROBOT)
Interdiction formelle d'écrire des dialogues littéraires, théâtraux ou explicatifs. Un personnage de webtoon ne fait jamais de phrases complètes quand il est sous pression.

**1. Interdit (exemples de rejet) :**
- ❌ *Trop poli / théâtral :* « Je ne m'attendais pas à te voir ici, Kael. Que viens-tu faire dans ce lieu ? »
- ❌ *Explicatif (le personnage raconte ce qu'il fait) :* « Je vais concentrer mon énergie dans mon épée pour briser ta garde ! »
- ❌ *Émotion nommée :* « Je ressens une profonde colère face à ta trahison ! »

**2. Standard manhwa à la place :**
- ✅ *Sec, sous-entendu, naturel :* « Kael... ? Qu'est-ce que tu fous là ? »
- ✅ *Action pure (un bruit ou un mot) :* [SFX : CRACK] → « Crève. »
- ✅ *Émotion montrée par le rythme :* « T'as vraiment osé... » / (case suivante, gros plan œil) / « ...espèce d'enfoiré. »

**3. Méthode en 2 passes obligatoires, pour chaque réplique, avant d'écrire le JSON :**
- **Passe 1 (Extraction) :** ce que le personnage veut dire selon le livre.
- **Passe 2 (Charcutage) :** couper 60 % des mots. Supprimer les sujets (« Je », « Tu ») quand le contexte est évident. Oralité française réelle (« T'es », « Y a », « Fous », « Putain », « Sérieux ? »). Remplacer les explications par du sarcasme, des questions rhétoriques ou du silence (`...`).

**Registre propre à La Lame-Grise (prime sur les exemples d'oralité ci-dessus) :**
Court, sec, sous-entendu, mais **langue d'époque**. Référence : les épisodes 1 et 2 (« Range ta langue. », « Pas mal, la mouche. », « Albrecht. Entre. Et dis-le vite. », « Je ne cours jamais. »).
- **Interdit** : argot et tics modernes (« putain », « fous », « sérieux ? », « genre », « grave », « pisser le sang », « ok ») et contractions écrites (« j'vous », « t'as », « t'étais », « y a »). Le « ne » peut tomber dans une réplique orale (« J'ai rien vu. »), sans plus.
- **À la place de l'insulte** : la pique, l'ironie, le mot retourné contre l'autre, le surnom moqueur et tendre (Brunhild : « la mouche » ; Gisela : « la souris »).
- **Vouvoiement** : les enfants vouvoient leur père ; on vouvoie un inconnu ; Wolfram tutoie Ottilie (il la regarde de haut), elle le vouvoie.
- **Profils vocaux** :
  - *Ottilie* : effrontée, réplique du tac au tac, reprend les mots des autres pour les retourner, nie l'évidence (« Pas du tout. »).
  - *Wolfram* : le moins de mots possible, impératifs, n'explique jamais, ne donne pas son nom.
  - *Gisela* : attaque par l'observation (« Tu as de la mousse dans les cheveux. »), ordres brefs.
  - *Ruprecht* : impératifs en trois temps, ne justifie rien.
  - *Matthias* : vantard, exclamations, exagère tout.
  - *Brunhild* : proverbes, pipe, « la mouche ».

**Toujours valable :**
- **Show, don't tell :** pas de narration descriptive reprise du livre ; si l'image montre l'émotion ou l'action, le texte disparaît.
- **15 mots maximum par bulle** (viser 2 à 6). Une réplique longue = deux bulles ou deux cases.
- **Profil vocal** de chaque personnage (`codex/personnages-principaux.md` pour Ottilie, Konrad, Wolfram ; `webtoon/personnages-arnsfeld.md` pour la maison d'Arnsfeld) : personne ne parle comme un livre.
- **Typologie :** `dialogue` (bulle parlée), `pensee` (texte flottant/encadré interne), `cri` (bulle hérissée), `sfx` (onomatopée intégrée à l'action, ex. *CRASH*, *FWOOSH*), `narration` (encadré, à réduire au strict minimum).
- `generate_webtoon.py` signale les tournures interdites détectables (émotion nommée, « je vais … pour … », bulles trop longues, argot moderne) **et le vocabulaire interdit** (noms Warhammer, termes périmés du Codex, voir § 8) dans les bulles, le SFX et les prompts : corriger avant de générer.

### D. Cohérence & Évolution du Codex
- Avant de générer un chapitre, lis `/codex/01_BIBLE_MONDE.md` pour récupérer les tokens visuels exacts des personnages et des lieux.
- Si l'extrait du livre introduit un nouveau personnage, un lieu récurrent ou un pouvoir, propose immédiatement une mise à jour de `01_BIBLE_MONDE.md` à la fin de ta réponse.

---

## 3 bis. MÉTHODE DE TRAVAIL PAR ÉPISODE (OBLIGATOIRE, DANS CET ORDRE)
0. **Le Codex et l'index font foi** : avant tout manuscrit, lire `claude/index-du-projet.md` (quel document fait foi sur quel sujet), `codex/tome-0-fondations.md`, `codex/personnages-principaux.md`, `webtoon/personnages-arnsfeld.md` et `webtoon/saison-01-plan.md` (numéros et contenu des épisodes). **Aucune scène ne s'écrit sur une zone floue** : une question sans réponse dans ces documents va dans `claude/decisions-ouvertes.md` (registre unique, aucune liste « à décider » ailleurs), pas dans une invention. Ces documents servent d'appui au même titre que le livre (`> 📐 Appui : Codex, § 3.6`).
1. **Manuscrit en prose** : `manuscrits/epNN_slug.md`. L'épisode écrit comme un court chapitre (scènes, gestes, répliques au registre de la série). Chaque scène commence par un bloc **Appui** : extraits **exacts** du livre transposé (`> « … »`), ou `🆕 invention` expliquée, et les écarts assumés. En fin de fichier : les **points à trancher**.
2. **Correction par l'auteur** : il modifie librement le manuscrit. **Rien n'est découpé tant qu'il ne l'a pas validé.**
3. **Découpage en cases** : `output/json/chapitre_NN.json`. Chaque case cite **mot pour mot** une phrase du manuscrit validé : `"source": {"manuscrit": "manuscrits/epNN_slug.md", "ref": "Scène 2", "extrait": "<phrase exacte>"}`. Les répliques sont reprises **telles quelles** du manuscrit (aucune réécriture au découpage). `generate_webtoon.py` vérifie que chaque extrait existe dans le manuscrit.
4. **Relecture** : `python scripts/relecture.py -c NN`, puis validation.
5. **Génération d'images** seulement ensuite (`--dry-run`, puis `--mode draft`, puis `--mode final`).

## 4. FORMAT DE SORTIE JSON OBLIGATOIRE

Chaque chapitre généré doit être sauvegardé dans `/output/json/chapitre_XX.json` selon ce schéma exact :

```json
{
  "chapitre": 1,
  "titre": "Titre de l'épisode",
  "cases": [
    {
      "id": "case_01",
      "format": "9:16",
      "image_prompt": "Extreme low-angle shot, [TOKEN_PERSONNAGE] standing on a dark rooftop, cold piercing gaze, wind blowing coat, neon city skyline at night, dramatic rim lighting, Korean manhwa style, cel shaded, sharp lineart",
      "reference_image": "kael_ref.png",
      "dialogues": [
        {
          "personnage": "Kael",
          "type": "pensee",
          "texte": "Ils pensaient vraiment que c'était fini ?"
        }
      ],
      "sfx": "WHOOSH",
      "transition_fond": "noir",
      "espace_apres_px": 500
    }
  ]
}
```

**Traçabilité obligatoire (source de chaque case) :**
- Chaque case porte un champ `source` :
  - soit `{"ref": "Livre I, ch. 1, § III. Le chasseur", "extrait": "<texte EXACT copié de source/livre_source.txt>", "note": "<écart ou transposition, optionnel>"}` (`extrait` peut être une liste de plusieurs passages) ;
  - soit `{"invention": "<ce qui est inventé et pourquoi>"}` quand la case n'a pas d'appui dans le livre.
- Chaque réplique porte un champ `intention` = la **passe 1** (ce que le personnage veut dire), à côté de `texte` = la **passe 2** (la réplique finale).
- Les extraits sont **copiés, jamais réécrits** : `generate_webtoon.py` vérifie qu'ils existent mot pour mot dans le livre et signale toute case sans source.
- `python scripts/relecture.py -c N` produit la version lisible avec, pour chaque case, l'extrait cité, l'intention et la réplique : c'est le document de travail pour améliorer le texte et la génération.

Exemple :
```json
"source": {"ref": "Livre I, ch. 1, § III. Le chasseur", "extrait": "Il aurait pu la tuer dix fois."},
"dialogues": [{"personnage": "Wolfram", "type": "dialogue", "intention": "Il veut qu'elle parte et oublie ce qu'elle a vu.", "texte": "Va-t'en."}]
```

Valeurs acceptées par le script :
- `format` : tout ratio `L:H` (`9:16`, `4:5`, `1:1`, `3:4`, `16:9`…). L'image est générée à ~1 MP puis redimensionnée à 800px de large.
- `transition_fond` : `noir`, `blanc`, `degrade_noir` (blanc → noir), `degrade_blanc` (noir → blanc).
- `type` de dialogue : `dialogue`, `pensee`, `cri`, `sfx` (et `narration`, à éviter).
- `reference_image` : nom de fichier dans `/codex/references/`, ou `null`.

---

## 5. SPÉCIFICATIONS DU SCRIPT PYTHON (`generate_webtoon.py`)

Lorsque l'utilisateur te demande de créer ou mettre à jour `/scripts/generate_webtoon.py`, code un script robuste avec les fonctionnalités suivantes :
1. **Mode Économique vs Mode Final :**
   - Flag `--mode draft` : Utilise `fal-ai/flux/schnell` (coût ~0.003$/image, 4 steps) pour valider le découpage et le rythme en quelques secondes.
   - Flag `--mode final` : Utilise `fal-ai/flux/dev` ou `fal-ai/flux-pulid` (si `reference_image` est renseigné dans le JSON) pour verrouiller le visage du personnage.
2. **Génération Ciblée :** Flag `--case case_05` permettant de ne régénérer qu'une seule case modifiée dans le JSON sans repayer tout le chapitre.
3. **Assemblage Automatique (Pillow) :**
   - Redimensionne chaque image générée à une largeur fixe de `800px` en conservant le ratio.
   - Crée une ou plusieurs bandes verticales (découpées tous les `10000px` de hauteur maximum pour éviter les limites de taille des plateformes comme Webtoon Canvas).
   - Insère automatiquement les espaces vides (`espace_apres_px`) avec la couleur demandée (`noir` ou `blanc`) entre chaque case.
   - Exporte un fichier `planche_texte.txt` récapitulant les dialogues case par case pour faciliter le lettrage final sous Clip Studio Paint ou Canva.

---

## 6. COMMANDES DE DÉMARRAGE POUR CLAUDE CODE
- **"Initialise le projet"** -> Crée toute l'arborescence, installe les dépendances (`fal-client`, `pillow`, `python-dotenv`) et génère `generate_webtoon.py`.
- **"Analyse mon texte et crée le Codex"** -> Lit `/source/livre_source.txt` et remplit `/codex/01_BIBLE_MONDE.md` avec les fiches personnages, tokens anglais et profils vocaux.
- **"Génère le chapitre X"** -> Découpe la partie correspondante du livre en `/output/json/chapitre_X.json` en appliquant toutes les règles Manhwa.

---

## 7. UTILISATION DU SCRIPT (depuis `webtoon-pipeline/`)
```bash
pip install -r requirements.txt
cp .env.example .env            # puis renseigner FAL_KEY
python scripts/relecture.py -c 1                        # version lisible du JSON (chapitre_01_relecture.md)
python scripts/generate_webtoon.py -c 1 --dry-run          # gratuit : images factices, valide le rythme
python scripts/generate_webtoon.py -c 1 --mode draft       # flux/schnell, ~0.003$/image
python scripts/generate_webtoon.py -c 1 --mode final       # flux/dev, ou flux-pulid si reference_image
python scripts/generate_webtoon.py -c 1 --mode final --case case_05   # ne repaie qu'une case
python scripts/generate_webtoon.py -c 1 --assemble-only    # réassemble sans appel API
```
Options utiles : `--force` (régénère même si l'image existe), `--seed 42`, `--max-height 10000`, `--format jpg`, `-y` (pas de confirmation de coût), `--no-assemble`.
Les images déjà générées sont réutilisées (pas de double paiement). L'assemblage prend la version `final` d'une case si elle existe, sinon `draft`.
Sorties : `output/strips/chapitre_XX/planche_NN.png` + `planche_texte.txt` (dialogues + position Y de chaque case, pour le lettrage).

---

## 8. PROJET EN COURS : « LA LAME-GRISE »
Le monde est travaillé dans le projet claude.ai « Jdr- Wagram et » et synchronisé ici par paquets (dernier : `claude/sync-2026-11-17.md`, 17/11/2026). **L'œuvre ne contient aucune référence à Warhammer** ; le jeu (JDR) reste en Warhammer, hors du studio.

**Lire en premier : `claude/index-du-projet.md`.** Il désigne, sujet par sujet, le document qui fait foi ; en cas de conflit, c'est lui qui tranche. En résumé :

| Sujet | Fait foi |
|---|---|
| Règles du monde, magie (mana, Noyau, cinq voies, Cercles), dieux, Huitième et pacte ottilien, Main Grise, histoire, lexique | `codex/tome-0-fondations.md` (v5.2) |
| Peuples, créatures, petit obscur | `codex/tome-1-bestiaire.md` ; lieux minces : `codex/lieux-minces.md` |
| Ottilie, Konrad, Wolfram, Jobst (personnalité, magie, voix) | `codex/personnages-principaux.md` |
| La maison d'Arnsfeld | `webtoon/personnages-arnsfeld.md` |
| Apparence de tous les personnages | `campagne/bible-visuelle-livre-1.md` (v3) |
| Lieux | `campagne/bible-decors-livre-1.md` (v3) |
| Noms (jeu → œuvre) | `campagne/bible-univers.md` (§ 1.4 : noms ajoutés dans le studio le 16/11) |
| Numéros et contenu des épisodes (26) | `webtoon/saison-01-plan.md` (v6) |
| Couleurs de la magie à l'image (contrôle d'image) | `webtoon/monde-et-introduction.md` § 2.3 |
| Magie en action, dialogues | `webtoon/action-et-dialogues.md`, `webtoon/bible-ecriture-webtoon.md` (modificateurs de prompt par voie) |
| Ce qui reste à décider | `claude/decisions-ouvertes.md` |

**Vocabulaire périmé, interdit dans les prompts et les bulles** (contrôlé par `generate_webtoon.py`) :
- « la Lie » → **l'Obscur** ; « Sang-de-Lie » → **Sang-Noirs** ;
- « Courant » au sens d'un Ordre ou d'une couleur de magie → **Ordre** (ou la **voie** : Souffle, Vif, Éther, Don, Ombre) ;
- « avoir l'oreille » → **un Noyau éveillé** ; « [l'œil] » → **l'Œil des Limbes** ; « [Dieu d'Entre-Deux] » → **le Huitième** ;
- « l'Abîme » → **l'Envers** (le monde des démons) ; « l'Abysse » = le vide où dorment les dieux anciens ; « Gisant » : supprimé ;
- et aucun nom Warhammer (Ulgu, Dhar, Collège, Stir, Talabec, Altdorf, Sigmar, Morr…).

**Le studio (ce dépôt) :**
- `source/livre_source.txt` — **Livre I « Origines »**, v1 transposée mécaniquement hors Warhammer par `scripts/transposer_livre.py` à partir de `source/livre_source_warhammer.txt` (original, ne jamais modifier) : des noms, et le vocabulaire de magie du Codex v5.2 ; chaque remplacement est dans `source/transposition_rapport.md`. **Le Livre I v2 sera réécrit dans le projet claude.ai** (chantier ouvert) : d'ici là, cette version sert à citer l'intrigue, pas à trancher une règle du monde (le Codex prime).
- `codex/01_BIBLE_MONDE.md` — tokens de prompt de 23 personnages et 19 lieux, dérivés des Planches (`codex/planches.json`, données brutes en vocabulaire de jeu). **Ne fait pas foi** : en cas d'écart, la bible visuelle et la bible des décors l'emportent.
- Images de référence : `codex/references/<id>_ref.jpg` (47 planches validées + Wolfram jeune et Moustache repris des épisodes ; index `codex/references/INDEX.md`). Ex. `c1_ref.jpg` = Konrad, `L2_ref.jpg` = manoir d'Arnsfeld. `"reference_image": "c1_ref.jpg"` active `flux-pulid` en mode final. **Konrad n'a plus de cicatrice à la lèvre** (16/11) : vérifié le 17/11, `c1_ref.jpg` n'en montre pas ; ses tokens dans `01_BIBLE_MONDE.md` ont été corrigés.
- Épisodes : `output/json/chapitre_01.json` (Les abeilles de Brunhild, 63 cases) et `chapitre_02.json` (Le sceau, 51 cases), **publiés**, images finales dans `output/panels/chapitre_0X/final/` ; prompts d'origine perdus (`image_prompt` vide) ; les bulles gardent leur position (`x,y,w` = coin et largeur en % de la case, `tx,ty` = pointe de la queue). À faire selon `webtoon/ep01-coda-et-ep02-plan.md` et `claude/decisions-ouvertes.md` : **la nouvelle page 18 de l'épisode 2** (Wolfram n'est plus blessé ; références : Ottilie, Moustache, page de style, **pas Wolfram**) et le relettrage de l'épisode 1 (cases 1.31 et 1.55, décision n° 1).
- Prochain épisode : **épisode 3 « La dernière journée »** (automne 791 ; plan de saison v6), à partir de `ep01-la-derniere-journee-v2.md` (projet claude.ai, absent du paquet du 17/11) ; le script v1 est dans `codex/archives/ep01_la_derniere_journee_script.md`.
- `archives/studio-2026-11-16/` : plan des fondations et brouillon « Le chasseur », remplacés par le paquet du 17/11.

Règles propres à la série (priment sur la section 3 en cas de conflit) : jamais de croix chrétienne, crucifix ni fleur de lys ; ne jamais citer de titres de référence dans les prompts ; l'Ombre = brume grise translucide aux reflets argentés, et chaque voie a sa couleur (`webtoon/monde-et-introduction.md` § 2.3) ; les objets récurrents (bague au tilleul couronné, sceau) ont une image de référence obligatoire ; ne pas redécrire les costumes quand une planche de référence est jointe.
