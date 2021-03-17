import scraper as sc
import table as tb
import mail as ml
import time

while True:
    sc.update()
    dataframe = tb.create_table()

    # Checks table for GPUs meeting criteria and emails accordingly
    if tb.check_available(dataframe) == True:
        list_of_gpus = '\n\n'.join(tb.gpu_names)
        print("The following GPU's are in stock: " + list_of_gpus)
        ml.send_email(dataframe)
        break

    else:
        print("No GPU's meet your criteria. Trying again in 5 minutes.")
        print(dataframe)
        time.sleep(300)
