#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

# set the default input/output folders
DOCDIR = ["documentation", "web"]

# set package name
APPNAME = "Akatab"

# retrieve all the authorship and other information from one of the master UFOs
getufoinfo('source/masters/Akatab-Regular.ufo')
DESC_SHORT = "Unicode font with OpenType and Graphite support for the Tifinagh script"

designspace('source/akatab.designspace',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/masters/Akatab-Regular.ufo ${DEP} ${TGT}'),
            cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')),
        ap = '${DS:FILENAME_BASE}.xml',
        classes = 'source/akatab_classes.xml',
        opentype = fea('source/${DS:FILENAME_BASE}.fea',
            master = 'source/akatab_master.feax',
            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/Akatab-WOFF-metadata.xml'),
        typetuner = typetuner('source/typetuner/akatab_feat_all.xml'),
        version = VERSION,
        )

# Make Neo-Tifinagh subset package
ntpackage = package(appname="AkatabNeo", docdir = {"documentation_neo": "documentation", "web_neo": "web"},
    package_files = {
                     'FONTLOG_neo.txt': 'FONTLOG.txt', 
                     'README_neo.txt': 'README.txt',
                    })
designspace('source/akatab_neo.designspace',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/masters/AkatabNeo-Regular.ufo ${DEP} ${TGT}'),
            cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')),
#        ap = '${DS:FILENAME_BASE}.xml',
#        classes = 'source/akatab_classes.xml',
#        opentype = fea('source/${DS:FILENAME_BASE}.fea',
#            master = 'source/akatab_master.feax',
#            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('web_neo/${DS:FILENAME_BASE}.woff', 
            params = '-v ' + VERSION + ' -m ../source/AkatabNeo-WOFF-metadata.xml',
            dontship=True),
#        typetuner = typetuner('source/typetuner/akatab_feat_all.xml'),
        version = VERSION,
        package = ntpackage
        )

