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

**Toujours valable :**
- **Show, don't tell :** pas de narration descriptive reprise du livre ; si l'image montre l'émotion ou l'action, le texte disparaît.
- **15 mots maximum par bulle** (viser 2 à 6). Une réplique longue = deux bulles ou deux cases.
- **Profil vocal** de chaque personnage (`codex/bibles/bible_personnages.md`) : la grossièreté se dose selon le personnage, mais personne ne parle comme un livre.
- **Typologie :** `dialogue` (bulle parlée), `pensee` (texte flottant/encadré interne), `cri` (bulle hérissée), `sfx` (onomatopée intégrée à l'action, ex. *CRASH*, *FWOOSH*), `narration` (encadré, à réduire au strict minimum).
- `generate_webtoon.py` signale les tournures interdites détectables (émotion nommée, « je vais … pour … », bulles trop longues) : corriger avant de générer.

### D. Cohérence & Évolution du Codex
- Avant de générer un chapitre, lis `/codex/01_BIBLE_MONDE.md` pour récupérer les tokens visuels exacts des personnages et des lieux.
- Si l'extrait du livre introduit un nouveau personnage, un lieu récurrent ou un pouvoir, propose immédiatement une mise à jour de `01_BIBLE_MONDE.md` à la fin de ta réponse.

---

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

## 8. PROJET EN COURS : « LA LAME-GRISE » (ressources reprises des artifacts claude.ai)
Ce pipeline est appliqué à **La Lame-Grise** (Konrad von Eichenwald, univers d'Erdheim). Avant tout travail, lire :
- `source/livre_source.txt` — **Konrad — Livre I : Origines** (7 chapitres), le texte source à adapter.
- `codex/01_BIBLE_MONDE.md` — tokens visuels de 23 personnages et 19 lieux + blocs de style/négatif (données brutes : `codex/planches.json`).
- `codex/bibles/` — `bible_personnages.md` (apparence, âges, voix), `bible_decors.md` (lieux, script couleur), `tome0_fondations.md` (magie, dieux, histoire, rangs), `tome1_bestiaire.md`, `bible_univers.md` (transposition hors Warhammer : **ne jamais réutiliser les noms Warhammer** — Reikland, Sigmar, Morr, Ulgu… → voir la table de transposition), `kit_chatgpt.md`.
- `codex/archives/` — anciens scripts (épisode 1 « La dernière journée », découpage ch. 1 du livre).
- `output/json/chapitre_01.json` (Les abeilles de Brunhild, 63 cases) et `chapitre_02.json` (Le sceau, 51 cases) — épisodes **déjà publiés**, images finales dans `output/panels/chapitre_0X/final/`. Leurs prompts d'origine sont perdus (`image_prompt` vide) ; les bulles gardent leur position (`x,y,w` = coin et largeur en % de la case, `tx,ty` = pointe de la queue).
- Épisode 3 « Le chasseur » : brouillon dans `output/json/chapitre_03.json` (relecture : `chapitre_03_relecture.md`), en attente de validation par l'auteur.

Règles propres à la série (priment sur la section 3 en cas de conflit) : jamais de croix chrétienne, crucifix ni fleur de lys ; ne jamais citer de titres de référence dans les prompts ; le Gris = brume grise translucide aux reflets argentés ; les objets récurrents (bague au tilleul couronné, sceau) ont une image de référence obligatoire ; ne pas redécrire les costumes quand une planche de référence est jointe.
Images de référence : `codex/references/<id>_ref.jpg` (47 planches validées, reprises de l'artifact « Planches — Livre I » ; index dans `codex/references/INDEX.md`). Ex. `c1_ref.jpg` = Konrad, `L2_ref.jpg` = manoir d'Arnsfeld. Les `_v1`, `_v2` sont d'autres âges ou versions antérieures. Seul le faux copiste (`c12`) n'a pas encore de planche. Dans un JSON de chapitre : `"reference_image": "c1_ref.jpg"` active `flux-pulid` en mode final.
