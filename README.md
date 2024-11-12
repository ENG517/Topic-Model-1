# DITA Topic Model - Using Matplotlib with Python

This repo contains a DITA topic model (TM) related to creating visualizations using Pyhon and Matplotlib.

## Authors

- Ademola Adepoju
- Justin Watson

## PROJECT MAPS

### User Scenario 1: James - Data Science Student

James is a data science student who is working on a data visualization project for his data science course. James needs to create a clear and customizable line chart using Python and Matplotlib to present a dataset. While James is familiar with basic Python syntax, he is not familiar with the Matplotlib library. James is looking for a step-by-step tutorial that helps him create a line chart. Not only that, James wants to be able to customize it by adding his own title, axis labels, and gridlines. 


#### Topics

**Concept Topic**: matplotlib-overview, about-line-chart, line-chart-type

**Task Topic**: how-to-install-matplotlib, create-a-line-chart, customize-the-line-chart

**Reference Topic**: python-verification-commands, pip-verification-commands

### User Scenario 2: Clara - Novice Python User

Clara, a statistics professional new to Python, needs to create a simple bar chart to analyze survey data. She requires a straightforward guide from installation through basic chart creation and customization.

#### Topics

**Concept Topics**: matplotlib-overview

**Task Topics**: how-to-install-matplotlib, create-a-bar-chart

**Reference Topics**: python-verification-commands

### User Scenario 3: Richard - Experienced Data Scientist

Richard, an experienced data scientist, requires a quick reference for advanced Matplotlib customizations, such as annotations and style adjustments, for an executive presentation.

#### Topics

**Concept Topics**: matplotlib-overview and line-chart-type

**Task Topics**: customize-the-line-chart

**Reference Topics**: python-verification-commands, pip-verification-commands


## Folders &amp; Files

- `.github`: Contains configuration files for "Github Actions".
- `assets`: Contains all assets used within the TM.
- `concepts`: Contains all concept topics.
- `references`: Contains all reference topics.
- `tasks`: Contains all task topics.
- `shared`: Contains all topic files that are shared across multiple maps.
- `out`: Contains all output folders.
- `themes`: Contains `.yaml` style configuration files.
- **Skeleton files**: All topic folders contain a single "skeleton" topic file for you to copy, whenever you need to quickly create a new file.
- `.keep` **files**: Ignore these files. They ensure that any empty folders are tracked by git. 
- `.gitignore`: This file tells git which files to ignore in the repo. You can leave this one be.

## Filenaming Conventions

- Task Topics: `t_verb_verbobject.dita`
- Concept Topics: `c_nounphrase.dita`
- Reference Topics: It varies, but something akin to `r_types_of_nounphrase.dita`
- Dita Maps: `_modelname.ditamap`

## Building Outputs with Github Actions

This repo uses Github Actions to create outputs. Refer to the following for details: 

- [.github/workflows/dita-ot-build-actions.yaml](.github/workflows/dita-ot-build-actions.yaml)
- [DITA User Docs - Using Github Actions](https://www.dita-ot.org/dev/topics/using-github-actions)
- [DITA Example YAML files](https://github.com/dita-ot/docs/blob/develop/samples/github-actions/build-using-a-project-file.yaml)

## Building Outputs Manually with the Command Line

See the DITA-OT user guide about how to generate output: [https://www.dita-ot.org/dev/topics/build-using-dita-command](https://www.dita-ot.org/dev/topics/build-using-dita-command)

### Sample DITA Commands

#### Help

To see all of the commands and parameters, use the following command:

```
dita --help
```

#### DITA options and arguments

```
-f == dita output format
-i == dita input map file
-o == dita output directory
-D&lt;property&gt;=&lt;value&gt; == add custom args
    with particular values to dita transformation
-filter &lt;file&gt; == filter and flagging file
```

#### Create an HTML5 site

```
dita -f html5 -i 'url/to/your/wanted.ditamap' \
  -o 'url/to/your/output/folder' \
```

#### Create an HTML5 site with a custom CSS file

```
dita -f html5 -i 'url/to/your/wanted.ditamap' \
  -o 'url/to/your/output/folder' \
  -Dargs.cssroot='url/to/your/assets/folder' \
  -Dargs.css='${cssroot}/your-custom-css-file.css' \
  -Dargs.csspath='css' \
  -Dargs.copycss='yes'
```

#### Create a PDF

```
dita -f pdf -i 'url/to/your/wanted.ditamap' \
  -o 'url/to/your/output/folder' \
```
