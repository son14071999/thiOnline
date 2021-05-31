import unidecode
import re
slug = "đề     thi thử số 1"
slug = re.sub(r'[ ]+', '-', unidecode.unidecode(slug))
print(slug)