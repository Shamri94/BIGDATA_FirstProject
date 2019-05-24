#!/bin/bash

mapred streaming \
				-D stream.num.map.output.key.fields=3 \
				-files mapper1Job3.py,reducer1Job3.py,historical_stocks.csv \
				-mapper mapper1Job3.py \
				-reducer reducer1Job3.py \
				-input /user/shamri/input/first_project_input/historical_stock_prices.csv \
				-output /user/shamri/output/first_project_output/tmp/tmp_JOB3_Total \
&& 	\
mapred streaming \
				-D stream.num.map.output.key.fields=3 \
				-files mapper2Job3.py,reducer2Job3.py \
				-mapper mapper2Job3.py \
				-reducer reducer2Job3.py \
				-input /user/shamri/output/first_project_output/tmp/tmp_JOB3_Total/part-00000 \
				-output /user/shamri/output/first_project_output/JOB3_Total
