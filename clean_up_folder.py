# -*- coding: utf-8 -*-
from os import listdir, mkdir, rmdir, linesep
from os.path import dirname, splitext, basename, exists, isdir, join, abspath
from shutil import move


curdir = dirname(__file__)
curfile = basename(__file__)
undofile = 'undo_' + curfile
files = listdir(curdir)
file_list = filter(lambda f: splitext(f)[1] not in ('.lnk', '.ini', ''), files)
if curfile in file_list:
    file_list.remove(curfile)
if undofile in file_list:
    file_list.remove(undofile)
ext_list = set([splitext(f)[1][1:] for f in file_list if f])
print ext_list
lines = ['# -*- coding: utf-8 -*-', 'from os import rmdir', 'from shutil import move']
mvlines = []
rmlines = []
for ext in ext_list:
    if exists(ext) and isdir(ext):
        pass
    else:
        os.mkdir(ext)
        print 'mkdir ' + repr(ext)
        undo_list.append('rmdir(%s)' % repr(join(curdir, ext)))
for f in file_list:
    dst = splitext(f)[1][1:]
    move(f, dst)
    print 'move ' + repr(f) + ' to ' + repr(dst)
    mvlines.append('move(%s, %s)' % (repr(join(curdir, dst, f)), repr(curdir)))
f = open(undofile, 'w')
lines = lines + mvlines + rmlines
contents = linesep.join(lines)
f.write(contents)
f.flush()
f.close()
