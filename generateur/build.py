import os, json, urllib.parse

# Le site est généré à la racine du dépôt (dossier parent de generateur/)
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WA_NUM = "224620028813"
EMAIL = "droum09@gmail.com"
SITE = "Amploi"
# Adresse publique du site (à changer si vous avez un nom de domaine)
SITE_URL = "https://nextstep224.vercel.app"

def wa(text):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(text)

# ---------- Icônes (style trait, 24x24) ----------
P = {
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
 "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "arrow": '<path d="M5 12h14M13 5l7 7-7 7"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
 "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
 "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10a7 7 0 0 1-14 0M12 17v5"/>',
 "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.3 18M7 6h1v4M16.7 13.9l.7.7-2.8 2.8"/>',
 "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
 "link": '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
 "doc-search": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h6"/><path d="M14 2v6h6v3"/><circle cx="17" cy="17" r="3"/><path d="m21 21-1.8-1.8"/>',
}
def ic(name, sw=2):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.5 1 3 .8 3.6.7.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.3A11.8 11.8 0 0 0 1.7 17.8L0 24l6.3-1.7a11.8 11.8 0 0 0 5.7 1.4A11.8 11.8 0 0 0 20.4 3.5z"/></svg>'

# ---------- Articles du blog ----------
POSTS = [
 dict(slug="erreurs-cv-eliminatoires", cat="CV", icon="doc-search", cover="c1",
      date="15 septembre 2026", iso="2026-09-15", read=6,
      title="7 erreurs qui font rejeter un CV en quelques secondes",
      excerpt="Photo mal choisie, adresse e-mail fantaisiste, liste de tâches sans résultats… Les erreurs qui envoient votre CV directement à la corbeille, et comment les corriger.",
      body="""
<p>Un recruteur qui reçoit cinquante, cent ou deux cents candidatures pour un poste ne lit pas chaque CV en détail. Il fait un premier tri rapide, souvent en quelques secondes par dossier. À ce stade, il ne cherche pas la meilleure candidature : <strong>il cherche une raison d'écarter la vôtre</strong>.</p>
<p>Voici les sept erreurs que nous rencontrons le plus souvent dans les CV qu'on nous envoie, et comment les éviter.</p>

<h2>1. Une adresse e-mail peu professionnelle</h2>
<p>« bebe.dalaba2000@… » ou « le_boss_224@… » : c'est la première chose que le recruteur voit, et cela suffit à donner une mauvaise impression. Créez une adresse simple, du type <strong>prenom.nom@gmail.com</strong>, et utilisez-la uniquement pour vos candidatures.</p>

<h2>2. Une photo inadaptée</h2>
<p>En Guinée, la photo reste courante sur un CV. Mais une photo de soirée, un selfie recadré ou une image floue fait plus de mal que de bien. Choisissez une photo récente, de face, sur fond neutre, avec une tenue que vous porteriez en entretien. Si vous n'en avez pas de bonne, mieux vaut ne pas en mettre.</p>

<h2>3. Une liste de tâches au lieu de résultats</h2>
<p>C'est l'erreur la plus répandue. Le recruteur connaît déjà les tâches d'un comptable ou d'un commercial. Ce qu'il veut savoir, c'est <em>ce que vous avez accompli</em>.</p>
<div class="compare">
  <div class="bad"><b>À éviter</b>Chargé de la gestion des clients.</div>
  <div class="good"><b>À préférer</b>Suivi d'un portefeuille de 120 clients, dont 15 nouveaux comptes signés en 2025.</div>
</div>

<h2>4. Un CV trop long</h2>
<p>Pour un jeune diplômé, une page suffit. Pour un profil expérimenté, deux pages maximum. Au-delà, le recruteur décroche. Supprimez les stages de plus de dix ans, les formations sans rapport avec le poste et les centres d'intérêt génériques (« lecture, voyages, musique »).</p>

<h2>5. Des fautes d'orthographe</h2>
<p>Une faute dans le titre ou dans le nom de l'entreprise visée est souvent éliminatoire, surtout pour les postes administratifs. Relisez à voix haute, puis faites relire par quelqu'un d'autre. Les outils de correction automatique ne détectent pas tout.</p>

<h2>6. Le même CV pour toutes les offres</h2>
<p>Un CV envoyé tel quel à une ONG, à une banque et à une société minière ne parle à aucune des trois. Reprenez le vocabulaire de l'offre, mettez en avant les expériences les plus proches du poste et adaptez votre titre de profil à chaque candidature.</p>

<h2>7. Une mise en page illisible par les logiciels de tri</h2>
<p>De plus en plus d'entreprises, notamment les grands groupes et les multinationales présentes à Conakry, Boké ou Kamsar, utilisent des logiciels qui lisent les CV automatiquement (ATS). Les tableaux complexes, les colonnes multiples, le texte dans des images ou les polices fantaisistes peuvent rendre votre CV illisible pour ces outils. Préférez une structure claire, des titres de section classiques (« Expérience professionnelle », « Formation », « Compétences ») et un export PDF propre.</p>

<blockquote>Retenez ceci : un bon CV ne raconte pas toute votre vie. Il donne au recruteur une raison claire de vous appeler.</blockquote>
"""),
 dict(slug="lettre-de-motivation-structure", cat="Lettre de motivation", icon="pen", cover="c2",
      date="2 septembre 2026", iso="2026-09-02", read=5,
      title="Lettre de motivation : la structure en 3 paragraphes qui fonctionne",
      excerpt="Vous, moi, nous : une méthode simple pour écrire une lettre courte, personnalisée et convaincante, avec un exemple concret à adapter.",
      body="""
<p>Beaucoup de candidats considèrent la lettre de motivation comme une formalité. Résultat : des lettres longues, génériques, qui commencent toutes par « Suite à votre annonce parue sur… ». Or une bonne lettre peut faire la différence entre deux profils équivalents.</p>
<p>La méthode la plus efficace tient en trois paragraphes : <strong>vous, moi, nous</strong>.</p>

<h2>Paragraphe 1 : « Vous » (l'entreprise)</h2>
<p>Commencez par montrer que vous connaissez l'entreprise et que vous ne postulez pas au hasard. Parlez d'un projet, d'une activité, d'une valeur ou d'une actualité qui vous intéresse réellement.</p>
<blockquote>« Votre engagement dans le développement de l'accès à l'énergie en zone rurale, notamment à travers votre projet en Moyenne-Guinée, correspond exactement au domaine dans lequel je souhaite construire ma carrière. »</blockquote>

<h2>Paragraphe 2 : « Moi » (ce que vous apportez)</h2>
<p>Ne répétez pas votre CV. Choisissez <strong>deux ou trois réalisations</strong> qui répondent directement aux besoins du poste, et donnez des éléments concrets : chiffres, résultats, situations.</p>
<ul>
  <li>Une expérience qui prouve une compétence demandée dans l'offre ;</li>
  <li>Un résultat chiffré ou une réussite précise ;</li>
  <li>Une qualité personnelle illustrée par un exemple, pas simplement affirmée.</li>
</ul>

<h2>Paragraphe 3 : « Nous » (la suite)</h2>
<p>Expliquez ce que vous pourriez accomplir ensemble, puis proposez une rencontre. Restez simple et direct.</p>
<blockquote>« Je serais heureux de vous présenter plus en détail la manière dont je pourrais contribuer à vos projets lors d'un entretien, à la date qui vous conviendra. »</blockquote>

<h2>Les règles à respecter</h2>
<ul>
  <li><strong>Une page maximum</strong>, idéalement 250 à 350 mots.</li>
  <li><strong>Le nom du recruteur</strong> si vous le connaissez, plutôt que « Madame, Monsieur ».</li>
  <li><strong>Le bon intitulé du poste</strong> et le bon nom d'entreprise : vérifiez deux fois.</li>
  <li><strong>Pas de copier-coller</strong> d'un modèle trouvé en ligne : les recruteurs les reconnaissent immédiatement.</li>
</ul>
<p>Une lettre réussie est courte, précise et adressée à <em>une</em> entreprise. Si elle pourrait être envoyée à n'importe qui, elle ne convaincra personne.</p>
"""),
 dict(slug="questions-entretien-frequentes", cat="Entretien", icon="mic", cover="c3",
      date="22 août 2026", iso="2026-08-22", read=7,
      title="Les 6 questions d'entretien les plus fréquentes (et comment y répondre)",
      excerpt="« Parlez-moi de vous », « Quels sont vos défauts ? »… Les questions qui reviennent dans presque tous les entretiens et les pièges à éviter.",
      body="""
<p>Chaque entretien est différent, mais certaines questions reviennent presque toujours. Bonne nouvelle : cela signifie que vous pouvez les préparer. Voici les six plus fréquentes et la manière d'y répondre.</p>

<h2>1. « Parlez-moi de vous. »</h2>
<p>Ce n'est pas une invitation à raconter votre vie depuis l'école primaire. Le recruteur attend un résumé professionnel de <strong>une à deux minutes</strong>. Utilisez la structure présent, passé, futur :</p>
<ul>
  <li><strong>Présent :</strong> qui vous êtes professionnellement aujourd'hui ;</li>
  <li><strong>Passé :</strong> deux ou trois expériences ou réalisations marquantes ;</li>
  <li><strong>Futur :</strong> pourquoi ce poste est la suite logique de votre parcours.</li>
</ul>

<h2>2. « Pourquoi voulez-vous travailler chez nous ? »</h2>
<p>La pire réponse : « Parce que c'est une grande entreprise. » Renseignez-vous avant l'entretien : site web, page LinkedIn, actualités récentes. Citez un élément précis qui vous attire et reliez-le à vos compétences.</p>

<h2>3. « Quels sont vos défauts ? »</h2>
<p>Évitez les faux défauts (« je suis trop perfectionniste ») que tous les recruteurs ont déjà entendus. Choisissez un vrai point d'amélioration, qui n'est pas central pour le poste, et montrez ce que vous faites pour progresser.</p>
<blockquote>« J'ai longtemps eu du mal à déléguer. Depuis un an, je planifie la répartition des tâches en début de semaine avec mon équipe, ce qui m'oblige à faire confiance et nous fait gagner du temps. »</blockquote>

<h2>4. « Racontez-nous une situation difficile que vous avez gérée. »</h2>
<p>Utilisez la méthode <strong>STAR</strong> :</p>
<ul>
  <li><strong>S</strong>ituation : le contexte, en une ou deux phrases ;</li>
  <li><strong>T</strong>âche : ce que vous deviez accomplir ;</li>
  <li><strong>A</strong>ction : ce que <em>vous</em> avez fait concrètement ;</li>
  <li><strong>R</strong>ésultat : ce qui a changé grâce à votre action, chiffré si possible.</li>
</ul>

<h2>5. « Où vous voyez-vous dans cinq ans ? »</h2>
<p>Le recruteur veut vérifier que votre projet est cohérent avec le poste et que vous ne partirez pas au bout de six mois. Montrez de l'ambition, mais une ambition qui peut se construire dans l'entreprise.</p>

<h2>6. « Avez-vous des questions ? »</h2>
<p>Ne répondez jamais « non ». Préparez deux ou trois questions qui montrent votre intérêt pour le poste :</p>
<ul>
  <li>« À quoi ressemblerait une journée type dans ce poste ? »</li>
  <li>« Quels sont les principaux défis de l'équipe pour les prochains mois ? »</li>
  <li>« Comment sera évaluée la réussite dans ce poste au bout d'un an ? »</li>
</ul>

<p>La clé n'est pas d'apprendre des réponses par cœur, mais de savoir quelles histoires de votre parcours vous allez raconter. Entraînez-vous à voix haute, idéalement devant quelqu'un qui peut vous faire un retour honnête.</p>
"""),
 dict(slug="ce-que-font-les-candidats-retenus", cat="Conseils", icon="target", cover="c4",
      date="19 juillet 2026", iso="2026-07-19", read=5,
      title="4 choses que les candidats retenus font différemment (+1 bonus)",
      excerpt="Ce n'est pas toujours le plus diplômé qui décroche le poste, c'est celui qui se présente le mieux. Voici ce que font différemment ceux qui réussissent.",
      body="""
<p><strong>Ce n'est pas toujours le plus diplômé qui décroche le poste. C'est celui qui se présente le mieux.</strong></p>
<p>Chaque année, des centaines de candidats qualifiés passent à côté d'opportunités qu'ils méritaient. Pas par manque de compétences, mais par manque de méthode. Voici ce que font différemment ceux qui obtiennent le poste.</p>

<h2>1. Ils adaptent leur CV à chaque offre</h2>
<p>Envoyer le même CV à toutes les entreprises est l'erreur la plus répandue. Chaque candidature est une nouvelle opportunité et doit être traitée comme telle : les mots-clés, les expériences mises en avant, la formulation même du profil doivent coller à l'offre visée. Un CV générique ne convainc personne : il donne simplement l'impression d'une candidature envoyée en masse.</p>

<h2>2. Ils mettent en avant des résultats, pas des tâches</h2>
<div class="compare">
  <div class="bad"><b>À éviter</b>Gestion de la clientèle.</div>
  <div class="good"><b>À préférer</b>Suivi de 200 clients avec 95 % de satisfaction.</div>
</div>
<p>Les recruteurs ne veulent pas savoir ce que vous avez fait au quotidien, ils veulent voir ce que vous avez accompli. Chaque ligne de votre CV devrait répondre à la question : <em>et alors ?</em></p>

<h2>3. Leur CV tient sur une page (deux au maximum)</h2>
<p>Un recruteur passe très peu de temps sur un premier passage de CV. S'il est dense, illisible ou trop long, il passe directement au suivant. La règle est simple : une page, claire, aérée, percutante. Tout ce qui n'apporte pas de valeur immédiate doit être coupé.</p>

<h2>4. Ils se préparent avant l'entretien</h2>
<p>Décrocher l'entretien, c'est bien. Le réussir, c'est mieux. Les candidats retenus arrivent préparés : ils connaissent l'entreprise, anticipent les questions difficiles et maîtrisent leur discours. L'improvisation se voit toujours, et rarement en bien.</p>

<h2>Bonus : ils sont présents sur LinkedIn</h2>
<p>Un profil LinkedIn actif et bien construit donne immédiatement plus de crédibilité à une candidature. C'est souvent la première chose qu'un recruteur consulte après avoir reçu un CV.</p>

<blockquote>La bonne nouvelle, c'est que tout cela s'apprend et se prépare. C'est exactement ce que fait Amploi : nous analysons votre dossier et vous disons précisément quoi améliorer.</blockquote>
"""),
 dict(slug="negocier-son-salaire", cat="Entretien", icon="coins", cover="c5",
      date="8 juillet 2026", iso="2026-07-08", read=5,
      title="Comment négocier son salaire lors d'un entretien ?",
      excerpt="Conseils pratiques et arguments clés pour aborder la question de la rémunération avec assurance, sans braquer le recruteur.",
      body="""
<p>Parler d'argent en entretien met beaucoup de candidats mal à l'aise. Par peur de paraître trop exigeants, ils acceptent la première proposition, ou donnent un chiffre au hasard. Pourtant, la négociation salariale est une étape normale du recrutement, et les recruteurs s'y attendent.</p>

<h2>1. Renseignez-vous sur le marché</h2>
<p>Avant l'entretien, faites vos recherches : quelles sont les rémunérations pratiquées pour ce type de poste, dans ce secteur, à Conakry ou en région ? Interrogez des personnes de votre réseau qui occupent des postes similaires, consultez les offres qui affichent un salaire. Les écarts peuvent être importants entre une PME locale, une ONG internationale et une société minière.</p>

<h2>2. Définissez une fourchette, pas un chiffre</h2>
<p>Préparez trois montants :</p>
<ul>
  <li><strong>Votre minimum</strong>, en dessous duquel vous refuserez le poste ;</li>
  <li><strong>Votre objectif</strong>, réaliste au vu du marché et de votre profil ;</li>
  <li><strong>Votre fourchette haute</strong>, que vous annoncerez en premier.</li>
</ul>

<h2>3. Laissez venir la question</h2>
<p>Évitez d'aborder la rémunération dès le début de l'entretien. Laissez le recruteur poser la question, ou attendez la fin du processus, quand l'entreprise est convaincue de vouloir vous recruter. Votre pouvoir de négociation est alors bien plus fort.</p>

<h2>4. Justifiez par votre valeur</h2>
<p>Ne parlez pas de vos besoins personnels (loyer, transport, famille). Parlez de ce que vous apportez : vos compétences rares, vos résultats passés, ce que vous pourrez accomplir dès les premiers mois.</p>
<blockquote>« Compte tenu de mes quatre ans d'expérience en logistique minière et des résultats obtenus sur la réduction des délais de livraison, je vise une rémunération comprise entre X et Y. »</blockquote>

<h2>5. Pensez au-delà du salaire</h2>
<p>Si l'entreprise ne peut pas bouger sur le salaire de base, d'autres éléments peuvent se négocier : prime de transport ou de logement, assurance santé, formation, téléphone, date de révision salariale. Ce sont parfois ces avantages qui font la différence.</p>

<p>Une négociation réussie se termine avec deux parties satisfaites. Restez courtois, ferme sur votre minimum, et souvenez-vous qu'un recruteur respecte un candidat qui connaît sa valeur.</p>
"""),
 dict(slug="linkedin-secteur-minier", cat="LinkedIn", icon="linkedin", cover="c6",
      date="28 juin 2026", iso="2026-06-28", read=6,
      title="Optimiser son profil LinkedIn pour le secteur minier",
      excerpt="Les mots-clés et les sections indispensables pour vous faire repérer par les grandes compagnies minières à Boké, Kamsar et ailleurs en Guinée.",
      body="""
<p>Le secteur minier est l'un des premiers recruteurs de Guinée, et les grandes compagnies présentes dans la région de Boké, à Kamsar ou à Siguiri recrutent de plus en plus via LinkedIn. Leurs équipes RH et les cabinets de recrutement y recherchent directement des profils à l'aide de mots-clés. Si votre profil n'est pas optimisé, vous êtes tout simplement invisible.</p>

<h2>1. Soignez votre titre professionnel</h2>
<p>Le titre (sous votre nom) est l'élément le plus important pour être trouvé. « En recherche d'emploi » ou « Étudiant » ne disent rien. Utilisez un intitulé précis, avec vos spécialités.</p>
<div class="compare">
  <div class="bad"><b>À éviter</b>À la recherche de nouvelles opportunités</div>
  <div class="good"><b>À préférer</b>Technicien HSE | Sécurité industrielle &amp; environnement | Exploitation de bauxite</div>
</div>

<h2>2. Intégrez les bons mots-clés</h2>
<p>Les recruteurs du secteur cherchent des termes précis. Selon votre métier, intégrez-les dans votre titre, votre résumé et vos expériences :</p>
<ul>
  <li><strong>HSE / QHSE</strong>, sécurité industrielle, gestion des risques ;</li>
  <li><strong>Bauxite</strong>, or, fer, exploitation à ciel ouvert ;</li>
  <li><strong>Maintenance</strong> des engins miniers, mécanique, électricité industrielle ;</li>
  <li><strong>Logistique</strong>, supply chain, opérations portuaires ;</li>
  <li><strong>RSE</strong>, relations communautaires, environnement.</li>
</ul>

<h2>3. Rédigez un résumé orienté résultats</h2>
<p>La section « Infos » est votre argumentaire. En quatre à six lignes, présentez votre expertise, vos principales réalisations et ce que vous recherchez. Écrivez à la première personne, de façon directe.</p>

<h2>4. Valorisez vos certifications</h2>
<p>Dans le secteur minier, les certifications comptent beaucoup : formations sécurité, permis d'engins, premiers secours, normes ISO, habilitations électriques. Ajoutez-les dans la section « Licences et certifications » avec leurs dates.</p>

<h2>5. Ajoutez une photo et une bannière professionnelles</h2>
<p>Un profil avec photo est beaucoup plus consulté qu'un profil sans. Une photo nette, souriante, en tenue de travail ou en tenue professionnelle fait l'affaire.</p>

<h2>6. Soyez actif</h2>
<p>Suivez les pages des entreprises qui vous intéressent, réagissez à leurs publications, connectez-vous avec des professionnels du secteur. Un profil actif remonte plus souvent dans les recherches des recruteurs.</p>

<blockquote>Votre profil LinkedIn travaille pour vous 24 h/24. Prenez le temps de le soigner une fois : il vous fera gagner des mois de recherche.</blockquote>
"""),
]
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from new_posts import NEW_POSTS, NEW_ICONS
P.update(NEW_ICONS)
POSTS += NEW_POSTS
from long1 import LONG1
from long2 import LONG2
P.update({
 "alert": '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "grid": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>',
 "refresh": '<path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 12a9 9 0 0 1 15.5-6.2L21 8"/><path d="M21 3v5h-5M3 21v-5h5"/>',
})
POSTS += LONG1 + LONG2
from articles_hebdo import HEBDO
POSTS += HEBDO

import re, unicodedata
def slugify(t):
    t = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", "", t)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

for p in POSTS:
    text = re.sub(r"<[^>]+>", " ", p["body"])
    p["read"] = max(2, round(len(text.split()) / 220))
    heads = []
    def add_id(m):
        hid = slugify(m.group(1)); heads.append((hid, m.group(1)))
        return f'<h2 id="{hid}">{m.group(1)}</h2>'
    p["body"] = re.sub(r"<h2>(.*?)</h2>", add_id, p["body"])
    p["toc"] = ""
    if len(heads) >= 5:
        items = "".join(f'<li><a href="#{h}">{t}</a></li>' for h, t in heads)
        p["toc"] = f'<nav class="toc" aria-label="Sommaire"><p class="toc-title">Sommaire</p><ul>{items}</ul></nav>'
POSTS.sort(key=lambda p: p["iso"], reverse=True)

# ---------- Gabarits communs ----------
def head(title, desc, root, path="", og_type="website", jsonld=None):
    url = f"{SITE_URL}/{path}"
    ld = ""
    for block in (jsonld or []):
        ld += f'    <script type="application/ld+json">{json.dumps(block, ensure_ascii=False)}</script>\n'
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{url}">
    <meta name="theme-color" content="#1a56db">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="Amploi">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{SITE_URL}/og-image.png">
    <meta property="og:locale" content="fr_FR">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%231a56db'/%3E%3Ctext x='32' y='44' font-family='Arial' font-weight='800' font-size='34' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{root}styles.css">
{ld}</head>
<body>
"""

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "name": "Amploi", "url": SITE_URL + "/", "image": SITE_URL + "/og-image.png",
    "description": "Accompagnement carrière et recrutement en Guinée : CV, lettre de motivation, LinkedIn et coaching d'entretien.",
    "telephone": "+224620028813", "email": EMAIL,
    "address": {"@type": "PostalAddress", "addressLocality": "Conakry", "addressCountry": "GN"},
    "areaServed": {"@type": "Country", "name": "Guinée"},
    "priceRange": "39 000 - 159 000 GNF",
}

def header(root, active=""):
    home = f"{root}index.html" if root else "index.html"
    def nav(href, label, key):
        cls = ' class="is-active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    links = [
        nav(f"{home}#services", "Services", "services"),
        nav(f"{home}#tarifs", "Tarifs", "tarifs"),
        nav(f"{home}#offres", "Offres d'emploi", "offres"),
        nav(f"{home}#recruteurs", "Recruteurs", "recruteurs"),
        nav(f"{root}blog.html", "Blog", "blog"),
        nav(f"{home}#contact", "Contact", "contact"),
    ]
    return f"""
    <header class="site-header">
        <div class="container header-inner">
            <a href="{home}" class="logo" aria-label="{SITE}, accueil">
                <span class="logo-mark">A</span>
                <span class="logo-text">Amploi<span>.</span></span>
            </a>
            <nav class="main-nav" id="main-nav" aria-label="Navigation principale">
                {"".join(links)}
            </nav>
            <div class="header-cta">
                <a href="{wa("Bonjour Amploi, je souhaite faire analyser mon CV.")}" class="btn btn-primary" target="_blank" rel="noopener">Envoyer mon CV</a>
                <button class="menu-toggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="main-nav"><span></span></button>
            </div>
        </div>
    </header>
"""

def footer(root):
    home = f"{root}index.html" if root else "index.html"
    return f"""
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <a href="{home}" class="logo"><span class="logo-mark">A</span><span class="logo-text">Amploi<span>.</span></span></a>
                    <p>Accompagnement carrière et recrutement en République de Guinée. CV, lettres de motivation, LinkedIn, coaching d'entretien.</p>
                </div>
                <div>
                    <h4>Candidats</h4>
                    <ul>
                        <li><a href="{home}#services">Nos services</a></li>
                        <li><a href="{home}#tarifs">Tarifs</a></li>
                        <li><a href="{home}#offres">Offres d'emploi</a></li>
                        <li><a href="{home}#faq">Questions fréquentes</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Ressources</h4>
                    <ul>
                        <li><a href="{root}blog.html">Blog carrière</a></li>
                        <li><a href="{home}#recruteurs">Espace recruteurs</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="https://wa.me/{WA_NUM}" target="_blank" rel="noopener">WhatsApp : +224 620 02 88 13</a></li>
                        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                        <li>Conakry, Guinée</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© <span data-year>2026</span> Amploi. Tous droits réservés.</span>
                <span>Fait en Guinée 🇬🇳</span>
            </div>
        </div>
    </footer>

    <a href="{wa("Bonjour Amploi, j'ai une question.")}" class="wa-float" target="_blank" rel="noopener" aria-label="Nous écrire sur WhatsApp">{WA_SVG}</a>

    <script src="{root}main.js"></script>
</body>
</html>
"""

def post_card(p, root, reveal=True):
    return f"""
                <a href="{root}blog/{p['slug']}.html" class="card post-card{' reveal' if reveal else ''}" data-cat="{p['cat']}">
                    <div class="post-cover {p['cover']}">{ic(p['icon'], 1.6)}<span class="post-cat">{p['cat']}</span></div>
                    <div class="post-body">
                        <div class="post-meta"><time datetime="{p['iso']}">{p['date']}</time> · {p['read']} min de lecture</div>
                        <h3>{p['title']}</h3>
                        <p>{p['excerpt']}</p>
                        <span class="read-more">Lire l'article {ic('arrow')}</span>
                    </div>
                </a>"""

# ---------- Accueil ----------
PACKS = [
 dict(name="Essentiel", for_="Jeunes diplômés et premiers emplois", price="39 000", note="Livré en 72 h", featured=False,
      items=["CV stratégique entièrement réécrit", "Mise en page moderne et professionnelle", "Compatible avec les logiciels de tri (ATS)", "Fichiers Word et PDF", "1 révision gratuite"]),
 dict(name="Pro", for_="Profils confirmés en recherche active", price="79 000", note="Livré en 48 h", featured=True,
      items=["Tout le pack Essentiel", "Lettre de motivation personnalisée", "14 jours de révisions gratuites", "Accès à nos formations gratuites", "Profil prioritaire dans notre CVthèque"]),
 dict(name="Premium", for_="Cadres, managers et postes stratégiques", price="159 000", note="Livré en 48 h", featured=False,
      items=["Tout le pack Pro", "Optimisation complète du profil LinkedIn", "Séance de coaching et simulation d'entretien", "Conseils personnalisés de négociation salariale", "Suivi prioritaire sur WhatsApp"]),
]

def pack_html(p):
    items = "".join(f"<li>{ic('check', 2.5)}<span>{i}</span></li>" for i in p["items"])
    badge = '<span class="price-badge">Le plus choisi</span>' if p["featured"] else ""
    btn = "btn-white" if p["featured"] else "btn-outline"
    msg = f"Bonjour Amploi, je souhaite commander le pack {p['name']} ({p['price']} GNF)."
    return f"""
                <div class="price-card{' featured' if p['featured'] else ''} reveal">
                    {badge}
                    <h3>{p['name']}</h3>
                    <p class="price-for">{p['for_']}</p>
                    <div class="price">{p['price'].replace(' ', '&nbsp;')} <small>GNF</small></div>
                    <p class="price-note">Paiement unique · {p['note']}</p>
                    <ul class="price-list">{items}</ul>
                    <a href="{wa(msg)}" class="btn {btn} btn-block" target="_blank" rel="noopener">Choisir le pack {p['name']}</a>
                </div>"""

JOBS = [
 dict(title="Responsable des Ressources Humaines", company="Société minière", tags=["CDI", "Conakry"], date="Publiée récemment"),
 dict(title="Ingénieur Sécurité & Environnement (HSE)", company="Groupe industriel international", tags=["CDI", "Kamsar"], date="Publiée récemment"),
 dict(title="Chef de projet transformation digitale", company="Opérateur de télécommunications", tags=["Consultance", "Conakry"], date="Publiée récemment"),
]
def job_html(j):
    tags = "".join(f'<span class="tag{" alt" if k else ""}">{t}</span>' for k, t in enumerate(j["tags"]))
    msg = f"Bonjour Amploi, je suis intéressé(e) par l'offre « {j['title']} »."
    return f"""
                <article class="card job-card reveal">
                    <div class="job-tags">{tags}</div>
                    <h3>{j['title']}</h3>
                    <p class="job-company">{j['company']}</p>
                    <div class="job-foot">
                        <span>{j['date']}</span>
                        <a href="{wa(msg)}" target="_blank" rel="noopener">Postuler {ic('arrow')}</a>
                    </div>
                </article>"""

SERVICES = [
 ("file", "Rédaction et refonte de CV", "On réécrit votre CV de A à Z : contenu, structure et présentation, pour qu'il retienne l'attention et passe les filtres automatiques."),
 ("pen", "Lettres de motivation", "Une lettre personnalisée pour chaque poste visé, courte et précise, qui donne envie au recruteur de vous rencontrer."),
 ("linkedin", "Optimisation LinkedIn", "Titre, résumé, compétences, mots-clés : un profil pensé pour que les recruteurs vous trouvent en premier."),
 ("mic", "Coaching d'entretien", "Simulation d'entretien en personne ou en ligne, avec un retour concret pour être à l'aise le jour J."),
]

STEPS = [
 ("Envoyez votre CV", "Par WhatsApp ou par e-mail, avec l'offre ou le type de poste que vous visez."),
 ("Recevez un diagnostic gratuit", "Sous 24 h, un consultant vous indique les points bloquants de votre candidature."),
 ("Choisissez votre pack", "Essentiel, Pro ou Premium, selon votre profil et vos objectifs."),
 ("Postulez avec confiance", "Vous recevez vos documents finalisés et ajustés jusqu'à ce qu'ils vous conviennent."),
]

# Avis clients : uniquement de VRAIS avis, avec l'accord du client.
# Format : dict(nom="Mariama D.", poste="Assistante RH", ville="Conakry", pack="Pro", note=5,
#               texte="Ce que le client a écrit, sans le réécrire.")
# Tant que la liste est vide, la section n'apparaît pas sur le site.
AVIS = [
]

def avis_html():
    # Section masquée tant qu'aucun avis réel n'a été ajouté.
    if not AVIS:
        return ""
    cards = ""
    for a in AVIS:
        n = max(1, min(5, int(a.get("note", 5))))
        stars = "".join(f'<span class="{"on" if i < n else "off"}">{ic("star")}</span>' for i in range(5))
        initiales = "".join(w[0] for w in a["nom"].replace(".", "").split()[:2]).upper()
        meta = " · ".join(x for x in (a.get("poste"), a.get("ville")) if x)
        pack = f'<span class="tag">Pack {a["pack"]}</span>' if a.get("pack") else ""
        cards += f"""
                <figure class="card avis-card reveal">
                    <div class="avis-note" aria-label="{n} étoiles sur 5">{stars}</div>
                    <blockquote>«&nbsp;{a['texte']}&nbsp;»</blockquote>
                    <figcaption>
                        <span class="avis-avatar" aria-hidden="true">{initiales}</span>
                        <span><strong>{a['nom']}</strong><small>{meta}</small></span>
                        {pack}
                    </figcaption>
                </figure>"""
    return f"""
        <!-- AVIS -->
        <section id="avis" class="section">
            <div class="container">
                <div class="section-head center">
                    <span class="eyebrow">Avis clients</span>
                    <h2 class="section-title">Ils ont fait confiance à Amploi</h2>
                </div>
                <div class="grid grid-3">{cards}
                </div>
            </div>
        </section>
"""

FAQ = [
 ("Comment fonctionne le diagnostic gratuit de mon CV ?", "Envoyez-nous votre CV actuel sur WhatsApp ou par e-mail. Un consultant l'analyse sous 24 h et vous fait un retour clair sur les principaux points à améliorer. Ce diagnostic est gratuit et sans engagement."),
 ("Quels sont vos délais de livraison ?", "Comptez 72 h pour le pack Essentiel et 48 h pour les packs Pro et Premium, à partir de la validation de votre commande et de la réception de toutes vos informations."),
 ("Comment se passe le paiement ?", "Une fois votre pack choisi, nous vous communiquons les modalités de paiement sur WhatsApp. Le travail commence dès réception du paiement."),
 ("Et si le résultat ne me convient pas ?", "Chaque pack inclut des révisions : une pour le pack Essentiel, et des révisions illimitées pendant 14 jours pour les packs Pro et Premium. Nous ajustons les documents jusqu'à ce qu'ils vous ressemblent."),
 ("Garantissez-vous que je vais trouver un emploi ?", "Personne ne peut honnêtement garantir une embauche. En revanche, nous mettons toutes les chances de votre côté : des documents qui passent le premier tri, un profil visible et une vraie préparation à l'entretien."),
 ("Je vis à l'étranger ou hors de Conakry. Puis-je faire appel à vous ?", "Oui. Tout se fait à distance, par WhatsApp et par e-mail, y compris le coaching d'entretien en visio."),
]

def build_index():
    services = "".join(f"""
                <article class="card reveal">
                    <div class="icon-box">{ic(i)}</div>
                    <h3>{t}</h3>
                    <p>{d}</p>
                </article>""" for i, t, d in SERVICES)
    steps = "".join(f"""
                <div class="step reveal">
                    <h3>{t}</h3>
                    <p>{d}</p>
                </div>""" for t, d in STEPS)
    faq = "".join(f"""
                <details>
                    <summary>{q}</summary>
                    <p>{a}</p>
                </details>""" for q, a in FAQ)
    posts = "".join(post_card(p, "") for p in POSTS[:3])

    html = head("Amploi | CV, coaching carrière et recrutement en Guinée",
                "Amploi aide les talents guinéens à décrocher le poste qu'ils méritent : CV professionnel, lettre de motivation, LinkedIn et coaching d'entretien. Packs dès 39 000 GNF.", "", "",
                jsonld=[ORG, {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}])
    html += header("", "")
    html += f"""
    <main>
        <!-- HERO -->
        <section class="hero">
            <div class="container hero-grid">
                <div>
                    <span class="hero-badge"><b>Gratuit</b> Diagnostic de votre CV sous 24 h</span>
                    <h1>Décrochez l'entretien <em>que vous méritez.</em></h1>
                    <p class="hero-lead">Amploi transforme votre CV, votre lettre et votre profil LinkedIn en outils qui convainquent les recruteurs, en Guinée comme à l'international.</p>
                    <div class="hero-actions">
                        <a href="#tarifs" class="btn btn-primary btn-lg">Voir les packs {ic('arrow')}</a>
                        <a href="{wa("Bonjour Amploi, je souhaite un diagnostic gratuit de mon CV.")}" class="btn btn-outline btn-lg" target="_blank" rel="noopener">Diagnostic gratuit</a>
                    </div>
                    <div class="hero-proof">
                        <div><strong data-count="250" data-prefix="+">+250</strong><span>candidats accompagnés</span></div>
                        <div><strong data-count="25" data-prefix="+">+25</strong><span>entreprises partenaires</span></div>
                        <div><strong>48 h</strong><span>délai de livraison</span></div>
                    </div>
                </div>

                <div class="hero-visual" aria-hidden="true">
                    <div class="float-chip chip-1"><span class="dot">{ic('doc-search')}</span><div>CV analysé<small>Retour sous 24 h</small></div></div>
                    <div class="cv-card">
                        <div class="cv-head">
                            <div class="cv-avatar"></div>
                            <div><div class="cv-name">Mariama Diallo</div><div class="cv-role">Responsable logistique</div></div>
                        </div>
                        <div class="cv-line w90"></div>
                        <div class="cv-line w80"></div>
                        <div class="cv-line w60"></div>
                        <div class="cv-label">Expérience</div>
                        <div class="cv-line blue w90"></div>
                        <div class="cv-line w80"></div>
                        <div class="cv-line w40"></div>
                        <div class="cv-label">Compétences</div>
                        <div class="cv-tags"><span>Supply chain</span><span>HSE</span><span>SAP</span><span>Leadership</span></div>
                    </div>
                    <div class="float-chip chip-2"><span class="dot">{ic('check', 2.5)}</span><div>Entretien obtenu<small>Kamsar · CDI</small></div></div>
                </div>
            </div>
        </section>

        <div class="trust">
            <div class="container trust-inner">
                <span>{ic('shield')} Diagnostic gratuit et sans engagement</span>
                <span>{ic('clock')} Livraison en 48 à 72 h</span>
                <span>{ic('pin')} Conakry et toute la Guinée</span>
                <span>{ic('chat')} Suivi sur WhatsApp</span>
            </div>
        </div>

        <!-- SERVICES -->
        <section id="services" class="section">
            <div class="container">
                <div class="section-head center">
                    <span class="eyebrow">Nos services</span>
                    <h2 class="section-title">Tout ce qu'il faut pour être recruté</h2>
                    <p class="section-lead">Jeune diplômé ou cadre expérimenté, nous renforçons chaque étape de votre candidature.</p>
                </div>
                <div class="grid grid-4">{services}
                </div>
            </div>
        </section>

        <!-- ÉTAPES -->
        <section class="section section-tint">
            <div class="container">
                <div class="section-head center">
                    <span class="eyebrow">Comment ça marche</span>
                    <h2 class="section-title">Simple, rapide, 100 % à distance</h2>
                </div>
                <div class="grid grid-4 steps">{steps}
                </div>
            </div>
        </section>

{avis_html()}
        <!-- TARIFS -->
        <section id="tarifs" class="section">
            <div class="container">
                <div class="section-head center">
                    <span class="eyebrow">Tarifs</span>
                    <h2 class="section-title">Investissez dans votre carrière</h2>
                    <p class="section-lead">Trois formules claires, sans frais cachés. Payez une fois, postulez en toute confiance.</p>
                </div>
                <div class="grid grid-3 pricing">{"".join(pack_html(p) for p in PACKS)}
                </div>
                <p class="pricing-foot">Vous hésitez ? <a href="{wa("Bonjour Amploi, j'hésite entre vos packs. Pouvez-vous me conseiller ?")}" target="_blank" rel="noopener">Demandez-nous conseil sur WhatsApp</a>.</p>
            </div>
        </section>

        <!-- OFFRES -->
        <section id="offres" class="section section-tint">
            <div class="container">
                <div class="section-head">
                    <span class="eyebrow">Offres d'emploi</span>
                    <h2 class="section-title">Dernières opportunités en Guinée</h2>
                    <p class="section-lead">Des postes confiés par nos entreprises partenaires. Postulez directement via Amploi.</p>
                </div>
                <div class="grid grid-3">{"".join(job_html(j) for j in JOBS)}
                </div>
                <div class="center-cta">
                    <a href="{wa("Bonjour Amploi, je souhaite recevoir les nouvelles offres d'emploi.")}" class="btn btn-outline" target="_blank" rel="noopener">Recevoir les offres sur WhatsApp</a>
                </div>
            </div>
        </section>

        <!-- RECRUTEURS -->
        <section id="recruteurs" class="section">
            <div class="container">
                <div class="recruit reveal">
                    <div>
                        <span class="eyebrow">Entreprises</span>
                        <h2>Vous recrutez en Guinée ?</h2>
                        <p>Gagnez du temps : nous présélectionnons pour vous des candidats aux dossiers vérifiés, prêts pour l'entretien.</p>
                        <div class="recruit-actions">
                            <a href="{wa("Bonjour Amploi, nous souhaitons vous confier un recrutement.")}" class="btn btn-white" target="_blank" rel="noopener">Confier un recrutement</a>
                            <a href="mailto:{EMAIL}?subject=Demande%20d%27acc%C3%A8s%20%C3%A0%20la%20CVth%C3%A8que" class="btn btn-ghost-white">Accéder à la CVthèque</a>
                        </div>
                    </div>
                    <ul class="recruit-list">
                        <li>{ic('users')}<span>CVthèque de candidats accompagnés et vérifiés</span></li>
                        <li>{ic('search')}<span>Présélection des profils selon vos critères</span></li>
                        <li>{ic('briefcase')}<span>Diffusion de vos offres auprès de notre réseau</span></li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- BLOG -->
        <section id="blog" class="section section-tint">
            <div class="container">
                <div class="section-head">
                    <span class="eyebrow">Blog carrière</span>
                    <h2 class="section-title">Nos derniers conseils</h2>
                    <p class="section-lead">Des conseils concrets pour améliorer vos candidatures et réussir vos entretiens.</p>
                </div>
                <div class="grid grid-3">{posts}
                </div>
                <div class="center-cta"><a href="blog.html" class="btn btn-outline">Voir tous les articles {ic('arrow')}</a></div>
            </div>
        </section>

        <!-- FAQ -->
        <section id="faq" class="section">
            <div class="container narrow">
                <div class="section-head center">
                    <span class="eyebrow">FAQ</span>
                    <h2 class="section-title">Questions fréquentes</h2>
                </div>
                <div class="faq">{faq}
                </div>
            </div>
        </section>

        <!-- CONTACT -->
        <section id="contact" class="section section-tint">
            <div class="container contact-grid">
                <div>
                    <span class="eyebrow">Contact</span>
                    <h2 class="section-title">Parlons de votre prochain poste</h2>
                    <p class="section-lead">Pas de formulaire compliqué : écrivez-nous directement, on vous répond rapidement.</p>
                    <div class="contact-cards">
                        <a href="https://wa.me/{WA_NUM}" class="card contact-card" target="_blank" rel="noopener">
                            <div class="icon-box">{ic('chat')}</div>
                            <div><h3>WhatsApp</h3><p>+224 620 02 88 13</p></div>
                        </a>
                        <a href="mailto:{EMAIL}" class="card contact-card">
                            <div class="icon-box">{ic('mail')}</div>
                            <div><h3>E-mail</h3><p>{EMAIL}</p></div>
                        </a>
                    </div>
                </div>
                <div class="contact-panel">
                    <h3>Pour un diagnostic gratuit, envoyez-nous :</h3>
                    <ol>
                        <li>Votre CV actuel (PDF, Word ou photo)</li>
                        <li>Le poste ou le secteur que vous visez</li>
                        <li>L'offre d'emploi, si vous en avez une</li>
                    </ol>
                    <a href="{wa("Bonjour Amploi, je vous envoie mon CV pour un diagnostic gratuit.")}" class="btn btn-primary btn-block" target="_blank" rel="noopener">Envoyer mon CV sur WhatsApp</a>
                </div>
            </div>
        </section>
    </main>
"""
    html += footer("")
    open(f"{OUT}/index.html", "w").write(html)

def build_blog():
    cats = []
    for p in POSTS:
        if p["cat"] not in cats: cats.append(p["cat"])
    filters = '<button class="filter is-active" data-filter="all">Tous</button>' + "".join(
        f'<button class="filter" data-filter="{c}">{c}</button>' for c in cats)
    html = head("Blog carrière | Amploi", "Conseils pratiques pour réussir votre CV, votre lettre de motivation, votre profil LinkedIn et vos entretiens d'embauche en Guinée.", "", "blog.html")
    html += header("", "blog")
    html += f"""
    <main>
        <section class="blog-hero">
            <div class="container">
                <span class="eyebrow">Blog carrière</span>
                <h1>Conseils pour décrocher le bon poste</h1>
                <p class="section-lead">CV, lettre de motivation, LinkedIn, entretien : des articles pratiques, pensés pour le marché de l'emploi guinéen.</p>
                <div class="filters" role="group" aria-label="Filtrer par catégorie">{filters}</div>
            </div>
        </section>
        <section class="section" style="padding-top:40px">
            <div class="container">
                <div class="grid grid-3" id="post-list">{"".join(post_card(p, "") for p in POSTS)}
                </div>
            </div>
        </section>
    </main>
"""
    html += footer("")
    open(f"{OUT}/blog.html", "w").write(html)

def build_posts():
    os.makedirs(f"{OUT}/blog", exist_ok=True)
    for p in POSTS:
        related = [q for q in POSTS if q is not p and q["cat"] == p["cat"]]
        related += [q for q in POSTS if q is not p and q not in related]
        url = f"{SITE_URL}/blog/{p['slug']}.html"
        html = head(f"{p['title']} | Blog Amploi", p["excerpt"], "../", f"blog/{p['slug']}.html", "article", [
            {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["excerpt"],
             "datePublished": p["iso"], "dateModified": p["iso"], "inLanguage": "fr", "mainEntityOfPage": url,
             "image": SITE_URL + "/og-image.png",
             "author": {"@type": "Organization", "name": "Amploi", "url": SITE_URL + "/"},
             "publisher": {"@type": "Organization", "name": "Amploi", "url": SITE_URL + "/"}},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE_URL + "/blog.html"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}])
        html += header("../", "blog")
        html += f"""
    <main>
        <article>
            <header class="article-head">
                <div class="container narrow">
                    <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="../index.html">Accueil</a> / <a href="../blog.html">Blog</a> / {p['cat']}</nav>
                    <h1>{p['title']}</h1>
                    <div class="article-meta">
                        <span class="tag">{p['cat']}</span>
                        <time datetime="{p['iso']}">{p['date']}</time>
                        <span>{p['read']} min de lecture</span>
                    </div>
                </div>
            </header>
            <div class="container narrow">
                <div class="post-cover article-cover {p['cover']}" aria-hidden="true">{ic(p['icon'], 1.6)}</div>
                {p['toc']}<div class="prose">{p['body']}</div>

                <div class="share" data-title="{p['title']}">
                    <span class="share-label">Partager :</span>
                    <a href="#" data-share="whatsapp" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
                    <a href="#" data-share="linkedin" target="_blank" rel="noopener">{ic('linkedin')} LinkedIn</a>
                    <a href="#" data-share="facebook" target="_blank" rel="noopener">{ic('facebook')} Facebook</a>
                    <button type="button" data-share="copy">{ic('link')} <span>Copier le lien</span></button>
                </div>

                <aside class="cta-box">
                    <h2>Envie d'un avis sur votre CV ?</h2>
                    <p>Envoyez-le-nous : un consultant Amploi vous fait un diagnostic gratuit sous 24 h.</p>
                    <div class="btns">
                        <a href="{wa("Bonjour Amploi, je viens de lire « " + p['title'] + " » et je souhaite un diagnostic gratuit de mon CV.")}" class="btn btn-white" target="_blank" rel="noopener">Diagnostic gratuit</a>
                        <a href="../index.html#tarifs" class="btn btn-ghost-white">Voir les packs</a>
                    </div>
                </aside>
            </div>
        </article>

        <section class="section section-tint">
            <div class="container">
                <div class="section-head"><h2 class="section-title">À lire aussi</h2></div>
                <div class="grid grid-3">{"".join(post_card(q, "../") for q in related[:3])}
                </div>
            </div>
        </section>
    </main>
"""
        html += footer("../")
        open(f"{OUT}/blog/{p['slug']}.html", "w").write(html)

def build_seo():
    urls = [("", POSTS[0]["iso"], "1.0"), ("blog.html", POSTS[0]["iso"], "0.8")]
    urls += [(f"blog/{p['slug']}.html", p["iso"], "0.7") for p in POSTS]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path, mod, prio in urls:
        xml += f"  <url><loc>{SITE_URL}/{path}</loc><lastmod>{mod}</lastmod><priority>{prio}</priority></url>\n"
    xml += "</urlset>\n"
    open(f"{OUT}/sitemap.xml", "w").write(xml)
    open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

build_index(); build_blog(); build_posts(); build_seo()
print("ok", len(POSTS))
