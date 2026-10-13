# alkotester.az
- 14 məhsul × 3 dil (az, ru, en), əl ilə yazılmış statik sayt — generator yoxdur, dəyişikliklər birbaşa HTML-də edilir.
- Yeni məhsul: mövcud məhsul səhifəsini 3 dildə köçür, kateqoriya səhifəsinə, index-ə, search.json (3 dil) və sitemap.xml-ə əlavə et.
- Dərcdən əvvəl: python3 _build/check.py  (qırıq keçid, sitemap, axtarış yoxlaması).
- Silinən faylların yolunu .deploy-remove.txt-ə yaz.
- Dərc: push → cPanel › Git Version Control › Manage › Pull or Deploy › Update from Remote → Deploy HEAD Commit.
