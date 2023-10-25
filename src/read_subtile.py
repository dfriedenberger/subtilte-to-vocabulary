import pysrt
import re

def read_subtile(srt_filename,encoding):

    lines = []
    subs = pysrt.open(srt_filename,encoding)

    for sub in subs:
        txt = sub.text_without_tags
        
        for line in txt.split('\n'):
            line = re.sub(r"^\s*[-]","",line).strip()
            line = re.sub(r"^\s*#","",line).strip()
            line = re.sub(r"#\s*$","",line).strip()

            line = re.sub("[(][^()]+[)]","",line).strip() #cleanup ()

            if line:
                lines.append(line)

    return lines