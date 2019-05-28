#!/bin/bash

hadoop fs -rm -r output/first_project_output/Job2_10M
mapred streaming \
	-D stream.num.map.output.key.fields=2 \
	-files ../mapperJob2.py,../reducerJob2.py,../historical_stocks.csv \
	-mapper mapperJob2.py \
	-reducer reducerJob2.py \
	-input input/first_project_input/historical_stock_prices_10M.csv \
	-output /user/shamri/output/first_project_output/Job2_10M
