# Reporte de Publicidad

Habilidad completa de Punilla Digital para crear informes de Google Ads desde CSV, capturas o tablas. Reemplaza la versión básica de este repositorio.

## Entrega y alcance

- Informe para un cliente y un intervalo inclusivo de fechas definido.
- PowerPoint editable y PDF exportado desde la misma presentación.
- Análisis, métricas, gráficos, comparativas y recomendaciones según la evidencia disponible.
- Diapositivas adaptables: agregar secciones útiles y retirar las que no correspondan.
- Tema Google Ads y recursos Facebook/Meta preparados para una futura ampliación.
- Analizador de CSV Google Ads con filtros de fecha y métricas calculadas.

La implementación actual se especializa en Google Ads. Los logos y temas Meta no equivalen a un adaptador probado de exportaciones Facebook Ads; los datos Meta requieren revisión manual y un alcance explícito.

## Archivos

- [SKILL.md](SKILL.md): flujo completo.
- [scripts/analyze_google_ads_csv.py](scripts/analyze_google_ads_csv.py): analizador.
- [references/report-spec.md](references/report-spec.md): métricas y evidencia.
- [references/presentation.md](references/presentation.md): narrativa y exportación.
- [references/themes.md](references/themes.md): temas y uso de logos.
- [references/pdf-report.md](references/pdf-report.md): revisión de PDF.
- [references/google-slides.md](references/google-slides.md): alternativa opcional.
- [references/logos-sources.json](references/logos-sources.json): procedencia de logos.
- [assets/modelo-google-ads.pptx](assets/modelo-google-ads.pptx): plantilla genérica sin datos de clientes.
- assets/: logos de plataformas e iconos de la habilidad.
- [agents/openai.yaml](agents/openai.yaml): metadatos de interfaz.

## Uso

Copiar la carpeta completa como `reporte-de-publicidad` al directorio de habilidades de un agente compatible. Mantener referencias, scripts y recursos junto al SKILL.md. Publicar en GitHub no instala automáticamente la habilidad en ChatGPT.

> Usá Reporte de Publicidad para analizar estas campañas de Google Ads del 1 al 15 de octubre de 2026, en ARS, y entregar PowerPoint y PDF.

## Analizador CSV

Requiere Python 3 y solo usa su biblioteca estándar. Normalizar primero el archivo: una granularidad, sin preámbulos, totales duplicados ni filas solapadas. Consultar report-spec.md para encabezados y formatos admitidos.

```bash
python scripts/analyze_google_ads_csv.py --input-file serie.csv --start 2026-10-01 --end 2026-10-15 --locale es-AR --output analisis.json
```

No sumar tablas distintas automáticamente ni interpretar clics como ventas. Confirmar moneda, filtros, zona horaria y definiciones de conversión.

## Modelo y recursos

El modelo incluido es una plantilla genérica nueva de ocho diapositivas editables, sin datos de clientes. Reemplaza el informe histórico de la habilidad instalada para permitir su distribución pública. Completar los campos con evidencia y adaptar la cantidad de diapositivas. No entregar los textos orientativos como resultados.

Los logos conservan sus fuentes y reglas de uso; no implican patrocinio, certificación ni asociación.

## Requisitos de presentación

Necesita herramientas de generación de PPTX y un exportador compatible a PDF, además de renderizado para revisar todos los archivos. Las habilidades externas mencionadas y los servicios de Google Slides no están incluidos. Si falla una exportación, informar el bloqueo sin declarar la entrega completa.

## Origen

Adaptación de la habilidad instalada en Complementos, publicada el 15/10/2026. Conserva instrucciones, analizador y recursos de plataforma; sustituye únicamente el modelo histórico por una plantilla genérica sin datos de clientes y adapta sus referencias. No modifica la habilidad instalada.

[Punilla Digital](https://punilladigital.com.ar/) · [Licencia](LICENSE)
