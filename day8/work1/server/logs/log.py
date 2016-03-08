import logging
def logger():
        logs = logging.getLogger('Ftplog')
        logs.setLevel(logging.INFO)
        #bin to file
        logfile = logging.FileHandler('ftp_log.log')
        logfile.setLevel(logging.INFO)
        #bin to console
        logconsole = logging.StreamHandler()
        logconsole.setLevel(logging.INFO)
        formaters =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logfile.setFormatter( formaters )
        logconsole.setFormatter(formaters)
        logs.addHandler( logfile )
        logs.addHandler(logconsole)
        return logs