# Parcoursup

![Stars](https://img.shields.io/github/stars/Inc44/Parcoursup?style=social)
![Forks](https://img.shields.io/github/forks/Inc44/Parcoursup?style=social)
![Watchers](https://img.shields.io/github/watchers/Inc44/Parcoursup?style=social)
![Repo Size](https://img.shields.io/github/repo-size/Inc44/Parcoursup)
![Language Count](https://img.shields.io/github/languages/count/Inc44/Parcoursup)
![Top Language](https://img.shields.io/github/languages/top/Inc44/Parcoursup)
[![Issues](https://img.shields.io/github/issues/Inc44/Parcoursup)](https://github.com/Inc44/Parcoursup/issues?q=is%3Aopen+is%3Aissue)
![Last Commit](https://img.shields.io/github/last-commit/Inc44/Parcoursup?color=red)
[![Release](https://img.shields.io/github/release/Inc44/Parcoursup.svg)](https://github.com/Inc44/Parcoursup/releases)
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/Inc44)

## 🎯 Objectif de la base de données

L'objectif principal de cette base de données est de récupérer et d'analyser toutes les informations liées à l'orientation et aux admissions des élèves dans l'enseignement supérieur via la plateforme Parcoursup. Elle permet de suivre de bout en bout le processus d'affectation, depuis le moment où les candidats formulent leurs vœux jusqu'à leur acceptation finale dans les différentes formations. On y retrouve tous les détails sur les établissements, leurs capacités d'accueil, et surtout le profil précis des postulants, par exemple s'ils sont boursiers, leur type de baccalauréat ou encore les mentions qu'ils ont obtenues. Grâce à toutes ces informations, le but est de pouvoir observer la sélectivité de chaque filière, d'étudier les taux d'accès selon les différentes phases d'admission principale ou complémentaire, et de comprendre comment se répartissent les futurs étudiants selon leur origine académique et géographique. Cela donne donc une vision globale pour analyser efficacement les critères d'intégration post-bac sans perdre la trace des spécificités de chaque candidature.

## 🔑 Modèle relationnel correspondant

parcoursup (<u>**session**</u>, <u>**cod_uai**</u>, <u>**cod_aff_form**</u>, contrat_etab, g_ea_lib_vx, dep, dep_lib, region_etab_aff, academies, ville_etab, lib_for_voe_ins, select_form, fili, lib_comp_voe_ins, form_lib_voe_acc, fil_lib_voe_acc, detail_forma, geolocalisation_des_formations_lon, geolocalisation_des_formations_lat, capa_fin, voe_tot, voe_tot_f, nb_voe_pp, nb_voe_pp_internat, nb_voe_pp_bg, nb_voe_pp_bg_brs, nb_voe_pp_bt, nb_voe_pp_bt_brs, nb_voe_pp_bp, nb_voe_pp_bp_brs, nb_voe_pp_at, nb_voe_pc, nb_voe_pc_bg, nb_voe_pc_bt, nb_voe_pc_bp, nb_voe_pc_at, nb_cla_pp, nb_cla_pc, nb_cla_pp_internat, nb_cla_pp_pasinternat, nb_cla_pp_bg, nb_cla_pp_bg_brs, nb_cla_pp_bt, nb_cla_pp_bt_brs, nb_cla_pp_bp, nb_cla_pp_bp_brs, nb_cla_pp_at, prop_tot, acc_tot, acc_tot_f, acc_pp, acc_pc, acc_debutpp, acc_datebac, acc_finpp, acc_internat, acc_brs, acc_neobac, acc_bg, acc_bt, acc_bp, acc_at, acc_mention_nonrenseignee, acc_sansmention, acc_ab, acc_b, acc_tb, acc_tbf, acc_bg_mention, acc_bt_mention, acc_bp_mention, acc_term, acc_term_f, acc_aca_orig, acc_aca_orig_idf, pct_acc_debutpp, pct_acc_datebac, pct_acc_finpp, pct_f, pct_aca_orig, pct_aca_orig_idf, pct_etab_orig, pct_bours, pct_neobac, pct_mention_nonrenseignee, pct_sansmention, pct_ab, pct_b, pct_tb, pct_tbf, pct_bg, pct_bg_mention, pct_bt, pct_bt_mention, pct_bp, pct_bp_mention, prop_tot_bg, prop_tot_bg_brs, prop_tot_bt, prop_tot_bt_brs, prop_tot_bp, prop_tot_bp_brs, prop_tot_at, lib_grp1, ran_grp1, lib_grp2, ran_grp2, lib_grp3, ran_grp3, list_com, tri, detail_forma2, lien_form_psup, taux_acces_ens, part_acces_gen, part_acces_tec, part_acces_pro, etablissement_id_paysage, composante_id_paysage)

---

departement (<u>**dep**</u>, dep_lib, region_etab_aff, academies)

etablissement (<u>**cod_uai**</u>, contrat_etab, g_ea_lib_vx, _#dep_, ville_etab, etablissement_id_paysage)

formation (<u>**cod_aff_form**</u>, _#cod_uai_, lib_for_voe_ins, select_form, fili, lib_comp_voe_ins, form_lib_voe_acc, fil_lib_voe_acc, detail_forma, geolocalisation_des_formations_lon, geolocalisation_des_formations_lat, list_com, tri, detail_forma2, lien_form_psup, composante_id_paysage)

statistiques (<u>_**session**_</u>, <u>_**#cod_aff_form**_</u>, capa_fin, voe_tot, voe_tot_f, nb_voe_pp, nb_voe_pp_internat, nb_voe_pp_bg, nb_voe_pp_bg_brs, nb_voe_pp_bt, nb_voe_pp_bt_brs, nb_voe_pp_bp, nb_voe_pp_bp_brs, nb_voe_pp_at, nb_voe_pc, nb_voe_pc_bg, nb_voe_pc_bt, nb_voe_pc_bp, nb_voe_pc_at, nb_cla_pp, nb_cla_pc, nb_cla_pp_internat, nb_cla_pp_pasinternat, nb_cla_pp_bg, nb_cla_pp_bg_brs, nb_cla_pp_bt, nb_cla_pp_bt_brs, nb_cla_pp_bp, nb_cla_pp_bp_brs, nb_cla_pp_at, prop_tot, acc_tot, acc_tot_f, acc_pp, acc_pc, acc_debutpp, acc_datebac, acc_finpp, acc_internat, acc_brs, acc_neobac, acc_bg, acc_bt, acc_bp, acc_at, acc_mention_nonrenseignee, acc_sansmention, acc_ab, acc_b, acc_tb, acc_tbf, acc_bg_mention, acc_bt_mention, acc_bp_mention, acc_term, acc_term_f, acc_aca_orig, acc_aca_orig_idf, pct_acc_debutpp, pct_acc_datebac, pct_acc_finpp, pct_f, pct_aca_orig, pct_aca_orig_idf, pct_etab_orig, pct_bours, pct_neobac, pct_mention_nonrenseignee, pct_sansmention, pct_ab, pct_b, pct_tb, pct_tbf, pct_bg, pct_bg_mention, pct_bt, pct_bt_mention, pct_bp, pct_bp_mention, prop_tot_bg, prop_tot_bg_brs, prop_tot_bt, prop_tot_bt_brs, prop_tot_bp, prop_tot_bp_brs, prop_tot_at, lib_grp1, ran_grp1, lib_grp2, ran_grp2, lib_grp3, ran_grp3, taux_acces_ens, part_acces_gen, part_acces_tec, part_acces_pro)

## ⚖️ Comparaison des deux versions de la base de données

On observe que la phase 1 présente une modélisation sous la forme d'une seule et unique table qui contient l'entièreté des données de la base. Cette modélisation entraîne d'importantes redondances, car les informations relatives aux départements, aux établissements et aux formations sont dupliquées à chaque nouvelle ligne de statistiques. Cela provoque des risques d'incohérence lors des mises à jour et alourdit la base. La phase 2 propose un schéma relationnel normalisé, décomposé en quatre tables distinctes liées par des clés étrangères : departement, etablissement, formation et statistiques. Cette modélisation résout les problèmes de la phase 1. Cette phase permet donc tout d'abord une élimination des redondances. En effet, la séparation des entités permet de stocker les informations descriptives une seule fois. Le libellé d'un département ou le nom d'un établissement n'est plus répété sur chaque ligne de statistiques. Elle permet également une correction des anomalies de modification : si le contrat d'un établissement change, la modification se fait sur une seule ligne dans la table etablissement, ce qui garantit la cohérence de la base et évite les erreurs de mise à jour partielles. De plus, elle met aussi en place une correction des anomalies d'insertion et de suppression, puisque le nouveau schéma permet d'insérer un département ou un établissement même si aucune formation ou statistique ne lui est encore attribuée. Inversement, la suppression d'une ligne de statistiques n'efface plus les données de la formation ou de l'établissement lié. Enfin, celle-ci permet une garantie de l'intégrité, car la mise en place des clés étrangères empêche l'ajout de statistiques pour une formation inexistante, permettant d'avoir une base de données cohérente et fiable pour les requêtes.

## ⛔ Contraintes d'intégrité

**Contraintes Statiques Explicites (exprimées dans le schéma du modèle)**
- **Clé primaire (Unicité) :**
	- Le triplet (`session`, `cod_uai`, `cod_aff_form`) doit être strictement unique.
- **Valeurs non nulles (Existence) :**
	- Les clés primaires et les attributs d'identification structurelle ne peuvent pas être `NULL`.

	_Note : `dep`, `dep_lib`, `region_etab_aff`, `detail_forma`, `geolocalisation_des_formations_lon`, `geolocalisation_des_formations_lat`, `nb_voe_pp_internat`, `nb_cla_pp_internat`, `nb_cla_pp_pasinternat`, `acc_internat`, `acc_term`, `acc_term_f`, `pct_etab_orig`, `lib_grp1`, `ran_grp1`, `lib_grp2`, `ran_grp2`, `lib_grp3`, `ran_grp3`, `detail_forma2`, `lien_form_psup`, `taux_acces_ens`, `part_acces_gen`, `part_acces_tec`, `part_acces_pro`, `etablissement_id_paysage`, `composante_id_paysage` peuvent être nuls._
- **Contraintes de domaine (CHECK) :**
    - Si un attribut représente un pourcentage (`pct_*`), alors sa valeur est comprise entre 0 et 100.
    - Si un attribut représente un effectif (`voe_*`, `nb_*`, `prop_*`, `acc_*`), alors sa valeur est supérieure ou égale à 0.

**Contraintes Statiques Sémantiques (basées sur les applications)**
- **Inclusion et cohérence des effectifs :**
	- Le nombre de candidates femmes ou de boursiers ne peut absolument pas dépasser le nombre total de vœux ou d'admis. Les attributs de sous-effectifs doivent obligatoirement être inférieurs ou égaux à leurs effectifs globaux de référence correspondants (ex. : `voe_tot_f` $\le$ `voe_tot`, `nb_voe_pp_bg_brs` $\le$ `nb_voe_pp_bg`, `acc_tot_f` $\le$ `acc_tot`, `acc_brs` $\le$ `acc_neobac`).
- **Dépendances fonctionnelles (DF) :**
	- Si l'attribut `cod_uai` est identique pour deux tuples, alors les attributs de localisation (`dep`, `dep_lib`, `region_etab_aff`, `academies`, `ville_etab`) doivent être strictement identiques.
- **Capacité d'accueil :**
	- Si l'attribut `acc_tot` (nombre total des candidats admis) est renseigné, alors il doit être inférieur ou égal à l'attribut `capa_fin` (capacité d'accueil de l'établissement par formation finale).

	_Note : ~12,3 % des entrées (6 860 lignes) présentent `acc_tot` > `capa_fin`. Cette violation de la contrainte reflète une réalité opérationnelle (ajustements tardifs des capacités d'accueil ou sur-inscriptions autorisées) et non une erreur de saisie système._

**Contraintes Dynamiques (mise à jour)**
- **Règle de non-régression :**
	- Si le processus d'admission avance, la valeur de l'attribut `acc_tot` lors d'une mise à jour (`UPDATE`) doit être strictement supérieure ou égale à l'ancienne valeur. Les acceptations définitivement confirmées ne peuvent pas être effacées du système.
- **Ouverture de phase complémentaire :**
	- L'ajout de candidatures en phase complémentaire ne peut se déclencher pour les vœux insérés dans la phase complémentaire active (`nb_voe_pc` > 0) que si le nombre d'admis en phase principale (`acc_pp`) est resté strictement inférieur à la capacité d'accueil de l'établissement par formation finale (`capa_fin`).

_Note : Comme les bases de données de [data.gouv.fr](https://www.data.gouv.fr) sont au format CSV/JSON, elles manquent de contraintes ; donc seules les contraintes statiques explicites ont été ajoutées automatiquement à cette phase._

## 🤔 Exemples de redondances et d'anomalies existantes dans le schéma

- **Redondances :**
	Le *Lycée Saint Exupéry* (UAI `0782539L`) propose deux formations (CPGE et BTS). L'intégralité de ses métadonnées (statut "Public", département "Yvelines", région "Ile-de-France", académie "Versailles", commune "Mantes-la-Jolie", coordonnées GPS "48.9974, 1.69372") est dupliquée à l'identique sur les deux lignes.
- **Anomalie d'insertion :**
	Il est impossible d'ajouter un nouvel établissement (ex : une université venant d'être construite) dans la base de données tant que cet établissement ne propose pas au moins une formation, car la clé primaire requiert un code de formation (`cod_aff_form`).
- **Anomalie de mise à jour :**
	Si la commune ou les coordonnées GPS de l'établissement *Lycée Saint Exupéry* (UAI `0782539L`) changent, il faut modifier cette information sur plusieurs lignes simultanément (CPGE et BTS). Une modification partielle entraînera une incohérence de la base.
- **Anomalie de suppression :**
	Si l'on supprime les formations "CPGE - Lettres" et "BTS - Services - Support à l'action managériale" du *Lycée Saint Exupéry* (UAI `0782539L`), l'existence même de ce lycée, ainsi que sa localisation et son code UAI, sont définitivement effacés de la base de données.

## 💀 Description du processus de normalisation

La normalisation consiste à éliminer les redondances et les anomalies (insertion, mise à jour, suppression) en décomposant la relation universelle.

### 🔗 Dépendances fonctionnelles (DF)

Nous avons identifié les dépendances fonctionnelles suivantes à partir de l'analyse des répétitions de données et de la compréhension de la sémantique des attributs dans le contexte de Parcoursup :

#### ✅ Valide

`acc_bg`, `acc_bt`, `acc_bp` $\to$ `acc_neobac`

`acc_tot`, `acc_datebac` $\to$ `pct_acc_datebac`

`acc_tot`, `acc_debutpp` $\to$ `pct_acc_debutpp`

`acc_tot`, `acc_finpp` $\to$ `pct_acc_finpp`

`acc_tot`, `acc_neobac` $\to$ `pct_neobac`

`acc_tot`, `acc_tot_f` $\to$ `pct_f`

`composante_id_paysage` $\to$ `dep`, `dep_lib`, `academies`, `etablissement_id_paysage`

`lib_comp_voe_ins` $\to$ `lib_for_voe_ins`

`lien_form_psup` $\to$ `cod_aff_form`

`nb_voe_pp_bg`, `nb_voe_pp_bt`, `nb_voe_pp_bp`, `nb_voe_pp_at` $\to$ `nb_voe_pp`

`session`, `cod_aff_form` $\to$ `capa_fin`, `voe_tot`, `voe_tot_f`, `nb_voe_pp`, `nb_voe_pp_internat`, `nb_voe_pp_bg`, `nb_voe_pp_bg_brs`, `nb_voe_pp_bt`, `nb_voe_pp_bt_brs`, `nb_voe_pp_bp`, `nb_voe_pp_bp_brs`, `nb_voe_pp_at`, `nb_voe_pc`, `nb_voe_pc_bg`, `nb_voe_pc_bt`, `nb_voe_pc_bp`, `nb_voe_pc_at`, `nb_cla_pp`, `nb_cla_pc`, `nb_cla_pp_internat`, `nb_cla_pp_pasinternat`, `nb_cla_pp_bg`, `nb_cla_pp_bg_brs`, `nb_cla_pp_bt`, `nb_cla_pp_bt_brs`, `nb_cla_pp_bp`, `nb_cla_pp_bp_brs`, `nb_cla_pp_at`, `prop_tot`, `acc_tot`, `acc_tot_f`, `acc_pp`, `acc_pc`, `acc_debutpp`, `acc_datebac`, `acc_finpp`, `acc_internat`, `acc_brs`, `acc_neobac`, `acc_bg`, `acc_bt`, `acc_bp`, `acc_at`, `acc_mention_nonrenseignee`, `acc_sansmention`, `acc_ab`, `acc_b`, `acc_tb`, `acc_tbf`, `acc_bg_mention`, `acc_bt_mention`, `acc_bp_mention`, `acc_term`, `acc_term_f`, `acc_aca_orig`, `acc_aca_orig_idf`, `prop_tot_bg`, `prop_tot_bg_brs`, `prop_tot_bt`, `prop_tot_bt_brs`, `prop_tot_bp`, `prop_tot_bp_brs`, `prop_tot_at`, `lib_grp1`, `lib_grp2`, `lib_grp3`, `taux_acces_ens`, `part_acces_gen`, `part_acces_tec`, `part_acces_pro`

`session`, `cod_aff_form`, `lib_grp1` $\to$ `ran_grp1`

`session`, `cod_aff_form`, `lib_grp2` $\to$ `ran_grp2`

`session`, `cod_aff_form`, `lib_grp3` $\to$ `ran_grp3`

#### #️⃣ Peut être valide après correction des erreurs de calcul

~~`acc_bg`, `acc_bt`, `acc_bp`, `acc_at` $\to$ `acc_tot`~~

~~`acc_pp`, `acc_pc` $\to$ `acc_tot`~~

~~`acc_sansmention`, `acc_ab`, `acc_b`, `acc_tb`, `acc_tbf` $\to$ `acc_neobac`~~

`acc_tot`, `acc_ab` $\to$ `pct_ab`

`acc_tot`, `acc_aca_orig_idf` $\to$ `pct_aca_orig_idf`

`acc_tot`, `acc_aca_orig` $\to$ `pct_aca_orig`

`acc_tot`, `acc_b` $\to$ `pct_b`

`acc_tot`, `acc_bg_mention` $\to$ `pct_bg_mention`

`acc_tot`, `acc_bg` $\to$ `pct_bg`

`acc_tot`, `acc_bp_mention` $\to$ `pct_bp_mention`

`acc_tot`, `acc_bp` $\to$ `pct_bp`

`acc_tot`, `acc_brs` $\to$ `pct_bours`

`acc_tot`, `acc_bt_mention` $\to$ `pct_bt_mention`

`acc_tot`, `acc_bt` $\to$ `pct_bt`

`acc_tot`, `acc_mention_nonrenseignee` $\to$ `pct_mention_nonrenseignee`

`acc_tot`, `acc_sansmention` $\to$ `pct_sansmention`

`acc_tot`, `acc_tb` $\to$ `pct_tb`

`acc_tot`, `acc_tbf` $\to$ `pct_tbf`

`acc_tot`, `acc_term` $\to$ `pct_etab_orig`

_Note : Les corrections ont été basées sur les recalculs mathématiques des effectifs totaux et des pourcentages._

#### 🔤 Peut être valide après correction des erreurs de grammaire

`academies` $\to$ `region_etab_aff`

`dep` $\to$ `dep_lib`, `region_etab_aff`, `academies`

_Note : Les corrections étaient basées sur les articles [Département français](https://fr.wikipedia.org/wiki/Département_français) et [Région française](https://fr.wikipedia.org/wiki/Région_française)._

#### 🔄 Peut être valide mais nécessite des corrections

`cod_aff_form` $\to$ `cod_uai`, `lib_comp_voe_ins`, `detail_forma`, `geolocalisation_des_formations_lon`, `geolocalisation_des_formations_lat`, `detail_forma2`, `list_com`, `tri`, `lien_form_psup`, `composante_id_paysage`

_Note : ~25,4 % des entrées (14 176 lignes) présentent des erreurs, car certaines données ont changé d'année en année. Donc, pour la migration, les données les plus récentes seront considérées comme correctes, car la vérification manuelle des données prend énormément de temps._

`cod_uai` $\to$ `contrat_etab`, `g_ea_lib_vx`, `dep`, `ville_etab`, `etablissement_id_paysage`

_Note : ~0,8 % des entrées (442 lignes) présentent des erreurs, car pour le même code UAI (Unité Administrative Immatriculée), il existe plusieurs formations même si, par définition, il s'agit d'un identifiant unique strictement codifié. Donc, pour la migration, les données les plus récentes seront considérées comme correctes, car la vérification manuelle des données prend énormément de temps._

~~`geolocalisation_des_formations_lon`, `geolocalisation_des_formations_lat` $\to$ `dep`, `dep_lib`, `region_etab_aff`, `academies`, `ville_etab`~~

~~_Note : ~3,8 % des entrées (2 134 lignes) présentent des erreurs avant et ~0,4 % (210 lignes) après les corrections mathématiques. Donc, les corrections restantes ont été apportées uniquement aux entrées de la session 2025 et le reste va être remplacé par les données les plus récentes, car la vérification des données par carte prend énormément de temps._~~

~~`lib_comp_voe_ins` $\to$ `select_form`, `fili`, `form_lib_voe_acc`, `fil_lib_voe_acc`~~

~~_Note : ~1,8 % des entrées (996 lignes) présentent des erreurs, telles que l'existence simultanée de la même formation non sélective et sélective, une formation correcte remplacée par "Autre formation", des troncations mal faites, etc. Donc, pour la migration, les données les plus récentes seront considérées comme correctes, car la vérification manuelle des données prend énormément de temps._~~

~~`nb_cla_pp_internat`, `nb_cla_pp_pasinternat` $\to$ `nb_cla_pp`~~

Le processus de normalisation exige la définition d'une couverture minimale. Cela implique d'éliminer les DF redondantes, transitives ou triviales pour construire des relations optimales. Pour cela, nous avons décidé que si une décomposition génère une relation 1:1 stricte sans bénéfice d'isolation sémantique, alors la décomposition est une overengineering et doit être annulée, c'est-à-dire qu'il vaut mieux avoir une table avec plusieurs attributs que d'avoir plusieurs tables avec des relations de clé primaire à un seul attribut (nous pensons que cela peut potentiellement réduire la performance (a cause de fragmentation), augmenter la complexité (a cause des jointures) et créer de l'incohérence (lors de mise à jour)). Selon notre humble avis, parmi les dépendances fonctionnelles testées, il semble préférable de préserver et d'utiliser les suivantes :

`dep` $\to$ `dep_lib`, `region_etab_aff`, `academies`

`cod_uai` $\to$ `contrat_etab`, `g_ea_lib_vx`, `dep`, `ville_etab`, `etablissement_id_paysage`

`cod_aff_form` $\to$ `cod_uai`, `lib_for_voe_ins`, `select_form`, `fili`, `lib_comp_voe_ins`, `form_lib_voe_acc`, `fil_lib_voe_acc`, `detail_forma`, `geolocalisation_des_formations_lon`, `geolocalisation_des_formations_lat`, `list_com`, `tri`, `detail_forma2`, `lien_form_psup`, `composante_id_paysage`

`session`, `cod_aff_form` $\to$ `capa_fin`, `voe_tot`, `voe_tot_f`, `nb_voe_pp`, `nb_voe_pp_internat`, `nb_voe_pp_bg`, `nb_voe_pp_bg_brs`, `nb_voe_pp_bt`, `nb_voe_pp_bt_brs`, `nb_voe_pp_bp`, `nb_voe_pp_bp_brs`, `nb_voe_pp_at`, `nb_voe_pc`, `nb_voe_pc_bg`, `nb_voe_pc_bt`, `nb_voe_pc_bp`, `nb_voe_pc_at`, `nb_cla_pp`, `nb_cla_pc`, `nb_cla_pp_internat`, `nb_cla_pp_pasinternat`, `nb_cla_pp_bg`, `nb_cla_pp_bg_brs`, `nb_cla_pp_bt`, `nb_cla_pp_bt_brs`, `nb_cla_pp_bp`, `nb_cla_pp_bp_brs`, `nb_cla_pp_at`, `prop_tot`, `acc_tot`, `acc_tot_f`, `acc_pp`, `acc_pc`, `acc_debutpp`, `acc_datebac`, `acc_finpp`, `acc_internat`, `acc_brs`, `acc_neobac`, `acc_bg`, `acc_bt`, `acc_bp`, `acc_at`, `acc_mention_nonrenseignee`, `acc_sansmention`, `acc_ab`, `acc_b`, `acc_tb`, `acc_tbf`, `acc_bg_mention`, `acc_bt_mention`, `acc_bp_mention`, `acc_term`, `acc_term_f`, `acc_aca_orig`, `acc_aca_orig_idf`, `pct_acc_debutpp`, `pct_acc_datebac`, `pct_acc_finpp`, `pct_f`, `pct_aca_orig`, `pct_aca_orig_idf`, `pct_etab_orig`, `pct_bours`, `pct_neobac`, `pct_mention_nonrenseignee`, `pct_sansmention`, `pct_ab`, `pct_b`, `pct_tb`, `pct_tbf`, `pct_bg`, `pct_bg_mention`, `pct_bt`, `pct_bt_mention`, `pct_bp`, `pct_bp_mention`, `prop_tot_bg`, `prop_tot_bg_brs`, `prop_tot_bt`, `prop_tot_bt_brs`, `prop_tot_bp`, `prop_tot_bp_brs`, `prop_tot_at`, `lib_grp1`, `ran_grp1`, `lib_grp2`, `ran_grp2`, `lib_grp3`, `ran_grp3`, `taux_acces_ens`, `part_acces_gen`, `part_acces_tec`, `part_acces_pro`

### 🔪 Décomposition

Vu la faible qualité de la base de données originale et donc la quantité d'erreurs parmi les données, ainsi que le fait qu'on ne peut garantir ni la correction ni la complétude de l'ensemble des dépendances fonctionnelles (ce qui est souvent le cas même en production), on ne peut pas utiliser d'algorithme pour la décomposition en 3NF SPI et SPD ni pour la décomposition en BCNF SPI. Néanmoins, nous pouvons faire la décomposition en utilisant notre propre algorithme, qui consiste à déterminer manuellement la couverture minimale (en fait, les 4 DF mentionnées ci-dessus) et à migrer les données de la façon suivante :

- Tous les pourcentages seront recalculés à partir des effectifs.
- Tous les départements et régions seront corrigés manuellement en utilisant les données les plus récentes disponibles en ligne.
- Si l'on rencontre une clé dupliquée et que les données ne sont pas les mêmes, on les met à jour.
	- Si les nouvelles données sont nulles, on préserve les anciennes.

Cela ne garantit ni le SPI ni le SPD, mais cela permet d'avoir les données les plus récentes dans les nouvelles tables (car MariaDB, par défaut, trie les données à partir du premier attribut, donc les données de 2022 seront remplacées par celles de 2023 en cas de conflit, puis par celles de 2024 et de 2025, car le premier attribut est la session), et cela évite aussi certaines pertes de données en évitant le remplacement par null si les nouvelles données ne sont pas complètes.
Si nous pouvions avoir les dépendances fonctionnelles correctes (pas inconsistantes à cause des variations des données), nous pourrions, mais le processus manuel de correction pourrait prendre plusieurs mois, ce qui est sans doute hors de ce projet. D'un autre côté, notre nouvelle relation est quand même bien en BCNF car :

- S'il n'y a pas de liste d'attributs, alors c'est en 1NF.
- Si chaque attribut non clé dépend de la totalité de la clé primaire sans dépendance partielle, alors c'est en 2NF.
- S'il n'y a pas de dépendances transitives entre attributs non clés, alors c'est en 3NF.
- Si, pour toute dépendance fonctionnelle non triviale, le déterminant est une surclé, alors le schéma final est en BCNF.

L'intégrité de la décomposition est démontrée. Si l'intersection des schémas décomposés est une clé primaire pour l'une des relations, alors la décomposition est SPI, prévenant la génération de tuples erronés lors des jointures, ce qui est bien le cas maintenant après normalisation. Si l'union des dépendances fonctionnelles préservées dans les nouvelles tables correspond à la couverture minimale initiale, alors la décomposition est SPD, ce qui est aussi bien le cas maintenant. L'architecture basée sur les clés étrangères (dep, cod_uai, cod_aff_form) valide strictement ces conditions structurelles.

## ⚙️ Features

| Key                              | Description                                                                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `session`                        | Session                                                                                                                                          |
| `contrat_etab`                   | Statut de l'établissement de la filière de formation (public, privé…)                                                                            |
| `cod_uai`                        | Code UAI de l'établissement                                                                                                                      |
| `g_ea_lib_vx`                    | Établissement                                                                                                                                    |
| `dep`                            | Code départemental de l'établissement                                                                                                            |
| `dep_lib`                        | Département de l'établissement                                                                                                                   |
| `region_etab_aff`                | Région de l'établissement                                                                                                                        |
| `academies`                      | Académie de l'établissement                                                                                                                      |
| `ville_etab`                     | Commune de l'établissement                                                                                                                       |
| `lib_for_voe_ins`                | Filière de formation                                                                                                                             |
| `select_form`                    | Sélectivité                                                                                                                                      |
| `fili`                           | Filière de formation très agrégée                                                                                                                |
| `lib_comp_voe_ins`               | Filière de formation détaillée                                                                                                                   |
| `form_lib_voe_acc`               | Filière de formation                                                                                                                             |
| `fil_lib_voe_acc`                | Filière de formation détaillée bis                                                                                                               |
| `detail_forma`                   | Filière de formation très détaillée                                                                                                              |
| `geolocalisation_des_formations` | Coordonnées GPS de la formation                                                                                                                  |
| `capa_fin`                       | Capacité de l'établissement par formation                                                                                                        |
| `voe_tot`                        | Effectif total des candidats pour une formation                                                                                                  |
| `voe_tot_f`                      | Dont effectif des candidates pour une formation                                                                                                  |
| `nb_voe_pp`                      | Effectif total des candidats en phase principale                                                                                                 |
| `nb_voe_pp_internat`             | Dont effectif des candidats ayant postulé en internat                                                                                            |
| `nb_voe_pp_bg`                   | Effectif des candidats néo bacheliers généraux en phase principale                                                                               |
| `nb_voe_pp_bg_brs`               | Dont effectif des candidats boursiers néo bacheliers généraux en phase principale                                                                |
| `nb_voe_pp_bt`                   | Effectif des candidats néo bacheliers technologiques en phase principale                                                                         |
| `nb_voe_pp_bt_brs`               | Dont effectif des candidats boursiers néo bacheliers technologiques en phase principale                                                          |
| `nb_voe_pp_bp`                   | Effectif des candidats néo bacheliers professionnels en phase principale                                                                         |
| `nb_voe_pp_bp_brs`               | Dont effectif des candidats boursiers néo bacheliers professionnels en phase principale                                                          |
| `nb_voe_pp_at`                   | Effectif des autres candidats en phase principale                                                                                                |
| `nb_voe_pc`                      | Effectif total des candidats en phase complémentaire                                                                                             |
| `nb_voe_pc_bg`                   | Effectif des candidats néo bacheliers généraux en phase complémentaire                                                                           |
| `nb_voe_pc_bt`                   | Effectif des candidats néo bacheliers technologique en phase complémentaire                                                                      |
| `nb_voe_pc_bp`                   | Effectif des candidats néo bacheliers professionnels en phase complémentaire                                                                     |
| `nb_voe_pc_at`                   | Effectifs des autres candidats en phase complémentaire                                                                                           |
| `nb_cla_pp`                      | Effectif total des candidats classés par l'établissement en phase principale                                                                     |
| `nb_cla_pc`                      | Effectif des candidats classés par l'établissement en phase complémentaire                                                                       |
| `nb_cla_pp_internat`             | Effectif des candidats classés par l'établissement en internat (CPGE)                                                                            |
| `nb_cla_pp_pasinternat`          | Effectif des candidats classés par l'établissement hors internat (CPGE)                                                                          |
| `nb_cla_pp_bg`                   | Effectif des candidats néo bacheliers généraux classés par l'établissement                                                                       |
| `nb_cla_pp_bg_brs`               | Dont effectif des candidats boursiers néo bacheliers généraux classés par l'établissement                                                        |
| `nb_cla_pp_bt`                   | Effectif des candidats néo bacheliers technologiques classés par l'établissement                                                                 |
| `nb_cla_pp_bt_brs`               | Dont effectif des candidats boursiers néo bacheliers technologiques classés par l'établissement                                                  |
| `nb_cla_pp_bp`                   | Effectif des candidats néo bacheliers professionnels classés par l'établissement                                                                 |
| `nb_cla_pp_bp_brs`               | Dont effectif des candidats boursiers néo bacheliers professionnels classés par l'établissement                                                  |
| `nb_cla_pp_at`                   | Effectif des autres candidats classés par l'établissement                                                                                        |
| `prop_tot`                       | Effectif total des candidats ayant reçu une proposition d'admission de la part de l'établissement                                                |
| `acc_tot`                        | Effectif total des candidats ayant accepté la proposition de l'établissement (admis)                                                             |
| `acc_tot_f`                      | Dont effectif des candidates admises                                                                                                             |
| `acc_pp`                         | Effectif des admis en phase principale                                                                                                           |
| `acc_pc`                         | Effectif des admis en phase complémentaire                                                                                                       |
| `acc_debutpp`                    | Dont effectif des admis ayant reçu leur proposition d'admission à l'ouverture de la procédure principale                                         |
| `acc_datebac`                    | Dont effectif des admis ayant reçu leur proposition d'admission avant le baccalauréat                                                            |
| `acc_finpp`                      | Dont effectif des admis ayant reçu leur proposition d'admission avant la fin de la procédure principale                                          |
| `acc_internat`                   | Dont effectif des admis en internat                                                                                                              |
| `acc_brs`                        | Dont effectif des admis boursiers néo bacheliers                                                                                                 |
| `acc_neobac`                     | Effectif des admis néo bacheliers                                                                                                                |
| `acc_bg`                         | Effectif des admis néo bacheliers généraux                                                                                                       |
| `acc_bt`                         | Effectif des admis néo bacheliers technologiques                                                                                                 |
| `acc_bp`                         | Effectif des admis néo bacheliers professionnels                                                                                                 |
| `acc_at`                         | Effectif des autres candidats admis                                                                                                              |
| `acc_mention_nonrenseignee`      | Dont effectif des admis néo bacheliers sans information sur la mention au bac                                                                    |
| `acc_sansmention`                | Dont effectif des admis néo bacheliers sans mention au bac                                                                                       |
| `acc_ab`                         | Dont effectif des admis néo bacheliers avec mention Assez Bien au bac                                                                            |
| `acc_b`                          | Dont effectif des admis néo bacheliers avec mention Bien au bac                                                                                  |
| `acc_tb`                         | Dont effectif des admis néo bacheliers avec mention Très Bien au bac                                                                             |
| `acc_tbf`                        | Dont effectif des admis néo bacheliers avec mention Très Bien avec félicitations au bac                                                          |
| `acc_bg_mention`                 | Effectif des admis néo bacheliers généraux ayant eu une mention au bac                                                                           |
| `acc_bt_mention`                 | Effectif des admis néo bacheliers technologiques ayant eu une mention au bac                                                                     |
| `acc_bp_mention`                 | Effectif des admis néo bacheliers professionnels ayant eu une mention au bac                                                                     |
| `acc_term`                       | Dont effectif des admis issus du même établissement (BTS/CPGE)                                                                                   |
| `acc_term_f`                     | Dont effectif des admises issues du même établissement (BTS/CPGE)                                                                                |
| `acc_aca_orig`                   | Dont effectif des admis issus de la même académie                                                                                                |
| `acc_aca_orig_idf`               | Dont effectif des admis issus de la même académie (Paris/Créteil/Versailles réunies)                                                             |
| `pct_acc_debutpp`                | % d'admis ayant reçu leur proposition d'admission à l'ouverture de la procédure principale                                                       |
| `pct_acc_datebac`                | % d'admis ayant reçu leur proposition d'admission avant le baccalauréat                                                                          |
| `pct_acc_finpp`                  | % d'admis ayant reçu leur proposition d'admission avant la fin de la procédure principale                                                        |
| `pct_f`                          | % d'admis dont filles                                                                                                                            |
| `pct_aca_orig`                   | % d'admis néo bacheliers issus de la même académie                                                                                               |
| `pct_aca_orig_idf`               | % d'admis néo bacheliers issus de la même académie (Paris/Créteil/Versailles réunies)                                                            |
| `pct_etab_orig`                  | % d'admis néo bacheliers issus du même établissement (BTS/CPGE)                                                                                  |
| `pct_bours`                      | % d'admis néo bacheliers boursiers                                                                                                               |
| `pct_neobac`                     | % d'admis néo bacheliers                                                                                                                         |
| `pct_mention_nonrenseignee`      | % d'admis néo bacheliers sans information sur la mention au bac                                                                                  |
| `pct_sansmention`                | % d'admis néo bacheliers sans mention au bac                                                                                                     |
| `pct_ab`                         | % d'admis néo bacheliers avec mention Assez Bien au bac                                                                                          |
| `pct_b`                          | % d'admis néo bacheliers avec mention Bien au bac                                                                                                |
| `pct_tb`                         | % d'admis néo bacheliers avec mention Très Bien au bac                                                                                           |
| `pct_tbf`                        | % d'admis néo bacheliers avec mention Très Bien avec félicitations au bac                                                                        |
| `pct_bg`                         | % d'admis néo bacheliers généraux                                                                                                                |
| `pct_bg_mention`                 | Dont % d'admis avec mention (BG)                                                                                                                 |
| `pct_bt`                         | % d'admis néo bacheliers technologiques                                                                                                          |
| `pct_bt_mention`                 | Dont % d'admis avec mention (BT)                                                                                                                 |
| `pct_bp`                         | % d'admis néo bacheliers professionnels                                                                                                          |
| `pct_bp_mention`                 | Dont % d'admis avec mention (BP)                                                                                                                 |
| `prop_tot_bg`                    | Effectif des candidats en terminale générale ayant reçu une proposition d'admission de la part de l'établissement                                |
| `prop_tot_bg_brs`                | Dont effectif des candidats boursiers en terminale générale ayant reçu une proposition d'admission de la part de l'établissement                 |
| `prop_tot_bt`                    | Effectif des candidats en terminale technologique ayant reçu une proposition d'admission de la part de l'établissement                           |
| `prop_tot_bt_brs`                | Dont effectif des candidats boursiers en terminale technologique ayant reçu une proposition d'admission de la part de l'établissement            |
| `prop_tot_bp`                    | Effectif des candidats en terminale professionnelle ayant reçu une proposition d'admission de la part de l'établissement                         |
| `prop_tot_bp_brs`                | Dont effectif des candidats boursiers en terminale générale professionnelle ayant reçu une proposition d'admission de la part de l'établissement |
| `prop_tot_at`                    | Effectif des autres candidats ayant reçu une proposition d'admission de la part de l'établissement                                               |
| `lib_grp1`                       | Regroupement 1 effectué par les formations pour les classements                                                                                  |
| `ran_grp1`                       | Rang du dernier appelé du groupe 1                                                                                                               |
| `lib_grp2`                       | Regroupement 2 effectué par les formations pour les classements                                                                                  |
| `ran_grp2`                       | Rang du dernier appelé du groupe 2                                                                                                               |
| `lib_grp3`                       | Regroupement 3 effectué par les formations pour les classements                                                                                  |
| `ran_grp3`                       | Rang du dernier appelé du groupe 3                                                                                                               |
| `list_com`                       | list_com                                                                                                                                         |
| `tri`                            | tri                                                                                                                                              |
| `cod_aff_form`                   | cod_aff_form                                                                                                                                     |
| `detail_forma2`                  | Concours communs et banque d'épreuves                                                                                                            |
| `lien_form_psup`                 | Lien de la formation sur la plateforme Parcoursup                                                                                                |
| `taux_acces_ens`                 | Taux d'accès                                                                                                                                     |
| `part_acces_gen`                 | Part des terminales générales qui étaient en position de recevoir une proposition en phase principale                                            |
| `part_acces_tec`                 | Part des terminales technologiques qui étaient en position de recevoir une proposition en phase principale                                       |
| `part_acces_pro`                 | Part des terminales professionnelles qui étaient en position de recevoir une proposition en phase principale                                     |
| `etablissement_id_paysage`       | etablissement_id_paysage                                                                                                                         |
| `composante_id_paysage`          | composante_id_paysage                                                                                                                            |

## ⚠️ Disclaimers

- **phpMyAdmin**: Import may take several minutes for a bzip2-compressed SQL file due to 14,252 entries with 117 attributes each.

## 📖 Usage Examples

### Standard Conversion

Convert specified input file using defaults for output, database, and table.
```bash
python -m parcoursup.cli -i fr-esr-parcoursup.json
```

Convert specified input files using defaults for output, database, and table. Rename keys, define primary keys, and set non-null values.
```bash
python -m parcoursup.cli -i fr-esr-parcoursup.json fr-esr-parcoursup_2024.json fr-esr-parcoursup_2023.json fr-esr-parcoursup_2022.json -r acad_mies:academies g_olocalisation_des_formations:geolocalisation_des_formations -p session cod_uai cod_aff_form -n -P -C
```

Create functional dependency SQL checks from a README file.
```bash
python -m parcoursup.cli -f README.md
```

Create functional dependency SQL checks from a README file with a session filter.
```bash
python -m parcoursup.cli -f README.md -w session=2025
```

## 🎨 Command-Line Arguments

| Argument                      | Description                                                             |
|-------------------------------|-------------------------------------------------------------------------|
| `-i, --input <path>`          | Path(s) to the input `.json` file(s)                                    |
| `-o, --output <path>`         | Path to the output `.sql` file                                          |
| `-d, --database <name>`       | Name of the MySQL database                                              |
| `-t, --table <name>`          | Name of the MySQL table                                                 |
| `-r, --rename <key:new_key>`  | Rename keys. Use key:new_key                                            |
| `-p, --primary <key>`         | Primary key(s)                                                          |
| `-n, --not-null`              | Set keys with non-null values as NOT NULL                               |
| `-P, --percentages`           | Check for percentages (0 to 100)                                        |
| `-C, --counts`                | Check for counts (>= 0)                                                 |
| `-s, --split`                 | Split insert requests into multiple `.sql` files                        |
| `--print`                     | Print non-null percentages or counts instead of producing a `.sql` file |
| `--range <start,end>`         | Process entries within the specified range (zero-indexed)               |
| `--range-start <n>`           | Set the starting entry index for the processing range                   |
| `--range-end <n>`             | Set the ending entry index for the processing range                     |
| `--first <n>`                 | Process only the first N entries                                        |
| `--last <n>`                  | Process only the last N entries                                         |
| `-f, --fds <path>`            | Path to the file containing functional dependencies to check            |
| `-w, --where <clause>`        | Append a custom WHERE clause for functional dependency checks           |

## 🐛 Bugs

Not yet found.

## ⛔ Known Limitations

Not yet known.

## 🙏 Thanks

Creators of:

- [Parcoursup 2025](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup/table/?sort=tri)
- [Parcoursup 2024](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2024/table/?sort=tri)
- [Parcoursup 2023](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2023/table/?sort=tri)
- [Parcoursup 2022](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-parcoursup_2022/table/?sort=tri)

People:

- Providing a way to check functional dependencies
	- [SQL statement to prove that A->B in a R(ABCD)](https://stackoverflow.com/questions/4352535/sql-statement-to-prove-that-a-b-in-a-rabcd)

## 🤝 Contribution

Contributions, suggestions, and new ideas are heartily welcomed. If you're considering significant modifications, please initiate an issue for discussion before submitting a pull request.

## 📜 License

[![MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💖 Support

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xamituchido)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/inc44)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/Inc44)