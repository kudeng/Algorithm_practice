inf = '/Users/kudengma/PycharmProjects/formegan/templates/front.html'
outf = '/Users/kudengma/Desktop/output.html'
with open(inf, 'r') as fin:
    with open(outf, 'w') as fout:
        for line in fin.readlines():
            if 'href=' in line:
                print('yes')
                l = len('href="')
                index = line.index('href="')
                end = line[:index+l].index('"') + 1
                url = 'main/' + line[index+l:end]
                newline = line[:index+l] + '{% static ' +  url + '%}' + line[end:]
                fout.write(newline)
