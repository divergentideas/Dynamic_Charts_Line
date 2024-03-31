@echo off
python 1.dynamic_line_chart.py True
timeout /t 1

set /p excelFileName=<excel_name.txt
python make_video.py %excelFileName% 60
timeout /t 1
