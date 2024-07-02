# Merge PDFs

## Project info
* A command-line tool to merge multiple PDFs into a single PDF file using Python
* Uses `click` for parsing command-line args
* Uses `setuptools` to package the project into a command-line tool


## Installing instructions
* For installing the tool, run the following command
```
python setup.py develop
```


## Using the tool after installing
* Run
```
merge-pdfs --file-pdf <full-path-to_pdf-1> --file-pdf <full-path-to_pdf-2> --file-pdf <full-path-to_pdf-3> .....
```