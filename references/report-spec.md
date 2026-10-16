# Métricas y evidencia

Registrar intervalo inclusivo, moneda, zona horaria, campañas, filtros, objetivos y definición de cada conversión. Mostrar fechas completas en portada y rango abreviado en pies. Preservar conversiones fraccionarias por atribución.

Calcular con totales compatibles:
- CTR (%) = clics / impresiones × 100.
- CPC = inversión / clics.
- Costo por conversión = inversión / conversiones.
- Tasa de conversión = conversiones / interacciones elegibles × 100; usar clics como denominador solo cuando corresponda y declararlo.
- Variación (%) = (actual / anterior − 1) × 100. Si anterior es cero, mostrar N/A o «desde cero» con diferencia absoluta.

No promediar CPC, CTR ni CPA diarios sin ponderación. Mostrar N/A ante denominador cero, no costo cero. Diferenciar cero real, ausente, ilegible y no aplicable. El script presupone encabezados y números normalizados; revisar siempre la salida.

No llamar ventas a conversiones ni personas únicas a clics. Distinguir conversiones principales, todas las conversiones y acciones secundarias. Un clic a WhatsApp no demuestra una conversación ni un cliente. Mostrar WhatsApp/formulario solo con acción y valor explícitos; la aparición de esas palabras no acredita desglose. ROAS requiere valor de conversión e inversión compatibles; no es beneficio neto.

Comparar períodos de duración, moneda, filtros y atribución equivalentes. Si difieren, declarar límites y complementar con promedios diarios; no ocultar fechas detrás de nombres de meses. No inventar un período anterior ausente.

Priorizar la métrica del objetivo. Para campañas de leads, conversiones verificadas y costo por conversión; para alcance, métricas pertinentes. Para días fuertes, ponderar conversiones, volumen y eficiencia sin afirmar causalidad. No recomendar presupuesto basándose solo en clics. Etiquetar fechas reales y explicar agrupaciones; no convertir promedios por bloques en días exactos.

Usar formato local: 7.204; 91,99; ARS 151.950,47. Respetar moneda de origen. Distinguir inversión publicitaria, impuestos y honorarios. Redactar observación → impacto comercial → acción sugerida, con evidencia y prudencia ante muestras pequeñas.

## Analizador incluido

Normalizar primero un CSV limpio, sin preámbulos, subtotales ni filas duplicadas, con una única granularidad. Requiere Fecha/Día/Date/Day en AAAA-MM-DD o DD/MM/AAAA y acepta encabezados Google en español o inglés. Ejecutar:

```bash
python scripts/analyze_google_ads_csv.py --input-file serie.csv --start 2026-09-14 --end 2026-09-27 --locale es-AR --output analisis.json
```

Usar `--locale en-US` para punto decimal. Revisar moneda y unidades antes del cálculo. El script conserva métricas incompletas como null y no suma CSV distintos automáticamente. Para otros encabezados, fechas o tablas sin serie diaria, adaptar y validar los datos explícitamente; no forzar datos agregados a fechas inventadas.
