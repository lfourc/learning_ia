# Bible des décors et ambiances — Livre I

*Lieux, lumière et couleurs pour garder un univers cohérent d'une image à l'autre. Va avec la bible visuelle des personnages et la bible d'écriture webtoon. Version 3, 16/11/2026. v2 : style aligné sur la bible webtoon (décors simplifiés, aplats nets). v3 : passage au monde d'Erdheim (magie du Codex v3, noms et dates AC, plus aucune référence à Warhammer).*

---

## 0. Direction artistique

### L'univers en une phrase
Un Saint-Empire de la fin du Moyen Âge, pauvre, humide et boisé, où le mana flotte dans l'air et où la magie ne brille presque jamais : elle s'insinue comme une brume.

### Les règles
- **Époque visuelle** : Allemagne des XVe et XVIe siècles. Colombages, pierre grise, toits de bardeaux ou de chaume, bois sombre, fer forgé. Rien de « high fantasy » : pas de tours de cristal, pas d'armures dorées, pas de couleurs saturées.
- **Ciel bas.** La Nebelmark vit sous les nuages : brume au sol, pluie fine, lumière diffuse. Le soleil franc est rare, donc précieux : on le garde pour les moments qui comptent.
- **Échelle humaine.** Les lieux sont petits, usés, habités. La maison forte est une grosse ferme fortifiée, pas un château de conte.
- **Des chênes partout.** C'est l'arbre d'Eichenwald (« forêt de chênes ») et le motif du domaine.
- **La magie à l'image** (Codex, Tome 0, § 2 ; tableau complet dans `webtoon/monde-et-introduction.md`, § 2.3) :
  - *le mana dense* (Eldwald, vieilles chênaies, tombes) : particules dorées qui flottent dans la lumière et dérivent contre le vent ;
  - *l'Ombre* : brume grise translucide aux reflets argentés qui monte du sol, contours qui se brouillent, feu qui baisse d'un coup ;
  - *la Seconde vue* (Éther) : fins **flux de mana** entre les arbres, comme la chaleur qui tremble sur une route ; ils sont plus denses autour des vieux chênes et dans la terre des tombes ;
  - *les signes des Sept* au-dessus des portes : gravures discrètes ; ils s'allument en or quand une bénédiction de seuil tient ;
  - *l'Obscur* : courant noir, huileux, à reflet violacé, qui serpente au ras du sol. Seule « couleur » vraiment dérangeante de tout le livre.
- **Manhwa, mais sobre** :
  - Chaque lieu a **un plan de référence** : un plan large, plus détaillé, qui fixe l'architecture, les matières et la lumière. Les prompts de cette bible servent à le générer.
  - **Dans les cases du webtoon, le décor est simplifié ou flou** : aplats nets, formes lisibles, peu de textures. Le détail est réservé aux visages et à l'objet important (voir `webtoon/bible-ecriture-webtoon.md`, section 7).
  - Lumière volumétrique (rayons dans la brume, lueur de bougie) autorisée. Les effets spectaculaires sont réservés à la magie et aux scènes clés.

### Le script couleur par chapitre
| Chapitre | Saison | Dominante | Accent |
|---|---|---|---|
| Webtoon, arc 1 — Arnsfeld (790-791) | automne, première neige, automne | vert profond de l'Eldwald, or du mana ; blanc et bleu de la neige | or du Don, ambre du Vif, gris argent de l'Ombre ; rouge du vin et orange de la torche à l'épisode 3 |
| 1 — Le chasseur et la survivante | automne, puis hiver | vert forêt profond, bleu nuit de pluie | orange de l'incendie |
| 2 — La guérisseuse de Moosbach | printemps | vert tendre, brun chaud | or pâle de l'aube |
| 3 — Le bâtard | années qui passent | ocre, gris pierre | vert chêne d'Eichenwald |
| 4 — L'hiver des lettres brûlées | hiver | blanc sale, gris-bleu | orange des lettres qui brûlent |
| 5 — La maison forte | pluies, crue | gris ardoise, brun boue | gris argent de l'Ombre ; noir et violet de l'Obscur à la Nebel |
| 6 — L'oncle gris | aubes, nuits | vert sombre, bleu lanterne | or des flux de mana ; noir violacé de l'Obscur |
| 7 — La route de Hautepierre | printemps | bleu froid des montagnes | lumière dorée d'Aurevaux |

### Bloc de style décor
À coller à la fin de chaque prompt de **plan de référence** d'un lieu :
```
Korean action-fantasy webtoon background art, clean sharp lineart, flat cel-shaded tones with crisp shadow shapes, readable simplified forms, cinematic wide shot, atmospheric perspective, volumetric light, muted desaturated palette, dark low-fantasy late medieval German setting, half-timbered houses, grey stone, dark wood, oak trees, no text, no christian crosses or crucifixes, religious symbols are invented pagan emblems (stylized hammer, raven, door)
```
Négatif :
```
oil painting, painterly brushstrokes, photorealism, soft airbrushed gradients, busy textures, cluttered foliage, grain, christian cross, crucifix, fleur-de-lis, text, letters, watermark
```
**Pour les cases du webtoon**, n'utilise pas ce bloc : les prompts des fichiers `epXX-pages-prompts-chatgpt.md` sont déjà complets.

Midjourney : `--ar 16:9 --niji`. Pour une case verticale de webtoon : `--ar 9:16`.

### Iconographie religieuse
Jamais de croix chrétiennes, de crucifix, de Vierge ni de saints. Les générateurs en ajoutent spontanément sur les chapelles : le bloc de style les exclut, mais vérifie chaque image. Les chapelles sont dédiées aux **Sept du Seuil** (Codex, Tome 0, § 3.2) :
- **Haldor** : un marteau stylisé ;
- **la Gardienne du Seuil** : une porte entrouverte gardée par un corbeau ;
- **le Vieux Cerf** : des bois de cerf, sculptés dans l'écorce des vieux chênes ;
- au-dessus des portes des maisons, le **signe des Sept**.

---

## L1. La forêt d'Arnsfeld et les ruches de Brunhild

**Région** : l'Eldwald. **Chapitre** : 1 ; webtoon, arc 1. **Scènes** : Ottilie qui rentre de chez Brunhild ; la fumée qu'elle sent avant de voir ; les ruches et l'essaim (épisode 1).
- Forêt immense et très ancienne, sans chemins. Troncs énormes couverts de mousse, fougères à hauteur de taille, lumière verte filtrée. « Une forêt qui se souvient. » La forêt du Vieux Cerf : des bois de cerf sculptés dans l'écorce marquent son entrée.
- Le mana y est saturé : particules dorées dans chaque rayon de lumière.
- À la lisière : la chaumière basse de Brunhild au toit de mousse, ruches de paille alignées sur des bancs, fumée de cheminée.
- L'Eldwald n'est pas la Nebelmark : plus sauvage, plus vert, plus profond, moins de brume, des arbres plus grands.
- **Palette** : `#1F3326` vert profond · `#5B6E3A` mousse · `#C9A24A` cire · accent `#E07A2E` orange de lanterne.

**Prompt — la lisière au crépuscule**
```
Edge of an immense ancient primeval forest at dusk, colossal moss-covered trunks, waist-high ferns, a low thatched cottage with straw beehives in a row, thin chimney smoke, tiny golden motes drifting in the last light, a young woman walking away into the trees with a lantern, deep green and amber light
```

## L2. Le manoir d'Arnsfeld

**Région** : l'Eldwald. **Chapitre** : 1 ; webtoon, arc 1. **Scènes** : la vie au domaine (790-791) ; l'incendie vu depuis la colline ; les deux silhouettes immobiles à la lisière du parc.
- Manoir noble de province, sur une colline : pierre claire, grande salle à charpente de bois, ailes basses, parc avec de vieux arbres, bannière verte au tilleul d'argent. Plus élégant qu'Eichenwald : une famille ancienne, discrète. Le village est en contrebas, au sud ; la poterne nord ouvre sur la forêt.
- Au-dessus de chaque porte, le signe des Sept que Gisela touche le soir.
- **L'incendie** : tout brûle d'un coup, les flammes sortent des fenêtres « comme par des bouches », le toit de la grande salle s'effondre dans une gerbe d'étincelles. **Personne ne sort.** Le silence est l'horreur de la scène.
- **Palette** : `#0F1626` nuit · `#2A3B2C` parc · accent `#F2762E` incendie · `#FFD08A` étincelles.

**Prompt — l'incendie**
```
A noble manor on a hill engulfed in flames at night, fire pouring out of every window, the great hall roof collapsing in a tower of sparks, dark parkland with old trees in the foreground, two motionless cloaked silhouettes standing at the edge of the park watching, no one fleeing, eerie silent horror, view from ferns on a forest hillside
```

## L3. La chapelle abandonnée de la Gardienne

**Région** : route du sud, Eldwald. **Chapitre** : 1. **Scène** : Wolfram baisse la lame.
- Petite chapelle de pierre au bord d'un bois, toit en partie effondré, autel nu, symbole de la Gardienne du Seuil (la porte et le corbeau) à demi effacé. Pluie torrentielle par la porte ouverte.
- Lumière : bleu-gris froid, un seul rayon pâle par le toit percé. Wolfram « gris dans le gris ».
- **Palette** : `#1D2430` bleu nuit · `#5A626E` pierre mouillée · accent `#AFC3D6` reflet de pluie.

**Prompt — sous la pluie**
```
Interior of a small abandoned stone chapel at the edge of a wood, partly collapsed roof, bare stone altar with a half-erased raven-and-door symbol, torrential rain falling through the open door and the broken roof, puddles reflecting cold blue-grey light, a single pale shaft of light, wet stone, dead leaves, oppressive silence
```

## L4. Le bac sur la Nebel

**Région** : frontière Eldwald / Nebelmark. **Chapitre** : 1. **Scène** : la traversée en janvier.
- Rivière large, grise, lente, bordée de roseaux gelés. Bac de bois tiré sur une corde, passeur emmitouflé. Sur l'autre rive : collines basses, forêts noires, ciel blanc. On jette une pièce à Varn avant de traverser.
- **Palette** : `#7D8A92` eau grise · `#D9DCD8` ciel blanc · `#3A3F35` forêt noire · accent `#8C6A44` bois du bac.

**Prompt — la traversée**
```
A wooden rope ferry crossing a wide slow grey river in deep winter, frozen reeds on the banks, a muffled ferryman pulling the rope, two cloaked passengers, low hills and black forests on the far bank under a white sky, light snow, bleak and quiet
```

## L5. Moosbach

**Région** : Nebelmark, domaine d'Eichenwald. **Chapitres** : 2 à 7. **Scènes** : la place du marché, la taverne, la fontaine, le cimetière sous la neige, le moulin.
- Village serré autour de sa chapelle de la Gardienne : maisons à colombages basses, toits de chaume et de bardeaux moussus, rues de boue, volets fermés avant la nuit (à l'est, l'Aschenland). Un moulin sur un affluent de la Nebel, une petite taverne, une fontaine.
- Pauvre, humide, méfiant. Chênes noirs tout autour.
- **Variantes** : jour de marché (811, l'homme aux pommes) ; hiver, cimetière sous la neige (802).
- **Palette** : `#4B4237` boue · `#6E6658` colombages · `#3E4A2E` chênes · accent `#C98B3A` fenêtres éclairées.

**Prompt — jour de marché**
```
A small poor village square in a damp hill country, low half-timbered houses with mossy thatched and shingle roofs, muddy streets, a stone fountain, a modest chapel with a dark slate roof, market stalls with apples and cabbages, villagers in drab wool, dark oak forest on the hills behind, overcast sky, faint mist
```

**Prompt — le cimetière sous la neige**
```
A tiny village cemetery behind a humble stone chapel in winter, simple wooden and stone grave markers half buried in snow, a fresh grave, bare black oaks, blue dusk light, a lone small child sitting by the grave, silence
```

## L6. La maison du bord de la forêt

**Région** : Moosbach. **Chapitres** : 2 à 4, puis 6 (vide). **Scènes** : la jambe d'Ottokar recousue sur la table ; Wolfram dans l'angle à l'aube ; les lettres brûlées dans la cheminée ; Mathilde sur le seuil.
- Petite maison de pierre et de bois à l'écart du village, contre la lisière. Une pièce principale : cheminée, grande table, herbes qui sèchent au plafond, pots de miel et d'onguents, un berceau puis une paillasse d'enfant.
- La maison la plus chaude du livre : c'est le seul vrai foyer de Konrad. Après 802, la même maison vide et froide.
- **Palette** : `#5A4632` bois · `#6E7A4A` herbes · `#E8C27A` lumière du feu · accent `#F08A3A` braises.

**Prompt — intérieur, le soir**
```
Interior of a small stone and timber healer's cottage at night, a crackling hearth, a heavy wooden table, bundles of drying herbs hanging from the low beams, shelves of honey jars and ointment pots, a cradle in the shadowy corner, warm amber firelight against cold blue window light
```

**Prompt — extérieur**
```
A small lonely stone and timber cottage at the very edge of a dark oak forest, a little apart from a village, herb garden, smoke from the chimney, a woman standing straight on the doorstep watching snow fall on the path, early winter dusk
```

## L7. La maison forte d'Eichenwald

**Région** : Nebelmark. **Chapitres** : 2 à 7. **Scène** : vue d'ensemble, retour au domaine.
- Grosse maison forte de barons de campagne : un donjon carré trapu en pierre grise, un corps de logis à colombages, une enceinte basse, une cour, des écuries, une petite chapelle d'Haldor. Feuille de chêne sculptée au-dessus de la porte.
- Plus ferme que château. Boue, chiens, fumier, chevaux. Riche pour Moosbach, rien du tout pour Wendelstadt.
- **Palette** : `#5E5F5C` pierre · `#4A3A2C` bois · `#3E4A2E` vert chêne · accent `#4F5F35` bannière.

**Prompt — vue d'ensemble**
```
A rustic fortified manor house of minor country barons on a low hill, squat square grey stone keep, half-timbered main hall, low curtain wall, muddy courtyard with stables and a small chapel, oak leaf carved above the gate, surrounded by dark oak forest and a misty river valley, overcast sky
```

## L8. La cour d'armes

**Chapitres** : 3, 5, 6. **Scènes** : Lothar frappe, Rüdiger regarde ailleurs ; Wolfram contre le pilier, dans l'ombre de l'auvent ; Konrad désarme Lothar, Ottokar sur la galerie ; les entraînements à l'aube à la lanterne.
- Cour pavée de travers, flaques, mannequins d'entraînement, râtelier d'épées de bois, auvent de bois sur piliers, galerie en surplomb.
- **Variantes** : sous la pluie (ch. 3) ; à l'aube à la lanterne (ch. 5) ; matin gris avec toute la maison qui regarde (ch. 6).
- **Palette** : `#6B6A64` pavés mouillés · `#4A3A2C` bois · accent `#E3B15A` lanterne.

**Prompt — sous la pluie**
```
A small castle training yard in the rain, uneven wet cobblestones and puddles, wooden training dummies, a rack of wooden practice swords, a timber awning on posts casting deep shadow, a wooden gallery above, grey stone walls, a cloaked figure barely visible leaning against a post in the shadow
```

**Prompt — l'aube à la lanterne**
```
The same castle training yard before dawn, darkness and fog, a single lantern on the ground lighting wet cobblestones, an old man with a stiff leg facing a thin boy with a wooden sword, long shadows, cold blue night turning to grey
```

## L9. La grande salle

**Chapitres** : 3, 5. **Scènes** : le bout de la table ; la famille réunie pour juger le vol de la dague ; l'émissaire de Wendelstadt.
- Salle longue, plafond à poutres noircies, grande cheminée, longue table de chêne, bancs, tapisseries de chasse usées, trophées (dont une hure de sanglier). Le baron en haut, Konrad tout au bout, dans la pénombre.
- **Palette** : `#2C2420` poutres · `#6B4A2E` chêne · `#8E3B2A` tapisseries · accent `#E8B060` cheminée.

**Prompt — le bout de la table**
```
Long great hall of a rustic manor, blackened ceiling beams, large stone fireplace, a long oak table with noble family seated near the fire at the far end, worn hunting tapestries, a boar's head trophy, warm light at the head of the table fading into shadow toward the near end where a lone child sits, strong depth composition
```

## L10. Le réduit au-dessus des écuries

**Chapitres** : 5 à 7. **Scènes** : la bague dans la paume ; Ottokar ivre sur le seuil ; Wolfram assis sur le coffre ; la brume à la lucarne ; le sac préparé.
- Grenier étroit sous le toit des écuries : paillasse, coffre de bois, une seule lucarne, poutres basses, foin, odeur de cheval. Escalier de bois raide qui monte depuis la cour.
- Le lieu de Konrad : pauvre, mais à lui. Lumière d'une seule source (lucarne ou chandelle).
- **Palette** : `#3B3128` bois sombre · `#B59A5E` foin · accent `#C9CED6` lumière de lucarne.

**Prompt — le réduit**
```
A cramped loft above the stables, sloping low roof beams, a straw pallet, a plain wooden chest, scattered hay, a single small dormer window letting in a pale beam of grey light with a faint unnatural mist lingering in its corner, a steep wooden staircase opening in the floor, poor but tidy
```

## L11. La chapelle d'Haldor et sa bibliothèque

**Chapitres** : 3, 5, 6. **Scènes** : la règle sur les doigts ; la porte de la bibliothèque laissée entrouverte ; les armoriaux où Konrad cherche les armes de la bague.
- Petite chapelle d'Haldor (marteau stylisé), bancs de bois, vitrail modeste. Derrière, une bibliothèque minuscule : étagères chargées de livres reliés, pupitre, chandelle.
- **Palette** : `#4A4440` pierre · `#6E2A26` rouge liturgique · accent `#E8C27A` chandelle.

**Prompt — la bibliothèque la nuit**
```
A tiny library behind a small manor chapel at night, shelves crammed with old leather-bound books and heraldry rolls, a slanted reading desk, a single candle, a door left slightly ajar onto the dark chapel with a modest stained-glass window, warm candlelight pool surrounded by darkness
```

## L12. La Nebel en crue

**Chapitre** : 5. **Scène** : Lothar pousse Konrad dans la rivière ; l'Ombre s'éveille, l'Obscur avec elle ; la brume grise monte en plein jour au-dessus de lui seul.
- Rivière brune gonflée, eaux rapides, troncs arrachés, berge de boue glissante, saules couchés. Grand soleil d'avril ailleurs, et une colonne de brume grise qui ne reste qu'au-dessus de l'enfant ; au cœur de la brume, des veines noires et violettes (l'Obscur), à peine visibles.
- **Palette** : `#6B5A3E` eau boueuse · `#9DB0A2` ciel d'avril · accent `#B9BEC4` brume de l'Ombre.

**Prompt — la brume en plein jour**
```
A swollen brown river in spring flood under bright sunshine, fast muddy water, uprooted branches, a slippery mud bank with bent willows, a column of unnatural grey mist rising from the water around a single small figure while the rest of the scene stays sunny, faint black-violet veins inside the mist, eerie and wondrous
```

## L13. La clairière des vieux chênes

**Chapitre** : 6. **Scènes** : la nuit de silence ; Wolfram qui ouvre la Seconde vue de Konrad ; les lettres de Langue Tordue dans la cendre.
- Clairière profonde dans la forêt d'Eichenwald, chênes si vieux que leurs branches se rejoignent en voûte. Souche, cendres d'un feu éteint, lit de feuilles. Un lieu sacré, presque une cathédrale, où le mana s'accumule.
- **Variantes** : nuit sans feu (bleu noir) ; matin de printemps avec la Seconde vue (flux de mana entre les troncs).
- **Palette** : `#1C2A22` vert nuit · `#4E5E3A` mousse · accent `#C9B060` or du mana.

**Prompt — la Seconde vue**
```
A deep clearing in an ancient oak forest where enormous old oaks meet overhead like a cathedral vault, spring morning mist, thin translucent threads of pale gold light flowing between the trunks like heat shimmer, denser around the oldest oaks and seeping from the earth, soft grey wisps pooling in every shadow, an old tree stump and the ashes of a dead fire, sacred and quiet
```

## L14. Torfmoor et la tourbière

**Chapitre** : 6. **Scène** : le village vide ; la chapelle profanée ; le courant noir de l'Obscur vers la cabane de roseaux.
- Hameau près des collines tournées vers l'Aschenland. Maisons debout mais vides, portes qui battent, chapelle aux signes des Sept grattés et repeints d'une matière sombre qui a coulé. Au-delà : tourbière noire, roseaux, brume basse.
- Seul décor « d'horreur » du livre : tout est suggéré, rien n'est montré en détail.
- **Palette** : `#2B2E26` tourbe · `#5C6250` roseaux · `#8A8F86` brume · accent `#2A1F33` noir violacé de l'Obscur.

**Prompt — le hameau vide**
```
An abandoned hamlet at the edge of a black peat bog under a heavy autumn sky, empty half-timbered houses with doors swinging open in the wind, a small chapel with defaced symbols painted over in something dark that has run down the stone, low mist over reeds, a thick oily black current with a violet sheen snaking along the ground between the houses toward a reed hut, dread, no people
```

## L15. L'auberge de relais sur la route de Wendelstadt

**Chapitre** : 4. **Scène** : Wolfram face au copiste ; le duel de deux maîtres de l'Ombre ; le feu qui baisse, la salle envahie de brume grise.
- Salle commune basse, poutres, grande cheminée, tables de bois, voyageurs fatigués. Neige dehors. Le copiste seul près du feu, une écritoire sur les genoux.
- **Palette** : `#2E2620` bois · `#D99A4E` feu · accent `#9EA4AA` brume grise.

**Prompt — la brume dans l'auberge**
```
Low-ceilinged common room of a roadside coaching inn on a snowy night, heavy beams, big hearth whose fire is suddenly dying, wooden tables with a few tired travelers, a thick grey fog rolling in from nowhere and filling the room, a lone man at a table by the fire with a writing desk on his knees, a tall grey figure seated across from him half dissolved in the mist, tense
```

## L16. La route de l'Ouest (le Kronland)

**Chapitre** : 7. **Scènes** : les péniches sur l'Aldra ; les tours de temple ; Konrad qui voudrait s'arrêter partout.
- Contraste avec la Nebelmark : plus riche, plus vert, plus bruyant. Grand fleuve avec des péniches, villes fortifiées, clochers et tours de temple d'Haldor, champs cultivés, routes pavées.
- **Palette** : `#6E8C5A` vert riche · `#7C93A6` fleuve · `#C8B48A` pierre claire · accent `#D9A441` soleil.

**Prompt — l'Aldra**
```
A broad busy river in a rich green countryside, cargo barges with sails, a large walled town with tall temple towers and red roofs on the far bank, cultivated fields and a paved road along the bank, two riders seen from behind, bright late spring light after the grey of the east
```

## L17. Le col de la Dame Voilée

**Chapitre** : 7 (et chapitre 1 de la campagne). **Scènes** : le feu au pied des montagnes ; la chapelle noire au sommet ; l'embuscade ; « Ce chemin-là, un jour, tu le reprendras dans l'autre sens. Seul. »
- Les Monts Cendrés : roche nue, précipices, postes de garde abandonnés, cairns au bord du vide. Au sommet du col, une petite chapelle de pierre noire battue par le vent, couverte d'offrandes de voyageurs. À l'est, l'Empire noyé dans les nuages.
- **Palette** : `#3C4049` roche · `#8E99A8` ciel froid · `#1A1B1E` chapelle noire · accent `#E6EAF0` neige.

**Prompt — la chapelle du col**
```
A high mountain pass between bare grey rock peaks, a tiny chapel of black stone battered by wind at the summit, travelers' offerings and ribbons tied around it, stone cairns at the edge of a sheer drop, an abandoned guard post, a sea of clouds below hiding the lowlands to the east, an older man and a young man in grey cloaks looking down, cold and vast
```

## L18. Hautepierre

**Région** : royaume d'Aurevaux. **Chapitre** : 7. **Scènes** : la ville perchée ; les aigles de guerre autour des tours du duc ; Konrad à la porte de la ville face aux montagnes.
- Ville accrochée à la montagne au-dessus d'une gorge : maisons hautes et étroites, ponts vertigineux, remparts, tours ducales orgueilleuses, bannières au soleil d'or. Chevaliers de l'Aigle en armure sur les routes, paysans pauvres. Aigles de guerre qui tournent très haut.
- Changement de monde : lumière plus dorée, pierre plus claire, architecture plus « chevaleresque » et plus française que l'Empire. Pas de fleurs de lys.
- **Palette** : `#C9B994` pierre claire · `#6C7F95` gorge bleutée · `#8A6A3A` plumage · accent `#E2B755` lumière dorée.

**Prompt — la ville perchée**
```
A proud medieval city clinging to a mountainside above a deep gorge, tall narrow houses of pale stone, dizzying stone bridges, ramparts, slender ducal towers with banners showing a golden sun, giant golden-brown war eagles with armored riders circling high above the towers, golden afternoon light, French-inspired chivalric architecture, no fleur-de-lis, a lone young traveler at the city gate seen from behind facing the mountains
```

## L19. La chambre d'auberge de Hautepierre

**Chapitre** : 7. **Scène** : le réveil ; la chambre vide ; la boîte de métal et la lettre cachetée de cire grise.
- Petite chambre de la ville basse, près des remparts : lit, table, fenêtre sur les toits et les montagnes. La cape grise n'est plus à la porte. Sur la table : une boîte de métal cabossée et une lettre.
- **Palette** : `#8C7B66` bois clair · `#B9C2CC` lumière du matin · accent `#9AA0A6` cire grise.

**Prompt — la chambre vide**
```
A small simple inn room in a mountain city at early morning, an unmade bed, an empty peg on the back of the door, a wooden table by the window with a dented metal box and a folded letter sealed with a plain drop of grey wax, cold pale light, rooftops and mountains through the window, a sense of absence
```
