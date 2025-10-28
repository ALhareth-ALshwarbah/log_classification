import pytest
import subprocess
from pathlib import Path

def test_cli(tmp_path):
    reading_temp = tmp_path/'sometime.json'
    writing_temp = tmp_path

    reading_temp.write_text('''
[2025-10-15 09:00:01] DEBUG    Starting system diagnostics or user: dev_admin\n
[2025-10-15 09:00:09] INFO     Application startup complete\n
[2025-10-15 09:00:16] WARNING  Slow response from API endpoint /fetch-data (2.4s)\n
[2025-10-15 09:00:22] ERROR    Database connection lost: db-prod-02\n
[2025-10-15 09:00:29] CRITICAL System instability detected — entering safe mode
                            ''')

    cli_arg = ['--de', '--inf', '--war', '--err', '--cri']
    levels_log = ['debug', 'info', 'warning', 'error','critical']

    for arg,level in zip(cli_arg,levels_log): 
        result = subprocess.run(['python','-m','classification.CLI',str(reading_temp),str(writing_temp),arg],
                    capture_output = True,
                    text = True)
        print(result.stderr)
        assert result.returncode == 0
        assert result.stdout.strip() == f'the {level}.log has been created and filled with the {level} data'

        if cli_arg == '--de':
            debug_log = writing_temp/'debug.log'
            read_debug = debug_log.read_text()
            assert '[2025-10-15 09:00:01] DEBUG    Starting system diagnostics or user: dev_admin' in debug_log

        elif cli_arg == '--inf':
            info_log = writing_temp/'info.log'
            read_info = info_log.read_text()
            assert '[2025-10-15 09:00:09] INFO     Application startup complete' in info_log

        elif cli_arg == '--war':
            warning_log = writing_temp/'warning.log'
            read_warning = warning_log.read_text()
            assert '[2025-10-15 09:00:16] WARNING  Slow response from API endpoint /fetch-data (2.4s)' in read_warning

        elif cli_arg == '--err':
            error_log = writing_temp/'error.log'
            read_error = error_log.read_text()
            assert '[2025-10-15 09:00:22] ERROR    Database connection lost: db-prod-02' in read_error

        elif cli_arg == '--cri':
            critical_log = writing_temp/'critical.log'
            read_critical = critical_log.read_text()
            assert '[2025-10-15 09:00:29] CRITICAL System instability detected — entering safe mode' in read_critical
