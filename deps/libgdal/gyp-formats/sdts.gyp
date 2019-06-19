{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_sdts_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/frmts/sdts/sdtsattrreader.cpp",
				"../gdal/frmts/sdts/sdts2shp.cpp",
				"../gdal/frmts/sdts/sdtsindexedreader.cpp",
				"../gdal/frmts/sdts/sdtsdataset.cpp",
				"../gdal/frmts/sdts/sdtsxref.cpp",
				"../gdal/frmts/sdts/sdtsiref.cpp",
				"../gdal/frmts/sdts/sdtscatd.cpp",
				"../gdal/frmts/sdts/sdtslinereader.cpp",
				"../gdal/frmts/sdts/sdtslib.cpp",
				"../gdal/frmts/sdts/sdtsrasterreader.cpp",
				"../gdal/frmts/sdts/sdtspointreader.cpp",
				"../gdal/frmts/sdts/sdtspolygonreader.cpp",
				"../gdal/frmts/sdts/sdtstransfer.cpp"
			],
			"include_dirs": [
				"../gdal/frmts/sdts"
			]
		}
	]
}
