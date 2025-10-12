---
mode: agent
---

**Objetivo**: Generar estadísticas descriptivas y visualizaciones para el conjunto de datos utilizando Python y bibliotecas como pandas, matplotlib y seaborn.

**Instrucciones**:
1. Cargar el conjunto de datos desde la ruta especificada: 'data\2_processed\df_models_synthetic.csv'.
2. Identificar y describir las variables en el conjunto de datos, incluyendo si son numéricas o categóricas, y proporcionar las etiquetas para las variables categóricas.
3. Analisis univariado:
   3.1 Calcular estadísticas descriptivas básicas para las variables numéricas (media, mediana, desviación estándar, valores mínimos y máximos). Guardar estos resultados en un archivo CSV en 'stats/descriptive_stats.csv'.
   3.2 Calcular frecuencias y proporciones para las variables categóricas. Guardar estos resultados en un archivo CSV en 'stats/categorical_stats.csv'.
   3.3 Generar visualizaciones  adecuadas para cada variable:
        - Histogramas para variables numéricas.
        - Gráficos de barras para variables categóricas.
   3.4 Guardar las visualizaciones en un directorio específico: 'output_graphs/univariado'.
4. Analisis bivariado: Comprobar las relaciones entre las otras variables y 'svi' (variable objetivo).
   4.1 Calcular correlaciones entre variables numéricas y guardar los resultados en 'stats/correlation_matrix.csv'.
   4.2 Generar un mapa de calor para visualizar la matriz de correlación y guardarlo en 'output_graphs/bivariado/correlation_heatmap.png'.
   4.3 Crear gráficos de dispersión, violin y barras para pares seleccionados de variables numéricas y guardarlos en 'output_graphs/bivariado'.
5. Asegurarse de que todo el código esté bien documentado y comentado para facilitar la comprensión.

**Notas adiciones**
- Para los graficos usa una paleta de colores de algun journal cientifico de medicina
- Si las carpetas a las que exportas los graficos o estadisticas no existen, crealas.

**Variables en el conjunto de datos**:

1. 'edad': variable numérica 
2. 'sexo': variable categórica
    - etiquetas: {1: Masculino, 0: Femenino}
3. 'estado_civil': variable categórica
    - etiquetas: {0: Soltero, 1: Casado, 2: Divorciado, 3: Viudo}
4. 'experiencia_radiologia': variable numérica 
5. 'ingresos_mensuales': variable categórica
    - etiquetas: {0: Menos de $3,000, 1: $3,001 - $5,000, 2: $5,001 - $7,000, 3: Más de $7,000}
6. 'condiciones_oculares': variable categórica
    - etiquetas: {1:si, 0:no}
7. 'lentes': variable categórica
    - etiquetas: {1:si, 0:no}
8. 'iluminacion': variable categórica
    - etiquetas: {1: Adecuada, 0: Inadecuada}
9. 'tiempo_de_exposicion': variable numérica
10. 'frecuencia_de_pausas': variable categórica
    - etiquetas: {1: Frecuente, 2: Ocasional, 0: Nulo}
11. 'duracion_de_jornada': variable numérica
12. 'uso_de_dispositivos': variable categórica
    - etiquetas: {0: menos de 1 hora, 1: 1 - 2 h, 2: 2 - 4 h, 3: Mayor de 4h}
13. 'distancia_hacia_el_monitor': variable categórica
    - etiquetas: {0: Menor de 30 cm, 1: 30 - 60  cm, 2: Mayor de 60 cm}
14. 'severidad_svi': variable categórica
    - etiquetas: ['No SVI', 'Leve', 'Moderado', 'Severo']
15. 'puntaje_sindrome_visual_informatico': variable numérica
16. 'svi': variable categórica
    - etiquetas: {1:si, 0:no}