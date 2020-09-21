def game():
    game_on = True
    tulos_määrä = 0
    while game_on:
        for kysymys, vastaus in kysymykset:
            print(kysymys)
            pelaaja_vastaus = input("Vastauksesi (anna numero, esim 1): ")
            if pelaaja_vastaus == vastaus:
                tulos_määrä += 1
                print("Oikein!")
            else:
                print("Väärin meni!")
        # print tulos_määrä #lopullinen tulos
        print(f"Vastasit oikein {tulos_määrä} kysymykseen {len(kysymykset)}")
        game_on = False

kysymykset = {
    "Maila ja pallo maksavat yhteensä 1,10 euroa. Maila maksaa 1 euron enemmän kuin pallo. Kuinka paljon pallo maksaa?": "5",
    "Jos viidellä laitteella kestää viisi minuuttia valmistaa viisi tuotetta, kuinka kauan sadalta koneelta kestää valmistaa sata tuotetta?": "5",
    "Järvi on täynnä lumpeenlehtiä. Joka päivä lumpeiden peittämä alue kaksinkertaistuu. Jos lumpeet täyttävät koko järven 48 päivässä, kuinka kauan kestää, että järvi on peittynyt puolilleen?": "47"
          }
print("helou, welkom tu our geim.")
player_name = input("Pliis tel me juur neim: ")
print(f"Welcome, {player_name}")