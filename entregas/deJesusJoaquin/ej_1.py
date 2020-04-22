import numpy as np
import pandas as pd

### Ejercicio 1  - Probabilidad condicional #####

## Se puede calcular todo lo que se pide sin necesidad de usar el teo de bayes


df=pd.read_csv('student-mat.csv')
print(df.head())

##########################
## Sin teorema de Bayes ##
##########################

## Primero debo saber cuantos alumnos sacaron grade mayor a 12
grade_mayor_12_bool = df['G3'] >= 12

df_grade_mayor_12 = df[grade_mayor_12_bool]

total_grade_mayor_12 = len(df_grade_mayor_12) # total de casos de alumnos con grade mayor a 12

# sobre df_grade_mayor_12, debo calcular calcular cuantos faltaron menos de 3 veces
df_menos_de_3_bool = df_grade_mayor_12['absences'] < 3
df_menos_de_3 = df_grade_mayor_12[df_menos_de_3_bool] ## dataframe con todos los que faltaron menos de 3 y sacaron mas de 12

n_menos_de_3 = len(df_menos_de_3)



# probabilidad
pp = float(n_menos_de_3)/total_grade_mayor_12
print("SIN TEOREMA DE BAYES")
print("La probabilidad que se pide es %i/%i = %.2f" % (n_menos_de_3, total_grade_mayor_12, pp))
print("\n")

##########################
## Con teorema de Bayes ##
##########################

# B = faltar menos de 3
# A = sacar mas de 60%
# Necesito P(B|A) = P(A|B) * pB/pA

n_total = len(df) # cantidad total de alumnos
n_grade_mayor_12 = len(df_grade_mayor_12) # cantidad de alumnos que sacaron mayor o igual a 12

df_menos_de_3_bool = df['absences'] < 3 #a diferencia de antes, ahora lo calculo sobre el conjunto total de alumnos, no sobre aquellos con mayor a 12
df_menos_de_3 = df[df_menos_de_3_bool]

n_menos_de_3 = len(df_menos_de_3)

pB = float(n_menos_de_3)/n_total #proba de faltar menos de 3
pA = float(total_grade_mayor_12) / n_total #proba de sacar mas de 12

# Ahora a calcular P(A|B)

df_condicionada = df_menos_de_3[df_menos_de_3['G3'] >= 12]
pA_B = float(len(df_condicionada))/ len(df_menos_de_3)
pB_A = pA_B * pB/pA # Teorema Bayes

print("CON TEOREMA DE BAYES")
print("La probabilidad que se pide es P(B|A) = P(A|B) * pB/pA = %.2f * %.2f/%.2f = %.2f" % (pA_B, pB, pA, pB_A ))
print("\n")

print("Ambas coinciden? : %s" % (pp == pB_A))
