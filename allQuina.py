# -------------------------------------
# --- Python para Android (SL4A).
# --- Calcula palpites da Quina,
# --- de acordo com as distribuicoes de cada dezena.
# --- jorgearacaty.
# --- criado em, 31 jul 2014 - 0916.
# --- modificado em, 6 ago 2014 - 1839.
# -------------------------------------

import android
import random 

droid = android.Android()

# -----------------------------
# --- loop principal

while 1:

  z1 = round(random.gammavariate(1.4033,9.6109))
  if z1 < 1: z1 = 1
  if z1 > 80: z1 = 80

  z2 = z1
  while z2 == z1:
    z2 = round(random.weibullvariate(30.6001,2.0633))
  if z2 < 1: z2 = 1
  if z2 > 80: z2 = 80
  
  z3 = z2
  while z3 == z2 or z3 == z1:
    z3 = round(random.weibullvariate(45.5179,3.1123))
  if z3 < 1: z3 = 1
  if z3 > 80: z3 = 80
  
  z4 = z3
  while z4 == z3 or z4 == z2 or z4 == z1:
    z4 = round(random.weibullvariate(59.1316,4.6452))
  if z4 < 1: z4 = 1
  if z4 > 80: z4 = 80

  # inversão da gammavariate.  
  z5 = z4
  while z5 == z4 or z5 == z3 or z5 == z2 or z5 == z1:
    z5 = (81 - round(random.gammavariate(1.4033,9.6109)))
  print(z5)
  if z5 < 1: z5 = 1
  if z5 > 80: z5 = 80

  z1 = "%0.f" % z1
  z2 = "%0.f" % z2
  z3 = "%0.f" % z3    
  z4 = "%0.f" % z4
  z5 = "%0.f" % z5   	
  
  zz = "      "+z1+" - "+z2+" - " \
  +z3+" - "+z4+" - "+z5

  title = '       Palpite da Quina (pdf)'
  
  droid.dialogCreateAlert(title, zz)
  droid.dialogSetPositiveButtonText('Continuar')
  droid.dialogSetNegativeButtonText('Fechar')
  droid.dialogShow()
  
  response = droid.dialogGetResponse().result
  droid.dialogDismiss()

  if not 'which' in response or response['which'] != 'positive': sys.exit()

# -----------------------------
