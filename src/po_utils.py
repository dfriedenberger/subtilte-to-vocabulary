import os
import polib

def po_file_to_cache(filename):

    cache = {}

    if os.path.isfile(filename):
        po = polib.pofile(filename)
        for entry in po:
            cache[entry.msgid] = entry.msgstr

    return cache

def pot_file_to_list(filename):

    msg_ids = []
    po = polib.pofile(filename)
    
    for entry in po:
        msg_ids.append(entry.msgid)

    return msg_ids


def write_po_file(filename,data):
    # create po file
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'projekte@frittenburgerde',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    for msgid , msgstr in data:
        entry = polib.POEntry(
            msgid = msgid,
            msgstr = msgstr,
            occurrences=[]
        )
        po.append(entry)

    po.save(filename)


def write_pot_file(filename,data):
    # create po file
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'projekte@frittenburgerde',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    for msgid in data:
        entry = polib.POEntry(
            msgid = msgid,
            msgstr = "",
            occurrences=[]
        )
        po.append(entry)

    po.save(filename)
