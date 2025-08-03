import collections

# Read and parse the data
data = []
with open('tchampsa.txt', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 7:
            year, division, weight, place, first, last, school = parts
            data.append({
                'year': year,
                'division': division,
                'weight': weight,
                'place': place,
                'name': f"{first} {last}",
                'school': school
            })
print(f"Loaded {len(data)} rows")
# Organize by weight, then by division
weights = collections.OrderedDict()
for entry in data:
    w = entry['weight']
    d = entry['division']
    if w not in weights:
        weights[w] = {}
    if d not in weights[w]:
        weights[w][d] = []
    weights[w][d].append(entry)

# Output HTML
for weight, divisions in weights.items():
    print(f'    <h2>{weight}</h2>')
    print('    <div class="table-row-flex">')
    for division in sorted(divisions.keys(), reverse=True):  # 6A first if present
        print('        <div class="table-wrapper">')
        print('            <table>')
        print(f'                <h2>{division}</h2>')
        print('                <colgroup>')
        print('                    <col style="width: 5%;">')
        print('                    <col style="width: 45%;">')
        print('                    <col style="width: 50%;">')
        print('                </colgroup>')
        for entry in sorted(divisions[division], key=lambda x: int(x['place'])):
            print(f'                <tr><td style="text-align: center;">{entry["place"]}</td><td>{entry["name"]}</td><td>{entry["school"]}</td></tr>')
        print('            </table>')
        print('        </div>')
    print('    </div>\n')
    