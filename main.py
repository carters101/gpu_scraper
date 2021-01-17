import scraper as sc
import table as tb
import mail as ml
import time
from pretty_html_table import build_table

while True:
    sc.update()
    dataframe = tb.create_table()

    # Creates HTML table in pretty format
    output_table = build_table(dataframe, 'blue_light')

    if tb.check_available(dataframe) != True:
        list_of_gpus = '\n\n'.join(tb.gpu_names)
        print("The following GPU's are in stock: " + list_of_gpus)
        ml.send_email(output_table)

    else:
        print("No GPU's meet your criteria. Trying again in 10 minutes.")
        time.sleep(600)
