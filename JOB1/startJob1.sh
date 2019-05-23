#!/bin/bash

mapred streaming \
	-D stream.num.map.output.key.fields=2 \
	-files mapperJob1.py,reducerJob1.py \
	-mapper mapperJob1.py \
	-reducer reducerJob1.py \
	-input input/first_project_input/historical_stock_prices.csv \
	-output /user/shamri/output/first_project_output/JOB1_Total
