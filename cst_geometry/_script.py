import os

_script_source = '''Sub Main()
geometry_file = "{}"

Dim studio As Object
'Starts CST MICROWAVE STUDIO
Set studio = CreateObject("CSTStudio.Application")
Dim proj As Object
Set proj = studio.Active3D

Dim Text As String, textline As String, posLat As Integer, posLong As Integer
Dim t As String
Dim route As String, Output As String


Component.New "Geometry"
Dim tau As Double
Dim i,j,l As Integer

Dim x0(1000) As Double
Dim y0(1000) As Double
Dim z0(1000) As Double
Dim x1(1000) As Double
Dim y1(1000) As Double
Dim z1(1000) As Double


Dim row() As String


Open geometry_file For Input As #1
Do Until EOF(1)
    Line Input #1, textline
    row = Split(textline)
	If (UBound(row) - LBound(row) + 1) = 2 Then
		number_of_wires = CInt(row(0))
		radius_of_wire = CDbl(row(1)) * 100
	Else
		x0(i) = CDbl(row(0))
		y0(i) = CDbl(row(1))
		z0(i) = CDbl(row(2))
		x1(i) = CDbl(row(3))
		y1(i) = CDbl(row(4))
		z1(i) = CDbl(row(5))
	i += 1
	End If
Loop
Close #1

StoreDoubleParameter "r", radius_of_wire
SetParameterDescription  ( "r",  "wire radius"  )
StoreDoubleParameter "N", number_of_wires
SetParameterDescription  ( "N",  "Number of wires"  )


t = ""
For i=0 To number_of_wires - 1
	t = t & "With Wire" & vbCrLf
	     t = t & ".Reset" & vbCrLf
	     t = t & ".Name ""c" & CStr(i) & """" & vbCrLf
	     t = t & ".Folder ""Geometry""" & vbCrLf
	     t = t & ".Type ""BondWire""" & vbCrLf
	     t = t & ".Material ""PEC""" & vbCrLf
	     t = t & ".Radius ""r""" & vbCrLf
		  t = t &   ".Point1 " & CStr(x0(i)) & ", " &  CStr(y0(i)) & ", " &  CStr(z0(i)) & ", ""False""" & vbCrLf
		  t = t &   ".Point2 " & CStr(x1(i)) & ", " &  CStr(y1(i)) & ", " &  CStr(z1(i)) & ", ""False""" & vbCrLf
		  t = t &   ".BondWireType ""Spline""" & vbCrLf
		  t = t &   ".Alpha ""75""" & vbCrLf
		  t = t &   ".Beta ""35""" & vbCrLf
		  t = t &   ".RelativeCenterPosition ""0.5""" & vbCrLf
		   t = t &  ".SolidWireModel ""False""" & vbCrLf
		  t = t &   ".Termination ""Extended""" & vbCrLf
	     t = t & ".add" & vbCrLf
	t = t & "End With" & vbCrLf
Next
	AddToHistory("make geometry", t)

't = ""
'For i=0 To number_of_wires - 1
	't = t & "With Cylinder" & vbCrLf
	     't = t & ".Reset" & vbCrLf
	     't = t & ".Name ""c" & CStr(i) & """" & vbCrLf
	     't = t & ".Component ""Geometry""" & vbCrLf
	     't = t & ".Material ""PEC""" & vbCrLf
	     't = t & ".OuterRadius ""r""" & vbCrLf
	     't = t & ".InnerRadius ""0""" & vbCrLf
	     't = t & ".Axis ""y""" & vbCrLf
	     't = t & ".Yrange " & CStr(z0(i)) & ", " &  CStr(z1(i)) & vbCrLf
	     't = t & ".Xcenter " & CStr(y0(i)) & vbCrLf
	     't = t & ".Zcenter " & CStr(x0(i)) & vbCrLf
	     't = t & ".Segments ""0""" & vbCrLf
	     't = t & ".Create" & vbCrLf
	't = t & "End With" & vbCrLf
'Next
	'AddToHistory("make cubic geometry", t)

AddToHistory("make planewave", "With PlaneWave" & vbCrLf & _
     ".Reset" & vbCrLf & _
     ".Normal ""-1"", ""0"", ""0""" & vbCrLf & _
     ".EVector ""0"", ""0"", ""1""" & vbCrLf & _
     ".Polarization ""Linear""" & vbCrLf & _
     ".ReferenceFrequency ""0""" & vbCrLf & _
     ".PhaseDifference ""-90.0""" & vbCrLf & _
     ".CircularDirection ""Left""" & vbCrLf & _
     ".AxialRatio ""0.0""" & vbCrLf & _
     ".SetUserDecouplingPlane ""False""" & vbCrLf & _
     ".Store" & vbCrLf & _
"End With")

AddToHistory("make monitors", "With Monitor" & vbCrLf & _
          ".Reset" & vbCrLf & _
          ".Domain ""Frequency""" & vbCrLf & _
          ".FieldType ""Farfield""" & vbCrLf & _
          ".ExportFarfieldSource ""False""" & vbCrLf & _
          ".UseSubvolume ""False""" & vbCrLf & _
          ".Coordinates ""Structure""" & vbCrLf & _
          ".SetSubvolume ""-30.25"", ""30.25"", ""-70.5"", ""70.5"", ""-30.25"", ""30.25""" & vbCrLf & _
          ".SetSubvolumeOffset ""10"", ""10"", ""10"", ""10"", ""10"", ""10""" & vbCrLf & _
          ".SetSubvolumeInflateWithOffset ""False""" & vbCrLf & _
          ".SetSubvolumeOffsetType ""FractionOfWavelength""" & vbCrLf & _
          ".EnableNearfieldCalculation ""True""" & vbCrLf & _
          ".CreateUsingLinearSamples ""5"", ""7"", ""20""" & vbCrLf & _
"End With")

AddToHistory("make probe","With Probe" & vbCrLf & _
     ".Reset"  & vbCrLf & _
     ".ID 0" & vbCrLf & _
     ".AutoLabel 1"  & vbCrLf & _
     ".Field ""RCS"""  & vbCrLf & _
     ".Orientation ""All"""  & vbCrLf & _
     ".SetPosition1 ""-10"""  & vbCrLf & _
     ".SetPosition2 ""0.0"""  & vbCrLf & _
     ".SetPosition3 ""0.0"""   & vbCrLf & _
     ".SetCoordinateSystemType ""Cartesian"""  & vbCrLf & _
     ".Create"  & vbCrLf & _
"End With")

	Dim sCommand As String

	'@ define units
	sCommand = ""
	sCommand = sCommand + "With Units " + vbLf
	sCommand = sCommand + ".Geometry ""mm""" + vbLf
	sCommand = sCommand + ".Frequency ""GHz""" + vbLf
	sCommand = sCommand + ".Time ""ns""" + vbLf
	sCommand = sCommand + "End With"
	AddToHistory "define units", sCommand

AddToHistory("Set frequency Solver", "ChangeSolverType ""HF Frequency Domain""")


proj.SaveAs "{}", True
proj.Quit
Set studio = Nothing
End Sub'''


class Script:
    def __init__(self, name, route_geometry, route_cst):
        self.create_script(name, route_geometry, route_cst)

    @staticmethod
    def create_script(name, route_geometry, route_cst):
        path_to_geometry = os.path.abspath(f"{route_geometry}\{name}.txt")
        path_to_cst_file = os.path.abspath(f"{route_cst}\{name}.cst")
        source = _script_source.format(path_to_geometry, path_to_cst_file)

        with open(os.path.abspath('script.bas'), 'w+') as f:
            for line in source.split('\n'):
                f.write(f'{line}\n')
            print(f'script added at {os.path.abspath("script.bas")}')

    @staticmethod
    def remove_script():
        os.remove(os.path.abspath('script.bas')); print(f'script removed from {os.path.abspath("script.bas")}')
        print(f'script removed from {os.path.abspath("script.bas")}')


