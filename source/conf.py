# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'botbotbot'
copyright = '2021, Mineinjava, Astr0clad'
author = 'Mineinjava, Astr0clad'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxext.opengraph",
    "myst_parser",
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'furo'

#MARK: Theme Options
html_theme_options = {
    "light_css_variables": {

        "color-problematic": "#BF616A",

        # Base Colors
        "color-foreground-primary": "2E3440", # for main text and headings
        "color-foreground-secondary": "#3B4252", # for secondary text
        "color-foreground-muted": "#434C5E", # for muted text
        "color-foreground-border": "#4C566A", # for content borders

        "color-background-primary": "#ECEFF4", # for content
        "color-background-secondary": "#E5E9F0", # for navigation + ToC
        "color-background-hover": "#E5E9F0ff", # for navigation-item hover
        "color-background-hover-transparent": "#E5E9F000",
        "color-background-border": "#eeebee", #// for UI border
         # Announcements
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#D8DEE9",
         # Brand colors
        "color-brand-primary": "#81A1C1",
        "color-brand-content": "#5E81AC"

    },
    #MARK: Dark
    "dark_css_variables": {
        "color-problematic": "#BF616A",

        # Base Colors
        "color-foreground-primary": "#ECEFF4", # for main text and headings
        "color-foreground-secondary": "#E5E9F0", # for secondary text
        "color-foreground-muted": "#D8DEE9", # for muted text
        "color-foreground-border": "#4C566A", # for content borders

        "color-background-primary": "#2E3440", # for content
        "color-background-secondary": "#3B4252", # for navigation + ToC
        "color-background-hover": "#434C5Eff", # for navigation-item hover
        "color-background-hover-transparent": "#434C5E00",
        "color-background-border": "#434C5E", #// for UI border
         # Announcements
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#eeebee",
         # Brand colors
        "color-brand-primary": "#5E81AC",
        "color-brand-content": "#81A1C1"

    },
}

ogp_site_url = "https://d-botbotbot.github.io/docs/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
