# 1. Aplicación del CVS-Q

> **Enunciado del problema**: ¿Existe asociación entre el tiempo de exposición a pantallas y la fatiga visual en médicos radiólogos del Departamento de Radiodiagnóstico del Instituto Nacional de Enfermedades Neoplásicas, durante el periodo de julio a octubre de 2025?

> **Objetivo principal**: Evaluar la asociación entre el tiempo de exposición a pantallas y la fatiga visual en médicos radiólogos del Departamento de Radiodiagnóstico del Instituto Nacional de Enfermedades Neoplásicas, durante el periodo de julio a octubre de 2025.

## Estructura del instrumento (encuesta)

16 ítems, cada uno correspondiente a un síntoma visual o extraocular relacionado con el uso prolongado de pantallas.
Los síntomas incluyen: ardor, picazón, sensación de cuerpo extraño, lagrimeo, parpadeo excesivo, enrojecimiento, dolor ocular, pesadez palpebral, sequedad, visión borrosa, visión doble, dificultad para enfocar de cerca, fotofobia, halos de colores, sensación de empeoramiento visual y cefalea.

## Escalas de respuesta
Para cada ítem, el participante responde dos dimensiones:

1. Frecuencia (¿con qué frecuencia experimenta el síntoma?):
- 0 = Nunca
- 1 = Ocasionalmente
- 2 = A menudo / Siempre

2. Intensidad (¿qué tan intenso es el síntoma?):
- 0 = Ninguno (solo si la frecuencia es “Nunca”)
- 1 = Moderado
- 2 = Intenso

Nota: Si la frecuencia es “Nunca”, la intensidad se codifica automáticamente como 0, aunque no se pregunte explícitamente.

# 2. Cálculo del puntaje de severidad

Para cada ítem, se calcula un puntaje de severidad individual mediante la fórmula:

$$Severidad = Frecuencia × Intensidad $$

Este producto genera valores posibles de: 0, 1, 2 o 4

# 3. Interpretación del resultado

Este punto de corte ha sido validado en múltiples estudios, incluyendo los realizados en Perú por Huapaya, 2020 y Aguilar-Ramírez & Meneses, 2022:

1. Puntaje total ≥ 6 puntos: se considera que el participante presenta síndrome visual informático (SVI).

Además, se puede clasificar la severidad del SVI según el puntaje total:

1. Leve: 6–10 puntos
2. Moderado: 11–20 puntos
3. Severo: >20 puntos

Esta categorización se usa en varios estudios peruanos, aunque no está estandarizada oficialmente en el instrumento original.

# 4. Análisis estadístico (según estudios que lo han usado)

## Análisis descriptivo

1. **Prevalencia del SVI**: proporción de participantes con puntaje $≥6$.

2. **Frecuencia de síntomas individuales**: porcentaje de participantes que reportan cada síntoma con frecuencia $≥1$.

3. **Medidas de tendencia central**: media, mediana y desviación estándar del puntaje total. Especialmente útil cuando los datos no son normales, como en Alhasan & Aalam, 2022.

## Análisis inferencial

1. **Asociación con variables independientes** (edad, tiempo de exposición, uso de lentes, pausas, etc.):
   - Chi-cuadrado o Fisher exacto para variables categóricas.
   - t de Student o Mann-Whitney U para comparar puntajes medios entre grupos.
   - Regresión logística para identificar factores asociados a la presencia de SVI (variable dicotómica: sí/no).
   - Regresión lineal o de Poisson si se usa el puntaje total como variable continua o de recuento.
   - **Confiabilidad del instrumento** (en estudios de validación)
     - Alfa de Cronbach: para consistencia interna (valores >0,70 aceptables; en Perú se reportó 0,939).
     - Coeficiente de correlación intraclase (CCI): para estabilidad temporal (test-retest), con valores >0,75 considerados buenos.
3. **Interpretación del resultado**
   - Puntaje total ≥ 6 puntos: se considera que el participante presenta síndrome visual informático (SVI).
   - (Este punto de corte ha sido validado en múltiples estudios, incluyendo los realizados en Perú por Huapaya, 2020 y Aguilar-Ramírez & Meneses, 2022).
   - Además, se puede clasificar la severidad del SVI según el puntaje total:
     - Leve: 6–10 puntos
     - Moderado: 11–20 puntos
     - Severo: >20 puntos
   - (Esta categorización se usa en varios estudios peruanos, aunque no está estandarizada oficialmente en el instrumento original).


4. **Análisis estadístico** (según estudios que lo han usado)
   - **Análisis descriptivo**
     - Prevalencia del SVI: proporción de participantes con puntaje ≥6.
     - Frecuencia de síntomas individuales: porcentaje de participantes que reportan cada síntoma con frecuencia ≥1.
     - Medidas de tendencia central: media, mediana y desviación estándar del puntaje total (especialmente útil cuando los datos no son normales, como en Alhasan & Aalam, 2022).

   - **Análisis inferencial**
     - Asociación con variables independientes (edad, tiempo de exposición, uso de lentes, pausas, etc.):
       - Chi-cuadrado o Fisher exacto para variables categóricas.
       - t de Student o Mann-Whitney U para comparar puntajes medios entre grupos.
       - Regresión logística para identificar factores asociados a la presencia de SVI (variable dicotómica: sí/no).
       - Regresión lineal o de Poisson si se usa el puntaje total como variable continua o de recuento.
   - **Confiabilidad del instrumento** (en estudios de validación)
     - Alfa de Cronbach: para consistencia interna (valores >0,70 aceptables; en Perú se reportó 0,939).
     - Coeficiente de correlación intraclase (CCI): para estabilidad temporal (test-retest), con valores >0,75 considerados buenos.

# Environment packages

The following packages are installed in the project's virtual environment (output of `pip freeze`):

```
asttokens==3.0.0
colorama==0.4.6
comm==0.2.3
debugpy==1.8.17
decorator==5.2.1
et_xmlfile==2.0.0
executing==2.2.1
iniconfig==2.1.0
ipykernel==6.30.1
ipython==9.5.0
ipython_pygments_lexers==1.1.1
jedi==0.19.2
jupyter_client==8.6.3
jupyter_core==5.8.1
matplotlib-inline==0.1.7
narwhals==2.5.0
nest-asyncio==1.6.0
numpy==2.3.3
openpyxl==3.1.5
packaging==25.0
pandas==2.3.2
parso==0.8.5
platformdirs==4.4.0
pluggy==1.6.0
prompt_toolkit==3.0.52
psutil==7.1.0
pure_eval==0.2.3
Pygments==2.19.2
pyreadstat==1.3.1
pytest==8.4.2
python-dateutil==2.9.0.post0
pytz==2025.2
pywin32==311
pyzmq==27.1.0
six==1.17.0
stack-data==0.6.3
tornado==6.5.2
traitlets==5.14.3
tzdata==2025.2
wcwidth==0.2.14
```
