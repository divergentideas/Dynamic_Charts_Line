import sys
sys.path.append('thebeautyofdata')
import thebeautyofdata
import json
from thebeautyofdata import DataHandler, Canvas, LineChart, StaticText
import argparse
import os
# Add argument parsing
parser = argparse.ArgumentParser(description="False not take image, True take image")
parser.add_argument("takeimmage", type=lambda x: (str(x).lower() == 'true'), help="True or False")
args = parser.parse_args()
takeimmage = args.takeimmage

width=1000
height=1000
# Define all constants
fps = 32
# Set duration based on the takeimmage value
Duration = 1 if takeimmage else 0.3

# load colors
with open('colors/colors_modify_line_chart.json') as f:
    colors = json.load(f)

events = {
    "Dot-com Bubble Burst": ["10/03/2000", "30/09/2001"],  # The collapse of the dot-com bubble affected stock markets significantly, with gold often acting as a safe haven.
    # "September 11 Attacks": ["11/09/2001", "11/09/2001"],  # These attacks had a significant immediate negative impact on stock markets, with investors turning to gold as a safe haven.
    "Global Financial Crisis": ["01/09/2008", "31/12/2009"],  # A major crisis that led to a drop in stock markets and a surge in gold prices as investors sought safety.
    "European Sovereign Debt Crisis": ["01/01/2010", "31/12/2012"],  # Economic instability in Europe affected global markets and increased gold's appeal.
    "US Federal Reserve's Quantitative Easing": ["01/12/2008", "29/10/2014"],  # The Fed's policy to stimulate the economy influenced both stock and gold markets.
    "Brexit Referendum": ["23/06/2016", "23/06/2016"],  # Uncertainty around the UK's decision to leave the EU impacted global markets and increased the appeal of gold.
    "US-China Trade War": ["01/01/2018", "15/01/2020"],  # Market volatility during the trade tensions affected both stock and gold prices.
    "COVID-19 Pandemic": ["01/03/2020", "01/12/2022"],  # The pande
# NOTE: the time format must be day/month/year
    }
# defining the canvas
canvas = Canvas.canvas()
line_width=5
point_radius=8
radius_limit_to_decrease_line_width=6
final_radius=4 # minimal radius
remove_point=1 # if remoe point =1 _delere point
size_of_legend=12
font_size=19
min_value_at_start=0
chose_max_of_y_axis=0 # =1 mean chose max
max_of_y_axis=0
move_chart_along_x=0
move_chart_along_y=0
speed_of_decrease_radius=0.01
##################################################################
File = "data/working-hours-per-worker-per-week.xlsx"
##################################################################
# Extract file name without extension
file_name_without_extension = os.path.splitext(os.path.basename(File))[0]
# Write the file name to a text file
with open("excel_name.txt", "w") as file:
    file.write(file_name_without_extension)

df = DataHandler.DataHandler(excel_file=File, number_of_frames=fps*Duration*60).df
# defining the line chart
line = LineChart.line_chart(canvas=canvas, df=df, colors=colors, events=events,line_width=line_width,point_radius=point_radius,
radius_limit_to_decrease_line_width=radius_limit_to_decrease_line_width,final_radius=final_radius,remove_point=remove_point,
size_of_legend=size_of_legend,min_value_at_start=min_value_at_start,chose_max_of_y_axis=chose_max_of_y_axis,
max_of_y_axis=max_of_y_axis,move_chart_along_x=move_chart_along_x,move_chart_along_y=move_chart_along_y,speed_of_decrease_radius=speed_of_decrease_radius,
                                                     unit="h",font_size=font_size,draw_points=True)
##################################################################
static_text = canvas.canvas.create_text(80, 120, text="Unit: hours/week",  anchor='w',font=("Purisa", 15),)
##################################################################
canvas.add_title("",font_size=22,color=(0, 0, 0))

canvas.add_sub_plot(line)
canvas.add_sub_title("",font_size=15)
canvas.add_time(time_indicator="month", df=df,font_size=15,x=900,y=100 )
x=15
move_text_along_x=-100
##################################################################
static_text = canvas.canvas.create_text(700+move_text_along_x-100, 40, text="Working hours per worker per week",  anchor='c',font=("Purisa", 22),) # Title
static_text = canvas.canvas.create_text(700+move_text_along_x-100, 90, text="Created by: Chi "
                                                                            "Research Data",
                                        anchor='c',font=("Purisa", 13),)   # sub-title
##################################################################
##################################################################
static_text = canvas.canvas.create_text(200+move_text_along_x, 970+x, text="Data source:Yahoo Finance",  anchor='w', font=("Purisa", 12)) # source of data
##################################################################
static_text = canvas.canvas.create_text(200+move_text_along_x, 1000+x, text="Software: tiktokchart.com",  anchor='w', font=("Purisa", 12))
static_text = canvas.canvas.create_text(200+move_text_along_x, 1030+x, text="",  anchor='w', font=("Purisa", 12))
# static_text = canvas.canvas.create_text(200+move_text_along_x, 1055+x, text="if subject to the current age specific mortality rates.",  anchor='w', font=("Purisa", 9))
canvas.play(fps=fps, save_image=takeimmage, x1=460, y1=0, x2=1460, y2=1080, location="images/export_all/")
