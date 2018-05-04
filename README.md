
## XML Creation for a Vantage Workflow

A Python script to create simple XML for use in Telestream Vantage workflows. 


## Project Description

This Python script was created out the need to automate the archiving of video projects and associated .WAV files through a Telestream Vantage Workflow.    

The script generates an XML document for each individual sub-directory in a given 'watch folder'. The XML contains two elements `<ProjectName>` and `<ProjectPath>`. The creation of the XML file triggers the start of the Vantage workflow. The two elements from the XML are used to generate variables for the Vantage workflow:  `<ProjectName>` translates to the `Project Name` variable, and `<ProjectPath>` translates to the `Project Path - text` variable. The Vantage workflow


The Vantage workflow and video encoding software 
The Vantage workflows are file-based, a directory cannot trigger a workflow. 


## Prerequisites

* Windows Server OS (http://www.telestream.net/vantage/tech-specs.htm) 
* Python 2.7 or 3.5  (https://www.python.org/downloads/)
* Telestream Vantage 6.3 or above (http://www.telestream.net/vantage/overview.htm)


## Files Included

__Vantage_XML_Creation.py__ - The python script for generating the XML. 

__Vantage_XSLT_Transform.xml__ - XSLT used to transform the generic XML from the python script to a 'style sheet' used inside the Vantage Workflow. 

__Vantage_ZIP_Workflow.xml__ - The Vantage workflow that accepts the XML created by the Python script. 


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









