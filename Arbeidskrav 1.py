# Arbeidskrav 1


FS_EL = 5000    # EL bil forsikring pr/år
DB_EL = 0.2     # Drivstoffbruk kWh/km
SP = 2          # Strømpris ved hjemmeladning kr/kWh
BA_EL = 0.1     # Bomavgift EL bil kr/km 


FS_BS = 7500    # Bensin bil forsikring pr/år
DB_BS = 1       # Drivstoffbruk bensinbil kr/km
BA_BS = 0.3     # Bomavgift bensinbil kr/km


TFA = 8.38      # Trafikkforsikringsavgift pr/dag
KM = 16000      # Kjørte km/år
ÅR = 365        # Dager i år 

#Bensin bil

Drivstoff_år = DB_BS*KM # Kostnad for drivstoff per år
Bomavgift_år = BA_BS*KM # Kostnad for bom per år 
TFA_år = TFA*ÅR # Trafikkforsikringsavift per år
print ("Kostnad bensin bil pr.år: ", Drivstoff_år + Bomavgift_år + TFA_år + FS_BS)


# EL bil

Drivstoff_km_el = DB_EL*KM # Dristofforbruk per år
Kost_ladning = Drivstoff_km_el*SP # Kostnad for drivstoff per år 
Bomavgift_år_el = BA_EL*KM # Kostnad bom per år 

print ("Kostnad el bil pr.år: ", Kost_ladning + Bomavgift_år_el + TFA_år + FS_EL)


print ("Differanse bensin vs el:", (Drivstoff_år + Bomavgift_år + TFA_år + FS_BS)-(Kost_ladning + Bomavgift_år_el + TFA_år + FS_EL))
