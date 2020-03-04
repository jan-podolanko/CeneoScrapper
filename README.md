# CeneoScrapper
## Etap 1 - pobranie składowych pojedynczej opinii
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div.reviewer-name-line
- rekomendacja: div.product-review-summary > em
- gwiazdki: span.review-score-count
- potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.review-time > time["datetime"] - pierwszy element listy
- data zakupu: span.review-time > time["datetime"] - drugi element listy(o ile istnieje)
- przydatna: span[id=^votes-yes]
    lub        button.vote-yes["data-total-vote"]
    lub        button.vote-yes > span
- nieprzydatna: span[id=^votes-no]
    lub        button.vote-no["data-total-vote"]
    lub        button.vote-no > span
- treść: p.product-review-body
- wady: div.cons-cell > ul
- zalety: div.pros-cell > ul
