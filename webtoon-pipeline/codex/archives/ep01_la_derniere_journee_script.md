# La Lame-Grise — Webtoon
# Épisode 1 : La dernière journée

*Script webtoon original. Il précède le chapitre 1 du livre, sans le modifier : l'épisode s'arrête au moment où Ottilie part chez Brunhild, là où commence le chapitre. Version 1, 14/11/2026, 46 cases.*

---

## 0. Ce qu'il faut savoir avant de générer

### Le nouveau bloc de style manhwa
Il remplace l'ancien bloc pour **toutes les cases du webtoon**. À coller à la fin de chaque prompt (ChatGPT le fait si les instructions sont mises à jour) :
```
Korean manhwa webtoon panel, clean confident ink lineart, cel shading with two or three flat tone steps, crisp edges, dramatic rim light, high contrast, cinematic dynamic camera angle, expressive faces, simplified soft background when the focus is emotional, muted desaturated palette with one accent color, no painterly texture, no text
```
Négatif :
```
oil painting, painterly brushstrokes, photorealism, overly detailed background everywhere, grain, christian cross, crucifix, fleur-de-lis, text, watermark, speech bubbles, extra fingers
```

### Les formats de cases
| Code | Format | Usage |
|---|---|---|
| **[LARGE]** | 16:9 | plan d'ensemble, installation d'un lieu |
| **[VERT]** | 9:16 | personnage en pied, moment fort |
| **[CASE]** | 4:3 | plan moyen, dialogue à deux |
| **[INSERT]** | 1:1 | détail : une main, un objet, un œil |
| **[BANDE]** | 3:1 | case étroite : un regard, un geste rapide |
| **[NOIR]** | pas d'image | case noire ou blanche avec texte, pour le silence |

### Le lettrage (ajouté au montage, jamais dans l'image)
- **ENCADRÉ** : boîte carrée sombre, narration et contexte.
- **FICHE** : boîte carrée claire, présentation d'un personnage (nom, rang, âge).
- **BULLE** : dialogue. **PENSÉE** : pensée. **CRI** : bulle en éclats.
- **SFX** : onomatopée dessinée.

### Les nouveaux personnages (planches à générer avant l'épisode)
| Personnage | Âge | Apparence | Prompt de planche |
|---|---|---|---|
| **Baron Ruprecht von Arnsfeld**, père d'Ottilie, veuf | 52 | grand, droit, barbe blonde grisonnante taillée court, yeux bleus las, pourpoint vert sombre, chaîne d'argent au tilleul | `Character reference sheet, front, three-quarter and back views, tall upright nobleman about 52, short-trimmed greying blond beard, tired clear blue eyes, dark green doublet with burgundy trim, silver chain with a linden tree pendant, dignified and weary, plain background` |
| **Matthias von Arnsfeld**, frère aîné, héritier | 24 | blond, carrure de cavalier, sourire facile, impatient | `Character reference sheet, front, three-quarter and back views, young nobleman about 24, athletic rider build, tousled blond hair, blue eyes, easy confident grin, green riding coat with burgundy trim, riding gloves, plain background` |
| **Tante Gisela**, sœur du baron, tient la maison | 48 | sèche, chignon gris-blond, trousseau de clés, regard qui voit tout | `Character reference sheet, front and three-quarter views, sharp lean noblewoman about 48, grey-blond hair in a tight bun under a small veil, keen blue eyes, dark burgundy gown, ring of household keys at her waist, plain background` |
| **Ottilie l'aînée**, cousine | 24 | blonde aussi, plus grande, coquette, moqueuse et tendre | `Character reference sheet, front and three-quarter views, tall pretty young noblewoman about 24, elaborate blonde braids, teasing smile, rich green and gold gown, plain background` |
| **Lorenz**, cousin, frère d'Ottilie l'aînée | 26 | large, joyeux, cheveux mouillés en permanence (il nage partout) | `Character reference sheet, front and three-quarter views, broad cheerful young man about 26, wet tousled light brown hair, open shirt and leather vest, laughing, plain background` |
| **Mathilde**, la nourrice | 64 | petite, ronde, coiffe blanche, mains de farine | `Character reference sheet, front and three-quarter views, small round old nursemaid about 64, white linen coif, flour on her hands and apron, warm stern face, plain background` |

### Les armes de la maison d'Arnsfeld
- **Armes publiques** : *de sinople au tilleul d'argent* (un tilleul argenté sur fond vert). On les voit sur le portail, la bannière, la chaîne du baron, la vaisselle.
- **Armes anciennes, secrètes** : le même tilleul, mais avec **une couronne d'or prise dans ses branches**. Ce sont les armes d'avant 604, celles du sang ottilien. On ne les voit que sur **la bague de la mère d'Ottilie**, et dans un coin de la vieille tapisserie de la grande salle, à demi caché. C'est la bague que Konrad tiendra un jour, « armes effacées ».

---

## Séquence A — Le domaine (le matin)

**E1.01 [LARGE]**
Le village d'Arnsfeld au petit matin d'automne, maisons à colombages, toits de chaume, fumées. Au-dessus, sur sa colline, le manoir de pierre claire. Tout autour, la forêt immense.
ENCADRÉ : « L'Eldwald, automne de l'an 791 de la Couronne. »
ENCADRÉ : « Sur les terres d'Arnsfeld, on disait que la forêt écoutait. »
`Wide establishing shot at early autumn morning, a small prosperous village of half-timbered houses with thatched roofs and chimney smoke, a pale stone noble manor on a green hill above it, an immense ancient forest all around, soft golden mist, peaceful`

**E1.02 [INSERT]**
La bannière du manoir qui claque au vent : un tilleul d'argent sur fond vert.
ENCADRÉ : « Les Arnsfeld. Une petite maison noble, vassale du prince d'Eldenheim. Trente âmes au manoir, quatre villages, beaucoup d'arbres. »
SFX : *flap flap*
`Close-up of a green banner snapping in the wind on a stone tower, embroidered with a silver linden tree, blue morning sky, fabric motion`

**E1.03 [VERT]**
Ottilie, 19 ans, dévale l'escalier extérieur du manoir en courant, un panier au bras, les cheveux défaits, déjà de la mousse sur la robe.
FICHE : « Ottilie von Arnsfeld. 19 ans. Cadette du baron. Préfère la forêt aux salons. »
`Dynamic low-angle shot, a young blonde noblewoman with blue eyes and freckles running down the outer stone stairs of a manor, basket on her arm, hair loose and flying, green gown with burgundy trim and a little moss on it, joyful, morning light`

**E1.04 [CASE]**
En bas de l'escalier, Mathilde la nourrice l'attend, bras croisés, les mains pleines de farine.
BULLE (Mathilde) : « Où est-ce qu'on court comme ça, sans avoir mangé ? »
BULLE (Ottilie) : « Chez Brunhild ! Elle a de la cire pour les onguents. »
`Medium shot at the foot of manor stairs, a small round old nursemaid in a white coif with floury hands and arms crossed, stopping a breathless young blonde woman with a basket, warm comedic tension, morning courtyard`

**E1.05 [BANDE]**
Mathilde lui fourre un petit pain chaud dans la main.
BULLE (Mathilde) : « Ce soir. Tu iras ce soir. Ta tante te cherche. »
`Narrow close shot, an old floury hand pushing a small warm bread roll into a young woman's hand, steam rising`

**E1.06 [CASE]**
Ottilie mord dans le pain en faisant la grimace, Mathilde secoue la tête en souriant.
FICHE : « Mathilde. Nourrice de la maison depuis quarante ans. A élevé Ottilie après la mort de sa mère. »
BULLE (Ottilie, la bouche pleine) : « Elle me cherche toujours. »
`Medium shot, a young blonde woman biting into bread with a playful grimace while the old nursemaid shakes her head with a fond smile, light comedy`

---

## Séquence B — La maison (la matinée)

**E1.07 [LARGE]**
La grande salle du manoir : longue table, grande cheminée, et au mur une immense tapisserie ancienne montrant un tilleul dans une forêt.
ENCADRÉ : « La grande salle d'Arnsfeld. On y mangeait, on y jugeait, on y recevait. »
`Wide interior of a noble manor great hall, long oak table, huge stone fireplace, morning light through tall windows, a huge faded antique tapestry on the wall depicting a great linden tree in a forest`

**E1.08 [CASE]**
Tante Gisela compte des draps avec une servante, le trousseau de clés à la ceinture. Elle voit Ottilie entrer sans tourner la tête.
FICHE : « Gisela von Arnsfeld. Sœur du baron. Veuve. Tient la maison, les comptes et tout le monde. »
BULLE (Gisela) : « Tu as de la mousse dans les cheveux. »
`Medium shot, a sharp lean noblewoman about 48 with a grey-blond bun and keys at her waist counting linen with a servant, not looking up, while a young blonde woman enters behind her`

**E1.09 [BANDE]**
Ottilie se tâte les cheveux et en retire un brin de mousse.
PENSÉE (Ottilie) : « Comment elle fait ? »
`Narrow close shot, a young woman's hand pulling a sprig of moss out of her blonde hair, embarrassed expression at the edge of the frame`

**E1.10 [CASE]**
Entrée bruyante de Lorenz, trempé, et d'Ottilie l'aînée qui rit derrière lui.
BULLE (Lorenz) : « J'ai traversé l'Elda à la nage ! Deux fois ! »
BULLE (Ottilie l'aînée) : « Il a perdu une botte. Deux fois. »
FICHE : « Lorenz et Ottilie l'aînée. Les cousins. Chez les Arnsfeld, chaque génération a sa Ottilie. Dans celle-ci, il y en a deux. »
`Medium shot, a broad cheerful soaking wet young man bursting into a great hall with one bare foot, laughing, behind him a tall elegant blonde young woman with elaborate braids laughing, water dripping on the floor`

**E1.11 [INSERT]**
La tante Gisela regarde la flaque par terre. Un seul sourcil levé.
`Extreme close-up of a stern noblewoman's single raised eyebrow, puddle of water reflected below, comedic beat`

**E1.12 [CASE]**
Ottilie et sa cousine, côte à côte devant la tapisserie.
BULLE (Ottilie l'aînée) : « La grande et la petite Ottilie. Père dit que c'est une tradition. »
BULLE (Ottilie) : « Père ne dit jamais pourquoi. »
`Medium shot, two blonde young women side by side in front of a huge antique tapestry of a linden tree, the taller one teasing, the younger one thoughtful, soft hall light`

**E1.13 [INSERT]**
Gros plan sur un coin usé de la tapisserie : dans les branches du tilleul, à demi effacée, une petite couronne d'or.
ENCADRÉ : « Il y avait des choses, dans cette maison, que personne ne regardait de trop près. »
`Extreme close-up of a worn corner of an antique tapestry, woven linden branches, half-faded, a small golden crown hidden among the leaves, dust in the light, mysterious`

---

## Séquence C — Le visiteur (midi)

**E1.14 [LARGE]**
Des cavaliers montent la route vers le manoir : un noble richement vêtu et deux hommes d'escorte. Bannière inconnue.
`Wide shot of three riders climbing the road toward a pale stone manor on a hill, a richly dressed nobleman in front with a dark blue cloak, two armed escorts, autumn trees, midday light`

**E1.15 [CASE]**
Dans la cour, Matthias, en tenue de cheval, accueille les visiteurs.
FICHE : « Matthias von Arnsfeld. 24 ans. L'héritier. Bon cavalier, mauvais diplomate. »
BULLE (Matthias) : « Comte von Weissenau. Mon père ne vous attendait pas. »
BULLE (le comte) : « Ton père ne m'attend jamais, mon garçon. C'est pour ça que je viens. »
`Medium shot in a manor courtyard, a young athletic blond nobleman in a green riding coat greeting a dismounting older nobleman in a rich dark blue cloak with a silver beard and a smooth smile, tension under courtesy`

**E1.16 [VERT]**
Le baron Ruprecht apparaît en haut des marches, droit, sans sourire.
FICHE : « Ruprecht von Arnsfeld. Baron d'Arnsfeld. 52 ans. Veuf. N'a jamais rien demandé à personne. »
BULLE (Ruprecht) : « Albrecht. Entre. Et dis-le vite. »
`Low-angle full shot, a tall upright nobleman about 52 with a greying blond beard and tired blue eyes standing at the top of manor stairs, silver linden chain on his chest, cold authority, midday light behind him`

**E1.17 [BANDE]**
Ottilie, à une fenêtre de l'étage, regarde la scène, curieuse.
`Narrow shot, a young blonde woman's face at an upper manor window, watching the courtyard below, curious`

**E1.18 [CASE]**
Le cabinet du baron. Le comte pose une liasse de lettres scellées sur la table.
BULLE (le comte) : « Douze familles de l'Eldwald, Ruprecht. Douze. Elles n'attendent qu'un nom. »
BULLE (Ruprecht) : « Elles attendront longtemps. »
`Medium shot in a small study with books and a window, a smooth older nobleman in dark blue placing a stack of sealed letters on a desk in front of a seated stern baron, candle and daylight mixed, conspiratorial mood`

**E1.19 [INSERT]**
Gros plan sur la liasse : les sceaux de cire portent tous le même signe, un tilleul couronné.
`Extreme close-up of a stack of folded letters sealed with red wax, each seal stamped with a linden tree wearing a crown`

**E1.20 [CASE]**
Derrière la porte entrouverte, Ottilie écoute, le panier contre elle.
BULLE (hors champ, le comte) : « Le sang n'est pas un fardeau. C'est une couronne qu'on a mise de côté. »
PENSÉE (Ottilie) : « ... le sang ? »
`Medium shot through a gap in a half-open door, a young blonde woman listening in the corridor, clutching her basket, wide blue eyes, the study visible in the gap`

**E1.21 [VERT]**
Le baron se lève et jette toute la liasse dans le feu de la cheminée.
BULLE (Ruprecht) : « Nous sommes des Arnsfeld. Des gens de la forêt. »
BULLE (Ruprecht) : « Rentre à Eldenheim, Albrecht. Et ne reviens pas. »
SFX : *FFWOUF*
`Dramatic shot, a stern baron throwing a stack of sealed letters into a roaring fireplace, flames flaring up, the smooth visitor recoiling, strong orange light on their faces, the only warm color in a cold room`

**E1.22 [CASE]**
Le comte remet ses gants, sans colère, avec un sourire triste.
BULLE (le comte) : « Ce n'est pas moi qu'il faut craindre, Ruprecht. Ce sont ceux qui savent compter aussi bien que moi. »
`Medium shot, the older nobleman in dark blue slowly putting on his gloves, a sad knowing smile, the baron's back turned in the foreground`

**E1.23 [NOIR]**
ENCADRÉ (texte blanc sur noir) : « Douze familles savaient. »
ENCADRÉ : « Combien d'autres ? »

---

## Séquence D — Le secret (l'après-midi)

**E1.24 [CASE]**
Plus tard. Le baron trouve Ottilie assise sur les marches de la chapelle, le panier sur les genoux.
BULLE (Ruprecht) : « Tu écoutes aux portes, maintenant ? »
BULLE (Ottilie) : « Seulement à celles qui parlent de moi. »
`Medium shot, afternoon, a tall weary baron approaching his young daughter sitting on the stone steps of a small family chapel, basket on her knees, autumn leaves, gentle tension`

**E1.25 [CASE]**
Il s'assoit à côté d'elle, lourdement. Un long silence.
ENCADRÉ : « Son père ne lui avait parlé du sang qu'une seule fois, trois ans plus tôt. À voix basse, comme d'une maladie de famille. »
`Medium shot, the baron sitting down heavily beside his daughter on chapel steps, both looking at the forest, quiet, long shadows`

**E1.26 [CASE]**
BULLE (Ottilie) : « Le comte a dit "couronne". »
BULLE (Ruprecht) : « Le comte dit beaucoup de choses. Ce qui compte, c'est ce qu'on ne dit pas. »
`Two-shot close, father and daughter on chapel steps, she looking at him intently, he looking away at the trees`

**E1.27 [INSERT]**
Il lui prend la main et fait glisser à son doigt une bague d'or ancienne.
`Close-up of an older man's hands sliding an old gold signet ring onto a young woman's finger, autumn light`

**E1.28 [INSERT]**
Gros plan sur la bague : le tilleul, et la petite couronne dans ses branches.
ENCADRÉ : « Les armes d'avant. »
`Extreme close-up of an old gold signet ring engraved with a linden tree and a tiny crown caught in its branches, slightly worn, glinting`

**E1.29 [CASE]**
BULLE (Ruprecht) : « C'était celle de ta mère. Elle ne la montrait jamais. »
BULLE (Ruprecht) : « Toi non plus. Promets. »
BULLE (Ottilie) : « ... Je promets. »
`Medium close-up, the baron holding his daughter's hand with the ring, serious and tender, her blue eyes shining`

**E1.30 [BANDE]**
Elle referme le poing sur la bague.
`Narrow close shot, a young woman's hand closing into a fist over a gold ring`

**E1.31 [NOIR]**
ENCADRÉ : « Elle tiendrait cette promesse onze ans. »

---

## Séquence E — Le cadeau (fin d'après-midi)

**E1.32 [LARGE]**
Une charrette entre dans la cour du manoir, chargée de trois tonneaux. Le charretier porte un chapeau qui cache son visage.
`Wide shot, late afternoon golden light, a cart with three wine barrels entering a manor courtyard, the carter's face hidden under a wide hat, servants approaching`

**E1.33 [CASE]**
Tante Gisela lit un billet qu'il lui tend.
BULLE (Gisela) : « "Avec les excuses du comte von Weissenau, pour son impolitesse." »
BULLE (Matthias) : « Il s'excuse avec du vin, au moins. »
`Medium shot, the sharp aunt reading a small note in the courtyard next to the cart, the young heir grinning beside her, the hatted carter looking down`

**E1.34 [INSERT]**
Le cachet de cire du billet : un tilleul couronné, mais **le trait est différent**, comme une copie.
`Extreme close-up of a broken red wax seal on a note, showing a crowned linden tree, but slightly crude and imprecise like a forgery`

**E1.35 [BANDE]**
Le charretier repart. Sous le chapeau, on ne voit qu'un menton rasé et une bouche qui ne sourit pas.
`Narrow shot, a carter driving away seen from below his wide hat brim, only a clean-shaven chin and an unsmiling mouth visible, cold`

---

## Séquence F — Le départ (le soir)

**E1.36 [CASE]**
La cuisine. Mathilde emballe un pot de miel pour Brunhild.
BULLE (Mathilde) : « Tu rentres avant le souper. On ouvre le vin du comte. »
BULLE (Ottilie) : « Gardez-m'en un verre ! »
`Medium shot in a warm manor kitchen at dusk, the old nursemaid wrapping a honey pot in cloth, the young blonde woman taking a lantern from a hook, cozy firelight`

**E1.37 [CASE]**
Dans la grande salle, Matthias et Lorenz font rouler un tonneau en riant. Le baron les regarde, plus détendu.
BULLE (Lorenz) : « Pour une fois qu'Eldenheim nous fait un cadeau ! »
`Medium shot, two young men laughing while rolling a wine barrel across a great hall, the baron watching with a rare small smile, candles being lit`

**E1.38 [VERT]**
Ottilie, à la porte du manoir, lanterne à la main. Elle se retourne une dernière fois vers la maison éclairée.
ENCADRÉ : « Elle se retourna une dernière fois. Elle ne savait pas pourquoi. »
`Full shot from behind, a young blonde woman at the manor's open gate at dusk holding a lit lantern, turning back to look at the warmly lit manor windows, blue evening falling, the forest dark ahead`

**E1.39 [CASE]**
Sa cousine lui fait signe d'une fenêtre, une coupe à la main.
BULLE (Ottilie l'aînée) : « Ne laisse pas la vieille Brunhild te garder jusqu'à minuit ! »
`Medium shot looking up, the tall blonde cousin leaning out of a lit upper window waving with a wine cup in her hand, warm light, blue dusk around`

**E1.40 [BANDE]**
Ottilie rit et s'enfonce dans la forêt. La lanterne devient un point.
`Narrow wide shot, a small lantern light disappearing into a vast dark forest at dusk`

---

## Séquence G — Le souper (la nuit)

**E1.41 [LARGE]**
La grande salle illuminée, toute la maisonnée à table : le baron, Matthias, Gisela, Lorenz, Ottilie l'aînée, et au bout les domestiques. Une chaise vide.
`Wide warm interior at night, a noble family and servants feasting at a long table in a candlelit great hall, the baron at the head, laughter, one empty chair, the antique linden tapestry behind them`

**E1.42 [INSERT]**
Le vin rouge versé dans les coupes.
SFX : *glou glou*
`Close-up of dark red wine pouring from a jug into pewter cups, candlelight reflections`

**E1.43 [CASE]**
Le baron lève sa coupe.
BULLE (Ruprecht) : « À la maison d'Arnsfeld. »
TOUS : « À Arnsfeld ! »
`Medium shot, the baron raising a pewter cup, family members raising theirs around the table, warm candlelight, faces happy`

**E1.44 [INSERT]**
La chaise vide d'Ottilie, une coupe pleine posée devant.
`Close-up of an empty wooden chair at a feast table with a full untouched cup of red wine in front of it, candlelight`

**E1.45 [LARGE]**
Dehors, sur la colline, à la lisière du parc, deux silhouettes encapuchonnées regardent les fenêtres éclairées du manoir. Elles ne bougent pas.
`Wide night shot, cold blue, two motionless hooded figures standing at the dark edge of a park looking up at a manor with warm glowing windows, utterly still, ominous`

**E1.46 [NOIR]**
ENCADRÉ : « Ce fut leur dernier repas. »
*Fin de l'épisode 1.*
*(L'épisode 2 reprend avec le chapitre 1 du livre : Ottilie chez Brunhild, la fumée, l'incendie.)*

---

## Notes pour la suite
- **Ce que l'épisode ajoute au récit** : le comte von Weissenau, chef des restaurationnistes de l'Eldwald (il revient plus tard) ; le vin offert sous un faux sceau (c'est ainsi que la Main Grise a endormi la maison : « un sommeil qu'on leur avait donné ») ; la bague remise par le père. **Ces trois points restent des propositions** : ils ne changent rien au texte du livre et peuvent y être ajoutés plus tard si tu les valides.
- **Le nom d'Ottilie** : chez elle, on l'appelle « la petite Ottilie ». Ça la distingue de sa cousine et ça rendra plus forte la mort de la grande au chapitre 1.
- **Ordre de génération conseillé** : d'abord les 6 nouvelles planches de personnages, puis les cases dans l'ordre. Les [NOIR] ne se génèrent pas : je les fais au montage.
