import re
from pathlib import Path

class Classify:
    def __init__(self , ReadingPath:Path , WritingPath:Path):

            self.ReadingPath = Path(ReadingPath)
            self.WritingPath = Path(WritingPath)
            if not self.WritingPath.exists():
                self.WritingPath.write_text()
        

    def _read_file(self):
        try:
            return self.ReadingPath.read_text()
        except FileNotFoundError:
            print('the file doesn\'t exist check your path')

           
    def act(self , log_level:str):
        word = log_level
        logRegex = re.compile(rf'.+ {word} .*?(?=\n|\Z)')
        extracted_data = self._read_file()
        
        if log_level == 'DEBUG':
            debug_log = self.WritingPath/'debug.log'
            collected_de = logRegex.findall(extracted_data)
            de = '\n'.join(collected_de)
            debug_log.write_text(str(de))
            print('the debug.log has been created and filled with the debug data')

        elif log_level == 'INFO':
            info_log = self.WritingPath/'info.log'
            collected_inf = logRegex.findall(extracted_data)
            inf = '\n'.join(collected_inf)
            info_log.write_text(str(inf))
            print('the info.log has been created and filled with the info data')

        elif log_level == 'WARNING':
            warning_log = self.WritingPath/'warning.log'
            collected_war = logRegex.findall(extracted_data)
            war = '\n'.join(collected_war)
            warning_log.write_text(str(war))
            print('the warning.log has been created and filled with the warning data')

        elif log_level == 'ERROR':
            error_log = self.WritingPath/'error.log'
            collected_err = logRegex.findall(extracted_data)
            err = '\n'.join(collected_err)
            error_log.write_text(str(err))
            print('the error.log has been created and filled with the error data')

        elif log_level == 'CRITICAL':
            critical_log = self.WritingPath/'critical.log'
            collected_cri = logRegex.findall(extracted_data)
            cri = '\n'.join(collected_cri)
            critical_log.write_text(str(cri))
            print('the critical.log has been created and filled with the critical data')

        else:
            print('there is 5 levels :DEBUG,INFO,WARNING,ERROR,CRITICAL')

                
