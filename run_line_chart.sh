#!/bin/bash
echo "Running 1.dynamic_line_chart.py..."
python3 1.dynamic_line_chart.py True
sleep 1

echo "Reading excel file name..."
excelFileName=$(<excel_name.txt)
echo "Running make_video.py with $excelFileName..."
python3 make_video.py "$excelFileName" 60
sleep 1
