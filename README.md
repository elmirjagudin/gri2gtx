Geoid Grid Tables
-----------------

This repo contains orthometric (geoidal) datum tables in GTX format for geoid models used in Ireland and Sweden.

The files are:

|   GTX file          |     Geoid Model
|---------------------|--------------------
|  OSGM15_Malin.gtx   | OSGM15 Malin Head datum
|  OSGM15_Belfast.gtx | OSGM15 Belfast datum
|  SWEN17_RH2000.gtx  | RH2000

These tables can be used together as input to [proj4][0] utilities to derive orthometric heights in the respective geoid models.

For example convert WSG84 coordinate to OSGM15 (Malin Head datum) height following command can be used:

  echo "-9.45 54.15 95.22" | cs2cs +init=epsg:4326 +to +init=epsg:2157 +geoidgrids=./OSGM15_Malin.gtx

To covert WSG84 coordinate to RH2000 height:

  echo "14.72 59.36 100.0" | cs2cs +init=epsg:4326 +to +init=epsg:5845 +geoidgrids=./SWEN17_RH2000.gtx

The above commands assume that proj4 command line utilities are installed and that *.gtx files are located in the current directory.


Source Files
------------

The GTX files are derived from the source files provided by [Ordnance Survey][1] and [Lantmäteriet][2].

|   GTX file         |     Source File    | Source Archive
|--------------------|--------------------|---------------
| OSGM15_Malin.gtx   | OSGM15_Malin.gri   | https://www.ordnancesurvey.co.uk/docs/gps/OSTN15-OSGM15_DevelopersPack.zip
| OSGM15_Belfast.gtx | OSGM15_Belfast.gri | https://www.ordnancesurvey.co.uk/docs/gps/OSTN15-OSGM15_DevelopersPack.zip
| SWEN17_RH2000.gtx  | SWEN17_RH2000.txt  | https://www.lantmateriet.se/globalassets/kartor-och-geografisk-information/gps-och-matning/geodesi/transformationer/swen17_rh2000_txt.zip

The files were converted with gri2gtx.py python 3 script, in this repository.
See the Makefile for details how to run the conversion script.

[0]: https://proj4.org/
[1]: https://www.ordnancesurvey.co.uk/
[2]: https://www.lantmateriet.se/en/
