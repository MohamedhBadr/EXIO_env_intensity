# EXIO_env_intensity
Comparison of environmental intensity of economic production over time using EXIOBASE3
Throughout this analysis the Pymrio python library is used to parse and read in EXIOBASE3
link: https://pymrio.readthedocs.io/en/latest/intro.html#

How do consumption related impact multipliers (i.e., the environmental intensity of purchasing 1EUR of a sectors product) change over time? To what extent is the multiplier reduced over time, and will this rate be enough to achieve substantial reductions in environmental impacts if the current trends, including increases in consumption, continue? Which sectors are particularly relevant, and will there be a limit to how much individual sectors, or the whole economy, can become less intensive? Make a choice of indicator (carbon, land, biodiversity, materials) and regions.

Current Prgress: until now the Pymrio library is used to parse EXIOBASE.For now I use the two years 1995 and 2011. Pymrio offers automated calculations of all matrices. Using the calc_all() function we can get the M matrix (multipliers) which we can then use for our analysis. We still need to choose indicators and regions.
