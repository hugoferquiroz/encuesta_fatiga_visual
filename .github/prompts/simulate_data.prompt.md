---
mode: agent
---

> **Objetivo principal**: Simular una data que muestre la asociación entre el tiempo de exposición a pantallas y la fatiga visual en médicos radiólogos

Muestra: 60 médicos radiólogos del Departamento de Radiodiagnóstico del Instituto Nacional de Enfermedades Neoplásicas, durante el periodo de julio a octubre de 2025.

# Variables demográficas y laborales

La encuesta tiene las siguientes preguntas y opciones de respuesta:

1. 'edad': 
    - media 34, desviacion estandar 6,
2. 'sexo': 
    - opciones: {1: Masculino, 0: Femenino}
    - 50% de cada uno
3. 'estado_civil': 
    - opciones: {0: Soltero, 1: Casado, 2: Divorciado, 3: Viudo}
    - 40% soltero, 40% casado, 10% divorciado, 10% viudo
4. 'experiencia_radiologia': 
    - media 4.3, desviacion estandar 3.2, minimo 1, maximo 15
5. 'ingresos_mensuales': 
    - opciones: {0: Menos de $3,000, 1: $3,001 - $5,000, 2: $5,001 - $7,000, 3: Más de $7,000}
    - 10% menos de $3,000, 30% entre $3,001 y $5,000, 50% entre $5,001 y $7,000, 10% más de $7,000
6. 'condiciones_oculares':
    - opciones: {1:si, 0:no}
    - 60% si, 40% no
7. 'lentes':
    - opciones: {1:si, 0:no}
    - 60% si, 40% no
8. 'iluminacion':
    - opciones: {1: Adecuada, 0: Inadecuada}
    - 80% adecuada, 20% inadecuada
9. 'tiempo_de_exposicion':
    - media 12, desviacion estandar 4, minimo 8, maximo 16
10. 'frecuencia_de_pausas':
    - opciones: {1: Frecuente, 2: Ocasional, 0: Nulo}
    - 50% frecuente, 30% ocasional, 20% nulo
11. 'duracion_de_jornada':
    - media 12, desviacion estandar 4, minimo 6, maximo 16
12. 'uso_de_dispositivos':
    - opciones: {0: menos de 1 hora, 1: 1 - 2 h, 2: 2 - 4 h, 3: Mayor de 4h}
    - 5% menos de 1h, 15% 1-2h, 10% 2-4h, 70% mayor de 4h
13. 'distancia_hacia_el_monitor':
    - opciones: {0: Menor de 30 cm, 1: 30 - 60  cm, 2: Mayor de 60 cm}
    - 20% menor de 30 cm, 60% entre 30 y 60 cm, 20% mayor de 60 cm

# Estructura del instrumento de fatiga visual

Para evaluar la fatiga visual, se utiliza un cuestionario de 16 ítems, cada uno correspondiente a un síntoma visual o extraocular relacionado con el uso prolongado de pantallas. Los síntomas incluyen: 

["ardor", "picor", "sensacion_cuerpo_extraño", "lagrimeo", "parpadeo_excesivo", "enrojecimiento_ocular", "dolor_ocular",
"pesadez_parpados", "sequedad", "vision_borrosa", "vision_doble",
"dificultad_al_enfocar", "aumento_sensiblidad_luz",
"halos_de_colores", "sensacion_de_ver_peor", "dolor_de_cabeza"]

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

## Cálculo del puntaje de severidad

Para cada ítem, se calcula un puntaje de severidad individual mediante la fórmula:

$$Severidad = Frecuencia × Intensidad $$

Este producto genera valores posibles de: 0, 1, 2 o 4

## 3. Interpretación del resultado

1. Puntaje total ≥ 6 puntos: se considera que el participante presenta síndrome visual informático (SVI).

Además, se puede clasificar la severidad del SVI según el puntaje total:

1. Leve: 6–10 puntos
2. Moderado: 11–20 puntos
3. Severo: >20 puntos

# Simulación de datos
Generar una data simulada para 60 médicos radiólogos, asegurando que al menos el 70% presenten SVI (puntaje total ≥ 6). La severidad del SVI debe distribuirse de la siguiente manera: 50% leve, 30% moderado y 20% severo. El resto (30%) no debe presentar SVI (puntaje total < 6).

Asegurar que las variables demográficas y laborales tengan las distribuciones especificadas anteriormente.

# Relación entre tiempo de exposición y fatiga visual
Asegurar que exista una correlación positiva entre el tiempo de exposición a pantallas ('tiempo_de_exposicion') y el puntaje total de fatiga visual. Es decir, a mayor tiempo de exposición, mayor puntaje de fatiga visual.

Genera la data en un DataFrame de pandas y guarda el archivo como "df_models_synthetic.csv" en la carpeta "data/2_processed".

