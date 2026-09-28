# Classic Beyblade physics and asset-reference revision

The attached knowledge file was treated as domain reference material. Dialogue timing and v9 occupancy locks were preserved.

- Classic shooter attachment, rigid-winder release, planted-tip landing, stadium-slope motion, Attack Ring collision/recoil, wobble-to-stop, and Bit Beast anchoring were corrected where relevant.
- Every shot now names each visible canonical asset with its stable H3 `<Subject N>` label.
- Every segment now persists the same canonical attachment list on the importer-facing `canonicalReferences` field with `attach: true`, explicit image order and H3 role, so runtime prompt recompilation retains props, people and locations.
- IPA spellings in dialogue were restored to the original written words: Ebudhou, Pakhangba, Baba, Eema, and Kangla.
- Five storyboard images were replaced: SEG_SC005_001, SEG_SC005_008, SEG_SC006_003, SEG_SC006_005, SEG_SC007_002.

## Segments that do not need reshoot

SEG_SC001_003, SEG_SC002_001, SEG_SC002_002, SEG_SC002_003, SEG_SC002_004, SEG_SC002_005, SEG_SC003_001, SEG_SC003_002, SEG_SC003_003, SEG_SC003_004, SEG_SC003_005, SEG_SC003_006, SEG_SC004_001, SEG_SC004_002, SEG_SC004_003, SEG_SC004_004, SEG_SC005_002, SEG_SC005_003, SEG_SC005_004, SEG_SC005_005, SEG_SC005_006, SEG_SC005_007, SEG_SC006_002, SEG_SC006_007, SEG_SC006_009, SEG_SC007_003, SEG_SC008_001, SEG_SC008_002

## Segments recommended for reshoot

SEG_SC001_001, SEG_SC001_002, SEG_SC005_001, SEG_SC005_008, SEG_SC005_009, SEG_SC006_001, SEG_SC006_003, SEG_SC006_004, SEG_SC006_005, SEG_SC006_006, SEG_SC006_008, SEG_SC007_001, SEG_SC007_002, SEG_SC007_004, SEG_SC007_005

Static importer, H3, asset-path, continuity, dialogue, and storyboard checks passed. Motion must still be checked on newly generated video takes.
