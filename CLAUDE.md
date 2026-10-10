# Site Amploi

Site statique (HTML/CSS/JS, sans framework) d'Amploi : accompagnement carrière et recrutement en Guinée.
Marque « Amploi », couleurs bleu et blanc, contenu en français. Hébergé via Vercel depuis la branche `main`.

## Ne pas modifier les pages HTML à la main

Toutes les pages (`index.html`, `blog.html`, `blog/*.html`, `sitemap.xml`, `robots.txt`) sont **générées**
par `generateur/build.py`. Modifier le générateur ou les données, puis lancer :

```
python3 generateur/build.py
```

- Contenu de l'accueil (packs, FAQ, offres, services) : `generateur/build.py`
- Articles : `generateur/build.py` (POSTS), `new_posts.py`, `long1.py`, `long2.py`, `articles_hebdo.py`
- Styles : `styles.css` (non généré) ; scripts : `main.js` (non généré)
- Adresse du site pour le SEO : `SITE_URL` dans `generateur/build.py`

Tarifs fixés : Essentiel 39 000 GNF, Pro 79 000 GNF, Premium 159 000 GNF. Contact WhatsApp +224 620 02 88 13, e-mail droum09@gmail.com.

## Avis clients

Liste `AVIS` dans `generateur/build.py`. N'y mettre que de **vrais** avis transmis par le propriétaire du site,
avec l'accord du client, sans réécrire le texte. Ne jamais inventer d'avis. Liste vide = la section n'apparaît pas.

## Ajouter l'article de la semaine

1. Lister les titres existants pour ne pas répéter un sujet : `grep -h 'title=' generateur/*.py`
2. Choisir un sujet utile aux chercheurs d'emploi en Guinée, qui n'est pas déjà traité.
3. Ajouter un `dict(...)` **à la fin** de la liste `HEBDO` dans `generateur/articles_hebdo.py`, au même format que les articles existants :
   - `slug` en minuscules avec tirets ; `cat` parmi : CV, Lettre de motivation, Entretien, LinkedIn, Conseils, Carrière
   - `icon` et `cover` : champs conservés pour compatibilité mais plus affichés depuis la refonte ; `icon` parmi : file mail linkedin chat check arrow shield clock users briefcase target star pin search pen mic coins facebook link doc-search alert calendar grid refresh
   - `cover` de `c1` à `c6` (alterner) ; `date` en toutes lettres (« 17 octobre 2026 ») et `iso` (« 2026-10-17 ») = date du jour
   - `body` en HTML : `<p>`, `<h2>`, `<h3>`, `<ul>`, `<blockquote>`, `<div class="compare"><div class="bad"><b>À éviter</b>…</div><div class="good"><b>À préférer</b>…</div></div>`
4. Règles de rédaction : 900 à 1 500 mots, au moins 5 sections `<h2>` (un sommaire est alors généré), ton concret et bienveillant,
   exemples adaptés à la Guinée. **Ne jamais inventer** de chiffres, statistiques, lois, salaires ou faits précis sur des entreprises réelles ;
   les prénoms et noms d'exemple sont fictifs. Liens internes possibles vers d'autres articles : `href="slug.html"`.
5. Lancer `python3 generateur/build.py`, vérifier que la nouvelle page existe dans `blog/` et que les liens internes pointent vers des fichiers existants.
6. Committer, pousser sur une branche, ouvrir une pull request vers `main` et la fusionner (squash).
