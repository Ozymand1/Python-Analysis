#!/usr/bin/python3.9

from ROOT import TFile, TTree, TH1D

file = TFile('pions_3.root')
hists = dict()
TOF = TH1D('tof', 'tof', 1000, 0, 8)
tree = file.Get('hits')
output = TFile('output.root', 'RECREATE')

print(tree.GetEntries())

for entry in tree:
	if(entry.det == 4):
		TOF.Fill(entry.tof)

TOF.Write()
