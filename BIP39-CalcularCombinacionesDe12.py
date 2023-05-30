#!/bin/bash

# Pongo a disposición pública este script bajo el término de "software de dominio público".
# Puedes hacer lo que quieras con él porque es libre de verdad; no libre con condiciones como las licencias GNU y otras patrañas similares.
# Si se te llena la boca hablando de libertad entonces hazlo realmente libre.
# No tienes que aceptar ningún tipo de términos de uso o licencia para utilizarlo o modificarlo porque va sin CopyLeft.

# ----------
# Script de NiPeGun para calcular todas las combinaciones posibles de las palabras leidas en un archivo
#
# Ejecución remota:
#   curl -s x | bash
# ----------

def fCombinarPalabras(words, vTotalArupadas, combination=[], combinations=set()):
  if len(combination) == vTotalArupadas:
    combinations.add(tuple(combination))
    return

  for word in words:
    if word not in combination:
      fCombinarPalabras(words, vTotalArupadas, combination + [word], combinations)
    return combinations


def fLeerPalabrasDeArchivo(filename):
  words = []
  with open(filename, 'r') as file:
    for line in file:
      line = line.strip()
      line_words = line.split()
      words.extend(line_words)
  return words

# Ejemplo de uso
vArchivo = '12Palabras.txt'
words = fLeerPalabrasDeArchivo(vArchivo)

vTotalArupadas = 12
all_combinations = fCombinarPalabras(words, vTotalArupadas)

for combination in all_combinations:
  print(' '.join(combination))
