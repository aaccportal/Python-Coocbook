# 4.13. Creating Data Processing Pipelines

# Problem
# You want to process data iteratively in the style of a data processing pipeline (similar to
# Unix pipes). For instance, you have a huge amount of data that needs to be processed,
# but it can’t fit entirely into memory.

# Solution
# Generator functions are a good way to implement processing pipelines. To illustrate,
# suppose you have a huge directory of log files that you want to process:

# Проблема
# Вы хотите обрабатывать данные итеративно в стиле конвейера обработки данных (аналогично
# каналы Unix). Например, у вас есть огромное количество данных, которые необходимо обработать.
# но это не может полностью уместиться в памяти.

# Решение
# Функции-генераторы — хороший способ реализации конвейеров обработки. Проиллюстрировать,
# предположим, у вас есть огромный каталог файлов журналов, которые вы хотите обработать:

# To process these files, you could define a collection of small generator functions that
# perform specific self-contained tasks. For example:

def gen_find(filepat, top):
    '''
Find all filenames in a directory tree that match a shell wildcard pattern
'''
for path, dirlist, filelist in os.walk(top):
for name in fnmatch.filter(filelist, filepat):
yield os.path.join(path,name)
def gen_opener(filenames):
'''
Open a sequence of filenames one at a time producing a file object.
The file is closed immediately when proceeding to the next iteration.
'''
for filename in filenames:
if filename.endswith('.gz'):
f = gzip.open(filename, 'rt')
elif filename.endswith('.bz2'):
f = bz2.open(filename, 'rt')
else:
f = open(filename, 'rt')
yield f
f.close()
def gen_concatenate(iterators):
'''
Chain a sequence of iterators together into a single sequence.
'''
for it in iterators:
yield from it
def gen_grep(pattern, lines):
'''
Look for a regex pattern in a sequence of lines
'''
pat = re.compile(pattern)
for line in lines:
if pat.search(line):
yield line