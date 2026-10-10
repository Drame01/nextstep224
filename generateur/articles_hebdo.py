# Articles hebdomadaires du blog Amploi.
# Ajouter chaque nouvel article EN FIN de liste, au même format (voir CLAUDE.md à la racine).
# Puis lancer : python3 generateur/build.py
HEBDO = [
 dict(slug="excel-poste-administratif", cat="Conseils", icon="grid", cover="c5",
      date="10 octobre 2026", iso="2026-10-10",
      title="Excel : les 10 fonctions à maîtriser pour décrocher un poste administratif",
      excerpt="« Maîtrise d'Excel exigée » : cette ligne revient dans presque toutes les offres. Voici ce que les recruteurs entendent vraiment par là, et les fonctions à apprendre en priorité.",
      body="""
<p>Assistant administratif, comptable, gestionnaire de stock, chargé de suivi-évaluation, logisticien, assistant RH : dans presque toutes ces offres, on retrouve la même ligne, « Bonne maîtrise d'Excel ». Beaucoup de candidats l'écrivent sur leur CV sans savoir exactement ce qu'elle recouvre, et se retrouvent en difficulté lors d'un test pratique.</p>
<p>Bonne nouvelle : il n'est pas nécessaire de tout connaître. Une dizaine de fonctions et d'outils couvrent l'essentiel des besoins d'un poste administratif. Les voici, avec un exemple concret pour chacune.</p>

<h2>Ce que « maîtrise d'Excel » veut dire pour un recruteur</h2>
<p>Pour la plupart des postes administratifs, le recruteur attend que vous sachiez :</p>
<ul>
  <li><strong>Construire un tableau propre</strong> : titres de colonnes, formats de nombres et de dates, largeur des colonnes, mise en forme lisible ;</li>
  <li><strong>Faire des calculs</strong> sans calculatrice, avec des formules qui se mettent à jour automatiquement ;</li>
  <li><strong>Retrouver et trier l'information</strong> rapidement dans un fichier de plusieurs centaines de lignes ;</li>
  <li><strong>Résumer des données</strong> pour un rapport : totaux par mois, par client, par projet.</li>
</ul>
<p>Les dix outils ci-dessous répondent à ces quatre besoins.</p>

<h2>1. SOMME, MOYENNE, MIN et MAX</h2>
<p>Ce sont les bases. <strong>=SOMME(B2:B50)</strong> additionne une colonne, <strong>=MOYENNE(B2:B50)</strong> calcule la moyenne, <strong>=MIN</strong> et <strong>=MAX</strong> donnent la plus petite et la plus grande valeur.</p>
<p><em>Exemple :</em> le total des dépenses du mois, le montant moyen d'une facture, la vente la plus élevée de la semaine.</p>

<h2>2. Les références absolues ($)</h2>
<p>Quand vous recopiez une formule vers le bas, Excel décale automatiquement les cellules. Parfois, vous voulez qu'une cellule reste fixe : un taux, un prix unitaire, un total. Le signe <strong>$</strong> bloque la référence : <strong>=B2*$E$1</strong>.</p>
<p><em>Exemple :</em> calculer la TVA de chaque ligne en multipliant le montant par un taux écrit une seule fois en haut du tableau. C'est l'une des questions les plus fréquentes dans les tests pratiques.</p>

<h2>3. SI</h2>
<p>La fonction <strong>SI</strong> affiche un résultat différent selon une condition : <strong>=SI(C2>=100000;"Remise";"Pas de remise")</strong>.</p>
<p><em>Exemple :</em> indiquer si une facture est payée ou non, si un stock est sous le seuil d'alerte, si un objectif est atteint.</p>

<h2>4. NB.SI et SOMME.SI</h2>
<p>Ces fonctions comptent ou additionnent uniquement les lignes qui respectent une condition :</p>
<ul>
  <li><strong>=NB.SI(D2:D200;"Conakry")</strong> compte le nombre de lignes où la ville est Conakry ;</li>
  <li><strong>=SOMME.SI(D2:D200;"Conakry";E2:E200)</strong> additionne les montants de ces lignes.</li>
</ul>
<p>Leurs versions <strong>NB.SI.ENS</strong> et <strong>SOMME.SI.ENS</strong> acceptent plusieurs conditions à la fois (par exemple : la ville <em>et</em> le mois).</p>
<p><em>Exemple :</em> le total des ventes par agence, le nombre de bénéficiaires par préfecture, les dépenses par ligne budgétaire.</p>

<h2>5. RECHERCHEV (ou RECHERCHEX)</h2>
<p>C'est la fonction la plus demandée en entretien. Elle va chercher une information dans un autre tableau à partir d'un identifiant : <strong>=RECHERCHEV(A2;Produits!A:C;3;FAUX)</strong> cherche le code produit de la cellule A2 dans la feuille « Produits » et renvoie la valeur de la 3<sup>e</sup> colonne (par exemple, le prix).</p>
<p>N'oubliez pas le dernier argument <strong>FAUX</strong>, qui impose une correspondance exacte : c'est l'erreur la plus fréquente. Dans les versions récentes d'Excel, <strong>RECHERCHEX</strong> fait la même chose de façon plus simple et plus souple.</p>
<p><em>Exemple :</em> retrouver le nom et le service d'un employé à partir de son matricule, ou le prix d'un article à partir de son code.</p>

<h2>6. SIERREUR</h2>
<p>Quand une formule ne trouve pas de résultat, Excel affiche une erreur du type #N/A, peu agréable dans un rapport. <strong>=SIERREUR(RECHERCHEV(...);"Introuvable")</strong> remplace l'erreur par un texte de votre choix.</p>

<h2>7. Le tri et les filtres</h2>
<p>Ce ne sont pas des fonctions, mais des outils indispensables. Sélectionnez votre tableau, puis <strong>Données &gt; Filtrer</strong> : une flèche apparaît sur chaque titre de colonne. Vous pouvez alors afficher uniquement les factures impayées, trier les clients par montant, ou retrouver toutes les lignes d'un fournisseur.</p>
<p>Astuce : transformez votre plage en <strong>tableau Excel</strong> (Ctrl + L, ou Ctrl + T selon la version). Les filtres s'ajoutent automatiquement et les formules s'étendent seules aux nouvelles lignes.</p>

<h2>8. La mise en forme conditionnelle</h2>
<p>Elle colore automatiquement les cellules selon leur valeur : en rouge les stocks sous le seuil, en vert les objectifs atteints, en orange les échéances proches. Menu <strong>Accueil &gt; Mise en forme conditionnelle</strong>.</p>
<p>Pour un responsable qui lit votre fichier, c'est la différence entre un tableau de chiffres et un outil de pilotage qui se lit en un coup d'œil.</p>

<h2>9. Les tableaux croisés dynamiques</h2>
<p>C'est l'outil qui impressionne le plus en entretien, et il est plus simple qu'il n'y paraît. À partir d'une liste de plusieurs centaines de lignes (par exemple toutes les ventes de l'année), il crée en quelques clics un résumé : total par mois, par commercial, par produit. Menu <strong>Insertion &gt; Tableau croisé dynamique</strong>, puis glissez les champs dans les zones Lignes, Colonnes et Valeurs.</p>
<p><em>Exemple :</em> préparer le rapport mensuel des dépenses par catégorie, ou le nombre de formations réalisées par région.</p>

<h2>10. Les fonctions de date et de texte</h2>
<ul>
  <li><strong>=AUJOURDHUI()</strong> affiche la date du jour ; combinée à une date d'échéance, elle calcule un retard : <strong>=AUJOURDHUI()-C2</strong> ;</li>
  <li><strong>=MOIS(C2)</strong> et <strong>=ANNEE(C2)</strong> extraient le mois ou l'année d'une date, pratique pour regrouper ;</li>
  <li><strong>=CONCAT(A2;" ";B2)</strong> (ou CONCATENER) assemble le prénom et le nom ;</li>
  <li><strong>=SUPPRESPACE(A2)</strong> supprime les espaces en trop, fréquents dans les fichiers copiés depuis d'autres sources.</li>
</ul>

<h2>Comment apprendre rapidement</h2>
<ul>
  <li><strong>Pratiquez sur un vrai cas</strong> : créez un fichier de suivi de vos propres dépenses, ou de vos candidatures, et appliquez chaque fonction. On retient beaucoup mieux en faisant.</li>
  <li><strong>Une fonction par jour</strong> : en deux semaines, vous aurez parcouru toute la liste.</li>
  <li><strong>Utilisez les ressources gratuites</strong> : l'aide intégrée d'Excel, les nombreux tutoriels vidéo en français, et les formations en ligne gratuites.</li>
  <li><strong>Pas d'ordinateur ?</strong> Les tableurs gratuits comme Google Sheets ou LibreOffice Calc utilisent presque les mêmes formules, et Google Sheets fonctionne même sur smartphone.</li>
</ul>

<h2>Comment le mettre en valeur sur votre CV</h2>
<p>Ne vous contentez pas d'écrire « Excel ». Soyez précis, et montrez une utilisation concrète :</p>
<div class="compare">
  <div class="bad"><b>À éviter</b>Informatique : Word, Excel, PowerPoint.</div>
  <div class="good"><b>À préférer</b>Excel : RECHERCHEV, SOMME.SI, tableaux croisés dynamiques. Création d'un fichier de suivi des stocks utilisé chaque semaine par l'équipe.</div>
</div>
<p>Et soyez honnête : de nombreux recruteurs font passer un test pratique de 20 à 30 minutes. Un candidat qui annonce une « maîtrise avancée » et bloque sur une RECHERCHEV perd toute crédibilité. Mieux vaut annoncer un niveau juste, puis le dépasser le jour du test.</p>

<blockquote>Excel n'est pas une compétence réservée aux comptables. C'est un outil de travail quotidien dans presque tous les bureaux. Dix fonctions bien maîtrisées suffisent pour faire la différence face à d'autres candidats.</blockquote>
"""),
]
