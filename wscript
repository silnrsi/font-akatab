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

d = designspace('source/akatab.designspace',
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
npackage = package(appname="AkatabNeo", 
                   version = VERSION, 
                   package_files = {
                                    'README.txt': '/nul', 
                                    'source/subset-neo/AkatabNeo*.ttf': '/',
                                    'source/subset-neo/FONTLOG.txt': '/', 
                                    'source/subset-neo/OFL.txt': '/', 
                                    'source/subset-neo/OFL-FAQ.txt': '/', 
                                    'source/subset-neo/README.txt': '/', 
                                    'source/subset-neo/documentation/*.*': 'documentation/', 
                                    'source/subset-neo/web/*.*': 'web/'
                                   })
d = designspace('source/subset-neo/source/akatab_neo.designspace',
        target = process('source/subset-neo/${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/subset-neo/source/masters/AkatabNeo-Regular.ufo ${DEP} ${TGT}'),
            cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')),
#        ap = '${DS:FILENAME_BASE}.xml',
#        classes = 'source/akatab_classes.xml',
#        opentype = fea('source/${DS:FILENAME_BASE}.fea',
#            master = 'source/akatab_master.feax',
#            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('source/subset-neo/web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/subset-neo/source/AkatabNeo-WOFF-metadata.xml'),
#        typetuner = typetuner('source/typetuner/akatab_feat_all.xml'),
        version = VERSION,
        )
