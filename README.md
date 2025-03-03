# ZeissIQS-pages

Source of the generated documentation in [zeissiqs.github.io](https://zeissiqs.github.io/).

> [!NOTE]
> Please see [ZEISS Industrial Quality Solutions](https://zeissiqs.github.io) for the resulting rendered output.

## General

* The documentation accessible via [ZeissIQS.github.io](https://github.com/ZeissIQS/ZeissIQS.github.io) is generated from the files in this repository.
* The [sphinx documentation conversion tool](https://www.sphinx-doc.org) is used for that purpose.
* The generated documentation is then committed into a repository with some special name and can the be rendered by the site https://zeissiqs.github.io/.

## Installation

> For ZEISS IQS software developers: The necessary tools are already part of the build system. You do not need to execute the following steps !

* You need a Python 3 installation
* Add the necessary Python packages:

~~~
python -m pip install sphinx sphinx_rtd_theme myst_parser sphinx_favicon sphinx_sitemap sphinxcontrib-newsfeed
~~~

## Repositories

* Clone the source and the target repository into a common parent directory

~~~
cd my_working_directory
git clone https://github.com/Zeiss/ZeissIQS-pages.git
git clone https://github.com/Zeiss/ZeissIQS.github.io.git
~~~

## Editing

### Editing process

* Edit the documentation source (mostly markdown files) in the ZeissIQS-pages directory.
* Execute 'make.bat' from that ZeissIQS-pages directory to update the target repository.
* You can preview the generated documentation by opening ZeissIQS.github.io/index.html in a browser.

### Hints

* The markdown syntax uses the [MyST parser extensions](https://myst-parser.readthedocs.io/en/latest/index.html).
* The project documentation is based on [sphinx](https://www.sphinx-doc.org/en/master/index.html).


## Uploading

* Commit both source and target directory

~~~
cd ZeissIQS-pages

# Perform edits
make.bat

git add -A
git commit -m "Some useful message"
git push

cd ..

cd ZeissIQS.github.io
git add -A
git commit -m "Some useful message"
git push
~~~

* After the changes have been pushed into the 'ZeissIQS.github.io' repository, the live pages at [](https://zeissiqs.github.io) will be updated automatically after app. one minute.
