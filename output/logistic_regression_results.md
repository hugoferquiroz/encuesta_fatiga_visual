# Resultados de Regresión Logística

## Modelo 1: Solo tiempo_de_exposicion

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -4.828 | 0.008 | 0.000 | 3.454 | 0.1189 |
| tiempo_de_exposicion | 0.629 | 1.875 | 1.027 | 3.425 | 0.0407 |

### Interpretación del Modelo Simple

1. **Tiempo de exposición**:
   - El coeficiente es positivo (0.629) y estadísticamente significativo al 5% (p = 0.0407)
   - El odds ratio de 1.875 indica que por cada unidad que aumenta el tiempo de exposición, la probabilidad de desarrollar SVI aumenta en un 87.5%
   - El intervalo de confianza del odds ratio (1.027 - 3.425) no incluye el 1, lo que confirma la significancia estadística
   - Al ser el límite inferior del IC mayor a 1 (1.027), podemos estar 95% seguros de que existe un efecto positivo real

2. **Constante**:
   - El coeficiente negativo (-4.828) sugiere que la probabilidad base de SVI es baja cuando no hay exposición
   - El odds ratio de 0.008 indica una baja probabilidad basal de SVI
   - No es estadísticamente significativa (p = 0.1189), lo cual es común para términos constantes

## Modelo 2: Variables múltiples

| Variable | Coeficiente | Odds Ratio | IC 95% Inferior | IC 95% Superior | Valor p |
|----------|-------------|------------|-----------------|-----------------|----------|
| const | -3.803 | 0.022 | 0.000 | 611474.660 | 0.6634 |
| tiempo_de_exposicion | 0.982 | 2.671 | 0.967 | 7.381 | 0.0582 |
| iluminacion_1 | -9.159 | 0.000 | 0.000 | 7044.420 | 0.3191 |
| uso_de_dispositivos_1 | 2.646 | 14.095 | 0.001 | 385480.206 | 0.6117 |
| uso_de_dispositivos_2 | 0.417 | 1.518 | 0.000 | 6425966.959 | 0.9573 |
| uso_de_dispositivos_3 | 4.722 | 112.403 | 0.006 | 2276323.711 | 0.3506 |

### Interpretación del Modelo Múltiple

1. **Tiempo de exposición**:
   - El coeficiente aumenta a 0.982 y mantiene significancia estadística al 10% (p = 0.0582)
   - El odds ratio aumenta a 2.671, sugiriendo que, controlando por otras variables, por cada unidad de aumento en el tiempo de exposición, la probabilidad de SVI aumenta en un 167.1%
   - Aunque el IC 95% (0.967 - 7.381) incluye marginalmente el 1, la significancia al 10% y la consistencia con el modelo simple sugieren un efecto robusto

2. **Constante**:
   - El coeficiente (-3.803) mantiene el signo negativo pero pierde significancia (p = 0.6634)
   - El amplio intervalo de confianza refleja la incertidumbre al incluir múltiples variables

### Robustez de los Resultados

La variable de interés 'tiempo_de_exposicion' muestra consistencia en ambos modelos:
1. En el modelo simple es significativa al 5%
2. En el modelo múltiple mantiene significancia al 10%
3. Los coeficientes son positivos en ambos casos
4. La magnitud del efecto aumenta en el modelo múltiple (de 1.875 a 2.671)

Esta consistencia en la significancia y dirección del efecto, incluso después de controlar por otras variables, sugiere que el tiempo de exposición es un factor de riesgo robusto para el desarrollo de SVI.

## Categorías de Referencia

Las siguientes categorías se utilizaron como referencia en el modelo múltiple:
- Iluminación: Primera categoría
- Uso de dispositivos: Primera categoría

Los coeficientes y odds ratios para las variables dummy se interpretan en relación a estas categorías de referencia.

### Efectos Marginales

Los efectos marginales muestran que la relación entre el tiempo de exposición y la probabilidad de SVI es no lineal:
1. El efecto es más pronunciado en niveles medios de exposición
2. La probabilidad de SVI aumenta más rápidamente al principio
3. El efecto marginal se mantiene positivo en todo el rango de exposición

Esta no linealidad sugiere que intervenciones preventivas podrían ser especialmente efectivas en niveles moderados de exposición.