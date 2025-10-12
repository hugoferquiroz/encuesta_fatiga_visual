---
mode: agent
---

**Objetivo principal**: Modelar la asociación entre el tiempo de exposición a pantallas y la fatiga visual en médicos radiólogos

**Instrucciones**: Utiliza el dataset simulado `df_models_synthetic.csv` para modelar una relación estadisticamente significativa entre el tiempo de exposición a pantallas ('tiempo_de_exposicion') y la presencia de síndrome visual informático ('svi') en médicos radiólogos usando un enfoque estadístico inferencial.

<!-- 1. **Validar el instrumento**: Usar el alpha de Cronbach para validar la consistencia interna del cuestionario que mide el síndrome visual informático. Documentar los resultados y explicar su significado. Para eso vas a usar las columnas:  ["ardor", "picor", "sensacion_cuerpo_extraño", "lagrimeo", "parpadeo_excesivo", "enrojecimiento_ocular", "dolor_ocular",
"pesadez_parpados", "sequedad", "vision_borrosa", "vision_doble", "dificultad_al_enfocar", "aumento_sensiblidad_luz", "halos_de_colores", "sensacion_de_ver_peor", "dolor_de_cabeza"]. -->

**RESTRICCIONES IMPORTANTES**:
Excluir también puntaje_sindrome_visual_informatico y severidad_svi.
Usar solo Python para todo el análisis.
Usar TODO el dataset para el modelado (no dividir en train/test).

**VARIABLES DISPONIBLES PARA MODELADO**:
Demográficas: edad, sexo, estado_civil, ingresos_mensuales
Laborales: experiencia_radiologia, tiempo_de_exposicion, duracion_de_jornada
Condiciones y hábitos: condiciones_oculares, lentes, iluminacion, frecuencia_de_pausas, uso_de_dispositivos, distancia_hacia_el_monitor
Variable objetivo: svi (variable binaria: 0 = sin SVI, 1 = con SVI)

**TAREAS A EJECUTAR**:

1. Análisis de asociación bivariada
Chi-cuadrado para variables categóricas
t-test o Mann-Whitney para variables continuas

Detectar multicolinealidad mediante matriz de correlación sin eliminar la columna que estamos investigando que es 'tiempo_de_exposicion' y VIF
Identificar variables candidatas significativas (p < 0.05 o p < 0.10)
Generar visualizaciones relevantes

2. MODELADO ESTADÍSTICO
Ajustar los siguientes modelos usando TODO el dataset:

a) Regresión Logística Simple

Modelos univariados para cada predictor
Reportar OR, IC 95%, p-valores

b) Regresión Logística Multivariada

Modelo completo con todas las variables candidatas
Modelo reducido (backward elimination o stepwise)
Reportar OR ajustados, IC 95%, p-valores
Evaluar bondad de ajuste (pseudo R²)
Analizar residuos y valores influyentes

c) Modelos Alternativos (opcional)

Regresión de Poisson modificada
Modelos aditivos generalizados (GAM) si hay no-linealidad

3. VALIDACIÓN Y DIAGNÓSTICO

Verificar supuestos del modelo:

Linealidad en el logit
Ausencia de multicolinealidad excesiva (VIF < 5)
Puntos influyentes (distancia de Cook)

4. INTERPRETACIÓN CAUSAL

Identificar factores de riesgo significativos (OR > 1) y protectores (OR < 1)
Interpretar magnitud de efectos (ORs ajustados)
Analizar interacciones relevantes entre variables

Discutir plausibilidad causal considerando:
    - Temporalidad
    - Fuerza de asociación
    - Consistencia con literatura   
    - Plausibilidad biológica/ocupacional

OUTPUT ESPERADO:
Tabla descriptiva por grupos (SVI=0 vs SVI=1)
Tabla de análisis bivariado con p-valores
Tabla de coeficientes del modelo final con OR, IC 95% y p-valores
Visualizaciones: forest plot de ORs, curva ROC
Interpretación causal de los principales factores de riesgo
Recomendaciones prácticas para prevención del SVIcontinua.