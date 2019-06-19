{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_ogr_sua_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/ogr/ogrsf_frmts/sua/ogrsualayer.cpp",
				"../gdal/ogr/ogrsf_frmts/sua/ogrsuadatasource.cpp",
				"../gdal/ogr/ogrsf_frmts/sua/ogrsuadriver.cpp"
			],
			"include_dirs": [
				"../gdal/ogr/ogrsf_frmts/sua"
			]
		}
	]
}
