from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env, alnfile = 'seqs.ali', knowns = 'vp1', sequence = 'GQ121419')
a.starting_model = 1
a.ending_model =1
a.library_scedule=autosched.slow
a.max_var_iterations = 300
a.md_level=refine.slow
a.max_molpdf = 1e6
a.make()
