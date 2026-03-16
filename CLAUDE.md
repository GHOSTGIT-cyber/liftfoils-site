# Contexte projet — Lift Foils France (liftfoils.fr)

## MCP WordPress connectés

Deux serveurs MCP WordPress sont actifs via `.mcp.json` à la racine `C:\Users\bakar\` :

- **wordpress-live** → `https://liftfoils.fr/` (site de production)
- **wordpress-staging** → `https://liftfoils.fr/staging/` (site de test)

Les tokens JWT expirent dans ~30 jours. Pour les renouveler :
wp-admin > Réglages > WordPress MCP > Generate New Token

## Accès direct site (session curl)

```bash
# Login curl (cookies stockés dans /tmp/wp_cookies.txt)
curl -sc /tmp/wp_cookies.txt "https://liftfoils.fr/wp-login.php" \
  -d "log=bakari06%40live.fr&pwd=VOTRE_MDP&wp-submit=Se+connecter&testcookie=1" \
  -H "Cookie: wordpress_test_cookie=WP+Cookie+check" -L
```

## Infos site

- **URL live** : https://liftfoils.fr
- **URL staging** : https://liftfoils.fr/staging
- **table_prefix** : `wor5145_`
- **Thème actif** : Atelier Child (OceanWP parent)
- **Plugins clés** : WP Rocket (cache), Elementor, WooCommerce, Swift Framework, Yoast SEO
- **Elementor** : ne s'ouvre PAS sur le live (bug en cours, nonce expiré)
- **PHP** : 8.4.x sur les deux environnements

## Méthode de création de pages (sans Elementor)

Utiliser `mcp__wordpress-live__wp_add_page` avec du HTML custom en blocs Gutenberg (`<!-- wp:html -->`).

### Structure CSS utilisée (préfixe `.lf2-`)

Pages déjà créées en brouillon :
- **ID 29945** — Accueil V2 (simple, sections colorées)
- **ID 29946** — Accueil V3 (premium, style liftfoils.com avec hero vidéo, marquee, split panels)

### Assets disponibles sur le serveur

**Images produit (CDN Shopify liftfoils.com) :**
```
LIFT5 Pro 4'4  : https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_4_4_SUNKISSED_Package_Iso_Shadow_2000x2000_07c630aa-b1ef-4ab3-b824-407ba3d03c1f.png
LIFT5 Sport 4'9: https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_4_9_STEELBLUE_Package_Iso_Shadow_2000x2000_5a4014ba-a3ec-4a38-8006-2e4d32168877.png
LIFT5 Cruiser 5'4: https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFT5_5_4_CARBONBLACK_Package_Iso_Shadow_2000x2000_c59a7777-4dde-4045-8362-15f929401768.png
LIFTX 4'3      : https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFTX_4_3_OFFWHITE_Package_Iso_Shadow_2000x2000_f621ab95-452d-4c71-9790-1df69d7ca8c3.png
LIFTX 4'8      : https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFTX_4_8_SPARKBLUE_Package_Iso_Shadow_2000x2000_a6ae3fee-ff22-4811-ab12-ba5e5242a9af.png
LIFTX 5'2      : https://cdn.shopify.com/s/files/1/0607/0907/7155/files/2025_LIFTX_5_2_DAWNPATROL_Package_Iso_Shadow_2000x2000_012a6dba-e31b-40a0-9675-8947a4d21e69.png
```

**Vidéos (serveur liftfoils.fr) :**
```
Hero principal : https://liftfoils.fr/wp-content/uploads/2021/03/Lift-Foils-eFoil-Electric-Surfboard-Premium-Surf-Hydrofoils-10.mp4
Lift5 drone    : https://liftfoils.fr/wp-content/uploads/2021/03/Lift-Foils-eFoil-Lift-5-vue-drone.mp4
LiftX hybride  : https://liftfoils.fr/wp-content/uploads/2021/03/LIFTX-eFoil-Hybrid-eFoil-Beyond-Foil-Assist-for-Surf-Progression-3.mp4
LiftX rouge    : https://liftfoils.fr/wp-content/uploads/2021/03/LIFTX-eFoil-mec-en-rouge.mp4
```

**Photos lifestyle (serveur liftfoils.fr) :**
```
Cliff 1        : https://liftfoils.fr/wp-content/uploads/2021/03/0097_Lift5Launch_Sunkiss_Cliff_011325.JPG.JPG
Famille cliff  : https://liftfoils.fr/wp-content/uploads/2021/03/0094_Lift5Launch_Family_Cliff_011325.JPG
Anna côte azur : https://liftfoils.fr/wp-content/uploads/2025/12/Lift_sunrise-71-e1677709687465-e...
```

## Charte graphique liftfoils.com

- **Couleur accent** : `#36B7B2` (teal)
- **Fond sombre** : `#0a0a0a` / `#0d0d0d`
- **Fond clair** : `#fff` / `#f5f5f3`
- **Texte** : `#111` / `#555` / `#aaa`
- **Typographie** : font-weight 200 (titres), 300 (body), 500 (emphasis)
- **Letterspacing** : 0.1-0.25em sur les labels/eyebrows
- **Style** : minimaliste premium, espaces généreux, no border-radius

## Données produits (prix en EUR pour liftfoils.fr)

| Produit | Prix FR |
|---|---|
| Lift5 Pro 4'4" | À partir de 13 499 € |
| Lift5 Sport 4'9" | À partir de 13 499 € |
| Lift5 Cruiser 5'4" | À partir de 13 499 € |
| LiftX 4'3" | À partir de 9 999 € |
| LiftX 4'8" | À partir de 9 999 € |
| LiftX 5'2" | À partir de 9 999 € |

## Données scrappées liftfoils.com

Fichier JSON disponible : `C:\Users\bakar\Downloads\liftfoils_scraped.json`
Format : `{ url, scraped_at, site_type: "shopify", shopify: { products, collections, pages } }`

## Fichiers importants

| Fichier | Emplacement |
|---|---|
| Config MCP | `C:\Users\bakar\.mcp.json` |
| Settings Claude | `C:\Users\bakar\.claude\settings.json` |
| .htaccess live (corrigé) | `C:\Users\bakar\Desktop\.htaccess` |
| wp-config.php live (corrigé) | `C:\Users\bakar\Desktop\wp-config.php` |
| JSON scrapping liftfoils.com | `C:\Users\bakar\Downloads\liftfoils_scraped.json` |
