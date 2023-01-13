# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

string = 'Jkngs ароф wroko абв ддабваьд вла аБв'
new_string = list(filter(lambda wd:'абв' not in wd, string.lower().split()))
print(' '.join(new_string))