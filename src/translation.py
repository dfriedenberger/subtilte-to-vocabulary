import os
import deepl

from .util import get_config

from .po_utils import po_file_to_cache

class Translator:

    def __init__(self,source_language,target_language):
        self.source_language = source_language
        self.target_language = target_language

        # Cache
        self.cache = {}
        dirname = os.path.dirname(__file__)
        cache_path = os.path.join(dirname, f'../cache/{self.source_language}_{self.target_language}')
        for file in os.listdir(cache_path):
            c = po_file_to_cache(os.path.join(cache_path,file))
            self.cache.update(c)

        # Deepl
        auth_key = get_config()["deepl"]["api_key"]
        self.translator = deepl.Translator(auth_key)

    def translate(self,phrase):

        if phrase in self.cache:
            return self.cache[phrase]

        #Translate with deepl
        result = self.translator.translate_text(phrase, source_lang=self.source_language,target_lang=self.target_language)
        print("translated",phrase,result.text)
        return result.text
