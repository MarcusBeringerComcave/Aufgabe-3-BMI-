def bmi(gewicht, groesse):
  bmi = gewicht / groesse**2
  if bmi < 10:
    print("Bitte überprüfen Sie Ihre Eingabe")
  elif bmi >= 10 and bmi < 15:
    print("Sie leiden an Magersucht")
  elif bmi >= 15 and bmi < 20:
    print("Sie leiden unter Untergewicht")
  elif bmi >= 20 and bmi < 25:
    print("Sie haben ein Normalgewicht")
  elif bmi >= 25 and bmi < 30:
    print("Sie leiden an Übergewicht")
  elif bmi >= 30 and bmi < 40:
    print("Sie leiden an Fettsucht")
  elif bmi >= 40 and bmi < 50:
    print("Sie leiden an morbider Fettsucht")
  else:
    print("Bitte überprüfen Sie Ihre Eingabe")
  
while True:  
  gewicht = float(input("Bitte geben Sie ihr Gewicht in kg ein: "))
  groesse = float(input("Bitte geben Sie ihre Größe in m ein: "))
  bmi(gewicht, groesse)