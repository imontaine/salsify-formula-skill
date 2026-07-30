# Salsify Time Zone Names for Formulas

Source: Salsify "Time Zone Names for Formulas"
Source last modified: May 27, 2025
Extracted: July 30, 2026

This reference contains all **149 accepted time-zone names** across **33 UTC offsets** documented by Salsify. Use the name exactly as shown, including any parenthetical text.

**Related functions:** [`TIME_IN_TIMEZONE`](salsify-functions.md#time-in-timezone) | [`NOW`](salsify-functions.md#now) | [`FORMAT_DATETIME`](salsify-functions.md#format-datetime)

> **Signature note:** The May 2025 article describes these names for functions that accept a time-zone parameter and mentions `NOW()`. The newer June 2026 cheat sheet explicitly documents time-zone parameters for `TIME_IN_TIMEZONE`, while its `NOW` signature only displays an optional format parameter. Use these names only in a parameter position accepted by the current formula editor.

## Example

The current Salsify cheat sheet uses two names from this table in its `TIME_IN_TIMEZONE` example:

```text
TIME_IN_TIMEZONE('2019-08-28T01:56:41+00:00','Eastern Time (US & Canada)','Lisbon')
```

**Documented output:** `2019-08-28T06:56:41+00:00`

## Accepted time-zone names

| UTC offset | Accepted Salsify time-zone names |
|---|---|
| UTC -11:00 | `American Samoa`<br>`International Date Line West`<br>`Midway Island` |
| UTC -10:00 | `Hawaii` |
| UTC -09:00 | `Alaska` |
| UTC -08:00 | `Pacific Time (US & Canada)`<br>`Tijuana` |
| UTC -07:00 | `Arizona`<br>`Chihuahua`<br>`Mazatlan`<br>`Mountain Time (US & Canada)` |
| UTC -06:00 | `Central America`<br>`Central Time (US & Canada)`<br>`Guadalajara`<br>`Mexico City`<br>`Monterrey`<br>`Saskatchewan` |
| UTC -05:00 | `Bogota`<br>`Eastern Time (US & Canada)`<br>`Indiana (East)`<br>`Lima`<br>`Quito` |
| UTC -04:00 | `Atlantic Time (Canada)`<br>`Caracas`<br>`Georgetown`<br>`La Paz`<br>`Santiago` |
| UTC -03:30 | `Newfoundland` |
| UTC -03:00 | `Brasilia`<br>`Buenos Aires`<br>`Greenland`<br>`Montevideo` |
| UTC -02:00 | `Mid-Atlantic` |
| UTC -01:00 | `Azores`<br>`Cape Verde Is.` |
| UTC +00:00 | `Casablanca`<br>`Dublin`<br>`Edinburgh`<br>`Lisbon`<br>`London`<br>`Monrovia` |
| UTC +01:00 | `Amsterdam`<br>`Belgrade`<br>`Berlin`<br>`Bern`<br>`Bratislava`<br>`Brussels`<br>`Budapest`<br>`Copenhagen`<br>`Ljubljana`<br>`Madrid`<br>`Paris`<br>`Prague`<br>`Rome`<br>`Sarajevo`<br>`Skopje`<br>`Stockholm`<br>`Vienna`<br>`Warsaw`<br>`West Central Africa`<br>`Zagreb`<br>`Zurich` |
| UTC +02:00 | `Athens`<br>`Bucharest`<br>`Cairo`<br>`Harare`<br>`Helsinki`<br>`Jerusalem`<br>`Kaliningrad`<br>`Kyiv`<br>`Pretoria`<br>`Riga`<br>`Sofia`<br>`Tallinn`<br>`Vilnius` |
| UTC +03:00 | `Baghdad`<br>`Istanbul`<br>`Kuwait`<br>`Minsk`<br>`Moscow`<br>`Nairobi`<br>`Riyadh`<br>`St. Petersburg`<br>`Volgograd` |
| UTC +03:30 | `Tehran` |
| UTC +04:00 | `Abu Dhabi`<br>`Baku`<br>`Muscat`<br>`Samara`<br>`Tbilisi`<br>`Yerevan` |
| UTC +04:30 | `Kabul` |
| UTC +05:00 | `Ekaterinburg`<br>`Islamabad`<br>`Karachi`<br>`Tashkent` |
| UTC +05:30 | `Chennai`<br>`Kolkata`<br>`Mumbai`<br>`New Delhi`<br>`Sri Jayawardenepura` |
| UTC +05:45 | `Kathmandu` |
| UTC +06:00 | `Almaty`<br>`Astana`<br>`Dhaka`<br>`Urumqi` |
| UTC +06:30 | `Rangoon` |
| UTC +07:00 | `Bangkok`<br>`Hanoi`<br>`Jakarta`<br>`Krasnoyarsk`<br>`Novosibirsk` |
| UTC +08:00 | `Beijing`<br>`Chongqing`<br>`Hong Kong`<br>`Irkutsk`<br>`Kuala Lumpur`<br>`Perth`<br>`Singapore`<br>`Taipei`<br>`Ulaanbaatar` |
| UTC +09:00 | `Osaka`<br>`Sapporo`<br>`Seoul`<br>`Tokyo`<br>`Yakutsk` |
| UTC +09:30 | `Adelaide`<br>`Darwin` |
| UTC +10:00 | `Brisbane`<br>`Canberra`<br>`Guam`<br>`Hobart`<br>`Melbourne`<br>`Port Moresby`<br>`Sydney`<br>`Vladivostok` |
| UTC +11:00 | `Magadan`<br>`New Caledonia`<br>`Solomon Is.`<br>`Srednekolymsk` |
| UTC +12:00 | `Auckland`<br>`Fiji`<br>`Kamchatka`<br>`Marshall Is.`<br>`Wellington` |
| UTC +12:45 | `Chatham Is.` |
| UTC +13:00 | `Nuku'alofa`<br>`Samoa`<br>`Tokelau Is.` |

## Alphabetical index

- `Abu Dhabi` ? UTC +04:00
- `Adelaide` ? UTC +09:30
- `Alaska` ? UTC -09:00
- `Almaty` ? UTC +06:00
- `American Samoa` ? UTC -11:00
- `Amsterdam` ? UTC +01:00
- `Arizona` ? UTC -07:00
- `Astana` ? UTC +06:00
- `Athens` ? UTC +02:00
- `Atlantic Time (Canada)` ? UTC -04:00
- `Auckland` ? UTC +12:00
- `Azores` ? UTC -01:00
- `Baghdad` ? UTC +03:00
- `Baku` ? UTC +04:00
- `Bangkok` ? UTC +07:00
- `Beijing` ? UTC +08:00
- `Belgrade` ? UTC +01:00
- `Berlin` ? UTC +01:00
- `Bern` ? UTC +01:00
- `Bogota` ? UTC -05:00
- `Brasilia` ? UTC -03:00
- `Bratislava` ? UTC +01:00
- `Brisbane` ? UTC +10:00
- `Brussels` ? UTC +01:00
- `Bucharest` ? UTC +02:00
- `Budapest` ? UTC +01:00
- `Buenos Aires` ? UTC -03:00
- `Cairo` ? UTC +02:00
- `Canberra` ? UTC +10:00
- `Cape Verde Is.` ? UTC -01:00
- `Caracas` ? UTC -04:00
- `Casablanca` ? UTC +00:00
- `Central America` ? UTC -06:00
- `Central Time (US & Canada)` ? UTC -06:00
- `Chatham Is.` ? UTC +12:45
- `Chennai` ? UTC +05:30
- `Chihuahua` ? UTC -07:00
- `Chongqing` ? UTC +08:00
- `Copenhagen` ? UTC +01:00
- `Darwin` ? UTC +09:30
- `Dhaka` ? UTC +06:00
- `Dublin` ? UTC +00:00
- `Eastern Time (US & Canada)` ? UTC -05:00
- `Edinburgh` ? UTC +00:00
- `Ekaterinburg` ? UTC +05:00
- `Fiji` ? UTC +12:00
- `Georgetown` ? UTC -04:00
- `Greenland` ? UTC -03:00
- `Guadalajara` ? UTC -06:00
- `Guam` ? UTC +10:00
- `Hanoi` ? UTC +07:00
- `Harare` ? UTC +02:00
- `Hawaii` ? UTC -10:00
- `Helsinki` ? UTC +02:00
- `Hobart` ? UTC +10:00
- `Hong Kong` ? UTC +08:00
- `Indiana (East)` ? UTC -05:00
- `International Date Line West` ? UTC -11:00
- `Irkutsk` ? UTC +08:00
- `Islamabad` ? UTC +05:00
- `Istanbul` ? UTC +03:00
- `Jakarta` ? UTC +07:00
- `Jerusalem` ? UTC +02:00
- `Kabul` ? UTC +04:30
- `Kaliningrad` ? UTC +02:00
- `Kamchatka` ? UTC +12:00
- `Karachi` ? UTC +05:00
- `Kathmandu` ? UTC +05:45
- `Kolkata` ? UTC +05:30
- `Krasnoyarsk` ? UTC +07:00
- `Kuala Lumpur` ? UTC +08:00
- `Kuwait` ? UTC +03:00
- `Kyiv` ? UTC +02:00
- `La Paz` ? UTC -04:00
- `Lima` ? UTC -05:00
- `Lisbon` ? UTC +00:00
- `Ljubljana` ? UTC +01:00
- `London` ? UTC +00:00
- `Madrid` ? UTC +01:00
- `Magadan` ? UTC +11:00
- `Marshall Is.` ? UTC +12:00
- `Mazatlan` ? UTC -07:00
- `Melbourne` ? UTC +10:00
- `Mexico City` ? UTC -06:00
- `Mid-Atlantic` ? UTC -02:00
- `Midway Island` ? UTC -11:00
- `Minsk` ? UTC +03:00
- `Monrovia` ? UTC +00:00
- `Monterrey` ? UTC -06:00
- `Montevideo` ? UTC -03:00
- `Moscow` ? UTC +03:00
- `Mountain Time (US & Canada)` ? UTC -07:00
- `Mumbai` ? UTC +05:30
- `Muscat` ? UTC +04:00
- `Nairobi` ? UTC +03:00
- `New Caledonia` ? UTC +11:00
- `New Delhi` ? UTC +05:30
- `Newfoundland` ? UTC -03:30
- `Novosibirsk` ? UTC +07:00
- `Nuku'alofa` ? UTC +13:00
- `Osaka` ? UTC +09:00
- `Pacific Time (US & Canada)` ? UTC -08:00
- `Paris` ? UTC +01:00
- `Perth` ? UTC +08:00
- `Port Moresby` ? UTC +10:00
- `Prague` ? UTC +01:00
- `Pretoria` ? UTC +02:00
- `Quito` ? UTC -05:00
- `Rangoon` ? UTC +06:30
- `Riga` ? UTC +02:00
- `Riyadh` ? UTC +03:00
- `Rome` ? UTC +01:00
- `Samara` ? UTC +04:00
- `Samoa` ? UTC +13:00
- `Santiago` ? UTC -04:00
- `Sapporo` ? UTC +09:00
- `Sarajevo` ? UTC +01:00
- `Saskatchewan` ? UTC -06:00
- `Seoul` ? UTC +09:00
- `Singapore` ? UTC +08:00
- `Skopje` ? UTC +01:00
- `Sofia` ? UTC +02:00
- `Solomon Is.` ? UTC +11:00
- `Srednekolymsk` ? UTC +11:00
- `Sri Jayawardenepura` ? UTC +05:30
- `St. Petersburg` ? UTC +03:00
- `Stockholm` ? UTC +01:00
- `Sydney` ? UTC +10:00
- `Taipei` ? UTC +08:00
- `Tallinn` ? UTC +02:00
- `Tashkent` ? UTC +05:00
- `Tbilisi` ? UTC +04:00
- `Tehran` ? UTC +03:30
- `Tijuana` ? UTC -08:00
- `Tokelau Is.` ? UTC +13:00
- `Tokyo` ? UTC +09:00
- `Ulaanbaatar` ? UTC +08:00
- `Urumqi` ? UTC +06:00
- `Vienna` ? UTC +01:00
- `Vilnius` ? UTC +02:00
- `Vladivostok` ? UTC +10:00
- `Volgograd` ? UTC +03:00
- `Warsaw` ? UTC +01:00
- `Wellington` ? UTC +12:00
- `West Central Africa` ? UTC +01:00
- `Yakutsk` ? UTC +09:00
- `Yerevan` ? UTC +04:00
- `Zagreb` ? UTC +01:00
- `Zurich` ? UTC +01:00
