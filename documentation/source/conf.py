# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "VerTIGo"
copyright = "2024, Alexandre Tuleu"
author = "Alexandre Tuleu"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.githubpages", "sphinx.ext.duration"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "source_repository": "https://github.com/iNkawuVervetProject/vertigo",
    "source_branch": "main",
    "source_directory": "documentation/source",
}
