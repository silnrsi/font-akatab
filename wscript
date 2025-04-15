#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

# set the default input/output folders
DOCDIR = ["documentation", "web"]

# set package name
APPNAME = "Akatab"

# retrieve all the authorship and other information from one of the master UFOs
getufoinfo('source/masters/Akatab-Regular.ufo')
DESC_SHORT = "Unicode font with OpenType support for the Tifinagh script"

designspace('source/akatab.designspace',
        params = '-c ^_',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/masters/Akatab-Regular.ufo ${DEP} ${TGT}'),
            cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')),
        ap = '${DS:FILENAME_BASE}.xml',
        classes = 'source/akatab_classes.xml',
        opentype = fea('source/${DS:FILENAME_BASE}.fea',
            master = 'source/akatab_master.feax',
            make_params = '--ignoreglyphs ^_',
            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/Akatab-WOFF-metadata.xml'),
        typetuner = typetuner('source/typetuner/akatab_feat_all.xml'),
        version = VERSION,
        )

# Make Tirra Neo-Tifinagh subset package
tpackage = package(appname="Tirra", docdir = {"documentation_tirra": "documentation", "web_tirra": "web"})
#    package_files = {
#                     'FONTLOG_tirra.txt': 'FONTLOG.txt', 
#                     'README_tirra.txt': 'README.txt',
#                    })
designspace('source/tirra.designspace',
        params = '-c ^_',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/masters/Tirra-Regular.ufo ${DEP} ${TGT}'),
            cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')),
#        ap = '${DS:FILENAME_BASE}.xml',
        opentype = fea('source/${DS:FILENAME_BASE}.fea',
            master = 'source/tirra.feax',
            make_params = '--ignoreglyphs ^_'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('web_tirra/${DS:FILENAME_BASE}.woff', 
            params = '-v ' + VERSION + ' -m ../source/Tirra-WOFF-metadata.xml',
            dontship=True),
        version = VERSION,
        package = tpackage
        )

