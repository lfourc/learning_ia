# Bible visuelle — Livre I (personnages)

*Character design pour les fiches et la future BD. Style : manhwa / webtoon d'action-fantasy. Version 1, 14/11/2026.*

---

## 0. Mode d'emploi

**Galerie des planches** (prompts à copier, images à déposer, référence à choisir) : https://claude.ai/artifact/LqfQNCNN2Dh72uzC5GSgcH

**Règle de cohérence.** Pour chaque personnage, on génère d'abord une **planche de référence** (face / trois-quarts / dos, fond neutre). On garde la meilleure image, puis on s'en sert comme référence pour toutes les autres (Midjourney : `--cref <url>` ; ChatGPT / autres : joindre l'image et écrire « same character as reference »). Sans cette étape, le visage change à chaque image.

**Les prompts sont en anglais** : les générateurs les suivent mieux. Les descriptions restent en français.

**Bloc de style commun** (à coller à la fin de chaque prompt) :

```
Korean webtoon manhwa art style, sharp clean lineart, cel shading with soft gradients, dramatic cinematic lighting, strong rim light, muted desaturated palette with one accent color, detailed fabric and leather, dark low-fantasy medieval setting, high detail, character reference sheet quality
```

**Négatif commun** (si l'outil le permet) :

```
chibi, cartoonish, 3D render, photo, plate armor everywhere, modern clothing, text, watermark, extra fingers, deformed hands, christian cross, crucifix, Virgin Mary, christian saints, fleur-de-lis, grain noise, speckles
```

**Variantes d'âge** : toujours générer à partir de la référence validée du personnage (image jointe). Les prompts d'âge commencent par « Same character as the reference image » pour que le visage reste le même.

**Midjourney** : ajouter `--ar 2:3 --niji` pour un portrait en pied, `--ar 3:2` pour une planche face/profil/dos.

### Langage visuel du manhwa
- **Ulgu = brume grise.** La magie de Konrad et de Wolfram n'est jamais lumineuse : fumée grise qui monte, contours qui se brouillent, reflets argentés dans les yeux. Contraste voulu avec les « auras » colorées habituelles du genre.
- **Une couleur d'accent par personnage** (voir chaque fiche). Konrad est gris sur gris, avec une seule touche d'or : la bague.
- **Trois familles de couleurs** : Eichenwald = vert chêne et brun ; Arnsfeld (sang ottilien) = bordeaux et or terni ; Ordre Gris = gris, ardoise, argent.

### Transposition hors Warhammer
La BD finale sortira de l'univers Warhammer. Tous les designs évitent les marqueurs trop canon (pas de symboles de Sigmar lisibles, pas d'armes ou d'emblèmes officiels). À remplacer au moment du passage :

| Warhammer | Équivalent neutre |
|---|---|
| Collège Gris / Ulgu | Ordre des Ombres / magie de brume |
| Magister Vigilant | Traqueur de mages renégats |
| Sigmar (chapelain) | Dieu-guerrier, symbole : marteau stylisé → à redessiner |
| Morr (chapelle, registre) | Dieu des morts, symbole : corbeau / porte |
| Empire, Stirland, Talabecland | Empire et provinces à renommer |
| Sang ottilien | Lignée d'une ancienne impératrice déchue |

---

## 1. Konrad von Eichenwald — « la Lame-Grise »

**Rôle** : héros. Bâtard officiel du baron, en réalité fils de Wolfram et dernier du sang ottilien.
**Âge de référence** : 18 ans (2512). Variantes : 8 ans (la cour d'armes), 12 ans (la brume sur la Stir).
**Couleur d'accent** : or terni (la bague).

- **Silhouette** : grand, élancé, nerveux. Pas la carrure de Lothar : épaules fines, gestes économes. Il se tient droit comme un noble, mais toujours légèrement de biais, prêt à esquiver (« une guêpe »).
- **Visage** : traits fins, pommettes marquées, mâchoire étroite. Visage fermé, le « masque » appris à la maison forte. Une petite cicatrice à la lèvre inférieure (le coup de Lothar à 8 ans).
- **Yeux** : **clairs, presque dorés, tirant sur le vert**. Ni le bleu d'Ottilie, ni le noir des Eichenwald. Dans un visage gris sur gris, ce sont eux qui accrochent la lumière. Pour Ottokar, ce sont des yeux clairs comme ceux de Mathilde : « Tu as ses yeux. Tu n'as rien de moi. » Les « yeux sombres » du nouveau-né au chapitre 2 restent justes (tous les bébés naissent avec des yeux foncés). Quand il canalise Ulgu, l'or s'éteint en argent et des volutes de brume montent au coin des yeux.
- **Cheveux** : **châtain**. Mi-longs, mèches qui tombent sur le front, souvent attachés en catogan bas pendant l'action.
- **Peau** : claire, celle de sa mère. Contraste visible à table avec les Eichenwald, tannés par le grand air.
- **Ironie visuelle** : Konrad ne ressemble à aucun Eichenwald, Wolfram compris. Personne ne peut le relier à son vrai père par la couleur, ce qui protège le secret. La parenté ne se lit que dans la forme : même mâchoire, même maigreur, même façon de se tenir dans l'ombre.
- **Tenue de route** : cape grise à capuche, usée, ourlet effiloché ; pourpoint de cuir sombre ajusté sur chemise de lin écru ; pantalon sombre, bottes souples. Ceinture croisée portant les deux lames.
- **Tenue noble** : pourpoint gris anthracite à col montant, boutons d'étain, pas d'armoiries (il n'en a pas le droit). Élégant mais sans éclat.
- **Objets signature** (toujours visibles, c'est son identité graphique) :
  - la **bague** d'Ottilie au bout d'un cordon de cuir, au cou, armes effacées : seul point doré du personnage ;
  - la **dague grise** de Wolfram (main droite), lame mate, garde simple ;
  - le **couteau à écorcer** de sa mère (main gauche), petite lame courbe, souvent tenue à l'envers comme Ottilie dans la chapelle ;
  - les **gants de cuir fin** de Rüdiger, usés, couleur tabac ;
  - la **boîte de métal** cabossée (grimoire), en bandoulière dans une besace.
- **Attitude / expressions clés** : regard en coin ; silence ; demi-sourire très rare ; colère froide (mâchoire serrée, yeux qui s'assombrissent).
- **Palette** : `#2B2D31` anthracite · `#6B6E73` gris cape · `#4A3A2C` cuir · `#E8E1D3` lin · accent `#B8963E` or terni.

**Prompt — 18 ans, planche de référence**
```
Character reference sheet, front view, three-quarter view and back view, young man 18 years old, tall lean agile build, sharp fine facial features, high cheekbones, fair skin, small scar on lower lip, striking pale eyes almost golden with a green tint, chestnut brown shoulder-length hair with strands over the forehead tied in a low ponytail, worn grey hooded cloak, slightly frayed at the hem but intact, not torn or ragged, fitted dark leather doublet over off-white linen shirt, dark trousers, soft leather boots, thin worn tobacco-brown leather gloves, a small plain grey steel dagger on the right hip, short hand-length blade with a minimal guard, clearly a dagger and not a sword, and a small curved bark-peeling knife on the left, a tarnished gold signet ring hanging on a leather cord around his neck, dented metal box in a shoulder satchel, cold composed expression, noble posture slightly turned sideways, plain light grey background
```

**Prompt — scène, magie d'Ulgu**
```
Young man in a grey hooded cloak crouching on a rooftop at night, a small plain grey dagger with a hand-length blade in one hand and a small curved knife held in reverse grip in the other, grey mist rising from his shoulders and swallowing his outline, his golden-green eyes fading to silver, tarnished gold ring on a cord swinging from his neck, moonlit medieval town below, low angle, dramatic
```

**Prompt — 8 ans**
```
Thin quiet fair-skinned boy 8 years old, messy chestnut hair, pale golden-green eyes, coarse wool clothes too plain for a noble courtyard, split lower lip bleeding, holding a wooden practice sword, standing alone in a rainy castle training yard, defiant silent stare
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 5 ans | 2499 | 3 | Petit, maigre, cheveux châtains en bataille, vêtements de laine simples. Pas encore de bague. |
| 8 ans | 2502 | 3–4 | Lèvre fendue (le coup de Lothar). À partir de la mort de sa mère : la bague au cou. |
| 12 ans | 2506 | 5 | Grand et maigre, habits de domestique trop courts, couteau à écorcer. Vit dans le réduit. |
| 15 ans | 2509 | 6 | Presque adulte, deux lames, se déplace sans bruit. Il a battu Lothar. |
| 18 ans | 2512 | 7 | Référence principale. |

**Prompt — 5 ans (planche)**
```
Same character as the reference image, now a small thin boy 5 years old, fair skin, messy chestnut hair, pale golden-green eyes, plain undyed wool tunic and trousers, bare feet, standing among bundles of drying herbs in a cottage, one finger raised to his lips, serious quiet expression, character reference sheet front and side views
```

**Prompt — 12 ans (planche)**
```
Same character as the reference image, now a lanky thin boy 12 years old, fair skin, chestnut hair grown long and unkempt, pale golden-green eyes, faint scar on lower lip, servant's hand-me-down clothes too short at the wrists, a tarnished gold ring on a leather lace under his shirt, small curved bark-peeling knife in his hand, guarded watchful expression, character reference sheet front, three-quarter and back views
```

**Prompt — 15 ans (planche)**
```
Same character as the reference image, now a lean teenage boy 15 years old, growing tall, sharper face, fair skin, chestnut hair tied back, pale golden-green eyes, faint scar on lower lip, dark plain practical clothes, a small plain grey dagger and a small curved bark-peeling knife, tarnished gold ring on a leather cord around his neck, light silent stance on the balls of his feet, character reference sheet front, three-quarter and back views
```

---

## 2. Wolfram von Eichenwald — « l'oncle gris »

**Rôle** : sorcier gris, Magister Vigilant, vrai père de Konrad. Ne peut rien dire.
**Âges** : né en **2460**, cadet d'Ottokar de deux ou trois ans. **32 ans** en 2492 (la chapelle), **52 ans** en 2512 (Parravon), **60 ans** vers 2520 (retour possible dans la campagne).
**Couleur d'accent** : argent froid.

- **Silhouette** : maigre, long, un peu voûté par la fatigue. Il prend peu de place et semble toujours appuyé contre un mur ou un pilier, dans l'ombre.
- **Un Eichenwald** : cheveux noirs, yeux noirs, peau tannée par le soleil, comme son frère. Mais là où Ottokar est massif, Wolfram est sec et maigre : même sang, autre vie.
- **Visage** : creusé, joues maigres, peau tannée. En 2512, rides de fatigue profondes, barbe courte poivre et sel mal entretenue ; rasé de près en 2492. Ressemblance discrète avec Konrad, par la forme seulement : même ligne de mâchoire, même maigreur. Le lecteur doit pouvoir la voir, pas les personnages.
- **Yeux** : **noirs**. En manhwa : deux points sombres, sans reflet, dans l'ombre de la capuche.
- **Cheveux** : **noirs**, tirés en arrière, longs jusqu'à la nuque. En 2512, gris aux tempes et mèches grises.
- **Tenue** : longue cape grise de l'Ordre, épaisse, qui traîne presque au sol, capuche profonde ; vêtements gris superposés, sans aucun ornement ; bottes de voyage usées ; gants gris.
- **Objets signature** : une dague grise (jumelle de celle qu'il donnera à Konrad) ; une **broche d'épée stylisée** discrète sur la cape (rune d'Ulgu → à neutraliser) ; une sacoche de cuir pleine de notes.
- **Effet visuel** : il apparaît « sans ouvrir les portes ». En manhwa : silhouette qui se densifie à partir de la brume, contours d'abord flous puis nets.
- **Attitude** : immobile, attentif. Expression signature : la bouche qui s'ouvre pour dire la vérité, puis se referme.
- **Palette** : `#3A3D42` ardoise · `#8A5E42` peau tannée · `#1C1B1A` noir · `#1E1F22` ombre · accent `#C9CED6` argent.

**Prompt — 52 ans, planche de référence**
```
Character reference sheet, front, three-quarter and back views, gaunt tall man about 52 years old, slightly stooped, sun-tanned skin, hollow cheeks, deep tired lines around the eyes, pitch black eyes with dark irises, black hair swept back to the nape with grey temples, short unkempt salt-and-pepper beard, long heavy grey hooded cloak almost touching the ground, layered plain grey clothing with no ornament, worn travel boots, grey gloves, small silver sword-shaped brooch on the cloak, plain grey steel dagger at the belt, leather satchel stuffed with papers, calm watchful expression, plain light grey background
```

**Prompt — 2492, la chapelle**
```
Lean man 32 years old, clean-shaven, sun-tanned skin, black hair soaked by rain, pitch black eyes with dark irises under the hood, grey hooded cloak dripping, standing between a young woman and the altar of an abandoned stone chapel, dagger lowered, grey mist curling around his body as if he just materialized, heavy rain through the open door, cold blue-grey lighting
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 32 ans | 2492 | 1–2 | Rasé de près, cheveux noirs, joues moins creusées. |
| 41 ans | 2501–2502 | 3–4 | Barbe courte noire, premiers fils gris, déjà maigre. |
| 47 ans | 2507 | 6 | Le maître. Barbe noire semée de gris, tempes qui grisonnent. |
| 52 ans | 2512 | 7 | Référence principale : fatigue, mèches grises. |

**Prompt — 41 ans (planche)**
```
Same character as the reference image, now 41 years old, gaunt tall man, sun-tanned skin, pitch black eyes, black hair swept back with the first grey threads, short black beard, long heavy grey hooded cloak, plain grey clothes, grey dagger, leaning against a pillar in the shadow, character reference sheet front, three-quarter and back views
```

**Prompt — 47 ans (planche)**
```
Same character as the reference image, now 47 years old, gaunt tall man, sun-tanned skin, pitch black eyes, black hair with greying temples, short black beard flecked with grey, long grey hooded cloak, plain grey clothes, sitting on a tree stump with a small curved knife across his knees, calm demanding teacher's expression, character reference sheet front and three-quarter views
```

---

## 3. Ottilie von Arnsfeld / « Mathilde »

**Rôle** : mère de Konrad, dernière du sang ottilien, devenue guérisseuse à Moosbach. Morte en 2502.
**Âges de référence** : 20 ans (2492, en fuite) et environ 30 ans (2502, Mathilde).
**Couleur d'accent** : bordeaux (le sang Arnsfeld), qu'elle cache.

- **Silhouette** : moyenne, droite, solide malgré la minceur. Une femme qui ne recule pas.
- **Visage** : visage ovale, traits nets et nobles qu'aucun vêtement de paysanne ne cache vraiment. Regard direct, presque dur. Konrad lui ressemble beaucoup.
- **Yeux** : **bleus**, clairs et directs.
- **Cheveux** : **blonds**. En 2492 : **coupés court, mal**, au couteau. En 2502 : longs, tressés et relevés sous un fichu, quelques mèches qui s'échappent.
- **Tenue 2492** : robe de voyage de bonne qualité mais déchirée et boueuse, manteau trop grand, sac en bandoulière.
- **Tenue Mathilde** : robe de laine brune ou vert sombre, tablier taché de plantes, manches retroussées, sacoche d'herbes, bouquets séchés à la ceinture.
- **Objets signature** : la **bague** (à son doigt jusqu'à sa mort, puis à Konrad) ; le **couteau à écorcer** tenu à l'envers ; des mains abîmées par les plantes.
- **Attitude** : calme, contrôlée. Elle « hésitait rarement ». Expression clé : le doigt sur les lèvres, « la règle ».
- **Palette** : `#5A4632` brun laine · `#3F4A36` vert sombre · `#D8CDB6` tablier · accent `#6E2233` bordeaux · `#B8963E` or de la bague.

**Prompt — Mathilde, planche de référence**
```
Character reference sheet, front, three-quarter and back views, woman about 30 years old, straight posture, oval face with refined noble features under simple peasant clothes, clear blue eyes with a direct steady gaze, long blonde hair braided and pinned under a headscarf with a few loose strands, brown wool dress, stained apron, sleeves rolled up, satchel of herbs, dried herb bundles at the belt, worn hands, a tarnished gold signet ring on her finger, small curved bark-peeling knife, calm controlled expression, plain light background
```

**Prompt — 2492, la fugitive**
```
Young woman 20 years old, clear blue eyes, blonde hair cut short and unevenly with a knife, soaked by rain, torn mud-stained travel dress of fine quality, oversized cloak, standing in an abandoned stone chapel, holding a tiny curved knife in a clumsy reverse grip, refusing to step back, fierce exhausted eyes, cold rain light
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 19 ans | 2491 | 1 | Noble d'Arnsfeld : cheveux longs, belle robe simple, la bague au doigt. |
| 20 ans | 2492 | 1 | La fugitive : cheveux coupés court au couteau. |
| 22 ans | 2494 | 2 | Jeune mère : cheveux aux épaules sous un fichu, enceinte puis le bébé dans les bras. |
| 30 ans | 2502 | 3–4 | Référence principale (Mathilde). Malade sur la fin : joues creuses, lèvres grises. |

**Prompt — 19 ans, noble d'Arnsfeld (planche)**
```
Same character as the reference image, now a young noblewoman 19 years old, refined features, clear blue eyes, long loose blonde hair with moss caught in it, fine but simple dark green wool gown with burgundy trim, a gold signet ring on her finger, holding an unlit lantern, standing at the edge of an ancient forest at dusk, character reference sheet front, three-quarter and back views
```

**Prompt — 22 ans, jeune mère (planche)**
```
Same character as the reference image, now 22 years old, clear blue eyes, shoulder-length blonde hair tied under a simple headscarf, plain brown wool dress, apron, holding a newborn wrapped in linen, tired fierce protective gaze, gold signet ring on her finger, character reference sheet front and three-quarter views
```

---

## 4. Baron Ottokar von Eichenwald

**Rôle** : père officiel. Baron de campagne, chasseur, croit que Konrad est son fils et le méprise pour ça.
**Âges** : né vers 2458, aîné de Wolfram. **Âge de référence** : 48 ans (2506). Voir les variantes plus bas.
**Couleur d'accent** : vert chêne.

- **Silhouette** : massif, large d'épaules, ventre de buveur. Légère boiterie depuis le sanglier.
- **Trait de famille Eichenwald** : cheveux noirs, yeux noirs, peau tannée par le soleil et la vie au grand air. Le même trait chez Wolfram, Lothar et Dietrich ; Adelheid tient de sa mère.
- **Visage** : visage carré, peau tannée et rougie par la boisson, nez cassé, grosse barbe noire qui grisonne (toute grise en 2512). Front lourd. Yeux noirs, regard qui fuit.
- **Cheveux** : noirs, courts, clairsemés.
- **Tenue** : vêtements de chasse de noble de province : tunique vert chêne, gilet de cuir, épais manteau doublé de fourrure, bottes hautes. Coutelas de chasse à la ceinture.
- **Objets signature** : les **gants de cuir brodés d'une feuille de chêne** (armes d'Eichenwald), qu'il garde à la main ; une coupe ou une gourde ; une **cicatrice de défense de sanglier** à la cuisse.
- **Mise en scène** : on le dessine **toujours sur un seuil**, jamais dans la pièce.
- **Palette** : `#3E4A2E` vert chêne · `#6B4A2E` cuir · `#8A5E42` peau tannée · `#1C1B1A` noir · accent `#4F5F35` feuille de chêne.

**Prompt**
```
Character reference sheet, front, three-quarter and back views, heavy broad-shouldered provincial baron about 48 years old, beer belly, square sun-tanned ruddy face, broken nose, black eyes, thick black beard turning grey, short thinning black hair, oak-green hunting tunic, leather vest, thick fur-lined cloak, tall boots, hunting knife at the belt, holding leather gloves embroidered with an oak leaf, slight limp, gaze avoiding the viewer, standing in a doorway, plain light background
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 35 ans | 2493 | 2 | Vigoureux, encore en forme, barbe noire pleine. Blessé à la cuisse par le sanglier. |
| 48 ans | 2506 | 5 | Référence principale : ventre, barbe grisonnante, la boisson. |
| 54 ans | 2512 | 7 | Barbe toute grise, visage bouffi, vieilli. |

**Prompt — 35 ans (planche)**
```
Same character as the reference image, now 35 years old, strong vigorous provincial baron, broad shoulders, no belly yet, sun-tanned skin, black eyes, full black beard, short black hair, oak-green hunting tunic, leather vest, tall boots, thigh wrapped in a bloodied bandage from a boar's tusk, leather gloves embroidered with an oak leaf, proud rough expression, character reference sheet front, three-quarter and back views
```

**Prompt — 54 ans (planche)**
```
Same character as the reference image, now 54 years old, heavy aged provincial baron, puffy sun-tanned face, black eyes, fully grey beard, thinning grey-black hair, oak-green tunic and fur-lined cloak worn with age, oak-leaf gloves in hand, standing in a doorway without entering, weary bitter expression, character reference sheet front and three-quarter views
```

---

## 5. Baronne Hildegard von Eichenwald

**Rôle** : épouse d'Ottokar. Dit « celui-là ». Ne regarde jamais Wolfram.
**Âge de référence** : environ 45 ans (2502).
**Couleur d'accent** : bleu froid.

- **Silhouette** : grande, raide, très droite, mains croisées devant elle.
- **Visage** *(proposition)* : long et pâle, lèvres fines, pommettes hautes, menton levé. Beauté sévère. Le regard qui passe au-dessus de Konrad.
- **Cheveux** : blond pâle tirant sur le gris, entièrement couverts d'une coiffe et d'un voile empesé.
- **Tenue** : robe longue bleu nuit à col haut, manches serrées, ceinture d'orfèvrerie, médaillon aux armes d'Eichenwald. La seule personne de la maison forte habillée « comme à Wurtbad ».
- **Objets signature** : trousseau de clés de la maison ; vaisselle brisée (la scène du chapitre 2).
- **Palette** : `#1F2A44` bleu nuit · `#E6E2DA` voile · `#C9B27A` or pâle · accent `#5B7BA6` bleu froid.

**Prompt**
```
Tall rigid noblewoman about 45 years old, pale long face, thin lips, high cheekbones, chin raised, severe beauty, pale blonde hair entirely hidden under a starched white linen wimple and veil, smooth linen with no knitted texture, high-collared midnight blue gown with tight sleeves, goldsmith belt, oak-leaf medallion, ring of keys at her waist, hands folded, looking past the viewer with cold contempt, plain light background, character reference sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 37 ans | 2494 | 2 | Belle et glaciale, au faîte de son autorité (la vaisselle brisée). |
| 45 ans | 2502 | 3–5 | Référence principale. |
| 55 ans | 2512 | 7 | Rides dures, la même raideur. |

**Prompt — 37 ans (planche)**
```
Same character as the reference image, now 37 years old, tall rigid noblewoman, severe cold beauty, pale skin, starched white linen wimple and veil, high-collared midnight blue gown with oak-leaf brocade panels, ring of keys at her waist, chin raised in anger, character reference sheet front, three-quarter and back views
```

**Prompt — 55 ans (planche)**
```
Same character as the reference image, now 55 years old, tall rigid noblewoman, hard deep lines around the mouth, pale skin, starched white linen wimple and veil, high-collared midnight blue gown slightly faded, ring of keys at her waist, cold contemptuous look past the viewer, character reference sheet front and three-quarter views
```

---

## 6. Lothar von Eichenwald

**Rôle** : héritier, brute. Frappe Konrad « à l'entraînement », le pousse dans la Stir.
**Âges de référence** : 14 ans (2500) et 20 ans (2506).
**Couleur d'accent** : rouge brique.

- **Silhouette** : « la carrure de son père » : massif, cou épais, mains énormes. Déjà un homme à 14 ans.
- **Visage** : large, mâchoire lourde, nez épaté, sourire de travers. Accent épais de chasseur que le dessin traduit par une bouche toujours un peu ouverte.
- **Cheveux / yeux** : noirs, coupés court, yeux noirs, peau tannée (le portrait de son père jeune). Barbe naissante à 20 ans.
- **Tenue** : tunique d'entraînement rembourrée, brassards de cuir ; tenue d'héritier vert et brun, plus voyante que celle de son père.
- **Objets signature** : l'**épée de bois** (2500), la **dague d'Averland au pommeau d'argent** (2503).
- **Expression clé** : les bras croisés à la barrière (« le cuir était vieux »).
- **Palette** : `#4A3A2C` cuir · `#3E4A2E` vert · accent `#8E3B2A` rouge brique.

**Prompt — 20 ans**
```
Hulking young nobleman 20 years old, thick neck, huge hands, broad heavy jaw, flat nose, crooked smug grin, sun-tanned skin, black eyes, short black hair, light black stubble, padded training gambeson with leather bracers, arms crossed leaning on a wooden fence of a castle training yard, silver-pommeled dagger at his belt, arrogant bully expression, plain light background, character reference sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 14 ans | 2500 | 3 | Déjà massif, visage d'enfant, épée de bois. |
| 20 ans | 2506 | 5 | Référence principale. |
| 26 ans | 2512 | 6–7 | Marié, barbe noire courte, vêtements d'héritier plus riches, plus lourd. |

**Prompt — 14 ans (planche)**
```
Same character as the reference image, now a hulking boy 14 years old, already as broad as a man, round heavy face, sun-tanned skin, black eyes, short black hair, padded training gambeson, wooden practice sword, smug bully grin, character reference sheet front, three-quarter and back views
```

**Prompt — 26 ans (planche)**
```
Same character as the reference image, now 26 years old, heavy married heir, thick neck, sun-tanned skin, black eyes, short black hair, short black beard, rich oak-green doublet with fur trim, silver-pommeled dagger at his belt, sullen resentful expression, character reference sheet front and three-quarter views
```

---

## 7. Adelheid von Eichenwald

**Rôle** : fille du baron. Moqueuse, manipulatrice. Fait accuser Konrad du vol de la dague ; le coffret de nacre la brise.
**Âges de référence** : 10 ans (2500) et 16 ans (2506).
**Couleur d'accent** : rose nacré.

- **Silhouette** : fine, gracieuse, très consciente d'être regardée.
- **Visage** : joli, petit nez, lèvres qui se retroussent pour rire. Après 2506 : même visage, mais yeux rouges et regard qui s'écarte.
- **Cheveux** : blond doré de sa mère, longs, nattés avec des rubans.
- **Tenue** : robes claires et soignées, la plus coquette de la maison forte.
- **Objets signature** : le **coffret de nacre** (lettres de l'écuyer) ; le **rideau** de sa fenêtre qui bouge.
- **Deux expressions à dessiner** : le rire méprisant (avant) et le recul silencieux dans le couloir (après).
- **Palette** : `#E9D9C4` crème · `#C9A86A` blond · `#7A8FA6` bleu pâle · accent `#E3C4C8` nacre rosée.

**Prompt — 16 ans**
```
Graceful noble girl 16 years old, pretty face with a small nose, long golden blonde hair braided with ribbons, elegant cream and pale blue dress, holding a small mother-of-pearl jewelry box, two expressions side by side: mocking laughter, then red-rimmed eyes stepping aside in a dark corridor, plain light background, character expression sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 10 ans | 2500 | 3 | Petite fille blonde et moqueuse, rubans, robe claire. |
| 16 ans | 2506 | 5 | Référence principale. Quitte Eichenwald avant 2512, fiancée à un noble du Sud. |

**Prompt — 10 ans (planche)**
```
Same character as the reference image, now a pretty noble girl 10 years old, golden blonde hair braided with ribbons, small nose, cream and pale blue dress, hand over her mouth laughing mockingly, character reference sheet front, three-quarter and back views
```

---

## 8. Dietrich von Eichenwald

**Rôle** : cadet légitime, un an de moins que Konrad. Suiveur, puis témoin qui avoue (« J'ai vu ce qu'il a fait »).
**Âges de référence** : 11 ans (2506) et 17 ans (2512).
**Couleur d'accent** : ocre.

- **Silhouette** : moyen, un peu mou, épaules rentrées. Toujours un pas derrière Lothar.
- **Visage** : rond, doux, sourcils inquiets. Le seul de la fratrie dont le visage peut montrer de la honte.
- **Cheveux / yeux** : noirs, en désordre, yeux noirs, peau tannée.
- **Tenue** : vêtements hérités de Lothar, trop grands aux épaules.
- **Scène signature** : debout sur une marche de l'escalier des écuries, immobile.
- **Palette** : `#6B4A2E` brun · `#3E4A2E` vert délavé · accent `#B07A3A` ocre.

**Prompt — 17 ans**
```
Soft-faced noble teenager 17 years old, round gentle sun-tanned face, black eyes, worried eyebrows, messy black hair, slightly hunched shoulders, oversized hand-me-down green and brown tunic too wide at the shoulders, standing still on a wooden stable staircase, guilty hesitant expression, plain light background, character reference sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 5 ans | 2500 | 3 | Petit garçon rond qui répète ce que disent les grands. |
| 11 ans | 2506 | 5 | Témoin silencieux de la Stir. |
| 17 ans | 2512 | 7 | Référence principale. |

**Prompt — 5 ans (planche)**
```
Same character as the reference image, now a chubby little boy 5 years old, round face, sun-tanned skin, black eyes, messy black hair, small green tunic, hiding half behind a bigger boy's leg, copying a mocking grin, character reference sheet front and three-quarter views
```

**Prompt — 11 ans (planche)**
```
Same character as the reference image, now a soft round-faced boy 11 years old, sun-tanned skin, black eyes, messy black hair, hand-me-down green and brown tunic too big for him, standing on a muddy riverbank looking frightened and guilty, character reference sheet front, three-quarter and back views
```

---

## 9. Père Anselm

**Rôle** : chapelain de Sigmar, précepteur. Hostile, frappe avec sa règle ; laisse pourtant la bibliothèque entrouverte.
**Âge de référence** : environ 55 ans (2500).
**Couleur d'accent** : rouge sombre liturgique.

- **Silhouette** : petit, sec, voûté sur ses livres.
- **Visage** : maigre, nez en bec, lèvres pincées, yeux plissés de myope, tonsure grise.
- **Tenue** : robe de bure épaisse, étole rouge sombre, ceinture de corde. Symbole religieux en marteau **stylisé et non canonique**.
- **Objets signature** : la **règle de bois** ; un gros livre relié ; la clé de la petite bibliothèque.
- **Palette** : `#3B3530` bure · `#6E2A26` étole · accent `#A88A5C` cuir des livres.

**Prompt**
```
Small dry stooped priest about 55 years old, thin face, hooked nose, pursed lips, squinting short-sighted eyes, grey tonsure, thick dark homespun robe, dark red stole, rope belt, simple stylized hammer pendant, holding a wooden ruler in one hand and a heavy leather-bound book in the other, stern disapproving look, plain light background, character reference sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 55 ans | 2500 | 3 | Référence principale. |
| 67 ans | 2512 | 7 | Plus voûté, plus fragile, toujours la règle. |

**Prompt — 67 ans (planche)**
```
Same character as the reference image, now 67 years old, frail stooped priest, thin wrinkled face, hooked nose, squinting eyes, white tonsure, thick dark homespun robe, dark red stole, wooden ruler tucked in his rope belt, standing in a small chapel library, character reference sheet front and three-quarter views
```

---

## 10. Rüdiger

**Rôle** : vieux maître d'armes à la jambe raide. Premier à reconnaître le talent de Konrad. « Bats-toi comme une guêpe. »
**Âge de référence** : environ 60 ans (2506).
**Couleur d'accent** : acier.

- **Silhouette** : ancien soldat, encore large mais sec, une **jambe raide** (canne ou bâton d'entraînement comme appui).
- **Visage** : buriné, cicatrices fines, moustache grise tombante, crâne rasé ou cheveux gris très courts. Yeux clairs, amusés, qui regardent « ailleurs » puis regardent quand même.
- **Tenue** : gambison délavé, tablier de cuir de la salle d'armes, bottes usées.
- **Objets signature** : la **lanterne** de l'entraînement à l'aube ; le chiffon à graisser les lames ; les **gants de cuir fin** qu'il donnera à Konrad.
- **Palette** : `#5C5A52` gambison · `#4A3A2C` cuir · accent `#9AA3AD` acier.

**Prompt**
```
Weathered old weapons master about 60 years old, still broad but wiry, stiff right leg leaning on a wooden training staff, thin old scars on his face, drooping grey mustache, close-cropped grey hair, pale amused eyes, faded gambeson, leather workshop apron, holding a lantern in a dark courtyard before dawn, pair of thin worn leather gloves tucked in his belt, plain light background, character reference sheet
```


### Âges dans le Livre I
| Âge | Année | Chapitre | Ce qui change |
|---|---|---|---|
| 54 ans | 2500 | 3 | Moustache encore poivre et sel, plus massif. |
| 60 ans | 2506 | 5 | Référence principale. |
| 66 ans | 2512 | 7 | Moustache blanche, plus maigre, il graisse des lames qu'on n'utilise plus. |

**Prompt — 54 ans (planche)**
```
Same character as the reference image, now 54 years old, broad old soldier, stiff right leg, salt-and-pepper drooping mustache, close-cropped grey-black hair, pale eyes, faded gambeson, standing in a rainy castle training yard with a wooden practice sword, looking away on purpose, character reference sheet front, three-quarter and back views
```

**Prompt — 66 ans (planche)**
```
Same character as the reference image, now 66 years old, thin old weapons master, stiff right leg, white drooping mustache, white cropped hair, pale eyes, leather apron, oiling an old blade with a rag in a dim armory, a pair of thin worn leather gloves on the bench, character reference sheet front and three-quarter views
```

---

## 11. Le faux copiste

**Rôle** : sorcier gris de la Main Grise, assassin d'Ottilie (2502). Tué par Wolfram. Sans nom pour l'instant.
**Âge de référence** : environ 45 ans.
**Couleur d'accent** : aucune. C'est son design : il n'a rien qui accroche l'œil.

- **Silhouette** : moyenne, ordinaire. Le seul détail qui le trahit, c'est **sa façon de se tenir** : trop droit, trop immobile, dos jamais tourné à une porte. Dans les cases, c'est ce que Mathilde reconnaît.
- **Visage** : banal, oubliable, rasé de près, cheveux châtains coupés court.
- **Tenue** : manteau brun de copiste, sacoche à plumes et rouleaux, encre sur les doigts. Sous le manteau, en case révélation : une dague grise.
- **Effet visuel** : l'air autour de lui est « un peu plus gris » (même code que l'homme aux pommes de 2511).
- **Palette** : `#6B5E4E` brun terne · `#8A8378` gris sale.

**Prompt**
```
Unremarkable forgettable man about 45 years old, plain clean-shaven face, short brown hair, dull brown scrivener's coat, satchel of quills and scrolls, ink-stained fingers, posture too straight and too still for a clerk, faint grey haze around his silhouette, a grey dagger barely visible under the coat, snowy village inn background, subtle menace
```

---

## 12. Sigurður Broksson — « Sigurd »

**Rôle** : deuxième héros (personnage de l'autre joueur). Nain, ranger, chasseur de primes.
**Ce que dit la fiche** : 1,55 m, yeux vert émeraude, CC 42, Endurance 40, Force Mentale 49, Agilité 17. Talents : Résistance à la magie, Vision nocturne, Implacable, Résolu, Robuste, Coup assommant. Savoirs : métallurgie, géologie ; un métier.
**Non renseigné** : âge, cheveux. Les propositions ci-dessous sont à faire valider par son joueur.
**Couleur d'accent** : vert émeraude (les yeux).

- **Silhouette** : **grand pour un nain** (1,55 m), donc presque à hauteur d'épaule de Konrad. Un bloc : torse en tonneau, bras épais, jambes courtes et solides. Lent et lourd (Agilité basse), mais rien ne le fait reculer (Robuste, Implacable). Le contraste avec Konrad est le cœur du duo à l'image : la guêpe et l'enclume.
- **Visage** : large, nez fort, sourcils broussailleux, front marqué. Expression par défaut : impassible, têtu.
- **Yeux** : **vert émeraude**, très lumineux. En manhwa, ils brillent légèrement dans le noir (Vision nocturne).
- **Cheveux et barbe** *(proposition)* : roux cuivré foncé, barbe longue en deux tresses fixées par des anneaux de métal qu'il a forgés lui-même (métallurgie).
- **Âge** *(proposition)* : environ 70 ans, c'est-à-dire un jeune adulte pour un nain. Pas de gris dans la barbe.
- **Tenue** : manteau de cuir épais et long, capuche, gilet de cuir clouté, cotte de mailles courte dessous, bottes ferrées. Couleurs de terre et de pierre.
- **Objets signature** :
  - une **masse ou un marteau à tête ronde** (Coup assommant : il ramène ses primes vivantes) ;
  - des **menottes et une corde** à la ceinture, son outil de chasseur de primes ;
  - un **rouleau d'avis de recherche** glissé dans le manteau ;
  - une petite **pioche ou un marteau de géologue** et une bourse à échantillons de pierre.
- **Attitude** : bras croisés, pieds plantés. Expression clé : le regard émeraude qui ne cligne pas pendant un interrogatoire (Intimidation).
- **Palette** : `#5A4433` cuir · `#6E6A62` pierre · `#8C4A2A` cuivre (barbe) · `#3A3A3A` fer · accent `#2FA36B` émeraude.

**Prompt — planche de référence**
```
Character reference sheet, front, three-quarter and back views, tall stocky dwarf bounty hunter, barrel chest, thick arms, short sturdy legs, broad face, strong nose, bushy eyebrows, bright emerald green eyes, long dark copper-red beard in two braids bound with hand-forged iron rings, long heavy hooded leather coat, studded leather vest over a short chainmail shirt, iron-shod boots, round-headed war mace at the belt, iron manacles and coiled rope hanging from the belt, rolled wanted posters in the coat, small geologist hammer and a pouch of stone samples, arms crossed, stubborn impassive expression, plain light background
```

**Prompt — le duo**
```
A tall lean young man in a grey hooded cloak holding two daggers and a stocky dwarf bounty hunter with a copper braided beard and glowing emerald eyes holding a mace and manacles, standing back to back in a dark mountain pass at night, storm clouds, grey mist around the young man, dramatic contrast between the agile wasp and the immovable anvil
```

---

## 13. Brunhild

**Rôle** : vieille apicultrice à la lisière de la forêt d'Arnsfeld. Sauve Ottilie sans le savoir (chapitre 1).
**Âge** : environ 70 ans (2491).
- Petite, ronde, le dos courbé, des mains énormes. Visage ridé comme une pomme d'hiver, yeux vifs.
- Fichu, tablier taché de cire, voile d'apicultrice relevé. Ruches de paille autour d'elle.
- **Palette** : `#C9A24A` cire · `#6B5A3E` brun · `#3F4A36` vert forêt · accent `#E0B341` miel.

**Prompt — planche de référence**
```
Small round old beekeeper woman about 70 years old, bent back, huge gentle hands, face wrinkled like a winter apple, lively eyes, headscarf, beeswax-stained apron, beekeeper's veil pushed up, standing among straw beehives at the edge of an ancient forest at dusk, character reference sheet front and three-quarter views
```

---

## 14. Le vieux prêtre de Morr (Moosbach)

**Rôle** : tient le registre où Ottokar barre « père non déclaré ». Au chevet de Mathilde, l'enterre.
**Âge** : environ 65 ans (2496), 71 ans (2502).
- Grand, décharné, voûté, longues mains pâles. Crâne chauve, yeux cernés, très doux.
- Robe noire usée, symbole du dieu des morts (porte ou corbeau stylisé, non canonique), registre relié de cuir sous le bras.
- **Palette** : `#1E1E22` noir · `#5C5A60` gris · accent `#8A7CA8` violet fané.

**Prompt — planche de référence**
```
Tall gaunt stooped old priest of a god of death about 70 years old, long pale hands, bald head, dark-circled gentle eyes, worn black robe, small stylized raven-and-door pendant, a thick leather-bound register under his arm, quiet village chapel background, character reference sheet front and three-quarter views
```

---

## 15. La femme du meunier

**Rôle** : premier soutien de Mathilde à Moosbach ; témoin de la naissance de Konrad et de la mort de sa mère.
**Âge** : environ 35 ans (2494), 43 ans (2502).
- Robuste, joues rouges, bras couverts de farine, chignon défait. Parle trop quand elle a peur (« Il a les yeux de son père »).
- Robe de laine bleu passé, tablier blanc de farine.
- **Palette** : `#5D6E86` bleu passé · `#EDE6D6` farine · accent `#B5553C` joues.

**Prompt — planche de référence**
```
Sturdy village miller's wife about 35 years old, red cheeks, flour-covered forearms, loose brown bun, faded blue wool dress, flour-white apron, warm talkative nervous expression, watermill interior background, character reference sheet front and three-quarter views
```

---

## 16. Le rebouteux de Torfmoor

**Rôle** : sorcier de village corrompu par le Dhar (chapitre 6). Première vision du mal pour Konrad.
**Règle de mise en scène** : jamais montré en entier ni en gros plan. Silhouette dans la pénombre d'une cabane de roseaux, peau qui « n'a plus tout à fait la forme d'une peau », courant noir huileux autour de lui. L'horreur est suggérée, pas détaillée.
- **Palette** : `#1A1C17` noir tourbe · `#3B4031` vert vase · accent `#2A1F33` noir huileux violacé.

**Prompt — silhouette**
```
Dim interior of a reed hut at the edge of a peat bog, a hunched human silhouette in the shadows whose outline subtly warps and ripples, thick oily black mist with a faint violet sheen coiling around him and across the floor, dried herbs and animal bones hanging from the ceiling, unsettling suggestive horror, no gore, details hidden in darkness
```

---

## Points à valider par Lyes

- Couleur des cheveux d'Hildegard (proposition : blond pâle ; Adelheid en hérite).
- Sigurd : âge et couleur de cheveux à faire confirmer par son joueur.
- La cicatrice à la lèvre de Konrad (issue du chapitre 3) : à garder ?
- Personnages secondaires non faits : le meunier et son fils, la sage-femme, l'écuyer de Wurtbad, l'épouse de Lothar.
