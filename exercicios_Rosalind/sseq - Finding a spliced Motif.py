def find_motif(data, motif):
    position, indices = -1, ''
    for nucleotide in motif:
        position = data.find(nucleotide, position+1)
        indices += str(position+1) + ' '
    print(indices)


with open('test.txt', 'r') as file:
    content = file.read()
DNAs_number, lines, line_number, DNAs = content.count('>'), content.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)

find_motif(DNAs[0], DNAs[1])