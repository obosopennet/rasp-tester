# rasp-tester
Simple testing program for third-party technicians to use for testing at customer premises. 

Quick description of buttons: 
Speedtest: starts a speedtest towards an auto selected server, output is piped to speed-log.tsv 
When the test is done .tsv output is converted to readable form and printed. 

Bbk: starts a speedtest towards an auto selected bredbandskollen server, output is gotten via bbk-log and converted for printing. 

Iperf3: Starts a speedtest salvo towards on of our servers in the core. Output is not presented for now. 

SEND RESULTS: Uploads all logs to server. 
