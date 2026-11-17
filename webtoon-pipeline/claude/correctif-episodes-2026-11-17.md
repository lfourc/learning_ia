# Correctif — mauvais épisodes de référence

*17/11/2026. À appliquer par Claude Code, après `SYNC-CLAUDE-CODE.md`.*

## Le problème
Les anciens fichiers de « La dernière journée » s'appellent encore `ep01-…`. Ce n'est plus l'épisode 1 : c'est la base du futur **épisode 3**. Ils ont été pris pour l'épisode 1.

## Ce qu'il faut faire
1. **Copier** `webtoon/episodes-references.md` dans le studio. C'est désormais la table qui dit quel fichier sert à quel épisode, et elle fait foi.
2. **Renommer** dans le studio (sections « Renommage conseillé » de cette table) :
   - `ep01-la-derniere-journee-v2.md` → `ep03-base-ancien-ep01-la-derniere-journee.md`
   - `ep01-v2-prompts-chatgpt.md` → `ep03-base-ancien-ep01-prompts.md`
   - `ep01-la-derniere-journee.md` → `archives/ancien-ep01-la-derniere-journee-v1.md`
   - `decoupage-ch01.md` → `archives/decoupage-ch01.md`
3. **Mettre à jour** tout ce qui pointait vers ces fichiers (`CLAUDE.md`, `refs.yaml`, scripts).
4. **Corriger les fichiers d'épisodes du studio** :
   - `ep02-pages-prompts-chatgpt.md` : remplacer la section « PAGE 18 — l'homme sous le chêne » par la « PAGE 18 (nouvelle) — personne » de `ep01-coda-et-ep02-plan.md`, et son carton de fin par « À suivre — Épisode 3 : La dernière journée ». Sa ligne « Réf. : » devient : `Ottilie, Moustache, page de style`.
   - `ep01-pages-prompts-chatgpt.md`, page 21 : remplacer « rubbing her sore wrist » par « tired ».
5. **Annuler** ce qui a été produit à partir des mauvais fichiers depuis la dernière synchronisation (pages générées, découpages, lettrage), et le signaler à Lyes avant de régénérer quoi que ce soit.
6. **Ajouter dans `CLAUDE.md`** la règle : « Le préfixe d'un fichier ne donne pas le numéro d'épisode. Toujours vérifier `webtoon/episodes-references.md`. »
7. **Faire un compte rendu** à Lyes : fichiers renommés, fichiers corrigés, productions annulées.
