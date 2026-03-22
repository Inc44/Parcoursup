## ⛔ Contraintes d'intégrité

### Rappel du schéma (synthèse fonctionnelle)

- Si une formation existe, alors elle est identifiée par `cod_aff_form`, qui pointe vers un établissement identifié par `cod_uai`, lui-même rattaché à un département `dep`, une académie, une région.
- Si une ligne de la table « indicateurs par session et formation » existe, alors elle est identifiée par `(session, cod_aff_form)` et décrit des volumes de vœux, de capacités et d'admissions pour cette formation et cette session.

---

### Contraintes d'existence (statiques)

1. Si un département `dep` existe dans la table département, alors il doit apparaître dans les enregistrements d'établissement qui y sont rattachés (`dep` de la table établissement ∈ table département).
2. Si un établissement existe (`cod_uai` dans la table établissement), alors sa clé `cod_uai` doit être non nulle, unique et référencée par au moins une formation ou zéro selon le modèle (clé primaire + clé étrangère dans la table formation).
3. Si une formation existe (`cod_aff_form` dans la table formation), alors sa clé `cod_aff_form` doit être non nulle, unique, et référencée dans la table des indicateurs par session (`session, cod_aff_form`) ou non selon les sessions.
4. Si une ligne d'indicateurs existe pour une formation et une session, alors `(session, cod_aff_form)` est une clé primaire non nulle et unique dans la table des indicateurs.

---

### Contraintes de référence (intégrité référentielle)

5. Si un établissement référence un département (`dep`), alors cette valeur `dep` doit exister dans la table département.
6. Si une formation référence un établissement (`cod_uai`), alors cette valeur `cod_uai` doit exister dans la table établissement.
7. Si une formation référence une composante (`composante_id_paysage`) ou un établissement paysage (`etablissement_id_paysage`), alors ces identifiants doivent exister dans les tables paysage correspondantes.
8. Si la table indicateurs contient un tuple `(session, cod_aff_form)`, alors `cod_aff_form` doit exister dans la table formation et `session` doit appartenir au domaine des sessions autorisées (liste finie de millésimes).

---

### Contraintes de domaine / valeurs (statiques)

9. Si un attribut numérique décrit un effectif ou un nombre de vœux/admissions (`capa_fin, voe_tot, acc_tot, nb_voe_pp, nb_cla_pp`, etc.), alors sa valeur doit être entière et ≥ 0.
10. Si un attribut décrit une capacité d'accueil `capa_fin`, alors `capa_fin` est entière, ≥ 0, et compatible avec la nature de la formation (par exemple pas de capacité pour des formations supprimées).
11. Si un attribut est un pourcentage (`pct_*`, `taux_acces_ens`, `part_acces_gen`, `part_acces_tec`, `part_acces_pro`), alors sa valeur doit être comprise dans [0, 100].
12. Si un attribut est une coordonnée géographique (`geolocalisation_des_formations_lat`, `geolocalisation_des_formations_lon`), alors la latitude est dans [-90, 90] et la longitude dans [-180, 180].
13. Si un attribut joue le rôle de code de tri, de rang, ou d'ordre (`tri`, `ran_grp1`, `ran_grp2`, `ran_grp3`), alors sa valeur doit être entière, ≥ 1, et cohérente avec le nombre de groupes ou de modalités.
14. Si un attribut code un type ou une filière (`fili`, `lib_grp1..3`, `lib_for_voe_ins`, `fil_lib_voe_acc`), alors sa valeur doit appartenir à un domaine énuméré de valeurs autorisées (liste officielle des filières et catégories).
15. Si un attribut « lien » est renseigné (`lien_form_psup`), alors il doit respecter la forme d'une URL valide.

---

### Contraintes d'agrégation locales (statiques)

16. Si une ligne contient `voe_tot` et ses déclinaisons par bac ou par sexe (`voe_tot_f`, `prop_tot_bg`, `prop_tot_bt`, `prop_tot_bp`, etc.), alors la somme de ces sous-effectifs ne doit pas dépasser `voe_tot` et doit en général l'atteindre modulo arrondis éventuels.
17. Si une ligne contient `acc_tot` et ses sous-découpages (`acc_bg, acc_bt, acc_bp, acc_at`), alors la somme des sous-découpages ne doit pas dépasser `acc_tot`.
18. Si une ligne contient la décomposition par mentions (`acc_mention_nonrenseignee, acc_sansmention, acc_ab, acc_b, acc_tb, acc_tbf`), alors la somme de ces valeurs doit être égale à `acc_neobac` ou `acc_tot` selon la définition choisie.
19. Si des attributs de type « part » (`part_acces_gen, part_acces_tec, part_acces_pro`) sont définis, alors leur somme doit être égale à 100 (ou 1 si stockés en proportions) au plus près des arrondis.
20. Si des pourcentages sont dérivés d'effectifs (`pct_bours` à partir de `acc_brs`, `pct_f` à partir de `acc_tot_f`), alors chaque pourcentage doit être égal au rapport des effectifs correspondants sur la base de référence, dans les tolérances d'arrondi.

---

### Contraintes entre capacité, vœux et admissions (statiques)

21. Si une formation a une capacité `capa_fin`, alors le nombre d'admissions finales `acc_tot` ne doit pas dépasser `capa_fin` sauf cas explicitement prévus (débordement contrôlé, redoublants non comptés dans `capa_fin`, etc.).
22. Si une formation a un nombre total de vœux `voe_tot`, alors le nombre de candidats classés (`nb_cla_pp + nb_cla_pc`) ne doit pas dépasser `voe_tot`.
23. Si une formation a `acc_tot` admis, alors `acc_tot` ne peut pas dépasser le nombre de candidats classés (`nb_cla_pp + nb_cla_pc`) ni le nombre total de vœux `voe_tot`.
24. Si une formation a un taux d'accès (`taux_acces_ens` ou équivalent) défini, alors ce taux doit être compatible avec le rang du dernier appelé et le nombre de candidats ayant validé un vœu, selon la formule officielle de Parcoursup.

---

### Contraintes de cohérence profil / proportions (statiques)

25. Si un pourcentage de boursiers `pct_bours` est stocké, alors il doit être cohérent avec le nombre `acc_brs` d'admis boursiers et la base d'effectifs utilisée (généralement `acc_tot` ou `acc_neobac`).
26. Si des pourcentages par type de bac (`pct_bg, pct_bt, pct_bp`) sont stockés, alors la répartition des effectifs correspondants doit refléter ces pourcentages à l'arrondi près.
27. Si des pourcentages par mention (`pct_ab, pct_b, pct_tb, pct_tbf, pct_sansmention, pct_mention_nonrenseignee`) sont stockés, alors la somme de ces pourcentages doit être 100 (± arrondi) et leurs produits par l'effectif de base doivent approcher les effectifs `acc_*` correspondants.

---

### Contraintes sur groupes et rangs (statiques)

28. Si des groupes d'appelés sont utilisés (`lib_grp1..3, ran_grp1..3`), alors chaque rang de groupe doit être compris entre 1 et le nombre total de classés pertinents, et `ran_grp1 ≤ ran_grp2 ≤ ran_grp3`.
29. Si `list_com` identifie une liste commune, alors les rangs d'appel et les nombres de classés doivent être cohérents au niveau de l'ensemble de la liste, pas uniquement de chaque formation isolée.

---

### Contraintes dynamiques sur insertion / mise à jour

30. Si une nouvelle formation est insérée, alors `cod_aff_form` doit être nouveau, `cod_uai` doit déjà exister dans la table établissement, et les coordonnées géographiques doivent être valides.
31. Si la capacité d'une formation (`capa_fin`) est modifiée, alors après mise à jour, on doit conserver `acc_tot ≤ capa_fin` pour la session concernée.
32. Si un établissement change de département (`dep` modifié), alors toutes les formations rattachées à cet établissement voient implicitement leur département logique changer, et aucune formation ne doit rester rattachée à un département inexistant.
33. Si un code de formation (`cod_aff_form`) est modifié, alors toutes les lignes d'indicateurs référant ce code doivent être mises à jour de manière atomique pour préserver l'intégrité référentielle.
34. Si des effectifs ou des pourcentages sont recalculés suite à un changement d'état (ajout/suppression d'admis, correction d'un effectif de boursiers, etc.), alors toutes les contraintes d'agrégation et de pourcentage ci-dessus doivent rester vérifiées après la mise à jour.

---

### Contraintes dynamiques sur suppression

35. Si un établissement est supprimé, alors aucune formation ne doit référencer encore son `cod_uai` (suppression en cascade, interdiction de suppression, ou mise à jour à NULL selon la politique choisie).
36. Si une formation est supprimée, alors aucune ligne d'indicateurs ne doit conserver son `cod_aff_form` (même logique : cascade, interdiction ou mise à NULL).
37. Si une session est supprimée ou close au niveau des indicateurs, alors aucune mise à jour ne doit être autorisée sur les tuples de cette session (verrouillage logique des données historiques).

---

### Contraintes logiques métier (statiques ou dynamiques)

38. Si une formation est marquée comme non sélective, alors le mécanisme d'admission (rangs, listes d'attente, groupes d'appelés) doit respecter les règles de droit commun des licences non sélectives, ce qui limite certaines combinaisons de valeurs (`ran_grp*`, `taux_acces_ens`).
39. Si un candidat est compté dans `acc_neobac`, alors il doit aussi être compté dans `acc_tot`, et les effectifs `acc_neobac` ne doivent pas dépasser `acc_tot`.
40. Si une formation n'accueille pas de profil donné (par exemple aucun bac pro), alors tous les effectifs et pourcentages associés à ce profil doivent être nuls pour cette ligne.

---

### Types de contraintes SQL utilisables (méta-niveau)

41. Si une contrainte porte sur un seul attribut (non nullité, domaine, bornes), alors elle peut être exprimée par `NOT NULL`, `CHECK` ou `DEFAULT` au niveau de la colonne.
42. Si une contrainte porte sur une combinaison d'attributs d'une même table (somme, comparaison, intervalles), alors elle peut être exprimée par une contrainte `CHECK` de table.
43. Si une contrainte porte sur la relation entre plusieurs tables ou sur des conditions avant/après modification, alors elle peut être exprimée par une clé étrangère, un déclencheur (trigger) ou une assertion globale.