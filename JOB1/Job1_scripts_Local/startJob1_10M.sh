#!/bin/bash

hadoop fs -rm -r output/first_project_output/Job1_10M
mapred streaming \
	-D stream.num.map.output.key.fields=2 \
	-files ../mapperJob1.py,../reducerJob1.py \
	-mapper mapperJob1.py \
	-reducer reducerJob1.py \
	-input input/first_project_input/historical_stock_prices_10M.csv \
	-output /user/shamri/output/first_project_output/Job1_10M
