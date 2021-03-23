# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import subprocess as sub
import csv

#Theme
sg.theme('DarkAmber')

#Define our two colums for the layout, 
venstre = [
	[sg.Text('Choose a test:',font=("Helvetica", 15))],
	[sg.Button('Speedtest',size=(10, 2),font=("Helvetica", 15))],
	[sg.Button('Bbk',size=(10, 2),font=("Helvetica", 15))],
	[sg.Button('Iperf3',size=(10, 2),font=("Helvetica", 15))],
	[sg.Button('MTR',size=(10, 2),font=("Helvetica", 15))],
	[sg.Text('_'*20)],
	[sg.Button('SEND RESULTS',size=(10, 2),font=("Helvetica", 15))]
]

#Results etc, need function to fill this
høyre = [
	[sg.Text("Speedtest results:",font=("Helvetica", 14))],
	[sg.Multiline(size=(100, 4),font=("Helvetica", 15),disabled=True, background_color='black', text_color='white', key='speed-log')],
	[sg.Text("Bbk results:",font=("Helvetica", 15))],
	[sg.Multiline(size=(100, 4),font=("Helvetica", 14),disabled=True, background_color='black', text_color='white', key='bbk-log')],
	[sg.Text("Iperf3 results:",font=("Helvetica", 15))],
	[sg.Multiline(size=(100, 4),font=("Helvetica", 14),disabled=True, background_color='black', text_color='white', key='iperf-log')]
]

#Full layout
layout = [
    [
        sg.Column(venstre),
        sg.VSeperator(),
        sg.Column(høyre),
    ]
]

#Main window 
#TODO: Set size, fullscreen max?
window = sg.Window('Speedtester', layout,size=(800,480))

#Definere hjelpefunksjoner 
#5 og 6 er hastigheten. 
#4 packetloss 3 ping 2 jitt
def speelog_upd():
	tsv_file = open("speed-log.tsv")
	read_tsv = csv.reader(tsv_file, delimiter="\t")
	for row in read_tsv:
		touple="Download: ",round(int(row[5])/125000,2)," Upload: ",round(int(row[6])/125000,2)," Loss: ",row[4]," Ping: ",row[2]," Jitter: ",row[3]
		built = ""
		for ele in touple:
			built += str(ele)
		window.FindElement('speed-log').print(built)

#Set windows maximized.
#window.Maximize() crashing with this lol

#Event handler wooo
while True:
    event, values = window.read()
    #Close window etc
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speedtest':
    	log_file = open("speed-log.tsv",'a')
    	#sg.Popup("Speedtest kjører", button_type=5)
    	window[SPeedtest].Update(disabled=True)
    	sub.run(["speedtest","--format=tsv"], stdout=log_file)
    	log_file.close()
    	speelog_upd()


window.close()

