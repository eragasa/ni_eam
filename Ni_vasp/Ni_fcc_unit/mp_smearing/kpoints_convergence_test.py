import numpy as np
#import pyflamestk.base as base
#import pyflamestk.vasp as vasp

poscar_in = "../structures/unrelaxed/Ni_fcc_unit.vasp" 

def kpoints_automatic_mesh(fname_out='KPOINTS',
                           nkpoints=0,
                           length=10):
    """
    nkpoints (int) - if set to zero, then automatic

    """

    str_out  = "Automatic mesh\n"
    str_out += "{} ! number of kpoints 0 => automatic generation scheme\n".format(nkpoints)
    str_out += "Auto\n"
    str_out += "{} ! length (l)\n".format(length)

    f.open(fname_out,"w")
    f.write(str_out)
    f.close()

def incar_file(fname_out='INCAR',
               system='fcc Ni',
               smear_type='gaussian',
               sigma=0.05):
    str_out  = "SYSTEM = {}\n".format('fcc Ni')
    str_out += "ISTART = {}\n".format(0)
    str_out += "ICHARG = {}\n".format(2)
    str_out += "ENCUT = {}\n".format(270)
    str_out += "\n"
    str_out += "# Treatment of final occupancies\n"
    str_out += "ISMEAR = 0\n # Gaussian smearing"
    str_out += "SIGMA = {}\n".format(sigma)

def potcar_file(fname_out="POTCAR"):
    pass

def poscar_file(fname_in="POSCAR",fname_out="POSCAR"):
    pass    

def kpoints_convergence_automatic_mesh(l_low=10,l_high=100,l_step=10):
    l_vector  = range(l_low,l_high+1,l_step)
    dir_names = ['kp_{}'.format(v) for v in l_vector]
    for i,v in enumerate(l_vector):
        print(i,v,dir_names[i])


l_low = 10; l_high = 100; l_step= 10
kpoints_convergence_automatic_mesh(l_low,l_high,l_step)
