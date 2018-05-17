
# XML Creation based on Directory Name and Path

A Python script to create a simple XML for use in Telestream Vantage workflows.

## Project Description

Vantage, by Telestream, is a Windows-based solution for designing and managing
fully automated media workflows. Project archving is a typical workflow that
occurs at the end of media pipeline. The media archives are created by placing a
collection of files and/or project folders into a container (.ZIP, .dmg, .iso,
etc) The problem with using Vantage for this task is that it's workflows are
file-based, a project directory cannot trigger a Vantage workflow.

This Python script was created out the need to automate the archiving of media
projects from within a Vantage workflow. These projects exist in the filesystem
as a directory with any number of sub-directories and files. In order to place
the project into a Vantage watch-folder and trigger a workflow, the Python
script must first generate some type of associated file and metadata.

The Python script generates an XML document for each project directory in a
given 'watch folder'. The XML contains two elements `<ProjectName>` and
`<ProjectPath>`. The creation of the XML file by the Python script triggers the
start of the Vantage workflow. The two elements from the XML are used to
generate variables inside the Vantage workflow:  `<ProjectName>` translates to
the `Project Name` text variable, and `<ProjectPath>` translates to the `Project
Path` - path variable. The Vantage workflow uses this information to archive the
entire contents of Project at the given path.

## Prerequisites

[Windows Server OS 2008 R2 or later](https://www.microsoft.com/en-us/cloud-platform/windows-server)

[Python 2.7 or later](https://www.python.org/downloads/)

[Telestream Vantage 6.3 or later](http://www.telestream.net/vantage/overview.htm)

## Files Included

**``Vantage_XML_Creation.py``** - The python script for generating the XML.

**``Vantage_XSLT_Transform.xml``** - XSLT used to transform the generic XML from the 
python script to a 'style sheet' used inside the Vantage Workflow.

**``Vantage_Project_Archive_Workflow.xml``** - The Vantage workflow that accepts the 
XML created by the Python script.

## Getting Started

After the prerequisites are installed.

1. Open the __Vantage_XML_Creation.py__ and add the paths for: 
	* `watch_folder`
	* `output_dir01`
	* `output_dir02`

2. Add the Python script to the Windows Task Scheduler, and set it run on a
given interval.

3. Import the **``Vantage_Project_Archive_Workflow.xml``** and
**``Vantage_XSLT_Transform.xml``** files into Vantage.

4. Set the watch folder, output location, and variables in the
**``Vantage_Project_Archive_Workflow.xml``**

## Vantage Workflow Actions

1. `Watch` - Monitors the watch folder location.
2. `Transform` - Define the Style Sheet, the XML attachment, and the Metadata Label.
3. `Populate` - Select the Metadata Label, and use it to define workflow variables.
4. `Construct` - Build the complete project path, taken from the ``project path`` variable.
5. `Gather` - Use the `project path` variable to define a project folder to gather for archive.
6. `Archive` - Archive (zip) the project folder defined in the Gather action.
7. `Move` - Move the original unzipped project folder to final destination.
8. `Delete` - elete the original XML file used to trigger the workflow.
