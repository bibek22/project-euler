archive = []
for each in range(2, 101):
    for all in range(2, 101):
        new = each ** all
        if new in archive:
            pass
        else:
            archive.append(new)
print len(archive)
