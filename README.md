
## XML Creation based on Directory Name and Path

A Python script to create a simple XML for use in Telestream Vantage workflows. 


## Project Description

Vantage, by Telestream, is a Windows-based solution for media transcoding and workflow creation. As part of automating the media pipeline, there is a need to automate the archiving of projects and associated files by placing the collective files into a container (.ZIP, .dmg, ,iso, etc) The problem with using Vantage for this task - it's workflows are file-based, a directory cannot trigger a Vantage workflow. 

This Python script was created out the need to automate the archiving of media projects from within a Vantage workflow. These projects exist in the filesystem as a directory with a given number of sub-directories an files. In order to place
the project into a Vantage watch-folder and trigger a workflow, the Python script must first generate some type of associated file with metadata. 

The Python script generates an XML document for each project directory in a given 'watch folder'. The XML contains two elements `<ProjectName>` and `<ProjectPath>`. The creation of the XML file triggers the start of the Vantage workflow. The two elements from the XML are used to generate variables inside the Vantage workflow:  `<ProjectName>` translates to the `Project Name` text variable, and `<ProjectPath>` translates to the `Project Path` - text variable. The Vantage workflow uses this information to archive the entire contents of Project at the given path. 


## Prerequisites

* Windows Server OS (http://www.telestream.net/vantage/tech-specs.htm) 
* Python 2.7 or later (https://www.python.org/downloads/)
* Telestream Vantage 6.3 or later (http://www.telestream.net/vantage/overview.htm)


## Files Included

__Vantage_XML_Creation.py__ - The python script for generating the XML. 

__Vantage_XSLT_Transform.xml__ - XSLT used to transform the generic XML from the python script to a 'style sheet' used inside the Vantage Workflow. 

__Vantage_ZIP_Workflow.xml__ - The Vantage workflow that accepts the XML created by the Python script. 

__MOVE_Project.bat__ - simple batch script that is called at teh end of the Zip workflow. It moves the unzipped archive into its file location. 


## Getting Started

After the prerequisites are downloaded and installed. 

1. Open the __Vantage_XML_Creation.py__ and add the paths for: 
 * `watch_folder`
 * `output_dir01`
 * `output_dir02`

 2. 

Execute commands: 

1. 
2. 
3. 
4. 
5. 
6. 

##Vantage Workflow Actions

1. `Watch`
2. `Transform`
3. `Populate`
4. `Construct`
5. `Gather`
6. `Archive`
7. `Move`
8. `Delete`









