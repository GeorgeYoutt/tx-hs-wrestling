print("Script started")
import collections

# Read and parse the data (6 columns: year, weight, place, first, last, school)
data = []
with open('tchampsa.txt', encoding='utf-8') as f:
    for line in f:
        print(f"LINE: {line!r}")  # Add this line
        parts = line.strip().split('\t')
        print(f"PARTS: {parts}")  # And this line
        if len(parts) == 6:
            year, weight, place, first, last, school = parts
            data.append({
                'year': year,
                'weight': weight,
                'place': place,
                'name': f"{first} {last}",
                'school': school
            })
print(f"Loaded {len(data)} rows")
# Group by weight
weights = collections.OrderedDict()
for entry in data:
    w = entry['weight']
    if w not in weights:
        weights[w] = []
    weights[w].append(entry)

# Sort weights numerically if possible
def weight_key(w):
    try:
        return int(w)
    except ValueError:
        return float('inf')

sorted_weights = sorted(weights.keys(), key=weight_key)

# Output HTML: two tables per row
i = 0
while i < len(sorted_weights):
    print('<div class="table-row-flex">')
    for j in range(2):
        if i + j < len(sorted_weights):
            weight = sorted_weights[i + j]
            print('    <div class="table-wrapper">')
            print('        <table>')
            print(f'            <h2>{weight}</h2>')
            print('            <colgroup>')
            print('                <col style="width: 5%;">')
            print('                <col style="width: 45%;">')
            print('                <col style="width: 50%;">')
            print('            </colgroup>')
            for entry in sorted(weights[weight], key=lambda x: int(x['place'])):
                print(f'            <tr><td style="text-align: center;">{entry["place"]}</td><td>{entry["name"]}</td><td>{entry["school"]}</td></tr>')
            print('        </table>')
            print('    </div>')
    print('</div>\n')
    i += 2
