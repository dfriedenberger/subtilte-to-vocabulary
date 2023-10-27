import os
import argparse

from src.translation import Translator
from src.po_utils import po_file_to_cache, pot_file_to_list, write_po_file

def parse_args():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Script for translating pot files to po files')

    parser.add_argument("--input-file", required=True,
                        metavar="INPUT",
                        help="input file in pot format")
    parser.add_argument("--input-language", required=True,
                        metavar="INPUT_LANGUAGE",
                        choices=['de', 'en', 'es'],
                        help="language of input file (de,en,es)")
    parser.add_argument("--output-language", required=True,
                        metavar="OUTPUT_LANGUAGE",
                        choices=['de', 'en', 'es'],
                        help="language of output file (de,en,es)")

    args = parser.parse_args()

    return args.input_file, args.input_language, args.output_language




input_file, input_language, output_language = parse_args()

translator = Translator(input_language,output_language)

path = os.path.dirname(input_file)
output_file = os.path.join(path,f"{output_language}.po")


#read entries

data = []
for msgid in pot_file_to_list(input_file):

    msgstr = translator.translate(msgid)
    data.append((msgid,msgstr))

write_po_file(output_file,data)
