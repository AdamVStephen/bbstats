#!/usr/bin/env python
"""
Screenscrape statistics from broadband router and update GoogleDocs spreadsheet.
"""
import subprocess
import time
#from gdocs import LogRowInGDocSpreadsheet
from gdocs import LogRowInBBstats

client_id       = ""
client_secret   = ""
spreadsheet_key = ""
headings = ["Date", "Upstream", "Downstream"] #column headings can't have spaces

BB_ERR_SIM = {'condition' : 'simulated data - do not confuse with real'}


def bbPoll():
    '''Screenscrape the statistics data from the BB router.'''
    sample = {'Error' : BB_ERR_SIM,  'Upstream' : 0,  'Downstream' : 0}
    # TODO implement screenscrape
    return sample

def main():
        # This is the main routine of the program

        # set how long to wait between logs
        poll_interval = 30

        # Get the start time
        timer = time.time() - poll_interval

        # main loop forever
        while (True):
                #log the temperature every X seconds
                if time.time() - timer > poll_interval:
                        # get the latest temperature from
                        #the sensor
                        sample = bbPoll()
                        if (sample['Error' == BB_ERR_SIM):
                                #reset the timer and try again
                                #after the 5 min delay
                                start_time = time.time()
                                # TODO : use logging, not print
                                print("simulation : Upstream %f\tDownstream %f\n" % (sample["Upstream"], sample["Downstream"])
                                continue

                        timestamp = time.time()
                        upstream = sample["Upstream"]
                        downstream = sample["Downstream"]

                        #Send the temperature reading to Google Docs
                        LogRowInGDocSpreadsheet(client_id, client_secret, spreadsheet_key, headings, timestamp, upstream, downstream);

                        # reset the timer
                        timer = time.time()
                time.sleep(.2)

if __name__ == "__main__":
        main()

