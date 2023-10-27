import json
import argparse
import yaml
import polib

from src.read_subtile import read_subtile
from src.nlp_utils import get_sentences
from src.language_processing import language_processing
from src.po_utils import write_pot_file
def parse_args():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Script for converting subtilte files (srt) to vocabulary learnsets')

    parser.add_argument("--input-file", required=True,
                        metavar="INPUT",
                        help="subtitle input file in srt format")
    parser.add_argument("--language", required=True,
                        metavar="LANGUAGE",
                        choices=['de', 'en', 'es'],
                        help="language of subtitle (de,en,es)")
    parser.add_argument("--encoding", nargs='?', default="UTF-8",
                        metavar="ENCODING",
                        help="encoding of srt input file e.g iso-8859-1, utf-8 is default")
    
    parser.add_argument("--output-folder",required=True,
                        metavar="FOLDER",
                        help="output folder")
    
    args = parser.parse_args()

    return args.input_file, args.language , args.encoding, args.output_folder

input_file, language, encoding, output_folder = parse_args()
# read file and parse sentences

lines = read_subtile(input_file,encoding)

text = ' '.join(lines)
sentences = get_sentences(text,language)

# language processing of sentences
phrases = language_processing(sentences,language)

# create json file
with open(f"{output_folder}/phrases.json",mode='w',encoding="UTF-8") as f:
    json.dump(phrases,f,ensure_ascii=False,indent  = 4)

# create po file
data = []
for phrase in phrases:
    data.append(phrase['text'])

write_pot_file(f'{output_folder}/phrases.pot',data)

