# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Genomics Requisition System User Manual'
copyright = '2025, OICR Genomics'
author = 'Morgan Taschuk'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
	"logo_only": "True",
	"style_nav_header_background":"white"
}
#https://www.sphinx-doc.org/en/master/usage/configuration.html
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_logo = 'images/logo-genomics-forms.png'
html_title = "OICR Genomics Requisition System User Manual"
html_favicon = "images/favicon.png"
