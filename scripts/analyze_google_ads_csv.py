#!/usr/bin/env python3
"""Analyze one clean, non-overlapping Google Ads table; standard library only."""
import argparse
import csv
import io
import json
from datetime import date, datetime
from pathlib import Path


def number(value, locale='es-AR'):
    if value is None or str(value).strip() in ('', '--', '—', 'N/A'):
        return None
    text = str(value).strip().replace('\u00a0', '').replace(' ', '')
    for symbol in ('ARS', 'USD', '$', '%'):
        text = text.replace(symbol, '')
    if locale == 'es-AR':
        text = text.replace('.', '').replace(',', '.')
    else:
        text = text.replace(',', '')
    return float(text)


def read_csv(path):
    data = path.read_bytes()
    text = data.decode('utf-16') if data.startswith((b'\xff\xfe', b'\xfe\xff')) else data.decode('utf-8-sig')
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=',;\t')
    except csv.Error:
        raise ValueError('Separador no reconocido: normalizar el CSV y quitar preámbulos.')
    return [{k.strip(): v for k, v in row.items() if k is not None} for row in csv.DictReader(io.StringIO(text), dialect=dialect)]


ALIASES = {'clicks': ('Clics', 'Clicks'), 'impressions': ('Impresiones', 'Impressions'),
           'cost': ('Coste', 'Costo', 'Cost'), 'conversions': ('Conversiones', 'Conversions')}


def analyze(rows, start, end, locale):
    selected = []
    for row in rows:
        raw = row.get('Fecha') or row.get('Día') or row.get('Date') or row.get('Day')
        if not raw:
            raise ValueError('Se requiere una columna Fecha/Día/Date/Day para validar el intervalo.')
        parsed = None
        for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y'):
            try:
                parsed = datetime.strptime(raw.strip(), fmt).date()
                break
            except ValueError:
                pass
        if parsed is None:
            raise ValueError(f'Fecha no reconocida o fila total: {raw!r}. Limpiar el CSV.')
        if start <= parsed <= end:
            selected.append(dict(row, _date=parsed.isoformat()))
    if not selected:
        raise ValueError('No hay datos dentro del intervalo solicitado.')
    totals = {}
    for metric, aliases in ALIASES.items():
        values = [number(next((r[k] for k in aliases if k in r), None), locale) for r in selected]
        totals[metric] = sum(values) if all(v is not None for v in values) else None
    def ratio(a, b):
        return a / b if a is not None and b is not None and b != 0 else None
    totals.update(ctr_percent=(lambda x: x * 100 if x is not None else None)(ratio(totals['clicks'], totals['impressions'])),
                  cpc=ratio(totals['cost'], totals['clicks']), cost_per_conversion=ratio(totals['cost'], totals['conversions']))
    return {'start': start.isoformat(), 'end': end.isoformat(), 'totals': totals,
            'rows': sorted(selected, key=lambda r: r['_date']),
            'notes': ['Confirmar manualmente moneda, zona horaria, filtros, granularidad y ausencia de duplicados.',
                      'Desglose por acción de conversión requiere una tabla explícita; no se infiere por palabras.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-file', required=True, type=Path)
    parser.add_argument('--start', required=True, type=date.fromisoformat)
    parser.add_argument('--end', required=True, type=date.fromisoformat)
    parser.add_argument('--locale', choices=('es-AR', 'en-US'), default='es-AR')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.start > args.end:
        parser.error('La fecha inicial debe ser anterior o igual a la final.')
    output = analyze(read_csv(args.input_file), args.start, args.end, args.locale)
    output['source'] = str(args.input_file)
    payload = json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False)
    if args.output:
        args.output.write_text(payload + '\n', encoding='utf-8')
    else:
        print(payload)


if __name__ == '__main__':
    main()
