# Import the ParFlow package
#
from parflow import Run
import os
import shutil 


#preliminaries
os.chdir('output')

# copy CLM files
shutil.copyfile('../inputs/drv_clmin.dat', 'drv_clmin.dat')
shutil.copyfile('../inputs/drv_vegm.dat', 'drv_vegm.dat')
shutil.copyfile('../inputs/drv_vegp.dat', 'drv_vegp.dat')

# Set our Run Name 
PFCLM_SC = Run("PFCLM_SC", __file__)


stopt = 8760

#-----------------------------------------------------------------------------
# File input version number
#-----------------------------------------------------------------------------
PFCLM_SC.FileVersion = 4

#-----------------------------------------------------------------------------
# Process Topology
#-----------------------------------------------------------------------------

PFCLM_SC.Process.Topology.P = 1
PFCLM_SC.Process.Topology.Q = 1
PFCLM_SC.Process.Topology.R = 1

#-----------------------------------------------------------------------------
# Computational Grid
#-----------------------------------------------------------------------------
PFCLM_SC.ComputationalGrid.Lower.X = 0.0
PFCLM_SC.ComputationalGrid.Lower.Y = 0.0
PFCLM_SC.ComputationalGrid.Lower.Z = 0.0

PFCLM_SC.ComputationalGrid.DX      = 2.0
PFCLM_SC.ComputationalGrid.DY      = 2.0
PFCLM_SC.ComputationalGrid.DZ      = 0.1

PFCLM_SC.ComputationalGrid.NX      = 1
PFCLM_SC.ComputationalGrid.NY      = 1
PFCLM_SC.ComputationalGrid.NZ      = 20

#-----------------------------------------------------------------------------
# The Names of the GeomInputs
#-----------------------------------------------------------------------------
PFCLM_SC.GeomInput.Names = 'domain_input'

#-----------------------------------------------------------------------------
# Domain Geometry Input
#-----------------------------------------------------------------------------
PFCLM_SC.GeomInput.domain_input.InputType = 'Box'
PFCLM_SC.GeomInput.domain_input.GeomName  = 'domain'

#-----------------------------------------------------------------------------
# Domain Geometry
#-----------------------------------------------------------------------------
PFCLM_SC.Geom.domain.Lower.X = 0.0
PFCLM_SC.Geom.domain.Lower.Y = 0.0
PFCLM_SC.Geom.domain.Lower.Z = 0.0

PFCLM_SC.Geom.domain.Upper.X = 2.0
PFCLM_SC.Geom.domain.Upper.Y = 2.0
PFCLM_SC.Geom.domain.Upper.Z = 2.0

PFCLM_SC.Geom.domain.Patches = 'x_lower x_upper y_lower y_upper z_lower z_upper'


#--------------------------------------------
# variable dz assignments
#------------------------------------------

PFCLM_SC.Solver.Nonlinear.VariableDz = True
PFCLM_SC.dzScale.GeomNames           = 'domain'
PFCLM_SC.dzScale.Type                = 'nzList'
PFCLM_SC.dzScale.nzListNumber        = 20

# cells start at the bottom (0) and moves up to the top
# domain is 3.21 m thick, root zone is down to 19 cells 
# so the root zone is 2.21 m thick
PFCLM_SC.Cell._0.dzScale.Value  = 10.0   # first cell is 10*0.1 1m thick
PFCLM_SC.Cell._1.dzScale.Value  = 5.0    # next cell is 5*0.1 50 cm thick
PFCLM_SC.Cell._2.dzScale.Value  = 1.0   
PFCLM_SC.Cell._3.dzScale.Value  = 1.0
PFCLM_SC.Cell._4.dzScale.Value  = 1.0
PFCLM_SC.Cell._5.dzScale.Value  = 1.0
PFCLM_SC.Cell._6.dzScale.Value  = 1.0
PFCLM_SC.Cell._7.dzScale.Value  = 1.0
PFCLM_SC.Cell._8.dzScale.Value  = 1.0
PFCLM_SC.Cell._9.dzScale.Value  = 1.0
PFCLM_SC.Cell._10.dzScale.Value = 1.0
PFCLM_SC.Cell._11.dzScale.Value = 1.0
PFCLM_SC.Cell._12.dzScale.Value = 1.0
PFCLM_SC.Cell._13.dzScale.Value = 1.0
PFCLM_SC.Cell._14.dzScale.Value = 1.0
PFCLM_SC.Cell._15.dzScale.Value = 1.0
PFCLM_SC.Cell._16.dzScale.Value = 1.0
PFCLM_SC.Cell._17.dzScale.Value = 1.0
PFCLM_SC.Cell._18.dzScale.Value = 1.0
PFCLM_SC.Cell._19.dzScale.Value = 0.1   #0.1* 0.1 = 0.01  1 cm top layer

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------
PFCLM_SC.Geom.Perm.Names              = 'domain'
PFCLM_SC.Geom.domain.Perm.Type        = 'Constant'
PFCLM_SC.Geom.domain.Perm.Value       = 0.001465
PFCLM_SC.Perm.TensorType              = 'TensorByGeom'
PFCLM_SC.Geom.Perm.TensorByGeom.Names = 'domain'
PFCLM_SC.Geom.domain.Perm.TensorValX  = 1.0
PFCLM_SC.Geom.domain.Perm.TensorValY  = 1.0
PFCLM_SC.Geom.domain.Perm.TensorValZ  = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

PFCLM_SC.SpecificStorage.Type              = 'Constant'
PFCLM_SC.SpecificStorage.GeomNames         = 'domain'
PFCLM_SC.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

PFCLM_SC.Phase.Names = 'water'

PFCLM_SC.Phase.water.Density.Type     = 'Constant'
PFCLM_SC.Phase.water.Density.Value    = 1.0

PFCLM_SC.Phase.water.Viscosity.Type   = 'Constant'
PFCLM_SC.Phase.water.Viscosity.Value  = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------
PFCLM_SC.Contaminants.Names = ''


#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

PFCLM_SC.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

PFCLM_SC.TimingInfo.BaseUnit     = 1.0
PFCLM_SC.TimingInfo.StartCount   = 0
PFCLM_SC.TimingInfo.StartTime    = 0.0
PFCLM_SC.TimingInfo.StopTime     = stopt
PFCLM_SC.TimingInfo.DumpInterval = 1.0
PFCLM_SC.TimeStep.Type           = 'Constant'
PFCLM_SC.TimeStep.Value          = 1.0


#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

PFCLM_SC.Geom.Porosity.GeomNames    = 'domain'

PFCLM_SC.Geom.domain.Porosity.Type  = 'Constant'
PFCLM_SC.Geom.domain.Porosity.Value = 0.3

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------
PFCLM_SC.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Mobility
#-----------------------------------------------------------------------------
PFCLM_SC.Phase.water.Mobility.Type  = 'Constant'
PFCLM_SC.Phase.water.Mobility.Value = 1.0

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

PFCLM_SC.Phase.RelPerm.Type        = 'VanGenuchten'
PFCLM_SC.Phase.RelPerm.GeomNames   = 'domain'

PFCLM_SC.Geom.domain.RelPerm.Alpha = 2.0
PFCLM_SC.Geom.domain.RelPerm.N     = 2.0

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

PFCLM_SC.Phase.Saturation.Type        = 'VanGenuchten'
PFCLM_SC.Phase.Saturation.GeomNames   = 'domain'

PFCLM_SC.Geom.domain.Saturation.Alpha = 2.0
PFCLM_SC.Geom.domain.Saturation.N     = 3.0
PFCLM_SC.Geom.domain.Saturation.SRes  = 0.2
PFCLM_SC.Geom.domain.Saturation.SSat  = 1.0

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------
PFCLM_SC.Wells.Names = ''


#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------
PFCLM_SC.Cycle.Names = 'constant'
PFCLM_SC.Cycle.constant.Names = 'alltime'
PFCLM_SC.Cycle.constant.alltime.Length = 1
PFCLM_SC.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------
PFCLM_SC.BCPressure.PatchNames = 'x_lower x_upper y_lower y_upper z_lower z_upper'

PFCLM_SC.Patch.x_lower.BCPressure.Type          = 'FluxConst'
PFCLM_SC.Patch.x_lower.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.x_lower.BCPressure.alltime.Value = 0.0

PFCLM_SC.Patch.y_lower.BCPressure.Type          = 'FluxConst'
PFCLM_SC.Patch.y_lower.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.y_lower.BCPressure.alltime.Value = 0.0

#PFCLM_SC.Patch.z_lower.BCPressure.Type = 'FluxConst'
PFCLM_SC.Patch.z_lower.BCPressure.Type          = 'DirEquilRefPatch'
PFCLM_SC.Patch.z_lower.BCPressure.RefGeom       = 'domain'
PFCLM_SC.Patch.z_lower.BCPressure.RefPatch      = 'z_lower'
PFCLM_SC.Patch.z_lower.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.z_lower.BCPressure.alltime.Value = 0.0

PFCLM_SC.Patch.x_upper.BCPressure.Type          = 'FluxConst'
PFCLM_SC.Patch.x_upper.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.x_upper.BCPressure.alltime.Value = 0.0

PFCLM_SC.Patch.y_upper.BCPressure.Type          = 'FluxConst'
PFCLM_SC.Patch.y_upper.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.y_upper.BCPressure.alltime.Value = 0.0

PFCLM_SC.Patch.z_upper.BCPressure.Type          = 'OverlandFlow'
PFCLM_SC.Patch.z_upper.BCPressure.Cycle         = 'constant'
PFCLM_SC.Patch.z_upper.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

PFCLM_SC.TopoSlopesX.Type              = 'Constant'
PFCLM_SC.TopoSlopesX.GeomNames         = 'domain'
PFCLM_SC.TopoSlopesX.Geom.domain.Value = 0.05

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

PFCLM_SC.TopoSlopesY.Type              = 'Constant'
PFCLM_SC.TopoSlopesY.GeomNames         = 'domain'
PFCLM_SC.TopoSlopesY.Geom.domain.Value = 0.00

#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

PFCLM_SC.Mannings.Type               = 'Constant'
PFCLM_SC.Mannings.GeomNames          = 'domain'
PFCLM_SC.Mannings.Geom.domain.Value  = 2.e-6

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

PFCLM_SC.PhaseSources.water.Type              = 'Constant'
PFCLM_SC.PhaseSources.water.GeomNames         = 'domain'
PFCLM_SC.PhaseSources.water.Geom.domain.Value = 0.0

#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

PFCLM_SC.KnownSolution = 'NoKnownSolution'

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

PFCLM_SC.Solver         = 'Richards'
PFCLM_SC.Solver.MaxIter = 9000

PFCLM_SC.Solver.Nonlinear.MaxIter           = 100
PFCLM_SC.Solver.Nonlinear.ResidualTol       = 1e-5
PFCLM_SC.Solver.Nonlinear.EtaChoice         = 'Walker1'
PFCLM_SC.Solver.Nonlinear.EtaValue          = 0.01
PFCLM_SC.Solver.Nonlinear.UseJacobian       = False
PFCLM_SC.Solver.Nonlinear.DerivativeEpsilon = 1e-12
PFCLM_SC.Solver.Nonlinear.StepTol           = 1e-30
PFCLM_SC.Solver.Nonlinear.Globalization     = 'LineSearch'
PFCLM_SC.Solver.Linear.KrylovDimension      = 100
PFCLM_SC.Solver.Linear.MaxRestarts          = 5
PFCLM_SC.Solver.Linear.Preconditioner       = 'PFMG'
PFCLM_SC.Solver.PrintSubsurf                = False
PFCLM_SC.Solver.Drop                        = 1E-20
PFCLM_SC.Solver.AbsTol                      = 1E-9

#Writing output options for ParFlow
#  PFB only no SILO
PFCLM_SC.Solver.PrintSubsurfData         = True
PFCLM_SC.Solver.PrintPressure            = True
PFCLM_SC.Solver.PrintSaturation          = True
PFCLM_SC.Solver.PrintCLM                 = True
PFCLM_SC.Solver.PrintMask                = True
PFCLM_SC.Solver.PrintSpecificStorage     = True
PFCLM_SC.Solver.WriteSiloMannings        = False
PFCLM_SC.Solver.WriteSiloMask            = False
PFCLM_SC.Solver.WriteSiloSlopes          = False
PFCLM_SC.Solver.WriteSiloSaturation      = False

#---------------------------------------------------
# LSM / CLM options
#---------------------------------------------------

# set LSM options to CLM
PFCLM_SC.Solver.LSM              = 'CLM'
# specify type of forcing, file name and location
PFCLM_SC.Solver.CLM.MetForcing   = '1D'
#PFCLM_SC.Solver.CLM.MetFileName = 'forcing_1.txt'
PFCLM_SC.Solver.CLM.MetFileName  = 'narr_1hr.txt'
PFCLM_SC.Solver.CLM.MetFilePath  = '../forcing'

# Set CLM Plant Water Use Parameters
PFCLM_SC.Solver.CLM.EvapBeta       = 'Linear'
PFCLM_SC.Solver.CLM.VegWaterStress = 'Saturation'
PFCLM_SC.Solver.CLM.ResSat         = 0.2
PFCLM_SC.Solver.CLM.WiltingPoint   = 0.2
PFCLM_SC.Solver.CLM.FieldCapacity  = 1.00
PFCLM_SC.Solver.CLM.IrrigationType = 'none'
PFCLM_SC.Solver.CLM.RootZoneNZ     =  19
PFCLM_SC.Solver.CLM.SoiLayer       =  15

#Writing output options for CLM
#  PFB only, no SILO, no native CLM logs
PFCLM_SC.Solver.PrintLSMSink        = False
PFCLM_SC.Solver.CLM.CLMDumpInterval = 1
PFCLM_SC.Solver.CLM.CLMFileDir      = 'output/'
PFCLM_SC.Solver.CLM.BinaryOutDir    = False
PFCLM_SC.Solver.CLM.IstepStart      = 1
PFCLM_SC.Solver.WriteCLMBinary      = False
PFCLM_SC.Solver.WriteSiloCLM        = False
PFCLM_SC.Solver.CLM.WriteLogs       = False
PFCLM_SC.Solver.CLM.WriteLastRST    = True
PFCLM_SC.Solver.CLM.DailyRST        = False
PFCLM_SC.Solver.CLM.SingleFile      = True

#---------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------

PFCLM_SC.ICPressure.Type                 = 'HydroStaticPatch'
PFCLM_SC.ICPressure.GeomNames            = 'domain'
PFCLM_SC.Geom.domain.ICPressure.Value    = -1.0
PFCLM_SC.Geom.domain.ICPressure.RefGeom  = 'domain'
PFCLM_SC.Geom.domain.ICPressure.RefPatch = 'z_upper'

#-----------------------------------------------------------------------------
# Run ParFlow 
#-----------------------------------------------------------------------------

PFCLM_SC.run()
