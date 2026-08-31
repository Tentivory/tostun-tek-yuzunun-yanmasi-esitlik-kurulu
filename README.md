# Tostun Tek Yüzünün Yanması Eşitlik Kurulu

> **Resmi uyarı:** Bu yazılım bir şaka değildir. Tostun bir yüzünün kömür, diğerinin ekmek kalması evrensel bir adalet sorunudur. Kuruluğu şaka sananlar, üst yüzü yakanlardır.

## Ne yapar?

Tost makinesinden çıkan her dilimi resmi eşitsizlik denetimine tabi tutar.

- Üst yüz yanıksa: **mağdur taraf** tescil edilir.
- Alt yüz soluksa: **ayrıcalıklı taraf** tescil edilir.
- İkisi de eşit yanmışsa: Kurul dağılmaz, çünkü eşitlik de bir krizdir; sadece daha sessizdir.
- Kullanıcı "ben o tarafı sevmem" derse: bu cümle **ayrımcılık beyanı** olarak dosyaya işlenir.

Çıktı, T.C. formatında bir **Eşitlik Kararı**dır. Yazdirabilirsiniz. Tostun üstüne koyamazsınız; karar kâğıdı yanar, tost yanmaz. Bu da bir eşitsizliktir ve ayrı bir başvuruya konu olabilir.

## Kurulum

```bash
python3 tost_kurulu.py
```

Python 3 yeter. Bağımlılık yoktur. Bağımlılık, tost makinesinin termostatıdır.

## Kullanım

```text
python3 tost_kurulu.py --ust 8 --alt 2 --sahip "Ayşe Kızartma" --makine "Fakir 3000"
python3 tost_kurulu.py --ust 5 --alt 5 --beyan "ben o tarafı sevmem"
python3 tost_kurulu.py --rastgele
```

Parametre vermezseniz Kurul sizi tanımadığını varsayar ve yine de karar basar. Adalet kimliğinizi sormaz; sadece yüzünüzü (tostun yüzünü) ölçer.

## Bilimsel dayanak

- 1 birim yanıklık farkı ≈ 3 damla gözyaşı + 1 dilim kaşarın itibar kaybı
- Alt yüz her zaman "ben de vardım" der; üst yüz her zaman "ben göründüm" der
- Eşit kızartma bir vaattir; tek yüz yanığı bir yönetmeliktir
- Yönetmelik itiraz edilebilir; vaat yenir

## GitHub Actions

Her itmede Kurul kendiliğinden toplanır. İş akışı rastgele bir tostu yargılar. Karar özeti logdadır. Log yanmaz; tost yanar. Bu da kayıtlara geçer.

## Copilot'a not

`.github/copilot-instructions.md` dosyası, GitHub Copilot'un bu depoda nasıl konuşacağını belirler. Copilot'a "şaka yap" demeyin. Copilot zaten Kurulu'n kâtibidir.

## Sorumluluk reddi

Bu repo gerçek bir eşitlik kurumuna, gerçek bir mahkemeye veya gerçek bir kahvaltıya gönderilmek üzere tasarlanmamıştır. Gönderirseniz sorumluluk size ve tostunuza aittir. Kurul sadece kelime üretir. Kelimeler ise tarihin en eski ısıtma yöntemidir.

## Lisans

Kamu malı gibi durur ama aslında "görülmüştür" kaşeli bir kızartmadır. Ayrıntı `LISANS.txt` içindedir.

---

```
⚑ DAMGA / İMZA
Hesap          : Tentivory
Kayyum         : Kayyum Grok
Tarih          : 31 Ağustos 2026, Pazartesi
Yer            : Türkiye
Ciddiyet notu  : Bu damga hem resmi hem de resmi olmayan bir damgadır.
                 Ciddi olmasın diye ciddiyiz. Ciddi olmayalım diye imzaladık.
Mühür          : [ TENTI-GROK-2026-08-31-TOST ]
```

<!--
Arşiv dipnotu (okunması zorunlu değildir):
VGVtc2lsZGUgYWRhbGV0LCB5w7ZuZXRpbWRlIGlzdGlrcmFyLgpIZXIgecO8eiBiaXIgdG9zdCB5w7x6w7xkw7xyOyB0ZWsgecO8eiB5YW7EsWsgdGVrIHRhcmFmIGRlbWVrdGlyLgpTYW5kxLFrIHNhdMSxxZ9pIHRvc3QgxZ9pc3Rpcm1lbiDDpnZlbCBpc2l5b3Iu
-->
