# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ZEISS Industrial Quality Solutions'
copyright = '2024, Carl Zeiss GOM Metrology GmbH'
author = 'Carl Zeiss GOM Metrology GmbH'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinx_favicon', 'sphinx_sitemap']
source_suffix = ['.rst', '.md']
exclude_patterns = ['README.md']

# -- Options for sitemap -----------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/en/latest/getting-started.html
html_baseurl = 'https://zeissiqs.github.io/'
sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# Do not show "View page source" link on every page
html_show_sourcelink = False

html_theme = "sphinx_rtd_theme"

# "sphinx_rtd_theme" appends " &mdash; <project>  documentation" to the page heading -
# this changes the title to "<page_heading> &mdash; <project>"
html_title = project

html_static_path = ["_static"]  # html_static_path is required if you use the "static-file" parameter

# -- Override some Read the Docs styles to match ZEISS branding ---------------
# https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
html_style = "css/theme_zeiss.css"

favicons = [
    {
        "rel": "icon",
        "sizes": "16x16",
        "static-file": "favicon.png",  # => use `_static/favicon.png`
        "type": "image/png",
    }
]

# Source: https://brand.zeiss.com/cmsPublic/brandportal/basic-design-elements/logo-tagline.html
html_logo =  "_static/zeiss-logo-rgb.png"
