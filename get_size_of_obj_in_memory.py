import cPickle as cP

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size


def measure(l, fp, sizes, names):
    cP.dump(l, fp)
    sizes.append(getSize(fp))
    names.append(name)

filename = 'obj_dump'

#loc = locals()
#for key,l in loc.items:

names = []
sizes = []

for name in loc:
    l = locals()[name]
    fp = open(filename, 'wb')
    try:
        measure(l, fp, sizes, names)
    except:
        pass


