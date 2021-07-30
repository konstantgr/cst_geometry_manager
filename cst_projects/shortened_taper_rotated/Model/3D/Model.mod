'# MWS Version: Version 2021.2 - Jan 06 2021 - ACIS 30.0.1 -

'# length = mm
'# frequency = GHz
'# time = ns
'# frequency range: fmin = 0.0 fmax = 0.0
'# created = '[VERSION]2021.2|30.0.1|20210106[/VERSION]


'@ make geometry

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
With Wire
.Reset
.Name "c0"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 5, 0, 0, "False"
.Point2 1, 0, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c1"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 3.53553390593274, 3.53553390593274, 0, "False"
.Point2 0.707106781186548, 0.707106781186548, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c2"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 3.06161699786838E-16, 5, 0, "False"
.Point2 6.12323399573677E-17, 1, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c3"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 -3.53553390593274, 3.53553390593274, 0, "False"
.Point2 -0.707106781186547, 0.707106781186548, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c4"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 -5, 6.12323399573677E-16, 0, "False"
.Point2 -1, 1.22464679914735E-16, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c5"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 -3.53553390593274, -3.53553390593274, 0, "False"
.Point2 -0.707106781186548, -0.707106781186547, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c6"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 -9.18485099360515E-16, -5, 0, "False"
.Point2 -1.83697019872103E-16, -1, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With
With Wire
.Reset
.Name "c7"
.Folder "Geometry"
.Type "BondWire"
.Material "PEC"
.Radius "r"
.Point1 3.53553390593274, -3.53553390593274, 0, "False"
.Point2 0.707106781186547, -0.707106781186548, 3, "False"
.BondWireType "Spline"
.Alpha "75"
.Beta "35"
.RelativeCenterPosition "0.5"
.SolidWireModel "False"
.Termination "Extended"
.add
End With

'@ make planewave

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
With PlaneWave
.Reset
.Normal "-1", "0", "0"
.EVector "0", "0", "1"
.Polarization "Linear"
.ReferenceFrequency "0"
.PhaseDifference "-90.0"
.CircularDirection "Left"
.AxialRatio "0.0"
.SetUserDecouplingPlane "False"
.Store
End With

'@ make monitors

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
With Monitor
.Reset
.Domain "Frequency"
.FieldType "Farfield"
.ExportFarfieldSource "False"
.UseSubvolume "False"
.Coordinates "Structure"
.SetSubvolume "-30.25", "30.25", "-70.5", "70.5", "-30.25", "30.25"
.SetSubvolumeOffset "10", "10", "10", "10", "10", "10"
.SetSubvolumeInflateWithOffset "False"
.SetSubvolumeOffsetType "FractionOfWavelength"
.EnableNearfieldCalculation "True"
.CreateUsingLinearSamples "5", "7", "20"
End With

'@ make probe

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
With Probe
.Reset
.ID 0
.AutoLabel 1
.Field "RCS"
.Orientation "All"
.SetPosition1 "-10"
.SetPosition2 "0.0"
.SetPosition3 "0.0"
.SetCoordinateSystemType "Cartesian"
.Create
End With

'@ define units

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
With Units 
.Geometry "mm"
.Frequency "GHz"
.Time "ns"
End With

'@ Set frequency Solver

'[VERSION]2021.2|30.0.1|20210106[/VERSION]
ChangeSolverType "HF Frequency Domain"

