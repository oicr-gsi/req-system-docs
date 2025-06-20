# Documentation for the Requisition System

* Requisition System: https://requisition.genomics.oicr.on.ca
* User Manual: https://req-system-docs.readthedocs.io/latest/

This user manual is referenced in QM-031 of the OICR Genomics Quality Management System.

## Building

This site is built using Sphinx and requires Python 3.11+.

Installing:

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Building the site:

```
make html
```

Open build/index.html in a browser

## Read The Docs

The configuration for Read The Docs: https://app.readthedocs.org/projects/req-system-docs/
