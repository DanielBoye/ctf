oleid easy_flag.xlsm

også 
olevba easy_flag.xlsm

olevba easy_flag.xlsm --decode


/mnt/c/Users/danie/Downloads/easy_flag$ olevba easy_flag.xlsm --decode
olevba 0.60.1 on Python 3.10.12 - http://decalage.info/python/oletools
===============================================================================
FILE: easy_flag.xlsm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisWorkbook.cls
in file: xl/vbaProject.bin - OLE stream: 'VBA/ThisWorkbook'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Private Sub Workbook_Open()
    flag = "helsectf{maldoc=malicious_document}"
End Sub
-------------------------------------------------------------------------------
VBA MACRO Sheet1.cls
in file: xl/vbaProject.bin - OLE stream: 'VBA/Sheet1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(empty macro)
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Workbook_Open       |Runs when the Excel Workbook is opened       |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
|Hex String|'\x00\x02\x08\x19'  |00020819                                     |
|Hex String|'\x00\x00\x00\x00\x0|000000000046                                 |
|          |0F'                 |                                             |
|Hex String|'\x00\x02\x08 '     |00020820                                     |
+----------+--------------------+---------------------------------------------+

/mnt/c/Users/danie/Downloads/easy_flag$