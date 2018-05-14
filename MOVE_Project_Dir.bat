:: this script will MOVE a folder, all files and sub-folders contained within. 
:: it is executed at the end of the "Vantage-Zip" workflow.
:: after a project has been sucessfully archived, vantage will pass the path of the source folder into this script. 

MOVE /Y %1 X:\file-path-to-Zip-CheckIn\Zip-Archive-Output