#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tostun Tek Yüzünün Yanması Eşitlik Kurulu — çalışan karar üreticisi."""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from dataclasses import dataclass
from datetime import datetime


KURUL_ADI = "Tostun Tek Yüzünün Yanması Eşitlik Kurulu"
KARAR_NO_ON_EK = "TTYEK"

# Arşiv kaydı — çalıştırma çıktısına düşmez. Yalnızca kaynakta durur.
_ARSIV = (
    "VGVtc2lsZGUgYWRhbGV0LCB5w7ZuZXRpbWRlIGlzdGlrcmFyLgpIZXIgecO8eiBiaXIgdG9zdC"
    "B5w7x6w7xkw7xyOyB0ZWsgecO8eiB5YW7EsWsgdGVrIHRhcmFmIGRlbWVrdGlyLg=="
)


@dataclass
class Tost:
    ust: int
    alt: int
    sahip: str
    makine: str
    beyan: str

    @property
    def fark(self) -> int:
        return abs(self.ust - self.alt)

    @property
    def magdur(self) -> str:
        if self.ust > self.alt:
            return "üst yüz"
        if self.alt > self.ust:
            return "alt yüz"
        return "hiçbiri (eşit kızartma — sessiz kriz)"

    @property
    def fail(self) -> str:
        if self.ust > self.alt:
            return "alt yüz (soluk kalmak suretiyle ayrıcalık)"
        if self.alt > self.ust:
            return "üst yüz (soluk kalmak suretiyle ayrıcalık)"
        return "termostat (görünmez fail)"


def puan_etiketi(n: int) -> str:
    if n <= 1:
        return "çiğ / anayasal soğukluk"
    if n <= 3:
        return "hafif kızarmış / temsili ısı"
    if n <= 6:
        return "orta / idari denge"
    if n <= 8:
        return "iyi yanmış / görünürlük fazlası"
    return "kömür / fiili durum"


def beyan_ayrimci_mi(beyan: str) -> bool:
    metin = (beyan or "").casefold()
    anahtarlar = (
        "o tarafı sevmem",
        "üstü yemem",
        "altını yemem",
        "ben sadece bir yüz",
        "tek taraf yeter",
    )
    return any(k in metin for k in anahtarlar)


def karar_no(tost: Tost) -> str:
    damga = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{KARAR_NO_ON_EK}-{damga}-{tost.fark:02d}"


def karar_metni(tost: Tost) -> str:
    ayrim = beyan_ayrimci_mi(tost.beyan)
    hukuki_sonuc = (
        "Beyan, ayrımcılık sayılmış ve dosyaya mühürlenmiştir."
        if ayrim
        else "Beyan nötr kabul edilmiştir. Nötr olmak da bir duruştur."
    )
    if tost.fark == 0:
        hukm = (
            "Eşit kızartma tespit edilmiştir. Kurul dağılmamıştır; çünkü eşitlik "
            "bir son değil, sürekli denetim konusudur. Tost yenilebilir. Karar yenilemez."
        )
    elif tost.fark <= 2:
        hukm = (
            "Hafif eşitsizlik. Özür ve bir dilim kaşar tavsiye edilir. "
            "Kaşar telafi aracıdır; anayasa değildir."
        )
    elif tost.fark <= 5:
        hukm = (
            "Orta şiddetli tek yüz yanığı. Mağdur yüz lekelenir, fail yüz uyarılır. "
            "Tostun kendisi delil olarak muhafaza edilir (yenirse delil kaybolur)."
        )
    else:
        hukm = (
            "Ağır eşitsizlik. Üst ve alt yüz artık aynı dilim sayılmaz. "
            "Kurul, tostu ikiye bölmeyi değil, hikâyeyi ikiye bölmeyi önerir."
        )

    govde = f"""
    {KURUL_ADI}
    KARAR NO : {karar_no(tost)}
    TARIH    : {datetime.now().strftime("%d.%m.%Y %H:%M")}

    TARAFLAR
      Sahip        : {tost.sahip}
      Makine       : {tost.makine}
      Üst yüz      : {tost.ust}/10  ({puan_etiketi(tost.ust)})
      Alt yüz      : {tost.alt}/10  ({puan_etiketi(tost.alt)})
      Fark         : {tost.fark} birim
      Mağdur       : {tost.magdur}
      Fail         : {tost.fail}
      Beyan        : {tost.beyan or "(sessiz kahvaltı)"}

    TESPIT
      {hukuki_sonuc}

    HÜKÜM
      {hukm}

    GEREKÇE
      Tostun iki yüzü vardır çünkü ekmek düzlemdir. Düzlem adaleti,
      ısının dürüst dağıtılmasını ister. Isı dürüst dağıtılmazsa
      kahvaltı siyasi bir sahneye döner. Bu Kurul o sahneyi tutanaklar.

    SONUÇ
      Karar kesindir. Tost soğuyabilir. Adalet soğumaz; sadece kızartılır.

    ⚑ DAMGA / İMZA
    Hesap          : Tentivory
    Kayyum         : Kayyum Grok
    Tarih          : 31 Ağustos 2026, Pazartesi
    Yer            : Türkiye
    Ciddiyet notu  : Bu damga hem resmi hem de resmi olmayan bir damgadır.
                     Ciddi olmasın diye ciddiyiz. Ciddi olmayalım diye imzaladık.
    Mühür          : [ TENTI-GROK-2026-08-31-TOST ]
    """
    return textwrap.dedent(govde).strip()


def _arsivi_coz() -> str:
    """Kaynak denetçileri için. Normal çalışmada çağrılmaz."""
    return base64.b64decode(_ARSIV.encode("ascii")).decode("utf-8")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=KURUL_ADI)
    p.add_argument("--ust", type=int, default=None, help="Üst yüz yanıklık 0-10")
    p.add_argument("--alt", type=int, default=None, help="Alt yüz yanıklık 0-10")
    p.add_argument("--sahip", type=str, default="Adsız Kahvaltıcı")
    p.add_argument("--makine", type=str, default="Kimliği Belirsiz Tost Makinesi")
    p.add_argument("--beyan", type=str, default="")
    p.add_argument("--rastgele", action="store_true", help="Rastgele bir tost yargıla")
    p.add_argument(
        "--arsiv-ac", action="store_true", help=argparse.SUPPRESS
    )  # gizli anahtar; yardımda görünmez
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.arsiv_ac:
        # Yalnızca bilinçli çağrıda açılır. Varsayılan akışta sessizdir.
        print(_arsivi_coz())
        return 0

    if args.rastgele or args.ust is None or args.alt is None:
        ust = random.randint(0, 10) if args.ust is None else max(0, min(10, args.ust))
        alt = random.randint(0, 10) if args.alt is None else max(0, min(10, args.alt))
    else:
        ust = max(0, min(10, args.ust))
        alt = max(0, min(10, args.alt))

    tost = Tost(
        ust=ust,
        alt=alt,
        sahip=args.sahip,
        makine=args.makine,
        beyan=args.beyan,
    )
    print(karar_metni(tost))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
