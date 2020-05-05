#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

# set the default input/output folders
DOCDIR = ["documentation", "web"]
STANDARDS = 'tests/reference'

# set package name
APPNAME = "Akatab"
#BUILDLABEL = "Beta"

# retrieve all the authorship and other information from one of the master UFOs
getufoinfo('source/masters/Akatab-Regular.ufo')
DESC_SHORT = "Smart font for the Tifinagh script"

d = designspace('source/akatab.designspace',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ../source/masters/Akatab-Regular.ufo ${DEP} ${TGT}')),
        instanceparams = "-W",
        ap = '${DS:FILENAME_BASE}.xml',
        classes = 'source/akatab_classes.xml',
        opentype = fea('source/${DS:FILENAME_BASE}.fea',
            master = 'source/akatab_master.feax',
            mapfile = 'source/typetuner/${DS:FILENAME_BASE}.map'),
        graphite = gdl('source/${DS:FILENAME_BASE}.gdl',
            master = 'source/akatab.gdl',
            make_params = ' --package "../tools/perllib/gdl_tif_aka.pm"'),
        script = ['tfng'],
        pdf = fret(params='-r -b'),
        woff = woff('web/${DS:FILENAME_BASE}.woff', params = '-v ' + VERSION + ' -m ../source/Akatab-WOFF-metadata.xml'),
        typetuner = typetuner('source/typetuner/akatab_feat_all.xml'),
        version = VERSION,
        )

# Create RTL package to build a font with cmap pointing to .rtl glyphs
rtlpackage = package(appname="AkatabRTL", version=VERSION)
for f in d.fonts:
    font(target = process(f.target.replace('Akatab', 'AkatabRTL'),
            cmd('ttfremap -r -c ${SRC} ${DEP} ${TGT}', ['source/rtl_remap.txt']),
            name('AkatabRTL')),
        opentype = internal(),
        source = f.target,
        package = rtlpackage)

