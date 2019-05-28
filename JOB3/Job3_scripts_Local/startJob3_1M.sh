#!/bin/bash

hadoop fs -rm -r output/first_project_output/tmp/tmp_Job3_1M
hadoop fs -rm -r output/first_project_output/Job3_1M
mapred streaming \
	-D stream.num.map.output.key.fields=3 \
	-files ../mapper1Job3.py,../reducer1Job3.py,../historical_stocks.csv \
	-mapper mapper1Job3.py \
	-reducer reducer1Job3.py \
	-input input/first_project_input/historical_stock_prices_1M.csv \
	-output output/first_project_output/tmp/tmp_Job3_1M \
&& \
mapred streaming \
	-D stream.num.map.output.key.fields=3 \
	-files ../mapper2Job3.py,../reducer2Job3.py \
	-mapper mapper2Job3.py \
	-reducer reducer2Job3.py \
	-input output/first_project_output/tmp/tmp_Job3_1M/part-00000 \
	-output output/first_project_output/Job3_1M
