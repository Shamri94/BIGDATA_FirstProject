#!/bin/bash

hadoop fs -rm -r /user/output/Job2_10M
hadoop \
	jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.8.5-amzn-3.jar \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.job.reduces=1 \
	-input /user/input/historical_stock_prices_10M.csv \
	-output /user/output/Job2_10M \
	-file /home/hadoop/Job_2/historical_stocks.csv \
	-file /home/hadoop/Job_2/mapperJob2.py \
	-file /home/hadoop/Job_2/reducerJob2.py \
	-mapper mapperJob2.py \
	-reducer reducerJob2.py
