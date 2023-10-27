

# subtilte-to-vocabulary

Convert subtiltes or other text to vocabulary learnsets

## Installation



```bash
pip install -r requieremnts
```

## Usage


### Convert subtitle files to vocabulary and pot files (subtitles from https://opensubtitles.org/) 
```bash
python convert_subtitle.py --input-file <srt-file> --language de|es|en [--encoding iso-8859-1] --output-folder tmp
```

### Translate 
```bash
python translate_pot.py --input-file <pot-file> --input-language de|es|en --output-language de|es|en
```

### Example
```
python convert_subtitle.py --input-file tmp/Ready.to.Mingle.2019.SPANISH.WEBRip.x264-VXT.srt --language es --output-folder tmp/ ```

```
python translate_pot.py --input-file tmp/phrases.pot --input-language es --output-language de
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)