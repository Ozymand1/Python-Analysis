#!/usr/bin/python3.9

from ROOT import TF2, TFile, TCanvas

proton_mass = 938
pion_mass = 140

output = TFile('func.root', 'RECREATE')

momentum = 1000

Length = 1

sigma = 0.1

c = 3*10**8

func = TF2('sigma', 'y/([0]*x)*(sqrt([1]*[1]+x*x)-sqrt([2]*[2]+x*x))', 0.5*momentum, 1.5*momentum, 0.1*Length, 1.5*Length)
func2 = TF2('cut', '10^(-10)', 0.5*momentum, 1.5*momentum, 0.1*Length, 1.5*Length)
func.SetParameters(c, proton_mass, pion_mass)
c1 = TCanvas('c1', 'c1', 200, 10, 1920, 1080)
print(func.Eval(1, 1.8))
func2.Draw('surf4')
func.Draw('surf4, SAME')

c1.Write()