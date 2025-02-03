def calcola_antenna(frequenza_mhz, tipo):
  """
  Calcola la lunghezza dell'antenna in metri in base alla frequenza operativa.
  """
  if tipo == "dipolo":
      lunghezza = 143 / frequenza_mhz  # Mezza onda
      return f"Per un'antenna dipolo la lunghezza totale è di {lunghezza:.2f} metri ({lunghezza/2:.2f} m per braccio)."

  elif tipo == "verticale":
      lunghezza = 71.5 / frequenza_mhz  # Quarto d'onda
      return f"Per un'antenna verticale la lunghezza è di {lunghezza:.2f} metri."

  elif tipo == "yagi":
      lunghezza_elemento_principale = 143 / frequenza_mhz
      lunghezza_director = lunghezza_elemento_principale * 0.9
      lunghezza_reflector = lunghezza_elemento_principale * 1.05
      return (f"Antenna Yagi:\n"
              f"- Elemento principale: {lunghezza_elemento_principale:.2f} m\n"
              f"- Director: {lunghezza_director:.2f} m\n"
              f"- Reflector: {lunghezza_reflector:.2f} m")

  elif tipo == "loop":
      lunghezza_loop = 300 / frequenza_mhz  # Loop a onda intera
      return f"Per un'antenna loop la lunghezza del perimetro è di {lunghezza_loop:.2f} metri."

  else:
      return "Tipo di antenna non riconosciuto. Scegli tra: dipolo, verticale, yagi, loop."

def scegli_modello(frequenza_mhz):
  """
  Suggerisce il miglior modello di antenna in base alla frequenza.
  """
  if frequenza_mhz < 10:
      return "Consigliata un'antenna dipolo o loop per HF (lunghe distanze)."
  elif 10 <= frequenza_mhz < 50:
      return "Consigliata un'antenna Yagi per VHF o una verticale per buona copertura omnidirezionale."
  else:
      return "Consigliata un'antenna verticale per UHF o una Yagi direzionale per massima efficienza."

def materiali_suggeriti(tipo):
  """
  Suggerisce i materiali necessari per la costruzione dell'antenna.
  """
  materiali_base = {
      "dipolo": ["Filo di rame smaltato 2 mm", "Balun 1:1", "Supporti isolanti", "Cavo coassiale RG-58"],
      "verticale": ["Tubo di alluminio", "Unun 9:1", "Radiali da 3 metri", "Palo telescopico"],
      "yagi": ["Boom in alluminio", "Elementi direttivi in acciaio", "Gamma match", "Cavo coassiale RG-213"],
      "loop": ["Cavo in rame da 4 mm", "Condensatore variabile", "Balun 4:1", "Supporti in PVC"]
  }
  return materiali_base.get(tipo, ["Materiali non disponibili per questo tipo di antenna."])

# --- ESEMPIO DI UTILIZZO ---
frequenza = float(input("Inserisci la frequenza operativa in MHz: "))
tipo_antenna = input("Inserisci il tipo di antenna (dipolo, verticale, yagi, loop): ").strip().lower()

print("\n--- RISULTATI ---")
print(calcola_antenna(frequenza, tipo_antenna))
print("\nSuggerimento per il miglior modello:", scegli_modello(frequenza))
print("\nMateriali consigliati:", ", ".join(materiali_suggeriti(tipo_antenna)))
