#!/bin/bash

mapred streaming \
				-D stream.num.map.output.key.fields=2 \
				-files mapperJob2.py,reducerJob2.py,historical_stocks.csv \
				-mapper mapperJob2.py \
				-reducer reducerJob2.py \
				-input input/first_project_input/historical_stock_prices.csv \
				-output output/first_project_output/JOB2_Total
