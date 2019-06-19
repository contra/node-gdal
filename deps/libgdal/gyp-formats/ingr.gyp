{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_ingr_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/frmts/ingr/IntergraphDataset.cpp",
				"../gdal/frmts/ingr/JpegHelper.cpp",
				"../gdal/frmts/ingr/IngrTypes.cpp",
				"../gdal/frmts/ingr/IntergraphBand.cpp"
			],
			"include_dirs": [
				"../gdal/frmts/ingr"
			]
		}
	]
}
