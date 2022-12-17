from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tehdas import Tehdas


def main():
    
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()
        if vastaus not in ("a", "b", "c"):
            break

        tehdas = Tehdas()
        
        peli = tehdas.luo_peli(vastaus)
        peli.pelaa()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        
        

if __name__ == "__main__":
    main()
